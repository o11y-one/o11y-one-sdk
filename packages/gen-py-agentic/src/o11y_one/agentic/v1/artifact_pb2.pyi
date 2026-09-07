import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from o11y_one.agentic.v1 import evaluation_pb2 as _evaluation_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContentDigestAlgorithmV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTENT_DIGEST_ALGORITHM_V1_UNSPECIFIED: _ClassVar[ContentDigestAlgorithmV1]
    CONTENT_DIGEST_ALGORITHM_V1_SHA256: _ClassVar[ContentDigestAlgorithmV1]
    CONTENT_DIGEST_ALGORITHM_V1_SHA512: _ClassVar[ContentDigestAlgorithmV1]
    CONTENT_DIGEST_ALGORITHM_V1_BLAKE3: _ClassVar[ContentDigestAlgorithmV1]

class ContentSensitivityClassV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTENT_SENSITIVITY_CLASS_V1_UNSPECIFIED: _ClassVar[ContentSensitivityClassV1]
    CONTENT_SENSITIVITY_CLASS_V1_PUBLIC: _ClassVar[ContentSensitivityClassV1]
    CONTENT_SENSITIVITY_CLASS_V1_INTERNAL: _ClassVar[ContentSensitivityClassV1]
    CONTENT_SENSITIVITY_CLASS_V1_CONFIDENTIAL: _ClassVar[ContentSensitivityClassV1]
    CONTENT_SENSITIVITY_CLASS_V1_RESTRICTED: _ClassVar[ContentSensitivityClassV1]

class RedactionClassV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REDACTION_CLASS_V1_UNSPECIFIED: _ClassVar[RedactionClassV1]
    REDACTION_CLASS_V1_NONE: _ClassVar[RedactionClassV1]
    REDACTION_CLASS_V1_PARTIAL: _ClassVar[RedactionClassV1]
    REDACTION_CLASS_V1_WITHHELD: _ClassVar[RedactionClassV1]
    REDACTION_CLASS_V1_UNCLASSIFIED: _ClassVar[RedactionClassV1]

class RetentionClassV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RETENTION_CLASS_V1_UNSPECIFIED: _ClassVar[RetentionClassV1]
    RETENTION_CLASS_V1_STANDARD: _ClassVar[RetentionClassV1]
    RETENTION_CLASS_V1_EXTENDED: _ClassVar[RetentionClassV1]
    RETENTION_CLASS_V1_RELEASE_EVIDENCE: _ClassVar[RetentionClassV1]
    RETENTION_CLASS_V1_LEGAL_HOLD: _ClassVar[RetentionClassV1]

class ArtifactTypeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ARTIFACT_TYPE_V1_UNSPECIFIED: _ClassVar[ArtifactTypeV1]
    ARTIFACT_TYPE_V1_DOCUMENT: _ClassVar[ArtifactTypeV1]
    ARTIFACT_TYPE_V1_DATASET: _ClassVar[ArtifactTypeV1]
    ARTIFACT_TYPE_V1_MODEL: _ClassVar[ArtifactTypeV1]
    ARTIFACT_TYPE_V1_PROMPT: _ClassVar[ArtifactTypeV1]
    ARTIFACT_TYPE_V1_SOURCE_CODE: _ClassVar[ArtifactTypeV1]
    ARTIFACT_TYPE_V1_BUILD_OUTPUT: _ClassVar[ArtifactTypeV1]
    ARTIFACT_TYPE_V1_CONFIGURATION: _ClassVar[ArtifactTypeV1]
    ARTIFACT_TYPE_V1_IMAGE: _ClassVar[ArtifactTypeV1]
    ARTIFACT_TYPE_V1_AUDIO: _ClassVar[ArtifactTypeV1]
    ARTIFACT_TYPE_V1_VIDEO: _ClassVar[ArtifactTypeV1]
    ARTIFACT_TYPE_V1_LOG_BUNDLE: _ClassVar[ArtifactTypeV1]
    ARTIFACT_TYPE_V1_REPORT: _ClassVar[ArtifactTypeV1]
    ARTIFACT_TYPE_V1_TOOL_RESULT: _ClassVar[ArtifactTypeV1]
    ARTIFACT_TYPE_V1_OTHER: _ClassVar[ArtifactTypeV1]

