"""A fake Loop for the trainer adapters' tests: the generated LoopRolloutService WSGI app,
served on 127.0.0.1 over gRPC-web as the SDK speaks it. It records every request
and the key it came with, can hold a verb's calls to count how many are in
flight at once, and answers each close with the rewards a test scripts.

Every Python socket this process connects is recorded too, so a test can prove
nothing but the SDK's transport talks to the network.
"""

from __future__ import annotations

import contextlib
import io
import socket
import sys
import threading
import time
from collections import Counter
from socketserver import ThreadingMixIn
from wsgiref.simple_server import WSGIRequestHandler, WSGIServer

from connectrpc.code import Code
from connectrpc.errors import ConnectError
from o11y_one.agentic.v1.rollout_connect import (
    LoopRolloutServiceSync,
)
from o11y_one.agentic.v1.rollout_pb2 import (
    CloseLoopRolloutResponse,
    LoopRewardV1,
    LoopRolloutFailureV1,
    LoopRolloutRejectionV1,
    LoopRolloutV1,
    LoopToolResultV1,
    ResetLoopRolloutResponse,
    StepLoopRolloutResponse,
)

# Obvious fakes.
CREDENTIAL = "o11y_mach.AAAAAAAAAAAAAAAAAAAAAA.BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBA"
RUN = "trn_06AZ3XN1YQF4KD2M8RP7TV5W9C"

CONNECTS: list[object] = []


def _audit(event: str, args: tuple) -> None:
    if event == "socket.connect" and args[0].family in (socket.AF_INET, socket.AF_INET6):
        CONNECTS.append(args[1][:2])


sys.addaudithook(_audit)


def refusal(reason: str) -> ConnectError:
    detail = LoopRolloutRejectionV1(reason_code=reason, limit=8)
    return ConnectError(Code.RESOURCE_EXHAUSTED, reason.replace("_", " "), details=[detail])


class FakeLoop(LoopRolloutServiceSync):
    def __init__(self) -> None:
        self.lock = threading.Lock()
        self.requests: list[tuple[str, object]] = []
        self.keys: set[str] = set()
        self.in_flight: Counter[str] = Counter()
        self.held: dict[str, threading.Event] = {}
        self.refusals: dict[str, list[ConnectError]] = {}
        # rollout id -> (failure class, rewards) for its close; else tests_passed = its number / 10.
        self.closes: dict[str, tuple[int, list[tuple[str, float]]]] = {}
        self.url = ""

    def hold(self, verb: str) -> threading.Event:
        self.held[verb] = threading.Event()
        return self.held[verb]

    def wait_in_flight(self, verb: str, count: int) -> None:
        deadline = time.monotonic() + 10
        while self.in_flight[verb] < count:
            assert time.monotonic() < deadline, f"{self.in_flight[verb]} {verb}s in flight"
            time.sleep(0.005)

    def sent(self, verb: str) -> list:
        return [request for name, request in self.requests if name == verb]

    @contextlib.contextmanager
    def _call(self, verb: str, request: object, ctx: object):
        with self.lock:
            self.requests.append((verb, request))
            self.keys.add(ctx.request_headers().get("x-o11y-key", ""))
            self.in_flight[verb] += 1
            number = len(self.sent(verb))
            refused = self.refusals.get(verb)
            error = refused.pop(0) if refused else None
        try:
            if verb in self.held:
                assert self.held[verb].wait(10), f"{verb} held past 10 s"
            if error is not None:
                raise error
            yield number
        finally:
            with self.lock:
                self.in_flight[verb] -= 1

    def reset_loop_rollout(self, request, ctx):
        with self._call("reset", request, ctx) as number:
            return ResetLoopRolloutResponse(rollout=LoopRolloutV1(rollout_id=f"r-{number}"))

    def step_loop_rollout(self, request, ctx):
        with self._call("step", request, ctx):
            results = [
                LoopToolResultV1(exit_code=0, stdout=f"ran {call.WhichOneof('call')}".encode())
                for call in request.calls
            ]
            return StepLoopRolloutResponse(step=1, results=results)

    def close_loop_rollout(self, request, ctx):
        with self._call("close", request, ctx):
            number = int(request.rollout_id.removeprefix("r-"))
            failure_class, rewards = self.closes.get(
                request.rollout_id, (0, [("tests_passed", number / 10), ("all_passed", 0.0)])
            )
            failure = (
                LoopRolloutFailureV1(failure_class=failure_class, code="x")
                if failure_class
                else None
            )
            rollout = LoopRolloutV1(
                rollout_id=request.rollout_id,
                failure=failure,
                rewards=[LoopRewardV1(name=name, value=value) for name, value in rewards],
            )
            return CloseLoopRolloutResponse(rollout=rollout)


def _unchunked(app):
    """wsgiref hands the app the raw socket, and the SDK's gRPC-web requests are chunked."""

    def bounded(environ, start_response):
        raw, body = environ["wsgi.input"], bytearray()
        if environ.get("HTTP_TRANSFER_ENCODING") == "chunked":
            while size := int(raw.readline().split(b";")[0], 16):
                body += raw.read(size)
                raw.readline()
            raw.readline()
        else:
            body += raw.read(int(environ.get("CONTENT_LENGTH") or 0))
        environ["wsgi.input"] = io.BytesIO(bytes(body))
        return app(environ, start_response)

    return bounded


class _Server(ThreadingMixIn, WSGIServer):
    daemon_threads = True


class _Quiet(WSGIRequestHandler):
    def log_message(self, *args: object) -> None:
        pass
