"""Smoke tests for the hand-written Python SDK.

No network. What these prove is the only thing the wrapper can get wrong on its
own: that the credential and scoping headers actually reach the request context,
that local validation rejects the common mistakes, and that a server error maps
onto the right disposition.

They also assert the PEP 420 namespace actually works — that ``o11y_one.sdk``
(this distribution) and ``o11y_one.agentic.v1`` (the generated one) coexist. That
is the single most fragile thing about the packaging here, so it is tested.
"""

from __future__ import annotations

import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest
from connectrpc.code import Code
from connectrpc.errors import ConnectError
from connectrpc.method import IdempotencyLevel, MethodInfo
from connectrpc.request import Headers, RequestContext
from o11y_one.sdk import (
    CREDENTIAL_HEADER,
    ORG_ID_HEADER,
    TENANT_ID_HEADER,
    CredentialInterceptor,
    Disposition,
    O11yClient,
    assert_looks_like_machine_credential,
    classify,
)

CREDENTIAL = "o11y_mach.AAAAAAAAAAAAAAAAAAAAAA.BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBA"


def test_generated_package_shares_the_namespace() -> None:
    """o11y-one-api-agentic and o11y-one both contribute to o11y_one.*."""
    from o11y_one.agentic.v1 import evaluation_pb2
    from o11y_one.agentic.v1.evaluation_connect import AgenticEvaluationServiceClientSync

    # And the proto package name — the thing the server routes on — survived the
    # import re-rooting described in tools/sync-proto.sh.
    assert evaluation_pb2.ListEvaluationDefinitionsRequest.DESCRIPTOR.full_name.startswith(
        "o11y_one.agentic.v1."
    )
    assert AgenticEvaluationServiceClientSync is not None


@pytest.mark.parametrize(
    ("value", "match"),
    [
        ("", "empty"),
        ("eyJhbGciOi.JWT.looking", "o11y_mach"),
        ("o11y_mach.onlytwo", "malformed"),
        ("o11y_mach." + "x" * 200, "over the"),
    ],
)
def test_credential_validation_rejects_common_mistakes(value: str, match: str) -> None:
    with pytest.raises(ValueError, match=match):
        assert_looks_like_machine_credential(value)


def test_credential_validation_strips_shell_quotes() -> None:
    assert assert_looks_like_machine_credential(f'"{CREDENTIAL}"') == CREDENTIAL
    assert assert_looks_like_machine_credential(f"  {CREDENTIAL}  ") == CREDENTIAL


def _ctx() -> RequestContext:
    return RequestContext(
        method=MethodInfo(
            name="ListEvaluationDefinitions",
            service_name="o11y_one.agentic.v1.AgenticEvaluationService",
            input=object,
            output=object,
            idempotency_level=IdempotencyLevel.UNKNOWN,
        ),
        http_method="POST",
        request_headers=Headers(),
    )


def test_interceptor_stamps_credential_and_scoping_headers() -> None:
    interceptor = CredentialInterceptor(
        credential=CREDENTIAL, org_id="org_123", tenant_id="tenant_456"
    )
    ctx = _ctx()
    seen: dict[str, str] = {}

    def call_next(request: object, ctx: RequestContext) -> str:
        seen.update(dict(ctx.request_headers()))
        return "ok"

    assert interceptor.intercept_unary_sync(call_next, object(), ctx) == "ok"
    assert seen[CREDENTIAL_HEADER] == CREDENTIAL
    assert seen[ORG_ID_HEADER] == "org_123"
    assert seen[TENANT_ID_HEADER] == "tenant_456"


def test_interceptor_without_credential_sends_no_auth_header() -> None:
    # Unauthenticated surfaces (capability discovery) must stay reachable.
    interceptor = CredentialInterceptor()
    ctx = _ctx()
    interceptor.intercept_unary_sync(lambda _req, _ctx: None, object(), ctx)
    assert CREDENTIAL_HEADER not in ctx.request_headers()


def test_client_speaks_uncompressed_grpc_web() -> None:
    """The API serves gRPC and gRPC-web, not the Connect protocol, and the
    agentic service accepts no request compression."""
    from o11y_one.agentic.v1.evaluation_connect import AgenticEvaluationServiceClientSync
    from o11y_one.agentic.v1.evaluation_pb2 import ListEvaluationDefinitionsRequest

    seen: dict[str, object] = {}

    class Handler(BaseHTTPRequestHandler):
        def do_POST(self) -> None:
            seen["path"] = self.path
            seen["headers"] = self.headers
            # A gRPC-web trailers-only error: no body to hand-encode.
            self.send_response(200)
            self.send_header("content-type", "application/grpc-web+proto")
            self.send_header("grpc-status", "7")
            self.send_header("grpc-message", "missing%20scope%20eval%3Aread")
            self.send_header("content-length", "0")
            self.end_headers()

    with HTTPServer(("127.0.0.1", 0), Handler) as server:
        threading.Thread(target=server.handle_request, daemon=True).start()
        o11y = O11yClient(
            base_url=f"http://127.0.0.1:{server.server_port}",
            credential=CREDENTIAL,
            timeout_ms=5_000,
        )
        evals = o11y.service_sync(AgenticEvaluationServiceClientSync)
        with pytest.raises(ConnectError) as exc:
            evals.list_evaluation_definitions(ListEvaluationDefinitionsRequest())

    headers = seen["headers"]
    assert seen["path"] == "/o11y_one.agentic.v1.AgenticEvaluationService/ListEvaluationDefinitions"
    assert headers["content-type"] == "application/grpc-web+proto"
    # tonic answers UNIMPLEMENTED to any grpc-encoding a service did not enable.
    assert headers.get("grpc-encoding", "identity") == "identity"
    assert headers[CREDENTIAL_HEADER] == CREDENTIAL
    assert classify(exc.value).missing_scope == "eval:read"


def test_error_taxonomy_does_not_collapse_auth_failures() -> None:
    unauth = classify(ConnectError(Code.UNAUTHENTICATED, "credential revoked"))
    assert unauth.disposition is Disposition.REAUTHENTICATE
    assert unauth.retryable is False

    denied = classify(ConnectError(Code.PERMISSION_DENIED, "principal lacks scope eval:read"))
    assert denied.disposition is Disposition.INSUFFICIENT_SCOPE
    assert denied.missing_scope == "eval:read"

    down = classify(ConnectError(Code.UNAVAILABLE, "auth backend down"))
    assert down.disposition is Disposition.RETRY_WITH_BACKOFF
    assert down.retryable is True

    skew = classify(ConnectError(Code.INVALID_ARGUMENT, "unknown scope discriminant 9"))
    assert skew.disposition is Disposition.VERSION_SKEW

    # A DNS failure is not an auth failure.
    other = classify(OSError("name resolution failed"))
    assert other.disposition is Disposition.UNCLASSIFIED
    assert other.code is None
