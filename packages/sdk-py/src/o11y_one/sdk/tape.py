"""Record and replay for an externally executed candidate.

One tape per lease, one case handle per leased case, and the same harness code
in both modes. Mirrors ``packages/sdk-ts/src/tape.ts``.

Recording buffers each model and tool call in memory and sends a lease's cases
together, one chunk per case, when the next call would cross a bound the server
publishes on ``sdk_record_replay``, or on ``flush()``. Record, then submit: call
``flush()`` after ``finish()`` and before ``submit_case_outputs``. Steps that
never reached a flush are lost with the process; the case's recording stays
incomplete, and the server replays it as ``RECORDING_INCOMPLETE``.

Replay answers each call from the recording through ``LookupReplayStep`` and
never runs ``live``. The first call that leaves the recording raises
:class:`ReplayDivergedError`; the server has already made that the case's
verdict, so the harness stops the case and does not submit it.

Redaction is the server's, before anything is digested or stored. Nothing here
logs a call, or puts a request or response body in an exception.
"""

from __future__ import annotations

import asyncio
import threading
from collections.abc import Awaitable, Callable
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from o11y_one.agentic.v1.evaluation_pb2 import (
    ExternalSubmissionAckKindV1,
    LeasedEvaluationCaseV1,
    LookupReplayStepResponse,
    RecordedCallKindV1,
    RecordedCallV1,
    RecordedTrajectoryChunkV1,
    ReplayDivergenceKindV1,
    ReplayDivergenceV1,
)

from .recovery import bare_enum_name
from .results import Refusal
from .validation import ValidationError

if TYPE_CHECKING:
    from .agentic import AgenticClient, AgenticClientSync

__all__ = [
    "CaseRecordingRejectedError",
    "CaseTape",
    "CaseTapeSync",
    "LeaseRefusedError",
    "LeaseTape",
    "LeaseTapeSync",
    "RecordReplayLimits",
    "RecordingUnavailableError",
    "ReplayDivergedError",
    "ReplayDivergence",
]

# The server's own margin between its request bound and its per-call bound.
_FRAMING_MARGIN_BYTES = 64 << 10
# ponytail: a flat per-call framing estimate rather than serializing the request on every
# step; the margin above absorbs it until calls get tiny and numerous enough to need an
# exact ByteSize().
_CALL_FRAMING_BYTES = 16
_RECORDING_CONFLICT = "recording_conflict"
_MODEL = RecordedCallKindV1.RECORDED_CALL_KIND_V1_MODEL
_TOOL = RecordedCallKindV1.RECORDED_CALL_KIND_V1_TOOL
_REJECTED = ExternalSubmissionAckKindV1.EXTERNAL_SUBMISSION_ACK_KIND_V1_REJECTED


class LeaseRefusedError(Exception):
    """The lease plane refused the request. ``refusal.reason_code`` names the wire kind."""

    def __init__(self, refusal: Refusal, message: str | None = None) -> None:
        self.refusal = refusal
        super().__init__(message or f"the lease plane refused the request ({refusal.reason_code})")


class RecordingUnavailableError(LeaseRefusedError):
    """This deployment cannot record or replay. Retrying will not change that."""

    retryable = False

    def __init__(self, refusal: Refusal | None = None) -> None:
        text = "recording and replay are unavailable on this deployment (RECORDING_UNAVAILABLE)"
        super().__init__(
            refusal or Refusal(reason_code="RECORDING_UNAVAILABLE", message=text), text
        )


class CaseRecordingRejectedError(Exception):
    """The server stored none of one case's chunk, for a reason a resend will not fix."""

    def __init__(self, code: str, case: LeasedEvaluationCaseV1) -> None:
        self.code = code
        self.cohort_key = case.cohort_key
        self.candidate_key = case.candidate_key
        self.case_revision_id = case.case_revision_id
        self.trial = case.trial
        super().__init__(f"the server rejected case {case.case_revision_id}'s recording ({code})")


@dataclass(frozen=True, slots=True)
class ReplayDivergence:
    step: int
    reason: str
    # sha256 hex of the recorded request; empty when the recording holds no such step.
    expected_request_digest: str
    observed_request_digest: str


class ReplayDivergedError(Exception):
    """The replayed agent left its recording at ``divergence.step``.

    Stop the case and do not submit it: the server already made this its verdict.
    """

    def __init__(self, divergence: ReplayDivergenceV1) -> None:
        self.divergence = ReplayDivergence(
            step=divergence.step,
            reason=bare_enum_name(ReplayDivergenceKindV1, divergence.kind),
            expected_request_digest=divergence.expected_request_digest,
            observed_request_digest=divergence.observed_request_digest,
        )
        super().__init__(
            f"the replayed agent left its recording at step {divergence.step} "
            f"({self.divergence.reason})"
        )


def lease_refused_error(refusal: Refusal) -> LeaseRefusedError:
    if refusal.reason_code == "RECORDING_UNAVAILABLE":
        return RecordingUnavailableError(refusal)
    return LeaseRefusedError(refusal)


