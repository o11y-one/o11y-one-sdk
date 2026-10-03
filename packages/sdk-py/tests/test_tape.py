"""Record and replay on the external lease plane, against a fake generated client.

The fake keeps each trajectory's next step the way the server does, so a test
reads what was stored and in which chunks. Mirrors packages/sdk-ts/test/tape.test.js.
"""

from __future__ import annotations

import asyncio

import pytest
from connectrpc.code import Code
from connectrpc.errors import ConnectError
from o11y_one.agentic.v1.evaluation_pb2 import (
    AgenticEvaluationCapabilitiesV1,
    CapabilityLimitV1,
    CapabilityPostureV1,
    CapabilityStateV1,
    EvaluationFailureV1,
    ExternalCaseLeaseV1,
    ExternalLeaseRefusalKindV1,
    ExternalLeaseRefusalV1,
    ExternalSubmissionAckKindV1,
    GetAgenticEvaluationCapabilitiesResponse,
    LeasedEvaluationCaseV1,
    LookupReplayStepResponse,
    RecordedCallKindV1,
    RecordedChunkAckV1,
    RecordEvaluationCaseStepsRequest,
    RecordEvaluationCaseStepsResponse,
    ReplayDivergenceV1,
)
from o11y_one.sdk import (
    AgenticClient,
    AgenticClientSync,
    CaseRecordingRejectedError,
    LeaseRefusedError,
    RecordingUnavailableError,
    ReplayDivergedError,
    ValidationError,
)
from test_agentic import FakeAsyncClient, FakeSyncClient

MARGIN = 64 << 10
LEASE = ExternalCaseLeaseV1(lease_id="l1", lease_token="t1")
CASE_A = LeasedEvaluationCaseV1(cohort_key="c", candidate_key="k", case_revision_id="r1", trial=0)
CASE_B = LeasedEvaluationCaseV1(cohort_key="c", candidate_key="k", case_revision_id="r2", trial=0)
SECRET = "sk-canary-0000"
MODEL = RecordedCallKindV1.RECORDED_CALL_KIND_V1_MODEL
TOOL = RecordedCallKindV1.RECORDED_CALL_KIND_V1_TOOL
ACCEPTED = ExternalSubmissionAckKindV1.EXTERNAL_SUBMISSION_ACK_KIND_V1_ACCEPTED
REJECTED = ExternalSubmissionAckKindV1.EXTERNAL_SUBMISSION_ACK_KIND_V1_REJECTED
UNAVAILABLE_KIND = ExternalLeaseRefusalKindV1.EXTERNAL_LEASE_REFUSAL_KIND_V1_RECORDING_UNAVAILABLE


def capabilities(state=CapabilityStateV1.CAPABILITY_STATE_V1_AVAILABLE, **overrides):
    limits = {
        "max_record_request_bytes": MARGIN + 1000,
        "max_call_bytes": 600,
        "max_chunks_per_request": 50,
        "max_calls_per_request": 65536,
        "max_tool_name_bytes": 128,
        **overrides,
    }
    posture = CapabilityPostureV1(
        capability_key="sdk_record_replay",
        state=state,
        limits=[CapabilityLimitV1(limit_key=k, limit_value=v) for k, v in limits.items()],
    )
    return GetAgenticEvaluationCapabilitiesResponse(
        capabilities=AgenticEvaluationCapabilitiesV1(postures=[posture])
    )


def storing(req: RecordEvaluationCaseStepsRequest) -> RecordEvaluationCaseStepsResponse:
    return RecordEvaluationCaseStepsResponse(
        acks=[
            RecordedChunkAckV1(
                case_revision_id=c.case_revision_id,
                kind=ACCEPTED,
                next_step=c.first_step + len(c.calls),
                complete=c.last,
            )
            for c in req.chunks
        ]
    )


def sync_tape(*, caps=None, replay=False, **handlers):
    handlers.setdefault("record_evaluation_case_steps", storing)
    fake = FakeSyncClient(get_agentic_evaluation_capabilities=caps or capabilities(), **handlers)
    client = AgenticClientSync(fake)
    open_tape = client.replay_lease if replay else client.record_lease
    return fake, open_tape(evaluation_run_id="run_1", lease=LEASE)


def sent(fake) -> list[RecordEvaluationCaseStepsRequest]:
    return [req for name, req in fake.calls if name == "record_evaluation_case_steps"]


def test_record_buffers_steps_and_sends_one_chunk_per_case_on_flush() -> None:
    fake, tape = sync_tape()
    a, b = tape.case(CASE_A), tape.case(CASE_B)
    assert a.model('{"m":1}', lambda: '{"r":1}') == '{"r":1}'
    assert a.tool("search", '{"q":2}', lambda: '{"r":2}') == '{"r":2}'
    assert b.model('{"m":3}', lambda: '{"r":3}') == '{"r":3}'
    assert sent(fake) == [], "a step costs no round trip"
    a.finish()
    tape.flush()

    [req] = sent(fake)
    ca, cb = req.chunks
    assert [(c.kind, c.tool_name, c.request_json, c.response_json) for c in ca.calls] == [
        (MODEL, "", '{"m":1}', '{"r":1}'),
        (TOOL, "search", '{"q":2}', '{"r":2}'),
    ]
    assert (ca.first_step, ca.last, cb.last) == (0, True, False)
    assert (req.lease_id, req.lease_token) == ("l1", "t1")

    b.model('{"m":4}', lambda: '{"r":4}')
    b.finish()
    tape.flush()
    [chunk] = sent(fake)[1].chunks
    assert (chunk.first_step, len(chunk.calls), chunk.last) == (1, 1, True)

    tape.flush()
    assert len(sent(fake)) == 2, "nothing pending sends nothing"


