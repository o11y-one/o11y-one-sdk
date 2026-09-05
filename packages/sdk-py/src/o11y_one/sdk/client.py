"""Transport construction and credential injection.

Scope discipline: this module builds clients and attaches headers. It does NOT
wrap RPCs in convenience methods. ``o11y-one-api`` already ships a
``*ServiceClient`` for every service; a hand-written facade over 29 of them would
be a second API surface to keep in sync with the proto, and it would rot the
first time a field is added upstream.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import Any, TypeVar

from connectrpc.client import ConnectClient, ConnectClientSync
from connectrpc.interceptor import Interceptor, InterceptorSync
from connectrpc.request import RequestContext

from .auth import (
    CREDENTIAL_HEADER,
    ORG_ID_HEADER,
    TENANT_ID_HEADER,
    assert_looks_like_machine_credential,
)

__all__ = ["CredentialInterceptor", "O11yClient"]

_REQ = TypeVar("_REQ")
_RES = TypeVar("_RES")
_SyncClientT = TypeVar("_SyncClientT", bound=ConnectClientSync)
_AsyncClientT = TypeVar("_AsyncClientT", bound=ConnectClient)


class CredentialInterceptor:
    """Stamps the credential and scoping headers onto every outbound request.

    This is THE auth-injection point for the Python SDK. Everything about the
    shape it injects is settled (see :mod:`o11y_one.sdk.auth`). What is NOT
    settled, and is the one open dependency this package has on the backend:

    TODO(w50a-auth-shape / lane 50A): the machine-principal management surface --
        ``CreateMachinePrincipal``, ``ListMachinePrincipals``,
        ``CreateMachineCredential``, ``RevokeMachineCredential``,
        ``RevokeMachinePrincipal``, ``GetCallerPrincipal`` -- does not exist in
        the proto snapshot at PROTO_PIN (fb8f5098). ``auth.proto`` there carries
        only ``AuthFoundationService.ListAuthMethods``. The RPC NAMES are held by
        50A and will not move, so when lane A lands them:

          1. bump PROTO_PIN and run ``tools/sync-proto.sh``;
          2. add ``O11yClient.whoami()`` over ``GetCallerPrincipal`` -- the
             introspection call that answers "is my credential valid, and which
             scopes does it carry?" BEFORE a run. That is what makes
             ``o11y-eval doctor`` possible, and what turns an UNAUTHENTICATED at
             minute 40 into an error at minute 0.

        Nothing else in this module changes: the header, the encoding, and the
        error taxonomy are already the final ones.

    Implements both the sync and async unary interceptor protocols, which
    connect-python matches structurally (``runtime_checkable`` Protocols), so one
    object serves ``ConnectClient`` and ``ConnectClientSync`` alike.
    """

    __slots__ = ("_headers",)

    def __init__(
        self,
        *,
        credential: str | None = None,
        org_id: str | None = None,
        tenant_id: str | None = None,
    ) -> None:
        headers: dict[str, str] = {}
        if credential is not None:
            headers[CREDENTIAL_HEADER] = assert_looks_like_machine_credential(credential)
        if org_id is not None:
            headers[ORG_ID_HEADER] = org_id
        if tenant_id is not None:
            headers[TENANT_ID_HEADER] = tenant_id
        self._headers = headers

    def _apply(self, ctx: RequestContext) -> None:
        request_headers = ctx.request_headers()
        for key, value in self._headers.items():
            request_headers[key] = value

    def intercept_unary_sync(
        self,
        call_next: Callable[[_REQ, RequestContext], _RES],
        request: _REQ,
        ctx: RequestContext,
    ) -> _RES:
        self._apply(ctx)
        return call_next(request, ctx)

    async def intercept_unary(
        self,
        call_next: Callable[[_REQ, RequestContext], Any],
        request: _REQ,
        ctx: RequestContext,
    ) -> Any:
        self._apply(ctx)
        return await call_next(request, ctx)


class O11yClient:
    """Holds connection settings so callers construct credentials once and mint
    typed service clients per service.

    ::

        from o11y_one.sdk import O11yClient
        from o11y_one.billing.v1.billing_connect import BillingUsageServiceClient

        o11y = O11yClient(base_url="https://api.o11y.one", credential=os.environ["O11Y_API_KEY"])
        billing = o11y.service_sync(BillingUsageServiceClient)
        quota = billing.get_quota_status(GetQuotaStatusRequest())

    Protocol note: Connect over HTTP, not gRPC. It is the protocol o11y-web
    already speaks and the one that survives proxies and CI egress rules without
    HTTP/2 prior knowledge.
    """

    __slots__ = ("_base_url", "_interceptor", "_extra_interceptors", "_timeout_ms")

    def __init__(
        self,
        *,
        base_url: str,
        credential: str | None = None,
        org_id: str | None = None,
        tenant_id: str | None = None,
        timeout_ms: int | None = None,
        interceptors: Iterable[Interceptor | InterceptorSync] = (),
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._interceptor = CredentialInterceptor(
            credential=credential, org_id=org_id, tenant_id=tenant_id
        )
        self._extra_interceptors = tuple(interceptors)
        self._timeout_ms = timeout_ms

    @property
    def interceptor(self) -> CredentialInterceptor:
        """The credential interceptor, exposed so callers who construct a
        generated client themselves can install the same header discipline."""
        return self._interceptor

    def _kwargs(self) -> dict[str, Any]:
        return {
            "interceptors": (self._interceptor, *self._extra_interceptors),
            "timeout_ms": self._timeout_ms,
        }

    def service_sync(self, client_cls: type[_SyncClientT]) -> _SyncClientT:
        """Mint a synchronous client from a generated ``*ServiceClientSync`` class."""
        return client_cls(self._base_url, **self._kwargs())

    def service(self, client_cls: type[_AsyncClientT]) -> _AsyncClientT:
        """Mint an asynchronous client from a generated ``*ServiceClient`` class."""
        return client_cls(self._base_url, **self._kwargs())
