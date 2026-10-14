"""The Loop rollout client against the statuses the server sends.

Each refusal below is the server's own (``loop_rollout.rs``'s ``refusal``): its
gRPC code, its sentence and its ``LoopRolloutRejectionV1``. A fake service
stands in for the generated client, and a fake clock for ``time``, so no test
sleeps. One test goes over a real gRPC-web socket, to prove the key reaches the
wire and never a log, repr or message.
"""

from __future__ import annotations

import asyncio
import base64
import copy
import importlib.util
import inspect
import logging
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest
from connectrpc.code import Code
from connectrpc.errors import ConnectError
from google.protobuf import any_pb2
from o11y_one.agentic.v1.rollout_pb2 import (
    CloseLoopRolloutResponse,
    ForkLoopRolloutResponse,
    LoopRolloutRejectionV1,
    LoopRolloutV1,
    LoopToolCallV1,
    LoopToolExecV1,
    ResetLoopRolloutResponse,
    StepLoopRolloutResponse,
)
from o11y_one.sdk import CREDENTIAL_HEADER, Disposition, classify, loop
from o11y_one.sdk.loop import AsyncLoopClient, LoopClient, RolloutRefused

CREDENTIAL = "o11y_mach.AAAAAAAAAAAAAAAAAAAAAA.BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBA"
RUN = "trn_06AZ3XN1YQF4KD2M8RP7TV5W9C"

# (reason code, gRPC code, the server's sentence), as loop_rollout.rs sends them.
RECORDED = [
    ("run_paused", Code.UNAVAILABLE, "the run is paused; resets wait until it resumes"),
    (
        "plan_concurrency_reached",
        Code.RESOURCE_EXHAUSTED,
        "the organization has as many environments open as its plan allows",
    ),
    (
        "run_concurrency_reached",
        Code.RESOURCE_EXHAUSTED,
        "the run has as many environments open as it allows",
    ),
    ("run_stopped", Code.FAILED_PRECONDITION, "the run was stopped, so it starts no rollout"),
    (
        "run_spend_cap_reached",
        Code.RESOURCE_EXHAUSTED,
        "the run's spend cap is reached; raise it to go on",
    ),
    (
        "rate_limited",
        Code.RESOURCE_EXHAUSTED,
        "resets are arriving faster than the run's environments allow",
    ),
    (
        "capacity_unavailable",
        Code.UNAVAILABLE,
        "no environment came up within the reset's wait; not billed",
    ),
    ("step_in_progress", Code.FAILED_PRECONDITION, "the rollout runs one step at a time"),
    (
        "loop_rollouts_unavailable",
        Code.FAILED_PRECONDITION,
        "capability `loop_rollouts` is not available",
    ),
]


def refusal(
    reason: str, *, retry_after_ms: int | None = None, limit: int | None = None
) -> ConnectError:
    code, message = next((c, m) for r, c, m in RECORDED if r == reason)
    detail = LoopRolloutRejectionV1(
        reason_code=reason, retry_after_millis=retry_after_ms, limit=limit
    )
    return ConnectError(code, message, details=[detail])


def rollout(rollout_id: str) -> LoopRolloutV1:
    return LoopRolloutV1(rollout_id=rollout_id, run_id=RUN)


class FakeService:
    """Answers each generated method from its own queue, in order, and records every request."""

    def __init__(self, **answers: list[object]) -> None:
        self.answers = answers
        self.calls: list[tuple[str, object]] = []

    def __getattr__(self, method: str):
        def call(request: object) -> object:
            self.calls.append((method, copy.deepcopy(request)))
            answer = self.answers[method].pop(0)
            if isinstance(answer, BaseException):
                raise answer
            return answer

        return call


class FakeClock:
    def __init__(self) -> None:
        self.now = 0.0
        self.slept: list[float] = []

    def monotonic(self) -> float:
        return self.now

    def sleep(self, seconds: float) -> None:
        self.slept.append(seconds)
        self.now += seconds

    async def asleep(self, seconds: float) -> None:
        self.sleep(seconds)


@pytest.fixture
def clock(monkeypatch: pytest.MonkeyPatch) -> FakeClock:
    fake = FakeClock()
    monkeypatch.setattr(loop, "time", fake)
    monkeypatch.setattr(loop.asyncio, "sleep", fake.asleep)
    return fake


class AsyncService:
    """A FakeService's answers, awaited, as the generated async client gives them."""

    def __init__(self, service: FakeService) -> None:
        self.service = service

    def __getattr__(self, method: str):
        call = getattr(self.service, method)

        async def awaited(request: object) -> object:
            return call(request)

        return awaited


@pytest.fixture(params=[LoopClient, AsyncLoopClient], ids=["sync", "async"])
def kind(request: pytest.FixtureRequest) -> type:
    return request.param