class ArtifactRoleV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ARTIFACT_ROLE_V1_UNSPECIFIED: _ClassVar[ArtifactRoleV1]
    ARTIFACT_ROLE_V1_CONSUMED: _ClassVar[ArtifactRoleV1]
    ARTIFACT_ROLE_V1_PRODUCED: _ClassVar[ArtifactRoleV1]
    ARTIFACT_ROLE_V1_EVIDENCE: _ClassVar[ArtifactRoleV1]
    ARTIFACT_ROLE_V1_REFERENCED: _ClassVar[ArtifactRoleV1]

class ArtifactRelationV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ARTIFACT_RELATION_V1_UNSPECIFIED: _ClassVar[ArtifactRelationV1]
    ARTIFACT_RELATION_V1_INPUT_TO: _ClassVar[ArtifactRelationV1]
    ARTIFACT_RELATION_V1_OUTPUT_OF: _ClassVar[ArtifactRelationV1]
    ARTIFACT_RELATION_V1_DERIVED_FROM: _ClassVar[ArtifactRelationV1]
    ARTIFACT_RELATION_V1_EVIDENCE_FOR: _ClassVar[ArtifactRelationV1]
    ARTIFACT_RELATION_V1_ATTACHED_TO: _ClassVar[ArtifactRelationV1]
    ARTIFACT_RELATION_V1_SUPERSEDES: _ClassVar[ArtifactRelationV1]
    ARTIFACT_RELATION_V1_OTHER: _ClassVar[ArtifactRelationV1]

class ArtifactAvailabilityV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ARTIFACT_AVAILABILITY_V1_UNSPECIFIED: _ClassVar[ArtifactAvailabilityV1]
    ARTIFACT_AVAILABILITY_V1_AVAILABLE: _ClassVar[ArtifactAvailabilityV1]
    ARTIFACT_AVAILABILITY_V1_TOMBSTONED: _ClassVar[ArtifactAvailabilityV1]
    ARTIFACT_AVAILABILITY_V1_UNRESOLVED: _ClassVar[ArtifactAvailabilityV1]
    ARTIFACT_AVAILABILITY_V1_REVOKED: _ClassVar[ArtifactAvailabilityV1]
    ARTIFACT_AVAILABILITY_V1_FORBIDDEN: _ClassVar[ArtifactAvailabilityV1]

class ArtifactLinkSourceKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ARTIFACT_LINK_SOURCE_KIND_V1_UNSPECIFIED: _ClassVar[ArtifactLinkSourceKindV1]
    ARTIFACT_LINK_SOURCE_KIND_V1_SPAN_EVENT: _ClassVar[ArtifactLinkSourceKindV1]
    ARTIFACT_LINK_SOURCE_KIND_V1_CORRELATED_LOG: _ClassVar[ArtifactLinkSourceKindV1]
    ARTIFACT_LINK_SOURCE_KIND_V1_SPAN_ATTRIBUTE: _ClassVar[ArtifactLinkSourceKindV1]
    ARTIFACT_LINK_SOURCE_KIND_V1_FALLBACK_RPC: _ClassVar[ArtifactLinkSourceKindV1]
    ARTIFACT_LINK_SOURCE_KIND_V1_BACKFILL: _ClassVar[ArtifactLinkSourceKindV1]
    ARTIFACT_LINK_SOURCE_KIND_V1_PLATFORM_EXECUTOR: _ClassVar[ArtifactLinkSourceKindV1]

class ArtifactLinkStatusV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ARTIFACT_LINK_STATUS_V1_UNSPECIFIED: _ClassVar[ArtifactLinkStatusV1]
    ARTIFACT_LINK_STATUS_V1_ACCEPTED: _ClassVar[ArtifactLinkStatusV1]
    ARTIFACT_LINK_STATUS_V1_CORRECTED: _ClassVar[ArtifactLinkStatusV1]
    ARTIFACT_LINK_STATUS_V1_REVOKED: _ClassVar[ArtifactLinkStatusV1]
    ARTIFACT_LINK_STATUS_V1_REJECTED: _ClassVar[ArtifactLinkStatusV1]
    ARTIFACT_LINK_STATUS_V1_UNRESOLVED: _ClassVar[ArtifactLinkStatusV1]

