"""Tests for the ``AgenticEvaluationService`` ergonomic facade.

No network, no mocked HTTP transport: the facade classes take any object with
the right method names (structural typing — Python does not check the
``ConnectClientSync``/``ConnectClient`` type hint at runtime), so a plain fake
object standing in for the generated client is enough to prove the
validation, refusal-decoding and orchestration logic works. This also proves
the wrapper never touches the network by construction — there is no transport
for it to reach even if it tried.
"""

from __future__ import annotations

import asyncio
from datetime import UTC, datetime

import pytest
from connectrpc.code import Code
from connectrpc.errors import ConnectError
from google.protobuf import timestamp_pb2
from o11y_one.agentic.v1.evaluation_pb2 import (
    ApproveDatasetCaseDraftResponse,
    CaptureEvaluationCaseResponse,
    CreateMachineCredentialResponse,
    DatasetCaseDraftRejectionReasonV1,
    EvaluationLaunchRejectionKindV1,
    EvaluationLaunchRejectionV1,
    ExternalCaseLeaseV1,
    ExternalCaseOutputAckV1,
    ExternalLeaseRefusalKindV1,
    ExternalLeaseRefusalV1,
    ExternalSubmissionAckKindV1,
    GetCallerPrincipalResponse,
    LeaseEvaluationCasesResponse,
    MachineCredentialV1,
    PlatformAnnotationKindV1,
    PrincipalKindV1,
    PrincipalRefV1,
    ReleaseEvaluationCaseLeaseResponse,
    SubmitEvaluationCaseOutputsResponse,
    UpdateDatasetCaseDraftResponse,
)
from o11y_one.sdk.agentic import AgenticClient, AgenticClientSync, CaseOutput
from o11y_one.sdk.results import Refusal
from o11y_one.sdk.validation import ValidationError


class FakeSyncClient:
    """Stands in for ``AgenticEvaluationServiceClientSync``: one attribute per
    RPC the facade calls, each recording its request and returning a canned
    response (or raising, for error-path tests)."""

    def __init__(self, **handlers):
        self._handlers = handlers
        self.calls: list[tuple[str, object]] = []

    def __getattr__(self, name: str):
        def method(request, *, headers=None, timeout_ms=None):
            self.calls.append((name, request))
            handler = self._handlers.get(name)
            if handler is None:
                raise AssertionError(f"unexpected call: {name}")
            if isinstance(handler, Exception):
                raise handler
            return handler(request) if callable(handler) else handler

        return method


class FakeAsyncClient(FakeSyncClient):
    """Same fake, awaitable methods — stands in for ``AgenticEvaluationServiceClient``."""

    def __getattr__(self, name: str):
        sync_method = super().__getattr__(name)

        async def method(request, *, headers=None, timeout_ms=None):
            return sync_method(request, headers=headers, timeout_ms=timeout_ms)

        return method


# --------------------------------------------------------------------------
# whoami / machine principal + credential management
# --------------------------------------------------------------------------


def test_whoami_passes_through() -> None:
    caller = PrincipalRefV1(kind=PrincipalKindV1.PRINCIPAL_KIND_V1_MACHINE, principal_id="mp_1")
    fake = FakeSyncClient(
        get_caller_principal=GetCallerPrincipalResponse(caller=caller, tenant_id="t1", org_id="o1")
    )
    client = AgenticClientSync(fake)
    resp = client.whoami()
    assert resp.tenant_id == "t1"
    assert resp.caller.principal_id == "mp_1"


def test_create_machine_principal_rejects_blank_display_name() -> None:
    client = AgenticClientSync(FakeSyncClient())
    with pytest.raises(ValidationError, match="display_name"):
        client.create_machine_principal(display_name="", scopes=["eval:read"])


def test_create_machine_principal_rejects_unknown_scope_name() -> None:
    client = AgenticClientSync(FakeSyncClient())
    with pytest.raises(ValidationError, match="unknown scope name"):
        client.create_machine_principal(display_name="ci-runner", scopes=["not-a-real-scope"])


