"""Ergonomic facade over ``AgenticEvaluationServiceClient`` / ``...ClientSync``.

This is the one generated client this SDK wraps with convenience methods
rather than leaving callers to import ``o11y_one.agentic.v1.evaluation_connect``
directly (see :mod:`o11y_one.sdk.client` for why the SDK otherwise stays thin).
The exception is deliberate: this surface is what an eval-authoring or
externally-executed runtime integration actually calls minute to minute, its
messages are large and its refusal/idempotency/capability conventions repeat
across dozens of RPCs, and getting any one of those conventions wrong locally
degrades to an opaque network error. What this module adds, RPC by RPC:

* input validation BEFORE the wire call (:mod:`o11y_one.sdk.validation`);
* BOTH refusal-delivery channels folded into the same ``T | Refusal`` shape
  (:mod:`o11y_one.sdk.results`, :mod:`o11y_one.sdk.recovery`): a refusal field
  on an otherwise-successful response (the externally-executed lease loop),
  and a typed detail packed onto a thrown ``ConnectError`` (run launch,
  dataset case capture, dataset version publish, platform annotations) — a
  caller checks ``isinstance(result, Refusal)`` once, never a ``HasField``
  here and a ``try/except`` there;
* the one-time machine credential token kept on its own type
  (:class:`IssuedMachineCredential`) so it cannot be echoed back accidentally
  by logging a generic response object.

Everything else — pagination shape, field names, enum discriminants — passes
through unchanged from the generated messages. This module does not re-derive
or duplicate them.

Every method exists in two forms: an ``async def`` on :class:`AgenticClient`
(wrapping ``AgenticEvaluationServiceClient``) and a plain ``def`` on
:class:`AgenticClientSync` (wrapping ``AgenticEvaluationServiceClientSync``),
mirroring the sync/async split :class:`o11y_one.sdk.client.O11yClient` already
exposes via ``service()`` / ``service_sync()``. The request-building,
validation and response-decoding logic is shared as module-level functions so
the two classes cannot drift from each other.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime

from connectrpc.errors import ConnectError
from connectrpc.request import Headers
from o11y_one.agentic.v1.evaluation_connect import (
    AgenticEvaluationServiceClient,
    AgenticEvaluationServiceClientSync,
)
from o11y_one.agentic.v1.evaluation_pb2 import (
    ApproveDatasetCaseDraftRequest,
    ApproveDatasetCaseDraftResponse,
    CaptureEvaluationCaseRequest,
    CaptureEvaluationCaseResponse,
    CreateEvaluationRunRequest,
    CreateEvaluationRunResponse,
    CreateMachineCredentialRequest,
    CreateMachinePrincipalRequest,
    DatasetCaseDraftRejectionReasonV1,
    DatasetFieldMappingV1,
    EvaluationCaptureCellSourceV1,
    EvaluationCaptureRefusalKindV1,
    EvaluationCaptureRefusalV1,
    EvaluationCaptureSpanSourceV1,
    EvaluationCellRefV1,
    EvaluationDatasetVersionRejectionKindV1,
    EvaluationDatasetVersionRejectionV1,
    EvaluationLaunchRejectionKindV1,
    EvaluationLaunchRejectionV1,
    ExternalCaseFailureV1,
    ExternalCaseOutputV1,
    ExternalCaseUsageV1,
    ExternalLeaseRefusalKindV1,
    GetCallerPrincipalRequest,
    GetCallerPrincipalResponse,
    LeaseEvaluationCasesRequest,
    LeaseEvaluationCasesResponse,
    ListMachinePrincipalsRequest,
    ListMachinePrincipalsResponse,
    ListPlatformAnnotationsRequest,
    MachinePrincipalScopeV1,
    MergeDatasetCaseDraftRequest,
    MergeDatasetCaseDraftResponse,
    PlatformAnnotationAttributeV1,
    PlatformAnnotationKindV1,
    PlatformAnnotationLinkV1,
    PlatformAnnotationRejectionReasonV1,
    PlatformAnnotationRejectionV1,
    PreviewEvaluationRunRequest,
    PreviewEvaluationRunResponse,
    PreviewPublishDatasetChangesetRequest,
    PreviewPublishDatasetChangesetResponse,
    PublishDatasetCaseDraftsRequest,
    PublishDatasetCaseDraftsResponse,
    RecordPlatformAnnotationRequest,
    RecordPlatformAnnotationResponse,
    RejectDatasetCaseDraftRequest,
    RejectDatasetCaseDraftResponse,
    ReleaseEvaluationCaseLeaseRequest,
    ReleaseEvaluationCaseLeaseResponse,
    RenewEvaluationCaseLeaseRequest,
    RenewEvaluationCaseLeaseResponse,
    RevokeMachineCredentialRequest,
    RevokeMachineCredentialResponse,
    RevokeMachinePrincipalRequest,
    RevokeMachinePrincipalResponse,
    SubmitEvaluationCaseOutputsRequest,
    SubmitEvaluationCaseOutputsResponse,
    UpdateDatasetCaseDraftRequest,
    UpdateDatasetCaseDraftResponse,
)
from o11y_one.common.v1.common_pb2 import PageRequestV1

from .errors import MACHINE_SCOPES as _MACHINE_SCOPE_STRINGS
from .recovery import bare_enum_name, find_error_detail
from .results import Refusal
from .validation import (
    ValidationError,
    require_exactly_one,
    require_non_empty,
    require_non_empty_sequence,
    require_not_unspecified,
    require_valid_enum_choices,
)

__all__ = [
    "AgenticClient",
    "AgenticClientSync",
    "CaseOutput",
    "IssuedMachineCredential",
    "MACHINE_SCOPE_NAME_TO_ENUM",
    "ValidationError",
]

# --------------------------------------------------------------------------
# Scope strings: reuse the canonical names errors.MACHINE_SCOPES already
# freezes, mapped onto the wire enum, so callers write "eval:read" and never
# have to import the generated enum directly.
# --------------------------------------------------------------------------

MACHINE_SCOPE_NAME_TO_ENUM: dict[str, MachinePrincipalScopeV1] = {
    "eval:read": MachinePrincipalScopeV1.MACHINE_PRINCIPAL_SCOPE_V1_EVAL_READ,
    "run:execute": MachinePrincipalScopeV1.MACHINE_PRINCIPAL_SCOPE_V1_RUN_EXECUTE,
    "dataset:write": MachinePrincipalScopeV1.MACHINE_PRINCIPAL_SCOPE_V1_DATASET_WRITE,
    "lease:submit": MachinePrincipalScopeV1.MACHINE_PRINCIPAL_SCOPE_V1_LEASE_SUBMIT,
    "platform-annotation:write": (
        MachinePrincipalScopeV1.MACHINE_PRINCIPAL_SCOPE_V1_PLATFORM_ANNOTATION_WRITE
    ),
}
assert set(MACHINE_SCOPE_NAME_TO_ENUM) == set(_MACHINE_SCOPE_STRINGS)
_VALID_SCOPE_DISCRIMINANTS = frozenset(MACHINE_SCOPE_NAME_TO_ENUM.values())


def _scopes_to_enum(scopes: Iterable[str], *, field: str) -> list[MachinePrincipalScopeV1]:
    try:
        values = [MACHINE_SCOPE_NAME_TO_ENUM[s] for s in scopes]
    except KeyError as exc:
        raise ValidationError(field, f"unknown scope name: {exc.args[0]!r}") from None
    return require_valid_enum_choices(values, field=field, valid=_VALID_SCOPE_DISCRIMINANTS)


@dataclass(frozen=True, slots=True)
class IssuedMachineCredential:
    """The response to a credential creation, kept apart from every later read.

    ``one_time_token`` is the ONLY place the plaintext credential ever appears
    (proto comment on ``CreateMachineCredentialResponse.plaintext_token_once``:
    "returned exactly once ... with no read-back RPC and no recovery path").
    Keeping it on its own dataclass rather than folding it into the generic
    ``MachineCredentialV1`` resource means a caller cannot accidentally forward
    it by logging or serializing the resource they'd normally hold onto.
    """

    credential_id: str
    token_prefix: str
    one_time_token: str


@dataclass(frozen=True, slots=True)
class CaseOutput:
    """One case's result for :meth:`AgenticClientSync.submit_case_outputs`.

    Exactly one of ``output_payload_json`` / ``failure_code`` must be set —
    the same ``oneof`` the wire message enforces
    (``ExternalCaseOutputV1.result``), checked here before the batch is built
    so a malformed element is caught locally rather than surfacing as one
    opaque per-case rejection among fifty.
    """

    cohort_key: str
    candidate_key: str
    case_revision_id: str
    trial: int
    attempt_generation: int = 0
    output_payload_json: str | None = None
    failure_code: str | None = None
    failure_message: str | None = None
    input_tokens: int | None = None
    output_tokens: int | None = None
    latency_micros: int | None = None
    retry_count: int | None = None


def _build_case_output(case: CaseOutput) -> ExternalCaseOutputV1:
    require_non_empty(case.cohort_key, field="cohort_key")
    require_non_empty(case.candidate_key, field="candidate_key")
    require_non_empty(case.case_revision_id, field="case_revision_id")
    require_exactly_one(
        {"output_payload_json": case.output_payload_json, "failure_code": case.failure_code},
        oneof="output_payload_json | failure_code",
    )
    kwargs: dict[str, object] = {
        "cohort_key": case.cohort_key,
        "candidate_key": case.candidate_key,
        "case_revision_id": case.case_revision_id,
        "trial": case.trial,
        "attempt_generation": case.attempt_generation,
    }
    if case.output_payload_json is not None:
        kwargs["output_payload_json"] = case.output_payload_json
    else:
        kwargs["failure"] = ExternalCaseFailureV1(
            code=require_non_empty(case.failure_code, field="failure_code"),
            sanitized_message=case.failure_message or "",
        )
    if (
        case.input_tokens is not None
        or case.output_tokens is not None
        or case.latency_micros is not None
    ):
        kwargs["usage"] = ExternalCaseUsageV1(
            input_tokens=case.input_tokens,
            output_tokens=case.output_tokens,
            latency_micros=case.latency_micros,
            retry_count=case.retry_count,
        )
    return ExternalCaseOutputV1(**kwargs)


# --------------------------------------------------------------------------
# Request builders + response decoders (transport-agnostic; shared by both
# the sync and the async facade below).
# --------------------------------------------------------------------------


def _build_create_machine_principal(
    *, display_name: str, scopes: Iterable[str], description: str | None
) -> CreateMachinePrincipalRequest:
    require_non_empty(display_name, field="display_name")
    scope_values = _scopes_to_enum(scopes, field="scopes")
    return CreateMachinePrincipalRequest(
        display_name=display_name, description=description or None, scopes=scope_values
    )


def _build_create_machine_credential(
    *,
    machine_principal_id: str,
    description: str | None,
    expires_at: datetime | None,
) -> CreateMachineCredentialRequest:
    require_non_empty(machine_principal_id, field="machine_principal_id")
    return CreateMachineCredentialRequest(
        machine_principal_id=machine_principal_id,
        description=description or None,
        expires_at=expires_at,
    )


def _decode_issued_credential(resp: object) -> IssuedMachineCredential:
    credential = resp.credential  # type: ignore[attr-defined]
    return IssuedMachineCredential(
        credential_id=credential.credential_id,
        token_prefix=credential.token_prefix,
        one_time_token=resp.plaintext_token_once,  # type: ignore[attr-defined]
    )


def _build_revoke_machine_credential(
    *, credential_id: str, reason: str | None
) -> RevokeMachineCredentialRequest:
    require_non_empty(credential_id, field="credential_id")
    return RevokeMachineCredentialRequest(credential_id=credential_id, revoke_reason=reason or None)


def _build_revoke_machine_principal(
    *, machine_principal_id: str, reason: str | None
) -> RevokeMachinePrincipalRequest:
    require_non_empty(machine_principal_id, field="machine_principal_id")
    return RevokeMachinePrincipalRequest(
        machine_principal_id=machine_principal_id, revoke_reason=reason or None
    )


def _build_list_machine_principals(
    *, page_size: int | None, page_token: str | None
) -> ListMachinePrincipalsRequest:
    return ListMachinePrincipalsRequest(page_size=page_size, page_token=page_token or None)


def _build_preview_run(
    *, definition_id: str, revision_id: str | None
) -> PreviewEvaluationRunRequest:
    require_non_empty(definition_id, field="definition_id")
    return PreviewEvaluationRunRequest(definition_id=definition_id, revision_id=revision_id or None)


def _build_create_run(
    *, definition_id: str, idempotency_key: str, preview_token: str | None
) -> CreateEvaluationRunRequest:
    require_non_empty(definition_id, field="definition_id")
    require_non_empty(idempotency_key, field="idempotency_key")
    return CreateEvaluationRunRequest(
        definition_id=definition_id,
        idempotency_key=idempotency_key,
        preview_token=preview_token or None,
    )


def _build_lease_request(
    *,
    evaluation_run_id: str,
    candidate_key: str,
    runtime_key: str,
    max_cases: int,
    lease_seconds: int,
) -> LeaseEvaluationCasesRequest:
    require_non_empty(evaluation_run_id, field="evaluation_run_id")
    require_non_empty(candidate_key, field="candidate_key")
    require_non_empty(runtime_key, field="runtime_key")
    if max_cases < 0:
        raise ValidationError("max_cases", "must not be negative")
    if lease_seconds < 0:
        raise ValidationError("lease_seconds", "must not be negative")
    return LeaseEvaluationCasesRequest(
        evaluation_run_id=evaluation_run_id,
        candidate_key=candidate_key,
        runtime_key=runtime_key,
        max_cases=max_cases,
        lease_seconds=lease_seconds,
    )


def _decode_lease_response(
    resp: LeaseEvaluationCasesResponse,
) -> LeaseEvaluationCasesResponse | Refusal:
    if resp.HasField("refusal"):
        return _refusal_from_lease(resp.refusal, state_field="lease")
    return resp


def _build_renew_request(
    *, evaluation_run_id: str, lease_id: str, lease_token: str, lease_seconds: int
) -> RenewEvaluationCaseLeaseRequest:
    require_non_empty(evaluation_run_id, field="evaluation_run_id")
    require_non_empty(lease_id, field="lease_id")
    require_non_empty(lease_token, field="lease_token")
    if lease_seconds < 0:
        raise ValidationError("lease_seconds", "must not be negative")
    return RenewEvaluationCaseLeaseRequest(
        evaluation_run_id=evaluation_run_id,
        lease_id=lease_id,
        lease_token=lease_token,
        lease_seconds=lease_seconds,
    )


def _decode_renew_response(
    resp: RenewEvaluationCaseLeaseResponse,
) -> RenewEvaluationCaseLeaseResponse | Refusal:
    if resp.HasField("refusal"):
        return _refusal_from_lease(resp.refusal, state_field="lease")
    return resp


def _build_submit_outputs_request(
    *,
    evaluation_run_id: str,
    lease_id: str,
    lease_token: str,
    outputs: Sequence[CaseOutput],
    idempotency_key: str,
) -> SubmitEvaluationCaseOutputsRequest:
    require_non_empty(evaluation_run_id, field="evaluation_run_id")
    require_non_empty(lease_id, field="lease_id")
    require_non_empty(lease_token, field="lease_token")
    require_non_empty(idempotency_key, field="idempotency_key")
    require_non_empty_sequence(outputs, field="outputs")
    return SubmitEvaluationCaseOutputsRequest(
        evaluation_run_id=evaluation_run_id,
        lease_id=lease_id,
        lease_token=lease_token,
        outputs=[_build_case_output(c) for c in outputs],
        idempotency_key=idempotency_key,
    )


def _decode_submit_response(
    resp: SubmitEvaluationCaseOutputsResponse,
) -> SubmitEvaluationCaseOutputsResponse | Refusal:
    if resp.HasField("refusal"):
        return _refusal_from_lease(resp.refusal, state_field="outputs")
    return resp


def _build_release_request(
    *, evaluation_run_id: str, lease_id: str, lease_token: str
) -> ReleaseEvaluationCaseLeaseRequest:
    require_non_empty(evaluation_run_id, field="evaluation_run_id")
    require_non_empty(lease_id, field="lease_id")
    require_non_empty(lease_token, field="lease_token")
    return ReleaseEvaluationCaseLeaseRequest(
        evaluation_run_id=evaluation_run_id, lease_id=lease_id, lease_token=lease_token
    )


def _decode_release_response(
    resp: ReleaseEvaluationCaseLeaseResponse,
) -> ReleaseEvaluationCaseLeaseResponse | Refusal:
    if resp.HasField("refusal"):
        return _refusal_from_lease(resp.refusal, state_field="lease")
    return resp


def _refusal_from_lease(refusal, *, state_field: str) -> Refusal:
    return Refusal(
        reason_code=bare_enum_name(ExternalLeaseRefusalKindV1, refusal.kind),
        field=state_field,
        message=refusal.message,
        missing_scope=refusal.missing_scope or None,
    )


def _refusal_from_launch_rejection(detail: EvaluationLaunchRejectionV1) -> Refusal:
    return Refusal(
        reason_code=bare_enum_name(EvaluationLaunchRejectionKindV1, detail.kind),
        field="preview_token",
        message=detail.detail or "run launch rejected",
    )


def _refusal_from_capture_refusal(detail: EvaluationCaptureRefusalV1) -> Refusal:
    return Refusal(
        reason_code=bare_enum_name(EvaluationCaptureRefusalKindV1, detail.kind),
        field="source",
        message=detail.detail or "case capture refused",
    )


def _refusal_from_dataset_version_rejection(detail: EvaluationDatasetVersionRejectionV1) -> Refusal:
    return Refusal(
        reason_code=bare_enum_name(EvaluationDatasetVersionRejectionKindV1, detail.kind),
        field="changeset_id",
        message=detail.reason_code or "dataset version publish rejected",
    )


def _refusal_from_annotation_rejection(detail: PlatformAnnotationRejectionV1) -> Refusal:
    return Refusal(
        reason_code=bare_enum_name(PlatformAnnotationRejectionReasonV1, detail.reason),
        field=detail.field or None,
        message="platform annotation rejected",
    )


def _build_capture_case(
    *,
    dataset_collection_id: str,
    draft_id: str | None,
    trace_id: bytes | None,
    span_id: bytes | None,
    evaluation_run_id: str | None,
    cell: EvaluationCellRefV1 | None,
    field_mappings: Mapping[str, str],
    recorded_output_field_path: str | None,
    idempotency_key: str,
) -> CaptureEvaluationCaseRequest:
    require_non_empty(dataset_collection_id, field="dataset_collection_id")
    require_non_empty(idempotency_key, field="idempotency_key")
    is_span = trace_id is not None or span_id is not None
    is_cell = evaluation_run_id is not None or cell is not None
    require_exactly_one({"span": is_span or None, "cell": is_cell or None}, oneof="span | cell")
    kwargs: dict[str, object] = {
        "dataset_collection_id": dataset_collection_id,
        "draft_id": draft_id or None,
        "field_mappings": [
            DatasetFieldMappingV1(source_field=src, target_field=dst)
            for src, dst in field_mappings.items()
        ],
        "recorded_output_field_path": recorded_output_field_path or None,
        "idempotency_key": idempotency_key,
    }
    if is_span:
        kwargs["span"] = EvaluationCaptureSpanSourceV1(trace_id=trace_id, span_id=span_id)
    else:
        require_non_empty(evaluation_run_id, field="evaluation_run_id")
        if cell is None:
            raise ValidationError("cell", "is required when evaluation_run_id is set")
        kwargs["cell"] = EvaluationCaptureCellSourceV1(
            evaluation_run_id=evaluation_run_id, cell=cell
        )
    return CaptureEvaluationCaseRequest(**kwargs)


def _build_update_case_draft(
    *,
    proposed_case_id: str,
    expected_draft_version: int,
    expected_output_json: str | None,
    expected_output_absence_reason: str | None,
    correction_payload_json: str | None,
    needs_ground_truth: bool,
    idempotency_key: str,
) -> UpdateDatasetCaseDraftRequest:
    require_non_empty(proposed_case_id, field="proposed_case_id")
    require_non_empty(idempotency_key, field="idempotency_key")
    # "Setting this clears the absence; clearing it requires a typed reason"
    # (evaluation.proto, UpdateDatasetCaseDraftRequest) — a caller cannot send
    # both a value and an absence reason for the same field in the same call.
    if expected_output_json is not None and expected_output_absence_reason is not None:
        raise ValidationError(
            "expected_output_json | expected_output_absence_reason",
            "at most one of these may be set in the same update",
        )
    return UpdateDatasetCaseDraftRequest(
        proposed_case_id=proposed_case_id,
        expected_draft_version=expected_draft_version,
        expected_output_json=expected_output_json,
        expected_output_absence_reason=expected_output_absence_reason,
        correction_payload_json=correction_payload_json,
        needs_ground_truth=needs_ground_truth,
        idempotency_key=idempotency_key,
    )


def _build_approve_case_draft(
    *, proposed_case_id: str, expected_draft_version: int, note: str | None, idempotency_key: str
) -> ApproveDatasetCaseDraftRequest:
    require_non_empty(proposed_case_id, field="proposed_case_id")
    require_non_empty(idempotency_key, field="idempotency_key")
    return ApproveDatasetCaseDraftRequest(
        proposed_case_id=proposed_case_id,
        expected_draft_version=expected_draft_version,
        note=note or None,
        idempotency_key=idempotency_key,
    )


def _build_reject_case_draft(
    *,
    proposed_case_id: str,
    expected_draft_version: int,
    reason: DatasetCaseDraftRejectionReasonV1,
    note: str | None,
    idempotency_key: str,
) -> RejectDatasetCaseDraftRequest:
    require_non_empty(proposed_case_id, field="proposed_case_id")
    require_non_empty(idempotency_key, field="idempotency_key")
    require_not_unspecified(reason, field="reason")
    return RejectDatasetCaseDraftRequest(
        proposed_case_id=proposed_case_id,
        expected_draft_version=expected_draft_version,
        reason=reason,
        note=note or None,
        idempotency_key=idempotency_key,
    )


def _build_merge_case_draft(
    *,
    proposed_case_id: str,
    expected_draft_version: int,
    target_case_revision_id: str,
    note: str | None,
    idempotency_key: str,
) -> MergeDatasetCaseDraftRequest:
    require_non_empty(proposed_case_id, field="proposed_case_id")
    require_non_empty(target_case_revision_id, field="target_case_revision_id")
    require_non_empty(idempotency_key, field="idempotency_key")
    return MergeDatasetCaseDraftRequest(
        proposed_case_id=proposed_case_id,
        expected_draft_version=expected_draft_version,
        target_case_revision_id=target_case_revision_id,
        note=note or None,
        idempotency_key=idempotency_key,
    )


def _build_preview_publish(*, changeset_id: str) -> PreviewPublishDatasetChangesetRequest:
    require_non_empty(changeset_id, field="changeset_id")
    return PreviewPublishDatasetChangesetRequest(changeset_id=changeset_id)


def _build_publish_case_drafts(
    *, changeset_id: str, preview_digest: str, label: str | None, idempotency_key: str
) -> PublishDatasetCaseDraftsRequest:
    require_non_empty(changeset_id, field="changeset_id")
    require_non_empty(preview_digest, field="preview_digest")
    require_non_empty(idempotency_key, field="idempotency_key")
    return PublishDatasetCaseDraftsRequest(
        changeset_id=changeset_id,
        preview_digest=preview_digest,
        label=label or None,
        idempotency_key=idempotency_key,
    )


def _build_record_annotation(
    *,
    kind: PlatformAnnotationKindV1,
    title: str,
    start_at: datetime,
    end_at: datetime | None,
    attributes: Mapping[str, str],
    links: Sequence[tuple[int, str]],
    idempotency_key: str,
) -> RecordPlatformAnnotationRequest:
    require_not_unspecified(kind, field="kind")
    require_non_empty(title, field="title")
    require_non_empty(idempotency_key, field="idempotency_key")
    return RecordPlatformAnnotationRequest(
        kind=kind,
        title=title,
        start_at=start_at,
        end_at=end_at,
        attributes=[PlatformAnnotationAttributeV1(key=k, value=v) for k, v in attributes.items()],
        links=[PlatformAnnotationLinkV1(kind=link_kind, ref=ref) for link_kind, ref in links],
        idempotency_key=idempotency_key,
    )


def _build_list_annotations(
    *,
    window_start: datetime | None,
    window_end: datetime | None,
    kinds: Iterable[PlatformAnnotationKindV1],
    page: PageRequestV1 | None,
) -> ListPlatformAnnotationsRequest:
    return ListPlatformAnnotationsRequest(
        window_start=window_start, window_end=window_end, kinds=list(kinds), page=page
    )


# --------------------------------------------------------------------------
# Async facade
# --------------------------------------------------------------------------


class AgenticClient:
    """Async ergonomic facade.

    Construct via ``O11yClient.service(AgenticEvaluationServiceClient)``.
    """

    __slots__ = ("_client",)

    def __init__(self, client: AgenticEvaluationServiceClient) -> None:
        self._client = client

    async def whoami(
        self, *, headers: Headers | None = None, timeout_ms: int | None = None
    ) -> GetCallerPrincipalResponse:
        """Introspect the caller: which principal, which credential, which org/tenant.

        Raises the classified auth exception (see :mod:`o11y_one.sdk.errors`)
        if the credential itself is invalid — this call never returns a
        refusal-on-200, because there is no "caller" to attach one to until
        the credential resolves to one.
        """
        return await self._client.get_caller_principal(
            GetCallerPrincipalRequest(), headers=headers, timeout_ms=timeout_ms
        )

    async def create_machine_principal(
        self,
        *,
        display_name: str,
        scopes: Iterable[str] = (),
        description: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ):
        req = _build_create_machine_principal(
            display_name=display_name, scopes=scopes, description=description
        )
        return await self._client.create_machine_principal(
            req, headers=headers, timeout_ms=timeout_ms
        )

    async def list_machine_principals(
        self,
        *,
        page_size: int | None = None,
        page_token: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> ListMachinePrincipalsResponse:
        req = _build_list_machine_principals(page_size=page_size, page_token=page_token)
        return await self._client.list_machine_principals(
            req, headers=headers, timeout_ms=timeout_ms
        )

    async def create_machine_credential(
        self,
        *,
        machine_principal_id: str,
        description: str | None = None,
        expires_at: datetime | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> IssuedMachineCredential:
        req = _build_create_machine_credential(
            machine_principal_id=machine_principal_id,
            description=description,
            expires_at=expires_at,
        )
        resp = await self._client.create_machine_credential(
            req, headers=headers, timeout_ms=timeout_ms
        )
        return _decode_issued_credential(resp)

    async def revoke_machine_credential(
        self,
        *,
        credential_id: str,
        reason: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> RevokeMachineCredentialResponse:
        req = _build_revoke_machine_credential(credential_id=credential_id, reason=reason)
        return await self._client.revoke_machine_credential(
            req, headers=headers, timeout_ms=timeout_ms
        )

    async def revoke_machine_principal(
        self,
        *,
        machine_principal_id: str,
        reason: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> RevokeMachinePrincipalResponse:
        req = _build_revoke_machine_principal(
            machine_principal_id=machine_principal_id, reason=reason
        )
        return await self._client.revoke_machine_principal(
            req, headers=headers, timeout_ms=timeout_ms
        )

    async def preview_run(
        self,
        *,
        definition_id: str,
        revision_id: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> PreviewEvaluationRunResponse:
        req = _build_preview_run(definition_id=definition_id, revision_id=revision_id)
        return await self._client.preview_evaluation_run(
            req, headers=headers, timeout_ms=timeout_ms
        )

    async def create_run(
        self,
        *,
        definition_id: str,
        idempotency_key: str,
        preview_token: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> CreateEvaluationRunResponse | Refusal:
        """Submit a run.

        A run always references a definition by id (there is no "inline
        draft" launch path on this generated surface — see ``l2-notes.md``
        for why this diverges from the abstract "definition rev XOR inline
        draft" framing). ``preview_token`` is optional: omit it to launch the
        definition's current published revision directly, or pass the token a
        prior :meth:`preview_run` returned to launch exactly what was
        previewed (the server pins the previewed revision and estimates to
        that token; passing it is how a caller gets a launch that matches what
        it showed a human before submitting).

        A launch rejection (stale preview, moved dependency versions, a reused
        idempotency key against a different preview, ...) arrives as a typed
        ``EvaluationLaunchRejectionV1`` detail on a thrown ``ConnectError``
        rather than a response field — see :mod:`o11y_one.sdk.recovery`. This
        method decodes that detail and returns a :class:`Refusal` instead of
        letting the raw error propagate; any other exception still raises.
        """
        req = _build_create_run(
            definition_id=definition_id,
            idempotency_key=idempotency_key,
            preview_token=preview_token,
        )
        try:
            return await self._client.create_evaluation_run(
                req, headers=headers, timeout_ms=timeout_ms
            )
        except ConnectError as err:
            detail = find_error_detail(err, EvaluationLaunchRejectionV1)
            if detail is None:
                raise
            return _refusal_from_launch_rejection(detail)

    async def lease_cases(
        self,
        *,
        evaluation_run_id: str,
        candidate_key: str,
        runtime_key: str,
        max_cases: int = 0,
        lease_seconds: int = 0,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> LeaseEvaluationCasesResponse | Refusal:
        req = _build_lease_request(
            evaluation_run_id=evaluation_run_id,
            candidate_key=candidate_key,
            runtime_key=runtime_key,
            max_cases=max_cases,
            lease_seconds=lease_seconds,
        )
        resp = await self._client.lease_evaluation_cases(
            req, headers=headers, timeout_ms=timeout_ms
        )
        return _decode_lease_response(resp)

    async def renew_lease(
        self,
        *,
        evaluation_run_id: str,
        lease_id: str,
        lease_token: str,
        lease_seconds: int = 0,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> RenewEvaluationCaseLeaseResponse | Refusal:
        """Heartbeat: extend a held lease's expiry before it lapses."""
        req = _build_renew_request(
            evaluation_run_id=evaluation_run_id,
            lease_id=lease_id,
            lease_token=lease_token,
            lease_seconds=lease_seconds,
        )
        resp = await self._client.renew_evaluation_case_lease(
            req, headers=headers, timeout_ms=timeout_ms
        )
        return _decode_renew_response(resp)

    async def submit_case_outputs(
        self,
        *,
        evaluation_run_id: str,
        lease_id: str,
        lease_token: str,
        outputs: Sequence[CaseOutput],
        idempotency_key: str,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> SubmitEvaluationCaseOutputsResponse | Refusal:
        """Submit a batch of case results under a held lease.

        A rejected element never fails the batch (proto: "the other forty-nine
        land"): inspect ``response.acks`` for the per-case
        accepted/already-submitted/rejected outcome. A whole-batch
        :class:`~o11y_one.sdk.results.Refusal` means the fence itself was
        lost — its ``reason_code`` is the bare ``ExternalLeaseRefusalKindV1``
        member name (see :mod:`o11y_one.sdk.recovery`).
        """
        req = _build_submit_outputs_request(
            evaluation_run_id=evaluation_run_id,
            lease_id=lease_id,
            lease_token=lease_token,
            outputs=outputs,
            idempotency_key=idempotency_key,
        )
        resp = await self._client.submit_evaluation_case_outputs(
            req, headers=headers, timeout_ms=timeout_ms
        )
        return _decode_submit_response(resp)

    async def release_lease(
        self,
        *,
        evaluation_run_id: str,
        lease_id: str,
        lease_token: str,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> ReleaseEvaluationCaseLeaseResponse | Refusal:
        req = _build_release_request(
            evaluation_run_id=evaluation_run_id, lease_id=lease_id, lease_token=lease_token
        )
        resp = await self._client.release_evaluation_case_lease(
            req, headers=headers, timeout_ms=timeout_ms
        )
        return _decode_release_response(resp)

    async def submit_recorded_outputs(
        self,
        *,
        evaluation_run_id: str,
        candidate_key: str,
        runtime_key: str,
        outputs: Sequence[CaseOutput],
        idempotency_key: str,
        lease_seconds: int = 0,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> SubmitEvaluationCaseOutputsResponse | Refusal:
        """Batched submit for a candidate whose outputs already exist.

        Convenience over the four lease primitives for the case where there is
        nothing to heartbeat: the caller already has every output in hand
        (``EVALUATION_CANDIDATE_KIND_V1_RECORDED_OUTPUT``), so this leases
        exactly ``len(outputs)`` cases, submits the whole batch in one
        idempotent call, and releases the lease — three RPCs behind one call.
        Use :meth:`lease_cases` / :meth:`renew_lease` / :meth:`submit_case_outputs`
        / :meth:`release_lease` directly for the externally-executed journey,
        where work is produced incrementally and needs heartbeating.
        """
        require_non_empty_sequence(outputs, field="outputs")
        leased = await self.lease_cases(
            evaluation_run_id=evaluation_run_id,
            candidate_key=candidate_key,
            runtime_key=runtime_key,
            max_cases=len(outputs),
            lease_seconds=lease_seconds,
        )
        if isinstance(leased, Refusal):
            return leased
        lease = leased.lease
        try:
            return await self.submit_case_outputs(
                evaluation_run_id=evaluation_run_id,
                lease_id=lease.lease_id,
                lease_token=lease.lease_token,
                outputs=outputs,
                idempotency_key=idempotency_key,
            )
        finally:
            await self.release_lease(
                evaluation_run_id=evaluation_run_id,
                lease_id=lease.lease_id,
                lease_token=lease.lease_token,
            )

    async def capture_case_draft(
        self,
        *,
        dataset_collection_id: str,
        idempotency_key: str,
        draft_id: str | None = None,
        trace_id: bytes | None = None,
        span_id: bytes | None = None,
        evaluation_run_id: str | None = None,
        cell: EvaluationCellRefV1 | None = None,
        field_mappings: Mapping[str, str] = {},
        recorded_output_field_path: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> CaptureEvaluationCaseResponse | Refusal:
        """Create a dataset case draft from a span or an evaluation cell.

        Exactly one source must be given: ``trace_id``/``span_id`` (a live
        telemetry span) XOR ``evaluation_run_id``/``cell`` (an evaluation
        matrix cell coordinate).

        A capture refusal (source not found, a declared field path that
        resolved nothing, a moved preview digest, ...) arrives as a typed
        ``EvaluationCaptureRefusalV1`` detail on a thrown ``ConnectError`` —
        decoded here into a :class:`Refusal`; any other exception still
        raises.
        """
        req = _build_capture_case(
            dataset_collection_id=dataset_collection_id,
            draft_id=draft_id,
            trace_id=trace_id,
            span_id=span_id,
            evaluation_run_id=evaluation_run_id,
            cell=cell,
            field_mappings=field_mappings,
            recorded_output_field_path=recorded_output_field_path,
            idempotency_key=idempotency_key,
        )
        try:
            return await self._client.capture_evaluation_case(
                req, headers=headers, timeout_ms=timeout_ms
            )
        except ConnectError as err:
            detail = find_error_detail(err, EvaluationCaptureRefusalV1)
            if detail is None:
                raise
            return _refusal_from_capture_refusal(detail)

    async def update_case_draft(
        self,
        *,
        proposed_case_id: str,
        expected_draft_version: int,
        idempotency_key: str,
        expected_output_json: str | None = None,
        expected_output_absence_reason: str | None = None,
        correction_payload_json: str | None = None,
        needs_ground_truth: bool = False,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> UpdateDatasetCaseDraftResponse:
        """Append/amend a dataset case draft (the optimistic-concurrency edit path)."""
        req = _build_update_case_draft(
            proposed_case_id=proposed_case_id,
            expected_draft_version=expected_draft_version,
            expected_output_json=expected_output_json,
            expected_output_absence_reason=expected_output_absence_reason,
            correction_payload_json=correction_payload_json,
            needs_ground_truth=needs_ground_truth,
            idempotency_key=idempotency_key,
        )
        return await self._client.update_dataset_case_draft(
            req, headers=headers, timeout_ms=timeout_ms
        )

    async def approve_case_draft(
        self,
        *,
        proposed_case_id: str,
        expected_draft_version: int,
        idempotency_key: str,
        note: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> ApproveDatasetCaseDraftResponse:
        req = _build_approve_case_draft(
            proposed_case_id=proposed_case_id,
            expected_draft_version=expected_draft_version,
            note=note,
            idempotency_key=idempotency_key,
        )
        return await self._client.approve_dataset_case_draft(
            req, headers=headers, timeout_ms=timeout_ms
        )

    async def reject_case_draft(
        self,
        *,
        proposed_case_id: str,
        expected_draft_version: int,
        reason: DatasetCaseDraftRejectionReasonV1,
        idempotency_key: str,
        note: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> RejectDatasetCaseDraftResponse:
        req = _build_reject_case_draft(
            proposed_case_id=proposed_case_id,
            expected_draft_version=expected_draft_version,
            reason=reason,
            note=note,
            idempotency_key=idempotency_key,
        )
        return await self._client.reject_dataset_case_draft(
            req, headers=headers, timeout_ms=timeout_ms
        )

    async def merge_case_draft(
        self,
        *,
        proposed_case_id: str,
        expected_draft_version: int,
        target_case_revision_id: str,
        idempotency_key: str,
        note: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> MergeDatasetCaseDraftResponse:
        req = _build_merge_case_draft(
            proposed_case_id=proposed_case_id,
            expected_draft_version=expected_draft_version,
            target_case_revision_id=target_case_revision_id,
            note=note,
            idempotency_key=idempotency_key,
        )
        return await self._client.merge_dataset_case_draft(
            req, headers=headers, timeout_ms=timeout_ms
        )

    async def preview_publish_case_drafts(
        self, *, changeset_id: str, headers: Headers | None = None, timeout_ms: int | None = None
    ) -> PreviewPublishDatasetChangesetResponse:
        req = _build_preview_publish(changeset_id=changeset_id)
        return await self._client.preview_publish_dataset_changeset(
            req, headers=headers, timeout_ms=timeout_ms
        )

    async def publish_case_drafts(
        self,
        *,
        changeset_id: str,
        preview_digest: str,
        idempotency_key: str,
        label: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> PublishDatasetCaseDraftsResponse | Refusal:
        """Publish a reviewed batch of case drafts as a new dataset version.

        ``preview_digest`` must be the digest :meth:`preview_publish_case_drafts`
        just returned — the server recomputes it from the rows it is about to
        commit and refuses on a mismatch rather than silently rebasing. That
        refusal (and every other publish rejection: collection cap exceeded,
        malformed line, draft not finalizable, ...) arrives as a typed
        ``EvaluationDatasetVersionRejectionV1`` detail on a thrown
        ``ConnectError`` — decoded here into a :class:`Refusal`.
        """
        req = _build_publish_case_drafts(
            changeset_id=changeset_id,
            preview_digest=preview_digest,
            label=label,
            idempotency_key=idempotency_key,
        )
        try:
            return await self._client.publish_dataset_case_drafts(
                req, headers=headers, timeout_ms=timeout_ms
            )
        except ConnectError as err:
            detail = find_error_detail(err, EvaluationDatasetVersionRejectionV1)
            if detail is None:
                raise
            return _refusal_from_dataset_version_rejection(detail)

    async def record_annotation(
        self,
        *,
        kind: PlatformAnnotationKindV1,
        title: str,
        start_at: datetime,
        idempotency_key: str,
        end_at: datetime | None = None,
        attributes: Mapping[str, str] = {},
        links: Sequence[tuple[int, str]] = (),
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> RecordPlatformAnnotationResponse | Refusal:
        """Record a platform annotation.

        A rejection (unknown kind, an oversized title/attribute/link, an
        inverted window, a reused idempotency key against different content,
        ...) arrives as a typed ``PlatformAnnotationRejectionV1`` detail on a
        thrown ``ConnectError`` — decoded here into a :class:`Refusal`.
        """
        req = _build_record_annotation(
            kind=kind,
            title=title,
            start_at=start_at,
            end_at=end_at,
            attributes=attributes,
            links=links,
            idempotency_key=idempotency_key,
        )
        try:
            return await self._client.record_platform_annotation(
                req, headers=headers, timeout_ms=timeout_ms
            )
        except ConnectError as err:
            detail = find_error_detail(err, PlatformAnnotationRejectionV1)
            if detail is None:
                raise
            return _refusal_from_annotation_rejection(detail)

    async def list_annotations(
        self,
        *,
        window_start: datetime | None = None,
        window_end: datetime | None = None,
        kinds: Iterable[PlatformAnnotationKindV1] = (),
        page: PageRequestV1 | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ):
        req = _build_list_annotations(
            window_start=window_start, window_end=window_end, kinds=kinds, page=page
        )
        return await self._client.list_platform_annotations(
            req, headers=headers, timeout_ms=timeout_ms
        )


# --------------------------------------------------------------------------
# Sync facade — identical surface, blocking calls, built from the same
# request builders and decoders above.
# --------------------------------------------------------------------------


class AgenticClientSync:
    """Sync ergonomic facade.

    Construct via ``O11yClient.service_sync(AgenticEvaluationServiceClientSync)``.
    """

    __slots__ = ("_client",)

    def __init__(self, client: AgenticEvaluationServiceClientSync) -> None:
        self._client = client

    def whoami(
        self, *, headers: Headers | None = None, timeout_ms: int | None = None
    ) -> GetCallerPrincipalResponse:
        return self._client.get_caller_principal(
            GetCallerPrincipalRequest(), headers=headers, timeout_ms=timeout_ms
        )

    def create_machine_principal(
        self,
        *,
        display_name: str,
        scopes: Iterable[str] = (),
        description: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ):
        req = _build_create_machine_principal(
            display_name=display_name, scopes=scopes, description=description
        )
        return self._client.create_machine_principal(req, headers=headers, timeout_ms=timeout_ms)

    def list_machine_principals(
        self,
        *,
        page_size: int | None = None,
        page_token: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> ListMachinePrincipalsResponse:
        req = _build_list_machine_principals(page_size=page_size, page_token=page_token)
        return self._client.list_machine_principals(req, headers=headers, timeout_ms=timeout_ms)

    def create_machine_credential(
        self,
        *,
        machine_principal_id: str,
        description: str | None = None,
        expires_at: datetime | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> IssuedMachineCredential:
        req = _build_create_machine_credential(
            machine_principal_id=machine_principal_id,
            description=description,
            expires_at=expires_at,
        )
        resp = self._client.create_machine_credential(req, headers=headers, timeout_ms=timeout_ms)
        return _decode_issued_credential(resp)

    def revoke_machine_credential(
        self,
        *,
        credential_id: str,
        reason: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> RevokeMachineCredentialResponse:
        req = _build_revoke_machine_credential(credential_id=credential_id, reason=reason)
        return self._client.revoke_machine_credential(req, headers=headers, timeout_ms=timeout_ms)

    def revoke_machine_principal(
        self,
        *,
        machine_principal_id: str,
        reason: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> RevokeMachinePrincipalResponse:
        req = _build_revoke_machine_principal(
            machine_principal_id=machine_principal_id, reason=reason
        )
        return self._client.revoke_machine_principal(req, headers=headers, timeout_ms=timeout_ms)

    def preview_run(
        self,
        *,
        definition_id: str,
        revision_id: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> PreviewEvaluationRunResponse:
        req = _build_preview_run(definition_id=definition_id, revision_id=revision_id)
        return self._client.preview_evaluation_run(req, headers=headers, timeout_ms=timeout_ms)

    def create_run(
        self,
        *,
        definition_id: str,
        idempotency_key: str,
        preview_token: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> CreateEvaluationRunResponse | Refusal:
        req = _build_create_run(
            definition_id=definition_id,
            idempotency_key=idempotency_key,
            preview_token=preview_token,
        )
        try:
            return self._client.create_evaluation_run(req, headers=headers, timeout_ms=timeout_ms)
        except ConnectError as err:
            detail = find_error_detail(err, EvaluationLaunchRejectionV1)
            if detail is None:
                raise
            return _refusal_from_launch_rejection(detail)

    def lease_cases(
        self,
        *,
        evaluation_run_id: str,
        candidate_key: str,
        runtime_key: str,
        max_cases: int = 0,
        lease_seconds: int = 0,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> LeaseEvaluationCasesResponse | Refusal:
        req = _build_lease_request(
            evaluation_run_id=evaluation_run_id,
            candidate_key=candidate_key,
            runtime_key=runtime_key,
            max_cases=max_cases,
            lease_seconds=lease_seconds,
        )
        resp = self._client.lease_evaluation_cases(req, headers=headers, timeout_ms=timeout_ms)
        return _decode_lease_response(resp)

    def renew_lease(
        self,
        *,
        evaluation_run_id: str,
        lease_id: str,
        lease_token: str,
        lease_seconds: int = 0,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> RenewEvaluationCaseLeaseResponse | Refusal:
        req = _build_renew_request(
            evaluation_run_id=evaluation_run_id,
            lease_id=lease_id,
            lease_token=lease_token,
            lease_seconds=lease_seconds,
        )
        resp = self._client.renew_evaluation_case_lease(req, headers=headers, timeout_ms=timeout_ms)
        return _decode_renew_response(resp)

    def submit_case_outputs(
        self,
        *,
        evaluation_run_id: str,
        lease_id: str,
        lease_token: str,
        outputs: Sequence[CaseOutput],
        idempotency_key: str,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> SubmitEvaluationCaseOutputsResponse | Refusal:
        req = _build_submit_outputs_request(
            evaluation_run_id=evaluation_run_id,
            lease_id=lease_id,
            lease_token=lease_token,
            outputs=outputs,
            idempotency_key=idempotency_key,
        )
        resp = self._client.submit_evaluation_case_outputs(
            req, headers=headers, timeout_ms=timeout_ms
        )
        return _decode_submit_response(resp)

    def release_lease(
        self,
        *,
        evaluation_run_id: str,
        lease_id: str,
        lease_token: str,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> ReleaseEvaluationCaseLeaseResponse | Refusal:
        req = _build_release_request(
            evaluation_run_id=evaluation_run_id, lease_id=lease_id, lease_token=lease_token
        )
        resp = self._client.release_evaluation_case_lease(
            req, headers=headers, timeout_ms=timeout_ms
        )
        return _decode_release_response(resp)

    def submit_recorded_outputs(
        self,
        *,
        evaluation_run_id: str,
        candidate_key: str,
        runtime_key: str,
        outputs: Sequence[CaseOutput],
        idempotency_key: str,
        lease_seconds: int = 0,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> SubmitEvaluationCaseOutputsResponse | Refusal:
        require_non_empty_sequence(outputs, field="outputs")
        leased = self.lease_cases(
            evaluation_run_id=evaluation_run_id,
            candidate_key=candidate_key,
            runtime_key=runtime_key,
            max_cases=len(outputs),
            lease_seconds=lease_seconds,
        )
        if isinstance(leased, Refusal):
            return leased
        lease = leased.lease
        try:
            return self.submit_case_outputs(
                evaluation_run_id=evaluation_run_id,
                lease_id=lease.lease_id,
                lease_token=lease.lease_token,
                outputs=outputs,
                idempotency_key=idempotency_key,
            )
        finally:
            self.release_lease(
                evaluation_run_id=evaluation_run_id,
                lease_id=lease.lease_id,
                lease_token=lease.lease_token,
            )

    def capture_case_draft(
        self,
        *,
        dataset_collection_id: str,
        idempotency_key: str,
        draft_id: str | None = None,
        trace_id: bytes | None = None,
        span_id: bytes | None = None,
        evaluation_run_id: str | None = None,
        cell: EvaluationCellRefV1 | None = None,
        field_mappings: Mapping[str, str] = {},
        recorded_output_field_path: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> CaptureEvaluationCaseResponse | Refusal:
        req = _build_capture_case(
            dataset_collection_id=dataset_collection_id,
            draft_id=draft_id,
            trace_id=trace_id,
            span_id=span_id,
            evaluation_run_id=evaluation_run_id,
            cell=cell,
            field_mappings=field_mappings,
            recorded_output_field_path=recorded_output_field_path,
            idempotency_key=idempotency_key,
        )
        try:
            return self._client.capture_evaluation_case(req, headers=headers, timeout_ms=timeout_ms)
        except ConnectError as err:
            detail = find_error_detail(err, EvaluationCaptureRefusalV1)
            if detail is None:
                raise
            return _refusal_from_capture_refusal(detail)

    def update_case_draft(
        self,
        *,
        proposed_case_id: str,
        expected_draft_version: int,
        idempotency_key: str,
        expected_output_json: str | None = None,
        expected_output_absence_reason: str | None = None,
        correction_payload_json: str | None = None,
        needs_ground_truth: bool = False,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> UpdateDatasetCaseDraftResponse:
        req = _build_update_case_draft(
            proposed_case_id=proposed_case_id,
            expected_draft_version=expected_draft_version,
            expected_output_json=expected_output_json,
            expected_output_absence_reason=expected_output_absence_reason,
            correction_payload_json=correction_payload_json,
            needs_ground_truth=needs_ground_truth,
            idempotency_key=idempotency_key,
        )
        return self._client.update_dataset_case_draft(req, headers=headers, timeout_ms=timeout_ms)

    def approve_case_draft(
        self,
        *,
        proposed_case_id: str,
        expected_draft_version: int,
        idempotency_key: str,
        note: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> ApproveDatasetCaseDraftResponse:
        req = _build_approve_case_draft(
            proposed_case_id=proposed_case_id,
            expected_draft_version=expected_draft_version,
            note=note,
            idempotency_key=idempotency_key,
        )
        return self._client.approve_dataset_case_draft(req, headers=headers, timeout_ms=timeout_ms)

    def reject_case_draft(
        self,
        *,
        proposed_case_id: str,
        expected_draft_version: int,
        reason: DatasetCaseDraftRejectionReasonV1,
        idempotency_key: str,
        note: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> RejectDatasetCaseDraftResponse:
        req = _build_reject_case_draft(
            proposed_case_id=proposed_case_id,
            expected_draft_version=expected_draft_version,
            reason=reason,
            note=note,
            idempotency_key=idempotency_key,
        )
        return self._client.reject_dataset_case_draft(req, headers=headers, timeout_ms=timeout_ms)

    def merge_case_draft(
        self,
        *,
        proposed_case_id: str,
        expected_draft_version: int,
        target_case_revision_id: str,
        idempotency_key: str,
        note: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> MergeDatasetCaseDraftResponse:
        req = _build_merge_case_draft(
            proposed_case_id=proposed_case_id,
            expected_draft_version=expected_draft_version,
            target_case_revision_id=target_case_revision_id,
            note=note,
            idempotency_key=idempotency_key,
        )
        return self._client.merge_dataset_case_draft(req, headers=headers, timeout_ms=timeout_ms)

    def preview_publish_case_drafts(
        self, *, changeset_id: str, headers: Headers | None = None, timeout_ms: int | None = None
    ) -> PreviewPublishDatasetChangesetResponse:
        req = _build_preview_publish(changeset_id=changeset_id)
        return self._client.preview_publish_dataset_changeset(
            req, headers=headers, timeout_ms=timeout_ms
        )

    def publish_case_drafts(
        self,
        *,
        changeset_id: str,
        preview_digest: str,
        idempotency_key: str,
        label: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> PublishDatasetCaseDraftsResponse | Refusal:
        req = _build_publish_case_drafts(
            changeset_id=changeset_id,
            preview_digest=preview_digest,
            label=label,
            idempotency_key=idempotency_key,
        )
        try:
            return self._client.publish_dataset_case_drafts(
                req, headers=headers, timeout_ms=timeout_ms
            )
        except ConnectError as err:
            detail = find_error_detail(err, EvaluationDatasetVersionRejectionV1)
            if detail is None:
                raise
            return _refusal_from_dataset_version_rejection(detail)

    def record_annotation(
        self,
        *,
        kind: PlatformAnnotationKindV1,
        title: str,
        start_at: datetime,
        idempotency_key: str,
        end_at: datetime | None = None,
        attributes: Mapping[str, str] = {},
        links: Sequence[tuple[int, str]] = (),
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> RecordPlatformAnnotationResponse | Refusal:
        req = _build_record_annotation(
            kind=kind,
            title=title,
            start_at=start_at,
            end_at=end_at,
            attributes=attributes,
            links=links,
            idempotency_key=idempotency_key,
        )
        try:
            return self._client.record_platform_annotation(
                req, headers=headers, timeout_ms=timeout_ms
            )
        except ConnectError as err:
            detail = find_error_detail(err, PlatformAnnotationRejectionV1)
            if detail is None:
                raise
            return _refusal_from_annotation_rejection(detail)

    def list_annotations(
        self,
        *,
        window_start: datetime | None = None,
        window_end: datetime | None = None,
        kinds: Iterable[PlatformAnnotationKindV1] = (),
        page: PageRequestV1 | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ):
        req = _build_list_annotations(
            window_start=window_start, window_end=window_end, kinds=kinds, page=page
        )
        return self._client.list_platform_annotations(req, headers=headers, timeout_ms=timeout_ms)