class ArtifactLinkConflictPostureV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ARTIFACT_LINK_CONFLICT_POSTURE_V1_UNSPECIFIED: _ClassVar[ArtifactLinkConflictPostureV1]
    ARTIFACT_LINK_CONFLICT_POSTURE_V1_NONE: _ClassVar[ArtifactLinkConflictPostureV1]
    ARTIFACT_LINK_CONFLICT_POSTURE_V1_DUPLICATE: _ClassVar[ArtifactLinkConflictPostureV1]
    ARTIFACT_LINK_CONFLICT_POSTURE_V1_CONFLICTING: _ClassVar[ArtifactLinkConflictPostureV1]

class ArtifactResolverPostureV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ARTIFACT_RESOLVER_POSTURE_V1_UNSPECIFIED: _ClassVar[ArtifactResolverPostureV1]
    ARTIFACT_RESOLVER_POSTURE_V1_NOT_CONFIGURED: _ClassVar[ArtifactResolverPostureV1]
    ARTIFACT_RESOLVER_POSTURE_V1_CONFIGURED_NOT_RESOLVED: _ClassVar[ArtifactResolverPostureV1]
    ARTIFACT_RESOLVER_POSTURE_V1_RESOLVED: _ClassVar[ArtifactResolverPostureV1]
    ARTIFACT_RESOLVER_POSTURE_V1_DENIED: _ClassVar[ArtifactResolverPostureV1]
    ARTIFACT_RESOLVER_POSTURE_V1_FAILED: _ClassVar[ArtifactResolverPostureV1]
    ARTIFACT_RESOLVER_POSTURE_V1_EXPIRED: _ClassVar[ArtifactResolverPostureV1]

class ArtifactLinkFallbackReasonV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ARTIFACT_LINK_FALLBACK_REASON_V1_UNSPECIFIED: _ClassVar[ArtifactLinkFallbackReasonV1]
    ARTIFACT_LINK_FALLBACK_REASON_V1_UNAVAILABLE_INSTRUMENTATION: _ClassVar[ArtifactLinkFallbackReasonV1]
    ARTIFACT_LINK_FALLBACK_REASON_V1_BACKFILL: _ClassVar[ArtifactLinkFallbackReasonV1]
    ARTIFACT_LINK_FALLBACK_REASON_V1_CORRECTION: _ClassVar[ArtifactLinkFallbackReasonV1]
    ARTIFACT_LINK_FALLBACK_REASON_V1_REVOCATION: _ClassVar[ArtifactLinkFallbackReasonV1]