def test_create_machine_principal_sends_mapped_scope_enum() -> None:
    fake = FakeSyncClient(create_machine_principal=lambda req: req)
    client = AgenticClientSync(fake)
    client.create_machine_principal(display_name="ci-runner", scopes=["eval:read", "lease:submit"])
    _, sent = fake.calls[0]
    assert sent.display_name == "ci-runner"
    assert len(sent.scopes) == 2


def test_create_machine_credential_returns_distinct_issued_type_with_one_time_token() -> None:
    credential = MachineCredentialV1(credential_id="cred_1", token_prefix="o11y_mach.AAAA")
    fake = FakeSyncClient(
        create_machine_credential=CreateMachineCredentialResponse(
            credential=credential, plaintext_token_once="o11y_mach.AAAA.SECRET"
        )
    )
    client = AgenticClientSync(fake)
    issued = client.create_machine_credential(machine_principal_id="mp_1")
    assert issued.credential_id == "cred_1"
    assert issued.token_prefix == "o11y_mach.AAAA"
    assert issued.one_time_token == "o11y_mach.AAAA.SECRET"
    # It is its own type — not the generic MachineCredentialV1 resource — so a
    # caller cannot accidentally hold onto / log a resource that also carries
    # the secret.
    assert not hasattr(credential, "plaintext_token_once")


def test_create_machine_credential_rejects_blank_principal_id() -> None:
    client = AgenticClientSync(FakeSyncClient())
    with pytest.raises(ValidationError, match="machine_principal_id"):
        client.create_machine_credential(machine_principal_id="")


def test_revoke_machine_credential_rejects_blank_id() -> None:
    client = AgenticClientSync(FakeSyncClient())
    with pytest.raises(ValidationError, match="credential_id"):
        client.revoke_machine_credential(credential_id="")


# --------------------------------------------------------------------------
# run submit
# --------------------------------------------------------------------------


def test_create_run_requires_definition_id_and_idempotency_key() -> None:
    client = AgenticClientSync(FakeSyncClient())
    with pytest.raises(ValidationError, match="definition_id"):
        client.create_run(definition_id="", idempotency_key="k1")
    with pytest.raises(ValidationError, match="idempotency_key"):
        client.create_run(definition_id="def_1", idempotency_key="")


def test_create_run_passes_optional_preview_token() -> None:
    fake = FakeSyncClient(create_evaluation_run=lambda req: req)
    client = AgenticClientSync(fake)
    client.create_run(definition_id="def_1", idempotency_key="k1", preview_token="tok_1")
    _, sent = fake.calls[0]
    assert sent.definition_id == "def_1"
    assert sent.preview_token == "tok_1"


def test_create_run_decodes_launch_rejection_detail_off_a_thrown_error() -> None:
    rejection = EvaluationLaunchRejectionV1(
        kind=EvaluationLaunchRejectionKindV1.EVALUATION_LAUNCH_REJECTION_KIND_V1_PREVIEW_EXPIRED,
        detail="the preview token expired",
    )
    fake = FakeSyncClient(
        create_evaluation_run=ConnectError(
            Code.FAILED_PRECONDITION, "rejected", details=[rejection]
        )
    )
    client = AgenticClientSync(fake)
    result = client.create_run(definition_id="def_1", idempotency_key="k1", preview_token="tok_1")
    assert isinstance(result, Refusal)
    assert result.reason_code == "PREVIEW_EXPIRED"
    assert result.message == "the preview token expired"


def test_create_run_reraises_transport_errors_without_a_matching_detail() -> None:
    fake = FakeSyncClient(create_evaluation_run=ConnectError(Code.UNAVAILABLE, "backend down"))
    client = AgenticClientSync(fake)
    with pytest.raises(ConnectError, match="backend down"):
        client.create_run(definition_id="def_1", idempotency_key="k1")


# --------------------------------------------------------------------------
# lease -> heartbeat -> submit -> release, and its typed refusals
# --------------------------------------------------------------------------


def test_lease_cases_rejects_negative_max_cases() -> None:
    client = AgenticClientSync(FakeSyncClient())
    with pytest.raises(ValidationError, match="max_cases"):
        client.lease_cases(
            evaluation_run_id="run_1", candidate_key="c1", runtime_key="rt1", max_cases=-1
        )