def client_with(service: FakeService, rollout_id: str | None = None, kind: type = LoopClient):
    client = kind(run=RUN, credential=CREDENTIAL)
    client._service = service if kind is LoopClient else AsyncService(service)
    client._open = rollout_id
    return client


def drive(client, verb: str, *args, **kwargs):
    """``client.verb(...)``, awaited when the client is async."""
    answer = getattr(client, verb)(*args, **kwargs)
    return asyncio.run(answer) if inspect.iscoroutine(answer) else answer


def test_the_loop_package_keeps_every_import_the_loop_module_had() -> None:
    from o11y_one.sdk.loop import LoopClient, RolloutRefused

    assert {LoopClient.__module__, RolloutRefused.__module__} == {"o11y_one.sdk.loop"}
    if importlib.util.find_spec("openenv") is None:
        with pytest.raises(ImportError, match=r"o11y-one\[openenv\]"):
            from o11y_one.sdk.loop import LoopEnvClient
    else:
        from o11y_one.sdk.loop import LoopEnvClient
        from openenv.core.generic_client import GenericEnvClient

        assert issubclass(LoopEnvClient, GenericEnvClient)


@pytest.mark.skipif(importlib.util.find_spec("trl") is not None, reason="the trl extra is here")
def test_the_trl_adapter_without_its_extra_says_which_to_install() -> None:
    with pytest.raises(ImportError, match=r"o11y-one\[trl\]"):
        import o11y_one.sdk.loop.trl  # noqa: F401


@pytest.mark.parametrize(("reason", "code", "message"), RECORDED)
def test_each_recorded_refusal_raises_its_stable_code(
    kind: type, reason: str, code: Code, message: str
) -> None:
    sent = refusal(reason, retry_after_ms=1_500, limit=8)
    client = client_with(FakeService(step_loop_rollout=[sent]), "r-1", kind)
    with pytest.raises(RolloutRefused) as refused:
        drive(client, "step", [])
    assert (refused.value.code, refused.value.retry_after_ms) == (reason, 1_500)
    assert str(refused.value) == f"{reason}: {message}"
    assert refused.value.__cause__ is sent


def test_a_refusal_without_a_retry_after_says_none(kind: type) -> None:
    service = FakeService(step_loop_rollout=[refusal("step_in_progress")])
    with pytest.raises(RolloutRefused) as refused:
        drive(client_with(service, "r-1", kind), "step", [])
    assert refused.value.retry_after_ms is None


def test_a_status_without_a_rollout_refusal_is_raised_as_the_server_sent_it(kind: type) -> None:
    unknown = ConnectError(Code.NOT_FOUND, "no rollout in this organization has that id")
    revoked = ConnectError(Code.UNAUTHENTICATED, "Authentication failed")
    client = client_with(FakeService(step_loop_rollout=[unknown, revoked]), "r-1", kind)
    with pytest.raises(ConnectError) as raised:
        drive(client, "step", [])
    assert raised.value is unknown
    with pytest.raises(ConnectError) as raised:
        drive(client, "step", [])
    assert raised.value is revoked
    assert classify(raised.value).disposition is Disposition.REAUTHENTICATE


def test_plan_concurrency_reached_raises_at_once(kind: type, clock: FakeClock) -> None:
    service = FakeService(reset_loop_rollout=[refusal("plan_concurrency_reached", limit=200)])
    with pytest.raises(RolloutRefused) as refused:
        drive(client_with(service, kind=kind), "reset")
    assert refused.value.code == "plan_concurrency_reached"
    assert len(service.calls) == 1
    assert clock.slept == []


def test_a_paused_run_is_retried_after_each_retry_after_under_one_request_id(
    kind: type, clock: FakeClock
) -> None:
    paused = [refusal("run_paused", retry_after_ms=60_000) for _ in range(3)]
    service = FakeService(
        reset_loop_rollout=[*paused, ResetLoopRolloutResponse(rollout=rollout("r-1"))]
    )
    client = client_with(service, kind=kind)
    assert drive(client, "reset", group_size=4).rollout_id == "r-1"
    assert clock.slept == [60.0, 60.0, 60.0]
    requests = [request for _, request in service.calls]
    assert len({request.request_id for request in requests}) == 1
    assert {(request.run_id, request.group_size) for request in requests} == {(RUN, 4)}
    assert client.rollout_id == "r-1"


def test_a_paused_run_is_retried_for_30_minutes_then_raised(kind: type, clock: FakeClock) -> None:
    paused = [refusal("run_paused", retry_after_ms=60_000) for _ in range(40)]
    service = FakeService(reset_loop_rollout=paused)
    with pytest.raises(RolloutRefused) as refused:
        drive(client_with(service, kind=kind), "reset")
    assert refused.value.code == "run_paused"
    assert clock.slept == [60.0] * 30
    assert len(service.calls) == 31