CONTENT_DIGEST_ALGORITHM_V1_UNSPECIFIED: ContentDigestAlgorithmV1
CONTENT_DIGEST_ALGORITHM_V1_SHA256: ContentDigestAlgorithmV1
CONTENT_DIGEST_ALGORITHM_V1_SHA512: ContentDigestAlgorithmV1
CONTENT_DIGEST_ALGORITHM_V1_BLAKE3: ContentDigestAlgorithmV1
CONTENT_SENSITIVITY_CLASS_V1_UNSPECIFIED: ContentSensitivityClassV1
CONTENT_SENSITIVITY_CLASS_V1_PUBLIC: ContentSensitivityClassV1
CONTENT_SENSITIVITY_CLASS_V1_INTERNAL: ContentSensitivityClassV1
CONTENT_SENSITIVITY_CLASS_V1_CONFIDENTIAL: ContentSensitivityClassV1
CONTENT_SENSITIVITY_CLASS_V1_RESTRICTED: ContentSensitivityClassV1
REDACTION_CLASS_V1_UNSPECIFIED: RedactionClassV1
REDACTION_CLASS_V1_NONE: RedactionClassV1
REDACTION_CLASS_V1_PARTIAL: RedactionClassV1
REDACTION_CLASS_V1_WITHHELD: RedactionClassV1
REDACTION_CLASS_V1_UNCLASSIFIED: RedactionClassV1
RETENTION_CLASS_V1_UNSPECIFIED: RetentionClassV1
RETENTION_CLASS_V1_STANDARD: RetentionClassV1
RETENTION_CLASS_V1_EXTENDED: RetentionClassV1
RETENTION_CLASS_V1_RELEASE_EVIDENCE: RetentionClassV1
RETENTION_CLASS_V1_LEGAL_HOLD: RetentionClassV1
ARTIFACT_TYPE_V1_UNSPECIFIED: ArtifactTypeV1
ARTIFACT_TYPE_V1_DOCUMENT: ArtifactTypeV1
ARTIFACT_TYPE_V1_DATASET: ArtifactTypeV1
ARTIFACT_TYPE_V1_MODEL: ArtifactTypeV1
ARTIFACT_TYPE_V1_PROMPT: ArtifactTypeV1
ARTIFACT_TYPE_V1_SOURCE_CODE: ArtifactTypeV1
ARTIFACT_TYPE_V1_BUILD_OUTPUT: ArtifactTypeV1
ARTIFACT_TYPE_V1_CONFIGURATION: ArtifactTypeV1
ARTIFACT_TYPE_V1_IMAGE: ArtifactTypeV1
ARTIFACT_TYPE_V1_AUDIO: ArtifactTypeV1
ARTIFACT_TYPE_V1_VIDEO: ArtifactTypeV1
ARTIFACT_TYPE_V1_LOG_BUNDLE: ArtifactTypeV1
ARTIFACT_TYPE_V1_REPORT: ArtifactTypeV1
ARTIFACT_TYPE_V1_TOOL_RESULT: ArtifactTypeV1
ARTIFACT_TYPE_V1_OTHER: ArtifactTypeV1
ARTIFACT_ROLE_V1_UNSPECIFIED: ArtifactRoleV1
ARTIFACT_ROLE_V1_CONSUMED: ArtifactRoleV1
ARTIFACT_ROLE_V1_PRODUCED: ArtifactRoleV1
ARTIFACT_ROLE_V1_EVIDENCE: ArtifactRoleV1
ARTIFACT_ROLE_V1_REFERENCED: ArtifactRoleV1
ARTIFACT_RELATION_V1_UNSPECIFIED: ArtifactRelationV1
ARTIFACT_RELATION_V1_INPUT_TO: ArtifactRelationV1
ARTIFACT_RELATION_V1_OUTPUT_OF: ArtifactRelationV1
ARTIFACT_RELATION_V1_DERIVED_FROM: ArtifactRelationV1
ARTIFACT_RELATION_V1_EVIDENCE_FOR: ArtifactRelationV1
ARTIFACT_RELATION_V1_ATTACHED_TO: ArtifactRelationV1
ARTIFACT_RELATION_V1_SUPERSEDES: ArtifactRelationV1
ARTIFACT_RELATION_V1_OTHER: ArtifactRelationV1
ARTIFACT_AVAILABILITY_V1_UNSPECIFIED: ArtifactAvailabilityV1
ARTIFACT_AVAILABILITY_V1_AVAILABLE: ArtifactAvailabilityV1
ARTIFACT_AVAILABILITY_V1_TOMBSTONED: ArtifactAvailabilityV1
ARTIFACT_AVAILABILITY_V1_UNRESOLVED: ArtifactAvailabilityV1
ARTIFACT_AVAILABILITY_V1_REVOKED: ArtifactAvailabilityV1
ARTIFACT_AVAILABILITY_V1_FORBIDDEN: ArtifactAvailabilityV1
ARTIFACT_LINK_SOURCE_KIND_V1_UNSPECIFIED: ArtifactLinkSourceKindV1
ARTIFACT_LINK_SOURCE_KIND_V1_SPAN_EVENT: ArtifactLinkSourceKindV1
ARTIFACT_LINK_SOURCE_KIND_V1_CORRELATED_LOG: ArtifactLinkSourceKindV1
ARTIFACT_LINK_SOURCE_KIND_V1_SPAN_ATTRIBUTE: ArtifactLinkSourceKindV1
ARTIFACT_LINK_SOURCE_KIND_V1_FALLBACK_RPC: ArtifactLinkSourceKindV1
ARTIFACT_LINK_SOURCE_KIND_V1_BACKFILL: ArtifactLinkSourceKindV1
ARTIFACT_LINK_SOURCE_KIND_V1_PLATFORM_EXECUTOR: ArtifactLinkSourceKindV1
ARTIFACT_LINK_STATUS_V1_UNSPECIFIED: ArtifactLinkStatusV1
ARTIFACT_LINK_STATUS_V1_ACCEPTED: ArtifactLinkStatusV1
ARTIFACT_LINK_STATUS_V1_CORRECTED: ArtifactLinkStatusV1
ARTIFACT_LINK_STATUS_V1_REVOKED: ArtifactLinkStatusV1
ARTIFACT_LINK_STATUS_V1_REJECTED: ArtifactLinkStatusV1
ARTIFACT_LINK_STATUS_V1_UNRESOLVED: ArtifactLinkStatusV1
ARTIFACT_LINK_CONFLICT_POSTURE_V1_UNSPECIFIED: ArtifactLinkConflictPostureV1
ARTIFACT_LINK_CONFLICT_POSTURE_V1_NONE: ArtifactLinkConflictPostureV1
ARTIFACT_LINK_CONFLICT_POSTURE_V1_DUPLICATE: ArtifactLinkConflictPostureV1
ARTIFACT_LINK_CONFLICT_POSTURE_V1_CONFLICTING: ArtifactLinkConflictPostureV1
ARTIFACT_RESOLVER_POSTURE_V1_UNSPECIFIED: ArtifactResolverPostureV1
ARTIFACT_RESOLVER_POSTURE_V1_NOT_CONFIGURED: ArtifactResolverPostureV1
ARTIFACT_RESOLVER_POSTURE_V1_CONFIGURED_NOT_RESOLVED: ArtifactResolverPostureV1
ARTIFACT_RESOLVER_POSTURE_V1_RESOLVED: ArtifactResolverPostureV1
ARTIFACT_RESOLVER_POSTURE_V1_DENIED: ArtifactResolverPostureV1
ARTIFACT_RESOLVER_POSTURE_V1_FAILED: ArtifactResolverPostureV1
ARTIFACT_RESOLVER_POSTURE_V1_EXPIRED: ArtifactResolverPostureV1
ARTIFACT_LINK_FALLBACK_REASON_V1_UNSPECIFIED: ArtifactLinkFallbackReasonV1
ARTIFACT_LINK_FALLBACK_REASON_V1_UNAVAILABLE_INSTRUMENTATION: ArtifactLinkFallbackReasonV1
ARTIFACT_LINK_FALLBACK_REASON_V1_BACKFILL: ArtifactLinkFallbackReasonV1
ARTIFACT_LINK_FALLBACK_REASON_V1_CORRECTION: ArtifactLinkFallbackReasonV1
ARTIFACT_LINK_FALLBACK_REASON_V1_REVOCATION: ArtifactLinkFallbackReasonV1