def test_lease_cases_success_passes_through() -> None:
    lease = ExternalCaseLeaseV1(lease_id="lease_1", lease_token="tok", case_count=2)
    fake = FakeSyncClient(lease_evaluation_cases=LeaseEvaluationCasesResponse(lease=lease))
    client = AgenticClientSync(fake)
    result = client.lease_cases(evaluation_run_id="run_1", candidate_key="c1", runtime_key="rt1")
    assert not isinstance(result, Refusal)
    assert result.lease.lease_id == "lease_1"


def test_lease_cases_refusal_decodes_to_typed_recovery_state() -> None:
    refusal = ExternalLeaseRefusalV1(
        kind=ExternalLeaseRefusalKindV1.EXTERNAL_LEASE_REFUSAL_KIND_V1_LEASE_EXPIRED,
        message="lease expired",
    )
    fake = FakeSyncClient(lease_evaluation_cases=LeaseEvaluationCasesResponse(refusal=refusal))
    client = AgenticClientSync(fake)
    result = client.lease_cases(evaluation_run_id="run_1", candidate_key="c1", runtime_key="rt1")
    assert isinstance(result, Refusal)
    assert result.reason_code == "LEASE_EXPIRED"
    assert result.message == "lease expired"


def test_submit_case_outputs_rejects_empty_batch() -> None:
    client = AgenticClientSync(FakeSyncClient())
    with pytest.raises(ValidationError, match="outputs"):
        client.submit_case_outputs(
            evaluation_run_id="run_1",
            lease_id="lease_1",
            lease_token="tok",
            outputs=[],
            idempotency_key="k1",
        )


def test_case_output_rejects_neither_payload_nor_failure() -> None:
    client = AgenticClientSync(FakeSyncClient())
    bad = CaseOutput(cohort_key="c", candidate_key="cand", case_revision_id="rev", trial=0)
    with pytest.raises(ValidationError, match="output_payload_json"):
        client.submit_case_outputs(
            evaluation_run_id="run_1",
            lease_id="lease_1",
            lease_token="tok",
            outputs=[bad],
            idempotency_key="k1",
        )


def test_case_output_rejects_both_payload_and_failure() -> None:
    client = AgenticClientSync(FakeSyncClient())
    bad = CaseOutput(
        cohort_key="c",
        candidate_key="cand",
        case_revision_id="rev",
        trial=0,
        output_payload_json="{}",
        failure_code="TIMEOUT",
    )
    with pytest.raises(ValidationError, match="output_payload_json"):
        client.submit_case_outputs(
            evaluation_run_id="run_1",
            lease_id="lease_1",
            lease_token="tok",
            outputs=[bad],
            idempotency_key="k1",
        )


def test_submit_case_outputs_builds_batch_and_returns_partial_result() -> None:
    ack_ok = ExternalCaseOutputAckV1(
        cohort_key="c",
        candidate_key="a",
        case_revision_id="r1",
        trial=0,
        kind=ExternalSubmissionAckKindV1.EXTERNAL_SUBMISSION_ACK_KIND_V1_ACCEPTED,
    )
    ack_bad = ExternalCaseOutputAckV1(
        cohort_key="c",
        candidate_key="b",
        case_revision_id="r2",
        trial=0,
        kind=ExternalSubmissionAckKindV1.EXTERNAL_SUBMISSION_ACK_KIND_V1_REJECTED,
    )
    fake = FakeSyncClient(
        submit_evaluation_case_outputs=SubmitEvaluationCaseOutputsResponse(
            acks=[ack_ok, ack_bad], accepted_count=1, rejected_count=1
        )
    )
    client = AgenticClientSync(fake)
    outputs = [
        CaseOutput(
            cohort_key="c",
            candidate_key="a",
            case_revision_id="r1",
            trial=0,
            output_payload_json="{}",
        ),
        CaseOutput(
            cohort_key="c",
            candidate_key="b",
            case_revision_id="r2",
            trial=0,
            failure_code="TIMEOUT",
        ),
    ]
    result = client.submit_case_outputs(
        evaluation_run_id="run_1",
        lease_id="lease_1",
        lease_token="tok",
        outputs=outputs,
        idempotency_key="k1",
    )
    assert not isinstance(result, Refusal)
    assert result.accepted_count == 1
    assert result.rejected_count == 1
    _, sent = fake.calls[0]
    assert len(sent.outputs) == 2
    assert sent.outputs[0].output_payload_json == "{}"
    assert sent.outputs[1].failure.code == "TIMEOUT"