def test_record_flushes_before_a_call_would_cross_the_request_bound() -> None:
    fake, tape = sync_tape()
    a = tape.case(CASE_A)
    body = "x" * 200
    a.model(body, lambda: body)
    a.model(body, lambda: body)
    assert sent(fake) == []
    a.model(body, lambda: body)
    assert len(sent(fake)) == 1, "the third call flushed the first two"
    assert len(sent(fake)[0].chunks[0].calls) == 2
    a.finish()
    tape.flush()
    assert (sent(fake)[1].chunks[0].first_step, len(sent(fake)[1].chunks[0].calls)) == (2, 1)


def test_record_flushes_at_the_calls_per_request_bound() -> None:
    fake, tape = sync_tape(caps=capabilities(max_calls_per_request=2))
    a, b = tape.case(CASE_A), tape.case(CASE_B)
    a.model("{}", lambda: "{}")
    b.model("{}", lambda: "{}")
    assert sent(fake) == []
    a.model("{}", lambda: "{}")
    assert len(sent(fake)) == 1
    assert len(sent(fake)[0].chunks) == 2


def test_a_call_over_the_bound_is_refused_locally_naming_sizes_only() -> None:
    fake, tape = sync_tape()
    a = tape.case(CASE_A)
    big = f'"{SECRET}{"x" * 700}"'
    with pytest.raises(ValidationError, match=r"\d+ bytes, over the 600-byte bound") as info:
        a.model("{}", lambda: big)
    assert SECRET not in str(info.value)
    with pytest.raises(ValidationError):
        a.tool("t" * 129, "{}", lambda: "{}")
    tape.flush()
    assert sent(fake) == []


def test_a_conflict_keeps_the_chunk_and_another_rejection_raises() -> None:
    code = ["recording_conflict"]

    def rejecting(req):
        return RecordEvaluationCaseStepsResponse(
            acks=[
                RecordedChunkAckV1(
                    case_revision_id="r1",
                    kind=REJECTED,
                    rejection=EvaluationFailureV1(code=code[0]),
                )
            ]
        )

    fake, tape = sync_tape(record_evaluation_case_steps=rejecting)
    tape.case(CASE_A).model("{}", lambda: "{}")
    tape.flush()
    code[0] = "case_already_submitted"
    with pytest.raises(CaseRecordingRejectedError) as info:
        tape.flush()
    assert len(sent(fake)[1].chunks[0].calls) == 1, "the conflicted call was resent"
    assert (info.value.code, info.value.case_revision_id) == ("case_already_submitted", "r1")
    tape.flush()
    assert len(sent(fake)) == 2, "a rejected case is never resent"


def test_recording_unavailable_on_failed_precondition_is_typed_and_non_retryable() -> None:
    detail = ExternalLeaseRefusalV1(
        kind=UNAVAILABLE_KIND, message="recording and replay are unavailable"
    )
    _, tape = sync_tape(
        record_evaluation_case_steps=ConnectError(
            Code.FAILED_PRECONDITION, "unavailable", details=[detail]
        )
    )
    tape.case(CASE_A).model("{}", lambda: "{}")
    with pytest.raises(RecordingUnavailableError) as info:
        tape.flush()
    assert isinstance(info.value, LeaseRefusedError)
    assert info.value.retryable is False
    assert info.value.refusal.reason_code == "RECORDING_UNAVAILABLE"
    assert str(info.value) == (
        "recording and replay are unavailable on this deployment (RECORDING_UNAVAILABLE)"
    )


def test_recording_unavailable_on_unavailable_stays_a_connect_error_and_keeps_the_buffer() -> None:
    fail = [True]

    def flaky(req):
        if fail[0]:
            raise ConnectError(
                Code.UNAVAILABLE, "store", details=[ExternalLeaseRefusalV1(kind=UNAVAILABLE_KIND)]
            )
        return storing(req)

    fake, tape = sync_tape(record_evaluation_case_steps=flaky)
    tape.case(CASE_A).model("{}", lambda: "{}")
    with pytest.raises(ConnectError) as info:
        tape.flush()
    assert not isinstance(info.value, RecordingUnavailableError)
    fail[0] = False
    tape.flush()
    assert (sent(fake)[1].chunks[0].first_step, len(sent(fake)[1].chunks[0].calls)) == (0, 1)