@dataclass(frozen=True, slots=True)
class RecordReplayLimits:
    """The bounds ``sdk_record_replay`` publishes, each the constant the server enforces."""

    max_record_request_bytes: int
    max_call_bytes: int
    max_chunks_per_request: int
    max_calls_per_request: int
    max_tool_name_bytes: int


def _call_bytes(call: RecordedCallV1) -> int:
    return sum(len(s.encode()) for s in (call.tool_name, call.request_json, call.response_json))


@dataclass(slots=True)
class _Pending:
    case: LeasedEvaluationCaseV1
    first_step: int = 0
    calls: list[tuple[RecordedCallV1, int]] = field(default_factory=list)
    last: bool = False
    closed: bool = False


class _Buffer:
    """The transport-free half of a recording tape, shared by the async and sync twins."""

    def __init__(self, limits: RecordReplayLimits) -> None:
        self.limits = limits
        self.cases: list[_Pending] = []
        self.pending_bytes = 0
        self.pending_calls = 0

    def check_tool_name(self, tool_name: str) -> None:
        size = len(tool_name.encode())
        if size > self.limits.max_tool_name_bytes:
            raise ValidationError(
                "tool_name",
                f"tool_name is {size} bytes, over the {self.limits.max_tool_name_bytes}-byte bound",
            )

    def sized(self, call: RecordedCallV1) -> int:
        size = _call_bytes(call)
        if size > self.limits.max_call_bytes:
            raise ValidationError(
                "call", f"call is {size} bytes, over the {self.limits.max_call_bytes}-byte bound"
            )
        return size + _CALL_FRAMING_BYTES

    def must_flush_before(self, size: int) -> bool:
        return (
            self.pending_bytes + size > self.limits.max_record_request_bytes - _FRAMING_MARGIN_BYTES
            or self.pending_calls + 1 > self.limits.max_calls_per_request
        )

    def push(self, pending: _Pending, call: RecordedCallV1, size: int) -> None:
        pending.calls.append((call, size))
        self.pending_bytes += size
        self.pending_calls += 1

    def batches(self) -> list[list[_Pending]]:
        sending = [p for p in self.cases if p.calls or (p.last and not p.closed)]
        n = self.limits.max_chunks_per_request
        return [sending[i : i + n] for i in range(0, len(sending), n)]

    @staticmethod
    def chunks(batch: list[_Pending]) -> list[RecordedTrajectoryChunkV1]:
        return [
            RecordedTrajectoryChunkV1(
                cohort_key=p.case.cohort_key,
                candidate_key=p.case.candidate_key,
                case_revision_id=p.case.case_revision_id,
                trial=p.case.trial,
                attempt_generation=p.case.attempt_generation,
                first_step=p.first_step,
                calls=[call for call, _ in p.calls],
                last=p.last,
            )
            for p in batch
        ]

    def _drop(self, p: _Pending, count: int) -> None:
        for _, size in p.calls[:count]:
            self.pending_bytes -= size
            self.pending_calls -= 1
        del p.calls[:count]

    def apply(self, batch: list[_Pending], sent: list[int], resp) -> None:
        if not isinstance(resp, list):
            raise lease_refused_error(resp)
        rejected: CaseRecordingRejectedError | None = None
        for p, count, ack in zip(batch, sent, resp, strict=False):
            if ack.kind == _REJECTED:
                # A conflict: the trajectory moved under the write; keep the calls.
                if ack.rejection.code != _RECORDING_CONFLICT:
                    rejected = rejected or CaseRecordingRejectedError(ack.rejection.code, p.case)
                    # Never resent: a rejection names a case this lease can no longer record.
                    self._drop(p, len(p.calls))
                    p.closed = True
                continue
            # Calls appended while the request was in flight follow the ones sent: drop a prefix.
            stored = min(max(ack.next_step - p.first_step, 0), count)
            self._drop(p, stored)
            p.first_step += stored
            p.closed = p.closed or ack.complete
        if rejected is not None:
            raise rejected


def _answer(resp: LookupReplayStepResponse | Refusal) -> str:
    if isinstance(resp, Refusal):
        raise lease_refused_error(resp)
    if resp.WhichOneof("outcome") == "divergence":
        raise ReplayDivergedError(resp.divergence)
    if resp.WhichOneof("outcome") == "response_json":
        return resp.response_json
    raise RuntimeError("lookup_replay_step: neither an outcome nor a refusal was returned")