def test_a_paused_run_without_a_retry_after_waits_the_default(kind: type, clock: FakeClock) -> None:
    paused = [refusal("run_paused") for _ in range(400)]
    with pytest.raises(RolloutRefused):
        drive(client_with(FakeService(reset_loop_rollout=paused), kind=kind), "reset")
    assert set(clock.slept) == {loop.RUN_PAUSED_WAIT_S}
    assert sum(clock.slept) <= loop.RUN_PAUSED_RETRY_S


def test_reset_closes_the_open_rollout_before_the_next_reset(kind: type) -> None:
    service = FakeService(
        reset_loop_rollout=[
            ResetLoopRolloutResponse(rollout=rollout("r-1")),
            ResetLoopRolloutResponse(rollout=rollout("r-2")),
        ],
        close_loop_rollout=[
            CloseLoopRolloutResponse(rollout=rollout("r-1"), pending=True),
            CloseLoopRolloutResponse(rollout=rollout("r-1")),
        ],
    )
    client = client_with(service, kind=kind)
    drive(client, "reset")
    drive(client, "reset")
    sent = [(method, getattr(request, "rollout_id", "")) for method, request in service.calls]
    assert sent == [
        ("reset_loop_rollout", ""),
        ("close_loop_rollout", "r-1"),
        ("close_loop_rollout", "r-1"),
        ("reset_loop_rollout", ""),
    ]
    assert client.rollout_id == "r-2"


def test_close_answers_the_rewarded_rollout_and_leaves_none_open(kind: type) -> None:
    service = FakeService(close_loop_rollout=[CloseLoopRolloutResponse(rollout=rollout("r-1"))])
    client = client_with(service, "r-1", kind)
    assert drive(client, "close").rollout_id == "r-1"
    assert client.rollout_id is None
    assert drive(client, "close") is None
    assert len(service.calls) == 1


def test_step_sends_the_calls_and_model_message_on_the_open_rollout(kind: type) -> None:
    service = FakeService(step_loop_rollout=[StepLoopRolloutResponse(step=1)])
    client = client_with(service, "r-1", kind)
    call = LoopToolCallV1(timeout_millis=1_000, exec=LoopToolExecV1(argv=["true"]))
    assert drive(client, "step", [call], model_message='{"role":"assistant"}').step == 1
    ((_, request),) = service.calls
    assert (request.rollout_id, list(request.calls), request.model_message_json) == (
        "r-1",
        [call],
        '{"role":"assistant"}',
    )


def test_step_without_an_open_rollout_is_refused_locally(kind: type) -> None:
    with pytest.raises(RuntimeError, match="reset"):
        drive(client_with(FakeService(), kind=kind), "step", [])


def test_concurrent_steps_on_one_async_client_reach_loop_one_at_a_time() -> None:
    seen = {"in_flight": 0, "most": 0}

    class Slow:
        async def step_loop_rollout(self, request: object) -> StepLoopRolloutResponse:
            seen["in_flight"] += 1
            seen["most"] = max(seen["most"], seen["in_flight"])
            await asyncio.sleep(0.01)
            seen["in_flight"] -= 1
            return StepLoopRolloutResponse(step=1)

    client = AsyncLoopClient(run=RUN, credential=CREDENTIAL)
    client._service, client._open = Slow(), "r-1"

    async def at_once() -> list:
        return await asyncio.gather(*(client.step([]) for _ in range(4)))

    assert len(asyncio.run(at_once())) == 4
    assert seen["most"] == 1


def test_fork_answers_a_client_per_copy_the_rollout_itself_first() -> None:
    service = FakeService(
        fork_loop_rollout=[ForkLoopRolloutResponse(rollouts=[rollout("r-1"), rollout("r-2")])],
        step_loop_rollout=[StepLoopRolloutResponse(step=4)],
    )
    client = client_with(service, "r-1")
    forks = client.fork(2)
    assert forks[0] is client
    assert [fork.rollout_id for fork in forks] == ["r-1", "r-2"]
    forks[1].step([])
    (_, fork_request), (_, step_request) = service.calls
    assert (fork_request.rollout_id, fork_request.copies) == ("r-1", 2)
    assert step_request.rollout_id == "r-2"
    assert client.rollout_id == "r-1"


def test_run_and_credential_fall_back_to_the_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("O11Y_API_KEY", CREDENTIAL)
    monkeypatch.setenv("O11Y_RUN", RUN)
    service = FakeService(reset_loop_rollout=[ResetLoopRolloutResponse(rollout=rollout("r-1"))])
    client = LoopClient()
    client._service = service
    client.reset()
    assert service.calls[0][1].run_id == RUN


