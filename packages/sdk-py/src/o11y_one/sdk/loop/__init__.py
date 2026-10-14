"""The Loop rollout client a trainer drives.

A person mints a run in the web and hands the trainer its id (``O11Y_RUN``, not
a secret) and an organization's machine key with the ``rollout:drive`` scope
(``O11Y_API_KEY``). :class:`LoopClient` resets, steps, closes and forks that
run's rollouts over ``LoopRolloutService``, one open rollout at a time;
:class:`AsyncLoopClient` does the same for an asyncio trainer.

``LoopEnvClient``, OpenEnv's own client with the key on its WebSocket upgrade,
needs the ``openenv`` extra: ``pip install 'o11y-one[openenv]'``.
"""

from __future__ import annotations

import asyncio
import copy
import os
import time
import uuid
from collections.abc import Awaitable, Callable, Iterable
from importlib.metadata import version
from typing import Any, TypeVar

from connectrpc.errors import ConnectError
from o11y_one.agentic.v1.rollout_connect import (
    LoopRolloutServiceClient,
    LoopRolloutServiceClientSync,
)
from o11y_one.agentic.v1.rollout_pb2 import (
    CloseLoopRolloutRequest,
    ForkLoopRolloutRequest,
    LoopClientV1,
    LoopRolloutRejectionV1,
    LoopRolloutV1,
    LoopToolCallV1,
    ResetLoopRolloutRequest,
    StepLoopRolloutRequest,
    StepLoopRolloutResponse,
)

from ..client import O11yClient
from ..recovery import find_error_detail

__all__ = ["DEFAULT_BASE_URL", "AsyncLoopClient", "LoopClient", "RolloutRefused"]

DEFAULT_BASE_URL = "https://grpc.o11y.one"
#: How long a reset retries a paused run before it raises ``run_paused``.
RUN_PAUSED_RETRY_S = 30 * 60
#: The wait between those retries when the refusal names none.
RUN_PAUSED_WAIT_S = 5.0

_SDK_VERSION = version("o11y-one")
#: Random per trainer process: a new one on a run reads as a reconnect.
_SESSION_ID = str(uuid.uuid4())

_RES = TypeVar("_RES")


class RolloutRefused(Exception):
    """A ``LoopRolloutService`` refusal: its stable ``code``, e.g.
    ``plan_concurrency_reached``, and when a retry may be admitted, when the
    server said."""

    def __init__(self, code: str, retry_after_ms: int | None, message: str = "") -> None:
        super().__init__(f"{code}: {message}" if message else code)
        self.code = code
        self.retry_after_ms = retry_after_ms


def _call(method: Callable[[Any], _RES], request: object) -> _RES:
    """One RPC. A status carrying ``LoopRolloutRejectionV1`` raises
    :class:`RolloutRefused`; any other, e.g. ``UNAUTHENTICATED`` (which
    :func:`~o11y_one.sdk.errors.classify` reads as ``REAUTHENTICATE``), is
    raised as the server sent it."""
    try:
        return method(request)
    except ConnectError as error:
        _raise_refused(error)
        raise


async def _acall(method: Callable[[Any], Awaitable[_RES]], request: object) -> _RES:
    """:func:`_call`, awaited."""
    try:
        return await method(request)
    except ConnectError as error:
        _raise_refused(error)
        raise


def _raise_refused(error: ConnectError) -> None:
    detail = find_error_detail(error, LoopRolloutRejectionV1)
    if detail is not None:
        retry = detail.retry_after_millis if detail.HasField("retry_after_millis") else None
        raise RolloutRefused(detail.reason_code, retry, error.message) from error


def _paused_wait(refused: RolloutRefused, deadline: float) -> float:
    """How long to wait before a paused run's reset again; any other refusal,
    or a wait past ``deadline``, is raised."""
    ms = refused.retry_after_ms
    wait = RUN_PAUSED_WAIT_S if ms is None else ms / 1000
    if refused.code != "run_paused" or time.monotonic() + wait > deadline:
        raise refused
    return wait


class _Rollouts:
    """What both clients hold: the run, the service, the open rollout and who resets."""

    __slots__ = ("_identity", "_open", "_run", "_service")

    def __init__(
        self,
        *,
        run: str | None = None,
        credential: str | None = None,
        base_url: str | None = None,
        adapter: str = "",
        adapter_version: str = "",
        framework_version: str = "",
    ) -> None:
        run = run or os.environ.get("O11Y_RUN")
        if not run:
            raise ValueError("no run: pass run= or set O11Y_RUN")
        credential = credential or os.environ.get("O11Y_API_KEY", "")
        base_url = base_url or os.environ.get("O11Y_BASE_URL") or DEFAULT_BASE_URL
        self._service = self._connect(O11yClient(base_url=base_url, credential=credential))
        self._run = run
        self._open: str | None = None
        self._identity = LoopClientV1(
            sdk_version=_SDK_VERSION,
            session_id=_SESSION_ID,
            adapter=adapter,
            adapter_version=adapter_version,
            framework_version=framework_version,
        )

    @property
    def rollout_id(self) -> str | None:
        """The open rollout's id, or ``None``."""
        return self._open

    def _reset_request(self, fields: dict[str, Any]) -> ResetLoopRolloutRequest:
        return ResetLoopRolloutRequest(
            run_id=self._run, request_id=str(uuid.uuid4()), client=self._identity, **fields
        )

    def _step_request(
        self, calls: Iterable[LoopToolCallV1], model_message: str | None
    ) -> StepLoopRolloutRequest:
        return StepLoopRolloutRequest(
            rollout_id=self._require_open(), calls=calls, model_message_json=model_message or ""
        )

    def _require_open(self) -> str:
        if self._open is None:
            raise RuntimeError("no rollout is open: reset() first")
        return self._open