class LeaseTape:
    """One lease's tape. Build it with ``AgenticClient.record_lease`` or ``replay_lease``."""

    def __init__(
        self,
        client: AgenticClient,
        replay: bool,
        evaluation_run_id: str,
        lease_id: str,
        lease_token: str,
        limits: RecordReplayLimits,
    ) -> None:
        self._client = client
        self._replay = replay
        self._fence = {
            "evaluation_run_id": evaluation_run_id,
            "lease_id": lease_id,
            "lease_token": lease_token,
        }
        self._buffer = _Buffer(limits)
        # Serialized, so two flushes never send overlapping chunks for one case.
        self._lock = asyncio.Lock()

    def case(self, leased: LeasedEvaluationCaseV1) -> CaseTape:
        """The handle a harness routes one leased case's model and tool calls through."""
        pending = _Pending(case=leased)
        self._buffer.cases.append(pending)
        return CaseTape(self, pending)

    async def flush(self) -> None:
        """Send every buffered call and every finished case. A no-op under replay."""
        async with self._lock:
            await self._flush()

    async def _flush(self) -> None:
        for batch in self._buffer.batches():
            sent = [len(p.calls) for p in batch]
            resp = await self._client.record_case_steps(**self._fence, chunks=_Buffer.chunks(batch))
            self._buffer.apply(batch, sent, resp if isinstance(resp, Refusal) else list(resp.acks))

    async def _record(self, pending: _Pending, call: RecordedCallV1) -> None:
        size = self._buffer.sized(call)
        async with self._lock:
            if self._buffer.must_flush_before(size):
                await self._flush()
            self._buffer.push(pending, call, size)


class CaseTape:
    """One leased case's calls, made one at a time: steps are numbered as they complete."""

    def __init__(self, tape: LeaseTape, pending: _Pending) -> None:
        self._tape = tape
        self._pending = pending
        self._step = 0

    async def model(self, request_json: str, live: Callable[[], Awaitable[str]]) -> str:
        """A model call: ``live`` runs and is recorded, or replay returns the recording."""
        return await self._call(_MODEL, "", request_json, live)

    async def tool(
        self, tool_name: str, request_json: str, live: Callable[[], Awaitable[str]]
    ) -> str:
        """A tool call, as :meth:`model`."""
        return await self._call(_TOOL, tool_name, request_json, live)

    def finish(self) -> None:
        """The case made its last call: its next flush completes the recording."""
        self._pending.last = True

    async def _call(self, kind, tool_name: str, request_json: str, live) -> str:
        self._tape._buffer.check_tool_name(tool_name)
        if self._tape._replay:
            resp = await self._tape._client.lookup_replay_step(
                **self._tape._fence,
                case=self._pending.case,
                step=self._step,
                kind=kind,
                tool_name=tool_name,
                request_json=request_json,
            )
            response = _answer(resp)
            self._step += 1
            return response
        response = await live()
        call = RecordedCallV1(
            kind=kind, tool_name=tool_name, request_json=request_json, response_json=response
        )
        await self._tape._record(self._pending, call)
        return response


class LeaseTapeSync:
    """:class:`LeaseTape`, blocking, and safe to share across a harness's worker threads."""

    def __init__(
        self,
        client: AgenticClientSync,
        replay: bool,
        evaluation_run_id: str,
        lease_id: str,
        lease_token: str,
        limits: RecordReplayLimits,
    ) -> None:
        self._client = client
        self._replay = replay
        self._fence = {
            "evaluation_run_id": evaluation_run_id,
            "lease_id": lease_id,
            "lease_token": lease_token,
        }
        self._buffer = _Buffer(limits)
        self._lock = threading.Lock()

    def case(self, leased: LeasedEvaluationCaseV1) -> CaseTapeSync:
        pending = _Pending(case=leased)
        with self._lock:
            self._buffer.cases.append(pending)
        return CaseTapeSync(self, pending)

    def flush(self) -> None:
        with self._lock:
            self._flush()

    def _flush(self) -> None:
        for batch in self._buffer.batches():
            sent = [len(p.calls) for p in batch]
            resp = self._client.record_case_steps(**self._fence, chunks=_Buffer.chunks(batch))
            self._buffer.apply(batch, sent, resp if isinstance(resp, Refusal) else list(resp.acks))

    def _record(self, pending: _Pending, call: RecordedCallV1) -> None:
        size = self._buffer.sized(call)
        with self._lock:
            if self._buffer.must_flush_before(size):
                self._flush()
            self._buffer.push(pending, call, size)


class CaseTapeSync:
    """:class:`CaseTape`, blocking."""

    def __init__(self, tape: LeaseTapeSync, pending: _Pending) -> None:
        self._tape = tape
        self._pending = pending
        self._step = 0

    def model(self, request_json: str, live: Callable[[], str]) -> str:
        return self._call(_MODEL, "", request_json, live)

    def tool(self, tool_name: str, request_json: str, live: Callable[[], str]) -> str:
        return self._call(_TOOL, tool_name, request_json, live)

    def finish(self) -> None:
        self._pending.last = True

    def _call(self, kind, tool_name: str, request_json: str, live) -> str:
        self._tape._buffer.check_tool_name(tool_name)
        if self._tape._replay:
            resp = self._tape._client.lookup_replay_step(
                **self._tape._fence,
                case=self._pending.case,
                step=self._step,
                kind=kind,
                tool_name=tool_name,
                request_json=request_json,
            )
            response = _answer(resp)
            self._step += 1
            return response
        response = live()
        call = RecordedCallV1(
            kind=kind, tool_name=tool_name, request_json=request_json, response_json=response
        )
        self._tape._record(self._pending, call)
        return response