def test_a_reset_names_the_adapter_and_framework_the_client_was_made_with() -> None:
    service = FakeService(reset_loop_rollout=[ResetLoopRolloutResponse(rollout=rollout("r-1"))])
    client = LoopClient(
        run=RUN,
        credential=CREDENTIAL,
        adapter="o11y_one.sdk.loop.trl",
        adapter_version="0.3.0",
        framework_version="1.15.0",
    )
    client._service = service
    client.reset()
    sent = service.calls[0][1].client
    assert (sent.adapter, sent.adapter_version, sent.framework_version) == (
        "o11y_one.sdk.loop.trl",
        "0.3.0",
        "1.15.0",
    )
    assert (sent.sdk_version, sent.session_id) == (loop._SDK_VERSION, loop._SESSION_ID)


def test_a_missing_run_or_credential_is_refused_locally(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("O11Y_API_KEY", raising=False)
    monkeypatch.delenv("O11Y_RUN", raising=False)
    with pytest.raises(ValueError, match="O11Y_RUN"):
        LoopClient(credential=CREDENTIAL)
    with pytest.raises(ValueError, match="empty"):
        LoopClient(run=RUN)


def _status_details(code: Code, message: str, detail: LoopRolloutRejectionV1) -> str:
    """``grpc-status-details-bin`` as tonic sends it: a ``google.rpc.Status``, base64."""

    def varint(value: int) -> bytes:
        out = bytearray()
        while value > 0x7F:
            out.append(value & 0x7F | 0x80)
            value >>= 7
        return bytes([*out, value])

    def field(number: int, payload: bytes) -> bytes:
        return varint(number << 3 | 2) + varint(len(payload)) + payload

    packed = any_pb2.Any()
    packed.Pack(detail)
    grpc_code = {Code.RESOURCE_EXHAUSTED: 8}[code]
    status = (
        b"\x08"
        + varint(grpc_code)
        + field(2, message.encode())
        + field(3, packed.SerializeToString())
    )
    return base64.b64encode(status).decode()


def test_the_key_reaches_the_wire_and_never_a_log_repr_or_message(
    kind: type, monkeypatch: pytest.MonkeyPatch, caplog: pytest.LogCaptureFixture
) -> None:
    seen: dict[str, object] = {}
    reason, code, message = RECORDED[1]
    detail = LoopRolloutRejectionV1(reason_code=reason, limit=200)

    class Handler(BaseHTTPRequestHandler):
        def do_POST(self) -> None:
            seen["path"] = self.path
            seen["key"] = self.headers[CREDENTIAL_HEADER]
            self.send_response(200)
            self.send_header("content-type", "application/grpc-web+proto")
            self.send_header("grpc-status", "8")
            self.send_header("grpc-message", message.replace(" ", "%20"))
            self.send_header("grpc-status-details-bin", _status_details(code, message, detail))
            self.send_header("content-length", "0")
            self.end_headers()

    monkeypatch.setenv("O11Y_API_KEY", CREDENTIAL)
    caplog.set_level(logging.DEBUG)
    with HTTPServer(("127.0.0.1", 0), Handler) as server:
        threading.Thread(target=server.handle_request, daemon=True).start()
        client = kind(run=RUN, base_url=f"http://127.0.0.1:{server.server_port}")
        with pytest.raises(RolloutRefused) as refused:
            drive(client, "reset")

    assert seen == {
        "path": "/o11y_one.agentic.v1.LoopRolloutService/ResetLoopRollout",
        "key": CREDENTIAL,
    }
    assert (refused.value.code, refused.value.retry_after_ms) == (reason, None)
    shown = [repr(client), str(client), repr(refused.value), str(refused.value), caplog.text]
    assert not [text for text in shown if CREDENTIAL in text or "BBBBBBBB" in text]


def test_a_reset_is_answered_over_the_wire(kind: type) -> None:
    answer = ResetLoopRolloutResponse(rollout=rollout("r-1")).SerializeToString()
    trailer = b"grpc-status: 0\r\n"

    class Handler(BaseHTTPRequestHandler):
        def do_POST(self) -> None:
            self.rfile.read(int(self.headers.get("content-length") or 0))
            body = (
                b"\x00"
                + len(answer).to_bytes(4, "big")
                + answer
                + b"\x80"
                + len(trailer).to_bytes(4, "big")
                + trailer
            )
            self.send_response(200)
            self.send_header("content-type", "application/grpc-web+proto")
            self.send_header("content-length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    with HTTPServer(("127.0.0.1", 0), Handler) as server:
        threading.Thread(target=server.handle_request, daemon=True).start()
        client = kind(
            run=RUN, credential=CREDENTIAL, base_url=f"http://127.0.0.1:{server.server_port}"
        )
        assert drive(client, "reset").rollout_id == "r-1"
    assert client.rollout_id == "r-1"