def test_submit_recorded_outputs_orchestrates_lease_submit_release_and_releases_on_error() -> None:
    lease = ExternalCaseLeaseV1(lease_id="lease_1", lease_token="tok", case_count=1)
    fake = FakeSyncClient(
        lease_evaluation_cases=LeaseEvaluationCasesResponse(lease=lease),
        submit_evaluation_case_outputs=RuntimeError("network blip"),
        release_evaluation_case_lease=ReleaseEvaluationCaseLeaseResponse(released_case_count=1),
    )
    client = AgenticClientSync(fake)
    outputs = [
        CaseOutput(
            cohort_key="c",
            candidate_key="a",
            case_revision_id="r1",
            trial=0,
            output_payload_json="{}",
        )
    ]
    with pytest.raises(RuntimeError, match="network blip"):
        client.submit_recorded_outputs(
            evaluation_run_id="run_1",
            candidate_key="cand",
            runtime_key="rt1",
            outputs=outputs,
            idempotency_key="k1",
        )
    called = [name for name, _ in fake.calls]
    # The lease is released even though submission raised.
    assert called == [
        "lease_evaluation_cases",
        "submit_evaluation_case_outputs",
        "release_evaluation_case_lease",
    ]


def test_submit_recorded_outputs_returns_refusal_without_calling_submit() -> None:
    refusal = ExternalLeaseRefusalV1(
        kind=ExternalLeaseRefusalKindV1.EXTERNAL_LEASE_REFUSAL_KIND_V1_RUN_NOT_EXECUTABLE,
        message="no",
    )
    fake = FakeSyncClient(lease_evaluation_cases=LeaseEvaluationCasesResponse(refusal=refusal))
    client = AgenticClientSync(fake)
    outputs = [
        CaseOutput(
            cohort_key="c",
            candidate_key="a",
            case_revision_id="r1",
            trial=0,
            output_payload_json="{}",
        )
    ]
    result = client.submit_recorded_outputs(
        evaluation_run_id="run_1",
        candidate_key="cand",
        runtime_key="rt1",
        outputs=outputs,
        idempotency_key="k1",
    )
    assert isinstance(result, Refusal)
    assert [name for name, _ in fake.calls] == ["lease_evaluation_cases"]


# --------------------------------------------------------------------------
# dataset drafts
# --------------------------------------------------------------------------


def test_capture_case_draft_requires_exactly_one_source() -> None:
    client = AgenticClientSync(FakeSyncClient())
    with pytest.raises(ValidationError, match="span"):
        client.capture_case_draft(dataset_collection_id="dc_1", idempotency_key="k1")
    with pytest.raises(ValidationError, match="span"):
        client.capture_case_draft(
            dataset_collection_id="dc_1",
            idempotency_key="k1",
            trace_id=b"trace",
            evaluation_run_id="run_1",
        )


def test_capture_case_draft_span_source_passes_through() -> None:
    fake = FakeSyncClient(capture_evaluation_case=CaptureEvaluationCaseResponse())
    client = AgenticClientSync(fake)
    client.capture_case_draft(
        dataset_collection_id="dc_1", idempotency_key="k1", trace_id=b"trace", span_id=b"span"
    )
    _, sent = fake.calls[0]
    assert sent.span.trace_id == b"trace"


def test_update_case_draft_rejects_value_and_absence_reason_together() -> None:
    client = AgenticClientSync(FakeSyncClient())
    with pytest.raises(ValidationError, match="expected_output_json"):
        client.update_case_draft(
            proposed_case_id="pc_1",
            expected_draft_version=1,
            idempotency_key="k1",
            expected_output_json="{}",
            expected_output_absence_reason="no ground truth exists",
        )