@pytest.mark.parametrize(
    "caps",
    [
        GetAgenticEvaluationCapabilitiesResponse(),
        capabilities(state=CapabilityStateV1.CAPABILITY_STATE_V1_UNAVAILABLE),
    ],
)
def test_no_available_posture_is_refused_locally_before_any_step(caps) -> None:
    with pytest.raises(RecordingUnavailableError):
        sync_tape(caps=caps)
    with pytest.raises(RecordingUnavailableError):
        sync_tape(caps=caps, replay=True)


def test_a_whole_request_refusal_on_a_200_raises_lease_refused() -> None:
    refusal = ExternalLeaseRefusalV1(
        kind=ExternalLeaseRefusalKindV1.EXTERNAL_LEASE_REFUSAL_KIND_V1_LEASE_EXPIRED
    )
    _, tape = sync_tape(
        record_evaluation_case_steps=RecordEvaluationCaseStepsResponse(refusal=refusal)
    )
    tape.case(CASE_A).model("{}", lambda: "{}")
    with pytest.raises(LeaseRefusedError) as info:
        tape.flush()
    assert info.value.refusal.reason_code == "LEASE_EXPIRED"


def never() -> str:
    raise AssertionError("live must not run under replay")


def test_replay_answers_each_step_from_the_recording_without_calling_live() -> None:
    fake, tape = sync_tape(
        replay=True,
        lookup_replay_step=lambda req: LookupReplayStepResponse(
            response_json=f'{{"step":{req.step}}}'
        ),
    )
    a = tape.case(CASE_A)
    assert a.model('{"m":1}', never) == '{"step":0}'
    assert a.tool("search", '{"q":1}', never) == '{"step":1}'
    seen = [req for name, req in fake.calls if name == "lookup_replay_step"]
    assert [
        (r.step, r.observed.kind, r.observed.tool_name, r.case_revision_id, r.lease_token)
        for r in seen
    ] == [(0, MODEL, "", "r1", "t1"), (1, TOOL, "search", "r1", "t1")]
    a.finish()
    tape.flush()


@pytest.mark.parametrize(
    ("kind", "reason"),
    [
        (1, "MODEL_REQUEST_DIFFERS"),
        (2, "TOOL_REQUEST_DIFFERS"),
        (3, "RECORDING_EXHAUSTED"),
        (4, "RECORDING_INCOMPLETE"),
        (99, "UNSPECIFIED"),
    ],
)
def test_each_divergence_kind_raises_replay_diverged(kind, reason) -> None:
    _, tape = sync_tape(
        replay=True,
        lookup_replay_step=lambda req: LookupReplayStepResponse(
            divergence=ReplayDivergenceV1(
                step=req.step, kind=kind, expected_request_digest="aa", observed_request_digest="bb"
            )
        ),
    )
    with pytest.raises(ReplayDivergedError) as info:
        tape.case(CASE_A).model(f'{{"k":"{SECRET}"}}', never)
    d = info.value.divergence
    assert (d.reason, d.step, d.expected_request_digest, d.observed_request_digest) == (
        reason,
        0,
        "aa",
        "bb",
    )
    assert SECRET not in str(info.value)


def test_replay_refusals_on_a_200_and_in_the_details() -> None:
    done = ExternalLeaseRefusalV1(
        kind=ExternalLeaseRefusalKindV1.EXTERNAL_LEASE_REFUSAL_KIND_V1_CASE_ALREADY_SUBMITTED
    )
    _, tape = sync_tape(replay=True, lookup_replay_step=LookupReplayStepResponse(refusal=done))
    with pytest.raises(LeaseRefusedError) as info:
        tape.case(CASE_A).model("{}", never)
    assert info.value.refusal.reason_code == "CASE_ALREADY_SUBMITTED"

    _, off = sync_tape(
        replay=True,
        lookup_replay_step=ConnectError(
            Code.FAILED_PRECONDITION, "x", details=[ExternalLeaseRefusalV1(kind=UNAVAILABLE_KIND)]
        ),
    )
    with pytest.raises(RecordingUnavailableError):
        off.case(CASE_A).model("{}", never)


def test_async_tape_records_and_replays_like_the_sync_one() -> None:
    fake = FakeAsyncClient(
        get_agentic_evaluation_capabilities=capabilities(),
        record_evaluation_case_steps=storing,
        lookup_replay_step=lambda req: LookupReplayStepResponse(response_json=f"{req.step}"),
    )
    client = AgenticClient(fake)

    async def live() -> str:
        return '{"r":1}'

    async def run() -> None:
        tape = await client.record_lease(evaluation_run_id="run_1", lease=LEASE)
        a = tape.case(CASE_A)
        assert await a.model("{}", live) == '{"r":1}'
        a.finish()
        await tape.flush()
        replay = await client.replay_lease(evaluation_run_id="run_1", lease=LEASE)
        replayed = replay.case(CASE_A)
        assert await replayed.model("{}", never) == "0"
        assert await replayed.tool("t", "{}", never) == "1"

    asyncio.run(run())
    [req] = sent(fake)
    assert (len(req.chunks[0].calls), req.chunks[0].last) == (1, True)
    calls = [name for name, _ in fake.calls]
    assert calls.count("get_agentic_evaluation_capabilities") == 1, "limits are cached per client"