class LoopClient(_Rollouts):
    """One run's rollouts, one open at a time.

    ``run``, ``credential`` and ``base_url`` default to ``O11Y_RUN``,
    ``O11Y_API_KEY`` and ``O11Y_BASE_URL`` (else :data:`DEFAULT_BASE_URL`).
    The key is sent as ``x-o11y-key`` and is never logged or shown. A trainer
    adapter names itself and its framework's version, which every reset
    reports.
    """

    __slots__ = ()

    @staticmethod
    def _connect(o11y: O11yClient) -> LoopRolloutServiceClientSync:
        return o11y.service_sync(LoopRolloutServiceClientSync)

    def reset(self, **fields: Any) -> LoopRolloutV1:
        """Closes the open rollout, then starts one and answers once its
        environment is ready for its first step.

        ``fields`` are ``ResetLoopRolloutRequest``'s own: ``group_id``,
        ``group_index``, ``group_size``, ``case_revision_id``,
        ``trainer_step``, ``trainer_total_steps``, ``experiment_name``.

        A paused run is retried, under one request id, after each refusal's
        ``retry_after_ms`` (or :data:`RUN_PAUSED_WAIT_S`) for up to
        :data:`RUN_PAUSED_RETRY_S`; every other refusal raises at once.
        """
        self.close()
        request = self._reset_request(fields)
        deadline = time.monotonic() + RUN_PAUSED_RETRY_S
        while True:
            try:
                rollout = _call(self._service.reset_loop_rollout, request).rollout
                break
            except RolloutRefused as refused:
                time.sleep(_paused_wait(refused, deadline))
        self._open = rollout.rollout_id
        return rollout

    def step(
        self, calls: Iterable[LoopToolCallV1], model_message: str | None = None
    ) -> StepLoopRolloutResponse:
        """Runs 1 to 16 tool calls at once on the open rollout.
        ``model_message`` is the assistant message they came from, as JSON."""
        return _call(self._service.step_loop_rollout, self._step_request(calls, model_message))

    def close(self) -> LoopRolloutV1 | None:
        """Closes the open rollout and answers with it once its verifier
        reported: its ``rewards``, ``verdict`` and any ``failure``. ``None``
        when none is open."""
        rollout_id, self._open = self._open, None
        if rollout_id is None:
            return None
        request = CloseLoopRolloutRequest(rollout_id=rollout_id)
        while True:
            # Each close holds until the verifier reports or its wait ends.
            closed = _call(self._service.close_loop_rollout, request)
            if not closed.pending:
                return closed.rollout

    def fork(self, copies: int) -> list[LoopClient]:
        """Branches the open rollout into ``copies`` (2 to 64): a client per
        copy, this one first, each with its copy open."""
        request = ForkLoopRolloutRequest(
            rollout_id=self._require_open(), copies=copies, request_id=str(uuid.uuid4())
        )
        forked = _call(self._service.fork_loop_rollout, request)
        clients = [self]
        for rollout in forked.rollouts[1:]:
            client = copy.copy(self)
            client._open = rollout.rollout_id
            clients.append(client)
        return clients


class AsyncLoopClient(_Rollouts):
    """:class:`LoopClient` for an asyncio trainer: reset, step and close,
    awaited. Its steps take turns, so tool calls a trainer gathers at once
    never meet Loop's ``step_in_progress``."""

    __slots__ = ("_lock",)

    def __init__(self, **client: Any) -> None:
        super().__init__(**client)
        self._lock = asyncio.Lock()

    @staticmethod
    def _connect(o11y: O11yClient) -> LoopRolloutServiceClient:
        return o11y.service(LoopRolloutServiceClient)

    async def reset(self, **fields: Any) -> LoopRolloutV1:
        """:meth:`LoopClient.reset`: a paused run waits on ``asyncio.sleep``."""
        await self.close()
        request = self._reset_request(fields)
        deadline = time.monotonic() + RUN_PAUSED_RETRY_S
        while True:
            try:
                rollout = (await _acall(self._service.reset_loop_rollout, request)).rollout
                break
            except RolloutRefused as refused:
                await asyncio.sleep(_paused_wait(refused, deadline))
        self._open = rollout.rollout_id
        return rollout

    async def step(
        self, calls: Iterable[LoopToolCallV1], model_message: str | None = None
    ) -> StepLoopRolloutResponse:
        """:meth:`LoopClient.step`, one at a time."""
        async with self._lock:
            request = self._step_request(calls, model_message)
            return await _acall(self._service.step_loop_rollout, request)

    async def close(self) -> LoopRolloutV1 | None:
        """:meth:`LoopClient.close`."""
        rollout_id, self._open = self._open, None
        if rollout_id is None:
            return None
        request = CloseLoopRolloutRequest(rollout_id=rollout_id)
        while True:
            closed = await _acall(self._service.close_loop_rollout, request)
            if not closed.pending:
                return closed.rollout


def __getattr__(name: str) -> Any:
    if name != "LoopEnvClient":
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    try:
        from .._openenv import LoopEnvClient
    except ModuleNotFoundError as error:
        raise ImportError(
            "LoopEnvClient needs the openenv extra: pip install 'o11y-one[openenv]'"
        ) from error
    return LoopEnvClient