def test_update_case_draft_accepts_value_alone() -> None:
    fake = FakeSyncClient(update_dataset_case_draft=UpdateDatasetCaseDraftResponse())
    client = AgenticClientSync(fake)
    client.update_case_draft(
        proposed_case_id="pc_1",
        expected_draft_version=1,
        idempotency_key="k1",
        expected_output_json="{}",
    )
    assert fake.calls[0][0] == "update_dataset_case_draft"


def test_reject_case_draft_requires_non_unspecified_reason() -> None:
    client = AgenticClientSync(FakeSyncClient())
    with pytest.raises(ValidationError, match="reason"):
        client.reject_case_draft(
            proposed_case_id="pc_1",
            expected_draft_version=1,
            reason=DatasetCaseDraftRejectionReasonV1.DATASET_CASE_DRAFT_REJECTION_REASON_V1_UNSPECIFIED,
            idempotency_key="k1",
        )


def test_approve_case_draft_requires_idempotency_key() -> None:
    client = AgenticClientSync(FakeSyncClient())
    with pytest.raises(ValidationError, match="idempotency_key"):
        client.approve_case_draft(
            proposed_case_id="pc_1", expected_draft_version=1, idempotency_key=""
        )


def test_approve_case_draft_passes_through() -> None:
    fake = FakeSyncClient(approve_dataset_case_draft=ApproveDatasetCaseDraftResponse())
    client = AgenticClientSync(fake)
    client.approve_case_draft(
        proposed_case_id="pc_1", expected_draft_version=2, idempotency_key="k1"
    )
    assert fake.calls[0][0] == "approve_dataset_case_draft"


def test_publish_case_drafts_requires_preview_digest() -> None:
    client = AgenticClientSync(FakeSyncClient())
    with pytest.raises(ValidationError, match="preview_digest"):
        client.publish_case_drafts(changeset_id="cs_1", preview_digest="", idempotency_key="k1")


# --------------------------------------------------------------------------
# annotations
# --------------------------------------------------------------------------


def test_record_annotation_requires_kind_title_and_idempotency_key() -> None:
    client = AgenticClientSync(FakeSyncClient())
    now = datetime.now(UTC)
    with pytest.raises(ValidationError, match="kind"):
        client.record_annotation(
            kind=PlatformAnnotationKindV1.PLATFORM_ANNOTATION_KIND_V1_UNSPECIFIED,
            title="deploy",
            start_at=now,
            idempotency_key="k1",
        )
    with pytest.raises(ValidationError, match="title"):
        client.record_annotation(
            kind=PlatformAnnotationKindV1.PLATFORM_ANNOTATION_KIND_V1_DEPLOYMENT,
            title="",
            start_at=now,
            idempotency_key="k1",
        )
    with pytest.raises(ValidationError, match="idempotency_key"):
        client.record_annotation(
            kind=PlatformAnnotationKindV1.PLATFORM_ANNOTATION_KIND_V1_DEPLOYMENT,
            title="deploy",
            start_at=now,
            idempotency_key="",
        )


def test_record_annotation_builds_attributes_and_links() -> None:
    fake = FakeSyncClient(record_platform_annotation=lambda req: req)
    client = AgenticClientSync(fake)
    now = datetime.now(UTC)
    client.record_annotation(
        kind=PlatformAnnotationKindV1.PLATFORM_ANNOTATION_KIND_V1_DEPLOYMENT,
        title="deploy v42",
        start_at=now,
        idempotency_key="k1",
        attributes={"service": "api"},
    )
    _, sent = fake.calls[0]
    assert sent.title == "deploy v42"
    assert sent.attributes[0].key == "service"
    assert sent.attributes[0].value == "api"


# --------------------------------------------------------------------------
# fixture-replay: decode canned response bytes through the real decoders
# --------------------------------------------------------------------------