class ContentDigestV1(_message.Message):
    __slots__ = ("algorithm", "value")
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    algorithm: ContentDigestAlgorithmV1
    value: bytes
    def __init__(self, algorithm: _Optional[_Union[ContentDigestAlgorithmV1, str]] = ..., value: _Optional[bytes] = ...) -> None: ...

class TelemetryRefV1(_message.Message):
    __slots__ = ("trace_id", "span_id", "observation_id", "conversation_id", "session_id")
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    trace_id: bytes
    span_id: bytes
    observation_id: str
    conversation_id: str
    session_id: str
    def __init__(self, trace_id: _Optional[bytes] = ..., span_id: _Optional[bytes] = ..., observation_id: _Optional[str] = ..., conversation_id: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class ContentRangeRefV1(_message.Message):
    __slots__ = ("subject_id", "start_byte", "end_byte")
    SUBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    START_BYTE_FIELD_NUMBER: _ClassVar[int]
    END_BYTE_FIELD_NUMBER: _ClassVar[int]
    subject_id: str
    start_byte: int
    end_byte: int
    def __init__(self, subject_id: _Optional[str] = ..., start_byte: _Optional[int] = ..., end_byte: _Optional[int] = ...) -> None: ...

class EvaluationRunRefV1(_message.Message):
    __slots__ = ("evaluation_run_id",)
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    def __init__(self, evaluation_run_id: _Optional[str] = ...) -> None: ...

class EvaluationCellCoordinateV1(_message.Message):
    __slots__ = ("evaluation_run_id", "cohort_id", "candidate_id", "case_revision_id", "trial", "attempt_generation")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    COHORT_ID_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_ID_FIELD_NUMBER: _ClassVar[int]
    CASE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    TRIAL_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_GENERATION_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    cohort_id: str
    candidate_id: str
    case_revision_id: str
    trial: int
    attempt_generation: int
    def __init__(self, evaluation_run_id: _Optional[str] = ..., cohort_id: _Optional[str] = ..., candidate_id: _Optional[str] = ..., case_revision_id: _Optional[str] = ..., trial: _Optional[int] = ..., attempt_generation: _Optional[int] = ...) -> None: ...

class AttemptRefV1(_message.Message):
    __slots__ = ("attempt_id", "execution_id", "attempt_generation")
    ATTEMPT_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_GENERATION_FIELD_NUMBER: _ClassVar[int]
    attempt_id: str
    execution_id: str
    attempt_generation: int
    def __init__(self, attempt_id: _Optional[str] = ..., execution_id: _Optional[str] = ..., attempt_generation: _Optional[int] = ...) -> None: ...

class EvaluationSubjectRefV1(_message.Message):
    __slots__ = ("subject_id", "subject_revision_id")
    SUBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    subject_id: str
    subject_revision_id: str
    def __init__(self, subject_id: _Optional[str] = ..., subject_revision_id: _Optional[str] = ...) -> None: ...

class AgentRunRefV1(_message.Message):
    __slots__ = ("agent_run_id", "conversation_id")
    AGENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    agent_run_id: str
    conversation_id: str
    def __init__(self, agent_run_id: _Optional[str] = ..., conversation_id: _Optional[str] = ...) -> None: ...

class DatasetDraftRefV1(_message.Message):
    __slots__ = ("dataset_draft_id",)
    DATASET_DRAFT_ID_FIELD_NUMBER: _ClassVar[int]
    dataset_draft_id: str
    def __init__(self, dataset_draft_id: _Optional[str] = ...) -> None: ...

class DatasetCaseRevisionRefV1(_message.Message):
    __slots__ = ("case_revision_id", "dataset_version_id")
    CASE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    case_revision_id: str
    dataset_version_id: str
    def __init__(self, case_revision_id: _Optional[str] = ..., dataset_version_id: _Optional[str] = ...) -> None: ...

class RuleStepRefV1(_message.Message):
    __slots__ = ("rule_id", "rule_version_id", "step_id")
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    STEP_ID_FIELD_NUMBER: _ClassVar[int]
    rule_id: str
    rule_version_id: str
    step_id: str
    def __init__(self, rule_id: _Optional[str] = ..., rule_version_id: _Optional[str] = ..., step_id: _Optional[str] = ...) -> None: ...

class ReleaseEvidenceRefV1(_message.Message):
    __slots__ = ("release_id", "evidence_revision_id")
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    release_id: str
    evidence_revision_id: str
    def __init__(self, release_id: _Optional[str] = ..., evidence_revision_id: _Optional[str] = ...) -> None: ...

class EvidenceAnchorV1(_message.Message):
    __slots__ = ("evaluation_run", "evaluation_cell", "candidate_attempt", "scorer_attempt", "evaluation_subject", "telemetry", "agent_run", "dataset_draft", "dataset_case_revision", "rule_workflow_step", "release_evidence", "content_range")
    EVALUATION_RUN_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_CELL_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    SCORER_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_SUBJECT_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    AGENT_RUN_FIELD_NUMBER: _ClassVar[int]
    DATASET_DRAFT_FIELD_NUMBER: _ClassVar[int]
    DATASET_CASE_REVISION_FIELD_NUMBER: _ClassVar[int]
    RULE_WORKFLOW_STEP_FIELD_NUMBER: _ClassVar[int]
    RELEASE_EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_RANGE_FIELD_NUMBER: _ClassVar[int]
    evaluation_run: EvaluationRunRefV1
    evaluation_cell: EvaluationCellCoordinateV1
    candidate_attempt: AttemptRefV1
    scorer_attempt: AttemptRefV1
    evaluation_subject: EvaluationSubjectRefV1
    telemetry: TelemetryRefV1
    agent_run: AgentRunRefV1
    dataset_draft: DatasetDraftRefV1
    dataset_case_revision: DatasetCaseRevisionRefV1
    rule_workflow_step: RuleStepRefV1
    release_evidence: ReleaseEvidenceRefV1
    content_range: ContentRangeRefV1
    def __init__(self, evaluation_run: _Optional[_Union[EvaluationRunRefV1, _Mapping]] = ..., evaluation_cell: _Optional[_Union[EvaluationCellCoordinateV1, _Mapping]] = ..., candidate_attempt: _Optional[_Union[AttemptRefV1, _Mapping]] = ..., scorer_attempt: _Optional[_Union[AttemptRefV1, _Mapping]] = ..., evaluation_subject: _Optional[_Union[EvaluationSubjectRefV1, _Mapping]] = ..., telemetry: _Optional[_Union[TelemetryRefV1, _Mapping]] = ..., agent_run: _Optional[_Union[AgentRunRefV1, _Mapping]] = ..., dataset_draft: _Optional[_Union[DatasetDraftRefV1, _Mapping]] = ..., dataset_case_revision: _Optional[_Union[DatasetCaseRevisionRefV1, _Mapping]] = ..., rule_workflow_step: _Optional[_Union[RuleStepRefV1, _Mapping]] = ..., release_evidence: _Optional[_Union[ReleaseEvidenceRefV1, _Mapping]] = ..., content_range: _Optional[_Union[ContentRangeRefV1, _Mapping]] = ...) -> None: ...

class ExternalArtifactRefV1(_message.Message):
    __slots__ = ("artifact_id", "type", "filename", "version", "hash", "purl", "storage_system", "storage_key", "resolver_key", "policy_safe_url", "media_type", "size_bytes", "digest", "sensitivity", "redaction", "retention", "metadata", "availability")
    ARTIFACT_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    PURL_FIELD_NUMBER: _ClassVar[int]
    STORAGE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    STORAGE_KEY_FIELD_NUMBER: _ClassVar[int]
    RESOLVER_KEY_FIELD_NUMBER: _ClassVar[int]
    POLICY_SAFE_URL_FIELD_NUMBER: _ClassVar[int]
    MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    REDACTION_FIELD_NUMBER: _ClassVar[int]
    RETENTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    artifact_id: str
    type: ArtifactTypeV1
    filename: str
    version: str
    hash: str
    purl: str
    storage_system: str
    storage_key: str
    resolver_key: str
    policy_safe_url: str
    media_type: str
    size_bytes: int
    digest: ContentDigestV1
    sensitivity: ContentSensitivityClassV1
    redaction: RedactionClassV1
    retention: RetentionClassV1
    metadata: _containers.RepeatedCompositeFieldContainer[_evaluation_pb2.MetadataEntryV1]
    availability: ArtifactAvailabilityV1
    def __init__(self, artifact_id: _Optional[str] = ..., type: _Optional[_Union[ArtifactTypeV1, str]] = ..., filename: _Optional[str] = ..., version: _Optional[str] = ..., hash: _Optional[str] = ..., purl: _Optional[str] = ..., storage_system: _Optional[str] = ..., storage_key: _Optional[str] = ..., resolver_key: _Optional[str] = ..., policy_safe_url: _Optional[str] = ..., media_type: _Optional[str] = ..., size_bytes: _Optional[int] = ..., digest: _Optional[_Union[ContentDigestV1, _Mapping]] = ..., sensitivity: _Optional[_Union[ContentSensitivityClassV1, str]] = ..., redaction: _Optional[_Union[RedactionClassV1, str]] = ..., retention: _Optional[_Union[RetentionClassV1, str]] = ..., metadata: _Optional[_Iterable[_Union[_evaluation_pb2.MetadataEntryV1, _Mapping]]] = ..., availability: _Optional[_Union[ArtifactAvailabilityV1, str]] = ...) -> None: ...

class ArtifactLinkV1(_message.Message):
    __slots__ = ("tenant_id", "org_id", "link_id", "artifact", "role", "relation", "source", "anchor", "source_kind", "observed_at", "status", "supersedes_link_id", "correction_sequence", "provenance", "facts_watermark", "conflict_posture", "fallback_reason", "resolver_posture")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUPERSEDES_LINK_ID_FIELD_NUMBER: _ClassVar[int]
    CORRECTION_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    PROVENANCE_FIELD_NUMBER: _ClassVar[int]
    FACTS_WATERMARK_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_POSTURE_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_REASON_FIELD_NUMBER: _ClassVar[int]
    RESOLVER_POSTURE_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    org_id: str
    link_id: bytes
    artifact: ExternalArtifactRefV1
    role: ArtifactRoleV1
    relation: ArtifactRelationV1
    source: TelemetryRefV1
    anchor: EvidenceAnchorV1
    source_kind: ArtifactLinkSourceKindV1
    observed_at: _timestamp_pb2.Timestamp
    status: ArtifactLinkStatusV1
    supersedes_link_id: str
    correction_sequence: int
    provenance: _evaluation_pb2.SemanticConventionProvenanceV1
    facts_watermark: str
    conflict_posture: ArtifactLinkConflictPostureV1
    fallback_reason: ArtifactLinkFallbackReasonV1
    resolver_posture: ArtifactResolverPostureV1
    def __init__(self, tenant_id: _Optional[str] = ..., org_id: _Optional[str] = ..., link_id: _Optional[bytes] = ..., artifact: _Optional[_Union[ExternalArtifactRefV1, _Mapping]] = ..., role: _Optional[_Union[ArtifactRoleV1, str]] = ..., relation: _Optional[_Union[ArtifactRelationV1, str]] = ..., source: _Optional[_Union[TelemetryRefV1, _Mapping]] = ..., anchor: _Optional[_Union[EvidenceAnchorV1, _Mapping]] = ..., source_kind: _Optional[_Union[ArtifactLinkSourceKindV1, str]] = ..., observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[ArtifactLinkStatusV1, str]] = ..., supersedes_link_id: _Optional[str] = ..., correction_sequence: _Optional[int] = ..., provenance: _Optional[_Union[_evaluation_pb2.SemanticConventionProvenanceV1, _Mapping]] = ..., facts_watermark: _Optional[str] = ..., conflict_posture: _Optional[_Union[ArtifactLinkConflictPostureV1, str]] = ..., fallback_reason: _Optional[_Union[ArtifactLinkFallbackReasonV1, str]] = ..., resolver_posture: _Optional[_Union[ArtifactResolverPostureV1, str]] = ...) -> None: ...

class LinkExternalArtifactRequest(_message.Message):
    __slots__ = ("fallback_reason", "principal", "link", "idempotency_key")
    FALLBACK_REASON_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    fallback_reason: ArtifactLinkFallbackReasonV1
    principal: _evaluation_pb2.PrincipalRefV1
    link: ArtifactLinkV1
    idempotency_key: str
    def __init__(self, fallback_reason: _Optional[_Union[ArtifactLinkFallbackReasonV1, str]] = ..., principal: _Optional[_Union[_evaluation_pb2.PrincipalRefV1, _Mapping]] = ..., link: _Optional[_Union[ArtifactLinkV1, _Mapping]] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class LinkExternalArtifactResponse(_message.Message):
    __slots__ = ("link", "rejection_reason_code")
    LINK_FIELD_NUMBER: _ClassVar[int]
    REJECTION_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    link: ArtifactLinkV1
    rejection_reason_code: str
    def __init__(self, link: _Optional[_Union[ArtifactLinkV1, _Mapping]] = ..., rejection_reason_code: _Optional[str] = ...) -> None: ...