def test_fixture_replay_lease_refusal_response_bytes() -> None:
    """Round-trips a LeaseEvaluationCasesResponse through wire bytes, then
    through the same decoder the facade uses, exactly as if it had come off
    the transport."""
    refusal = ExternalLeaseRefusalV1(
        kind=ExternalLeaseRefusalKindV1.EXTERNAL_LEASE_REFUSAL_KIND_V1_RENEWAL_BUDGET_EXHAUSTED,
        message="renewal budget exhausted",
        missing_scope="",
    )
    wire = LeaseEvaluationCasesResponse(refusal=refusal).SerializeToString()

    decoded = LeaseEvaluationCasesResponse.FromString(wire)
    fake = FakeSyncClient(lease_evaluation_cases=decoded)
    client = AgenticClientSync(fake)
    result = client.lease_cases(evaluation_run_id="run_1", candidate_key="c1", runtime_key="rt1")

    assert isinstance(result, Refusal)
    assert result.reason_code == "RENEWAL_BUDGET_EXHAUSTED"
    assert result.missing_scope is None


def test_fixture_replay_issued_credential_response_bytes() -> None:
    credential = MachineCredentialV1(credential_id="cred_9", token_prefix="o11y_mach.ZZZZ")
    wire = CreateMachineCredentialResponse(
        credential=credential, plaintext_token_once="o11y_mach.ZZZZ.SECRET"
    ).SerializeToString()

    decoded = CreateMachineCredentialResponse.FromString(wire)
    fake = FakeSyncClient(create_machine_credential=decoded)
    client = AgenticClientSync(fake)
    issued = client.create_machine_credential(machine_principal_id="mp_1")

    assert issued.credential_id == "cred_9"
    assert issued.one_time_token == "o11y_mach.ZZZZ.SECRET"


def test_fixture_replay_annotation_timestamp_roundtrip() -> None:
    ts = timestamp_pb2.Timestamp()
    ts.FromDatetime(datetime(2026, 8, 31, 12, 0, tzinfo=UTC))
    fake = FakeSyncClient(record_platform_annotation=lambda req: req)
    client = AgenticClientSync(fake)
    client.record_annotation(
        kind=PlatformAnnotationKindV1.PLATFORM_ANNOTATION_KIND_V1_MARKER,
        title="canary start",
        start_at=ts.ToDatetime(tzinfo=UTC),
        idempotency_key="k1",
    )
    _, sent = fake.calls[0]
    wire = sent.SerializeToString()
    from o11y_one.agentic.v1.evaluation_pb2 import RecordPlatformAnnotationRequest

    roundtripped = RecordPlatformAnnotationRequest.FromString(wire)
    assert roundtripped.title == "canary start"
    assert roundtripped.start_at.ToDatetime(tzinfo=UTC).year == 2026


# --------------------------------------------------------------------------
# async facade parity — same builders/decoders, awaited instead of called
# --------------------------------------------------------------------------


def test_async_facade_whoami_and_lease_refusal() -> None:
    caller = PrincipalRefV1(kind=PrincipalKindV1.PRINCIPAL_KIND_V1_MACHINE, principal_id="mp_1")
    refusal = ExternalLeaseRefusalV1(
        kind=ExternalLeaseRefusalKindV1.EXTERNAL_LEASE_REFUSAL_KIND_V1_LEASE_EXPIRED,
        message="expired",
    )
    fake = FakeAsyncClient(
        get_caller_principal=GetCallerPrincipalResponse(caller=caller, tenant_id="t1"),
        lease_evaluation_cases=LeaseEvaluationCasesResponse(refusal=refusal),
    )
    client = AgenticClient(fake)

    async def run() -> None:
        who = await client.whoami()
        assert who.tenant_id == "t1"
        result = await client.lease_cases(
            evaluation_run_id="r1", candidate_key="c1", runtime_key="rt1"
        )
        assert isinstance(result, Refusal)
        assert result.reason_code == "LEASE_EXPIRED"

    asyncio.run(run())


def test_async_facade_validates_before_awaiting_transport() -> None:
    client = AgenticClient(FakeAsyncClient())

    async def run() -> None:
        with pytest.raises(ValidationError, match="definition_id"):
            await client.create_run(definition_id="", idempotency_key="k1")

    asyncio.run(run())
