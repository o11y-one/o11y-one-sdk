import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from o11y_one.common.v1 import common_pb2 as _common_pb2
from o11y_one.agentic.v1 import agentic_pb2 as _agentic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrincipalKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRINCIPAL_KIND_V1_UNSPECIFIED: _ClassVar[PrincipalKindV1]
    PRINCIPAL_KIND_V1_USER: _ClassVar[PrincipalKindV1]
    PRINCIPAL_KIND_V1_MACHINE: _ClassVar[PrincipalKindV1]
    PRINCIPAL_KIND_V1_SYSTEM: _ClassVar[PrincipalKindV1]

class CompletenessStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPLETENESS_STATE_V1_UNSPECIFIED: _ClassVar[CompletenessStateV1]
    COMPLETENESS_STATE_V1_COMPLETE: _ClassVar[CompletenessStateV1]
    COMPLETENESS_STATE_V1_INCOMPLETE: _ClassVar[CompletenessStateV1]
    COMPLETENESS_STATE_V1_STALE: _ClassVar[CompletenessStateV1]
    COMPLETENESS_STATE_V1_UNAVAILABLE: _ClassVar[CompletenessStateV1]

class MetricAvailabilityStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METRIC_AVAILABILITY_STATE_V1_UNSPECIFIED: _ClassVar[MetricAvailabilityStateV1]
    METRIC_AVAILABILITY_STATE_V1_AVAILABLE: _ClassVar[MetricAvailabilityStateV1]
    METRIC_AVAILABILITY_STATE_V1_NOT_SUPPORTED: _ClassVar[MetricAvailabilityStateV1]
    METRIC_AVAILABILITY_STATE_V1_NOT_OBSERVED: _ClassVar[MetricAvailabilityStateV1]
    METRIC_AVAILABILITY_STATE_V1_REDACTED: _ClassVar[MetricAvailabilityStateV1]
    METRIC_AVAILABILITY_STATE_V1_SAMPLED_OUT: _ClassVar[MetricAvailabilityStateV1]
    METRIC_AVAILABILITY_STATE_V1_NOT_SAMPLED: _ClassVar[MetricAvailabilityStateV1]
    METRIC_AVAILABILITY_STATE_V1_PENDING: _ClassVar[MetricAvailabilityStateV1]
    METRIC_AVAILABILITY_STATE_V1_ERROR: _ClassVar[MetricAvailabilityStateV1]

class EvaluationActionKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_ACTION_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationActionKindV1]
    EVALUATION_ACTION_KIND_V1_VIEW: _ClassVar[EvaluationActionKindV1]
    EVALUATION_ACTION_KIND_V1_EDIT: _ClassVar[EvaluationActionKindV1]
    EVALUATION_ACTION_KIND_V1_DUPLICATE: _ClassVar[EvaluationActionKindV1]
    EVALUATION_ACTION_KIND_V1_ARCHIVE: _ClassVar[EvaluationActionKindV1]
    EVALUATION_ACTION_KIND_V1_UNARCHIVE: _ClassVar[EvaluationActionKindV1]
    EVALUATION_ACTION_KIND_V1_LAUNCH_RUN: _ClassVar[EvaluationActionKindV1]
    EVALUATION_ACTION_KIND_V1_CANCEL_RUN: _ClassVar[EvaluationActionKindV1]
    EVALUATION_ACTION_KIND_V1_RETRY_CELLS: _ClassVar[EvaluationActionKindV1]
    EVALUATION_ACTION_KIND_V1_RETRY_SCORERS: _ClassVar[EvaluationActionKindV1]

class ActionBlockedReasonV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTION_BLOCKED_REASON_V1_UNSPECIFIED: _ClassVar[ActionBlockedReasonV1]
    ACTION_BLOCKED_REASON_V1_PERMISSION_DENIED: _ClassVar[ActionBlockedReasonV1]
    ACTION_BLOCKED_REASON_V1_INVALID_LIFECYCLE_STATE: _ClassVar[ActionBlockedReasonV1]
    ACTION_BLOCKED_REASON_V1_CAPABILITY_UNAVAILABLE: _ClassVar[ActionBlockedReasonV1]
    ACTION_BLOCKED_REASON_V1_DEPENDENCY_ARCHIVED: _ClassVar[ActionBlockedReasonV1]
    ACTION_BLOCKED_REASON_V1_EVIDENCE_INCOMPLETE: _ClassVar[ActionBlockedReasonV1]

class CapabilityStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CAPABILITY_STATE_V1_UNSPECIFIED: _ClassVar[CapabilityStateV1]
    CAPABILITY_STATE_V1_AVAILABLE: _ClassVar[CapabilityStateV1]
    CAPABILITY_STATE_V1_UNAVAILABLE: _ClassVar[CapabilityStateV1]
    CAPABILITY_STATE_V1_DEGRADED: _ClassVar[CapabilityStateV1]
    CAPABILITY_STATE_V1_NOT_LICENSED: _ClassVar[CapabilityStateV1]

class EvaluationDefinitionStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_DEFINITION_STATE_V1_UNSPECIFIED: _ClassVar[EvaluationDefinitionStateV1]
    EVALUATION_DEFINITION_STATE_V1_ACTIVE: _ClassVar[EvaluationDefinitionStateV1]
    EVALUATION_DEFINITION_STATE_V1_ARCHIVED: _ClassVar[EvaluationDefinitionStateV1]

class EvaluationRunStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_RUN_STATE_V1_UNSPECIFIED: _ClassVar[EvaluationRunStateV1]
    EVALUATION_RUN_STATE_V1_DRAFT_PREVIEWED: _ClassVar[EvaluationRunStateV1]
    EVALUATION_RUN_STATE_V1_PREPARING: _ClassVar[EvaluationRunStateV1]
    EVALUATION_RUN_STATE_V1_RUNNING: _ClassVar[EvaluationRunStateV1]
    EVALUATION_RUN_STATE_V1_AWAITING_REVIEW: _ClassVar[EvaluationRunStateV1]
    EVALUATION_RUN_STATE_V1_COMPLETED: _ClassVar[EvaluationRunStateV1]
    EVALUATION_RUN_STATE_V1_PARTIALLY_COMPLETED: _ClassVar[EvaluationRunStateV1]
    EVALUATION_RUN_STATE_V1_FAILED: _ClassVar[EvaluationRunStateV1]
    EVALUATION_RUN_STATE_V1_CANCELLED: _ClassVar[EvaluationRunStateV1]

class EvaluationExecutionStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_EXECUTION_STATE_V1_UNSPECIFIED: _ClassVar[EvaluationExecutionStateV1]
    EVALUATION_EXECUTION_STATE_V1_PREPARED: _ClassVar[EvaluationExecutionStateV1]
    EVALUATION_EXECUTION_STATE_V1_QUEUED: _ClassVar[EvaluationExecutionStateV1]
    EVALUATION_EXECUTION_STATE_V1_LEASED: _ClassVar[EvaluationExecutionStateV1]
    EVALUATION_EXECUTION_STATE_V1_RUNNING: _ClassVar[EvaluationExecutionStateV1]
    EVALUATION_EXECUTION_STATE_V1_AWAITING_SUBMISSION: _ClassVar[EvaluationExecutionStateV1]
    EVALUATION_EXECUTION_STATE_V1_SUCCEEDED: _ClassVar[EvaluationExecutionStateV1]
    EVALUATION_EXECUTION_STATE_V1_FAILED: _ClassVar[EvaluationExecutionStateV1]
    EVALUATION_EXECUTION_STATE_V1_TIMED_OUT: _ClassVar[EvaluationExecutionStateV1]
    EVALUATION_EXECUTION_STATE_V1_LEASE_EXPIRED: _ClassVar[EvaluationExecutionStateV1]
    EVALUATION_EXECUTION_STATE_V1_CANCELLED: _ClassVar[EvaluationExecutionStateV1]
    EVALUATION_EXECUTION_STATE_V1_SKIPPED: _ClassVar[EvaluationExecutionStateV1]
    EVALUATION_EXECUTION_STATE_V1_SUPERSEDED: _ClassVar[EvaluationExecutionStateV1]

class EvaluationLaunchModeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_LAUNCH_MODE_V1_UNSPECIFIED: _ClassVar[EvaluationLaunchModeV1]
    EVALUATION_LAUNCH_MODE_V1_COMPARISON: _ClassVar[EvaluationLaunchModeV1]
    EVALUATION_LAUNCH_MODE_V1_VALIDATION: _ClassVar[EvaluationLaunchModeV1]
    EVALUATION_LAUNCH_MODE_V1_SCRATCH: _ClassVar[EvaluationLaunchModeV1]

class EvaluationSubjectKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_SUBJECT_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationSubjectKindV1]
    EVALUATION_SUBJECT_KIND_V1_RESPONSE: _ClassVar[EvaluationSubjectKindV1]
    EVALUATION_SUBJECT_KIND_V1_CONVERSATION_TURN: _ClassVar[EvaluationSubjectKindV1]
    EVALUATION_SUBJECT_KIND_V1_CONVERSATION: _ClassVar[EvaluationSubjectKindV1]
    EVALUATION_SUBJECT_KIND_V1_TRAJECTORY: _ClassVar[EvaluationSubjectKindV1]
    EVALUATION_SUBJECT_KIND_V1_MODEL_GENERATION: _ClassVar[EvaluationSubjectKindV1]
    EVALUATION_SUBJECT_KIND_V1_TOOL_CALL: _ClassVar[EvaluationSubjectKindV1]
    EVALUATION_SUBJECT_KIND_V1_RETRIEVAL_OPERATION: _ClassVar[EvaluationSubjectKindV1]

class CohortNormalizationModeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COHORT_NORMALIZATION_MODE_V1_UNSPECIFIED: _ClassVar[CohortNormalizationModeV1]
    COHORT_NORMALIZATION_MODE_V1_NONE: _ClassVar[CohortNormalizationModeV1]
    COHORT_NORMALIZATION_MODE_V1_EQUAL_WEIGHT: _ClassVar[CohortNormalizationModeV1]
    COHORT_NORMALIZATION_MODE_V1_CASE_COUNT_WEIGHT: _ClassVar[CohortNormalizationModeV1]

class EvaluationCandidateKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_CANDIDATE_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationCandidateKindV1]
    EVALUATION_CANDIDATE_KIND_V1_RECORDED_OUTPUT: _ClassVar[EvaluationCandidateKindV1]
    EVALUATION_CANDIDATE_KIND_V1_PROVIDER_PROMPT: _ClassVar[EvaluationCandidateKindV1]
    EVALUATION_CANDIDATE_KIND_V1_HTTP_JSON_ENDPOINT: _ClassVar[EvaluationCandidateKindV1]
    EVALUATION_CANDIDATE_KIND_V1_EXPERIMENT_TARGET_REF: _ClassVar[EvaluationCandidateKindV1]
    EVALUATION_CANDIDATE_KIND_V1_AGENT_RELEASE_REVISION: _ClassVar[EvaluationCandidateKindV1]
    EVALUATION_CANDIDATE_KIND_V1_EXTERNALLY_EXECUTED: _ClassVar[EvaluationCandidateKindV1]
    EVALUATION_CANDIDATE_KIND_V1_CONVERSATION_SIMULATION: _ClassVar[EvaluationCandidateKindV1]

class ConversationTerminationKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONVERSATION_TERMINATION_KIND_V1_UNSPECIFIED: _ClassVar[ConversationTerminationKindV1]
    CONVERSATION_TERMINATION_KIND_V1_MAX_TURNS: _ClassVar[ConversationTerminationKindV1]
    CONVERSATION_TERMINATION_KIND_V1_GOAL_SATISFIED: _ClassVar[ConversationTerminationKindV1]
    CONVERSATION_TERMINATION_KIND_V1_SIMULATED_USER_EXIT: _ClassVar[ConversationTerminationKindV1]

class SideEffectPostureV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIDE_EFFECT_POSTURE_V1_UNSPECIFIED: _ClassVar[SideEffectPostureV1]
    SIDE_EFFECT_POSTURE_V1_NONE: _ClassVar[SideEffectPostureV1]
    SIDE_EFFECT_POSTURE_V1_IDEMPOTENT_READS: _ClassVar[SideEffectPostureV1]
    SIDE_EFFECT_POSTURE_V1_MUTATING_ATTESTED: _ClassVar[SideEffectPostureV1]
    SIDE_EFFECT_POSTURE_V1_UNATTESTED: _ClassVar[SideEffectPostureV1]

class EvaluationScorerTargetKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_SCORER_TARGET_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationScorerTargetKindV1]
    EVALUATION_SCORER_TARGET_KIND_V1_SUITE_REF: _ClassVar[EvaluationScorerTargetKindV1]
    EVALUATION_SCORER_TARGET_KIND_V1_EXPLICIT_LIST: _ClassVar[EvaluationScorerTargetKindV1]

class EvaluationScorerSuiteCombineRuleV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_SCORER_SUITE_COMBINE_RULE_V1_UNSPECIFIED: _ClassVar[EvaluationScorerSuiteCombineRuleV1]
    EVALUATION_SCORER_SUITE_COMBINE_RULE_V1_GATES_THEN_WEIGHTED_MEAN: _ClassVar[EvaluationScorerSuiteCombineRuleV1]

class EvaluationDecisionRuleKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_DECISION_RULE_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationDecisionRuleKindV1]
    EVALUATION_DECISION_RULE_KIND_V1_MIN_SCORE: _ClassVar[EvaluationDecisionRuleKindV1]
    EVALUATION_DECISION_RULE_KIND_V1_MAX_REGRESSION: _ClassVar[EvaluationDecisionRuleKindV1]
    EVALUATION_DECISION_RULE_KIND_V1_MAX_COST: _ClassVar[EvaluationDecisionRuleKindV1]
    EVALUATION_DECISION_RULE_KIND_V1_MIN_COVERAGE: _ClassVar[EvaluationDecisionRuleKindV1]

class EvaluationTrialsSourceV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_TRIALS_SOURCE_V1_UNSPECIFIED: _ClassVar[EvaluationTrialsSourceV1]
    EVALUATION_TRIALS_SOURCE_V1_AUTHORED: _ClassVar[EvaluationTrialsSourceV1]
    EVALUATION_TRIALS_SOURCE_V1_COMPARISON_DEFAULT: _ClassVar[EvaluationTrialsSourceV1]
    EVALUATION_TRIALS_SOURCE_V1_SINGLE_CANDIDATE_DEFAULT: _ClassVar[EvaluationTrialsSourceV1]

class EvaluationDefinitionConflictSectionV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_DEFINITION_CONFLICT_SECTION_V1_UNSPECIFIED: _ClassVar[EvaluationDefinitionConflictSectionV1]
    EVALUATION_DEFINITION_CONFLICT_SECTION_V1_IDENTITY: _ClassVar[EvaluationDefinitionConflictSectionV1]
    EVALUATION_DEFINITION_CONFLICT_SECTION_V1_COHORTS: _ClassVar[EvaluationDefinitionConflictSectionV1]
    EVALUATION_DEFINITION_CONFLICT_SECTION_V1_CANDIDATES: _ClassVar[EvaluationDefinitionConflictSectionV1]
    EVALUATION_DEFINITION_CONFLICT_SECTION_V1_SCORERS: _ClassVar[EvaluationDefinitionConflictSectionV1]
    EVALUATION_DEFINITION_CONFLICT_SECTION_V1_EXECUTION_POLICY: _ClassVar[EvaluationDefinitionConflictSectionV1]
    EVALUATION_DEFINITION_CONFLICT_SECTION_V1_BUDGET: _ClassVar[EvaluationDefinitionConflictSectionV1]
    EVALUATION_DEFINITION_CONFLICT_SECTION_V1_DECISION_POLICY: _ClassVar[EvaluationDefinitionConflictSectionV1]
    EVALUATION_DEFINITION_CONFLICT_SECTION_V1_HUMAN_REVIEW: _ClassVar[EvaluationDefinitionConflictSectionV1]
    EVALUATION_DEFINITION_CONFLICT_SECTION_V1_METADATA: _ClassVar[EvaluationDefinitionConflictSectionV1]

class EvaluationDefinitionSortKeyV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_DEFINITION_SORT_KEY_V1_UNSPECIFIED: _ClassVar[EvaluationDefinitionSortKeyV1]
    EVALUATION_DEFINITION_SORT_KEY_V1_CREATED_AT: _ClassVar[EvaluationDefinitionSortKeyV1]
    EVALUATION_DEFINITION_SORT_KEY_V1_UPDATED_AT: _ClassVar[EvaluationDefinitionSortKeyV1]
    EVALUATION_DEFINITION_SORT_KEY_V1_DISPLAY_NAME: _ClassVar[EvaluationDefinitionSortKeyV1]

class EvaluationBuilderReadinessSeverityV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_BUILDER_READINESS_SEVERITY_V1_UNSPECIFIED: _ClassVar[EvaluationBuilderReadinessSeverityV1]
    EVALUATION_BUILDER_READINESS_SEVERITY_V1_INFO: _ClassVar[EvaluationBuilderReadinessSeverityV1]
    EVALUATION_BUILDER_READINESS_SEVERITY_V1_WARNING: _ClassVar[EvaluationBuilderReadinessSeverityV1]
    EVALUATION_BUILDER_READINESS_SEVERITY_V1_BLOCKING: _ClassVar[EvaluationBuilderReadinessSeverityV1]

class EvaluationBuilderSectionV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_BUILDER_SECTION_V1_UNSPECIFIED: _ClassVar[EvaluationBuilderSectionV1]
    EVALUATION_BUILDER_SECTION_V1_WORKLOAD: _ClassVar[EvaluationBuilderSectionV1]
    EVALUATION_BUILDER_SECTION_V1_CANDIDATES: _ClassVar[EvaluationBuilderSectionV1]
    EVALUATION_BUILDER_SECTION_V1_SCORECARD: _ClassVar[EvaluationBuilderSectionV1]
    EVALUATION_BUILDER_SECTION_V1_CREDENTIALS: _ClassVar[EvaluationBuilderSectionV1]
    EVALUATION_BUILDER_SECTION_V1_EXECUTION: _ClassVar[EvaluationBuilderSectionV1]

class EvaluationFailureStageV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_FAILURE_STAGE_V1_UNSPECIFIED: _ClassVar[EvaluationFailureStageV1]
    EVALUATION_FAILURE_STAGE_V1_PREPARATION: _ClassVar[EvaluationFailureStageV1]
    EVALUATION_FAILURE_STAGE_V1_COHORT_RESOLUTION: _ClassVar[EvaluationFailureStageV1]
    EVALUATION_FAILURE_STAGE_V1_CANDIDATE_EXECUTION: _ClassVar[EvaluationFailureStageV1]
    EVALUATION_FAILURE_STAGE_V1_SUBJECT_RESOLUTION: _ClassVar[EvaluationFailureStageV1]
    EVALUATION_FAILURE_STAGE_V1_SCORER_EXECUTION: _ClassVar[EvaluationFailureStageV1]
    EVALUATION_FAILURE_STAGE_V1_AGGREGATION: _ClassVar[EvaluationFailureStageV1]
    EVALUATION_FAILURE_STAGE_V1_FACT_PUBLICATION: _ClassVar[EvaluationFailureStageV1]
    EVALUATION_FAILURE_STAGE_V1_HUMAN_REVIEW: _ClassVar[EvaluationFailureStageV1]
    EVALUATION_FAILURE_STAGE_V1_EXTERNAL_LEASE: _ClassVar[EvaluationFailureStageV1]

class RetryabilityV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RETRYABILITY_V1_UNSPECIFIED: _ClassVar[RetryabilityV1]
    RETRYABILITY_V1_RETRYABLE: _ClassVar[RetryabilityV1]
    RETRYABILITY_V1_NOT_RETRYABLE: _ClassVar[RetryabilityV1]
    RETRYABILITY_V1_RETRYABLE_AFTER_FIX: _ClassVar[RetryabilityV1]

class RecoveryActionV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RECOVERY_ACTION_V1_UNSPECIFIED: _ClassVar[RecoveryActionV1]
    RECOVERY_ACTION_V1_RETRY: _ClassVar[RecoveryActionV1]
    RECOVERY_ACTION_V1_RE_PREVIEW: _ClassVar[RecoveryActionV1]
    RECOVERY_ACTION_V1_EDIT_DEFINITION: _ClassVar[RecoveryActionV1]
    RECOVERY_ACTION_V1_WAIT: _ClassVar[RecoveryActionV1]
    RECOVERY_ACTION_V1_CONTACT_SUPPORT: _ClassVar[RecoveryActionV1]

class EvaluationRateSourceV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_RATE_SOURCE_V1_UNSPECIFIED: _ClassVar[EvaluationRateSourceV1]
    EVALUATION_RATE_SOURCE_V1_CANDIDATE_AUTHORED: _ClassVar[EvaluationRateSourceV1]
    EVALUATION_RATE_SOURCE_V1_STATIC_REGISTRY: _ClassVar[EvaluationRateSourceV1]
    EVALUATION_RATE_SOURCE_V1_STATIC_REGISTRY_PROVISIONAL: _ClassVar[EvaluationRateSourceV1]
    EVALUATION_RATE_SOURCE_V1_ORG_NEGOTIATED_OVERRIDE: _ClassVar[EvaluationRateSourceV1]

class EvaluationRateModifierKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_RATE_MODIFIER_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationRateModifierKindV1]
    EVALUATION_RATE_MODIFIER_KIND_V1_CONTEXT_LENGTH_TIER: _ClassVar[EvaluationRateModifierKindV1]
    EVALUATION_RATE_MODIFIER_KIND_V1_SERVICE_TIER: _ClassVar[EvaluationRateModifierKindV1]
    EVALUATION_RATE_MODIFIER_KIND_V1_BATCH_DISCOUNT: _ClassVar[EvaluationRateModifierKindV1]
    EVALUATION_RATE_MODIFIER_KIND_V1_OFF_PEAK_WINDOW: _ClassVar[EvaluationRateModifierKindV1]
    EVALUATION_RATE_MODIFIER_KIND_V1_LONG_OUTPUT_TIER: _ClassVar[EvaluationRateModifierKindV1]
    EVALUATION_RATE_MODIFIER_KIND_V1_CACHE_TTL_TIER: _ClassVar[EvaluationRateModifierKindV1]
    EVALUATION_RATE_MODIFIER_KIND_V1_REGIONAL_UPLIFT: _ClassVar[EvaluationRateModifierKindV1]
    EVALUATION_RATE_MODIFIER_KIND_V1_NON_TOKEN_CHARGE: _ClassVar[EvaluationRateModifierKindV1]

class EvaluationRateStalenessV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_RATE_STALENESS_V1_UNSPECIFIED: _ClassVar[EvaluationRateStalenessV1]
    EVALUATION_RATE_STALENESS_V1_FRESH: _ClassVar[EvaluationRateStalenessV1]
    EVALUATION_RATE_STALENESS_V1_STALE: _ClassVar[EvaluationRateStalenessV1]

class EvaluationOperationKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_OPERATION_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationOperationKindV1]
    EVALUATION_OPERATION_KIND_V1_PREPARE_RUN: _ClassVar[EvaluationOperationKindV1]
    EVALUATION_OPERATION_KIND_V1_RETRY_CELLS: _ClassVar[EvaluationOperationKindV1]
    EVALUATION_OPERATION_KIND_V1_CANCEL_RUN: _ClassVar[EvaluationOperationKindV1]
    EVALUATION_OPERATION_KIND_V1_EXPORT: _ClassVar[EvaluationOperationKindV1]

class EvaluationOperationStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_OPERATION_STATE_V1_UNSPECIFIED: _ClassVar[EvaluationOperationStateV1]
    EVALUATION_OPERATION_STATE_V1_PENDING: _ClassVar[EvaluationOperationStateV1]
    EVALUATION_OPERATION_STATE_V1_RUNNING: _ClassVar[EvaluationOperationStateV1]
    EVALUATION_OPERATION_STATE_V1_SUCCEEDED: _ClassVar[EvaluationOperationStateV1]
    EVALUATION_OPERATION_STATE_V1_FAILED: _ClassVar[EvaluationOperationStateV1]
    EVALUATION_OPERATION_STATE_V1_CANCELLED: _ClassVar[EvaluationOperationStateV1]

class EvaluationPreviewBlockerKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_PREVIEW_BLOCKER_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationPreviewBlockerKindV1]
    EVALUATION_PREVIEW_BLOCKER_KIND_V1_SCALE_LIMIT_EXCEEDED: _ClassVar[EvaluationPreviewBlockerKindV1]
    EVALUATION_PREVIEW_BLOCKER_KIND_V1_CAPABILITY_UNAVAILABLE: _ClassVar[EvaluationPreviewBlockerKindV1]
    EVALUATION_PREVIEW_BLOCKER_KIND_V1_MISSING_DEPENDENCY: _ClassVar[EvaluationPreviewBlockerKindV1]
    EVALUATION_PREVIEW_BLOCKER_KIND_V1_UNATTESTED_SIDE_EFFECT: _ClassVar[EvaluationPreviewBlockerKindV1]
    EVALUATION_PREVIEW_BLOCKER_KIND_V1_SCORER_BINDING_INCOMPLETE: _ClassVar[EvaluationPreviewBlockerKindV1]

class EvaluationLaunchRejectionKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_LAUNCH_REJECTION_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationLaunchRejectionKindV1]
    EVALUATION_LAUNCH_REJECTION_KIND_V1_PREVIEW_EXPIRED: _ClassVar[EvaluationLaunchRejectionKindV1]
    EVALUATION_LAUNCH_REJECTION_KIND_V1_PREVIEW_MALFORMED: _ClassVar[EvaluationLaunchRejectionKindV1]
    EVALUATION_LAUNCH_REJECTION_KIND_V1_DEFINITION_REVISION_MOVED: _ClassVar[EvaluationLaunchRejectionKindV1]
    EVALUATION_LAUNCH_REJECTION_KIND_V1_DEPENDENCY_VERSIONS_MOVED: _ClassVar[EvaluationLaunchRejectionKindV1]
    EVALUATION_LAUNCH_REJECTION_KIND_V1_CARDINALITY_MOVED: _ClassVar[EvaluationLaunchRejectionKindV1]
    EVALUATION_LAUNCH_REJECTION_KIND_V1_CAPABILITY_SET_MOVED: _ClassVar[EvaluationLaunchRejectionKindV1]
    EVALUATION_LAUNCH_REJECTION_KIND_V1_IDEMPOTENCY_KEY_REUSED: _ClassVar[EvaluationLaunchRejectionKindV1]

class EvaluationRetryIneligibilityV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_RETRY_INELIGIBILITY_V1_UNSPECIFIED: _ClassVar[EvaluationRetryIneligibilityV1]
    EVALUATION_RETRY_INELIGIBILITY_V1_CELL_SUCCEEDED_IMMUTABLE: _ClassVar[EvaluationRetryIneligibilityV1]
    EVALUATION_RETRY_INELIGIBILITY_V1_CELL_NOT_TERMINAL: _ClassVar[EvaluationRetryIneligibilityV1]
    EVALUATION_RETRY_INELIGIBILITY_V1_CELL_SKIPPED_BY_BUDGET: _ClassVar[EvaluationRetryIneligibilityV1]
    EVALUATION_RETRY_INELIGIBILITY_V1_CELL_CANCELLED: _ClassVar[EvaluationRetryIneligibilityV1]
    EVALUATION_RETRY_INELIGIBILITY_V1_CELL_AWAITING_REVIEW: _ClassVar[EvaluationRetryIneligibilityV1]
    EVALUATION_RETRY_INELIGIBILITY_V1_CELL_UNKNOWN: _ClassVar[EvaluationRetryIneligibilityV1]

class EvaluationScorerRetryIneligibilityV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_SCORER_RETRY_INELIGIBILITY_V1_UNSPECIFIED: _ClassVar[EvaluationScorerRetryIneligibilityV1]
    EVALUATION_SCORER_RETRY_INELIGIBILITY_V1_CANDIDATE_OUTPUT_ABSENT: _ClassVar[EvaluationScorerRetryIneligibilityV1]
    EVALUATION_SCORER_RETRY_INELIGIBILITY_V1_SCORER_NOT_DETERMINISTIC: _ClassVar[EvaluationScorerRetryIneligibilityV1]
    EVALUATION_SCORER_RETRY_INELIGIBILITY_V1_ATTEMPT_CEILING_REACHED: _ClassVar[EvaluationScorerRetryIneligibilityV1]
    EVALUATION_SCORER_RETRY_INELIGIBILITY_V1_COORDINATE_UNKNOWN: _ClassVar[EvaluationScorerRetryIneligibilityV1]
    EVALUATION_SCORER_RETRY_INELIGIBILITY_V1_JUDGE_REGRADE_NOT_DISPATCHABLE: _ClassVar[EvaluationScorerRetryIneligibilityV1]
    EVALUATION_SCORER_RETRY_INELIGIBILITY_V1_JUDGE_REGRADE_REQUIRES_JOB: _ClassVar[EvaluationScorerRetryIneligibilityV1]
    EVALUATION_SCORER_RETRY_INELIGIBILITY_V1_SCORER_IS_A_DERIVED_SUITE: _ClassVar[EvaluationScorerRetryIneligibilityV1]

class CostCategoryV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COST_CATEGORY_V1_UNSPECIFIED: _ClassVar[CostCategoryV1]
    COST_CATEGORY_V1_CANDIDATE_MODEL: _ClassVar[CostCategoryV1]
    COST_CATEGORY_V1_EVALUATOR_MODEL: _ClassVar[CostCategoryV1]
    COST_CATEGORY_V1_TOOL: _ClassVar[CostCategoryV1]
    COST_CATEGORY_V1_RETRIEVAL: _ClassVar[CostCategoryV1]
    COST_CATEGORY_V1_EXTERNAL_API: _ClassVar[CostCategoryV1]

class CostPostureV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COST_POSTURE_V1_UNSPECIFIED: _ClassVar[CostPostureV1]
    COST_POSTURE_V1_ACTUAL_PROVIDER_BILLED: _ClassVar[CostPostureV1]
    COST_POSTURE_V1_ESTIMATED: _ClassVar[CostPostureV1]

class ProviderStatusClassV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROVIDER_STATUS_CLASS_V1_UNSPECIFIED: _ClassVar[ProviderStatusClassV1]
    PROVIDER_STATUS_CLASS_V1_OK: _ClassVar[ProviderStatusClassV1]
    PROVIDER_STATUS_CLASS_V1_CLIENT_ERROR: _ClassVar[ProviderStatusClassV1]
    PROVIDER_STATUS_CLASS_V1_SERVER_ERROR: _ClassVar[ProviderStatusClassV1]
    PROVIDER_STATUS_CLASS_V1_TIMEOUT: _ClassVar[ProviderStatusClassV1]
    PROVIDER_STATUS_CLASS_V1_RATE_LIMITED: _ClassVar[ProviderStatusClassV1]
    PROVIDER_STATUS_CLASS_V1_CANCELLED: _ClassVar[ProviderStatusClassV1]
    PROVIDER_STATUS_CLASS_V1_NOT_APPLICABLE: _ClassVar[ProviderStatusClassV1]

class InstrumentationCompletenessStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INSTRUMENTATION_COMPLETENESS_STATE_V1_UNSPECIFIED: _ClassVar[InstrumentationCompletenessStateV1]
    INSTRUMENTATION_COMPLETENESS_STATE_V1_COMPLETE: _ClassVar[InstrumentationCompletenessStateV1]
    INSTRUMENTATION_COMPLETENESS_STATE_V1_PARTIAL: _ClassVar[InstrumentationCompletenessStateV1]
    INSTRUMENTATION_COMPLETENESS_STATE_V1_UNINSTRUMENTED: _ClassVar[InstrumentationCompletenessStateV1]
    INSTRUMENTATION_COMPLETENESS_STATE_V1_REDACTED: _ClassVar[InstrumentationCompletenessStateV1]
    INSTRUMENTATION_COMPLETENESS_STATE_V1_SAMPLED_OUT: _ClassVar[InstrumentationCompletenessStateV1]
    INSTRUMENTATION_COMPLETENESS_STATE_V1_CONVENTION_ALIAS: _ClassVar[InstrumentationCompletenessStateV1]

class ExecutionMetricsScopeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXECUTION_METRICS_SCOPE_V1_UNSPECIFIED: _ClassVar[ExecutionMetricsScopeV1]
    EXECUTION_METRICS_SCOPE_V1_CANDIDATE_EXECUTION: _ClassVar[ExecutionMetricsScopeV1]
    EXECUTION_METRICS_SCOPE_V1_SCORER_EXECUTION: _ClassVar[ExecutionMetricsScopeV1]
    EXECUTION_METRICS_SCOPE_V1_EVALUATOR_AGGREGATE: _ClassVar[ExecutionMetricsScopeV1]
    EXECUTION_METRICS_SCOPE_V1_EVALUATION_TOTAL: _ClassVar[ExecutionMetricsScopeV1]
    EXECUTION_METRICS_SCOPE_V1_EVALUATOR_EXECUTION: _ClassVar[ExecutionMetricsScopeV1]

class EvaluationVerdictV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_VERDICT_V1_UNSPECIFIED: _ClassVar[EvaluationVerdictV1]
    EVALUATION_VERDICT_V1_PASS: _ClassVar[EvaluationVerdictV1]
    EVALUATION_VERDICT_V1_FAIL: _ClassVar[EvaluationVerdictV1]
    EVALUATION_VERDICT_V1_ERROR: _ClassVar[EvaluationVerdictV1]
    EVALUATION_VERDICT_V1_SKIPPED: _ClassVar[EvaluationVerdictV1]
    EVALUATION_VERDICT_V1_NOT_APPLICABLE: _ClassVar[EvaluationVerdictV1]

class EvaluationCandidateSourceV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_CANDIDATE_SOURCE_V1_UNSPECIFIED: _ClassVar[EvaluationCandidateSourceV1]
    EVALUATION_CANDIDATE_SOURCE_V1_RECORDED_OUTPUT: _ClassVar[EvaluationCandidateSourceV1]
    EVALUATION_CANDIDATE_SOURCE_V1_PROVIDER_CALL: _ClassVar[EvaluationCandidateSourceV1]
    EVALUATION_CANDIDATE_SOURCE_V1_HTTP_ENDPOINT: _ClassVar[EvaluationCandidateSourceV1]
    EVALUATION_CANDIDATE_SOURCE_V1_EXTERNAL_SUBMISSION: _ClassVar[EvaluationCandidateSourceV1]

class EvaluationRunOverviewProfileV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_RUN_OVERVIEW_PROFILE_V1_UNSPECIFIED: _ClassVar[EvaluationRunOverviewProfileV1]
    EVALUATION_RUN_OVERVIEW_PROFILE_V1_INITIAL: _ClassVar[EvaluationRunOverviewProfileV1]
    EVALUATION_RUN_OVERVIEW_PROFILE_V1_FULL: _ClassVar[EvaluationRunOverviewProfileV1]

class EvaluationScorerCompletionStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_SCORER_COMPLETION_STATE_V1_UNSPECIFIED: _ClassVar[EvaluationScorerCompletionStateV1]
    EVALUATION_SCORER_COMPLETION_STATE_V1_NOT_STARTED: _ClassVar[EvaluationScorerCompletionStateV1]
    EVALUATION_SCORER_COMPLETION_STATE_V1_PARTIAL: _ClassVar[EvaluationScorerCompletionStateV1]
    EVALUATION_SCORER_COMPLETION_STATE_V1_COMPLETE: _ClassVar[EvaluationScorerCompletionStateV1]
    EVALUATION_SCORER_COMPLETION_STATE_V1_AWAITING_HUMAN_REVIEW: _ClassVar[EvaluationScorerCompletionStateV1]

class EvaluationResyncReasonV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_RESYNC_REASON_V1_UNSPECIFIED: _ClassVar[EvaluationResyncReasonV1]
    EVALUATION_RESYNC_REASON_V1_SNAPSHOT_SUPERSEDED: _ClassVar[EvaluationResyncReasonV1]
    EVALUATION_RESYNC_REASON_V1_FILTER_CHANGED: _ClassVar[EvaluationResyncReasonV1]
    EVALUATION_RESYNC_REASON_V1_CURSOR_MALFORMED: _ClassVar[EvaluationResyncReasonV1]
    EVALUATION_RESYNC_REASON_V1_BACKLOG_EXCEEDED: _ClassVar[EvaluationResyncReasonV1]

class EvaluationDecisionDriverKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_DECISION_DRIVER_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationDecisionDriverKindV1]
    EVALUATION_DECISION_DRIVER_KIND_V1_SCORER_REGRESSION: _ClassVar[EvaluationDecisionDriverKindV1]
    EVALUATION_DECISION_DRIVER_KIND_V1_SCORER_FAILURE_CONCENTRATION: _ClassVar[EvaluationDecisionDriverKindV1]
    EVALUATION_DECISION_DRIVER_KIND_V1_MISSING_SCORE_EVIDENCE: _ClassVar[EvaluationDecisionDriverKindV1]
    EVALUATION_DECISION_DRIVER_KIND_V1_CANDIDATE_EXECUTION_FAILURE: _ClassVar[EvaluationDecisionDriverKindV1]

class EvaluationDecisionConsequenceV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_DECISION_CONSEQUENCE_V1_UNSPECIFIED: _ClassVar[EvaluationDecisionConsequenceV1]
    EVALUATION_DECISION_CONSEQUENCE_V1_BLOCKS_RELEASE_GATE: _ClassVar[EvaluationDecisionConsequenceV1]
    EVALUATION_DECISION_CONSEQUENCE_V1_QUALITY_REGRESSION: _ClassVar[EvaluationDecisionConsequenceV1]
    EVALUATION_DECISION_CONSEQUENCE_V1_QUALITY_FAILURE: _ClassVar[EvaluationDecisionConsequenceV1]
    EVALUATION_DECISION_CONSEQUENCE_V1_EVIDENCE_INCOMPLETE: _ClassVar[EvaluationDecisionConsequenceV1]

class StatisticalTestV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATISTICAL_TEST_V1_UNSPECIFIED: _ClassVar[StatisticalTestV1]
    STATISTICAL_TEST_V1_MCNEMAR_EXACT: _ClassVar[StatisticalTestV1]

class MultipleComparisonCorrectionV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MULTIPLE_COMPARISON_CORRECTION_V1_UNSPECIFIED: _ClassVar[MultipleComparisonCorrectionV1]
    MULTIPLE_COMPARISON_CORRECTION_V1_NONE: _ClassVar[MultipleComparisonCorrectionV1]
    MULTIPLE_COMPARISON_CORRECTION_V1_HOLM: _ClassVar[MultipleComparisonCorrectionV1]

class StatisticalValidityV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATISTICAL_VALIDITY_V1_UNSPECIFIED: _ClassVar[StatisticalValidityV1]
    STATISTICAL_VALIDITY_V1_VALID: _ClassVar[StatisticalValidityV1]
    STATISTICAL_VALIDITY_V1_INSUFFICIENT_SAMPLE: _ClassVar[StatisticalValidityV1]
    STATISTICAL_VALIDITY_V1_NOT_APPLICABLE: _ClassVar[StatisticalValidityV1]

class EvaluationRepeatBasisV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_REPEAT_BASIS_V1_UNSPECIFIED: _ClassVar[EvaluationRepeatBasisV1]
    EVALUATION_REPEAT_BASIS_V1_SCORED_ROLLOUTS: _ClassVar[EvaluationRepeatBasisV1]
    EVALUATION_REPEAT_BASIS_V1_PREPARED_ROLLOUTS: _ClassVar[EvaluationRepeatBasisV1]

class ComparisonAlignmentRuleV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPARISON_ALIGNMENT_RULE_V1_UNSPECIFIED: _ClassVar[ComparisonAlignmentRuleV1]
    COMPARISON_ALIGNMENT_RULE_V1_SINGLE_ROLLOUT: _ClassVar[ComparisonAlignmentRuleV1]
    COMPARISON_ALIGNMENT_RULE_V1_MAJORITY_TIE_IS_NEITHER_WIN: _ClassVar[ComparisonAlignmentRuleV1]

class EvaluationSliceDimensionV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_SLICE_DIMENSION_V1_UNSPECIFIED: _ClassVar[EvaluationSliceDimensionV1]
    EVALUATION_SLICE_DIMENSION_V1_COHORT: _ClassVar[EvaluationSliceDimensionV1]

class DataQualityFindingKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATA_QUALITY_FINDING_KIND_V1_UNSPECIFIED: _ClassVar[DataQualityFindingKindV1]
    DATA_QUALITY_FINDING_KIND_V1_DUPLICATE_CASES: _ClassVar[DataQualityFindingKindV1]
    DATA_QUALITY_FINDING_KIND_V1_MISSING_GROUND_TRUTH: _ClassVar[DataQualityFindingKindV1]
    DATA_QUALITY_FINDING_KIND_V1_UNSCORED_EVIDENCE: _ClassVar[DataQualityFindingKindV1]
    DATA_QUALITY_FINDING_KIND_V1_COHORT_COVERAGE_GAP: _ClassVar[DataQualityFindingKindV1]
    DATA_QUALITY_FINDING_KIND_V1_CONFLICTING_EXPECTED_OUTPUT: _ClassVar[DataQualityFindingKindV1]
    DATA_QUALITY_FINDING_KIND_V1_LEAKAGE_SIGNAL: _ClassVar[DataQualityFindingKindV1]
    DATA_QUALITY_FINDING_KIND_V1_DISTRIBUTION_DRIFT: _ClassVar[DataQualityFindingKindV1]

class FindingSeverityV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FINDING_SEVERITY_V1_UNSPECIFIED: _ClassVar[FindingSeverityV1]
    FINDING_SEVERITY_V1_INFO: _ClassVar[FindingSeverityV1]
    FINDING_SEVERITY_V1_WARNING: _ClassVar[FindingSeverityV1]
    FINDING_SEVERITY_V1_BLOCKING: _ClassVar[FindingSeverityV1]

class EvaluationDecisionOutcomeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_DECISION_OUTCOME_V1_UNSPECIFIED: _ClassVar[EvaluationDecisionOutcomeV1]
    EVALUATION_DECISION_OUTCOME_V1_RECOMMENDED: _ClassVar[EvaluationDecisionOutcomeV1]
    EVALUATION_DECISION_OUTCOME_V1_NO_CLEAR_WINNER: _ClassVar[EvaluationDecisionOutcomeV1]
    EVALUATION_DECISION_OUTCOME_V1_INSUFFICIENT_EVIDENCE: _ClassVar[EvaluationDecisionOutcomeV1]
    EVALUATION_DECISION_OUTCOME_V1_BLOCKED: _ClassVar[EvaluationDecisionOutcomeV1]

class EvaluationDecisionProvenanceV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_DECISION_PROVENANCE_V1_UNSPECIFIED: _ClassVar[EvaluationDecisionProvenanceV1]
    EVALUATION_DECISION_PROVENANCE_V1_ADOPTED: _ClassVar[EvaluationDecisionProvenanceV1]
    EVALUATION_DECISION_PROVENANCE_V1_EXPLORATION: _ClassVar[EvaluationDecisionProvenanceV1]

class DecisionBlockerKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DECISION_BLOCKER_KIND_V1_UNSPECIFIED: _ClassVar[DecisionBlockerKindV1]
    DECISION_BLOCKER_KIND_V1_MIN_SCORE_NOT_MET: _ClassVar[DecisionBlockerKindV1]
    DECISION_BLOCKER_KIND_V1_MAX_REGRESSION_EXCEEDED: _ClassVar[DecisionBlockerKindV1]
    DECISION_BLOCKER_KIND_V1_MAX_COST_EXCEEDED: _ClassVar[DecisionBlockerKindV1]
    DECISION_BLOCKER_KIND_V1_MIN_COVERAGE_NOT_MET: _ClassVar[DecisionBlockerKindV1]
    DECISION_BLOCKER_KIND_V1_EVIDENCE_INCOMPLETE: _ClassVar[DecisionBlockerKindV1]
    DECISION_BLOCKER_KIND_V1_NOT_COMPARABLE: _ClassVar[DecisionBlockerKindV1]

class EvaluationMatrixSortKeyV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_MATRIX_SORT_KEY_V1_UNSPECIFIED: _ClassVar[EvaluationMatrixSortKeyV1]
    EVALUATION_MATRIX_SORT_KEY_V1_DECISION_IMPACT: _ClassVar[EvaluationMatrixSortKeyV1]
    EVALUATION_MATRIX_SORT_KEY_V1_CASE_ORDER: _ClassVar[EvaluationMatrixSortKeyV1]

class EvaluationMatrixDecisionImpactV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_MATRIX_DECISION_IMPACT_V1_UNSPECIFIED: _ClassVar[EvaluationMatrixDecisionImpactV1]
    EVALUATION_MATRIX_DECISION_IMPACT_V1_REGRESSED: _ClassVar[EvaluationMatrixDecisionImpactV1]
    EVALUATION_MATRIX_DECISION_IMPACT_V1_IMPROVED: _ClassVar[EvaluationMatrixDecisionImpactV1]
    EVALUATION_MATRIX_DECISION_IMPACT_V1_UNCHANGED: _ClassVar[EvaluationMatrixDecisionImpactV1]
    EVALUATION_MATRIX_DECISION_IMPACT_V1_DISAGREEMENT: _ClassVar[EvaluationMatrixDecisionImpactV1]
    EVALUATION_MATRIX_DECISION_IMPACT_V1_MISSING_EVIDENCE: _ClassVar[EvaluationMatrixDecisionImpactV1]

class EvaluationMatrixEvidenceStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_MATRIX_EVIDENCE_STATE_V1_UNSPECIFIED: _ClassVar[EvaluationMatrixEvidenceStateV1]
    EVALUATION_MATRIX_EVIDENCE_STATE_V1_COMPLETE: _ClassVar[EvaluationMatrixEvidenceStateV1]
    EVALUATION_MATRIX_EVIDENCE_STATE_V1_PARTIAL: _ClassVar[EvaluationMatrixEvidenceStateV1]
    EVALUATION_MATRIX_EVIDENCE_STATE_V1_CANDIDATE_FAILED: _ClassVar[EvaluationMatrixEvidenceStateV1]
    EVALUATION_MATRIX_EVIDENCE_STATE_V1_SCORER_FAILED: _ClassVar[EvaluationMatrixEvidenceStateV1]
    EVALUATION_MATRIX_EVIDENCE_STATE_V1_AWAITING_REVIEW: _ClassVar[EvaluationMatrixEvidenceStateV1]
    EVALUATION_MATRIX_EVIDENCE_STATE_V1_NOT_SAMPLED: _ClassVar[EvaluationMatrixEvidenceStateV1]
    EVALUATION_MATRIX_EVIDENCE_STATE_V1_SUPERSEDED: _ClassVar[EvaluationMatrixEvidenceStateV1]

class EvaluationMatrixFacetKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_MATRIX_FACET_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationMatrixFacetKindV1]
    EVALUATION_MATRIX_FACET_KIND_V1_REGRESSIONS: _ClassVar[EvaluationMatrixFacetKindV1]
    EVALUATION_MATRIX_FACET_KIND_V1_IMPROVEMENTS: _ClassVar[EvaluationMatrixFacetKindV1]
    EVALUATION_MATRIX_FACET_KIND_V1_DISAGREEMENTS: _ClassVar[EvaluationMatrixFacetKindV1]
    EVALUATION_MATRIX_FACET_KIND_V1_MISSING_EVIDENCE: _ClassVar[EvaluationMatrixFacetKindV1]
    EVALUATION_MATRIX_FACET_KIND_V1_CANDIDATE_FAILURES: _ClassVar[EvaluationMatrixFacetKindV1]
    EVALUATION_MATRIX_FACET_KIND_V1_SCORER_FAILURES: _ClassVar[EvaluationMatrixFacetKindV1]
    EVALUATION_MATRIX_FACET_KIND_V1_AWAITING_REVIEW: _ClassVar[EvaluationMatrixFacetKindV1]
    EVALUATION_MATRIX_FACET_KIND_V1_UNCHANGED: _ClassVar[EvaluationMatrixFacetKindV1]

class EvaluationCellEvidenceSourceV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_CELL_EVIDENCE_SOURCE_V1_UNSPECIFIED: _ClassVar[EvaluationCellEvidenceSourceV1]
    EVALUATION_CELL_EVIDENCE_SOURCE_V1_POSTGRES_PROJECTION: _ClassVar[EvaluationCellEvidenceSourceV1]
    EVALUATION_CELL_EVIDENCE_SOURCE_V1_FACT_PLANE_LOCATOR: _ClassVar[EvaluationCellEvidenceSourceV1]

class EvaluationScorerAttemptOriginV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_SCORER_ATTEMPT_ORIGIN_V1_UNSPECIFIED: _ClassVar[EvaluationScorerAttemptOriginV1]
    EVALUATION_SCORER_ATTEMPT_ORIGIN_V1_EXECUTION: _ClassVar[EvaluationScorerAttemptOriginV1]
    EVALUATION_SCORER_ATTEMPT_ORIGIN_V1_SCORER_RETRY: _ClassVar[EvaluationScorerAttemptOriginV1]
    EVALUATION_SCORER_ATTEMPT_ORIGIN_V1_HUMAN_REVIEW: _ClassVar[EvaluationScorerAttemptOriginV1]
    EVALUATION_SCORER_ATTEMPT_ORIGIN_V1_ADJUDICATION: _ClassVar[EvaluationScorerAttemptOriginV1]
    EVALUATION_SCORER_ATTEMPT_ORIGIN_V1_JUDGE_REGRADE: _ClassVar[EvaluationScorerAttemptOriginV1]

class EvaluationRunChangeKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_RUN_CHANGE_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationRunChangeKindV1]
    EVALUATION_RUN_CHANGE_KIND_V1_PROGRESS: _ClassVar[EvaluationRunChangeKindV1]
    EVALUATION_RUN_CHANGE_KIND_V1_CELL_BATCH: _ClassVar[EvaluationRunChangeKindV1]
    EVALUATION_RUN_CHANGE_KIND_V1_SECTION_REFRESHED: _ClassVar[EvaluationRunChangeKindV1]
    EVALUATION_RUN_CHANGE_KIND_V1_DECISION_REVISION: _ClassVar[EvaluationRunChangeKindV1]
    EVALUATION_RUN_CHANGE_KIND_V1_TERMINAL: _ClassVar[EvaluationRunChangeKindV1]
    EVALUATION_RUN_CHANGE_KIND_V1_RESYNC_REQUIRED: _ClassVar[EvaluationRunChangeKindV1]
    EVALUATION_RUN_CHANGE_KIND_V1_REPLAY_GAP: _ClassVar[EvaluationRunChangeKindV1]

class EvaluationArtifactContentStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_ARTIFACT_CONTENT_STATE_V1_UNSPECIFIED: _ClassVar[EvaluationArtifactContentStateV1]
    EVALUATION_ARTIFACT_CONTENT_STATE_V1_SERVED: _ClassVar[EvaluationArtifactContentStateV1]
    EVALUATION_ARTIFACT_CONTENT_STATE_V1_UNAUTHORIZED: _ClassVar[EvaluationArtifactContentStateV1]
    EVALUATION_ARTIFACT_CONTENT_STATE_V1_REVOKED: _ClassVar[EvaluationArtifactContentStateV1]
    EVALUATION_ARTIFACT_CONTENT_STATE_V1_REDACTED: _ClassVar[EvaluationArtifactContentStateV1]
    EVALUATION_ARTIFACT_CONTENT_STATE_V1_NOT_FOUND: _ClassVar[EvaluationArtifactContentStateV1]
    EVALUATION_ARTIFACT_CONTENT_STATE_V1_PLANE_NOT_SHIPPED: _ClassVar[EvaluationArtifactContentStateV1]
    EVALUATION_ARTIFACT_CONTENT_STATE_V1_BYTE_BUDGET_EXCEEDED: _ClassVar[EvaluationArtifactContentStateV1]

class EvaluationArtifactRemediationKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_ARTIFACT_REMEDIATION_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationArtifactRemediationKindV1]
    EVALUATION_ARTIFACT_REMEDIATION_KIND_V1_NONE: _ClassVar[EvaluationArtifactRemediationKindV1]
    EVALUATION_ARTIFACT_REMEDIATION_KIND_V1_REQUEST_ACCESS: _ClassVar[EvaluationArtifactRemediationKindV1]
    EVALUATION_ARTIFACT_REMEDIATION_KIND_V1_CONTACT_OWNER: _ClassVar[EvaluationArtifactRemediationKindV1]
    EVALUATION_ARTIFACT_REMEDIATION_KIND_V1_RETRY_NARROWER_BATCH: _ClassVar[EvaluationArtifactRemediationKindV1]
    EVALUATION_ARTIFACT_REMEDIATION_KIND_V1_WAIT_FOR_PLANE: _ClassVar[EvaluationArtifactRemediationKindV1]

class ConfigurationDimensionV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONFIGURATION_DIMENSION_V1_UNSPECIFIED: _ClassVar[ConfigurationDimensionV1]
    CONFIGURATION_DIMENSION_V1_CANDIDATE_RELEASE_REVISION: _ClassVar[ConfigurationDimensionV1]
    CONFIGURATION_DIMENSION_V1_PROVIDER_MODEL: _ClassVar[ConfigurationDimensionV1]
    CONFIGURATION_DIMENSION_V1_RESPONSE_MODEL: _ClassVar[ConfigurationDimensionV1]
    CONFIGURATION_DIMENSION_V1_PROMPT: _ClassVar[ConfigurationDimensionV1]
    CONFIGURATION_DIMENSION_V1_GENERATION_PARAMS: _ClassVar[ConfigurationDimensionV1]
    CONFIGURATION_DIMENSION_V1_TOOL_CATALOG: _ClassVar[ConfigurationDimensionV1]
    CONFIGURATION_DIMENSION_V1_TOOL_VERSION: _ClassVar[ConfigurationDimensionV1]
    CONFIGURATION_DIMENSION_V1_RETRIEVAL_BACKEND: _ClassVar[ConfigurationDimensionV1]
    CONFIGURATION_DIMENSION_V1_RETRIEVAL_CONFIG: _ClassVar[ConfigurationDimensionV1]
    CONFIGURATION_DIMENSION_V1_FEATURE_FLAG: _ClassVar[ConfigurationDimensionV1]
    CONFIGURATION_DIMENSION_V1_DEPLOYMENT: _ClassVar[ConfigurationDimensionV1]
    CONFIGURATION_DIMENSION_V1_ENVIRONMENT: _ClassVar[ConfigurationDimensionV1]
    CONFIGURATION_DIMENSION_V1_SCORER: _ClassVar[ConfigurationDimensionV1]
    CONFIGURATION_DIMENSION_V1_RUBRIC: _ClassVar[ConfigurationDimensionV1]
    CONFIGURATION_DIMENSION_V1_DECISION_POLICY: _ClassVar[ConfigurationDimensionV1]
    CONFIGURATION_DIMENSION_V1_DATASET: _ClassVar[ConfigurationDimensionV1]
    CONFIGURATION_DIMENSION_V1_COHORT: _ClassVar[ConfigurationDimensionV1]
    CONFIGURATION_DIMENSION_V1_SCHEMA: _ClassVar[ConfigurationDimensionV1]
    CONFIGURATION_DIMENSION_V1_NORMALIZATION: _ClassVar[ConfigurationDimensionV1]
    CONFIGURATION_DIMENSION_V1_TRIALS: _ClassVar[ConfigurationDimensionV1]

class EvaluationAuditEventKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_AUDIT_EVENT_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationAuditEventKindV1]
    EVALUATION_AUDIT_EVENT_KIND_V1_RUN_LAUNCHED: _ClassVar[EvaluationAuditEventKindV1]
    EVALUATION_AUDIT_EVENT_KIND_V1_RUN_STATE_CHANGED: _ClassVar[EvaluationAuditEventKindV1]
    EVALUATION_AUDIT_EVENT_KIND_V1_CELLS_RETRIED: _ClassVar[EvaluationAuditEventKindV1]
    EVALUATION_AUDIT_EVENT_KIND_V1_RUN_CANCELLED: _ClassVar[EvaluationAuditEventKindV1]
    EVALUATION_AUDIT_EVENT_KIND_V1_DECISION_ADOPTED: _ClassVar[EvaluationAuditEventKindV1]
    EVALUATION_AUDIT_EVENT_KIND_V1_REVIEW_SUBMITTED: _ClassVar[EvaluationAuditEventKindV1]
    EVALUATION_AUDIT_EVENT_KIND_V1_EXPORT_REQUESTED: _ClassVar[EvaluationAuditEventKindV1]
    EVALUATION_AUDIT_EVENT_KIND_V1_SHARE_CREATED: _ClassVar[EvaluationAuditEventKindV1]

class EvaluationReviewTaskStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_REVIEW_TASK_STATE_V1_UNSPECIFIED: _ClassVar[EvaluationReviewTaskStateV1]
    EVALUATION_REVIEW_TASK_STATE_V1_PENDING: _ClassVar[EvaluationReviewTaskStateV1]
    EVALUATION_REVIEW_TASK_STATE_V1_ASSIGNED: _ClassVar[EvaluationReviewTaskStateV1]
    EVALUATION_REVIEW_TASK_STATE_V1_RESERVED: _ClassVar[EvaluationReviewTaskStateV1]
    EVALUATION_REVIEW_TASK_STATE_V1_SUBMITTED: _ClassVar[EvaluationReviewTaskStateV1]
    EVALUATION_REVIEW_TASK_STATE_V1_RESERVATION_EXPIRED: _ClassVar[EvaluationReviewTaskStateV1]
    EVALUATION_REVIEW_TASK_STATE_V1_RELEASED: _ClassVar[EvaluationReviewTaskStateV1]
    EVALUATION_REVIEW_TASK_STATE_V1_CANCELLED: _ClassVar[EvaluationReviewTaskStateV1]
    EVALUATION_REVIEW_TASK_STATE_V1_WAIVED: _ClassVar[EvaluationReviewTaskStateV1]

class ReviewReservationStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REVIEW_RESERVATION_STATE_V1_UNSPECIFIED: _ClassVar[ReviewReservationStateV1]
    REVIEW_RESERVATION_STATE_V1_NONE: _ClassVar[ReviewReservationStateV1]
    REVIEW_RESERVATION_STATE_V1_ACTIVE: _ClassVar[ReviewReservationStateV1]
    REVIEW_RESERVATION_STATE_V1_EXPIRING: _ClassVar[ReviewReservationStateV1]
    REVIEW_RESERVATION_STATE_V1_EXPIRED: _ClassVar[ReviewReservationStateV1]
    REVIEW_RESERVATION_STATE_V1_RELEASED: _ClassVar[ReviewReservationStateV1]
    REVIEW_RESERVATION_STATE_V1_TRANSFERRED: _ClassVar[ReviewReservationStateV1]

class ReviewUnitCompletionStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REVIEW_UNIT_COMPLETION_STATE_V1_UNSPECIFIED: _ClassVar[ReviewUnitCompletionStateV1]
    REVIEW_UNIT_COMPLETION_STATE_V1_AWAITING_REVIEWERS: _ClassVar[ReviewUnitCompletionStateV1]
    REVIEW_UNIT_COMPLETION_STATE_V1_AWAITING_ADJUDICATION: _ClassVar[ReviewUnitCompletionStateV1]
    REVIEW_UNIT_COMPLETION_STATE_V1_COMPLETE: _ClassVar[ReviewUnitCompletionStateV1]
    REVIEW_UNIT_COMPLETION_STATE_V1_WAIVED: _ClassVar[ReviewUnitCompletionStateV1]
    REVIEW_UNIT_COMPLETION_STATE_V1_INCOMPLETE_EXPIRED: _ClassVar[ReviewUnitCompletionStateV1]

class ReviewAdjudicationStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REVIEW_ADJUDICATION_STATE_V1_UNSPECIFIED: _ClassVar[ReviewAdjudicationStateV1]
    REVIEW_ADJUDICATION_STATE_V1_NOT_REQUIRED: _ClassVar[ReviewAdjudicationStateV1]
    REVIEW_ADJUDICATION_STATE_V1_REQUIRED: _ClassVar[ReviewAdjudicationStateV1]
    REVIEW_ADJUDICATION_STATE_V1_ASSIGNED: _ClassVar[ReviewAdjudicationStateV1]
    REVIEW_ADJUDICATION_STATE_V1_RESOLVED: _ClassVar[ReviewAdjudicationStateV1]
    REVIEW_ADJUDICATION_STATE_V1_UNRESOLVABLE: _ClassVar[ReviewAdjudicationStateV1]

class EvaluationExportFormatV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_EXPORT_FORMAT_V1_UNSPECIFIED: _ClassVar[EvaluationExportFormatV1]
    EVALUATION_EXPORT_FORMAT_V1_CSV: _ClassVar[EvaluationExportFormatV1]
    EVALUATION_EXPORT_FORMAT_V1_JSONL: _ClassVar[EvaluationExportFormatV1]
    EVALUATION_EXPORT_FORMAT_V1_PARQUET: _ClassVar[EvaluationExportFormatV1]

class EvaluationShareStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_SHARE_STATE_V1_UNSPECIFIED: _ClassVar[EvaluationShareStateV1]
    EVALUATION_SHARE_STATE_V1_ACTIVE: _ClassVar[EvaluationShareStateV1]
    EVALUATION_SHARE_STATE_V1_REVOKED: _ClassVar[EvaluationShareStateV1]

class EvaluationWorkOperationKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_WORK_OPERATION_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationWorkOperationKindV1]
    EVALUATION_WORK_OPERATION_KIND_V1_CANDIDATE_CALL: _ClassVar[EvaluationWorkOperationKindV1]
    EVALUATION_WORK_OPERATION_KIND_V1_SCORER_EXECUTION: _ClassVar[EvaluationWorkOperationKindV1]
    EVALUATION_WORK_OPERATION_KIND_V1_RUN_PREPARATION: _ClassVar[EvaluationWorkOperationKindV1]

class EvaluationOperationDimensionV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_OPERATION_DIMENSION_V1_UNSPECIFIED: _ClassVar[EvaluationOperationDimensionV1]
    EVALUATION_OPERATION_DIMENSION_V1_HOST: _ClassVar[EvaluationOperationDimensionV1]
    EVALUATION_OPERATION_DIMENSION_V1_SERVICE: _ClassVar[EvaluationOperationDimensionV1]
    EVALUATION_OPERATION_DIMENSION_V1_CONTAINER: _ClassVar[EvaluationOperationDimensionV1]
    EVALUATION_OPERATION_DIMENSION_V1_NODE: _ClassVar[EvaluationOperationDimensionV1]
    EVALUATION_OPERATION_DIMENSION_V1_REGION: _ClassVar[EvaluationOperationDimensionV1]
    EVALUATION_OPERATION_DIMENSION_V1_TIME_BUCKET: _ClassVar[EvaluationOperationDimensionV1]
    EVALUATION_OPERATION_DIMENSION_V1_TELEMETRY_SPAN: _ClassVar[EvaluationOperationDimensionV1]

class EvaluationOperationCacheExplanationV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_OPERATION_CACHE_EXPLANATION_V1_UNSPECIFIED: _ClassVar[EvaluationOperationCacheExplanationV1]
    EVALUATION_OPERATION_CACHE_EXPLANATION_V1_NOT_REPORTED: _ClassVar[EvaluationOperationCacheExplanationV1]
    EVALUATION_OPERATION_CACHE_EXPLANATION_V1_NO_CACHE_ACTIVITY: _ClassVar[EvaluationOperationCacheExplanationV1]
    EVALUATION_OPERATION_CACHE_EXPLANATION_V1_CACHE_READS_OBSERVED: _ClassVar[EvaluationOperationCacheExplanationV1]
    EVALUATION_OPERATION_CACHE_EXPLANATION_V1_CACHE_WRITES_OBSERVED: _ClassVar[EvaluationOperationCacheExplanationV1]
    EVALUATION_OPERATION_CACHE_EXPLANATION_V1_NOT_APPLICABLE: _ClassVar[EvaluationOperationCacheExplanationV1]

class EvaluationAdjudicationRefusalV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_ADJUDICATION_REFUSAL_V1_UNSPECIFIED: _ClassVar[EvaluationAdjudicationRefusalV1]
    EVALUATION_ADJUDICATION_REFUSAL_V1_NOT_AN_ADJUDICATOR: _ClassVar[EvaluationAdjudicationRefusalV1]
    EVALUATION_ADJUDICATION_REFUSAL_V1_NO_CONFLICT_TO_ADJUDICATE: _ClassVar[EvaluationAdjudicationRefusalV1]
    EVALUATION_ADJUDICATION_REFUSAL_V1_UNIT_ALREADY_COMPLETE: _ClassVar[EvaluationAdjudicationRefusalV1]
    EVALUATION_ADJUDICATION_REFUSAL_V1_UNIT_NOT_FOUND: _ClassVar[EvaluationAdjudicationRefusalV1]

class EvaluationOrgNegotiatedRateStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_ORG_NEGOTIATED_RATE_STATE_V1_UNSPECIFIED: _ClassVar[EvaluationOrgNegotiatedRateStateV1]
    EVALUATION_ORG_NEGOTIATED_RATE_STATE_V1_SCHEDULED: _ClassVar[EvaluationOrgNegotiatedRateStateV1]
    EVALUATION_ORG_NEGOTIATED_RATE_STATE_V1_IN_FORCE: _ClassVar[EvaluationOrgNegotiatedRateStateV1]
    EVALUATION_ORG_NEGOTIATED_RATE_STATE_V1_ENDED: _ClassVar[EvaluationOrgNegotiatedRateStateV1]
    EVALUATION_ORG_NEGOTIATED_RATE_STATE_V1_VOIDED: _ClassVar[EvaluationOrgNegotiatedRateStateV1]

class EvaluationSeriesGrainV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_SERIES_GRAIN_V1_UNSPECIFIED: _ClassVar[EvaluationSeriesGrainV1]
    EVALUATION_SERIES_GRAIN_V1_DEFINITION: _ClassVar[EvaluationSeriesGrainV1]
    EVALUATION_SERIES_GRAIN_V1_CANDIDATE: _ClassVar[EvaluationSeriesGrainV1]
    EVALUATION_SERIES_GRAIN_V1_SCORER: _ClassVar[EvaluationSeriesGrainV1]
    EVALUATION_SERIES_GRAIN_V1_CANDIDATE_SCORER: _ClassVar[EvaluationSeriesGrainV1]
    EVALUATION_SERIES_GRAIN_V1_COHORT: _ClassVar[EvaluationSeriesGrainV1]
    EVALUATION_SERIES_GRAIN_V1_PRODUCTION_RULE: _ClassVar[EvaluationSeriesGrainV1]

class EvaluationSeriesPlaneV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_SERIES_PLANE_V1_UNSPECIFIED: _ClassVar[EvaluationSeriesPlaneV1]
    EVALUATION_SERIES_PLANE_V1_PROJECTION: _ClassVar[EvaluationSeriesPlaneV1]
    EVALUATION_SERIES_PLANE_V1_FACTS: _ClassVar[EvaluationSeriesPlaneV1]

class EvaluationCaptureSourceKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_CAPTURE_SOURCE_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationCaptureSourceKindV1]
    EVALUATION_CAPTURE_SOURCE_KIND_V1_TRACE_SPAN: _ClassVar[EvaluationCaptureSourceKindV1]
    EVALUATION_CAPTURE_SOURCE_KIND_V1_EVALUATION_MATRIX_CELL: _ClassVar[EvaluationCaptureSourceKindV1]
    EVALUATION_CAPTURE_SOURCE_KIND_V1_PRODUCTION_RULE: _ClassVar[EvaluationCaptureSourceKindV1]
    EVALUATION_CAPTURE_SOURCE_KIND_V1_MANUAL: _ClassVar[EvaluationCaptureSourceKindV1]
    EVALUATION_CAPTURE_SOURCE_KIND_V1_IMPORT: _ClassVar[EvaluationCaptureSourceKindV1]
    EVALUATION_CAPTURE_SOURCE_KIND_V1_MACHINE_PRINCIPAL: _ClassVar[EvaluationCaptureSourceKindV1]

class EvaluationCaptureRefusalKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_CAPTURE_REFUSAL_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationCaptureRefusalKindV1]
    EVALUATION_CAPTURE_REFUSAL_KIND_V1_SOURCE_NOT_FOUND: _ClassVar[EvaluationCaptureRefusalKindV1]
    EVALUATION_CAPTURE_REFUSAL_KIND_V1_SOURCE_PLANE_NOT_SHIPPED: _ClassVar[EvaluationCaptureRefusalKindV1]
    EVALUATION_CAPTURE_REFUSAL_KIND_V1_REQUIRED_FIELD_UNMAPPED: _ClassVar[EvaluationCaptureRefusalKindV1]
    EVALUATION_CAPTURE_REFUSAL_KIND_V1_MAPPING_RESOLVED_NOTHING: _ClassVar[EvaluationCaptureRefusalKindV1]
    EVALUATION_CAPTURE_REFUSAL_KIND_V1_INVALID_TARGET_PATH: _ClassVar[EvaluationCaptureRefusalKindV1]
    EVALUATION_CAPTURE_REFUSAL_KIND_V1_IDEMPOTENCY_KEY_REUSED: _ClassVar[EvaluationCaptureRefusalKindV1]
    EVALUATION_CAPTURE_REFUSAL_KIND_V1_DRAFT_CASE_CAP_EXCEEDED: _ClassVar[EvaluationCaptureRefusalKindV1]
    EVALUATION_CAPTURE_REFUSAL_KIND_V1_PREVIEW_DIGEST_MOVED: _ClassVar[EvaluationCaptureRefusalKindV1]
    EVALUATION_CAPTURE_REFUSAL_KIND_V1_SPAN_CONTENT_BUDGET_EXCEEDED: _ClassVar[EvaluationCaptureRefusalKindV1]
    EVALUATION_CAPTURE_REFUSAL_KIND_V1_PROMOTION_KEY_EXISTS: _ClassVar[EvaluationCaptureRefusalKindV1]
    EVALUATION_CAPTURE_REFUSAL_KIND_V1_REDACTION_BLOCKED: _ClassVar[EvaluationCaptureRefusalKindV1]
    EVALUATION_CAPTURE_REFUSAL_KIND_V1_REDACTION_INDETERMINATE: _ClassVar[EvaluationCaptureRefusalKindV1]

class EvaluationDatasetDraftStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_DATASET_DRAFT_STATE_V1_UNSPECIFIED: _ClassVar[EvaluationDatasetDraftStateV1]
    EVALUATION_DATASET_DRAFT_STATE_V1_OPEN: _ClassVar[EvaluationDatasetDraftStateV1]
    EVALUATION_DATASET_DRAFT_STATE_V1_FINALIZED: _ClassVar[EvaluationDatasetDraftStateV1]
    EVALUATION_DATASET_DRAFT_STATE_V1_ABANDONED: _ClassVar[EvaluationDatasetDraftStateV1]

class EvaluationProposedCaseStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_PROPOSED_CASE_STATE_V1_UNSPECIFIED: _ClassVar[EvaluationProposedCaseStateV1]
    EVALUATION_PROPOSED_CASE_STATE_V1_PROPOSED: _ClassVar[EvaluationProposedCaseStateV1]
    EVALUATION_PROPOSED_CASE_STATE_V1_VOIDED: _ClassVar[EvaluationProposedCaseStateV1]

class EvaluationSpanContentClassV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_SPAN_CONTENT_CLASS_V1_UNSPECIFIED: _ClassVar[EvaluationSpanContentClassV1]
    EVALUATION_SPAN_CONTENT_CLASS_V1_INPUT_MESSAGES: _ClassVar[EvaluationSpanContentClassV1]
    EVALUATION_SPAN_CONTENT_CLASS_V1_OUTPUT_MESSAGES: _ClassVar[EvaluationSpanContentClassV1]
    EVALUATION_SPAN_CONTENT_CLASS_V1_TOOL_DEFINITIONS: _ClassVar[EvaluationSpanContentClassV1]
    EVALUATION_SPAN_CONTENT_CLASS_V1_SYSTEM_INSTRUCTIONS: _ClassVar[EvaluationSpanContentClassV1]
    EVALUATION_SPAN_CONTENT_CLASS_V1_RETRIEVAL_DOCUMENTS: _ClassVar[EvaluationSpanContentClassV1]
    EVALUATION_SPAN_CONTENT_CLASS_V1_TOOL_ARGUMENTS: _ClassVar[EvaluationSpanContentClassV1]
    EVALUATION_SPAN_CONTENT_CLASS_V1_TOOL_RESULT: _ClassVar[EvaluationSpanContentClassV1]
    EVALUATION_SPAN_CONTENT_CLASS_V1_REASONING: _ClassVar[EvaluationSpanContentClassV1]

class EvaluationProviderCredentialRejectionKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_PROVIDER_CREDENTIAL_REJECTION_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationProviderCredentialRejectionKindV1]
    EVALUATION_PROVIDER_CREDENTIAL_REJECTION_KIND_V1_CAP_EXCEEDED: _ClassVar[EvaluationProviderCredentialRejectionKindV1]
    EVALUATION_PROVIDER_CREDENTIAL_REJECTION_KIND_V1_DUPLICATE_KEY_NAME: _ClassVar[EvaluationProviderCredentialRejectionKindV1]
    EVALUATION_PROVIDER_CREDENTIAL_REJECTION_KIND_V1_INVALID_PROVIDER: _ClassVar[EvaluationProviderCredentialRejectionKindV1]

class EvaluationScorerKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_SCORER_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationScorerKindV1]
    EVALUATION_SCORER_KIND_V1_DETERMINISTIC: _ClassVar[EvaluationScorerKindV1]
    EVALUATION_SCORER_KIND_V1_HUMAN: _ClassVar[EvaluationScorerKindV1]
    EVALUATION_SCORER_KIND_V1_LLM_JUDGE: _ClassVar[EvaluationScorerKindV1]

class EvaluationScorerEvaluatorV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_SCORER_EVALUATOR_V1_UNSPECIFIED: _ClassVar[EvaluationScorerEvaluatorV1]
    EVALUATION_SCORER_EVALUATOR_V1_EXACT: _ClassVar[EvaluationScorerEvaluatorV1]
    EVALUATION_SCORER_EVALUATOR_V1_NUMERIC_THRESHOLD: _ClassVar[EvaluationScorerEvaluatorV1]
    EVALUATION_SCORER_EVALUATOR_V1_PATTERN: _ClassVar[EvaluationScorerEvaluatorV1]

class EvaluationScorerConfigRejectionKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_SCORER_CONFIG_REJECTION_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationScorerConfigRejectionKindV1]
    EVALUATION_SCORER_CONFIG_REJECTION_KIND_V1_DUPLICATE_CONFIG_KEY: _ClassVar[EvaluationScorerConfigRejectionKindV1]
    EVALUATION_SCORER_CONFIG_REJECTION_KIND_V1_PINNED_BY_RUN: _ClassVar[EvaluationScorerConfigRejectionKindV1]
    EVALUATION_SCORER_CONFIG_REJECTION_KIND_V1_KIND_SPEC_MISMATCH: _ClassVar[EvaluationScorerConfigRejectionKindV1]
    EVALUATION_SCORER_CONFIG_REJECTION_KIND_V1_EVALUATOR_NOT_RETAINED: _ClassVar[EvaluationScorerConfigRejectionKindV1]
    EVALUATION_SCORER_CONFIG_REJECTION_KIND_V1_REVIEW_POLICY_UNSATISFIABLE: _ClassVar[EvaluationScorerConfigRejectionKindV1]
    EVALUATION_SCORER_CONFIG_REJECTION_KIND_V1_JUDGE_SPEC_INVALID: _ClassVar[EvaluationScorerConfigRejectionKindV1]
    EVALUATION_SCORER_CONFIG_REJECTION_KIND_V1_JUDGE_PROVIDER_NOT_AVAILABLE: _ClassVar[EvaluationScorerConfigRejectionKindV1]
    EVALUATION_SCORER_CONFIG_REJECTION_KIND_V1_JUDGE_TEMPLATE_MOVED: _ClassVar[EvaluationScorerConfigRejectionKindV1]

class EvaluationDatasetVersionRejectionKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_DATASET_VERSION_REJECTION_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationDatasetVersionRejectionKindV1]
    EVALUATION_DATASET_VERSION_REJECTION_KIND_V1_COLLECTION_CAP_EXCEEDED: _ClassVar[EvaluationDatasetVersionRejectionKindV1]
    EVALUATION_DATASET_VERSION_REJECTION_KIND_V1_VERSION_CAP_ALL_PINNED: _ClassVar[EvaluationDatasetVersionRejectionKindV1]
    EVALUATION_DATASET_VERSION_REJECTION_KIND_V1_MALFORMED_JSONL_LINE: _ClassVar[EvaluationDatasetVersionRejectionKindV1]
    EVALUATION_DATASET_VERSION_REJECTION_KIND_V1_EMPTY_INGEST: _ClassVar[EvaluationDatasetVersionRejectionKindV1]
    EVALUATION_DATASET_VERSION_REJECTION_KIND_V1_INGEST_TOO_LARGE: _ClassVar[EvaluationDatasetVersionRejectionKindV1]
    EVALUATION_DATASET_VERSION_REJECTION_KIND_V1_DRAFT_NOT_FINALIZABLE: _ClassVar[EvaluationDatasetVersionRejectionKindV1]
    EVALUATION_DATASET_VERSION_REJECTION_KIND_V1_INGEST_BYTES_EXCEEDED: _ClassVar[EvaluationDatasetVersionRejectionKindV1]
    EVALUATION_DATASET_VERSION_REJECTION_KIND_V1_INGEST_CASE_COUNT_EXCEEDED: _ClassVar[EvaluationDatasetVersionRejectionKindV1]
    EVALUATION_DATASET_VERSION_REJECTION_KIND_V1_DRAFT_HAS_UNAPPROVED_CASES: _ClassVar[EvaluationDatasetVersionRejectionKindV1]

class EvaluationScorerSuiteRejectionKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_SCORER_SUITE_REJECTION_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationScorerSuiteRejectionKindV1]
    EVALUATION_SCORER_SUITE_REJECTION_KIND_V1_DUPLICATE_SUITE_KEY: _ClassVar[EvaluationScorerSuiteRejectionKindV1]
    EVALUATION_SCORER_SUITE_REJECTION_KIND_V1_MEMBER_NOT_FOUND: _ClassVar[EvaluationScorerSuiteRejectionKindV1]
    EVALUATION_SCORER_SUITE_REJECTION_KIND_V1_EMPTY_MEMBERSHIP: _ClassVar[EvaluationScorerSuiteRejectionKindV1]
    EVALUATION_SCORER_SUITE_REJECTION_KIND_V1_DUPLICATE_MEMBER: _ClassVar[EvaluationScorerSuiteRejectionKindV1]
    EVALUATION_SCORER_SUITE_REJECTION_KIND_V1_MEMBER_CAP_EXCEEDED: _ClassVar[EvaluationScorerSuiteRejectionKindV1]
    EVALUATION_SCORER_SUITE_REJECTION_KIND_V1_COMBINE_RULE_NOT_SUPPORTED: _ClassVar[EvaluationScorerSuiteRejectionKindV1]
    EVALUATION_SCORER_SUITE_REJECTION_KIND_V1_MEMBER_NOT_SCOREABLE: _ClassVar[EvaluationScorerSuiteRejectionKindV1]
    EVALUATION_SCORER_SUITE_REJECTION_KIND_V1_MEMBER_WEIGHT_UNUSABLE: _ClassVar[EvaluationScorerSuiteRejectionKindV1]

class EvaluationJudgeRegradeJobStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_JUDGE_REGRADE_JOB_STATE_V1_UNSPECIFIED: _ClassVar[EvaluationJudgeRegradeJobStateV1]
    EVALUATION_JUDGE_REGRADE_JOB_STATE_V1_QUEUED: _ClassVar[EvaluationJudgeRegradeJobStateV1]
    EVALUATION_JUDGE_REGRADE_JOB_STATE_V1_RUNNING: _ClassVar[EvaluationJudgeRegradeJobStateV1]
    EVALUATION_JUDGE_REGRADE_JOB_STATE_V1_COMPLETED: _ClassVar[EvaluationJudgeRegradeJobStateV1]
    EVALUATION_JUDGE_REGRADE_JOB_STATE_V1_FAILED: _ClassVar[EvaluationJudgeRegradeJobStateV1]
    EVALUATION_JUDGE_REGRADE_JOB_STATE_V1_CANCELLED: _ClassVar[EvaluationJudgeRegradeJobStateV1]

class EvaluationJudgeRegradeCellStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_JUDGE_REGRADE_CELL_STATE_V1_UNSPECIFIED: _ClassVar[EvaluationJudgeRegradeCellStateV1]
    EVALUATION_JUDGE_REGRADE_CELL_STATE_V1_QUEUED: _ClassVar[EvaluationJudgeRegradeCellStateV1]
    EVALUATION_JUDGE_REGRADE_CELL_STATE_V1_LEASED: _ClassVar[EvaluationJudgeRegradeCellStateV1]
    EVALUATION_JUDGE_REGRADE_CELL_STATE_V1_SUCCEEDED: _ClassVar[EvaluationJudgeRegradeCellStateV1]
    EVALUATION_JUDGE_REGRADE_CELL_STATE_V1_FAILED: _ClassVar[EvaluationJudgeRegradeCellStateV1]
    EVALUATION_JUDGE_REGRADE_CELL_STATE_V1_CANCELLED: _ClassVar[EvaluationJudgeRegradeCellStateV1]

class EvaluationJudgeRegradeIneligibilityV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_JUDGE_REGRADE_INELIGIBILITY_V1_UNSPECIFIED: _ClassVar[EvaluationJudgeRegradeIneligibilityV1]
    EVALUATION_JUDGE_REGRADE_INELIGIBILITY_V1_CANDIDATE_OUTPUT_ABSENT: _ClassVar[EvaluationJudgeRegradeIneligibilityV1]
    EVALUATION_JUDGE_REGRADE_INELIGIBILITY_V1_SCORER_NOT_A_JUDGE: _ClassVar[EvaluationJudgeRegradeIneligibilityV1]
    EVALUATION_JUDGE_REGRADE_INELIGIBILITY_V1_SCORER_REQUIRES_HUMAN: _ClassVar[EvaluationJudgeRegradeIneligibilityV1]
    EVALUATION_JUDGE_REGRADE_INELIGIBILITY_V1_ATTEMPT_CEILING_REACHED: _ClassVar[EvaluationJudgeRegradeIneligibilityV1]
    EVALUATION_JUDGE_REGRADE_INELIGIBILITY_V1_COORDINATE_UNKNOWN: _ClassVar[EvaluationJudgeRegradeIneligibilityV1]
    EVALUATION_JUDGE_REGRADE_INELIGIBILITY_V1_PROVIDER_UNCONFIGURED: _ClassVar[EvaluationJudgeRegradeIneligibilityV1]
    EVALUATION_JUDGE_REGRADE_INELIGIBILITY_V1_COORDINATE_ALREADY_QUEUED: _ClassVar[EvaluationJudgeRegradeIneligibilityV1]
    EVALUATION_JUDGE_REGRADE_INELIGIBILITY_V1_SCORER_IS_A_DERIVED_SUITE: _ClassVar[EvaluationJudgeRegradeIneligibilityV1]

class EvaluationJudgeRegradeRateComparisonV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_JUDGE_REGRADE_RATE_COMPARISON_V1_UNSPECIFIED: _ClassVar[EvaluationJudgeRegradeRateComparisonV1]
    EVALUATION_JUDGE_REGRADE_RATE_COMPARISON_V1_UNCHANGED: _ClassVar[EvaluationJudgeRegradeRateComparisonV1]
    EVALUATION_JUDGE_REGRADE_RATE_COMPARISON_V1_MOVED: _ClassVar[EvaluationJudgeRegradeRateComparisonV1]
    EVALUATION_JUDGE_REGRADE_RATE_COMPARISON_V1_PIN_CARRIES_NO_RATE: _ClassVar[EvaluationJudgeRegradeRateComparisonV1]
    EVALUATION_JUDGE_REGRADE_RATE_COMPARISON_V1_REGISTRY_HAS_NO_ROW: _ClassVar[EvaluationJudgeRegradeRateComparisonV1]

class EvaluationReviewRequeueReasonV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_REVIEW_REQUEUE_REASON_V1_UNSPECIFIED: _ClassVar[EvaluationReviewRequeueReasonV1]
    EVALUATION_REVIEW_REQUEUE_REASON_V1_REVIEWER_UNAVAILABLE: _ClassVar[EvaluationReviewRequeueReasonV1]
    EVALUATION_REVIEW_REQUEUE_REASON_V1_AMBIGUOUS_GUIDANCE: _ClassVar[EvaluationReviewRequeueReasonV1]
    EVALUATION_REVIEW_REQUEUE_REASON_V1_WRONG_REVIEWER_POOL: _ClassVar[EvaluationReviewRequeueReasonV1]
    EVALUATION_REVIEW_REQUEUE_REASON_V1_CONTENT_UNREADABLE: _ClassVar[EvaluationReviewRequeueReasonV1]
    EVALUATION_REVIEW_REQUEUE_REASON_V1_OPERATOR_REBALANCE: _ClassVar[EvaluationReviewRequeueReasonV1]

class EvaluationReviewTaskRefusalKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_REVIEW_TASK_REFUSAL_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationReviewTaskRefusalKindV1]
    EVALUATION_REVIEW_TASK_REFUSAL_KIND_V1_NOT_HELD_BY_CALLER: _ClassVar[EvaluationReviewTaskRefusalKindV1]
    EVALUATION_REVIEW_TASK_REFUSAL_KIND_V1_TASK_NOT_FOUND: _ClassVar[EvaluationReviewTaskRefusalKindV1]
    EVALUATION_REVIEW_TASK_REFUSAL_KIND_V1_ALREADY_SUBMITTED: _ClassVar[EvaluationReviewTaskRefusalKindV1]
    EVALUATION_REVIEW_TASK_REFUSAL_KIND_V1_STILL_RESERVED: _ClassVar[EvaluationReviewTaskRefusalKindV1]
    EVALUATION_REVIEW_TASK_REFUSAL_KIND_V1_BATCH_TOO_LARGE: _ClassVar[EvaluationReviewTaskRefusalKindV1]
    EVALUATION_REVIEW_TASK_REFUSAL_KIND_V1_UNIT_NO_LONGER_OPEN: _ClassVar[EvaluationReviewTaskRefusalKindV1]

class ProductionRuleVersionStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCTION_RULE_VERSION_STATE_V1_UNSPECIFIED: _ClassVar[ProductionRuleVersionStateV1]
    PRODUCTION_RULE_VERSION_STATE_V1_DRAFT: _ClassVar[ProductionRuleVersionStateV1]
    PRODUCTION_RULE_VERSION_STATE_V1_ACTIVE: _ClassVar[ProductionRuleVersionStateV1]
    PRODUCTION_RULE_VERSION_STATE_V1_PAUSED: _ClassVar[ProductionRuleVersionStateV1]
    PRODUCTION_RULE_VERSION_STATE_V1_SUPERSEDED: _ClassVar[ProductionRuleVersionStateV1]
    PRODUCTION_RULE_VERSION_STATE_V1_DISABLED: _ClassVar[ProductionRuleVersionStateV1]
    PRODUCTION_RULE_VERSION_STATE_V1_ARCHIVED: _ClassVar[ProductionRuleVersionStateV1]

class ProductionRuleActionKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCTION_RULE_ACTION_KIND_V1_UNSPECIFIED: _ClassVar[ProductionRuleActionKindV1]
    PRODUCTION_RULE_ACTION_KIND_V1_SCORE: _ClassVar[ProductionRuleActionKindV1]
    PRODUCTION_RULE_ACTION_KIND_V1_CREATE_DATASET_DRAFT: _ClassVar[ProductionRuleActionKindV1]
    PRODUCTION_RULE_ACTION_KIND_V1_REQUEST_REVIEW: _ClassVar[ProductionRuleActionKindV1]
    PRODUCTION_RULE_ACTION_KIND_V1_RUN_LINKED_EVALUATION: _ClassVar[ProductionRuleActionKindV1]
    PRODUCTION_RULE_ACTION_KIND_V1_NOTIFY: _ClassVar[ProductionRuleActionKindV1]
    PRODUCTION_RULE_ACTION_KIND_V1_BLOCK_RELEASE: _ClassVar[ProductionRuleActionKindV1]

class ProductionRuleHealthStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCTION_RULE_HEALTH_STATE_V1_UNSPECIFIED: _ClassVar[ProductionRuleHealthStateV1]
    PRODUCTION_RULE_HEALTH_STATE_V1_ENABLED: _ClassVar[ProductionRuleHealthStateV1]
    PRODUCTION_RULE_HEALTH_STATE_V1_PAUSED: _ClassVar[ProductionRuleHealthStateV1]
    PRODUCTION_RULE_HEALTH_STATE_V1_DEGRADED: _ClassVar[ProductionRuleHealthStateV1]
    PRODUCTION_RULE_HEALTH_STATE_V1_FAILING: _ClassVar[ProductionRuleHealthStateV1]
    PRODUCTION_RULE_HEALTH_STATE_V1_INDETERMINATE: _ClassVar[ProductionRuleHealthStateV1]

class ProductionRuleRuntimeScopeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCTION_RULE_RUNTIME_SCOPE_V1_UNSPECIFIED: _ClassVar[ProductionRuleRuntimeScopeV1]
    PRODUCTION_RULE_RUNTIME_SCOPE_V1_AGENT_RUN: _ClassVar[ProductionRuleRuntimeScopeV1]
    PRODUCTION_RULE_RUNTIME_SCOPE_V1_SPAN: _ClassVar[ProductionRuleRuntimeScopeV1]

class ProductionRuleActionConditionKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCTION_RULE_ACTION_CONDITION_KIND_V1_UNSPECIFIED: _ClassVar[ProductionRuleActionConditionKindV1]
    PRODUCTION_RULE_ACTION_CONDITION_KIND_V1_ALWAYS: _ClassVar[ProductionRuleActionConditionKindV1]
    PRODUCTION_RULE_ACTION_CONDITION_KIND_V1_SCORE_BELOW: _ClassVar[ProductionRuleActionConditionKindV1]
    PRODUCTION_RULE_ACTION_CONDITION_KIND_V1_SCORE_AT_OR_ABOVE: _ClassVar[ProductionRuleActionConditionKindV1]
    PRODUCTION_RULE_ACTION_CONDITION_KIND_V1_SCORER_FAILED: _ClassVar[ProductionRuleActionConditionKindV1]
    PRODUCTION_RULE_ACTION_CONDITION_KIND_V1_VERDICT_IS: _ClassVar[ProductionRuleActionConditionKindV1]

class ProductionRuleDependencyKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCTION_RULE_DEPENDENCY_KIND_V1_UNSPECIFIED: _ClassVar[ProductionRuleDependencyKindV1]
    PRODUCTION_RULE_DEPENDENCY_KIND_V1_DATASET_COLLECTION: _ClassVar[ProductionRuleDependencyKindV1]
    PRODUCTION_RULE_DEPENDENCY_KIND_V1_DATASET_VERSION: _ClassVar[ProductionRuleDependencyKindV1]
    PRODUCTION_RULE_DEPENDENCY_KIND_V1_EVALUATION_DEFINITION: _ClassVar[ProductionRuleDependencyKindV1]
    PRODUCTION_RULE_DEPENDENCY_KIND_V1_SCORE_CONFIG: _ClassVar[ProductionRuleDependencyKindV1]
    PRODUCTION_RULE_DEPENDENCY_KIND_V1_SCORER_SUITE: _ClassVar[ProductionRuleDependencyKindV1]

class ProductionRuleDependencyHealthV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCTION_RULE_DEPENDENCY_HEALTH_V1_UNSPECIFIED: _ClassVar[ProductionRuleDependencyHealthV1]
    PRODUCTION_RULE_DEPENDENCY_HEALTH_V1_SATISFIED: _ClassVar[ProductionRuleDependencyHealthV1]
    PRODUCTION_RULE_DEPENDENCY_HEALTH_V1_UNSATISFIED: _ClassVar[ProductionRuleDependencyHealthV1]
    PRODUCTION_RULE_DEPENDENCY_HEALTH_V1_UNKNOWN: _ClassVar[ProductionRuleDependencyHealthV1]

class ProductionRuleVersionTransitionV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCTION_RULE_VERSION_TRANSITION_V1_UNSPECIFIED: _ClassVar[ProductionRuleVersionTransitionV1]
    PRODUCTION_RULE_VERSION_TRANSITION_V1_ACTIVATE: _ClassVar[ProductionRuleVersionTransitionV1]
    PRODUCTION_RULE_VERSION_TRANSITION_V1_PAUSE: _ClassVar[ProductionRuleVersionTransitionV1]
    PRODUCTION_RULE_VERSION_TRANSITION_V1_RESUME: _ClassVar[ProductionRuleVersionTransitionV1]
    PRODUCTION_RULE_VERSION_TRANSITION_V1_ARCHIVE: _ClassVar[ProductionRuleVersionTransitionV1]

class ProductionWorkflowExecutionStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCTION_WORKFLOW_EXECUTION_STATE_V1_UNSPECIFIED: _ClassVar[ProductionWorkflowExecutionStateV1]
    PRODUCTION_WORKFLOW_EXECUTION_STATE_V1_PENDING: _ClassVar[ProductionWorkflowExecutionStateV1]
    PRODUCTION_WORKFLOW_EXECUTION_STATE_V1_RUNNING: _ClassVar[ProductionWorkflowExecutionStateV1]
    PRODUCTION_WORKFLOW_EXECUTION_STATE_V1_SUCCEEDED: _ClassVar[ProductionWorkflowExecutionStateV1]
    PRODUCTION_WORKFLOW_EXECUTION_STATE_V1_PARTIALLY_SUCCEEDED: _ClassVar[ProductionWorkflowExecutionStateV1]
    PRODUCTION_WORKFLOW_EXECUTION_STATE_V1_FAILED: _ClassVar[ProductionWorkflowExecutionStateV1]
    PRODUCTION_WORKFLOW_EXECUTION_STATE_V1_DEAD_LETTERED: _ClassVar[ProductionWorkflowExecutionStateV1]
    PRODUCTION_WORKFLOW_EXECUTION_STATE_V1_CANCELLED: _ClassVar[ProductionWorkflowExecutionStateV1]

class ProductionWorkflowStepStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCTION_WORKFLOW_STEP_STATE_V1_UNSPECIFIED: _ClassVar[ProductionWorkflowStepStateV1]
    PRODUCTION_WORKFLOW_STEP_STATE_V1_PENDING: _ClassVar[ProductionWorkflowStepStateV1]
    PRODUCTION_WORKFLOW_STEP_STATE_V1_RUNNING: _ClassVar[ProductionWorkflowStepStateV1]
    PRODUCTION_WORKFLOW_STEP_STATE_V1_SUCCEEDED: _ClassVar[ProductionWorkflowStepStateV1]
    PRODUCTION_WORKFLOW_STEP_STATE_V1_RETRYABLE: _ClassVar[ProductionWorkflowStepStateV1]
    PRODUCTION_WORKFLOW_STEP_STATE_V1_FAILED: _ClassVar[ProductionWorkflowStepStateV1]
    PRODUCTION_WORKFLOW_STEP_STATE_V1_DEAD_LETTER: _ClassVar[ProductionWorkflowStepStateV1]
    PRODUCTION_WORKFLOW_STEP_STATE_V1_SKIPPED: _ClassVar[ProductionWorkflowStepStateV1]

class ProductionWorkflowStepSkipReasonV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCTION_WORKFLOW_STEP_SKIP_REASON_V1_UNSPECIFIED: _ClassVar[ProductionWorkflowStepSkipReasonV1]
    PRODUCTION_WORKFLOW_STEP_SKIP_REASON_V1_CONDITION_NOT_MET: _ClassVar[ProductionWorkflowStepSkipReasonV1]
    PRODUCTION_WORKFLOW_STEP_SKIP_REASON_V1_PREREQUISITE_NOT_SATISFIED: _ClassVar[ProductionWorkflowStepSkipReasonV1]
    PRODUCTION_WORKFLOW_STEP_SKIP_REASON_V1_BUDGET_EXHAUSTED: _ClassVar[ProductionWorkflowStepSkipReasonV1]
    PRODUCTION_WORKFLOW_STEP_SKIP_REASON_V1_EXECUTION_CANCELLED: _ClassVar[ProductionWorkflowStepSkipReasonV1]

class ProductionWorkflowAdmissionV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCTION_WORKFLOW_ADMISSION_V1_UNSPECIFIED: _ClassVar[ProductionWorkflowAdmissionV1]
    PRODUCTION_WORKFLOW_ADMISSION_V1_STARTED: _ClassVar[ProductionWorkflowAdmissionV1]
    PRODUCTION_WORKFLOW_ADMISSION_V1_IDEMPOTENT_REPLAY: _ClassVar[ProductionWorkflowAdmissionV1]
    PRODUCTION_WORKFLOW_ADMISSION_V1_SKIPPED_SAMPLED_OUT: _ClassVar[ProductionWorkflowAdmissionV1]
    PRODUCTION_WORKFLOW_ADMISSION_V1_SKIPPED_RULE_NOT_DISPATCHING: _ClassVar[ProductionWorkflowAdmissionV1]
    PRODUCTION_WORKFLOW_ADMISSION_V1_SKIPPED_BUDGET_EXHAUSTED: _ClassVar[ProductionWorkflowAdmissionV1]

class ReleaseBlockStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELEASE_BLOCK_STATE_V1_UNSPECIFIED: _ClassVar[ReleaseBlockStateV1]
    RELEASE_BLOCK_STATE_V1_ACTIVE: _ClassVar[ReleaseBlockStateV1]
    RELEASE_BLOCK_STATE_V1_INDETERMINATE: _ClassVar[ReleaseBlockStateV1]
    RELEASE_BLOCK_STATE_V1_CLEARED: _ClassVar[ReleaseBlockStateV1]
    RELEASE_BLOCK_STATE_V1_EXPIRED: _ClassVar[ReleaseBlockStateV1]
    RELEASE_BLOCK_STATE_V1_OVERRIDDEN: _ClassVar[ReleaseBlockStateV1]

class ProductionReleaseBlockEvidenceKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCTION_RELEASE_BLOCK_EVIDENCE_KIND_V1_UNSPECIFIED: _ClassVar[ProductionReleaseBlockEvidenceKindV1]
    PRODUCTION_RELEASE_BLOCK_EVIDENCE_KIND_V1_PRODUCTION_SCORE: _ClassVar[ProductionReleaseBlockEvidenceKindV1]
    PRODUCTION_RELEASE_BLOCK_EVIDENCE_KIND_V1_DATASET_VERSION: _ClassVar[ProductionReleaseBlockEvidenceKindV1]
    PRODUCTION_RELEASE_BLOCK_EVIDENCE_KIND_V1_EVALUATION_RUN: _ClassVar[ProductionReleaseBlockEvidenceKindV1]
    PRODUCTION_RELEASE_BLOCK_EVIDENCE_KIND_V1_WORKFLOW_EXECUTION: _ClassVar[ProductionReleaseBlockEvidenceKindV1]

class ProductionReleaseBlockClearConditionV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCTION_RELEASE_BLOCK_CLEAR_CONDITION_V1_UNSPECIFIED: _ClassVar[ProductionReleaseBlockClearConditionV1]
    PRODUCTION_RELEASE_BLOCK_CLEAR_CONDITION_V1_RULE_PASSES_AGAIN: _ClassVar[ProductionReleaseBlockClearConditionV1]
    PRODUCTION_RELEASE_BLOCK_CLEAR_CONDITION_V1_EXPIRY_ONLY: _ClassVar[ProductionReleaseBlockClearConditionV1]

class ReleaseIntegrationKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELEASE_INTEGRATION_KIND_V1_UNSPECIFIED: _ClassVar[ReleaseIntegrationKindV1]
    RELEASE_INTEGRATION_KIND_V1_SIGNED_DEPLOYMENT_WEBHOOK: _ClassVar[ReleaseIntegrationKindV1]
    RELEASE_INTEGRATION_KIND_V1_GITHUB_ACTIONS: _ClassVar[ReleaseIntegrationKindV1]
    RELEASE_INTEGRATION_KIND_V1_ARGO_CD: _ClassVar[ReleaseIntegrationKindV1]
    RELEASE_INTEGRATION_KIND_V1_KUBERNETES: _ClassVar[ReleaseIntegrationKindV1]
    RELEASE_INTEGRATION_KIND_V1_PROMPT_REGISTRY_LABEL: _ClassVar[ReleaseIntegrationKindV1]

class ReleaseIntegrationHealthV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELEASE_INTEGRATION_HEALTH_V1_UNSPECIFIED: _ClassVar[ReleaseIntegrationHealthV1]
    RELEASE_INTEGRATION_HEALTH_V1_HEALTHY: _ClassVar[ReleaseIntegrationHealthV1]
    RELEASE_INTEGRATION_HEALTH_V1_DEGRADED: _ClassVar[ReleaseIntegrationHealthV1]
    RELEASE_INTEGRATION_HEALTH_V1_UNREACHABLE: _ClassVar[ReleaseIntegrationHealthV1]
    RELEASE_INTEGRATION_HEALTH_V1_MISCONFIGURED: _ClassVar[ReleaseIntegrationHealthV1]
    RELEASE_INTEGRATION_HEALTH_V1_SECRET_UNAVAILABLE: _ClassVar[ReleaseIntegrationHealthV1]
    RELEASE_INTEGRATION_HEALTH_V1_ARCHIVED: _ClassVar[ReleaseIntegrationHealthV1]

class ReleaseSigningKeyStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELEASE_SIGNING_KEY_STATE_V1_UNSPECIFIED: _ClassVar[ReleaseSigningKeyStateV1]
    RELEASE_SIGNING_KEY_STATE_V1_ACTIVE: _ClassVar[ReleaseSigningKeyStateV1]
    RELEASE_SIGNING_KEY_STATE_V1_ROTATING: _ClassVar[ReleaseSigningKeyStateV1]
    RELEASE_SIGNING_KEY_STATE_V1_REVOKED: _ClassVar[ReleaseSigningKeyStateV1]

class ReleaseStageV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELEASE_STAGE_V1_UNSPECIFIED: _ClassVar[ReleaseStageV1]
    RELEASE_STAGE_V1_PRE_RELEASE: _ClassVar[ReleaseStageV1]
    RELEASE_STAGE_V1_CANARY: _ClassVar[ReleaseStageV1]
    RELEASE_STAGE_V1_RAMP: _ClassVar[ReleaseStageV1]
    RELEASE_STAGE_V1_PRODUCTION: _ClassVar[ReleaseStageV1]
    RELEASE_STAGE_V1_HELD: _ClassVar[ReleaseStageV1]
    RELEASE_STAGE_V1_ABORTING: _ClassVar[ReleaseStageV1]
    RELEASE_STAGE_V1_ABORTED: _ClassVar[ReleaseStageV1]
    RELEASE_STAGE_V1_ROLLING_BACK: _ClassVar[ReleaseStageV1]
    RELEASE_STAGE_V1_ROLLED_BACK: _ClassVar[ReleaseStageV1]
    RELEASE_STAGE_V1_FAILED: _ClassVar[ReleaseStageV1]
    RELEASE_STAGE_V1_VERIFICATION_REQUIRED: _ClassVar[ReleaseStageV1]

class ReleaseActionStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELEASE_ACTION_STATE_V1_UNSPECIFIED: _ClassVar[ReleaseActionStateV1]
    RELEASE_ACTION_STATE_V1_REQUESTED: _ClassVar[ReleaseActionStateV1]
    RELEASE_ACTION_STATE_V1_DISPATCHED: _ClassVar[ReleaseActionStateV1]
    RELEASE_ACTION_STATE_V1_ACCEPTED: _ClassVar[ReleaseActionStateV1]
    RELEASE_ACTION_STATE_V1_OBSERVED: _ClassVar[ReleaseActionStateV1]
    RELEASE_ACTION_STATE_V1_VERIFIED: _ClassVar[ReleaseActionStateV1]
    RELEASE_ACTION_STATE_V1_FAILED: _ClassVar[ReleaseActionStateV1]
    RELEASE_ACTION_STATE_V1_AMBIGUOUS: _ClassVar[ReleaseActionStateV1]
    RELEASE_ACTION_STATE_V1_SUPERSEDED: _ClassVar[ReleaseActionStateV1]

class ReleaseActionTypeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELEASE_ACTION_TYPE_V1_UNSPECIFIED: _ClassVar[ReleaseActionTypeV1]
    RELEASE_ACTION_TYPE_V1_START_CANARY: _ClassVar[ReleaseActionTypeV1]
    RELEASE_ACTION_TYPE_V1_PROMOTE: _ClassVar[ReleaseActionTypeV1]
    RELEASE_ACTION_TYPE_V1_HOLD: _ClassVar[ReleaseActionTypeV1]
    RELEASE_ACTION_TYPE_V1_ABORT: _ClassVar[ReleaseActionTypeV1]
    RELEASE_ACTION_TYPE_V1_ROLLBACK: _ClassVar[ReleaseActionTypeV1]
    RELEASE_ACTION_TYPE_V1_RECONCILE: _ClassVar[ReleaseActionTypeV1]

class ReleaseAdapterOperationV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELEASE_ADAPTER_OPERATION_V1_UNSPECIFIED: _ClassVar[ReleaseAdapterOperationV1]
    RELEASE_ADAPTER_OPERATION_V1_PREVIEW: _ClassVar[ReleaseAdapterOperationV1]
    RELEASE_ADAPTER_OPERATION_V1_START_CANARY: _ClassVar[ReleaseAdapterOperationV1]
    RELEASE_ADAPTER_OPERATION_V1_PROMOTE: _ClassVar[ReleaseAdapterOperationV1]
    RELEASE_ADAPTER_OPERATION_V1_HOLD: _ClassVar[ReleaseAdapterOperationV1]
    RELEASE_ADAPTER_OPERATION_V1_ABORT: _ClassVar[ReleaseAdapterOperationV1]
    RELEASE_ADAPTER_OPERATION_V1_ROLLBACK: _ClassVar[ReleaseAdapterOperationV1]
    RELEASE_ADAPTER_OPERATION_V1_OBSERVE: _ClassVar[ReleaseAdapterOperationV1]

class ReleaseValidationKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELEASE_VALIDATION_KIND_V1_UNSPECIFIED: _ClassVar[ReleaseValidationKindV1]
    RELEASE_VALIDATION_KIND_V1_COMPARABILITY: _ClassVar[ReleaseValidationKindV1]
    RELEASE_VALIDATION_KIND_V1_COMPLETENESS: _ClassVar[ReleaseValidationKindV1]
    RELEASE_VALIDATION_KIND_V1_FRESHNESS: _ClassVar[ReleaseValidationKindV1]
    RELEASE_VALIDATION_KIND_V1_GATE_STATUS: _ClassVar[ReleaseValidationKindV1]
    RELEASE_VALIDATION_KIND_V1_INTEGRATION_HEALTH: _ClassVar[ReleaseValidationKindV1]
    RELEASE_VALIDATION_KIND_V1_ROLLBACK_TARGET: _ClassVar[ReleaseValidationKindV1]

class ReleaseValidationStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELEASE_VALIDATION_STATE_V1_UNSPECIFIED: _ClassVar[ReleaseValidationStateV1]
    RELEASE_VALIDATION_STATE_V1_PASS: _ClassVar[ReleaseValidationStateV1]
    RELEASE_VALIDATION_STATE_V1_WARN: _ClassVar[ReleaseValidationStateV1]
    RELEASE_VALIDATION_STATE_V1_FAIL: _ClassVar[ReleaseValidationStateV1]
    RELEASE_VALIDATION_STATE_V1_INDETERMINATE: _ClassVar[ReleaseValidationStateV1]
    RELEASE_VALIDATION_STATE_V1_NOT_APPLICABLE: _ClassVar[ReleaseValidationStateV1]

class ReleaseActionReasonV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELEASE_ACTION_REASON_V1_UNSPECIFIED: _ClassVar[ReleaseActionReasonV1]
    RELEASE_ACTION_REASON_V1_QUALITY_REGRESSION: _ClassVar[ReleaseActionReasonV1]
    RELEASE_ACTION_REASON_V1_ERROR_RATE_REGRESSION: _ClassVar[ReleaseActionReasonV1]
    RELEASE_ACTION_REASON_V1_LATENCY_REGRESSION: _ClassVar[ReleaseActionReasonV1]
    RELEASE_ACTION_REASON_V1_COST_REGRESSION: _ClassVar[ReleaseActionReasonV1]
    RELEASE_ACTION_REASON_V1_EVIDENCE_STALE: _ClassVar[ReleaseActionReasonV1]
    RELEASE_ACTION_REASON_V1_EXTERNAL_DRIFT: _ClassVar[ReleaseActionReasonV1]
    RELEASE_ACTION_REASON_V1_OPERATOR_REQUEST: _ClassVar[ReleaseActionReasonV1]
    RELEASE_ACTION_REASON_V1_AUTOMATIC_HEALTH_POLICY: _ClassVar[ReleaseActionReasonV1]
    RELEASE_ACTION_REASON_V1_INTEGRATION_UNHEALTHY: _ClassVar[ReleaseActionReasonV1]

class ReleaseVerificationOverrideReasonV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELEASE_VERIFICATION_OVERRIDE_REASON_V1_UNSPECIFIED: _ClassVar[ReleaseVerificationOverrideReasonV1]
    RELEASE_VERIFICATION_OVERRIDE_REASON_V1_EXTERNAL_STATE_CONFIRMED_MANUALLY: _ClassVar[ReleaseVerificationOverrideReasonV1]
    RELEASE_VERIFICATION_OVERRIDE_REASON_V1_INTEGRATION_PERMANENTLY_UNAVAILABLE: _ClassVar[ReleaseVerificationOverrideReasonV1]
    RELEASE_VERIFICATION_OVERRIDE_REASON_V1_OPERATOR_ACCEPTS_RISK: _ClassVar[ReleaseVerificationOverrideReasonV1]

class ReleaseIntegrationCredentialStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELEASE_INTEGRATION_CREDENTIAL_STATE_V1_UNSPECIFIED: _ClassVar[ReleaseIntegrationCredentialStateV1]
    RELEASE_INTEGRATION_CREDENTIAL_STATE_V1_ACTIVE: _ClassVar[ReleaseIntegrationCredentialStateV1]
    RELEASE_INTEGRATION_CREDENTIAL_STATE_V1_REVOKED: _ClassVar[ReleaseIntegrationCredentialStateV1]

class EvaluationReviewSubjectKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_REVIEW_SUBJECT_KIND_V1_UNSPECIFIED: _ClassVar[EvaluationReviewSubjectKindV1]
    EVALUATION_REVIEW_SUBJECT_KIND_V1_EVALUATION_CELL: _ClassVar[EvaluationReviewSubjectKindV1]
    EVALUATION_REVIEW_SUBJECT_KIND_V1_DATASET_PROPOSED_CASE: _ClassVar[EvaluationReviewSubjectKindV1]

class DatasetRedactionDetectorKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_REDACTION_DETECTOR_KIND_V1_UNSPECIFIED: _ClassVar[DatasetRedactionDetectorKindV1]
    DATASET_REDACTION_DETECTOR_KIND_V1_EMAIL: _ClassVar[DatasetRedactionDetectorKindV1]
    DATASET_REDACTION_DETECTOR_KIND_V1_PHONE_E164: _ClassVar[DatasetRedactionDetectorKindV1]
    DATASET_REDACTION_DETECTOR_KIND_V1_CREDIT_CARD: _ClassVar[DatasetRedactionDetectorKindV1]
    DATASET_REDACTION_DETECTOR_KIND_V1_API_KEY: _ClassVar[DatasetRedactionDetectorKindV1]
    DATASET_REDACTION_DETECTOR_KIND_V1_JWT: _ClassVar[DatasetRedactionDetectorKindV1]
    DATASET_REDACTION_DETECTOR_KIND_V1_DENY_PATH: _ClassVar[DatasetRedactionDetectorKindV1]

class DatasetRedactionOutcomeKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_REDACTION_OUTCOME_KIND_V1_UNSPECIFIED: _ClassVar[DatasetRedactionOutcomeKindV1]
    DATASET_REDACTION_OUTCOME_KIND_V1_CLEAN: _ClassVar[DatasetRedactionOutcomeKindV1]
    DATASET_REDACTION_OUTCOME_KIND_V1_REDACTED: _ClassVar[DatasetRedactionOutcomeKindV1]
    DATASET_REDACTION_OUTCOME_KIND_V1_BLOCKED: _ClassVar[DatasetRedactionOutcomeKindV1]
    DATASET_REDACTION_OUTCOME_KIND_V1_INDETERMINATE: _ClassVar[DatasetRedactionOutcomeKindV1]

class DatasetDedupeSubjectKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_DEDUPE_SUBJECT_KIND_V1_UNSPECIFIED: _ClassVar[DatasetDedupeSubjectKindV1]
    DATASET_DEDUPE_SUBJECT_KIND_V1_DATASET_ITEM: _ClassVar[DatasetDedupeSubjectKindV1]
    DATASET_DEDUPE_SUBJECT_KIND_V1_PROPOSED_CASE: _ClassVar[DatasetDedupeSubjectKindV1]

class DatasetDuplicationVerdictV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_DUPLICATION_VERDICT_V1_UNSPECIFIED: _ClassVar[DatasetDuplicationVerdictV1]
    DATASET_DUPLICATION_VERDICT_V1_NO_MATCH: _ClassVar[DatasetDuplicationVerdictV1]
    DATASET_DUPLICATION_VERDICT_V1_EXACT_MATCH: _ClassVar[DatasetDuplicationVerdictV1]
    DATASET_DUPLICATION_VERDICT_V1_NEAR_MATCH: _ClassVar[DatasetDuplicationVerdictV1]
    DATASET_DUPLICATION_VERDICT_V1_CONFLICT: _ClassVar[DatasetDuplicationVerdictV1]
    DATASET_DUPLICATION_VERDICT_V1_UNAVAILABLE: _ClassVar[DatasetDuplicationVerdictV1]

class DatasetDedupeResolutionKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_DEDUPE_RESOLUTION_KIND_V1_UNSPECIFIED: _ClassVar[DatasetDedupeResolutionKindV1]
    DATASET_DEDUPE_RESOLUTION_KIND_V1_AUTO_EXACT: _ClassVar[DatasetDedupeResolutionKindV1]
    DATASET_DEDUPE_RESOLUTION_KIND_V1_MERGE_INTO: _ClassVar[DatasetDedupeResolutionKindV1]
    DATASET_DEDUPE_RESOLUTION_KIND_V1_KEEP_SEPARATE: _ClassVar[DatasetDedupeResolutionKindV1]
    DATASET_DEDUPE_RESOLUTION_KIND_V1_CONFLICT_BLOCKED: _ClassVar[DatasetDedupeResolutionKindV1]
    DATASET_DEDUPE_RESOLUTION_KIND_V1_AUDITED_OVERRIDE_SEPARATE: _ClassVar[DatasetDedupeResolutionKindV1]

class DatasetLeakageSourceKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_LEAKAGE_SOURCE_KIND_V1_UNSPECIFIED: _ClassVar[DatasetLeakageSourceKindV1]
    DATASET_LEAKAGE_SOURCE_KIND_V1_PRIOR_EVALUATION_CASES: _ClassVar[DatasetLeakageSourceKindV1]
    DATASET_LEAKAGE_SOURCE_KIND_V1_ADOPTED_RELEASE_EVIDENCE: _ClassVar[DatasetLeakageSourceKindV1]
    DATASET_LEAKAGE_SOURCE_KIND_V1_CONFIGURED_REFERENCE_SET: _ClassVar[DatasetLeakageSourceKindV1]

class DatasetLeakageVerdictV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_LEAKAGE_VERDICT_V1_UNSPECIFIED: _ClassVar[DatasetLeakageVerdictV1]
    DATASET_LEAKAGE_VERDICT_V1_NO_SIGNAL: _ClassVar[DatasetLeakageVerdictV1]
    DATASET_LEAKAGE_VERDICT_V1_EXACT_OVERLAP: _ClassVar[DatasetLeakageVerdictV1]
    DATASET_LEAKAGE_VERDICT_V1_NEAR_OVERLAP: _ClassVar[DatasetLeakageVerdictV1]
    DATASET_LEAKAGE_VERDICT_V1_NOT_COMPARABLE: _ClassVar[DatasetLeakageVerdictV1]

class DatasetSliceDimensionSourceV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_SLICE_DIMENSION_SOURCE_V1_UNSPECIFIED: _ClassVar[DatasetSliceDimensionSourceV1]
    DATASET_SLICE_DIMENSION_SOURCE_V1_SCHEMA_REVISION: _ClassVar[DatasetSliceDimensionSourceV1]
    DATASET_SLICE_DIMENSION_SOURCE_V1_SHIPPED_COHORT_ONLY: _ClassVar[DatasetSliceDimensionSourceV1]

class DatasetSliceFlagV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_SLICE_FLAG_V1_UNSPECIFIED: _ClassVar[DatasetSliceFlagV1]
    DATASET_SLICE_FLAG_V1_WITHIN_BAND: _ClassVar[DatasetSliceFlagV1]
    DATASET_SLICE_FLAG_V1_OVERREPRESENTED: _ClassVar[DatasetSliceFlagV1]
    DATASET_SLICE_FLAG_V1_UNDERREPRESENTED: _ClassVar[DatasetSliceFlagV1]
    DATASET_SLICE_FLAG_V1_MISSING: _ClassVar[DatasetSliceFlagV1]
    DATASET_SLICE_FLAG_V1_NOT_COMPARABLE: _ClassVar[DatasetSliceFlagV1]

class DatasetSchemaValueKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_SCHEMA_VALUE_KIND_V1_UNSPECIFIED: _ClassVar[DatasetSchemaValueKindV1]
    DATASET_SCHEMA_VALUE_KIND_V1_STRING: _ClassVar[DatasetSchemaValueKindV1]
    DATASET_SCHEMA_VALUE_KIND_V1_INTEGER: _ClassVar[DatasetSchemaValueKindV1]
    DATASET_SCHEMA_VALUE_KIND_V1_DOUBLE: _ClassVar[DatasetSchemaValueKindV1]
    DATASET_SCHEMA_VALUE_KIND_V1_BOOLEAN: _ClassVar[DatasetSchemaValueKindV1]
    DATASET_SCHEMA_VALUE_KIND_V1_TIMESTAMP: _ClassVar[DatasetSchemaValueKindV1]
    DATASET_SCHEMA_VALUE_KIND_V1_JSON: _ClassVar[DatasetSchemaValueKindV1]

class DatasetSchemaCompatibilityPolicyV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_SCHEMA_COMPATIBILITY_POLICY_V1_UNSPECIFIED: _ClassVar[DatasetSchemaCompatibilityPolicyV1]
    DATASET_SCHEMA_COMPATIBILITY_POLICY_V1_ADDITIVE_ONLY: _ClassVar[DatasetSchemaCompatibilityPolicyV1]
    DATASET_SCHEMA_COMPATIBILITY_POLICY_V1_STRICT: _ClassVar[DatasetSchemaCompatibilityPolicyV1]

class DatasetSchemaCompatibilityVerdictKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_SCHEMA_COMPATIBILITY_VERDICT_KIND_V1_UNSPECIFIED: _ClassVar[DatasetSchemaCompatibilityVerdictKindV1]
    DATASET_SCHEMA_COMPATIBILITY_VERDICT_KIND_V1_IDENTICAL: _ClassVar[DatasetSchemaCompatibilityVerdictKindV1]
    DATASET_SCHEMA_COMPATIBILITY_VERDICT_KIND_V1_COMPATIBLE_ADDITIVE: _ClassVar[DatasetSchemaCompatibilityVerdictKindV1]
    DATASET_SCHEMA_COMPATIBILITY_VERDICT_KIND_V1_INCOMPATIBLE: _ClassVar[DatasetSchemaCompatibilityVerdictKindV1]
    DATASET_SCHEMA_COMPATIBILITY_VERDICT_KIND_V1_NOT_COMPARABLE: _ClassVar[DatasetSchemaCompatibilityVerdictKindV1]

class DatasetSchemaChangeKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_SCHEMA_CHANGE_KIND_V1_UNSPECIFIED: _ClassVar[DatasetSchemaChangeKindV1]
    DATASET_SCHEMA_CHANGE_KIND_V1_INPUT_FIELD_ADDED: _ClassVar[DatasetSchemaChangeKindV1]
    DATASET_SCHEMA_CHANGE_KIND_V1_INPUT_FIELD_REMOVED: _ClassVar[DatasetSchemaChangeKindV1]
    DATASET_SCHEMA_CHANGE_KIND_V1_EXPECTED_FIELD_ADDED: _ClassVar[DatasetSchemaChangeKindV1]
    DATASET_SCHEMA_CHANGE_KIND_V1_EXPECTED_FIELD_REMOVED: _ClassVar[DatasetSchemaChangeKindV1]
    DATASET_SCHEMA_CHANGE_KIND_V1_FIELD_TYPE_CHANGED: _ClassVar[DatasetSchemaChangeKindV1]
    DATASET_SCHEMA_CHANGE_KIND_V1_FIELD_MADE_REQUIRED: _ClassVar[DatasetSchemaChangeKindV1]
    DATASET_SCHEMA_CHANGE_KIND_V1_FIELD_MADE_OPTIONAL: _ClassVar[DatasetSchemaChangeKindV1]
    DATASET_SCHEMA_CHANGE_KIND_V1_SLICE_DIMENSION_ADDED: _ClassVar[DatasetSchemaChangeKindV1]
    DATASET_SCHEMA_CHANGE_KIND_V1_SLICE_DIMENSION_REMOVED: _ClassVar[DatasetSchemaChangeKindV1]
    DATASET_SCHEMA_CHANGE_KIND_V1_SLICE_VOCABULARY_NARROWED: _ClassVar[DatasetSchemaChangeKindV1]
    DATASET_SCHEMA_CHANGE_KIND_V1_METADATA_KEY_ADDED: _ClassVar[DatasetSchemaChangeKindV1]
    DATASET_SCHEMA_CHANGE_KIND_V1_METADATA_KEY_REMOVED: _ClassVar[DatasetSchemaChangeKindV1]
    DATASET_SCHEMA_CHANGE_KIND_V1_MAPPING_RULE_CHANGED: _ClassVar[DatasetSchemaChangeKindV1]
    DATASET_SCHEMA_CHANGE_KIND_V1_POLICY_CHANGED: _ClassVar[DatasetSchemaChangeKindV1]

class DatasetCaseRegressionPostureV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_CASE_REGRESSION_POSTURE_V1_UNSPECIFIED: _ClassVar[DatasetCaseRegressionPostureV1]
    DATASET_CASE_REGRESSION_POSTURE_V1_IMPROVED: _ClassVar[DatasetCaseRegressionPostureV1]
    DATASET_CASE_REGRESSION_POSTURE_V1_UNCHANGED: _ClassVar[DatasetCaseRegressionPostureV1]
    DATASET_CASE_REGRESSION_POSTURE_V1_REGRESSED: _ClassVar[DatasetCaseRegressionPostureV1]
    DATASET_CASE_REGRESSION_POSTURE_V1_UNKNOWN: _ClassVar[DatasetCaseRegressionPostureV1]

class DatasetCaseResultPostureV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_CASE_RESULT_POSTURE_V1_UNSPECIFIED: _ClassVar[DatasetCaseResultPostureV1]
    DATASET_CASE_RESULT_POSTURE_V1_PASSED: _ClassVar[DatasetCaseResultPostureV1]
    DATASET_CASE_RESULT_POSTURE_V1_FAILED: _ClassVar[DatasetCaseResultPostureV1]
    DATASET_CASE_RESULT_POSTURE_V1_UNSCORED: _ClassVar[DatasetCaseResultPostureV1]
    DATASET_CASE_RESULT_POSTURE_V1_UNKNOWN: _ClassVar[DatasetCaseResultPostureV1]

class DatasetCaseCompletenessStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_CASE_COMPLETENESS_STATE_V1_UNSPECIFIED: _ClassVar[DatasetCaseCompletenessStateV1]
    DATASET_CASE_COMPLETENESS_STATE_V1_COMPLETE: _ClassVar[DatasetCaseCompletenessStateV1]
    DATASET_CASE_COMPLETENESS_STATE_V1_MISSING_INPUT: _ClassVar[DatasetCaseCompletenessStateV1]
    DATASET_CASE_COMPLETENESS_STATE_V1_MISSING_EXPECTED_OUTPUT: _ClassVar[DatasetCaseCompletenessStateV1]
    DATASET_CASE_COMPLETENESS_STATE_V1_MISSING_BOTH: _ClassVar[DatasetCaseCompletenessStateV1]

class DatasetCaseIdentitySourceV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_CASE_IDENTITY_SOURCE_V1_UNSPECIFIED: _ClassVar[DatasetCaseIdentitySourceV1]
    DATASET_CASE_IDENTITY_SOURCE_V1_DERIVED_FROM_LINEAGE: _ClassVar[DatasetCaseIdentitySourceV1]
    DATASET_CASE_IDENTITY_SOURCE_V1_CONTENT_ONLY: _ClassVar[DatasetCaseIdentitySourceV1]
    DATASET_CASE_IDENTITY_SOURCE_V1_REVIEWER_MERGE: _ClassVar[DatasetCaseIdentitySourceV1]
    DATASET_CASE_IDENTITY_SOURCE_V1_BACKFILLED_FROM_DATASET_ITEM: _ClassVar[DatasetCaseIdentitySourceV1]

class DatasetLineageAnchorAvailabilityV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_LINEAGE_ANCHOR_AVAILABILITY_V1_UNSPECIFIED: _ClassVar[DatasetLineageAnchorAvailabilityV1]
    DATASET_LINEAGE_ANCHOR_AVAILABILITY_V1_AVAILABLE: _ClassVar[DatasetLineageAnchorAvailabilityV1]
    DATASET_LINEAGE_ANCHOR_AVAILABILITY_V1_ANCHOR_TARGET_EXPIRED: _ClassVar[DatasetLineageAnchorAvailabilityV1]
    DATASET_LINEAGE_ANCHOR_AVAILABILITY_V1_ANCHOR_TARGET_DELETED: _ClassVar[DatasetLineageAnchorAvailabilityV1]
    DATASET_LINEAGE_ANCHOR_AVAILABILITY_V1_NOT_APPLICABLE: _ClassVar[DatasetLineageAnchorAvailabilityV1]

class DatasetCaseLineageAnchorKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_CASE_LINEAGE_ANCHOR_KIND_V1_UNSPECIFIED: _ClassVar[DatasetCaseLineageAnchorKindV1]
    DATASET_CASE_LINEAGE_ANCHOR_KIND_V1_NONE: _ClassVar[DatasetCaseLineageAnchorKindV1]
    DATASET_CASE_LINEAGE_ANCHOR_KIND_V1_TELEMETRY: _ClassVar[DatasetCaseLineageAnchorKindV1]
    DATASET_CASE_LINEAGE_ANCHOR_KIND_V1_AGENT_RUN: _ClassVar[DatasetCaseLineageAnchorKindV1]
    DATASET_CASE_LINEAGE_ANCHOR_KIND_V1_EVALUATION_CELL: _ClassVar[DatasetCaseLineageAnchorKindV1]
    DATASET_CASE_LINEAGE_ANCHOR_KIND_V1_RULE_WORKFLOW_STEP: _ClassVar[DatasetCaseLineageAnchorKindV1]

class DatasetCaseDraftStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_CASE_DRAFT_STATE_V1_UNSPECIFIED: _ClassVar[DatasetCaseDraftStateV1]
    DATASET_CASE_DRAFT_STATE_V1_EXTRACTED: _ClassVar[DatasetCaseDraftStateV1]
    DATASET_CASE_DRAFT_STATE_V1_NEEDS_GROUND_TRUTH: _ClassVar[DatasetCaseDraftStateV1]
    DATASET_CASE_DRAFT_STATE_V1_IN_REVIEW: _ClassVar[DatasetCaseDraftStateV1]
    DATASET_CASE_DRAFT_STATE_V1_CHANGES_REQUESTED: _ClassVar[DatasetCaseDraftStateV1]
    DATASET_CASE_DRAFT_STATE_V1_APPROVED: _ClassVar[DatasetCaseDraftStateV1]
    DATASET_CASE_DRAFT_STATE_V1_REJECTED: _ClassVar[DatasetCaseDraftStateV1]
    DATASET_CASE_DRAFT_STATE_V1_MERGED: _ClassVar[DatasetCaseDraftStateV1]
    DATASET_CASE_DRAFT_STATE_V1_NON_REPRESENTATIVE: _ClassVar[DatasetCaseDraftStateV1]
    DATASET_CASE_DRAFT_STATE_V1_PUBLISHED: _ClassVar[DatasetCaseDraftStateV1]
    DATASET_CASE_DRAFT_STATE_V1_SUPERSEDED: _ClassVar[DatasetCaseDraftStateV1]

class DatasetChangesetStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_CHANGESET_STATE_V1_UNSPECIFIED: _ClassVar[DatasetChangesetStateV1]
    DATASET_CHANGESET_STATE_V1_OPEN: _ClassVar[DatasetChangesetStateV1]
    DATASET_CHANGESET_STATE_V1_PREVIEWED: _ClassVar[DatasetChangesetStateV1]
    DATASET_CHANGESET_STATE_V1_REBASE_REQUIRED: _ClassVar[DatasetChangesetStateV1]
    DATASET_CHANGESET_STATE_V1_CONFLICTED: _ClassVar[DatasetChangesetStateV1]
    DATASET_CHANGESET_STATE_V1_COMMITTING: _ClassVar[DatasetChangesetStateV1]
    DATASET_CHANGESET_STATE_V1_COMMITTED: _ClassVar[DatasetChangesetStateV1]
    DATASET_CHANGESET_STATE_V1_ABANDONED: _ClassVar[DatasetChangesetStateV1]
    DATASET_CHANGESET_STATE_V1_FAILED: _ClassVar[DatasetChangesetStateV1]

class DatasetCaseReviewOutcomeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_CASE_REVIEW_OUTCOME_V1_UNSPECIFIED: _ClassVar[DatasetCaseReviewOutcomeV1]
    DATASET_CASE_REVIEW_OUTCOME_V1_CORRECTION: _ClassVar[DatasetCaseReviewOutcomeV1]
    DATASET_CASE_REVIEW_OUTCOME_V1_MERGE_WITH_EXISTING: _ClassVar[DatasetCaseReviewOutcomeV1]
    DATASET_CASE_REVIEW_OUTCOME_V1_NON_REPRESENTATIVE: _ClassVar[DatasetCaseReviewOutcomeV1]
    DATASET_CASE_REVIEW_OUTCOME_V1_NEEDS_GROUND_TRUTH: _ClassVar[DatasetCaseReviewOutcomeV1]
    DATASET_CASE_REVIEW_OUTCOME_V1_APPROVE: _ClassVar[DatasetCaseReviewOutcomeV1]
    DATASET_CASE_REVIEW_OUTCOME_V1_REJECT: _ClassVar[DatasetCaseReviewOutcomeV1]

class DatasetCaseDraftRejectionReasonV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_CASE_DRAFT_REJECTION_REASON_V1_UNSPECIFIED: _ClassVar[DatasetCaseDraftRejectionReasonV1]
    DATASET_CASE_DRAFT_REJECTION_REASON_V1_NON_REPRESENTATIVE: _ClassVar[DatasetCaseDraftRejectionReasonV1]
    DATASET_CASE_DRAFT_REJECTION_REASON_V1_INCORRECT_EXPECTED_OUTPUT: _ClassVar[DatasetCaseDraftRejectionReasonV1]
    DATASET_CASE_DRAFT_REJECTION_REASON_V1_SENSITIVE_CONTENT: _ClassVar[DatasetCaseDraftRejectionReasonV1]
    DATASET_CASE_DRAFT_REJECTION_REASON_V1_DUPLICATE_OF_EXISTING_CASE: _ClassVar[DatasetCaseDraftRejectionReasonV1]
    DATASET_CASE_DRAFT_REJECTION_REASON_V1_INSUFFICIENT_CONTEXT: _ClassVar[DatasetCaseDraftRejectionReasonV1]
    DATASET_CASE_DRAFT_REJECTION_REASON_V1_OUT_OF_SCOPE: _ClassVar[DatasetCaseDraftRejectionReasonV1]
    DATASET_CASE_DRAFT_REJECTION_REASON_V1_SUPERSEDED_BY_OVERRIDE: _ClassVar[DatasetCaseDraftRejectionReasonV1]

class DatasetDraftRefusalKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_DRAFT_REFUSAL_KIND_V1_UNSPECIFIED: _ClassVar[DatasetDraftRefusalKindV1]
    DATASET_DRAFT_REFUSAL_KIND_V1_ILLEGAL_TRANSITION: _ClassVar[DatasetDraftRefusalKindV1]
    DATASET_DRAFT_REFUSAL_KIND_V1_VERSION_CONFLICT: _ClassVar[DatasetDraftRefusalKindV1]
    DATASET_DRAFT_REFUSAL_KIND_V1_RESERVED_BY_ANOTHER_REVIEWER: _ClassVar[DatasetDraftRefusalKindV1]
    DATASET_DRAFT_REFUSAL_KIND_V1_UNRESOLVED_DEDUPE_DECISION: _ClassVar[DatasetDraftRefusalKindV1]
    DATASET_DRAFT_REFUSAL_KIND_V1_DRAFT_TERMINAL: _ClassVar[DatasetDraftRefusalKindV1]
    DATASET_DRAFT_REFUSAL_KIND_V1_BASE_VERSION_MOVED: _ClassVar[DatasetDraftRefusalKindV1]
    DATASET_DRAFT_REFUSAL_KIND_V1_PREVIEW_DIGEST_MISMATCH: _ClassVar[DatasetDraftRefusalKindV1]
    DATASET_DRAFT_REFUSAL_KIND_V1_UNAPPROVED_CASE_PRESENT: _ClassVar[DatasetDraftRefusalKindV1]
    DATASET_DRAFT_REFUSAL_KIND_V1_SCHEMA_INCOMPATIBLE: _ClassVar[DatasetDraftRefusalKindV1]
    DATASET_DRAFT_REFUSAL_KIND_V1_QUALITY_SIGNALS_BLOCK_PUBLISH: _ClassVar[DatasetDraftRefusalKindV1]
    DATASET_DRAFT_REFUSAL_KIND_V1_CHANGESET_NOT_PUBLISHABLE: _ClassVar[DatasetDraftRefusalKindV1]

class ProductionRulePreviewObservationBasisV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCTION_RULE_PREVIEW_OBSERVATION_BASIS_V1_UNSPECIFIED: _ClassVar[ProductionRulePreviewObservationBasisV1]
    PRODUCTION_RULE_PREVIEW_OBSERVATION_BASIS_V1_ADMITTED_EXECUTIONS_IN_WINDOW: _ClassVar[ProductionRulePreviewObservationBasisV1]

class ProductionRulePreviewTargetResolutionV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCTION_RULE_PREVIEW_TARGET_RESOLUTION_V1_UNSPECIFIED: _ClassVar[ProductionRulePreviewTargetResolutionV1]
    PRODUCTION_RULE_PREVIEW_TARGET_RESOLUTION_V1_NOT_APPLICABLE: _ClassVar[ProductionRulePreviewTargetResolutionV1]
    PRODUCTION_RULE_PREVIEW_TARGET_RESOLUTION_V1_RESOLVED: _ClassVar[ProductionRulePreviewTargetResolutionV1]
    PRODUCTION_RULE_PREVIEW_TARGET_RESOLUTION_V1_UNRESOLVED: _ClassVar[ProductionRulePreviewTargetResolutionV1]
    PRODUCTION_RULE_PREVIEW_TARGET_RESOLUTION_V1_ABSENT: _ClassVar[ProductionRulePreviewTargetResolutionV1]

class ProductionRulePreviewRedactionPostureV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCTION_RULE_PREVIEW_REDACTION_POSTURE_V1_UNSPECIFIED: _ClassVar[ProductionRulePreviewRedactionPostureV1]
    PRODUCTION_RULE_PREVIEW_REDACTION_POSTURE_V1_HYDRATION_UNAVAILABLE_IN_PREVIEW: _ClassVar[ProductionRulePreviewRedactionPostureV1]

class ProductionRulePreviewRevisionPinV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCTION_RULE_PREVIEW_REVISION_PIN_V1_UNSPECIFIED: _ClassVar[ProductionRulePreviewRevisionPinV1]
    PRODUCTION_RULE_PREVIEW_REVISION_PIN_V1_PINNED: _ClassVar[ProductionRulePreviewRevisionPinV1]
    PRODUCTION_RULE_PREVIEW_REVISION_PIN_V1_CURRENT_AT_DISPATCH: _ClassVar[ProductionRulePreviewRevisionPinV1]

class ProductionRulePreviewZeroMatchReasonV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCTION_RULE_PREVIEW_ZERO_MATCH_REASON_V1_UNSPECIFIED: _ClassVar[ProductionRulePreviewZeroMatchReasonV1]
    PRODUCTION_RULE_PREVIEW_ZERO_MATCH_REASON_V1_NO_OFFERS_IN_WINDOW: _ClassVar[ProductionRulePreviewZeroMatchReasonV1]
    PRODUCTION_RULE_PREVIEW_ZERO_MATCH_REASON_V1_VERSION_NOT_DISPATCHING: _ClassVar[ProductionRulePreviewZeroMatchReasonV1]
    PRODUCTION_RULE_PREVIEW_ZERO_MATCH_REASON_V1_ALL_SAMPLED_OUT: _ClassVar[ProductionRulePreviewZeroMatchReasonV1]
    PRODUCTION_RULE_PREVIEW_ZERO_MATCH_REASON_V1_ALL_BUDGET_BLOCKED: _ClassVar[ProductionRulePreviewZeroMatchReasonV1]
    PRODUCTION_RULE_PREVIEW_ZERO_MATCH_REASON_V1_ALL_ALREADY_EXECUTED: _ClassVar[ProductionRulePreviewZeroMatchReasonV1]
    PRODUCTION_RULE_PREVIEW_ZERO_MATCH_REASON_V1_MIXED_EXCLUSIONS: _ClassVar[ProductionRulePreviewZeroMatchReasonV1]

class ProductionRulePreviewRefusalKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCTION_RULE_PREVIEW_REFUSAL_KIND_V1_UNSPECIFIED: _ClassVar[ProductionRulePreviewRefusalKindV1]
    PRODUCTION_RULE_PREVIEW_REFUSAL_KIND_V1_SAMPLE_WINDOW_TOO_LARGE: _ClassVar[ProductionRulePreviewRefusalKindV1]
    PRODUCTION_RULE_PREVIEW_REFUSAL_KIND_V1_SAMPLING_RATE_INVALID: _ClassVar[ProductionRulePreviewRefusalKindV1]
    PRODUCTION_RULE_PREVIEW_REFUSAL_KIND_V1_ACTION_KIND_UNKNOWN: _ClassVar[ProductionRulePreviewRefusalKindV1]
    PRODUCTION_RULE_PREVIEW_REFUSAL_KIND_V1_SELECTOR_MALFORMED: _ClassVar[ProductionRulePreviewRefusalKindV1]

class ReleaseObservationConfidenceV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELEASE_OBSERVATION_CONFIDENCE_V1_UNSPECIFIED: _ClassVar[ReleaseObservationConfidenceV1]
    RELEASE_OBSERVATION_CONFIDENCE_V1_EXACT: _ClassVar[ReleaseObservationConfidenceV1]
    RELEASE_OBSERVATION_CONFIDENCE_V1_WINDOW: _ClassVar[ReleaseObservationConfidenceV1]

class MachinePrincipalScopeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MACHINE_PRINCIPAL_SCOPE_V1_UNSPECIFIED: _ClassVar[MachinePrincipalScopeV1]
    MACHINE_PRINCIPAL_SCOPE_V1_EVAL_READ: _ClassVar[MachinePrincipalScopeV1]
    MACHINE_PRINCIPAL_SCOPE_V1_RUN_EXECUTE: _ClassVar[MachinePrincipalScopeV1]
    MACHINE_PRINCIPAL_SCOPE_V1_DATASET_WRITE: _ClassVar[MachinePrincipalScopeV1]
    MACHINE_PRINCIPAL_SCOPE_V1_LEASE_SUBMIT: _ClassVar[MachinePrincipalScopeV1]
    MACHINE_PRINCIPAL_SCOPE_V1_PLATFORM_ANNOTATION_WRITE: _ClassVar[MachinePrincipalScopeV1]

class MachinePrincipalStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MACHINE_PRINCIPAL_STATE_V1_UNSPECIFIED: _ClassVar[MachinePrincipalStateV1]
    MACHINE_PRINCIPAL_STATE_V1_ACTIVE: _ClassVar[MachinePrincipalStateV1]
    MACHINE_PRINCIPAL_STATE_V1_DISABLED: _ClassVar[MachinePrincipalStateV1]
    MACHINE_PRINCIPAL_STATE_V1_REVOKED: _ClassVar[MachinePrincipalStateV1]

class MachineCredentialStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MACHINE_CREDENTIAL_STATE_V1_UNSPECIFIED: _ClassVar[MachineCredentialStateV1]
    MACHINE_CREDENTIAL_STATE_V1_ACTIVE: _ClassVar[MachineCredentialStateV1]
    MACHINE_CREDENTIAL_STATE_V1_ROTATING: _ClassVar[MachineCredentialStateV1]
    MACHINE_CREDENTIAL_STATE_V1_REVOKED: _ClassVar[MachineCredentialStateV1]

class ExternalSubmissionAckKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXTERNAL_SUBMISSION_ACK_KIND_V1_UNSPECIFIED: _ClassVar[ExternalSubmissionAckKindV1]
    EXTERNAL_SUBMISSION_ACK_KIND_V1_ACCEPTED: _ClassVar[ExternalSubmissionAckKindV1]
    EXTERNAL_SUBMISSION_ACK_KIND_V1_ALREADY_SUBMITTED: _ClassVar[ExternalSubmissionAckKindV1]
    EXTERNAL_SUBMISSION_ACK_KIND_V1_REJECTED: _ClassVar[ExternalSubmissionAckKindV1]

class ExternalLeaseRefusalKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXTERNAL_LEASE_REFUSAL_KIND_V1_UNSPECIFIED: _ClassVar[ExternalLeaseRefusalKindV1]
    EXTERNAL_LEASE_REFUSAL_KIND_V1_RUN_NOT_EXECUTABLE: _ClassVar[ExternalLeaseRefusalKindV1]
    EXTERNAL_LEASE_REFUSAL_KIND_V1_CANDIDATE_NOT_EXTERNALLY_EXECUTED: _ClassVar[ExternalLeaseRefusalKindV1]
    EXTERNAL_LEASE_REFUSAL_KIND_V1_LEASE_NOT_HELD: _ClassVar[ExternalLeaseRefusalKindV1]
    EXTERNAL_LEASE_REFUSAL_KIND_V1_LEASE_EXPIRED: _ClassVar[ExternalLeaseRefusalKindV1]
    EXTERNAL_LEASE_REFUSAL_KIND_V1_RENEWAL_BUDGET_EXHAUSTED: _ClassVar[ExternalLeaseRefusalKindV1]
    EXTERNAL_LEASE_REFUSAL_KIND_V1_BOUNDS_EXCEEDED: _ClassVar[ExternalLeaseRefusalKindV1]
    EXTERNAL_LEASE_REFUSAL_KIND_V1_SCOPE_MISSING: _ClassVar[ExternalLeaseRefusalKindV1]

class PlatformAnnotationKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PLATFORM_ANNOTATION_KIND_V1_UNSPECIFIED: _ClassVar[PlatformAnnotationKindV1]
    PLATFORM_ANNOTATION_KIND_V1_DEPLOYMENT: _ClassVar[PlatformAnnotationKindV1]
    PLATFORM_ANNOTATION_KIND_V1_MARKER: _ClassVar[PlatformAnnotationKindV1]
    PLATFORM_ANNOTATION_KIND_V1_HIGHLIGHT: _ClassVar[PlatformAnnotationKindV1]

class PlatformAnnotationLinkKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PLATFORM_ANNOTATION_LINK_KIND_V1_UNSPECIFIED: _ClassVar[PlatformAnnotationLinkKindV1]
    PLATFORM_ANNOTATION_LINK_KIND_V1_RELEASE: _ClassVar[PlatformAnnotationLinkKindV1]
    PLATFORM_ANNOTATION_LINK_KIND_V1_EVALUATION_RUN: _ClassVar[PlatformAnnotationLinkKindV1]
    PLATFORM_ANNOTATION_LINK_KIND_V1_AGENT_RUN: _ClassVar[PlatformAnnotationLinkKindV1]
    PLATFORM_ANNOTATION_LINK_KIND_V1_TRACE: _ClassVar[PlatformAnnotationLinkKindV1]

class PlatformAnnotationRejectionReasonV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PLATFORM_ANNOTATION_REJECTION_REASON_V1_UNSPECIFIED: _ClassVar[PlatformAnnotationRejectionReasonV1]
    PLATFORM_ANNOTATION_REJECTION_REASON_V1_KIND_UNKNOWN: _ClassVar[PlatformAnnotationRejectionReasonV1]
    PLATFORM_ANNOTATION_REJECTION_REASON_V1_TITLE_TOO_LARGE: _ClassVar[PlatformAnnotationRejectionReasonV1]
    PLATFORM_ANNOTATION_REJECTION_REASON_V1_ATTRIBUTE_TOO_LARGE: _ClassVar[PlatformAnnotationRejectionReasonV1]
    PLATFORM_ANNOTATION_REJECTION_REASON_V1_TOO_MANY_ATTRIBUTES: _ClassVar[PlatformAnnotationRejectionReasonV1]
    PLATFORM_ANNOTATION_REJECTION_REASON_V1_TOO_MANY_LINKS: _ClassVar[PlatformAnnotationRejectionReasonV1]
    PLATFORM_ANNOTATION_REJECTION_REASON_V1_LINK_REF_TOO_LARGE: _ClassVar[PlatformAnnotationRejectionReasonV1]
    PLATFORM_ANNOTATION_REJECTION_REASON_V1_RANGE_INVERTED: _ClassVar[PlatformAnnotationRejectionReasonV1]
    PLATFORM_ANNOTATION_REJECTION_REASON_V1_IDEMPOTENCY_KEY_REUSED: _ClassVar[PlatformAnnotationRejectionReasonV1]
    PLATFORM_ANNOTATION_REJECTION_REASON_V1_WINDOW_INVALID: _ClassVar[PlatformAnnotationRejectionReasonV1]

class EvaluationScorerArchivedFilterV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_SCORER_ARCHIVED_FILTER_V1_UNSPECIFIED: _ClassVar[EvaluationScorerArchivedFilterV1]
    EVALUATION_SCORER_ARCHIVED_FILTER_V1_ACTIVE_ONLY: _ClassVar[EvaluationScorerArchivedFilterV1]
    EVALUATION_SCORER_ARCHIVED_FILTER_V1_ARCHIVED_ONLY: _ClassVar[EvaluationScorerArchivedFilterV1]
    EVALUATION_SCORER_ARCHIVED_FILTER_V1_ALL: _ClassVar[EvaluationScorerArchivedFilterV1]
PRINCIPAL_KIND_V1_UNSPECIFIED: PrincipalKindV1
PRINCIPAL_KIND_V1_USER: PrincipalKindV1
PRINCIPAL_KIND_V1_MACHINE: PrincipalKindV1
PRINCIPAL_KIND_V1_SYSTEM: PrincipalKindV1
COMPLETENESS_STATE_V1_UNSPECIFIED: CompletenessStateV1
COMPLETENESS_STATE_V1_COMPLETE: CompletenessStateV1
COMPLETENESS_STATE_V1_INCOMPLETE: CompletenessStateV1
COMPLETENESS_STATE_V1_STALE: CompletenessStateV1
COMPLETENESS_STATE_V1_UNAVAILABLE: CompletenessStateV1
METRIC_AVAILABILITY_STATE_V1_UNSPECIFIED: MetricAvailabilityStateV1
METRIC_AVAILABILITY_STATE_V1_AVAILABLE: MetricAvailabilityStateV1
METRIC_AVAILABILITY_STATE_V1_NOT_SUPPORTED: MetricAvailabilityStateV1
METRIC_AVAILABILITY_STATE_V1_NOT_OBSERVED: MetricAvailabilityStateV1
METRIC_AVAILABILITY_STATE_V1_REDACTED: MetricAvailabilityStateV1
METRIC_AVAILABILITY_STATE_V1_SAMPLED_OUT: MetricAvailabilityStateV1
METRIC_AVAILABILITY_STATE_V1_NOT_SAMPLED: MetricAvailabilityStateV1
METRIC_AVAILABILITY_STATE_V1_PENDING: MetricAvailabilityStateV1
METRIC_AVAILABILITY_STATE_V1_ERROR: MetricAvailabilityStateV1
EVALUATION_ACTION_KIND_V1_UNSPECIFIED: EvaluationActionKindV1
EVALUATION_ACTION_KIND_V1_VIEW: EvaluationActionKindV1
EVALUATION_ACTION_KIND_V1_EDIT: EvaluationActionKindV1
EVALUATION_ACTION_KIND_V1_DUPLICATE: EvaluationActionKindV1
EVALUATION_ACTION_KIND_V1_ARCHIVE: EvaluationActionKindV1
EVALUATION_ACTION_KIND_V1_UNARCHIVE: EvaluationActionKindV1
EVALUATION_ACTION_KIND_V1_LAUNCH_RUN: EvaluationActionKindV1
EVALUATION_ACTION_KIND_V1_CANCEL_RUN: EvaluationActionKindV1
EVALUATION_ACTION_KIND_V1_RETRY_CELLS: EvaluationActionKindV1
EVALUATION_ACTION_KIND_V1_RETRY_SCORERS: EvaluationActionKindV1
ACTION_BLOCKED_REASON_V1_UNSPECIFIED: ActionBlockedReasonV1
ACTION_BLOCKED_REASON_V1_PERMISSION_DENIED: ActionBlockedReasonV1
ACTION_BLOCKED_REASON_V1_INVALID_LIFECYCLE_STATE: ActionBlockedReasonV1
ACTION_BLOCKED_REASON_V1_CAPABILITY_UNAVAILABLE: ActionBlockedReasonV1
ACTION_BLOCKED_REASON_V1_DEPENDENCY_ARCHIVED: ActionBlockedReasonV1
ACTION_BLOCKED_REASON_V1_EVIDENCE_INCOMPLETE: ActionBlockedReasonV1
CAPABILITY_STATE_V1_UNSPECIFIED: CapabilityStateV1
CAPABILITY_STATE_V1_AVAILABLE: CapabilityStateV1
CAPABILITY_STATE_V1_UNAVAILABLE: CapabilityStateV1
CAPABILITY_STATE_V1_DEGRADED: CapabilityStateV1
CAPABILITY_STATE_V1_NOT_LICENSED: CapabilityStateV1
EVALUATION_DEFINITION_STATE_V1_UNSPECIFIED: EvaluationDefinitionStateV1
EVALUATION_DEFINITION_STATE_V1_ACTIVE: EvaluationDefinitionStateV1
EVALUATION_DEFINITION_STATE_V1_ARCHIVED: EvaluationDefinitionStateV1
EVALUATION_RUN_STATE_V1_UNSPECIFIED: EvaluationRunStateV1
EVALUATION_RUN_STATE_V1_DRAFT_PREVIEWED: EvaluationRunStateV1
EVALUATION_RUN_STATE_V1_PREPARING: EvaluationRunStateV1
EVALUATION_RUN_STATE_V1_RUNNING: EvaluationRunStateV1
EVALUATION_RUN_STATE_V1_AWAITING_REVIEW: EvaluationRunStateV1
EVALUATION_RUN_STATE_V1_COMPLETED: EvaluationRunStateV1
EVALUATION_RUN_STATE_V1_PARTIALLY_COMPLETED: EvaluationRunStateV1
EVALUATION_RUN_STATE_V1_FAILED: EvaluationRunStateV1
EVALUATION_RUN_STATE_V1_CANCELLED: EvaluationRunStateV1
EVALUATION_EXECUTION_STATE_V1_UNSPECIFIED: EvaluationExecutionStateV1
EVALUATION_EXECUTION_STATE_V1_PREPARED: EvaluationExecutionStateV1
EVALUATION_EXECUTION_STATE_V1_QUEUED: EvaluationExecutionStateV1
EVALUATION_EXECUTION_STATE_V1_LEASED: EvaluationExecutionStateV1
EVALUATION_EXECUTION_STATE_V1_RUNNING: EvaluationExecutionStateV1
EVALUATION_EXECUTION_STATE_V1_AWAITING_SUBMISSION: EvaluationExecutionStateV1
EVALUATION_EXECUTION_STATE_V1_SUCCEEDED: EvaluationExecutionStateV1
EVALUATION_EXECUTION_STATE_V1_FAILED: EvaluationExecutionStateV1
EVALUATION_EXECUTION_STATE_V1_TIMED_OUT: EvaluationExecutionStateV1
EVALUATION_EXECUTION_STATE_V1_LEASE_EXPIRED: EvaluationExecutionStateV1
EVALUATION_EXECUTION_STATE_V1_CANCELLED: EvaluationExecutionStateV1
EVALUATION_EXECUTION_STATE_V1_SKIPPED: EvaluationExecutionStateV1
EVALUATION_EXECUTION_STATE_V1_SUPERSEDED: EvaluationExecutionStateV1
EVALUATION_LAUNCH_MODE_V1_UNSPECIFIED: EvaluationLaunchModeV1
EVALUATION_LAUNCH_MODE_V1_COMPARISON: EvaluationLaunchModeV1
EVALUATION_LAUNCH_MODE_V1_VALIDATION: EvaluationLaunchModeV1
EVALUATION_LAUNCH_MODE_V1_SCRATCH: EvaluationLaunchModeV1
EVALUATION_SUBJECT_KIND_V1_UNSPECIFIED: EvaluationSubjectKindV1
EVALUATION_SUBJECT_KIND_V1_RESPONSE: EvaluationSubjectKindV1
EVALUATION_SUBJECT_KIND_V1_CONVERSATION_TURN: EvaluationSubjectKindV1
EVALUATION_SUBJECT_KIND_V1_CONVERSATION: EvaluationSubjectKindV1
EVALUATION_SUBJECT_KIND_V1_TRAJECTORY: EvaluationSubjectKindV1
EVALUATION_SUBJECT_KIND_V1_MODEL_GENERATION: EvaluationSubjectKindV1
EVALUATION_SUBJECT_KIND_V1_TOOL_CALL: EvaluationSubjectKindV1
EVALUATION_SUBJECT_KIND_V1_RETRIEVAL_OPERATION: EvaluationSubjectKindV1
COHORT_NORMALIZATION_MODE_V1_UNSPECIFIED: CohortNormalizationModeV1
COHORT_NORMALIZATION_MODE_V1_NONE: CohortNormalizationModeV1
COHORT_NORMALIZATION_MODE_V1_EQUAL_WEIGHT: CohortNormalizationModeV1
COHORT_NORMALIZATION_MODE_V1_CASE_COUNT_WEIGHT: CohortNormalizationModeV1
EVALUATION_CANDIDATE_KIND_V1_UNSPECIFIED: EvaluationCandidateKindV1
EVALUATION_CANDIDATE_KIND_V1_RECORDED_OUTPUT: EvaluationCandidateKindV1
EVALUATION_CANDIDATE_KIND_V1_PROVIDER_PROMPT: EvaluationCandidateKindV1
EVALUATION_CANDIDATE_KIND_V1_HTTP_JSON_ENDPOINT: EvaluationCandidateKindV1
EVALUATION_CANDIDATE_KIND_V1_EXPERIMENT_TARGET_REF: EvaluationCandidateKindV1
EVALUATION_CANDIDATE_KIND_V1_AGENT_RELEASE_REVISION: EvaluationCandidateKindV1
EVALUATION_CANDIDATE_KIND_V1_EXTERNALLY_EXECUTED: EvaluationCandidateKindV1
EVALUATION_CANDIDATE_KIND_V1_CONVERSATION_SIMULATION: EvaluationCandidateKindV1
CONVERSATION_TERMINATION_KIND_V1_UNSPECIFIED: ConversationTerminationKindV1
CONVERSATION_TERMINATION_KIND_V1_MAX_TURNS: ConversationTerminationKindV1
CONVERSATION_TERMINATION_KIND_V1_GOAL_SATISFIED: ConversationTerminationKindV1
CONVERSATION_TERMINATION_KIND_V1_SIMULATED_USER_EXIT: ConversationTerminationKindV1
SIDE_EFFECT_POSTURE_V1_UNSPECIFIED: SideEffectPostureV1
SIDE_EFFECT_POSTURE_V1_NONE: SideEffectPostureV1
SIDE_EFFECT_POSTURE_V1_IDEMPOTENT_READS: SideEffectPostureV1
SIDE_EFFECT_POSTURE_V1_MUTATING_ATTESTED: SideEffectPostureV1
SIDE_EFFECT_POSTURE_V1_UNATTESTED: SideEffectPostureV1
EVALUATION_SCORER_TARGET_KIND_V1_UNSPECIFIED: EvaluationScorerTargetKindV1
EVALUATION_SCORER_TARGET_KIND_V1_SUITE_REF: EvaluationScorerTargetKindV1
EVALUATION_SCORER_TARGET_KIND_V1_EXPLICIT_LIST: EvaluationScorerTargetKindV1
EVALUATION_SCORER_SUITE_COMBINE_RULE_V1_UNSPECIFIED: EvaluationScorerSuiteCombineRuleV1
EVALUATION_SCORER_SUITE_COMBINE_RULE_V1_GATES_THEN_WEIGHTED_MEAN: EvaluationScorerSuiteCombineRuleV1
EVALUATION_DECISION_RULE_KIND_V1_UNSPECIFIED: EvaluationDecisionRuleKindV1
EVALUATION_DECISION_RULE_KIND_V1_MIN_SCORE: EvaluationDecisionRuleKindV1
EVALUATION_DECISION_RULE_KIND_V1_MAX_REGRESSION: EvaluationDecisionRuleKindV1
EVALUATION_DECISION_RULE_KIND_V1_MAX_COST: EvaluationDecisionRuleKindV1
EVALUATION_DECISION_RULE_KIND_V1_MIN_COVERAGE: EvaluationDecisionRuleKindV1
EVALUATION_TRIALS_SOURCE_V1_UNSPECIFIED: EvaluationTrialsSourceV1
EVALUATION_TRIALS_SOURCE_V1_AUTHORED: EvaluationTrialsSourceV1
EVALUATION_TRIALS_SOURCE_V1_COMPARISON_DEFAULT: EvaluationTrialsSourceV1
EVALUATION_TRIALS_SOURCE_V1_SINGLE_CANDIDATE_DEFAULT: EvaluationTrialsSourceV1
EVALUATION_DEFINITION_CONFLICT_SECTION_V1_UNSPECIFIED: EvaluationDefinitionConflictSectionV1
EVALUATION_DEFINITION_CONFLICT_SECTION_V1_IDENTITY: EvaluationDefinitionConflictSectionV1
EVALUATION_DEFINITION_CONFLICT_SECTION_V1_COHORTS: EvaluationDefinitionConflictSectionV1
EVALUATION_DEFINITION_CONFLICT_SECTION_V1_CANDIDATES: EvaluationDefinitionConflictSectionV1
EVALUATION_DEFINITION_CONFLICT_SECTION_V1_SCORERS: EvaluationDefinitionConflictSectionV1
EVALUATION_DEFINITION_CONFLICT_SECTION_V1_EXECUTION_POLICY: EvaluationDefinitionConflictSectionV1
EVALUATION_DEFINITION_CONFLICT_SECTION_V1_BUDGET: EvaluationDefinitionConflictSectionV1
EVALUATION_DEFINITION_CONFLICT_SECTION_V1_DECISION_POLICY: EvaluationDefinitionConflictSectionV1
EVALUATION_DEFINITION_CONFLICT_SECTION_V1_HUMAN_REVIEW: EvaluationDefinitionConflictSectionV1
EVALUATION_DEFINITION_CONFLICT_SECTION_V1_METADATA: EvaluationDefinitionConflictSectionV1
EVALUATION_DEFINITION_SORT_KEY_V1_UNSPECIFIED: EvaluationDefinitionSortKeyV1
EVALUATION_DEFINITION_SORT_KEY_V1_CREATED_AT: EvaluationDefinitionSortKeyV1
EVALUATION_DEFINITION_SORT_KEY_V1_UPDATED_AT: EvaluationDefinitionSortKeyV1
EVALUATION_DEFINITION_SORT_KEY_V1_DISPLAY_NAME: EvaluationDefinitionSortKeyV1
EVALUATION_BUILDER_READINESS_SEVERITY_V1_UNSPECIFIED: EvaluationBuilderReadinessSeverityV1
EVALUATION_BUILDER_READINESS_SEVERITY_V1_INFO: EvaluationBuilderReadinessSeverityV1
EVALUATION_BUILDER_READINESS_SEVERITY_V1_WARNING: EvaluationBuilderReadinessSeverityV1
EVALUATION_BUILDER_READINESS_SEVERITY_V1_BLOCKING: EvaluationBuilderReadinessSeverityV1
EVALUATION_BUILDER_SECTION_V1_UNSPECIFIED: EvaluationBuilderSectionV1
EVALUATION_BUILDER_SECTION_V1_WORKLOAD: EvaluationBuilderSectionV1
EVALUATION_BUILDER_SECTION_V1_CANDIDATES: EvaluationBuilderSectionV1
EVALUATION_BUILDER_SECTION_V1_SCORECARD: EvaluationBuilderSectionV1
EVALUATION_BUILDER_SECTION_V1_CREDENTIALS: EvaluationBuilderSectionV1
EVALUATION_BUILDER_SECTION_V1_EXECUTION: EvaluationBuilderSectionV1
EVALUATION_FAILURE_STAGE_V1_UNSPECIFIED: EvaluationFailureStageV1
EVALUATION_FAILURE_STAGE_V1_PREPARATION: EvaluationFailureStageV1
EVALUATION_FAILURE_STAGE_V1_COHORT_RESOLUTION: EvaluationFailureStageV1
EVALUATION_FAILURE_STAGE_V1_CANDIDATE_EXECUTION: EvaluationFailureStageV1
EVALUATION_FAILURE_STAGE_V1_SUBJECT_RESOLUTION: EvaluationFailureStageV1
EVALUATION_FAILURE_STAGE_V1_SCORER_EXECUTION: EvaluationFailureStageV1
EVALUATION_FAILURE_STAGE_V1_AGGREGATION: EvaluationFailureStageV1
EVALUATION_FAILURE_STAGE_V1_FACT_PUBLICATION: EvaluationFailureStageV1
EVALUATION_FAILURE_STAGE_V1_HUMAN_REVIEW: EvaluationFailureStageV1
EVALUATION_FAILURE_STAGE_V1_EXTERNAL_LEASE: EvaluationFailureStageV1
RETRYABILITY_V1_UNSPECIFIED: RetryabilityV1
RETRYABILITY_V1_RETRYABLE: RetryabilityV1
RETRYABILITY_V1_NOT_RETRYABLE: RetryabilityV1
RETRYABILITY_V1_RETRYABLE_AFTER_FIX: RetryabilityV1
RECOVERY_ACTION_V1_UNSPECIFIED: RecoveryActionV1
RECOVERY_ACTION_V1_RETRY: RecoveryActionV1
RECOVERY_ACTION_V1_RE_PREVIEW: RecoveryActionV1
RECOVERY_ACTION_V1_EDIT_DEFINITION: RecoveryActionV1
RECOVERY_ACTION_V1_WAIT: RecoveryActionV1
RECOVERY_ACTION_V1_CONTACT_SUPPORT: RecoveryActionV1
EVALUATION_RATE_SOURCE_V1_UNSPECIFIED: EvaluationRateSourceV1
EVALUATION_RATE_SOURCE_V1_CANDIDATE_AUTHORED: EvaluationRateSourceV1
EVALUATION_RATE_SOURCE_V1_STATIC_REGISTRY: EvaluationRateSourceV1
EVALUATION_RATE_SOURCE_V1_STATIC_REGISTRY_PROVISIONAL: EvaluationRateSourceV1
EVALUATION_RATE_SOURCE_V1_ORG_NEGOTIATED_OVERRIDE: EvaluationRateSourceV1
EVALUATION_RATE_MODIFIER_KIND_V1_UNSPECIFIED: EvaluationRateModifierKindV1
EVALUATION_RATE_MODIFIER_KIND_V1_CONTEXT_LENGTH_TIER: EvaluationRateModifierKindV1
EVALUATION_RATE_MODIFIER_KIND_V1_SERVICE_TIER: EvaluationRateModifierKindV1
EVALUATION_RATE_MODIFIER_KIND_V1_BATCH_DISCOUNT: EvaluationRateModifierKindV1
EVALUATION_RATE_MODIFIER_KIND_V1_OFF_PEAK_WINDOW: EvaluationRateModifierKindV1
EVALUATION_RATE_MODIFIER_KIND_V1_LONG_OUTPUT_TIER: EvaluationRateModifierKindV1
EVALUATION_RATE_MODIFIER_KIND_V1_CACHE_TTL_TIER: EvaluationRateModifierKindV1
EVALUATION_RATE_MODIFIER_KIND_V1_REGIONAL_UPLIFT: EvaluationRateModifierKindV1
EVALUATION_RATE_MODIFIER_KIND_V1_NON_TOKEN_CHARGE: EvaluationRateModifierKindV1
EVALUATION_RATE_STALENESS_V1_UNSPECIFIED: EvaluationRateStalenessV1
EVALUATION_RATE_STALENESS_V1_FRESH: EvaluationRateStalenessV1
EVALUATION_RATE_STALENESS_V1_STALE: EvaluationRateStalenessV1
EVALUATION_OPERATION_KIND_V1_UNSPECIFIED: EvaluationOperationKindV1
EVALUATION_OPERATION_KIND_V1_PREPARE_RUN: EvaluationOperationKindV1
EVALUATION_OPERATION_KIND_V1_RETRY_CELLS: EvaluationOperationKindV1
EVALUATION_OPERATION_KIND_V1_CANCEL_RUN: EvaluationOperationKindV1
EVALUATION_OPERATION_KIND_V1_EXPORT: EvaluationOperationKindV1
EVALUATION_OPERATION_STATE_V1_UNSPECIFIED: EvaluationOperationStateV1
EVALUATION_OPERATION_STATE_V1_PENDING: EvaluationOperationStateV1
EVALUATION_OPERATION_STATE_V1_RUNNING: EvaluationOperationStateV1
EVALUATION_OPERATION_STATE_V1_SUCCEEDED: EvaluationOperationStateV1
EVALUATION_OPERATION_STATE_V1_FAILED: EvaluationOperationStateV1
EVALUATION_OPERATION_STATE_V1_CANCELLED: EvaluationOperationStateV1
EVALUATION_PREVIEW_BLOCKER_KIND_V1_UNSPECIFIED: EvaluationPreviewBlockerKindV1
EVALUATION_PREVIEW_BLOCKER_KIND_V1_SCALE_LIMIT_EXCEEDED: EvaluationPreviewBlockerKindV1
EVALUATION_PREVIEW_BLOCKER_KIND_V1_CAPABILITY_UNAVAILABLE: EvaluationPreviewBlockerKindV1
EVALUATION_PREVIEW_BLOCKER_KIND_V1_MISSING_DEPENDENCY: EvaluationPreviewBlockerKindV1
EVALUATION_PREVIEW_BLOCKER_KIND_V1_UNATTESTED_SIDE_EFFECT: EvaluationPreviewBlockerKindV1
EVALUATION_PREVIEW_BLOCKER_KIND_V1_SCORER_BINDING_INCOMPLETE: EvaluationPreviewBlockerKindV1
EVALUATION_LAUNCH_REJECTION_KIND_V1_UNSPECIFIED: EvaluationLaunchRejectionKindV1
EVALUATION_LAUNCH_REJECTION_KIND_V1_PREVIEW_EXPIRED: EvaluationLaunchRejectionKindV1
EVALUATION_LAUNCH_REJECTION_KIND_V1_PREVIEW_MALFORMED: EvaluationLaunchRejectionKindV1
EVALUATION_LAUNCH_REJECTION_KIND_V1_DEFINITION_REVISION_MOVED: EvaluationLaunchRejectionKindV1
EVALUATION_LAUNCH_REJECTION_KIND_V1_DEPENDENCY_VERSIONS_MOVED: EvaluationLaunchRejectionKindV1
EVALUATION_LAUNCH_REJECTION_KIND_V1_CARDINALITY_MOVED: EvaluationLaunchRejectionKindV1
EVALUATION_LAUNCH_REJECTION_KIND_V1_CAPABILITY_SET_MOVED: EvaluationLaunchRejectionKindV1
EVALUATION_LAUNCH_REJECTION_KIND_V1_IDEMPOTENCY_KEY_REUSED: EvaluationLaunchRejectionKindV1
EVALUATION_RETRY_INELIGIBILITY_V1_UNSPECIFIED: EvaluationRetryIneligibilityV1
EVALUATION_RETRY_INELIGIBILITY_V1_CELL_SUCCEEDED_IMMUTABLE: EvaluationRetryIneligibilityV1
EVALUATION_RETRY_INELIGIBILITY_V1_CELL_NOT_TERMINAL: EvaluationRetryIneligibilityV1
EVALUATION_RETRY_INELIGIBILITY_V1_CELL_SKIPPED_BY_BUDGET: EvaluationRetryIneligibilityV1
EVALUATION_RETRY_INELIGIBILITY_V1_CELL_CANCELLED: EvaluationRetryIneligibilityV1
EVALUATION_RETRY_INELIGIBILITY_V1_CELL_AWAITING_REVIEW: EvaluationRetryIneligibilityV1
EVALUATION_RETRY_INELIGIBILITY_V1_CELL_UNKNOWN: EvaluationRetryIneligibilityV1
EVALUATION_SCORER_RETRY_INELIGIBILITY_V1_UNSPECIFIED: EvaluationScorerRetryIneligibilityV1
EVALUATION_SCORER_RETRY_INELIGIBILITY_V1_CANDIDATE_OUTPUT_ABSENT: EvaluationScorerRetryIneligibilityV1
EVALUATION_SCORER_RETRY_INELIGIBILITY_V1_SCORER_NOT_DETERMINISTIC: EvaluationScorerRetryIneligibilityV1
EVALUATION_SCORER_RETRY_INELIGIBILITY_V1_ATTEMPT_CEILING_REACHED: EvaluationScorerRetryIneligibilityV1
EVALUATION_SCORER_RETRY_INELIGIBILITY_V1_COORDINATE_UNKNOWN: EvaluationScorerRetryIneligibilityV1
EVALUATION_SCORER_RETRY_INELIGIBILITY_V1_JUDGE_REGRADE_NOT_DISPATCHABLE: EvaluationScorerRetryIneligibilityV1
EVALUATION_SCORER_RETRY_INELIGIBILITY_V1_JUDGE_REGRADE_REQUIRES_JOB: EvaluationScorerRetryIneligibilityV1
EVALUATION_SCORER_RETRY_INELIGIBILITY_V1_SCORER_IS_A_DERIVED_SUITE: EvaluationScorerRetryIneligibilityV1
COST_CATEGORY_V1_UNSPECIFIED: CostCategoryV1
COST_CATEGORY_V1_CANDIDATE_MODEL: CostCategoryV1
COST_CATEGORY_V1_EVALUATOR_MODEL: CostCategoryV1
COST_CATEGORY_V1_TOOL: CostCategoryV1
COST_CATEGORY_V1_RETRIEVAL: CostCategoryV1
COST_CATEGORY_V1_EXTERNAL_API: CostCategoryV1
COST_POSTURE_V1_UNSPECIFIED: CostPostureV1
COST_POSTURE_V1_ACTUAL_PROVIDER_BILLED: CostPostureV1
COST_POSTURE_V1_ESTIMATED: CostPostureV1
PROVIDER_STATUS_CLASS_V1_UNSPECIFIED: ProviderStatusClassV1
PROVIDER_STATUS_CLASS_V1_OK: ProviderStatusClassV1
PROVIDER_STATUS_CLASS_V1_CLIENT_ERROR: ProviderStatusClassV1
PROVIDER_STATUS_CLASS_V1_SERVER_ERROR: ProviderStatusClassV1
PROVIDER_STATUS_CLASS_V1_TIMEOUT: ProviderStatusClassV1
PROVIDER_STATUS_CLASS_V1_RATE_LIMITED: ProviderStatusClassV1
PROVIDER_STATUS_CLASS_V1_CANCELLED: ProviderStatusClassV1
PROVIDER_STATUS_CLASS_V1_NOT_APPLICABLE: ProviderStatusClassV1
INSTRUMENTATION_COMPLETENESS_STATE_V1_UNSPECIFIED: InstrumentationCompletenessStateV1
INSTRUMENTATION_COMPLETENESS_STATE_V1_COMPLETE: InstrumentationCompletenessStateV1
INSTRUMENTATION_COMPLETENESS_STATE_V1_PARTIAL: InstrumentationCompletenessStateV1
INSTRUMENTATION_COMPLETENESS_STATE_V1_UNINSTRUMENTED: InstrumentationCompletenessStateV1
INSTRUMENTATION_COMPLETENESS_STATE_V1_REDACTED: InstrumentationCompletenessStateV1
INSTRUMENTATION_COMPLETENESS_STATE_V1_SAMPLED_OUT: InstrumentationCompletenessStateV1
INSTRUMENTATION_COMPLETENESS_STATE_V1_CONVENTION_ALIAS: InstrumentationCompletenessStateV1
EXECUTION_METRICS_SCOPE_V1_UNSPECIFIED: ExecutionMetricsScopeV1
EXECUTION_METRICS_SCOPE_V1_CANDIDATE_EXECUTION: ExecutionMetricsScopeV1
EXECUTION_METRICS_SCOPE_V1_SCORER_EXECUTION: ExecutionMetricsScopeV1
EXECUTION_METRICS_SCOPE_V1_EVALUATOR_AGGREGATE: ExecutionMetricsScopeV1
EXECUTION_METRICS_SCOPE_V1_EVALUATION_TOTAL: ExecutionMetricsScopeV1
EXECUTION_METRICS_SCOPE_V1_EVALUATOR_EXECUTION: ExecutionMetricsScopeV1
EVALUATION_VERDICT_V1_UNSPECIFIED: EvaluationVerdictV1
EVALUATION_VERDICT_V1_PASS: EvaluationVerdictV1
EVALUATION_VERDICT_V1_FAIL: EvaluationVerdictV1
EVALUATION_VERDICT_V1_ERROR: EvaluationVerdictV1
EVALUATION_VERDICT_V1_SKIPPED: EvaluationVerdictV1
EVALUATION_VERDICT_V1_NOT_APPLICABLE: EvaluationVerdictV1
EVALUATION_CANDIDATE_SOURCE_V1_UNSPECIFIED: EvaluationCandidateSourceV1
EVALUATION_CANDIDATE_SOURCE_V1_RECORDED_OUTPUT: EvaluationCandidateSourceV1
EVALUATION_CANDIDATE_SOURCE_V1_PROVIDER_CALL: EvaluationCandidateSourceV1
EVALUATION_CANDIDATE_SOURCE_V1_HTTP_ENDPOINT: EvaluationCandidateSourceV1
EVALUATION_CANDIDATE_SOURCE_V1_EXTERNAL_SUBMISSION: EvaluationCandidateSourceV1
EVALUATION_RUN_OVERVIEW_PROFILE_V1_UNSPECIFIED: EvaluationRunOverviewProfileV1
EVALUATION_RUN_OVERVIEW_PROFILE_V1_INITIAL: EvaluationRunOverviewProfileV1
EVALUATION_RUN_OVERVIEW_PROFILE_V1_FULL: EvaluationRunOverviewProfileV1
EVALUATION_SCORER_COMPLETION_STATE_V1_UNSPECIFIED: EvaluationScorerCompletionStateV1
EVALUATION_SCORER_COMPLETION_STATE_V1_NOT_STARTED: EvaluationScorerCompletionStateV1
EVALUATION_SCORER_COMPLETION_STATE_V1_PARTIAL: EvaluationScorerCompletionStateV1
EVALUATION_SCORER_COMPLETION_STATE_V1_COMPLETE: EvaluationScorerCompletionStateV1
EVALUATION_SCORER_COMPLETION_STATE_V1_AWAITING_HUMAN_REVIEW: EvaluationScorerCompletionStateV1
EVALUATION_RESYNC_REASON_V1_UNSPECIFIED: EvaluationResyncReasonV1
EVALUATION_RESYNC_REASON_V1_SNAPSHOT_SUPERSEDED: EvaluationResyncReasonV1
EVALUATION_RESYNC_REASON_V1_FILTER_CHANGED: EvaluationResyncReasonV1
EVALUATION_RESYNC_REASON_V1_CURSOR_MALFORMED: EvaluationResyncReasonV1
EVALUATION_RESYNC_REASON_V1_BACKLOG_EXCEEDED: EvaluationResyncReasonV1
EVALUATION_DECISION_DRIVER_KIND_V1_UNSPECIFIED: EvaluationDecisionDriverKindV1
EVALUATION_DECISION_DRIVER_KIND_V1_SCORER_REGRESSION: EvaluationDecisionDriverKindV1
EVALUATION_DECISION_DRIVER_KIND_V1_SCORER_FAILURE_CONCENTRATION: EvaluationDecisionDriverKindV1
EVALUATION_DECISION_DRIVER_KIND_V1_MISSING_SCORE_EVIDENCE: EvaluationDecisionDriverKindV1
EVALUATION_DECISION_DRIVER_KIND_V1_CANDIDATE_EXECUTION_FAILURE: EvaluationDecisionDriverKindV1
EVALUATION_DECISION_CONSEQUENCE_V1_UNSPECIFIED: EvaluationDecisionConsequenceV1
EVALUATION_DECISION_CONSEQUENCE_V1_BLOCKS_RELEASE_GATE: EvaluationDecisionConsequenceV1
EVALUATION_DECISION_CONSEQUENCE_V1_QUALITY_REGRESSION: EvaluationDecisionConsequenceV1
EVALUATION_DECISION_CONSEQUENCE_V1_QUALITY_FAILURE: EvaluationDecisionConsequenceV1
EVALUATION_DECISION_CONSEQUENCE_V1_EVIDENCE_INCOMPLETE: EvaluationDecisionConsequenceV1
STATISTICAL_TEST_V1_UNSPECIFIED: StatisticalTestV1
STATISTICAL_TEST_V1_MCNEMAR_EXACT: StatisticalTestV1
MULTIPLE_COMPARISON_CORRECTION_V1_UNSPECIFIED: MultipleComparisonCorrectionV1
MULTIPLE_COMPARISON_CORRECTION_V1_NONE: MultipleComparisonCorrectionV1
MULTIPLE_COMPARISON_CORRECTION_V1_HOLM: MultipleComparisonCorrectionV1
STATISTICAL_VALIDITY_V1_UNSPECIFIED: StatisticalValidityV1
STATISTICAL_VALIDITY_V1_VALID: StatisticalValidityV1
STATISTICAL_VALIDITY_V1_INSUFFICIENT_SAMPLE: StatisticalValidityV1
STATISTICAL_VALIDITY_V1_NOT_APPLICABLE: StatisticalValidityV1
EVALUATION_REPEAT_BASIS_V1_UNSPECIFIED: EvaluationRepeatBasisV1
EVALUATION_REPEAT_BASIS_V1_SCORED_ROLLOUTS: EvaluationRepeatBasisV1
EVALUATION_REPEAT_BASIS_V1_PREPARED_ROLLOUTS: EvaluationRepeatBasisV1
COMPARISON_ALIGNMENT_RULE_V1_UNSPECIFIED: ComparisonAlignmentRuleV1
COMPARISON_ALIGNMENT_RULE_V1_SINGLE_ROLLOUT: ComparisonAlignmentRuleV1
COMPARISON_ALIGNMENT_RULE_V1_MAJORITY_TIE_IS_NEITHER_WIN: ComparisonAlignmentRuleV1
EVALUATION_SLICE_DIMENSION_V1_UNSPECIFIED: EvaluationSliceDimensionV1
EVALUATION_SLICE_DIMENSION_V1_COHORT: EvaluationSliceDimensionV1
DATA_QUALITY_FINDING_KIND_V1_UNSPECIFIED: DataQualityFindingKindV1
DATA_QUALITY_FINDING_KIND_V1_DUPLICATE_CASES: DataQualityFindingKindV1
DATA_QUALITY_FINDING_KIND_V1_MISSING_GROUND_TRUTH: DataQualityFindingKindV1
DATA_QUALITY_FINDING_KIND_V1_UNSCORED_EVIDENCE: DataQualityFindingKindV1
DATA_QUALITY_FINDING_KIND_V1_COHORT_COVERAGE_GAP: DataQualityFindingKindV1
DATA_QUALITY_FINDING_KIND_V1_CONFLICTING_EXPECTED_OUTPUT: DataQualityFindingKindV1
DATA_QUALITY_FINDING_KIND_V1_LEAKAGE_SIGNAL: DataQualityFindingKindV1
DATA_QUALITY_FINDING_KIND_V1_DISTRIBUTION_DRIFT: DataQualityFindingKindV1
FINDING_SEVERITY_V1_UNSPECIFIED: FindingSeverityV1
FINDING_SEVERITY_V1_INFO: FindingSeverityV1
FINDING_SEVERITY_V1_WARNING: FindingSeverityV1
FINDING_SEVERITY_V1_BLOCKING: FindingSeverityV1
EVALUATION_DECISION_OUTCOME_V1_UNSPECIFIED: EvaluationDecisionOutcomeV1
EVALUATION_DECISION_OUTCOME_V1_RECOMMENDED: EvaluationDecisionOutcomeV1
EVALUATION_DECISION_OUTCOME_V1_NO_CLEAR_WINNER: EvaluationDecisionOutcomeV1
EVALUATION_DECISION_OUTCOME_V1_INSUFFICIENT_EVIDENCE: EvaluationDecisionOutcomeV1
EVALUATION_DECISION_OUTCOME_V1_BLOCKED: EvaluationDecisionOutcomeV1
EVALUATION_DECISION_PROVENANCE_V1_UNSPECIFIED: EvaluationDecisionProvenanceV1
EVALUATION_DECISION_PROVENANCE_V1_ADOPTED: EvaluationDecisionProvenanceV1
EVALUATION_DECISION_PROVENANCE_V1_EXPLORATION: EvaluationDecisionProvenanceV1
DECISION_BLOCKER_KIND_V1_UNSPECIFIED: DecisionBlockerKindV1
DECISION_BLOCKER_KIND_V1_MIN_SCORE_NOT_MET: DecisionBlockerKindV1
DECISION_BLOCKER_KIND_V1_MAX_REGRESSION_EXCEEDED: DecisionBlockerKindV1
DECISION_BLOCKER_KIND_V1_MAX_COST_EXCEEDED: DecisionBlockerKindV1
DECISION_BLOCKER_KIND_V1_MIN_COVERAGE_NOT_MET: DecisionBlockerKindV1
DECISION_BLOCKER_KIND_V1_EVIDENCE_INCOMPLETE: DecisionBlockerKindV1
DECISION_BLOCKER_KIND_V1_NOT_COMPARABLE: DecisionBlockerKindV1
EVALUATION_MATRIX_SORT_KEY_V1_UNSPECIFIED: EvaluationMatrixSortKeyV1
EVALUATION_MATRIX_SORT_KEY_V1_DECISION_IMPACT: EvaluationMatrixSortKeyV1
EVALUATION_MATRIX_SORT_KEY_V1_CASE_ORDER: EvaluationMatrixSortKeyV1
EVALUATION_MATRIX_DECISION_IMPACT_V1_UNSPECIFIED: EvaluationMatrixDecisionImpactV1
EVALUATION_MATRIX_DECISION_IMPACT_V1_REGRESSED: EvaluationMatrixDecisionImpactV1
EVALUATION_MATRIX_DECISION_IMPACT_V1_IMPROVED: EvaluationMatrixDecisionImpactV1
EVALUATION_MATRIX_DECISION_IMPACT_V1_UNCHANGED: EvaluationMatrixDecisionImpactV1
EVALUATION_MATRIX_DECISION_IMPACT_V1_DISAGREEMENT: EvaluationMatrixDecisionImpactV1
EVALUATION_MATRIX_DECISION_IMPACT_V1_MISSING_EVIDENCE: EvaluationMatrixDecisionImpactV1
EVALUATION_MATRIX_EVIDENCE_STATE_V1_UNSPECIFIED: EvaluationMatrixEvidenceStateV1
EVALUATION_MATRIX_EVIDENCE_STATE_V1_COMPLETE: EvaluationMatrixEvidenceStateV1
EVALUATION_MATRIX_EVIDENCE_STATE_V1_PARTIAL: EvaluationMatrixEvidenceStateV1
EVALUATION_MATRIX_EVIDENCE_STATE_V1_CANDIDATE_FAILED: EvaluationMatrixEvidenceStateV1
EVALUATION_MATRIX_EVIDENCE_STATE_V1_SCORER_FAILED: EvaluationMatrixEvidenceStateV1
EVALUATION_MATRIX_EVIDENCE_STATE_V1_AWAITING_REVIEW: EvaluationMatrixEvidenceStateV1
EVALUATION_MATRIX_EVIDENCE_STATE_V1_NOT_SAMPLED: EvaluationMatrixEvidenceStateV1
EVALUATION_MATRIX_EVIDENCE_STATE_V1_SUPERSEDED: EvaluationMatrixEvidenceStateV1
EVALUATION_MATRIX_FACET_KIND_V1_UNSPECIFIED: EvaluationMatrixFacetKindV1
EVALUATION_MATRIX_FACET_KIND_V1_REGRESSIONS: EvaluationMatrixFacetKindV1
EVALUATION_MATRIX_FACET_KIND_V1_IMPROVEMENTS: EvaluationMatrixFacetKindV1
EVALUATION_MATRIX_FACET_KIND_V1_DISAGREEMENTS: EvaluationMatrixFacetKindV1
EVALUATION_MATRIX_FACET_KIND_V1_MISSING_EVIDENCE: EvaluationMatrixFacetKindV1
EVALUATION_MATRIX_FACET_KIND_V1_CANDIDATE_FAILURES: EvaluationMatrixFacetKindV1
EVALUATION_MATRIX_FACET_KIND_V1_SCORER_FAILURES: EvaluationMatrixFacetKindV1
EVALUATION_MATRIX_FACET_KIND_V1_AWAITING_REVIEW: EvaluationMatrixFacetKindV1
EVALUATION_MATRIX_FACET_KIND_V1_UNCHANGED: EvaluationMatrixFacetKindV1
EVALUATION_CELL_EVIDENCE_SOURCE_V1_UNSPECIFIED: EvaluationCellEvidenceSourceV1
EVALUATION_CELL_EVIDENCE_SOURCE_V1_POSTGRES_PROJECTION: EvaluationCellEvidenceSourceV1
EVALUATION_CELL_EVIDENCE_SOURCE_V1_FACT_PLANE_LOCATOR: EvaluationCellEvidenceSourceV1
EVALUATION_SCORER_ATTEMPT_ORIGIN_V1_UNSPECIFIED: EvaluationScorerAttemptOriginV1
EVALUATION_SCORER_ATTEMPT_ORIGIN_V1_EXECUTION: EvaluationScorerAttemptOriginV1
EVALUATION_SCORER_ATTEMPT_ORIGIN_V1_SCORER_RETRY: EvaluationScorerAttemptOriginV1
EVALUATION_SCORER_ATTEMPT_ORIGIN_V1_HUMAN_REVIEW: EvaluationScorerAttemptOriginV1
EVALUATION_SCORER_ATTEMPT_ORIGIN_V1_ADJUDICATION: EvaluationScorerAttemptOriginV1
EVALUATION_SCORER_ATTEMPT_ORIGIN_V1_JUDGE_REGRADE: EvaluationScorerAttemptOriginV1
EVALUATION_RUN_CHANGE_KIND_V1_UNSPECIFIED: EvaluationRunChangeKindV1
EVALUATION_RUN_CHANGE_KIND_V1_PROGRESS: EvaluationRunChangeKindV1
EVALUATION_RUN_CHANGE_KIND_V1_CELL_BATCH: EvaluationRunChangeKindV1
EVALUATION_RUN_CHANGE_KIND_V1_SECTION_REFRESHED: EvaluationRunChangeKindV1
EVALUATION_RUN_CHANGE_KIND_V1_DECISION_REVISION: EvaluationRunChangeKindV1
EVALUATION_RUN_CHANGE_KIND_V1_TERMINAL: EvaluationRunChangeKindV1
EVALUATION_RUN_CHANGE_KIND_V1_RESYNC_REQUIRED: EvaluationRunChangeKindV1
EVALUATION_RUN_CHANGE_KIND_V1_REPLAY_GAP: EvaluationRunChangeKindV1
EVALUATION_ARTIFACT_CONTENT_STATE_V1_UNSPECIFIED: EvaluationArtifactContentStateV1
EVALUATION_ARTIFACT_CONTENT_STATE_V1_SERVED: EvaluationArtifactContentStateV1
EVALUATION_ARTIFACT_CONTENT_STATE_V1_UNAUTHORIZED: EvaluationArtifactContentStateV1
EVALUATION_ARTIFACT_CONTENT_STATE_V1_REVOKED: EvaluationArtifactContentStateV1
EVALUATION_ARTIFACT_CONTENT_STATE_V1_REDACTED: EvaluationArtifactContentStateV1
EVALUATION_ARTIFACT_CONTENT_STATE_V1_NOT_FOUND: EvaluationArtifactContentStateV1
EVALUATION_ARTIFACT_CONTENT_STATE_V1_PLANE_NOT_SHIPPED: EvaluationArtifactContentStateV1
EVALUATION_ARTIFACT_CONTENT_STATE_V1_BYTE_BUDGET_EXCEEDED: EvaluationArtifactContentStateV1
EVALUATION_ARTIFACT_REMEDIATION_KIND_V1_UNSPECIFIED: EvaluationArtifactRemediationKindV1
EVALUATION_ARTIFACT_REMEDIATION_KIND_V1_NONE: EvaluationArtifactRemediationKindV1
EVALUATION_ARTIFACT_REMEDIATION_KIND_V1_REQUEST_ACCESS: EvaluationArtifactRemediationKindV1
EVALUATION_ARTIFACT_REMEDIATION_KIND_V1_CONTACT_OWNER: EvaluationArtifactRemediationKindV1
EVALUATION_ARTIFACT_REMEDIATION_KIND_V1_RETRY_NARROWER_BATCH: EvaluationArtifactRemediationKindV1
EVALUATION_ARTIFACT_REMEDIATION_KIND_V1_WAIT_FOR_PLANE: EvaluationArtifactRemediationKindV1
CONFIGURATION_DIMENSION_V1_UNSPECIFIED: ConfigurationDimensionV1
CONFIGURATION_DIMENSION_V1_CANDIDATE_RELEASE_REVISION: ConfigurationDimensionV1
CONFIGURATION_DIMENSION_V1_PROVIDER_MODEL: ConfigurationDimensionV1
CONFIGURATION_DIMENSION_V1_RESPONSE_MODEL: ConfigurationDimensionV1
CONFIGURATION_DIMENSION_V1_PROMPT: ConfigurationDimensionV1
CONFIGURATION_DIMENSION_V1_GENERATION_PARAMS: ConfigurationDimensionV1
CONFIGURATION_DIMENSION_V1_TOOL_CATALOG: ConfigurationDimensionV1
CONFIGURATION_DIMENSION_V1_TOOL_VERSION: ConfigurationDimensionV1
CONFIGURATION_DIMENSION_V1_RETRIEVAL_BACKEND: ConfigurationDimensionV1
CONFIGURATION_DIMENSION_V1_RETRIEVAL_CONFIG: ConfigurationDimensionV1
CONFIGURATION_DIMENSION_V1_FEATURE_FLAG: ConfigurationDimensionV1
CONFIGURATION_DIMENSION_V1_DEPLOYMENT: ConfigurationDimensionV1
CONFIGURATION_DIMENSION_V1_ENVIRONMENT: ConfigurationDimensionV1
CONFIGURATION_DIMENSION_V1_SCORER: ConfigurationDimensionV1
CONFIGURATION_DIMENSION_V1_RUBRIC: ConfigurationDimensionV1
CONFIGURATION_DIMENSION_V1_DECISION_POLICY: ConfigurationDimensionV1
CONFIGURATION_DIMENSION_V1_DATASET: ConfigurationDimensionV1
CONFIGURATION_DIMENSION_V1_COHORT: ConfigurationDimensionV1
CONFIGURATION_DIMENSION_V1_SCHEMA: ConfigurationDimensionV1
CONFIGURATION_DIMENSION_V1_NORMALIZATION: ConfigurationDimensionV1
CONFIGURATION_DIMENSION_V1_TRIALS: ConfigurationDimensionV1
EVALUATION_AUDIT_EVENT_KIND_V1_UNSPECIFIED: EvaluationAuditEventKindV1
EVALUATION_AUDIT_EVENT_KIND_V1_RUN_LAUNCHED: EvaluationAuditEventKindV1
EVALUATION_AUDIT_EVENT_KIND_V1_RUN_STATE_CHANGED: EvaluationAuditEventKindV1
EVALUATION_AUDIT_EVENT_KIND_V1_CELLS_RETRIED: EvaluationAuditEventKindV1
EVALUATION_AUDIT_EVENT_KIND_V1_RUN_CANCELLED: EvaluationAuditEventKindV1
EVALUATION_AUDIT_EVENT_KIND_V1_DECISION_ADOPTED: EvaluationAuditEventKindV1
EVALUATION_AUDIT_EVENT_KIND_V1_REVIEW_SUBMITTED: EvaluationAuditEventKindV1
EVALUATION_AUDIT_EVENT_KIND_V1_EXPORT_REQUESTED: EvaluationAuditEventKindV1
EVALUATION_AUDIT_EVENT_KIND_V1_SHARE_CREATED: EvaluationAuditEventKindV1
EVALUATION_REVIEW_TASK_STATE_V1_UNSPECIFIED: EvaluationReviewTaskStateV1
EVALUATION_REVIEW_TASK_STATE_V1_PENDING: EvaluationReviewTaskStateV1
EVALUATION_REVIEW_TASK_STATE_V1_ASSIGNED: EvaluationReviewTaskStateV1
EVALUATION_REVIEW_TASK_STATE_V1_RESERVED: EvaluationReviewTaskStateV1
EVALUATION_REVIEW_TASK_STATE_V1_SUBMITTED: EvaluationReviewTaskStateV1
EVALUATION_REVIEW_TASK_STATE_V1_RESERVATION_EXPIRED: EvaluationReviewTaskStateV1
EVALUATION_REVIEW_TASK_STATE_V1_RELEASED: EvaluationReviewTaskStateV1
EVALUATION_REVIEW_TASK_STATE_V1_CANCELLED: EvaluationReviewTaskStateV1
EVALUATION_REVIEW_TASK_STATE_V1_WAIVED: EvaluationReviewTaskStateV1
REVIEW_RESERVATION_STATE_V1_UNSPECIFIED: ReviewReservationStateV1
REVIEW_RESERVATION_STATE_V1_NONE: ReviewReservationStateV1
REVIEW_RESERVATION_STATE_V1_ACTIVE: ReviewReservationStateV1
REVIEW_RESERVATION_STATE_V1_EXPIRING: ReviewReservationStateV1
REVIEW_RESERVATION_STATE_V1_EXPIRED: ReviewReservationStateV1
REVIEW_RESERVATION_STATE_V1_RELEASED: ReviewReservationStateV1
REVIEW_RESERVATION_STATE_V1_TRANSFERRED: ReviewReservationStateV1
REVIEW_UNIT_COMPLETION_STATE_V1_UNSPECIFIED: ReviewUnitCompletionStateV1
REVIEW_UNIT_COMPLETION_STATE_V1_AWAITING_REVIEWERS: ReviewUnitCompletionStateV1
REVIEW_UNIT_COMPLETION_STATE_V1_AWAITING_ADJUDICATION: ReviewUnitCompletionStateV1
REVIEW_UNIT_COMPLETION_STATE_V1_COMPLETE: ReviewUnitCompletionStateV1
REVIEW_UNIT_COMPLETION_STATE_V1_WAIVED: ReviewUnitCompletionStateV1
REVIEW_UNIT_COMPLETION_STATE_V1_INCOMPLETE_EXPIRED: ReviewUnitCompletionStateV1
REVIEW_ADJUDICATION_STATE_V1_UNSPECIFIED: ReviewAdjudicationStateV1
REVIEW_ADJUDICATION_STATE_V1_NOT_REQUIRED: ReviewAdjudicationStateV1
REVIEW_ADJUDICATION_STATE_V1_REQUIRED: ReviewAdjudicationStateV1
REVIEW_ADJUDICATION_STATE_V1_ASSIGNED: ReviewAdjudicationStateV1
REVIEW_ADJUDICATION_STATE_V1_RESOLVED: ReviewAdjudicationStateV1
REVIEW_ADJUDICATION_STATE_V1_UNRESOLVABLE: ReviewAdjudicationStateV1
EVALUATION_EXPORT_FORMAT_V1_UNSPECIFIED: EvaluationExportFormatV1
EVALUATION_EXPORT_FORMAT_V1_CSV: EvaluationExportFormatV1
EVALUATION_EXPORT_FORMAT_V1_JSONL: EvaluationExportFormatV1
EVALUATION_EXPORT_FORMAT_V1_PARQUET: EvaluationExportFormatV1
EVALUATION_SHARE_STATE_V1_UNSPECIFIED: EvaluationShareStateV1
EVALUATION_SHARE_STATE_V1_ACTIVE: EvaluationShareStateV1
EVALUATION_SHARE_STATE_V1_REVOKED: EvaluationShareStateV1
EVALUATION_WORK_OPERATION_KIND_V1_UNSPECIFIED: EvaluationWorkOperationKindV1
EVALUATION_WORK_OPERATION_KIND_V1_CANDIDATE_CALL: EvaluationWorkOperationKindV1
EVALUATION_WORK_OPERATION_KIND_V1_SCORER_EXECUTION: EvaluationWorkOperationKindV1
EVALUATION_WORK_OPERATION_KIND_V1_RUN_PREPARATION: EvaluationWorkOperationKindV1
EVALUATION_OPERATION_DIMENSION_V1_UNSPECIFIED: EvaluationOperationDimensionV1
EVALUATION_OPERATION_DIMENSION_V1_HOST: EvaluationOperationDimensionV1
EVALUATION_OPERATION_DIMENSION_V1_SERVICE: EvaluationOperationDimensionV1
EVALUATION_OPERATION_DIMENSION_V1_CONTAINER: EvaluationOperationDimensionV1
EVALUATION_OPERATION_DIMENSION_V1_NODE: EvaluationOperationDimensionV1
EVALUATION_OPERATION_DIMENSION_V1_REGION: EvaluationOperationDimensionV1
EVALUATION_OPERATION_DIMENSION_V1_TIME_BUCKET: EvaluationOperationDimensionV1
EVALUATION_OPERATION_DIMENSION_V1_TELEMETRY_SPAN: EvaluationOperationDimensionV1
EVALUATION_OPERATION_CACHE_EXPLANATION_V1_UNSPECIFIED: EvaluationOperationCacheExplanationV1
EVALUATION_OPERATION_CACHE_EXPLANATION_V1_NOT_REPORTED: EvaluationOperationCacheExplanationV1
EVALUATION_OPERATION_CACHE_EXPLANATION_V1_NO_CACHE_ACTIVITY: EvaluationOperationCacheExplanationV1
EVALUATION_OPERATION_CACHE_EXPLANATION_V1_CACHE_READS_OBSERVED: EvaluationOperationCacheExplanationV1
EVALUATION_OPERATION_CACHE_EXPLANATION_V1_CACHE_WRITES_OBSERVED: EvaluationOperationCacheExplanationV1
EVALUATION_OPERATION_CACHE_EXPLANATION_V1_NOT_APPLICABLE: EvaluationOperationCacheExplanationV1
EVALUATION_ADJUDICATION_REFUSAL_V1_UNSPECIFIED: EvaluationAdjudicationRefusalV1
EVALUATION_ADJUDICATION_REFUSAL_V1_NOT_AN_ADJUDICATOR: EvaluationAdjudicationRefusalV1
EVALUATION_ADJUDICATION_REFUSAL_V1_NO_CONFLICT_TO_ADJUDICATE: EvaluationAdjudicationRefusalV1
EVALUATION_ADJUDICATION_REFUSAL_V1_UNIT_ALREADY_COMPLETE: EvaluationAdjudicationRefusalV1
EVALUATION_ADJUDICATION_REFUSAL_V1_UNIT_NOT_FOUND: EvaluationAdjudicationRefusalV1
EVALUATION_ORG_NEGOTIATED_RATE_STATE_V1_UNSPECIFIED: EvaluationOrgNegotiatedRateStateV1
EVALUATION_ORG_NEGOTIATED_RATE_STATE_V1_SCHEDULED: EvaluationOrgNegotiatedRateStateV1
EVALUATION_ORG_NEGOTIATED_RATE_STATE_V1_IN_FORCE: EvaluationOrgNegotiatedRateStateV1
EVALUATION_ORG_NEGOTIATED_RATE_STATE_V1_ENDED: EvaluationOrgNegotiatedRateStateV1
EVALUATION_ORG_NEGOTIATED_RATE_STATE_V1_VOIDED: EvaluationOrgNegotiatedRateStateV1
EVALUATION_SERIES_GRAIN_V1_UNSPECIFIED: EvaluationSeriesGrainV1
EVALUATION_SERIES_GRAIN_V1_DEFINITION: EvaluationSeriesGrainV1
EVALUATION_SERIES_GRAIN_V1_CANDIDATE: EvaluationSeriesGrainV1
EVALUATION_SERIES_GRAIN_V1_SCORER: EvaluationSeriesGrainV1
EVALUATION_SERIES_GRAIN_V1_CANDIDATE_SCORER: EvaluationSeriesGrainV1
EVALUATION_SERIES_GRAIN_V1_COHORT: EvaluationSeriesGrainV1
EVALUATION_SERIES_GRAIN_V1_PRODUCTION_RULE: EvaluationSeriesGrainV1
EVALUATION_SERIES_PLANE_V1_UNSPECIFIED: EvaluationSeriesPlaneV1
EVALUATION_SERIES_PLANE_V1_PROJECTION: EvaluationSeriesPlaneV1
EVALUATION_SERIES_PLANE_V1_FACTS: EvaluationSeriesPlaneV1
EVALUATION_CAPTURE_SOURCE_KIND_V1_UNSPECIFIED: EvaluationCaptureSourceKindV1
EVALUATION_CAPTURE_SOURCE_KIND_V1_TRACE_SPAN: EvaluationCaptureSourceKindV1
EVALUATION_CAPTURE_SOURCE_KIND_V1_EVALUATION_MATRIX_CELL: EvaluationCaptureSourceKindV1
EVALUATION_CAPTURE_SOURCE_KIND_V1_PRODUCTION_RULE: EvaluationCaptureSourceKindV1
EVALUATION_CAPTURE_SOURCE_KIND_V1_MANUAL: EvaluationCaptureSourceKindV1
EVALUATION_CAPTURE_SOURCE_KIND_V1_IMPORT: EvaluationCaptureSourceKindV1
EVALUATION_CAPTURE_SOURCE_KIND_V1_MACHINE_PRINCIPAL: EvaluationCaptureSourceKindV1
EVALUATION_CAPTURE_REFUSAL_KIND_V1_UNSPECIFIED: EvaluationCaptureRefusalKindV1
EVALUATION_CAPTURE_REFUSAL_KIND_V1_SOURCE_NOT_FOUND: EvaluationCaptureRefusalKindV1
EVALUATION_CAPTURE_REFUSAL_KIND_V1_SOURCE_PLANE_NOT_SHIPPED: EvaluationCaptureRefusalKindV1
EVALUATION_CAPTURE_REFUSAL_KIND_V1_REQUIRED_FIELD_UNMAPPED: EvaluationCaptureRefusalKindV1
EVALUATION_CAPTURE_REFUSAL_KIND_V1_MAPPING_RESOLVED_NOTHING: EvaluationCaptureRefusalKindV1
EVALUATION_CAPTURE_REFUSAL_KIND_V1_INVALID_TARGET_PATH: EvaluationCaptureRefusalKindV1
EVALUATION_CAPTURE_REFUSAL_KIND_V1_IDEMPOTENCY_KEY_REUSED: EvaluationCaptureRefusalKindV1
EVALUATION_CAPTURE_REFUSAL_KIND_V1_DRAFT_CASE_CAP_EXCEEDED: EvaluationCaptureRefusalKindV1
EVALUATION_CAPTURE_REFUSAL_KIND_V1_PREVIEW_DIGEST_MOVED: EvaluationCaptureRefusalKindV1
EVALUATION_CAPTURE_REFUSAL_KIND_V1_SPAN_CONTENT_BUDGET_EXCEEDED: EvaluationCaptureRefusalKindV1
EVALUATION_CAPTURE_REFUSAL_KIND_V1_PROMOTION_KEY_EXISTS: EvaluationCaptureRefusalKindV1
EVALUATION_CAPTURE_REFUSAL_KIND_V1_REDACTION_BLOCKED: EvaluationCaptureRefusalKindV1
EVALUATION_CAPTURE_REFUSAL_KIND_V1_REDACTION_INDETERMINATE: EvaluationCaptureRefusalKindV1
EVALUATION_DATASET_DRAFT_STATE_V1_UNSPECIFIED: EvaluationDatasetDraftStateV1
EVALUATION_DATASET_DRAFT_STATE_V1_OPEN: EvaluationDatasetDraftStateV1
EVALUATION_DATASET_DRAFT_STATE_V1_FINALIZED: EvaluationDatasetDraftStateV1
EVALUATION_DATASET_DRAFT_STATE_V1_ABANDONED: EvaluationDatasetDraftStateV1
EVALUATION_PROPOSED_CASE_STATE_V1_UNSPECIFIED: EvaluationProposedCaseStateV1
EVALUATION_PROPOSED_CASE_STATE_V1_PROPOSED: EvaluationProposedCaseStateV1
EVALUATION_PROPOSED_CASE_STATE_V1_VOIDED: EvaluationProposedCaseStateV1
EVALUATION_SPAN_CONTENT_CLASS_V1_UNSPECIFIED: EvaluationSpanContentClassV1
EVALUATION_SPAN_CONTENT_CLASS_V1_INPUT_MESSAGES: EvaluationSpanContentClassV1
EVALUATION_SPAN_CONTENT_CLASS_V1_OUTPUT_MESSAGES: EvaluationSpanContentClassV1
EVALUATION_SPAN_CONTENT_CLASS_V1_TOOL_DEFINITIONS: EvaluationSpanContentClassV1
EVALUATION_SPAN_CONTENT_CLASS_V1_SYSTEM_INSTRUCTIONS: EvaluationSpanContentClassV1
EVALUATION_SPAN_CONTENT_CLASS_V1_RETRIEVAL_DOCUMENTS: EvaluationSpanContentClassV1
EVALUATION_SPAN_CONTENT_CLASS_V1_TOOL_ARGUMENTS: EvaluationSpanContentClassV1
EVALUATION_SPAN_CONTENT_CLASS_V1_TOOL_RESULT: EvaluationSpanContentClassV1
EVALUATION_SPAN_CONTENT_CLASS_V1_REASONING: EvaluationSpanContentClassV1
EVALUATION_PROVIDER_CREDENTIAL_REJECTION_KIND_V1_UNSPECIFIED: EvaluationProviderCredentialRejectionKindV1
EVALUATION_PROVIDER_CREDENTIAL_REJECTION_KIND_V1_CAP_EXCEEDED: EvaluationProviderCredentialRejectionKindV1
EVALUATION_PROVIDER_CREDENTIAL_REJECTION_KIND_V1_DUPLICATE_KEY_NAME: EvaluationProviderCredentialRejectionKindV1
EVALUATION_PROVIDER_CREDENTIAL_REJECTION_KIND_V1_INVALID_PROVIDER: EvaluationProviderCredentialRejectionKindV1
EVALUATION_SCORER_KIND_V1_UNSPECIFIED: EvaluationScorerKindV1
EVALUATION_SCORER_KIND_V1_DETERMINISTIC: EvaluationScorerKindV1
EVALUATION_SCORER_KIND_V1_HUMAN: EvaluationScorerKindV1
EVALUATION_SCORER_KIND_V1_LLM_JUDGE: EvaluationScorerKindV1
EVALUATION_SCORER_EVALUATOR_V1_UNSPECIFIED: EvaluationScorerEvaluatorV1
EVALUATION_SCORER_EVALUATOR_V1_EXACT: EvaluationScorerEvaluatorV1
EVALUATION_SCORER_EVALUATOR_V1_NUMERIC_THRESHOLD: EvaluationScorerEvaluatorV1
EVALUATION_SCORER_EVALUATOR_V1_PATTERN: EvaluationScorerEvaluatorV1
EVALUATION_SCORER_CONFIG_REJECTION_KIND_V1_UNSPECIFIED: EvaluationScorerConfigRejectionKindV1
EVALUATION_SCORER_CONFIG_REJECTION_KIND_V1_DUPLICATE_CONFIG_KEY: EvaluationScorerConfigRejectionKindV1
EVALUATION_SCORER_CONFIG_REJECTION_KIND_V1_PINNED_BY_RUN: EvaluationScorerConfigRejectionKindV1
EVALUATION_SCORER_CONFIG_REJECTION_KIND_V1_KIND_SPEC_MISMATCH: EvaluationScorerConfigRejectionKindV1
EVALUATION_SCORER_CONFIG_REJECTION_KIND_V1_EVALUATOR_NOT_RETAINED: EvaluationScorerConfigRejectionKindV1
EVALUATION_SCORER_CONFIG_REJECTION_KIND_V1_REVIEW_POLICY_UNSATISFIABLE: EvaluationScorerConfigRejectionKindV1
EVALUATION_SCORER_CONFIG_REJECTION_KIND_V1_JUDGE_SPEC_INVALID: EvaluationScorerConfigRejectionKindV1
EVALUATION_SCORER_CONFIG_REJECTION_KIND_V1_JUDGE_PROVIDER_NOT_AVAILABLE: EvaluationScorerConfigRejectionKindV1
EVALUATION_SCORER_CONFIG_REJECTION_KIND_V1_JUDGE_TEMPLATE_MOVED: EvaluationScorerConfigRejectionKindV1
EVALUATION_DATASET_VERSION_REJECTION_KIND_V1_UNSPECIFIED: EvaluationDatasetVersionRejectionKindV1
EVALUATION_DATASET_VERSION_REJECTION_KIND_V1_COLLECTION_CAP_EXCEEDED: EvaluationDatasetVersionRejectionKindV1
EVALUATION_DATASET_VERSION_REJECTION_KIND_V1_VERSION_CAP_ALL_PINNED: EvaluationDatasetVersionRejectionKindV1
EVALUATION_DATASET_VERSION_REJECTION_KIND_V1_MALFORMED_JSONL_LINE: EvaluationDatasetVersionRejectionKindV1
EVALUATION_DATASET_VERSION_REJECTION_KIND_V1_EMPTY_INGEST: EvaluationDatasetVersionRejectionKindV1
EVALUATION_DATASET_VERSION_REJECTION_KIND_V1_INGEST_TOO_LARGE: EvaluationDatasetVersionRejectionKindV1
EVALUATION_DATASET_VERSION_REJECTION_KIND_V1_DRAFT_NOT_FINALIZABLE: EvaluationDatasetVersionRejectionKindV1
EVALUATION_DATASET_VERSION_REJECTION_KIND_V1_INGEST_BYTES_EXCEEDED: EvaluationDatasetVersionRejectionKindV1
EVALUATION_DATASET_VERSION_REJECTION_KIND_V1_INGEST_CASE_COUNT_EXCEEDED: EvaluationDatasetVersionRejectionKindV1
EVALUATION_DATASET_VERSION_REJECTION_KIND_V1_DRAFT_HAS_UNAPPROVED_CASES: EvaluationDatasetVersionRejectionKindV1
EVALUATION_SCORER_SUITE_REJECTION_KIND_V1_UNSPECIFIED: EvaluationScorerSuiteRejectionKindV1
EVALUATION_SCORER_SUITE_REJECTION_KIND_V1_DUPLICATE_SUITE_KEY: EvaluationScorerSuiteRejectionKindV1
EVALUATION_SCORER_SUITE_REJECTION_KIND_V1_MEMBER_NOT_FOUND: EvaluationScorerSuiteRejectionKindV1
EVALUATION_SCORER_SUITE_REJECTION_KIND_V1_EMPTY_MEMBERSHIP: EvaluationScorerSuiteRejectionKindV1
EVALUATION_SCORER_SUITE_REJECTION_KIND_V1_DUPLICATE_MEMBER: EvaluationScorerSuiteRejectionKindV1
EVALUATION_SCORER_SUITE_REJECTION_KIND_V1_MEMBER_CAP_EXCEEDED: EvaluationScorerSuiteRejectionKindV1
EVALUATION_SCORER_SUITE_REJECTION_KIND_V1_COMBINE_RULE_NOT_SUPPORTED: EvaluationScorerSuiteRejectionKindV1
EVALUATION_SCORER_SUITE_REJECTION_KIND_V1_MEMBER_NOT_SCOREABLE: EvaluationScorerSuiteRejectionKindV1
EVALUATION_SCORER_SUITE_REJECTION_KIND_V1_MEMBER_WEIGHT_UNUSABLE: EvaluationScorerSuiteRejectionKindV1
EVALUATION_JUDGE_REGRADE_JOB_STATE_V1_UNSPECIFIED: EvaluationJudgeRegradeJobStateV1
EVALUATION_JUDGE_REGRADE_JOB_STATE_V1_QUEUED: EvaluationJudgeRegradeJobStateV1
EVALUATION_JUDGE_REGRADE_JOB_STATE_V1_RUNNING: EvaluationJudgeRegradeJobStateV1
EVALUATION_JUDGE_REGRADE_JOB_STATE_V1_COMPLETED: EvaluationJudgeRegradeJobStateV1
EVALUATION_JUDGE_REGRADE_JOB_STATE_V1_FAILED: EvaluationJudgeRegradeJobStateV1
EVALUATION_JUDGE_REGRADE_JOB_STATE_V1_CANCELLED: EvaluationJudgeRegradeJobStateV1
EVALUATION_JUDGE_REGRADE_CELL_STATE_V1_UNSPECIFIED: EvaluationJudgeRegradeCellStateV1
EVALUATION_JUDGE_REGRADE_CELL_STATE_V1_QUEUED: EvaluationJudgeRegradeCellStateV1
EVALUATION_JUDGE_REGRADE_CELL_STATE_V1_LEASED: EvaluationJudgeRegradeCellStateV1
EVALUATION_JUDGE_REGRADE_CELL_STATE_V1_SUCCEEDED: EvaluationJudgeRegradeCellStateV1
EVALUATION_JUDGE_REGRADE_CELL_STATE_V1_FAILED: EvaluationJudgeRegradeCellStateV1
EVALUATION_JUDGE_REGRADE_CELL_STATE_V1_CANCELLED: EvaluationJudgeRegradeCellStateV1
EVALUATION_JUDGE_REGRADE_INELIGIBILITY_V1_UNSPECIFIED: EvaluationJudgeRegradeIneligibilityV1
EVALUATION_JUDGE_REGRADE_INELIGIBILITY_V1_CANDIDATE_OUTPUT_ABSENT: EvaluationJudgeRegradeIneligibilityV1
EVALUATION_JUDGE_REGRADE_INELIGIBILITY_V1_SCORER_NOT_A_JUDGE: EvaluationJudgeRegradeIneligibilityV1
EVALUATION_JUDGE_REGRADE_INELIGIBILITY_V1_SCORER_REQUIRES_HUMAN: EvaluationJudgeRegradeIneligibilityV1
EVALUATION_JUDGE_REGRADE_INELIGIBILITY_V1_ATTEMPT_CEILING_REACHED: EvaluationJudgeRegradeIneligibilityV1
EVALUATION_JUDGE_REGRADE_INELIGIBILITY_V1_COORDINATE_UNKNOWN: EvaluationJudgeRegradeIneligibilityV1
EVALUATION_JUDGE_REGRADE_INELIGIBILITY_V1_PROVIDER_UNCONFIGURED: EvaluationJudgeRegradeIneligibilityV1
EVALUATION_JUDGE_REGRADE_INELIGIBILITY_V1_COORDINATE_ALREADY_QUEUED: EvaluationJudgeRegradeIneligibilityV1
EVALUATION_JUDGE_REGRADE_INELIGIBILITY_V1_SCORER_IS_A_DERIVED_SUITE: EvaluationJudgeRegradeIneligibilityV1
EVALUATION_JUDGE_REGRADE_RATE_COMPARISON_V1_UNSPECIFIED: EvaluationJudgeRegradeRateComparisonV1
EVALUATION_JUDGE_REGRADE_RATE_COMPARISON_V1_UNCHANGED: EvaluationJudgeRegradeRateComparisonV1
EVALUATION_JUDGE_REGRADE_RATE_COMPARISON_V1_MOVED: EvaluationJudgeRegradeRateComparisonV1
EVALUATION_JUDGE_REGRADE_RATE_COMPARISON_V1_PIN_CARRIES_NO_RATE: EvaluationJudgeRegradeRateComparisonV1
EVALUATION_JUDGE_REGRADE_RATE_COMPARISON_V1_REGISTRY_HAS_NO_ROW: EvaluationJudgeRegradeRateComparisonV1
EVALUATION_REVIEW_REQUEUE_REASON_V1_UNSPECIFIED: EvaluationReviewRequeueReasonV1
EVALUATION_REVIEW_REQUEUE_REASON_V1_REVIEWER_UNAVAILABLE: EvaluationReviewRequeueReasonV1
EVALUATION_REVIEW_REQUEUE_REASON_V1_AMBIGUOUS_GUIDANCE: EvaluationReviewRequeueReasonV1
EVALUATION_REVIEW_REQUEUE_REASON_V1_WRONG_REVIEWER_POOL: EvaluationReviewRequeueReasonV1
EVALUATION_REVIEW_REQUEUE_REASON_V1_CONTENT_UNREADABLE: EvaluationReviewRequeueReasonV1
EVALUATION_REVIEW_REQUEUE_REASON_V1_OPERATOR_REBALANCE: EvaluationReviewRequeueReasonV1
EVALUATION_REVIEW_TASK_REFUSAL_KIND_V1_UNSPECIFIED: EvaluationReviewTaskRefusalKindV1
EVALUATION_REVIEW_TASK_REFUSAL_KIND_V1_NOT_HELD_BY_CALLER: EvaluationReviewTaskRefusalKindV1
EVALUATION_REVIEW_TASK_REFUSAL_KIND_V1_TASK_NOT_FOUND: EvaluationReviewTaskRefusalKindV1
EVALUATION_REVIEW_TASK_REFUSAL_KIND_V1_ALREADY_SUBMITTED: EvaluationReviewTaskRefusalKindV1
EVALUATION_REVIEW_TASK_REFUSAL_KIND_V1_STILL_RESERVED: EvaluationReviewTaskRefusalKindV1
EVALUATION_REVIEW_TASK_REFUSAL_KIND_V1_BATCH_TOO_LARGE: EvaluationReviewTaskRefusalKindV1
EVALUATION_REVIEW_TASK_REFUSAL_KIND_V1_UNIT_NO_LONGER_OPEN: EvaluationReviewTaskRefusalKindV1
PRODUCTION_RULE_VERSION_STATE_V1_UNSPECIFIED: ProductionRuleVersionStateV1
PRODUCTION_RULE_VERSION_STATE_V1_DRAFT: ProductionRuleVersionStateV1
PRODUCTION_RULE_VERSION_STATE_V1_ACTIVE: ProductionRuleVersionStateV1
PRODUCTION_RULE_VERSION_STATE_V1_PAUSED: ProductionRuleVersionStateV1
PRODUCTION_RULE_VERSION_STATE_V1_SUPERSEDED: ProductionRuleVersionStateV1
PRODUCTION_RULE_VERSION_STATE_V1_DISABLED: ProductionRuleVersionStateV1
PRODUCTION_RULE_VERSION_STATE_V1_ARCHIVED: ProductionRuleVersionStateV1
PRODUCTION_RULE_ACTION_KIND_V1_UNSPECIFIED: ProductionRuleActionKindV1
PRODUCTION_RULE_ACTION_KIND_V1_SCORE: ProductionRuleActionKindV1
PRODUCTION_RULE_ACTION_KIND_V1_CREATE_DATASET_DRAFT: ProductionRuleActionKindV1
PRODUCTION_RULE_ACTION_KIND_V1_REQUEST_REVIEW: ProductionRuleActionKindV1
PRODUCTION_RULE_ACTION_KIND_V1_RUN_LINKED_EVALUATION: ProductionRuleActionKindV1
PRODUCTION_RULE_ACTION_KIND_V1_NOTIFY: ProductionRuleActionKindV1
PRODUCTION_RULE_ACTION_KIND_V1_BLOCK_RELEASE: ProductionRuleActionKindV1
PRODUCTION_RULE_HEALTH_STATE_V1_UNSPECIFIED: ProductionRuleHealthStateV1
PRODUCTION_RULE_HEALTH_STATE_V1_ENABLED: ProductionRuleHealthStateV1
PRODUCTION_RULE_HEALTH_STATE_V1_PAUSED: ProductionRuleHealthStateV1
PRODUCTION_RULE_HEALTH_STATE_V1_DEGRADED: ProductionRuleHealthStateV1
PRODUCTION_RULE_HEALTH_STATE_V1_FAILING: ProductionRuleHealthStateV1
PRODUCTION_RULE_HEALTH_STATE_V1_INDETERMINATE: ProductionRuleHealthStateV1
PRODUCTION_RULE_RUNTIME_SCOPE_V1_UNSPECIFIED: ProductionRuleRuntimeScopeV1
PRODUCTION_RULE_RUNTIME_SCOPE_V1_AGENT_RUN: ProductionRuleRuntimeScopeV1
PRODUCTION_RULE_RUNTIME_SCOPE_V1_SPAN: ProductionRuleRuntimeScopeV1
PRODUCTION_RULE_ACTION_CONDITION_KIND_V1_UNSPECIFIED: ProductionRuleActionConditionKindV1
PRODUCTION_RULE_ACTION_CONDITION_KIND_V1_ALWAYS: ProductionRuleActionConditionKindV1
PRODUCTION_RULE_ACTION_CONDITION_KIND_V1_SCORE_BELOW: ProductionRuleActionConditionKindV1
PRODUCTION_RULE_ACTION_CONDITION_KIND_V1_SCORE_AT_OR_ABOVE: ProductionRuleActionConditionKindV1
PRODUCTION_RULE_ACTION_CONDITION_KIND_V1_SCORER_FAILED: ProductionRuleActionConditionKindV1
PRODUCTION_RULE_ACTION_CONDITION_KIND_V1_VERDICT_IS: ProductionRuleActionConditionKindV1
PRODUCTION_RULE_DEPENDENCY_KIND_V1_UNSPECIFIED: ProductionRuleDependencyKindV1
PRODUCTION_RULE_DEPENDENCY_KIND_V1_DATASET_COLLECTION: ProductionRuleDependencyKindV1
PRODUCTION_RULE_DEPENDENCY_KIND_V1_DATASET_VERSION: ProductionRuleDependencyKindV1
PRODUCTION_RULE_DEPENDENCY_KIND_V1_EVALUATION_DEFINITION: ProductionRuleDependencyKindV1
PRODUCTION_RULE_DEPENDENCY_KIND_V1_SCORE_CONFIG: ProductionRuleDependencyKindV1
PRODUCTION_RULE_DEPENDENCY_KIND_V1_SCORER_SUITE: ProductionRuleDependencyKindV1
PRODUCTION_RULE_DEPENDENCY_HEALTH_V1_UNSPECIFIED: ProductionRuleDependencyHealthV1
PRODUCTION_RULE_DEPENDENCY_HEALTH_V1_SATISFIED: ProductionRuleDependencyHealthV1
PRODUCTION_RULE_DEPENDENCY_HEALTH_V1_UNSATISFIED: ProductionRuleDependencyHealthV1
PRODUCTION_RULE_DEPENDENCY_HEALTH_V1_UNKNOWN: ProductionRuleDependencyHealthV1
PRODUCTION_RULE_VERSION_TRANSITION_V1_UNSPECIFIED: ProductionRuleVersionTransitionV1
PRODUCTION_RULE_VERSION_TRANSITION_V1_ACTIVATE: ProductionRuleVersionTransitionV1
PRODUCTION_RULE_VERSION_TRANSITION_V1_PAUSE: ProductionRuleVersionTransitionV1
PRODUCTION_RULE_VERSION_TRANSITION_V1_RESUME: ProductionRuleVersionTransitionV1
PRODUCTION_RULE_VERSION_TRANSITION_V1_ARCHIVE: ProductionRuleVersionTransitionV1
PRODUCTION_WORKFLOW_EXECUTION_STATE_V1_UNSPECIFIED: ProductionWorkflowExecutionStateV1
PRODUCTION_WORKFLOW_EXECUTION_STATE_V1_PENDING: ProductionWorkflowExecutionStateV1
PRODUCTION_WORKFLOW_EXECUTION_STATE_V1_RUNNING: ProductionWorkflowExecutionStateV1
PRODUCTION_WORKFLOW_EXECUTION_STATE_V1_SUCCEEDED: ProductionWorkflowExecutionStateV1
PRODUCTION_WORKFLOW_EXECUTION_STATE_V1_PARTIALLY_SUCCEEDED: ProductionWorkflowExecutionStateV1
PRODUCTION_WORKFLOW_EXECUTION_STATE_V1_FAILED: ProductionWorkflowExecutionStateV1
PRODUCTION_WORKFLOW_EXECUTION_STATE_V1_DEAD_LETTERED: ProductionWorkflowExecutionStateV1
PRODUCTION_WORKFLOW_EXECUTION_STATE_V1_CANCELLED: ProductionWorkflowExecutionStateV1
PRODUCTION_WORKFLOW_STEP_STATE_V1_UNSPECIFIED: ProductionWorkflowStepStateV1
PRODUCTION_WORKFLOW_STEP_STATE_V1_PENDING: ProductionWorkflowStepStateV1
PRODUCTION_WORKFLOW_STEP_STATE_V1_RUNNING: ProductionWorkflowStepStateV1
PRODUCTION_WORKFLOW_STEP_STATE_V1_SUCCEEDED: ProductionWorkflowStepStateV1
PRODUCTION_WORKFLOW_STEP_STATE_V1_RETRYABLE: ProductionWorkflowStepStateV1
PRODUCTION_WORKFLOW_STEP_STATE_V1_FAILED: ProductionWorkflowStepStateV1
PRODUCTION_WORKFLOW_STEP_STATE_V1_DEAD_LETTER: ProductionWorkflowStepStateV1
PRODUCTION_WORKFLOW_STEP_STATE_V1_SKIPPED: ProductionWorkflowStepStateV1
PRODUCTION_WORKFLOW_STEP_SKIP_REASON_V1_UNSPECIFIED: ProductionWorkflowStepSkipReasonV1
PRODUCTION_WORKFLOW_STEP_SKIP_REASON_V1_CONDITION_NOT_MET: ProductionWorkflowStepSkipReasonV1
PRODUCTION_WORKFLOW_STEP_SKIP_REASON_V1_PREREQUISITE_NOT_SATISFIED: ProductionWorkflowStepSkipReasonV1
PRODUCTION_WORKFLOW_STEP_SKIP_REASON_V1_BUDGET_EXHAUSTED: ProductionWorkflowStepSkipReasonV1
PRODUCTION_WORKFLOW_STEP_SKIP_REASON_V1_EXECUTION_CANCELLED: ProductionWorkflowStepSkipReasonV1
PRODUCTION_WORKFLOW_ADMISSION_V1_UNSPECIFIED: ProductionWorkflowAdmissionV1
PRODUCTION_WORKFLOW_ADMISSION_V1_STARTED: ProductionWorkflowAdmissionV1
PRODUCTION_WORKFLOW_ADMISSION_V1_IDEMPOTENT_REPLAY: ProductionWorkflowAdmissionV1
PRODUCTION_WORKFLOW_ADMISSION_V1_SKIPPED_SAMPLED_OUT: ProductionWorkflowAdmissionV1
PRODUCTION_WORKFLOW_ADMISSION_V1_SKIPPED_RULE_NOT_DISPATCHING: ProductionWorkflowAdmissionV1
PRODUCTION_WORKFLOW_ADMISSION_V1_SKIPPED_BUDGET_EXHAUSTED: ProductionWorkflowAdmissionV1
RELEASE_BLOCK_STATE_V1_UNSPECIFIED: ReleaseBlockStateV1
RELEASE_BLOCK_STATE_V1_ACTIVE: ReleaseBlockStateV1
RELEASE_BLOCK_STATE_V1_INDETERMINATE: ReleaseBlockStateV1
RELEASE_BLOCK_STATE_V1_CLEARED: ReleaseBlockStateV1
RELEASE_BLOCK_STATE_V1_EXPIRED: ReleaseBlockStateV1
RELEASE_BLOCK_STATE_V1_OVERRIDDEN: ReleaseBlockStateV1
PRODUCTION_RELEASE_BLOCK_EVIDENCE_KIND_V1_UNSPECIFIED: ProductionReleaseBlockEvidenceKindV1
PRODUCTION_RELEASE_BLOCK_EVIDENCE_KIND_V1_PRODUCTION_SCORE: ProductionReleaseBlockEvidenceKindV1
PRODUCTION_RELEASE_BLOCK_EVIDENCE_KIND_V1_DATASET_VERSION: ProductionReleaseBlockEvidenceKindV1
PRODUCTION_RELEASE_BLOCK_EVIDENCE_KIND_V1_EVALUATION_RUN: ProductionReleaseBlockEvidenceKindV1
PRODUCTION_RELEASE_BLOCK_EVIDENCE_KIND_V1_WORKFLOW_EXECUTION: ProductionReleaseBlockEvidenceKindV1
PRODUCTION_RELEASE_BLOCK_CLEAR_CONDITION_V1_UNSPECIFIED: ProductionReleaseBlockClearConditionV1
PRODUCTION_RELEASE_BLOCK_CLEAR_CONDITION_V1_RULE_PASSES_AGAIN: ProductionReleaseBlockClearConditionV1
PRODUCTION_RELEASE_BLOCK_CLEAR_CONDITION_V1_EXPIRY_ONLY: ProductionReleaseBlockClearConditionV1
RELEASE_INTEGRATION_KIND_V1_UNSPECIFIED: ReleaseIntegrationKindV1
RELEASE_INTEGRATION_KIND_V1_SIGNED_DEPLOYMENT_WEBHOOK: ReleaseIntegrationKindV1
RELEASE_INTEGRATION_KIND_V1_GITHUB_ACTIONS: ReleaseIntegrationKindV1
RELEASE_INTEGRATION_KIND_V1_ARGO_CD: ReleaseIntegrationKindV1
RELEASE_INTEGRATION_KIND_V1_KUBERNETES: ReleaseIntegrationKindV1
RELEASE_INTEGRATION_KIND_V1_PROMPT_REGISTRY_LABEL: ReleaseIntegrationKindV1
RELEASE_INTEGRATION_HEALTH_V1_UNSPECIFIED: ReleaseIntegrationHealthV1
RELEASE_INTEGRATION_HEALTH_V1_HEALTHY: ReleaseIntegrationHealthV1
RELEASE_INTEGRATION_HEALTH_V1_DEGRADED: ReleaseIntegrationHealthV1
RELEASE_INTEGRATION_HEALTH_V1_UNREACHABLE: ReleaseIntegrationHealthV1
RELEASE_INTEGRATION_HEALTH_V1_MISCONFIGURED: ReleaseIntegrationHealthV1
RELEASE_INTEGRATION_HEALTH_V1_SECRET_UNAVAILABLE: ReleaseIntegrationHealthV1
RELEASE_INTEGRATION_HEALTH_V1_ARCHIVED: ReleaseIntegrationHealthV1
RELEASE_SIGNING_KEY_STATE_V1_UNSPECIFIED: ReleaseSigningKeyStateV1
RELEASE_SIGNING_KEY_STATE_V1_ACTIVE: ReleaseSigningKeyStateV1
RELEASE_SIGNING_KEY_STATE_V1_ROTATING: ReleaseSigningKeyStateV1
RELEASE_SIGNING_KEY_STATE_V1_REVOKED: ReleaseSigningKeyStateV1
RELEASE_STAGE_V1_UNSPECIFIED: ReleaseStageV1
RELEASE_STAGE_V1_PRE_RELEASE: ReleaseStageV1
RELEASE_STAGE_V1_CANARY: ReleaseStageV1
RELEASE_STAGE_V1_RAMP: ReleaseStageV1
RELEASE_STAGE_V1_PRODUCTION: ReleaseStageV1
RELEASE_STAGE_V1_HELD: ReleaseStageV1
RELEASE_STAGE_V1_ABORTING: ReleaseStageV1
RELEASE_STAGE_V1_ABORTED: ReleaseStageV1
RELEASE_STAGE_V1_ROLLING_BACK: ReleaseStageV1
RELEASE_STAGE_V1_ROLLED_BACK: ReleaseStageV1
RELEASE_STAGE_V1_FAILED: ReleaseStageV1
RELEASE_STAGE_V1_VERIFICATION_REQUIRED: ReleaseStageV1
RELEASE_ACTION_STATE_V1_UNSPECIFIED: ReleaseActionStateV1
RELEASE_ACTION_STATE_V1_REQUESTED: ReleaseActionStateV1
RELEASE_ACTION_STATE_V1_DISPATCHED: ReleaseActionStateV1
RELEASE_ACTION_STATE_V1_ACCEPTED: ReleaseActionStateV1
RELEASE_ACTION_STATE_V1_OBSERVED: ReleaseActionStateV1
RELEASE_ACTION_STATE_V1_VERIFIED: ReleaseActionStateV1
RELEASE_ACTION_STATE_V1_FAILED: ReleaseActionStateV1
RELEASE_ACTION_STATE_V1_AMBIGUOUS: ReleaseActionStateV1
RELEASE_ACTION_STATE_V1_SUPERSEDED: ReleaseActionStateV1
RELEASE_ACTION_TYPE_V1_UNSPECIFIED: ReleaseActionTypeV1
RELEASE_ACTION_TYPE_V1_START_CANARY: ReleaseActionTypeV1
RELEASE_ACTION_TYPE_V1_PROMOTE: ReleaseActionTypeV1
RELEASE_ACTION_TYPE_V1_HOLD: ReleaseActionTypeV1
RELEASE_ACTION_TYPE_V1_ABORT: ReleaseActionTypeV1
RELEASE_ACTION_TYPE_V1_ROLLBACK: ReleaseActionTypeV1
RELEASE_ACTION_TYPE_V1_RECONCILE: ReleaseActionTypeV1
RELEASE_ADAPTER_OPERATION_V1_UNSPECIFIED: ReleaseAdapterOperationV1
RELEASE_ADAPTER_OPERATION_V1_PREVIEW: ReleaseAdapterOperationV1
RELEASE_ADAPTER_OPERATION_V1_START_CANARY: ReleaseAdapterOperationV1
RELEASE_ADAPTER_OPERATION_V1_PROMOTE: ReleaseAdapterOperationV1
RELEASE_ADAPTER_OPERATION_V1_HOLD: ReleaseAdapterOperationV1
RELEASE_ADAPTER_OPERATION_V1_ABORT: ReleaseAdapterOperationV1
RELEASE_ADAPTER_OPERATION_V1_ROLLBACK: ReleaseAdapterOperationV1
RELEASE_ADAPTER_OPERATION_V1_OBSERVE: ReleaseAdapterOperationV1
RELEASE_VALIDATION_KIND_V1_UNSPECIFIED: ReleaseValidationKindV1
RELEASE_VALIDATION_KIND_V1_COMPARABILITY: ReleaseValidationKindV1
RELEASE_VALIDATION_KIND_V1_COMPLETENESS: ReleaseValidationKindV1
RELEASE_VALIDATION_KIND_V1_FRESHNESS: ReleaseValidationKindV1
RELEASE_VALIDATION_KIND_V1_GATE_STATUS: ReleaseValidationKindV1
RELEASE_VALIDATION_KIND_V1_INTEGRATION_HEALTH: ReleaseValidationKindV1
RELEASE_VALIDATION_KIND_V1_ROLLBACK_TARGET: ReleaseValidationKindV1
RELEASE_VALIDATION_STATE_V1_UNSPECIFIED: ReleaseValidationStateV1
RELEASE_VALIDATION_STATE_V1_PASS: ReleaseValidationStateV1
RELEASE_VALIDATION_STATE_V1_WARN: ReleaseValidationStateV1
RELEASE_VALIDATION_STATE_V1_FAIL: ReleaseValidationStateV1
RELEASE_VALIDATION_STATE_V1_INDETERMINATE: ReleaseValidationStateV1
RELEASE_VALIDATION_STATE_V1_NOT_APPLICABLE: ReleaseValidationStateV1
RELEASE_ACTION_REASON_V1_UNSPECIFIED: ReleaseActionReasonV1
RELEASE_ACTION_REASON_V1_QUALITY_REGRESSION: ReleaseActionReasonV1
RELEASE_ACTION_REASON_V1_ERROR_RATE_REGRESSION: ReleaseActionReasonV1
RELEASE_ACTION_REASON_V1_LATENCY_REGRESSION: ReleaseActionReasonV1
RELEASE_ACTION_REASON_V1_COST_REGRESSION: ReleaseActionReasonV1
RELEASE_ACTION_REASON_V1_EVIDENCE_STALE: ReleaseActionReasonV1
RELEASE_ACTION_REASON_V1_EXTERNAL_DRIFT: ReleaseActionReasonV1
RELEASE_ACTION_REASON_V1_OPERATOR_REQUEST: ReleaseActionReasonV1
RELEASE_ACTION_REASON_V1_AUTOMATIC_HEALTH_POLICY: ReleaseActionReasonV1
RELEASE_ACTION_REASON_V1_INTEGRATION_UNHEALTHY: ReleaseActionReasonV1
RELEASE_VERIFICATION_OVERRIDE_REASON_V1_UNSPECIFIED: ReleaseVerificationOverrideReasonV1
RELEASE_VERIFICATION_OVERRIDE_REASON_V1_EXTERNAL_STATE_CONFIRMED_MANUALLY: ReleaseVerificationOverrideReasonV1
RELEASE_VERIFICATION_OVERRIDE_REASON_V1_INTEGRATION_PERMANENTLY_UNAVAILABLE: ReleaseVerificationOverrideReasonV1
RELEASE_VERIFICATION_OVERRIDE_REASON_V1_OPERATOR_ACCEPTS_RISK: ReleaseVerificationOverrideReasonV1
RELEASE_INTEGRATION_CREDENTIAL_STATE_V1_UNSPECIFIED: ReleaseIntegrationCredentialStateV1
RELEASE_INTEGRATION_CREDENTIAL_STATE_V1_ACTIVE: ReleaseIntegrationCredentialStateV1
RELEASE_INTEGRATION_CREDENTIAL_STATE_V1_REVOKED: ReleaseIntegrationCredentialStateV1
EVALUATION_REVIEW_SUBJECT_KIND_V1_UNSPECIFIED: EvaluationReviewSubjectKindV1
EVALUATION_REVIEW_SUBJECT_KIND_V1_EVALUATION_CELL: EvaluationReviewSubjectKindV1
EVALUATION_REVIEW_SUBJECT_KIND_V1_DATASET_PROPOSED_CASE: EvaluationReviewSubjectKindV1
DATASET_REDACTION_DETECTOR_KIND_V1_UNSPECIFIED: DatasetRedactionDetectorKindV1
DATASET_REDACTION_DETECTOR_KIND_V1_EMAIL: DatasetRedactionDetectorKindV1
DATASET_REDACTION_DETECTOR_KIND_V1_PHONE_E164: DatasetRedactionDetectorKindV1
DATASET_REDACTION_DETECTOR_KIND_V1_CREDIT_CARD: DatasetRedactionDetectorKindV1
DATASET_REDACTION_DETECTOR_KIND_V1_API_KEY: DatasetRedactionDetectorKindV1
DATASET_REDACTION_DETECTOR_KIND_V1_JWT: DatasetRedactionDetectorKindV1
DATASET_REDACTION_DETECTOR_KIND_V1_DENY_PATH: DatasetRedactionDetectorKindV1
DATASET_REDACTION_OUTCOME_KIND_V1_UNSPECIFIED: DatasetRedactionOutcomeKindV1
DATASET_REDACTION_OUTCOME_KIND_V1_CLEAN: DatasetRedactionOutcomeKindV1
DATASET_REDACTION_OUTCOME_KIND_V1_REDACTED: DatasetRedactionOutcomeKindV1
DATASET_REDACTION_OUTCOME_KIND_V1_BLOCKED: DatasetRedactionOutcomeKindV1
DATASET_REDACTION_OUTCOME_KIND_V1_INDETERMINATE: DatasetRedactionOutcomeKindV1
DATASET_DEDUPE_SUBJECT_KIND_V1_UNSPECIFIED: DatasetDedupeSubjectKindV1
DATASET_DEDUPE_SUBJECT_KIND_V1_DATASET_ITEM: DatasetDedupeSubjectKindV1
DATASET_DEDUPE_SUBJECT_KIND_V1_PROPOSED_CASE: DatasetDedupeSubjectKindV1
DATASET_DUPLICATION_VERDICT_V1_UNSPECIFIED: DatasetDuplicationVerdictV1
DATASET_DUPLICATION_VERDICT_V1_NO_MATCH: DatasetDuplicationVerdictV1
DATASET_DUPLICATION_VERDICT_V1_EXACT_MATCH: DatasetDuplicationVerdictV1
DATASET_DUPLICATION_VERDICT_V1_NEAR_MATCH: DatasetDuplicationVerdictV1
DATASET_DUPLICATION_VERDICT_V1_CONFLICT: DatasetDuplicationVerdictV1
DATASET_DUPLICATION_VERDICT_V1_UNAVAILABLE: DatasetDuplicationVerdictV1
DATASET_DEDUPE_RESOLUTION_KIND_V1_UNSPECIFIED: DatasetDedupeResolutionKindV1
DATASET_DEDUPE_RESOLUTION_KIND_V1_AUTO_EXACT: DatasetDedupeResolutionKindV1
DATASET_DEDUPE_RESOLUTION_KIND_V1_MERGE_INTO: DatasetDedupeResolutionKindV1
DATASET_DEDUPE_RESOLUTION_KIND_V1_KEEP_SEPARATE: DatasetDedupeResolutionKindV1
DATASET_DEDUPE_RESOLUTION_KIND_V1_CONFLICT_BLOCKED: DatasetDedupeResolutionKindV1
DATASET_DEDUPE_RESOLUTION_KIND_V1_AUDITED_OVERRIDE_SEPARATE: DatasetDedupeResolutionKindV1
DATASET_LEAKAGE_SOURCE_KIND_V1_UNSPECIFIED: DatasetLeakageSourceKindV1
DATASET_LEAKAGE_SOURCE_KIND_V1_PRIOR_EVALUATION_CASES: DatasetLeakageSourceKindV1
DATASET_LEAKAGE_SOURCE_KIND_V1_ADOPTED_RELEASE_EVIDENCE: DatasetLeakageSourceKindV1
DATASET_LEAKAGE_SOURCE_KIND_V1_CONFIGURED_REFERENCE_SET: DatasetLeakageSourceKindV1
DATASET_LEAKAGE_VERDICT_V1_UNSPECIFIED: DatasetLeakageVerdictV1
DATASET_LEAKAGE_VERDICT_V1_NO_SIGNAL: DatasetLeakageVerdictV1
DATASET_LEAKAGE_VERDICT_V1_EXACT_OVERLAP: DatasetLeakageVerdictV1
DATASET_LEAKAGE_VERDICT_V1_NEAR_OVERLAP: DatasetLeakageVerdictV1
DATASET_LEAKAGE_VERDICT_V1_NOT_COMPARABLE: DatasetLeakageVerdictV1
DATASET_SLICE_DIMENSION_SOURCE_V1_UNSPECIFIED: DatasetSliceDimensionSourceV1
DATASET_SLICE_DIMENSION_SOURCE_V1_SCHEMA_REVISION: DatasetSliceDimensionSourceV1
DATASET_SLICE_DIMENSION_SOURCE_V1_SHIPPED_COHORT_ONLY: DatasetSliceDimensionSourceV1
DATASET_SLICE_FLAG_V1_UNSPECIFIED: DatasetSliceFlagV1
DATASET_SLICE_FLAG_V1_WITHIN_BAND: DatasetSliceFlagV1
DATASET_SLICE_FLAG_V1_OVERREPRESENTED: DatasetSliceFlagV1
DATASET_SLICE_FLAG_V1_UNDERREPRESENTED: DatasetSliceFlagV1
DATASET_SLICE_FLAG_V1_MISSING: DatasetSliceFlagV1
DATASET_SLICE_FLAG_V1_NOT_COMPARABLE: DatasetSliceFlagV1
DATASET_SCHEMA_VALUE_KIND_V1_UNSPECIFIED: DatasetSchemaValueKindV1
DATASET_SCHEMA_VALUE_KIND_V1_STRING: DatasetSchemaValueKindV1
DATASET_SCHEMA_VALUE_KIND_V1_INTEGER: DatasetSchemaValueKindV1
DATASET_SCHEMA_VALUE_KIND_V1_DOUBLE: DatasetSchemaValueKindV1
DATASET_SCHEMA_VALUE_KIND_V1_BOOLEAN: DatasetSchemaValueKindV1
DATASET_SCHEMA_VALUE_KIND_V1_TIMESTAMP: DatasetSchemaValueKindV1
DATASET_SCHEMA_VALUE_KIND_V1_JSON: DatasetSchemaValueKindV1
DATASET_SCHEMA_COMPATIBILITY_POLICY_V1_UNSPECIFIED: DatasetSchemaCompatibilityPolicyV1
DATASET_SCHEMA_COMPATIBILITY_POLICY_V1_ADDITIVE_ONLY: DatasetSchemaCompatibilityPolicyV1
DATASET_SCHEMA_COMPATIBILITY_POLICY_V1_STRICT: DatasetSchemaCompatibilityPolicyV1
DATASET_SCHEMA_COMPATIBILITY_VERDICT_KIND_V1_UNSPECIFIED: DatasetSchemaCompatibilityVerdictKindV1
DATASET_SCHEMA_COMPATIBILITY_VERDICT_KIND_V1_IDENTICAL: DatasetSchemaCompatibilityVerdictKindV1
DATASET_SCHEMA_COMPATIBILITY_VERDICT_KIND_V1_COMPATIBLE_ADDITIVE: DatasetSchemaCompatibilityVerdictKindV1
DATASET_SCHEMA_COMPATIBILITY_VERDICT_KIND_V1_INCOMPATIBLE: DatasetSchemaCompatibilityVerdictKindV1
DATASET_SCHEMA_COMPATIBILITY_VERDICT_KIND_V1_NOT_COMPARABLE: DatasetSchemaCompatibilityVerdictKindV1
DATASET_SCHEMA_CHANGE_KIND_V1_UNSPECIFIED: DatasetSchemaChangeKindV1
DATASET_SCHEMA_CHANGE_KIND_V1_INPUT_FIELD_ADDED: DatasetSchemaChangeKindV1
DATASET_SCHEMA_CHANGE_KIND_V1_INPUT_FIELD_REMOVED: DatasetSchemaChangeKindV1
DATASET_SCHEMA_CHANGE_KIND_V1_EXPECTED_FIELD_ADDED: DatasetSchemaChangeKindV1
DATASET_SCHEMA_CHANGE_KIND_V1_EXPECTED_FIELD_REMOVED: DatasetSchemaChangeKindV1
DATASET_SCHEMA_CHANGE_KIND_V1_FIELD_TYPE_CHANGED: DatasetSchemaChangeKindV1
DATASET_SCHEMA_CHANGE_KIND_V1_FIELD_MADE_REQUIRED: DatasetSchemaChangeKindV1
DATASET_SCHEMA_CHANGE_KIND_V1_FIELD_MADE_OPTIONAL: DatasetSchemaChangeKindV1
DATASET_SCHEMA_CHANGE_KIND_V1_SLICE_DIMENSION_ADDED: DatasetSchemaChangeKindV1
DATASET_SCHEMA_CHANGE_KIND_V1_SLICE_DIMENSION_REMOVED: DatasetSchemaChangeKindV1
DATASET_SCHEMA_CHANGE_KIND_V1_SLICE_VOCABULARY_NARROWED: DatasetSchemaChangeKindV1
DATASET_SCHEMA_CHANGE_KIND_V1_METADATA_KEY_ADDED: DatasetSchemaChangeKindV1
DATASET_SCHEMA_CHANGE_KIND_V1_METADATA_KEY_REMOVED: DatasetSchemaChangeKindV1
DATASET_SCHEMA_CHANGE_KIND_V1_MAPPING_RULE_CHANGED: DatasetSchemaChangeKindV1
DATASET_SCHEMA_CHANGE_KIND_V1_POLICY_CHANGED: DatasetSchemaChangeKindV1
DATASET_CASE_REGRESSION_POSTURE_V1_UNSPECIFIED: DatasetCaseRegressionPostureV1
DATASET_CASE_REGRESSION_POSTURE_V1_IMPROVED: DatasetCaseRegressionPostureV1
DATASET_CASE_REGRESSION_POSTURE_V1_UNCHANGED: DatasetCaseRegressionPostureV1
DATASET_CASE_REGRESSION_POSTURE_V1_REGRESSED: DatasetCaseRegressionPostureV1
DATASET_CASE_REGRESSION_POSTURE_V1_UNKNOWN: DatasetCaseRegressionPostureV1
DATASET_CASE_RESULT_POSTURE_V1_UNSPECIFIED: DatasetCaseResultPostureV1
DATASET_CASE_RESULT_POSTURE_V1_PASSED: DatasetCaseResultPostureV1
DATASET_CASE_RESULT_POSTURE_V1_FAILED: DatasetCaseResultPostureV1
DATASET_CASE_RESULT_POSTURE_V1_UNSCORED: DatasetCaseResultPostureV1
DATASET_CASE_RESULT_POSTURE_V1_UNKNOWN: DatasetCaseResultPostureV1
DATASET_CASE_COMPLETENESS_STATE_V1_UNSPECIFIED: DatasetCaseCompletenessStateV1
DATASET_CASE_COMPLETENESS_STATE_V1_COMPLETE: DatasetCaseCompletenessStateV1
DATASET_CASE_COMPLETENESS_STATE_V1_MISSING_INPUT: DatasetCaseCompletenessStateV1
DATASET_CASE_COMPLETENESS_STATE_V1_MISSING_EXPECTED_OUTPUT: DatasetCaseCompletenessStateV1
DATASET_CASE_COMPLETENESS_STATE_V1_MISSING_BOTH: DatasetCaseCompletenessStateV1
DATASET_CASE_IDENTITY_SOURCE_V1_UNSPECIFIED: DatasetCaseIdentitySourceV1
DATASET_CASE_IDENTITY_SOURCE_V1_DERIVED_FROM_LINEAGE: DatasetCaseIdentitySourceV1
DATASET_CASE_IDENTITY_SOURCE_V1_CONTENT_ONLY: DatasetCaseIdentitySourceV1
DATASET_CASE_IDENTITY_SOURCE_V1_REVIEWER_MERGE: DatasetCaseIdentitySourceV1
DATASET_CASE_IDENTITY_SOURCE_V1_BACKFILLED_FROM_DATASET_ITEM: DatasetCaseIdentitySourceV1
DATASET_LINEAGE_ANCHOR_AVAILABILITY_V1_UNSPECIFIED: DatasetLineageAnchorAvailabilityV1
DATASET_LINEAGE_ANCHOR_AVAILABILITY_V1_AVAILABLE: DatasetLineageAnchorAvailabilityV1
DATASET_LINEAGE_ANCHOR_AVAILABILITY_V1_ANCHOR_TARGET_EXPIRED: DatasetLineageAnchorAvailabilityV1
DATASET_LINEAGE_ANCHOR_AVAILABILITY_V1_ANCHOR_TARGET_DELETED: DatasetLineageAnchorAvailabilityV1
DATASET_LINEAGE_ANCHOR_AVAILABILITY_V1_NOT_APPLICABLE: DatasetLineageAnchorAvailabilityV1
DATASET_CASE_LINEAGE_ANCHOR_KIND_V1_UNSPECIFIED: DatasetCaseLineageAnchorKindV1
DATASET_CASE_LINEAGE_ANCHOR_KIND_V1_NONE: DatasetCaseLineageAnchorKindV1
DATASET_CASE_LINEAGE_ANCHOR_KIND_V1_TELEMETRY: DatasetCaseLineageAnchorKindV1
DATASET_CASE_LINEAGE_ANCHOR_KIND_V1_AGENT_RUN: DatasetCaseLineageAnchorKindV1
DATASET_CASE_LINEAGE_ANCHOR_KIND_V1_EVALUATION_CELL: DatasetCaseLineageAnchorKindV1
DATASET_CASE_LINEAGE_ANCHOR_KIND_V1_RULE_WORKFLOW_STEP: DatasetCaseLineageAnchorKindV1
DATASET_CASE_DRAFT_STATE_V1_UNSPECIFIED: DatasetCaseDraftStateV1
DATASET_CASE_DRAFT_STATE_V1_EXTRACTED: DatasetCaseDraftStateV1
DATASET_CASE_DRAFT_STATE_V1_NEEDS_GROUND_TRUTH: DatasetCaseDraftStateV1
DATASET_CASE_DRAFT_STATE_V1_IN_REVIEW: DatasetCaseDraftStateV1
DATASET_CASE_DRAFT_STATE_V1_CHANGES_REQUESTED: DatasetCaseDraftStateV1
DATASET_CASE_DRAFT_STATE_V1_APPROVED: DatasetCaseDraftStateV1
DATASET_CASE_DRAFT_STATE_V1_REJECTED: DatasetCaseDraftStateV1
DATASET_CASE_DRAFT_STATE_V1_MERGED: DatasetCaseDraftStateV1
DATASET_CASE_DRAFT_STATE_V1_NON_REPRESENTATIVE: DatasetCaseDraftStateV1
DATASET_CASE_DRAFT_STATE_V1_PUBLISHED: DatasetCaseDraftStateV1
DATASET_CASE_DRAFT_STATE_V1_SUPERSEDED: DatasetCaseDraftStateV1
DATASET_CHANGESET_STATE_V1_UNSPECIFIED: DatasetChangesetStateV1
DATASET_CHANGESET_STATE_V1_OPEN: DatasetChangesetStateV1
DATASET_CHANGESET_STATE_V1_PREVIEWED: DatasetChangesetStateV1
DATASET_CHANGESET_STATE_V1_REBASE_REQUIRED: DatasetChangesetStateV1
DATASET_CHANGESET_STATE_V1_CONFLICTED: DatasetChangesetStateV1
DATASET_CHANGESET_STATE_V1_COMMITTING: DatasetChangesetStateV1
DATASET_CHANGESET_STATE_V1_COMMITTED: DatasetChangesetStateV1
DATASET_CHANGESET_STATE_V1_ABANDONED: DatasetChangesetStateV1
DATASET_CHANGESET_STATE_V1_FAILED: DatasetChangesetStateV1
DATASET_CASE_REVIEW_OUTCOME_V1_UNSPECIFIED: DatasetCaseReviewOutcomeV1
DATASET_CASE_REVIEW_OUTCOME_V1_CORRECTION: DatasetCaseReviewOutcomeV1
DATASET_CASE_REVIEW_OUTCOME_V1_MERGE_WITH_EXISTING: DatasetCaseReviewOutcomeV1
DATASET_CASE_REVIEW_OUTCOME_V1_NON_REPRESENTATIVE: DatasetCaseReviewOutcomeV1
DATASET_CASE_REVIEW_OUTCOME_V1_NEEDS_GROUND_TRUTH: DatasetCaseReviewOutcomeV1
DATASET_CASE_REVIEW_OUTCOME_V1_APPROVE: DatasetCaseReviewOutcomeV1
DATASET_CASE_REVIEW_OUTCOME_V1_REJECT: DatasetCaseReviewOutcomeV1
DATASET_CASE_DRAFT_REJECTION_REASON_V1_UNSPECIFIED: DatasetCaseDraftRejectionReasonV1
DATASET_CASE_DRAFT_REJECTION_REASON_V1_NON_REPRESENTATIVE: DatasetCaseDraftRejectionReasonV1
DATASET_CASE_DRAFT_REJECTION_REASON_V1_INCORRECT_EXPECTED_OUTPUT: DatasetCaseDraftRejectionReasonV1
DATASET_CASE_DRAFT_REJECTION_REASON_V1_SENSITIVE_CONTENT: DatasetCaseDraftRejectionReasonV1
DATASET_CASE_DRAFT_REJECTION_REASON_V1_DUPLICATE_OF_EXISTING_CASE: DatasetCaseDraftRejectionReasonV1
DATASET_CASE_DRAFT_REJECTION_REASON_V1_INSUFFICIENT_CONTEXT: DatasetCaseDraftRejectionReasonV1
DATASET_CASE_DRAFT_REJECTION_REASON_V1_OUT_OF_SCOPE: DatasetCaseDraftRejectionReasonV1
DATASET_CASE_DRAFT_REJECTION_REASON_V1_SUPERSEDED_BY_OVERRIDE: DatasetCaseDraftRejectionReasonV1
DATASET_DRAFT_REFUSAL_KIND_V1_UNSPECIFIED: DatasetDraftRefusalKindV1
DATASET_DRAFT_REFUSAL_KIND_V1_ILLEGAL_TRANSITION: DatasetDraftRefusalKindV1
DATASET_DRAFT_REFUSAL_KIND_V1_VERSION_CONFLICT: DatasetDraftRefusalKindV1
DATASET_DRAFT_REFUSAL_KIND_V1_RESERVED_BY_ANOTHER_REVIEWER: DatasetDraftRefusalKindV1
DATASET_DRAFT_REFUSAL_KIND_V1_UNRESOLVED_DEDUPE_DECISION: DatasetDraftRefusalKindV1
DATASET_DRAFT_REFUSAL_KIND_V1_DRAFT_TERMINAL: DatasetDraftRefusalKindV1
DATASET_DRAFT_REFUSAL_KIND_V1_BASE_VERSION_MOVED: DatasetDraftRefusalKindV1
DATASET_DRAFT_REFUSAL_KIND_V1_PREVIEW_DIGEST_MISMATCH: DatasetDraftRefusalKindV1
DATASET_DRAFT_REFUSAL_KIND_V1_UNAPPROVED_CASE_PRESENT: DatasetDraftRefusalKindV1
DATASET_DRAFT_REFUSAL_KIND_V1_SCHEMA_INCOMPATIBLE: DatasetDraftRefusalKindV1
DATASET_DRAFT_REFUSAL_KIND_V1_QUALITY_SIGNALS_BLOCK_PUBLISH: DatasetDraftRefusalKindV1
DATASET_DRAFT_REFUSAL_KIND_V1_CHANGESET_NOT_PUBLISHABLE: DatasetDraftRefusalKindV1
PRODUCTION_RULE_PREVIEW_OBSERVATION_BASIS_V1_UNSPECIFIED: ProductionRulePreviewObservationBasisV1
PRODUCTION_RULE_PREVIEW_OBSERVATION_BASIS_V1_ADMITTED_EXECUTIONS_IN_WINDOW: ProductionRulePreviewObservationBasisV1
PRODUCTION_RULE_PREVIEW_TARGET_RESOLUTION_V1_UNSPECIFIED: ProductionRulePreviewTargetResolutionV1
PRODUCTION_RULE_PREVIEW_TARGET_RESOLUTION_V1_NOT_APPLICABLE: ProductionRulePreviewTargetResolutionV1
PRODUCTION_RULE_PREVIEW_TARGET_RESOLUTION_V1_RESOLVED: ProductionRulePreviewTargetResolutionV1
PRODUCTION_RULE_PREVIEW_TARGET_RESOLUTION_V1_UNRESOLVED: ProductionRulePreviewTargetResolutionV1
PRODUCTION_RULE_PREVIEW_TARGET_RESOLUTION_V1_ABSENT: ProductionRulePreviewTargetResolutionV1
PRODUCTION_RULE_PREVIEW_REDACTION_POSTURE_V1_UNSPECIFIED: ProductionRulePreviewRedactionPostureV1
PRODUCTION_RULE_PREVIEW_REDACTION_POSTURE_V1_HYDRATION_UNAVAILABLE_IN_PREVIEW: ProductionRulePreviewRedactionPostureV1
PRODUCTION_RULE_PREVIEW_REVISION_PIN_V1_UNSPECIFIED: ProductionRulePreviewRevisionPinV1
PRODUCTION_RULE_PREVIEW_REVISION_PIN_V1_PINNED: ProductionRulePreviewRevisionPinV1
PRODUCTION_RULE_PREVIEW_REVISION_PIN_V1_CURRENT_AT_DISPATCH: ProductionRulePreviewRevisionPinV1
PRODUCTION_RULE_PREVIEW_ZERO_MATCH_REASON_V1_UNSPECIFIED: ProductionRulePreviewZeroMatchReasonV1
PRODUCTION_RULE_PREVIEW_ZERO_MATCH_REASON_V1_NO_OFFERS_IN_WINDOW: ProductionRulePreviewZeroMatchReasonV1
PRODUCTION_RULE_PREVIEW_ZERO_MATCH_REASON_V1_VERSION_NOT_DISPATCHING: ProductionRulePreviewZeroMatchReasonV1
PRODUCTION_RULE_PREVIEW_ZERO_MATCH_REASON_V1_ALL_SAMPLED_OUT: ProductionRulePreviewZeroMatchReasonV1
PRODUCTION_RULE_PREVIEW_ZERO_MATCH_REASON_V1_ALL_BUDGET_BLOCKED: ProductionRulePreviewZeroMatchReasonV1
PRODUCTION_RULE_PREVIEW_ZERO_MATCH_REASON_V1_ALL_ALREADY_EXECUTED: ProductionRulePreviewZeroMatchReasonV1
PRODUCTION_RULE_PREVIEW_ZERO_MATCH_REASON_V1_MIXED_EXCLUSIONS: ProductionRulePreviewZeroMatchReasonV1
PRODUCTION_RULE_PREVIEW_REFUSAL_KIND_V1_UNSPECIFIED: ProductionRulePreviewRefusalKindV1
PRODUCTION_RULE_PREVIEW_REFUSAL_KIND_V1_SAMPLE_WINDOW_TOO_LARGE: ProductionRulePreviewRefusalKindV1
PRODUCTION_RULE_PREVIEW_REFUSAL_KIND_V1_SAMPLING_RATE_INVALID: ProductionRulePreviewRefusalKindV1
PRODUCTION_RULE_PREVIEW_REFUSAL_KIND_V1_ACTION_KIND_UNKNOWN: ProductionRulePreviewRefusalKindV1
PRODUCTION_RULE_PREVIEW_REFUSAL_KIND_V1_SELECTOR_MALFORMED: ProductionRulePreviewRefusalKindV1
RELEASE_OBSERVATION_CONFIDENCE_V1_UNSPECIFIED: ReleaseObservationConfidenceV1
RELEASE_OBSERVATION_CONFIDENCE_V1_EXACT: ReleaseObservationConfidenceV1
RELEASE_OBSERVATION_CONFIDENCE_V1_WINDOW: ReleaseObservationConfidenceV1
MACHINE_PRINCIPAL_SCOPE_V1_UNSPECIFIED: MachinePrincipalScopeV1
MACHINE_PRINCIPAL_SCOPE_V1_EVAL_READ: MachinePrincipalScopeV1
MACHINE_PRINCIPAL_SCOPE_V1_RUN_EXECUTE: MachinePrincipalScopeV1
MACHINE_PRINCIPAL_SCOPE_V1_DATASET_WRITE: MachinePrincipalScopeV1
MACHINE_PRINCIPAL_SCOPE_V1_LEASE_SUBMIT: MachinePrincipalScopeV1
MACHINE_PRINCIPAL_SCOPE_V1_PLATFORM_ANNOTATION_WRITE: MachinePrincipalScopeV1
MACHINE_PRINCIPAL_STATE_V1_UNSPECIFIED: MachinePrincipalStateV1
MACHINE_PRINCIPAL_STATE_V1_ACTIVE: MachinePrincipalStateV1
MACHINE_PRINCIPAL_STATE_V1_DISABLED: MachinePrincipalStateV1
MACHINE_PRINCIPAL_STATE_V1_REVOKED: MachinePrincipalStateV1
MACHINE_CREDENTIAL_STATE_V1_UNSPECIFIED: MachineCredentialStateV1
MACHINE_CREDENTIAL_STATE_V1_ACTIVE: MachineCredentialStateV1
MACHINE_CREDENTIAL_STATE_V1_ROTATING: MachineCredentialStateV1
MACHINE_CREDENTIAL_STATE_V1_REVOKED: MachineCredentialStateV1
EXTERNAL_SUBMISSION_ACK_KIND_V1_UNSPECIFIED: ExternalSubmissionAckKindV1
EXTERNAL_SUBMISSION_ACK_KIND_V1_ACCEPTED: ExternalSubmissionAckKindV1
EXTERNAL_SUBMISSION_ACK_KIND_V1_ALREADY_SUBMITTED: ExternalSubmissionAckKindV1
EXTERNAL_SUBMISSION_ACK_KIND_V1_REJECTED: ExternalSubmissionAckKindV1
EXTERNAL_LEASE_REFUSAL_KIND_V1_UNSPECIFIED: ExternalLeaseRefusalKindV1
EXTERNAL_LEASE_REFUSAL_KIND_V1_RUN_NOT_EXECUTABLE: ExternalLeaseRefusalKindV1
EXTERNAL_LEASE_REFUSAL_KIND_V1_CANDIDATE_NOT_EXTERNALLY_EXECUTED: ExternalLeaseRefusalKindV1
EXTERNAL_LEASE_REFUSAL_KIND_V1_LEASE_NOT_HELD: ExternalLeaseRefusalKindV1
EXTERNAL_LEASE_REFUSAL_KIND_V1_LEASE_EXPIRED: ExternalLeaseRefusalKindV1
EXTERNAL_LEASE_REFUSAL_KIND_V1_RENEWAL_BUDGET_EXHAUSTED: ExternalLeaseRefusalKindV1
EXTERNAL_LEASE_REFUSAL_KIND_V1_BOUNDS_EXCEEDED: ExternalLeaseRefusalKindV1
EXTERNAL_LEASE_REFUSAL_KIND_V1_SCOPE_MISSING: ExternalLeaseRefusalKindV1
PLATFORM_ANNOTATION_KIND_V1_UNSPECIFIED: PlatformAnnotationKindV1
PLATFORM_ANNOTATION_KIND_V1_DEPLOYMENT: PlatformAnnotationKindV1
PLATFORM_ANNOTATION_KIND_V1_MARKER: PlatformAnnotationKindV1
PLATFORM_ANNOTATION_KIND_V1_HIGHLIGHT: PlatformAnnotationKindV1
PLATFORM_ANNOTATION_LINK_KIND_V1_UNSPECIFIED: PlatformAnnotationLinkKindV1
PLATFORM_ANNOTATION_LINK_KIND_V1_RELEASE: PlatformAnnotationLinkKindV1
PLATFORM_ANNOTATION_LINK_KIND_V1_EVALUATION_RUN: PlatformAnnotationLinkKindV1
PLATFORM_ANNOTATION_LINK_KIND_V1_AGENT_RUN: PlatformAnnotationLinkKindV1
PLATFORM_ANNOTATION_LINK_KIND_V1_TRACE: PlatformAnnotationLinkKindV1
PLATFORM_ANNOTATION_REJECTION_REASON_V1_UNSPECIFIED: PlatformAnnotationRejectionReasonV1
PLATFORM_ANNOTATION_REJECTION_REASON_V1_KIND_UNKNOWN: PlatformAnnotationRejectionReasonV1
PLATFORM_ANNOTATION_REJECTION_REASON_V1_TITLE_TOO_LARGE: PlatformAnnotationRejectionReasonV1
PLATFORM_ANNOTATION_REJECTION_REASON_V1_ATTRIBUTE_TOO_LARGE: PlatformAnnotationRejectionReasonV1
PLATFORM_ANNOTATION_REJECTION_REASON_V1_TOO_MANY_ATTRIBUTES: PlatformAnnotationRejectionReasonV1
PLATFORM_ANNOTATION_REJECTION_REASON_V1_TOO_MANY_LINKS: PlatformAnnotationRejectionReasonV1
PLATFORM_ANNOTATION_REJECTION_REASON_V1_LINK_REF_TOO_LARGE: PlatformAnnotationRejectionReasonV1
PLATFORM_ANNOTATION_REJECTION_REASON_V1_RANGE_INVERTED: PlatformAnnotationRejectionReasonV1
PLATFORM_ANNOTATION_REJECTION_REASON_V1_IDEMPOTENCY_KEY_REUSED: PlatformAnnotationRejectionReasonV1
PLATFORM_ANNOTATION_REJECTION_REASON_V1_WINDOW_INVALID: PlatformAnnotationRejectionReasonV1
EVALUATION_SCORER_ARCHIVED_FILTER_V1_UNSPECIFIED: EvaluationScorerArchivedFilterV1
EVALUATION_SCORER_ARCHIVED_FILTER_V1_ACTIVE_ONLY: EvaluationScorerArchivedFilterV1
EVALUATION_SCORER_ARCHIVED_FILTER_V1_ARCHIVED_ONLY: EvaluationScorerArchivedFilterV1
EVALUATION_SCORER_ARCHIVED_FILTER_V1_ALL: EvaluationScorerArchivedFilterV1

class StringListV1(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...

class Int64ListV1(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, values: _Optional[_Iterable[int]] = ...) -> None: ...

class DoubleListV1(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, values: _Optional[_Iterable[float]] = ...) -> None: ...

class MetadataValueV1(_message.Message):
    __slots__ = ("string_value", "int_value", "double_value", "bool_value", "timestamp_value", "string_list", "int_list", "double_list")
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_LIST_FIELD_NUMBER: _ClassVar[int]
    INT_LIST_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_LIST_FIELD_NUMBER: _ClassVar[int]
    string_value: str
    int_value: int
    double_value: float
    bool_value: bool
    timestamp_value: _timestamp_pb2.Timestamp
    string_list: StringListV1
    int_list: Int64ListV1
    double_list: DoubleListV1
    def __init__(self, string_value: _Optional[str] = ..., int_value: _Optional[int] = ..., double_value: _Optional[float] = ..., bool_value: _Optional[bool] = ..., timestamp_value: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., string_list: _Optional[_Union[StringListV1, _Mapping]] = ..., int_list: _Optional[_Union[Int64ListV1, _Mapping]] = ..., double_list: _Optional[_Union[DoubleListV1, _Mapping]] = ...) -> None: ...

class MetadataEntryV1(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: MetadataValueV1
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MetadataValueV1, _Mapping]] = ...) -> None: ...

class PrincipalRefV1(_message.Message):
    __slots__ = ("kind", "principal_id", "display_name", "credential_id", "on_behalf_of_user_id")
    KIND_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_ID_FIELD_NUMBER: _ClassVar[int]
    ON_BEHALF_OF_USER_ID_FIELD_NUMBER: _ClassVar[int]
    kind: PrincipalKindV1
    principal_id: str
    display_name: str
    credential_id: str
    on_behalf_of_user_id: str
    def __init__(self, kind: _Optional[_Union[PrincipalKindV1, str]] = ..., principal_id: _Optional[str] = ..., display_name: _Optional[str] = ..., credential_id: _Optional[str] = ..., on_behalf_of_user_id: _Optional[str] = ...) -> None: ...

class EvaluationFreshnessV1(_message.Message):
    __slots__ = ("projection_version", "facts_watermark", "complete_through", "updated_at", "completeness", "stale_reason_code")
    PROJECTION_VERSION_FIELD_NUMBER: _ClassVar[int]
    FACTS_WATERMARK_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_THROUGH_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETENESS_FIELD_NUMBER: _ClassVar[int]
    STALE_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    projection_version: int
    facts_watermark: str
    complete_through: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    completeness: CompletenessStateV1
    stale_reason_code: str
    def __init__(self, projection_version: _Optional[int] = ..., facts_watermark: _Optional[str] = ..., complete_through: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., completeness: _Optional[_Union[CompletenessStateV1, str]] = ..., stale_reason_code: _Optional[str] = ...) -> None: ...

class MetricAvailabilityV1(_message.Message):
    __slots__ = ("state", "reason_code", "provenance")
    STATE_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    PROVENANCE_FIELD_NUMBER: _ClassVar[int]
    state: MetricAvailabilityStateV1
    reason_code: str
    provenance: SemanticConventionProvenanceV1
    def __init__(self, state: _Optional[_Union[MetricAvailabilityStateV1, str]] = ..., reason_code: _Optional[str] = ..., provenance: _Optional[_Union[SemanticConventionProvenanceV1, _Mapping]] = ...) -> None: ...

class SemanticConventionProvenanceV1(_message.Message):
    __slots__ = ("convention_source", "convention_version", "alias_key")
    CONVENTION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CONVENTION_VERSION_FIELD_NUMBER: _ClassVar[int]
    ALIAS_KEY_FIELD_NUMBER: _ClassVar[int]
    convention_source: str
    convention_version: str
    alias_key: str
    def __init__(self, convention_source: _Optional[str] = ..., convention_version: _Optional[str] = ..., alias_key: _Optional[str] = ...) -> None: ...

class AllowedActionV1(_message.Message):
    __slots__ = ("kind", "allowed", "blocked_reason", "blocked_detail")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_REASON_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_DETAIL_FIELD_NUMBER: _ClassVar[int]
    kind: EvaluationActionKindV1
    allowed: bool
    blocked_reason: ActionBlockedReasonV1
    blocked_detail: str
    def __init__(self, kind: _Optional[_Union[EvaluationActionKindV1, str]] = ..., allowed: _Optional[bool] = ..., blocked_reason: _Optional[_Union[ActionBlockedReasonV1, str]] = ..., blocked_detail: _Optional[str] = ...) -> None: ...

class CapabilityLimitV1(_message.Message):
    __slots__ = ("limit_key", "limit_value")
    LIMIT_KEY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_VALUE_FIELD_NUMBER: _ClassVar[int]
    limit_key: str
    limit_value: int
    def __init__(self, limit_key: _Optional[str] = ..., limit_value: _Optional[int] = ...) -> None: ...

class CapabilityPostureV1(_message.Message):
    __slots__ = ("capability_key", "state", "limits", "unavailable_reason_code")
    CAPABILITY_KEY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LIMITS_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    capability_key: str
    state: CapabilityStateV1
    limits: _containers.RepeatedCompositeFieldContainer[CapabilityLimitV1]
    unavailable_reason_code: str
    def __init__(self, capability_key: _Optional[str] = ..., state: _Optional[_Union[CapabilityStateV1, str]] = ..., limits: _Optional[_Iterable[_Union[CapabilityLimitV1, _Mapping]]] = ..., unavailable_reason_code: _Optional[str] = ...) -> None: ...

class AgenticEvaluationCapabilitiesV1(_message.Message):
    __slots__ = ("capability_set_version", "postures", "checked_at")
    CAPABILITY_SET_VERSION_FIELD_NUMBER: _ClassVar[int]
    POSTURES_FIELD_NUMBER: _ClassVar[int]
    CHECKED_AT_FIELD_NUMBER: _ClassVar[int]
    capability_set_version: int
    postures: _containers.RepeatedCompositeFieldContainer[CapabilityPostureV1]
    checked_at: _timestamp_pb2.Timestamp
    def __init__(self, capability_set_version: _Optional[int] = ..., postures: _Optional[_Iterable[_Union[CapabilityPostureV1, _Mapping]]] = ..., checked_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CostAmountV1(_message.Message):
    __slots__ = ("amount_micros", "currency_code")
    AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    amount_micros: int
    currency_code: str
    def __init__(self, amount_micros: _Optional[int] = ..., currency_code: _Optional[str] = ...) -> None: ...

class DatasetFieldMappingV1(_message.Message):
    __slots__ = ("source_field", "target_field")
    SOURCE_FIELD_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_FIELD_NUMBER: _ClassVar[int]
    source_field: str
    target_field: str
    def __init__(self, source_field: _Optional[str] = ..., target_field: _Optional[str] = ...) -> None: ...

class CohortNormalizationPolicyV1(_message.Message):
    __slots__ = ("mode", "weight_floor")
    MODE_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FLOOR_FIELD_NUMBER: _ClassVar[int]
    mode: CohortNormalizationModeV1
    weight_floor: float
    def __init__(self, mode: _Optional[_Union[CohortNormalizationModeV1, str]] = ..., weight_floor: _Optional[float] = ...) -> None: ...

class EvaluationCohortSpecV1(_message.Message):
    __slots__ = ("cohort_key", "label", "dataset_collection_id", "dataset_version_id", "weight", "field_mappings", "normalization")
    COHORT_KEY_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    FIELD_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    NORMALIZATION_FIELD_NUMBER: _ClassVar[int]
    cohort_key: str
    label: str
    dataset_collection_id: str
    dataset_version_id: str
    weight: float
    field_mappings: _containers.RepeatedCompositeFieldContainer[DatasetFieldMappingV1]
    normalization: CohortNormalizationPolicyV1
    def __init__(self, cohort_key: _Optional[str] = ..., label: _Optional[str] = ..., dataset_collection_id: _Optional[str] = ..., dataset_version_id: _Optional[str] = ..., weight: _Optional[float] = ..., field_mappings: _Optional[_Iterable[_Union[DatasetFieldMappingV1, _Mapping]]] = ..., normalization: _Optional[_Union[CohortNormalizationPolicyV1, _Mapping]] = ...) -> None: ...

class RecordedOutputCandidateV1(_message.Message):
    __slots__ = ("dataset_field", "recorded_run_id")
    DATASET_FIELD_FIELD_NUMBER: _ClassVar[int]
    RECORDED_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    dataset_field: str
    recorded_run_id: str
    def __init__(self, dataset_field: _Optional[str] = ..., recorded_run_id: _Optional[str] = ...) -> None: ...

class ProviderPromptCandidateV1(_message.Message):
    __slots__ = ("model", "prompt_template_id", "prompt_version_id", "request_settings", "provider_endpoint_ref")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ENDPOINT_REF_FIELD_NUMBER: _ClassVar[int]
    model: _agentic_pb2.ProviderModelRefV1
    prompt_template_id: str
    prompt_version_id: str
    request_settings: _agentic_pb2.ProviderRequestSettingsV1
    provider_endpoint_ref: str
    def __init__(self, model: _Optional[_Union[_agentic_pb2.ProviderModelRefV1, _Mapping]] = ..., prompt_template_id: _Optional[str] = ..., prompt_version_id: _Optional[str] = ..., request_settings: _Optional[_Union[_agentic_pb2.ProviderRequestSettingsV1, _Mapping]] = ..., provider_endpoint_ref: _Optional[str] = ...) -> None: ...

class HttpJsonEndpointCandidateV1(_message.Message):
    __slots__ = ("endpoint_url", "http_method", "auth_credential_ref")
    ENDPOINT_URL_FIELD_NUMBER: _ClassVar[int]
    HTTP_METHOD_FIELD_NUMBER: _ClassVar[int]
    AUTH_CREDENTIAL_REF_FIELD_NUMBER: _ClassVar[int]
    endpoint_url: str
    http_method: str
    auth_credential_ref: str
    def __init__(self, endpoint_url: _Optional[str] = ..., http_method: _Optional[str] = ..., auth_credential_ref: _Optional[str] = ...) -> None: ...

class ExperimentTargetRefCandidateV1(_message.Message):
    __slots__ = ("experiment_target_id",)
    EXPERIMENT_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    experiment_target_id: str
    def __init__(self, experiment_target_id: _Optional[str] = ...) -> None: ...

class AgentReleaseRevisionCandidateV1(_message.Message):
    __slots__ = ("release_revision_id", "agent_endpoint_id")
    RELEASE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    release_revision_id: str
    agent_endpoint_id: str
    def __init__(self, release_revision_id: _Optional[str] = ..., agent_endpoint_id: _Optional[str] = ...) -> None: ...

class ExternalExecutionLeasePolicyV1(_message.Message):
    __slots__ = ("lease_ttl_seconds", "max_renewals", "max_in_flight")
    LEASE_TTL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MAX_RENEWALS_FIELD_NUMBER: _ClassVar[int]
    MAX_IN_FLIGHT_FIELD_NUMBER: _ClassVar[int]
    lease_ttl_seconds: int
    max_renewals: int
    max_in_flight: int
    def __init__(self, lease_ttl_seconds: _Optional[int] = ..., max_renewals: _Optional[int] = ..., max_in_flight: _Optional[int] = ...) -> None: ...

class ExternallyExecutedCandidateV1(_message.Message):
    __slots__ = ("runtime_key", "lease_policy", "submission_deadline_seconds", "expected_sdk_contract_version")
    RUNTIME_KEY_FIELD_NUMBER: _ClassVar[int]
    LEASE_POLICY_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_DEADLINE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SDK_CONTRACT_VERSION_FIELD_NUMBER: _ClassVar[int]
    runtime_key: str
    lease_policy: ExternalExecutionLeasePolicyV1
    submission_deadline_seconds: int
    expected_sdk_contract_version: str
    def __init__(self, runtime_key: _Optional[str] = ..., lease_policy: _Optional[_Union[ExternalExecutionLeasePolicyV1, _Mapping]] = ..., submission_deadline_seconds: _Optional[int] = ..., expected_sdk_contract_version: _Optional[str] = ...) -> None: ...

class ConversationTerminationPolicyV1(_message.Message):
    __slots__ = ("kind", "max_idle_turns")
    KIND_FIELD_NUMBER: _ClassVar[int]
    MAX_IDLE_TURNS_FIELD_NUMBER: _ClassVar[int]
    kind: ConversationTerminationKindV1
    max_idle_turns: int
    def __init__(self, kind: _Optional[_Union[ConversationTerminationKindV1, str]] = ..., max_idle_turns: _Optional[int] = ...) -> None: ...

class ConversationSimulationCandidateV1(_message.Message):
    __slots__ = ("simulated_user_spec_ref", "max_turns", "termination")
    SIMULATED_USER_SPEC_REF_FIELD_NUMBER: _ClassVar[int]
    MAX_TURNS_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_FIELD_NUMBER: _ClassVar[int]
    simulated_user_spec_ref: str
    max_turns: int
    termination: ConversationTerminationPolicyV1
    def __init__(self, simulated_user_spec_ref: _Optional[str] = ..., max_turns: _Optional[int] = ..., termination: _Optional[_Union[ConversationTerminationPolicyV1, _Mapping]] = ...) -> None: ...

class EvaluationRequestMappingV1(_message.Message):
    __slots__ = ("field_mappings",)
    FIELD_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    field_mappings: _containers.RepeatedCompositeFieldContainer[DatasetFieldMappingV1]
    def __init__(self, field_mappings: _Optional[_Iterable[_Union[DatasetFieldMappingV1, _Mapping]]] = ...) -> None: ...

class EvaluationResponseMappingV1(_message.Message):
    __slots__ = ("output_field", "error_field")
    OUTPUT_FIELD_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_FIELD_NUMBER: _ClassVar[int]
    output_field: str
    error_field: str
    def __init__(self, output_field: _Optional[str] = ..., error_field: _Optional[str] = ...) -> None: ...

class EvaluationTimeoutRetryPolicyV1(_message.Message):
    __slots__ = ("request_timeout_seconds", "max_attempts", "retry_backoff_seconds")
    REQUEST_TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    RETRY_BACKOFF_SECONDS_FIELD_NUMBER: _ClassVar[int]
    request_timeout_seconds: int
    max_attempts: int
    retry_backoff_seconds: int
    def __init__(self, request_timeout_seconds: _Optional[int] = ..., max_attempts: _Optional[int] = ..., retry_backoff_seconds: _Optional[int] = ...) -> None: ...

class ProviderCapabilitySnapshotV1(_message.Message):
    __slots__ = ("postures",)
    POSTURES_FIELD_NUMBER: _ClassVar[int]
    postures: _containers.RepeatedCompositeFieldContainer[CapabilityPostureV1]
    def __init__(self, postures: _Optional[_Iterable[_Union[CapabilityPostureV1, _Mapping]]] = ...) -> None: ...

class CandidateSideEffectAttestationV1(_message.Message):
    __slots__ = ("posture", "attested_by_principal_id", "attested_at", "attestation_note")
    POSTURE_FIELD_NUMBER: _ClassVar[int]
    ATTESTED_BY_PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    ATTESTED_AT_FIELD_NUMBER: _ClassVar[int]
    ATTESTATION_NOTE_FIELD_NUMBER: _ClassVar[int]
    posture: SideEffectPostureV1
    attested_by_principal_id: str
    attested_at: _timestamp_pb2.Timestamp
    attestation_note: str
    def __init__(self, posture: _Optional[_Union[SideEffectPostureV1, str]] = ..., attested_by_principal_id: _Optional[str] = ..., attested_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., attestation_note: _Optional[str] = ...) -> None: ...

class EvaluationCandidateV1(_message.Message):
    __slots__ = ("candidate_key", "display_label", "kind", "recorded_output", "provider_prompt", "http_json_endpoint", "experiment_target_ref", "agent_release_revision", "externally_executed", "conversation_simulation", "credential_ref", "request_mapping", "response_mapping", "timeout_retry", "provider_capabilities", "source_release_revision_id", "side_effects", "is_reference_candidate")
    CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_LABEL_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    RECORDED_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_PROMPT_FIELD_NUMBER: _ClassVar[int]
    HTTP_JSON_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_TARGET_REF_FIELD_NUMBER: _ClassVar[int]
    AGENT_RELEASE_REVISION_FIELD_NUMBER: _ClassVar[int]
    EXTERNALLY_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_SIMULATION_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_REF_FIELD_NUMBER: _ClassVar[int]
    REQUEST_MAPPING_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_MAPPING_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_RETRY_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_RELEASE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    SIDE_EFFECTS_FIELD_NUMBER: _ClassVar[int]
    IS_REFERENCE_CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    candidate_key: str
    display_label: str
    kind: EvaluationCandidateKindV1
    recorded_output: RecordedOutputCandidateV1
    provider_prompt: ProviderPromptCandidateV1
    http_json_endpoint: HttpJsonEndpointCandidateV1
    experiment_target_ref: ExperimentTargetRefCandidateV1
    agent_release_revision: AgentReleaseRevisionCandidateV1
    externally_executed: ExternallyExecutedCandidateV1
    conversation_simulation: ConversationSimulationCandidateV1
    credential_ref: str
    request_mapping: EvaluationRequestMappingV1
    response_mapping: EvaluationResponseMappingV1
    timeout_retry: EvaluationTimeoutRetryPolicyV1
    provider_capabilities: ProviderCapabilitySnapshotV1
    source_release_revision_id: str
    side_effects: CandidateSideEffectAttestationV1
    is_reference_candidate: bool
    def __init__(self, candidate_key: _Optional[str] = ..., display_label: _Optional[str] = ..., kind: _Optional[_Union[EvaluationCandidateKindV1, str]] = ..., recorded_output: _Optional[_Union[RecordedOutputCandidateV1, _Mapping]] = ..., provider_prompt: _Optional[_Union[ProviderPromptCandidateV1, _Mapping]] = ..., http_json_endpoint: _Optional[_Union[HttpJsonEndpointCandidateV1, _Mapping]] = ..., experiment_target_ref: _Optional[_Union[ExperimentTargetRefCandidateV1, _Mapping]] = ..., agent_release_revision: _Optional[_Union[AgentReleaseRevisionCandidateV1, _Mapping]] = ..., externally_executed: _Optional[_Union[ExternallyExecutedCandidateV1, _Mapping]] = ..., conversation_simulation: _Optional[_Union[ConversationSimulationCandidateV1, _Mapping]] = ..., credential_ref: _Optional[str] = ..., request_mapping: _Optional[_Union[EvaluationRequestMappingV1, _Mapping]] = ..., response_mapping: _Optional[_Union[EvaluationResponseMappingV1, _Mapping]] = ..., timeout_retry: _Optional[_Union[EvaluationTimeoutRetryPolicyV1, _Mapping]] = ..., provider_capabilities: _Optional[_Union[ProviderCapabilitySnapshotV1, _Mapping]] = ..., source_release_revision_id: _Optional[str] = ..., side_effects: _Optional[_Union[CandidateSideEffectAttestationV1, _Mapping]] = ..., is_reference_candidate: _Optional[bool] = ...) -> None: ...

class EvaluationScorerSelectionV1(_message.Message):
    __slots__ = ("score_config_id", "weight", "is_blocking_gate")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    IS_BLOCKING_GATE_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    weight: float
    is_blocking_gate: bool
    def __init__(self, score_config_id: _Optional[str] = ..., weight: _Optional[float] = ..., is_blocking_gate: _Optional[bool] = ...) -> None: ...

class EvaluationScorerTargetV1(_message.Message):
    __slots__ = ("kind", "scorer_suite_id", "scorers")
    KIND_FIELD_NUMBER: _ClassVar[int]
    SCORER_SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    SCORERS_FIELD_NUMBER: _ClassVar[int]
    kind: EvaluationScorerTargetKindV1
    scorer_suite_id: str
    scorers: _containers.RepeatedCompositeFieldContainer[EvaluationScorerSelectionV1]
    def __init__(self, kind: _Optional[_Union[EvaluationScorerTargetKindV1, str]] = ..., scorer_suite_id: _Optional[str] = ..., scorers: _Optional[_Iterable[_Union[EvaluationScorerSelectionV1, _Mapping]]] = ...) -> None: ...

class EvaluationScorerSuiteMemberV1(_message.Message):
    __slots__ = ("score_config_id", "config_key", "weight", "is_blocking_gate")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    IS_BLOCKING_GATE_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    config_key: str
    weight: float
    is_blocking_gate: bool
    def __init__(self, score_config_id: _Optional[str] = ..., config_key: _Optional[str] = ..., weight: _Optional[float] = ..., is_blocking_gate: _Optional[bool] = ...) -> None: ...

class EvaluationScorerSuiteV1(_message.Message):
    __slots__ = ("scorer_suite_id", "suite_key", "name", "version_discriminator", "combine_rule", "members", "created_at")
    SCORER_SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    SUITE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_DISCRIMINATOR_FIELD_NUMBER: _ClassVar[int]
    COMBINE_RULE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    scorer_suite_id: str
    suite_key: str
    name: str
    version_discriminator: str
    combine_rule: EvaluationScorerSuiteCombineRuleV1
    members: _containers.RepeatedCompositeFieldContainer[EvaluationScorerSuiteMemberV1]
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, scorer_suite_id: _Optional[str] = ..., suite_key: _Optional[str] = ..., name: _Optional[str] = ..., version_discriminator: _Optional[str] = ..., combine_rule: _Optional[_Union[EvaluationScorerSuiteCombineRuleV1, str]] = ..., members: _Optional[_Iterable[_Union[EvaluationScorerSuiteMemberV1, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EvaluationScorerSuiteSnapshotV1(_message.Message):
    __slots__ = ("scorer_suite_id", "suite_key", "version_discriminator", "combine_rule", "members")
    SCORER_SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    SUITE_KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_DISCRIMINATOR_FIELD_NUMBER: _ClassVar[int]
    COMBINE_RULE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    scorer_suite_id: str
    suite_key: str
    version_discriminator: str
    combine_rule: EvaluationScorerSuiteCombineRuleV1
    members: _containers.RepeatedCompositeFieldContainer[EvaluationScorerSuiteMemberV1]
    def __init__(self, scorer_suite_id: _Optional[str] = ..., suite_key: _Optional[str] = ..., version_discriminator: _Optional[str] = ..., combine_rule: _Optional[_Union[EvaluationScorerSuiteCombineRuleV1, str]] = ..., members: _Optional[_Iterable[_Union[EvaluationScorerSuiteMemberV1, _Mapping]]] = ...) -> None: ...

class EvaluationScorerSuiteRollupV1(_message.Message):
    __slots__ = ("scorer_suite_id", "suite_key", "version_discriminator", "combine_rule", "member_score_config_id", "gates_passed", "gates_availability", "failed_gate_config_key", "weighted_mean_score", "weighted_mean_availability", "verdict", "freshness")
    SCORER_SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    SUITE_KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_DISCRIMINATOR_FIELD_NUMBER: _ClassVar[int]
    COMBINE_RULE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    GATES_PASSED_FIELD_NUMBER: _ClassVar[int]
    GATES_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    FAILED_GATE_CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    WEIGHTED_MEAN_SCORE_FIELD_NUMBER: _ClassVar[int]
    WEIGHTED_MEAN_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    scorer_suite_id: str
    suite_key: str
    version_discriminator: str
    combine_rule: EvaluationScorerSuiteCombineRuleV1
    member_score_config_id: _containers.RepeatedScalarFieldContainer[str]
    gates_passed: bool
    gates_availability: MetricAvailabilityV1
    failed_gate_config_key: _containers.RepeatedScalarFieldContainer[str]
    weighted_mean_score: float
    weighted_mean_availability: MetricAvailabilityV1
    verdict: EvaluationVerdictV1
    freshness: EvaluationFreshnessV1
    def __init__(self, scorer_suite_id: _Optional[str] = ..., suite_key: _Optional[str] = ..., version_discriminator: _Optional[str] = ..., combine_rule: _Optional[_Union[EvaluationScorerSuiteCombineRuleV1, str]] = ..., member_score_config_id: _Optional[_Iterable[str]] = ..., gates_passed: _Optional[bool] = ..., gates_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., failed_gate_config_key: _Optional[_Iterable[str]] = ..., weighted_mean_score: _Optional[float] = ..., weighted_mean_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., verdict: _Optional[_Union[EvaluationVerdictV1, str]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class EvaluationScorerSuiteCellV1(_message.Message):
    __slots__ = ("candidate_key", "scorer_suite_id", "suite_key", "gates_passed", "failed_gate_config_key", "weighted_mean_score", "weighted_mean_availability", "verdict", "member_cell_count")
    CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    SCORER_SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    SUITE_KEY_FIELD_NUMBER: _ClassVar[int]
    GATES_PASSED_FIELD_NUMBER: _ClassVar[int]
    FAILED_GATE_CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    WEIGHTED_MEAN_SCORE_FIELD_NUMBER: _ClassVar[int]
    WEIGHTED_MEAN_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    MEMBER_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    candidate_key: str
    scorer_suite_id: str
    suite_key: str
    gates_passed: bool
    failed_gate_config_key: _containers.RepeatedScalarFieldContainer[str]
    weighted_mean_score: float
    weighted_mean_availability: MetricAvailabilityV1
    verdict: EvaluationVerdictV1
    member_cell_count: int
    def __init__(self, candidate_key: _Optional[str] = ..., scorer_suite_id: _Optional[str] = ..., suite_key: _Optional[str] = ..., gates_passed: _Optional[bool] = ..., failed_gate_config_key: _Optional[_Iterable[str]] = ..., weighted_mean_score: _Optional[float] = ..., weighted_mean_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., verdict: _Optional[_Union[EvaluationVerdictV1, str]] = ..., member_cell_count: _Optional[int] = ...) -> None: ...

class EvaluationExecutionPolicyV1(_message.Message):
    __slots__ = ("max_concurrency", "per_candidate_timeout_seconds", "max_attempts", "retry_backoff_seconds")
    MAX_CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    PER_CANDIDATE_TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    RETRY_BACKOFF_SECONDS_FIELD_NUMBER: _ClassVar[int]
    max_concurrency: int
    per_candidate_timeout_seconds: int
    max_attempts: int
    retry_backoff_seconds: int
    def __init__(self, max_concurrency: _Optional[int] = ..., per_candidate_timeout_seconds: _Optional[int] = ..., max_attempts: _Optional[int] = ..., retry_backoff_seconds: _Optional[int] = ...) -> None: ...

class EvaluationBudgetV1(_message.Message):
    __slots__ = ("candidate_budget", "evaluator_budget", "total_budget", "max_execution_count")
    CANDIDATE_BUDGET_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_BUDGET_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BUDGET_FIELD_NUMBER: _ClassVar[int]
    MAX_EXECUTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    candidate_budget: CostAmountV1
    evaluator_budget: CostAmountV1
    total_budget: CostAmountV1
    max_execution_count: int
    def __init__(self, candidate_budget: _Optional[_Union[CostAmountV1, _Mapping]] = ..., evaluator_budget: _Optional[_Union[CostAmountV1, _Mapping]] = ..., total_budget: _Optional[_Union[CostAmountV1, _Mapping]] = ..., max_execution_count: _Optional[int] = ...) -> None: ...

class EvaluationDecisionRuleV1(_message.Message):
    __slots__ = ("kind", "metric_key", "threshold", "cost_threshold")
    KIND_FIELD_NUMBER: _ClassVar[int]
    METRIC_KEY_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    COST_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    kind: EvaluationDecisionRuleKindV1
    metric_key: str
    threshold: float
    cost_threshold: CostAmountV1
    def __init__(self, kind: _Optional[_Union[EvaluationDecisionRuleKindV1, str]] = ..., metric_key: _Optional[str] = ..., threshold: _Optional[float] = ..., cost_threshold: _Optional[_Union[CostAmountV1, _Mapping]] = ...) -> None: ...

class EvaluationDecisionPolicyV1(_message.Message):
    __slots__ = ("rules", "reference_candidate_key", "minimum_confidence")
    RULES_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[EvaluationDecisionRuleV1]
    reference_candidate_key: str
    minimum_confidence: float
    def __init__(self, rules: _Optional[_Iterable[_Union[EvaluationDecisionRuleV1, _Mapping]]] = ..., reference_candidate_key: _Optional[str] = ..., minimum_confidence: _Optional[float] = ...) -> None: ...

class EvaluationReviewSamplingPolicyV1(_message.Message):
    __slots__ = ("sample_rate", "max_sampled_cases", "reviewers_per_case")
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    MAX_SAMPLED_CASES_FIELD_NUMBER: _ClassVar[int]
    REVIEWERS_PER_CASE_FIELD_NUMBER: _ClassVar[int]
    sample_rate: float
    max_sampled_cases: int
    reviewers_per_case: int
    def __init__(self, sample_rate: _Optional[float] = ..., max_sampled_cases: _Optional[int] = ..., reviewers_per_case: _Optional[int] = ...) -> None: ...

class EvaluationHumanReviewPolicyV1(_message.Message):
    __slots__ = ("enabled", "sampling", "rubric_score_config_id")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SAMPLING_FIELD_NUMBER: _ClassVar[int]
    RUBRIC_SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    sampling: EvaluationReviewSamplingPolicyV1
    rubric_score_config_id: str
    def __init__(self, enabled: _Optional[bool] = ..., sampling: _Optional[_Union[EvaluationReviewSamplingPolicyV1, _Mapping]] = ..., rubric_score_config_id: _Optional[str] = ...) -> None: ...

class EvaluationDefinitionDraftV1(_message.Message):
    __slots__ = ("display_name", "description", "cohorts", "candidates", "scorer_target", "trials", "execution_policy", "budget", "decision_policy", "launch_mode", "human_review_policy", "metadata", "trials_source")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COHORTS_FIELD_NUMBER: _ClassVar[int]
    CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    SCORER_TARGET_FIELD_NUMBER: _ClassVar[int]
    TRIALS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    BUDGET_FIELD_NUMBER: _ClassVar[int]
    DECISION_POLICY_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_MODE_FIELD_NUMBER: _ClassVar[int]
    HUMAN_REVIEW_POLICY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TRIALS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    description: str
    cohorts: _containers.RepeatedCompositeFieldContainer[EvaluationCohortSpecV1]
    candidates: _containers.RepeatedCompositeFieldContainer[EvaluationCandidateV1]
    scorer_target: EvaluationScorerTargetV1
    trials: int
    execution_policy: EvaluationExecutionPolicyV1
    budget: EvaluationBudgetV1
    decision_policy: EvaluationDecisionPolicyV1
    launch_mode: EvaluationLaunchModeV1
    human_review_policy: EvaluationHumanReviewPolicyV1
    metadata: _containers.RepeatedCompositeFieldContainer[MetadataEntryV1]
    trials_source: EvaluationTrialsSourceV1
    def __init__(self, display_name: _Optional[str] = ..., description: _Optional[str] = ..., cohorts: _Optional[_Iterable[_Union[EvaluationCohortSpecV1, _Mapping]]] = ..., candidates: _Optional[_Iterable[_Union[EvaluationCandidateV1, _Mapping]]] = ..., scorer_target: _Optional[_Union[EvaluationScorerTargetV1, _Mapping]] = ..., trials: _Optional[int] = ..., execution_policy: _Optional[_Union[EvaluationExecutionPolicyV1, _Mapping]] = ..., budget: _Optional[_Union[EvaluationBudgetV1, _Mapping]] = ..., decision_policy: _Optional[_Union[EvaluationDecisionPolicyV1, _Mapping]] = ..., launch_mode: _Optional[_Union[EvaluationLaunchModeV1, str]] = ..., human_review_policy: _Optional[_Union[EvaluationHumanReviewPolicyV1, _Mapping]] = ..., metadata: _Optional[_Iterable[_Union[MetadataEntryV1, _Mapping]]] = ..., trials_source: _Optional[_Union[EvaluationTrialsSourceV1, str]] = ...) -> None: ...

class EvaluationRunSummaryRefV1(_message.Message):
    __slots__ = ("evaluation_run_id", "definition_revision_id", "state", "created_at", "finished_at", "decision_summary")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    DECISION_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    definition_revision_id: str
    state: EvaluationRunStateV1
    created_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    decision_summary: str
    def __init__(self, evaluation_run_id: _Optional[str] = ..., definition_revision_id: _Optional[str] = ..., state: _Optional[_Union[EvaluationRunStateV1, str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., decision_summary: _Optional[str] = ...) -> None: ...

class EvaluationDefinitionV1(_message.Message):
    __slots__ = ("definition_id", "tenant_id", "org_id", "definition_key", "display_name", "description", "current_revision_id", "revision_number", "state", "metadata", "created_by", "created_at", "updated_at", "latest_run", "latest_run_availability", "run_count", "allowed_actions")
    DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_KEY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    LATEST_RUN_FIELD_NUMBER: _ClassVar[int]
    LATEST_RUN_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    definition_id: str
    tenant_id: str
    org_id: str
    definition_key: str
    display_name: str
    description: str
    current_revision_id: str
    revision_number: int
    state: EvaluationDefinitionStateV1
    metadata: _containers.RepeatedCompositeFieldContainer[MetadataEntryV1]
    created_by: PrincipalRefV1
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    latest_run: EvaluationRunSummaryRefV1
    latest_run_availability: MetricAvailabilityV1
    run_count: int
    allowed_actions: _containers.RepeatedCompositeFieldContainer[AllowedActionV1]
    def __init__(self, definition_id: _Optional[str] = ..., tenant_id: _Optional[str] = ..., org_id: _Optional[str] = ..., definition_key: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., current_revision_id: _Optional[str] = ..., revision_number: _Optional[int] = ..., state: _Optional[_Union[EvaluationDefinitionStateV1, str]] = ..., metadata: _Optional[_Iterable[_Union[MetadataEntryV1, _Mapping]]] = ..., created_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., latest_run: _Optional[_Union[EvaluationRunSummaryRefV1, _Mapping]] = ..., latest_run_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., run_count: _Optional[int] = ..., allowed_actions: _Optional[_Iterable[_Union[AllowedActionV1, _Mapping]]] = ...) -> None: ...

class EvaluationDefinitionRevisionV1(_message.Message):
    __slots__ = ("revision_id", "definition_id", "tenant_id", "org_id", "revision_number", "content_digest", "draft", "draft_schema_version", "created_by", "created_at", "change_summary", "source_revision_id")
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DIGEST_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    DRAFT_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CHANGE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    revision_id: str
    definition_id: str
    tenant_id: str
    org_id: str
    revision_number: int
    content_digest: str
    draft: EvaluationDefinitionDraftV1
    draft_schema_version: int
    created_by: PrincipalRefV1
    created_at: _timestamp_pb2.Timestamp
    change_summary: str
    source_revision_id: str
    def __init__(self, revision_id: _Optional[str] = ..., definition_id: _Optional[str] = ..., tenant_id: _Optional[str] = ..., org_id: _Optional[str] = ..., revision_number: _Optional[int] = ..., content_digest: _Optional[str] = ..., draft: _Optional[_Union[EvaluationDefinitionDraftV1, _Mapping]] = ..., draft_schema_version: _Optional[int] = ..., created_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., change_summary: _Optional[str] = ..., source_revision_id: _Optional[str] = ...) -> None: ...

class EvaluationDefinitionSummaryV1(_message.Message):
    __slots__ = ("definition_id", "tenant_id", "org_id", "definition_key", "display_name", "description", "state", "current_revision_id", "revision_number", "created_by", "created_at", "updated_at", "latest_run", "latest_run_availability", "run_count", "allowed_actions", "freshness")
    DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_KEY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    LATEST_RUN_FIELD_NUMBER: _ClassVar[int]
    LATEST_RUN_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    definition_id: str
    tenant_id: str
    org_id: str
    definition_key: str
    display_name: str
    description: str
    state: EvaluationDefinitionStateV1
    current_revision_id: str
    revision_number: int
    created_by: PrincipalRefV1
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    latest_run: EvaluationRunSummaryRefV1
    latest_run_availability: MetricAvailabilityV1
    run_count: int
    allowed_actions: _containers.RepeatedCompositeFieldContainer[AllowedActionV1]
    freshness: EvaluationFreshnessV1
    def __init__(self, definition_id: _Optional[str] = ..., tenant_id: _Optional[str] = ..., org_id: _Optional[str] = ..., definition_key: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., state: _Optional[_Union[EvaluationDefinitionStateV1, str]] = ..., current_revision_id: _Optional[str] = ..., revision_number: _Optional[int] = ..., created_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., latest_run: _Optional[_Union[EvaluationRunSummaryRefV1, _Mapping]] = ..., latest_run_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., run_count: _Optional[int] = ..., allowed_actions: _Optional[_Iterable[_Union[AllowedActionV1, _Mapping]]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class CreateEvaluationDefinitionRequest(_message.Message):
    __slots__ = ("definition_key", "draft", "change_summary")
    DEFINITION_KEY_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    CHANGE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    definition_key: str
    draft: EvaluationDefinitionDraftV1
    change_summary: str
    def __init__(self, definition_key: _Optional[str] = ..., draft: _Optional[_Union[EvaluationDefinitionDraftV1, _Mapping]] = ..., change_summary: _Optional[str] = ...) -> None: ...

class CreateEvaluationDefinitionResponse(_message.Message):
    __slots__ = ("definition", "revision")
    DEFINITION_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    definition: EvaluationDefinitionV1
    revision: EvaluationDefinitionRevisionV1
    def __init__(self, definition: _Optional[_Union[EvaluationDefinitionV1, _Mapping]] = ..., revision: _Optional[_Union[EvaluationDefinitionRevisionV1, _Mapping]] = ...) -> None: ...

class EvaluationDefinitionConflictV1(_message.Message):
    __slots__ = ("expected_revision_number", "current_revision_number", "current_revision_id", "changed_sections", "server_revision")
    EXPECTED_REVISION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CURRENT_REVISION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CURRENT_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    CHANGED_SECTIONS_FIELD_NUMBER: _ClassVar[int]
    SERVER_REVISION_FIELD_NUMBER: _ClassVar[int]
    expected_revision_number: int
    current_revision_number: int
    current_revision_id: str
    changed_sections: _containers.RepeatedScalarFieldContainer[EvaluationDefinitionConflictSectionV1]
    server_revision: EvaluationDefinitionRevisionV1
    def __init__(self, expected_revision_number: _Optional[int] = ..., current_revision_number: _Optional[int] = ..., current_revision_id: _Optional[str] = ..., changed_sections: _Optional[_Iterable[_Union[EvaluationDefinitionConflictSectionV1, str]]] = ..., server_revision: _Optional[_Union[EvaluationDefinitionRevisionV1, _Mapping]] = ...) -> None: ...

class UpdateEvaluationDefinitionRequest(_message.Message):
    __slots__ = ("definition_id", "expected_revision_number", "draft", "change_summary", "state")
    DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_REVISION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    CHANGE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    definition_id: str
    expected_revision_number: int
    draft: EvaluationDefinitionDraftV1
    change_summary: str
    state: EvaluationDefinitionStateV1
    def __init__(self, definition_id: _Optional[str] = ..., expected_revision_number: _Optional[int] = ..., draft: _Optional[_Union[EvaluationDefinitionDraftV1, _Mapping]] = ..., change_summary: _Optional[str] = ..., state: _Optional[_Union[EvaluationDefinitionStateV1, str]] = ...) -> None: ...

class UpdateEvaluationDefinitionResponse(_message.Message):
    __slots__ = ("definition", "revision", "conflict")
    DEFINITION_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_FIELD_NUMBER: _ClassVar[int]
    definition: EvaluationDefinitionV1
    revision: EvaluationDefinitionRevisionV1
    conflict: EvaluationDefinitionConflictV1
    def __init__(self, definition: _Optional[_Union[EvaluationDefinitionV1, _Mapping]] = ..., revision: _Optional[_Union[EvaluationDefinitionRevisionV1, _Mapping]] = ..., conflict: _Optional[_Union[EvaluationDefinitionConflictV1, _Mapping]] = ...) -> None: ...

class GetEvaluationDefinitionRequest(_message.Message):
    __slots__ = ("definition_id", "revision_id")
    DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    definition_id: str
    revision_id: str
    def __init__(self, definition_id: _Optional[str] = ..., revision_id: _Optional[str] = ...) -> None: ...

class GetEvaluationDefinitionResponse(_message.Message):
    __slots__ = ("definition", "revision", "freshness")
    DEFINITION_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    definition: EvaluationDefinitionV1
    revision: EvaluationDefinitionRevisionV1
    freshness: EvaluationFreshnessV1
    def __init__(self, definition: _Optional[_Union[EvaluationDefinitionV1, _Mapping]] = ..., revision: _Optional[_Union[EvaluationDefinitionRevisionV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class ListEvaluationDefinitionsRequest(_message.Message):
    __slots__ = ("page", "state_filter", "name_contains", "sort_key", "sort_direction")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    STATE_FILTER_FIELD_NUMBER: _ClassVar[int]
    NAME_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    SORT_KEY_FIELD_NUMBER: _ClassVar[int]
    SORT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    page: _common_pb2.PageRequestV1
    state_filter: EvaluationDefinitionStateV1
    name_contains: str
    sort_key: EvaluationDefinitionSortKeyV1
    sort_direction: _common_pb2.SortDirectionV1
    def __init__(self, page: _Optional[_Union[_common_pb2.PageRequestV1, _Mapping]] = ..., state_filter: _Optional[_Union[EvaluationDefinitionStateV1, str]] = ..., name_contains: _Optional[str] = ..., sort_key: _Optional[_Union[EvaluationDefinitionSortKeyV1, str]] = ..., sort_direction: _Optional[_Union[_common_pb2.SortDirectionV1, str]] = ...) -> None: ...

class ListEvaluationDefinitionsResponse(_message.Message):
    __slots__ = ("definitions", "page", "freshness", "capabilities", "resync")
    DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    RESYNC_FIELD_NUMBER: _ClassVar[int]
    definitions: _containers.RepeatedCompositeFieldContainer[EvaluationDefinitionSummaryV1]
    page: _common_pb2.PageResponseV1
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    resync: EvaluationCursorResyncV1
    def __init__(self, definitions: _Optional[_Iterable[_Union[EvaluationDefinitionSummaryV1, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponseV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., resync: _Optional[_Union[EvaluationCursorResyncV1, _Mapping]] = ...) -> None: ...

class NewDraftEntryV1(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EditDefinitionEntryV1(_message.Message):
    __slots__ = ("evaluation_id",)
    EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    evaluation_id: str
    def __init__(self, evaluation_id: _Optional[str] = ...) -> None: ...

class DuplicateDefinitionEntryV1(_message.Message):
    __slots__ = ("evaluation_id",)
    EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    evaluation_id: str
    def __init__(self, evaluation_id: _Optional[str] = ...) -> None: ...

class RerunDefinitionEntryV1(_message.Message):
    __slots__ = ("evaluation_id", "run_id")
    EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    evaluation_id: str
    run_id: str
    def __init__(self, evaluation_id: _Optional[str] = ..., run_id: _Optional[str] = ...) -> None: ...

class FromDatasetEntryV1(_message.Message):
    __slots__ = ("dataset_version_id",)
    DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    dataset_version_id: str
    def __init__(self, dataset_version_id: _Optional[str] = ...) -> None: ...

class FromProductionEvidenceEntryV1(_message.Message):
    __slots__ = ("evidence_selector",)
    EVIDENCE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    evidence_selector: str
    def __init__(self, evidence_selector: _Optional[str] = ...) -> None: ...

class FromReleaseEntryV1(_message.Message):
    __slots__ = ("release_revision_id",)
    RELEASE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    release_revision_id: str
    def __init__(self, release_revision_id: _Optional[str] = ...) -> None: ...

class GetEvaluationBuilderContextRequest(_message.Message):
    __slots__ = ("new_draft", "edit_definition", "duplicate_definition", "rerun_definition", "from_dataset", "from_production", "from_release")
    NEW_DRAFT_FIELD_NUMBER: _ClassVar[int]
    EDIT_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    DUPLICATE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    RERUN_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    FROM_DATASET_FIELD_NUMBER: _ClassVar[int]
    FROM_PRODUCTION_FIELD_NUMBER: _ClassVar[int]
    FROM_RELEASE_FIELD_NUMBER: _ClassVar[int]
    new_draft: NewDraftEntryV1
    edit_definition: EditDefinitionEntryV1
    duplicate_definition: DuplicateDefinitionEntryV1
    rerun_definition: RerunDefinitionEntryV1
    from_dataset: FromDatasetEntryV1
    from_production: FromProductionEvidenceEntryV1
    from_release: FromReleaseEntryV1
    def __init__(self, new_draft: _Optional[_Union[NewDraftEntryV1, _Mapping]] = ..., edit_definition: _Optional[_Union[EditDefinitionEntryV1, _Mapping]] = ..., duplicate_definition: _Optional[_Union[DuplicateDefinitionEntryV1, _Mapping]] = ..., rerun_definition: _Optional[_Union[RerunDefinitionEntryV1, _Mapping]] = ..., from_dataset: _Optional[_Union[FromDatasetEntryV1, _Mapping]] = ..., from_production: _Optional[_Union[FromProductionEvidenceEntryV1, _Mapping]] = ..., from_release: _Optional[_Union[FromReleaseEntryV1, _Mapping]] = ...) -> None: ...

class EvaluationBuilderDatasetVersionOptionV1(_message.Message):
    __slots__ = ("dataset_version_id", "version_number", "label", "case_count", "case_count_availability", "schema_fingerprint", "schema_fingerprint_availability", "created_at", "is_pinned")
    DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CASE_COUNT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FINGERPRINT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_PINNED_FIELD_NUMBER: _ClassVar[int]
    dataset_version_id: str
    version_number: int
    label: str
    case_count: int
    case_count_availability: MetricAvailabilityV1
    schema_fingerprint: str
    schema_fingerprint_availability: MetricAvailabilityV1
    created_at: _timestamp_pb2.Timestamp
    is_pinned: bool
    def __init__(self, dataset_version_id: _Optional[str] = ..., version_number: _Optional[int] = ..., label: _Optional[str] = ..., case_count: _Optional[int] = ..., case_count_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., schema_fingerprint: _Optional[str] = ..., schema_fingerprint_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., is_pinned: _Optional[bool] = ...) -> None: ...

class EvaluationBuilderDatasetOptionV1(_message.Message):
    __slots__ = ("dataset_collection_id", "name", "description", "versions", "updated_at")
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    dataset_collection_id: str
    name: str
    description: str
    versions: _containers.RepeatedCompositeFieldContainer[EvaluationBuilderDatasetVersionOptionV1]
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, dataset_collection_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., versions: _Optional[_Iterable[_Union[EvaluationBuilderDatasetVersionOptionV1, _Mapping]]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EvaluationBuilderModelOptionV1(_message.Message):
    __slots__ = ("model", "provider", "display_label", "posture")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_LABEL_FIELD_NUMBER: _ClassVar[int]
    POSTURE_FIELD_NUMBER: _ClassVar[int]
    model: _agentic_pb2.ProviderModelRefV1
    provider: _agentic_pb2.ProviderNameV1
    display_label: str
    posture: CapabilityPostureV1
    def __init__(self, model: _Optional[_Union[_agentic_pb2.ProviderModelRefV1, _Mapping]] = ..., provider: _Optional[_Union[_agentic_pb2.ProviderNameV1, str]] = ..., display_label: _Optional[str] = ..., posture: _Optional[_Union[CapabilityPostureV1, _Mapping]] = ...) -> None: ...

class EvaluationBuilderCandidateSourcesV1(_message.Message):
    __slots__ = ("models", "agent_endpoints", "release_revisions", "recorded_outputs")
    MODELS_FIELD_NUMBER: _ClassVar[int]
    AGENT_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    RELEASE_REVISIONS_FIELD_NUMBER: _ClassVar[int]
    RECORDED_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[EvaluationBuilderModelOptionV1]
    agent_endpoints: CapabilityPostureV1
    release_revisions: CapabilityPostureV1
    recorded_outputs: CapabilityPostureV1
    def __init__(self, models: _Optional[_Iterable[_Union[EvaluationBuilderModelOptionV1, _Mapping]]] = ..., agent_endpoints: _Optional[_Union[CapabilityPostureV1, _Mapping]] = ..., release_revisions: _Optional[_Union[CapabilityPostureV1, _Mapping]] = ..., recorded_outputs: _Optional[_Union[CapabilityPostureV1, _Mapping]] = ...) -> None: ...

class EvaluationBuilderScorerChoiceV1(_message.Message):
    __slots__ = ("score_config_id", "config_key", "name", "description", "metric_name", "success_dimension", "compatible_subject_kinds", "is_archived", "kind")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    COMPATIBLE_SUBJECT_KINDS_FIELD_NUMBER: _ClassVar[int]
    IS_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    config_key: str
    name: str
    description: str
    metric_name: str
    success_dimension: str
    compatible_subject_kinds: _containers.RepeatedScalarFieldContainer[EvaluationSubjectKindV1]
    is_archived: bool
    kind: EvaluationScorerKindV1
    def __init__(self, score_config_id: _Optional[str] = ..., config_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., metric_name: _Optional[str] = ..., success_dimension: _Optional[str] = ..., compatible_subject_kinds: _Optional[_Iterable[_Union[EvaluationSubjectKindV1, str]]] = ..., is_archived: _Optional[bool] = ..., kind: _Optional[_Union[EvaluationScorerKindV1, str]] = ...) -> None: ...

class EvaluationBuilderRecommendedMeasureV1(_message.Message):
    __slots__ = ("score_config_id", "rationale", "assumptions", "is_blocking_gate_by_default")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    RATIONALE_FIELD_NUMBER: _ClassVar[int]
    ASSUMPTIONS_FIELD_NUMBER: _ClassVar[int]
    IS_BLOCKING_GATE_BY_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    rationale: str
    assumptions: _containers.RepeatedScalarFieldContainer[str]
    is_blocking_gate_by_default: bool
    def __init__(self, score_config_id: _Optional[str] = ..., rationale: _Optional[str] = ..., assumptions: _Optional[_Iterable[str]] = ..., is_blocking_gate_by_default: _Optional[bool] = ...) -> None: ...

class EvaluationBuilderScorecardRecommendationV1(_message.Message):
    __slots__ = ("measures", "availability")
    MEASURES_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    measures: _containers.RepeatedCompositeFieldContainer[EvaluationBuilderRecommendedMeasureV1]
    availability: MetricAvailabilityV1
    def __init__(self, measures: _Optional[_Iterable[_Union[EvaluationBuilderRecommendedMeasureV1, _Mapping]]] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class EvaluationBuilderCredentialRefV1(_message.Message):
    __slots__ = ("credential_id", "credential_key", "provider", "is_default", "enabled", "posture_code")
    CREDENTIAL_ID_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_KEY_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    POSTURE_CODE_FIELD_NUMBER: _ClassVar[int]
    credential_id: str
    credential_key: str
    provider: _agentic_pb2.ProviderNameV1
    is_default: bool
    enabled: bool
    posture_code: str
    def __init__(self, credential_id: _Optional[str] = ..., credential_key: _Optional[str] = ..., provider: _Optional[_Union[_agentic_pb2.ProviderNameV1, str]] = ..., is_default: _Optional[bool] = ..., enabled: _Optional[bool] = ..., posture_code: _Optional[str] = ...) -> None: ...

class EvaluationBuilderExecutionDefaultsV1(_message.Message):
    __slots__ = ("execution_policy", "budget", "default_trials", "max_cohorts", "max_candidates", "max_scorers", "max_trials")
    EXECUTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    BUDGET_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TRIALS_FIELD_NUMBER: _ClassVar[int]
    MAX_COHORTS_FIELD_NUMBER: _ClassVar[int]
    MAX_CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    MAX_SCORERS_FIELD_NUMBER: _ClassVar[int]
    MAX_TRIALS_FIELD_NUMBER: _ClassVar[int]
    execution_policy: EvaluationExecutionPolicyV1
    budget: EvaluationBudgetV1
    default_trials: int
    max_cohorts: int
    max_candidates: int
    max_scorers: int
    max_trials: int
    def __init__(self, execution_policy: _Optional[_Union[EvaluationExecutionPolicyV1, _Mapping]] = ..., budget: _Optional[_Union[EvaluationBudgetV1, _Mapping]] = ..., default_trials: _Optional[int] = ..., max_cohorts: _Optional[int] = ..., max_candidates: _Optional[int] = ..., max_scorers: _Optional[int] = ..., max_trials: _Optional[int] = ...) -> None: ...

class EvaluationBuilderReadinessFindingV1(_message.Message):
    __slots__ = ("finding_code", "severity", "resolving_section", "detail", "posture_code")
    FINDING_CODE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    RESOLVING_SECTION_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    POSTURE_CODE_FIELD_NUMBER: _ClassVar[int]
    finding_code: str
    severity: EvaluationBuilderReadinessSeverityV1
    resolving_section: EvaluationBuilderSectionV1
    detail: str
    posture_code: str
    def __init__(self, finding_code: _Optional[str] = ..., severity: _Optional[_Union[EvaluationBuilderReadinessSeverityV1, str]] = ..., resolving_section: _Optional[_Union[EvaluationBuilderSectionV1, str]] = ..., detail: _Optional[str] = ..., posture_code: _Optional[str] = ...) -> None: ...

class EvaluationBuilderInferredSubjectV1(_message.Message):
    __slots__ = ("kind", "alternatives", "availability", "provenance_code")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ALTERNATIVES_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    PROVENANCE_CODE_FIELD_NUMBER: _ClassVar[int]
    kind: EvaluationSubjectKindV1
    alternatives: _containers.RepeatedScalarFieldContainer[EvaluationSubjectKindV1]
    availability: MetricAvailabilityV1
    provenance_code: str
    def __init__(self, kind: _Optional[_Union[EvaluationSubjectKindV1, str]] = ..., alternatives: _Optional[_Iterable[_Union[EvaluationSubjectKindV1, str]]] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., provenance_code: _Optional[str] = ...) -> None: ...

class GetEvaluationBuilderContextResponse(_message.Message):
    __slots__ = ("draft", "definition_id", "source_revision_id", "revision_number", "datasets", "candidate_sources", "scorer_choices", "scorecard_recommendation", "credentials", "execution_defaults", "capabilities", "readiness", "inferred_subject", "allowed_actions", "freshness")
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DATASETS_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_SOURCES_FIELD_NUMBER: _ClassVar[int]
    SCORER_CHOICES_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    READINESS_FIELD_NUMBER: _ClassVar[int]
    INFERRED_SUBJECT_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    draft: EvaluationDefinitionDraftV1
    definition_id: str
    source_revision_id: str
    revision_number: int
    datasets: _containers.RepeatedCompositeFieldContainer[EvaluationBuilderDatasetOptionV1]
    candidate_sources: EvaluationBuilderCandidateSourcesV1
    scorer_choices: _containers.RepeatedCompositeFieldContainer[EvaluationBuilderScorerChoiceV1]
    scorecard_recommendation: EvaluationBuilderScorecardRecommendationV1
    credentials: _containers.RepeatedCompositeFieldContainer[EvaluationBuilderCredentialRefV1]
    execution_defaults: EvaluationBuilderExecutionDefaultsV1
    capabilities: AgenticEvaluationCapabilitiesV1
    readiness: _containers.RepeatedCompositeFieldContainer[EvaluationBuilderReadinessFindingV1]
    inferred_subject: EvaluationBuilderInferredSubjectV1
    allowed_actions: _containers.RepeatedCompositeFieldContainer[AllowedActionV1]
    freshness: EvaluationFreshnessV1
    def __init__(self, draft: _Optional[_Union[EvaluationDefinitionDraftV1, _Mapping]] = ..., definition_id: _Optional[str] = ..., source_revision_id: _Optional[str] = ..., revision_number: _Optional[int] = ..., datasets: _Optional[_Iterable[_Union[EvaluationBuilderDatasetOptionV1, _Mapping]]] = ..., candidate_sources: _Optional[_Union[EvaluationBuilderCandidateSourcesV1, _Mapping]] = ..., scorer_choices: _Optional[_Iterable[_Union[EvaluationBuilderScorerChoiceV1, _Mapping]]] = ..., scorecard_recommendation: _Optional[_Union[EvaluationBuilderScorecardRecommendationV1, _Mapping]] = ..., credentials: _Optional[_Iterable[_Union[EvaluationBuilderCredentialRefV1, _Mapping]]] = ..., execution_defaults: _Optional[_Union[EvaluationBuilderExecutionDefaultsV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., readiness: _Optional[_Iterable[_Union[EvaluationBuilderReadinessFindingV1, _Mapping]]] = ..., inferred_subject: _Optional[_Union[EvaluationBuilderInferredSubjectV1, _Mapping]] = ..., allowed_actions: _Optional[_Iterable[_Union[AllowedActionV1, _Mapping]]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class EvaluationFailureV1(_message.Message):
    __slots__ = ("stage", "code", "retryability", "sanitized_message", "correlation_id", "recovery", "last_attempt_at")
    STAGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    RETRYABILITY_FIELD_NUMBER: _ClassVar[int]
    SANITIZED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_FIELD_NUMBER: _ClassVar[int]
    LAST_ATTEMPT_AT_FIELD_NUMBER: _ClassVar[int]
    stage: EvaluationFailureStageV1
    code: str
    retryability: RetryabilityV1
    sanitized_message: str
    correlation_id: str
    recovery: RecoveryActionV1
    last_attempt_at: _timestamp_pb2.Timestamp
    def __init__(self, stage: _Optional[_Union[EvaluationFailureStageV1, str]] = ..., code: _Optional[str] = ..., retryability: _Optional[_Union[RetryabilityV1, str]] = ..., sanitized_message: _Optional[str] = ..., correlation_id: _Optional[str] = ..., recovery: _Optional[_Union[RecoveryActionV1, str]] = ..., last_attempt_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EvaluationCohortSnapshotV1(_message.Message):
    __slots__ = ("spec", "frozen_case_count", "schema_fingerprint", "schema_fingerprint_availability", "dataset_schema_revision_id")
    SPEC_FIELD_NUMBER: _ClassVar[int]
    FROZEN_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FINGERPRINT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    DATASET_SCHEMA_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    spec: EvaluationCohortSpecV1
    frozen_case_count: int
    schema_fingerprint: str
    schema_fingerprint_availability: MetricAvailabilityV1
    dataset_schema_revision_id: str
    def __init__(self, spec: _Optional[_Union[EvaluationCohortSpecV1, _Mapping]] = ..., frozen_case_count: _Optional[int] = ..., schema_fingerprint: _Optional[str] = ..., schema_fingerprint_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., dataset_schema_revision_id: _Optional[str] = ...) -> None: ...

class EvaluationScorerVersionSnapshotV1(_message.Message):
    __slots__ = ("score_config_id", "config_key", "metric_name", "version_discriminator", "compatible_subject_kinds", "compatible_subject_kinds_availability", "required_context_availability", "weight", "is_blocking_gate")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_DISCRIMINATOR_FIELD_NUMBER: _ClassVar[int]
    COMPATIBLE_SUBJECT_KINDS_FIELD_NUMBER: _ClassVar[int]
    COMPATIBLE_SUBJECT_KINDS_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_CONTEXT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    IS_BLOCKING_GATE_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    config_key: str
    metric_name: str
    version_discriminator: str
    compatible_subject_kinds: _containers.RepeatedScalarFieldContainer[EvaluationSubjectKindV1]
    compatible_subject_kinds_availability: MetricAvailabilityV1
    required_context_availability: MetricAvailabilityV1
    weight: float
    is_blocking_gate: bool
    def __init__(self, score_config_id: _Optional[str] = ..., config_key: _Optional[str] = ..., metric_name: _Optional[str] = ..., version_discriminator: _Optional[str] = ..., compatible_subject_kinds: _Optional[_Iterable[_Union[EvaluationSubjectKindV1, str]]] = ..., compatible_subject_kinds_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., required_context_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., weight: _Optional[float] = ..., is_blocking_gate: _Optional[bool] = ...) -> None: ...

class EvaluationCredentialReferenceV1(_message.Message):
    __slots__ = ("credential_id", "credential_key", "provider")
    CREDENTIAL_ID_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_KEY_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    credential_id: str
    credential_key: str
    provider: _agentic_pb2.ProviderNameV1
    def __init__(self, credential_id: _Optional[str] = ..., credential_key: _Optional[str] = ..., provider: _Optional[_Union[_agentic_pb2.ProviderNameV1, str]] = ...) -> None: ...

class EvaluationModelRateV1(_message.Message):
    __slots__ = ("candidate_key", "provider", "model_id", "input_micros_per_million_tokens", "output_micros_per_million_tokens", "fixed_micros_per_call", "rate_source", "currency_code", "availability", "cache_read_micros_per_million_tokens", "cache_write_5m_micros_per_million_tokens", "cache_write_1h_micros_per_million_tokens", "reasoning_micros_per_million_tokens", "token_accounting", "dimension_notes", "modifiers", "rate_checked_date", "superseded_rate")
    CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_MICROS_PER_MILLION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_MICROS_PER_MILLION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    FIXED_MICROS_PER_CALL_FIELD_NUMBER: _ClassVar[int]
    RATE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    CACHE_READ_MICROS_PER_MILLION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_WRITE_5M_MICROS_PER_MILLION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_WRITE_1H_MICROS_PER_MILLION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    REASONING_MICROS_PER_MILLION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ACCOUNTING_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_NOTES_FIELD_NUMBER: _ClassVar[int]
    MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    RATE_CHECKED_DATE_FIELD_NUMBER: _ClassVar[int]
    SUPERSEDED_RATE_FIELD_NUMBER: _ClassVar[int]
    candidate_key: str
    provider: _agentic_pb2.ProviderNameV1
    model_id: str
    input_micros_per_million_tokens: int
    output_micros_per_million_tokens: int
    fixed_micros_per_call: int
    rate_source: EvaluationRateSourceV1
    currency_code: str
    availability: MetricAvailabilityV1
    cache_read_micros_per_million_tokens: int
    cache_write_5m_micros_per_million_tokens: int
    cache_write_1h_micros_per_million_tokens: int
    reasoning_micros_per_million_tokens: int
    token_accounting: EvaluationTokenAccountingV1
    dimension_notes: _containers.RepeatedCompositeFieldContainer[EvaluationRateDimensionNoteV1]
    modifiers: _containers.RepeatedCompositeFieldContainer[EvaluationRateModifierV1]
    rate_checked_date: str
    superseded_rate: EvaluationSupersededRateV1
    def __init__(self, candidate_key: _Optional[str] = ..., provider: _Optional[_Union[_agentic_pb2.ProviderNameV1, str]] = ..., model_id: _Optional[str] = ..., input_micros_per_million_tokens: _Optional[int] = ..., output_micros_per_million_tokens: _Optional[int] = ..., fixed_micros_per_call: _Optional[int] = ..., rate_source: _Optional[_Union[EvaluationRateSourceV1, str]] = ..., currency_code: _Optional[str] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., cache_read_micros_per_million_tokens: _Optional[int] = ..., cache_write_5m_micros_per_million_tokens: _Optional[int] = ..., cache_write_1h_micros_per_million_tokens: _Optional[int] = ..., reasoning_micros_per_million_tokens: _Optional[int] = ..., token_accounting: _Optional[_Union[EvaluationTokenAccountingV1, _Mapping]] = ..., dimension_notes: _Optional[_Iterable[_Union[EvaluationRateDimensionNoteV1, _Mapping]]] = ..., modifiers: _Optional[_Iterable[_Union[EvaluationRateModifierV1, _Mapping]]] = ..., rate_checked_date: _Optional[str] = ..., superseded_rate: _Optional[_Union[EvaluationSupersededRateV1, _Mapping]] = ...) -> None: ...

class EvaluationSupersededRateV1(_message.Message):
    __slots__ = ("rate_source", "input_micros_per_million_tokens", "output_micros_per_million_tokens", "fixed_micros_per_call", "reason_code")
    RATE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    INPUT_MICROS_PER_MILLION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_MICROS_PER_MILLION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    FIXED_MICROS_PER_CALL_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    rate_source: EvaluationRateSourceV1
    input_micros_per_million_tokens: int
    output_micros_per_million_tokens: int
    fixed_micros_per_call: int
    reason_code: str
    def __init__(self, rate_source: _Optional[_Union[EvaluationRateSourceV1, str]] = ..., input_micros_per_million_tokens: _Optional[int] = ..., output_micros_per_million_tokens: _Optional[int] = ..., fixed_micros_per_call: _Optional[int] = ..., reason_code: _Optional[str] = ...) -> None: ...

class EvaluationRateModifierV1(_message.Message):
    __slots__ = ("code", "kind", "applied", "reason_code", "effect", "threshold_tokens", "threshold_basis_code", "window_description", "kind_detail_code", "effective_from", "effective_until", "provenance")
    CODE_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_TOKENS_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_BASIS_CODE_FIELD_NUMBER: _ClassVar[int]
    WINDOW_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    KIND_DETAIL_CODE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_FROM_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_UNTIL_FIELD_NUMBER: _ClassVar[int]
    PROVENANCE_FIELD_NUMBER: _ClassVar[int]
    code: str
    kind: EvaluationRateModifierKindV1
    applied: bool
    reason_code: str
    effect: EvaluationRateEffectV1
    threshold_tokens: int
    threshold_basis_code: str
    window_description: str
    kind_detail_code: str
    effective_from: str
    effective_until: str
    provenance: EvaluationRateProvenanceV1
    def __init__(self, code: _Optional[str] = ..., kind: _Optional[_Union[EvaluationRateModifierKindV1, str]] = ..., applied: _Optional[bool] = ..., reason_code: _Optional[str] = ..., effect: _Optional[_Union[EvaluationRateEffectV1, _Mapping]] = ..., threshold_tokens: _Optional[int] = ..., threshold_basis_code: _Optional[str] = ..., window_description: _Optional[str] = ..., kind_detail_code: _Optional[str] = ..., effective_from: _Optional[str] = ..., effective_until: _Optional[str] = ..., provenance: _Optional[_Union[EvaluationRateProvenanceV1, _Mapping]] = ...) -> None: ...

class EvaluationRateEffectV1(_message.Message):
    __slots__ = ("scales", "replacements")
    SCALES_FIELD_NUMBER: _ClassVar[int]
    REPLACEMENTS_FIELD_NUMBER: _ClassVar[int]
    scales: _containers.RepeatedCompositeFieldContainer[EvaluationRateScaleV1]
    replacements: _containers.RepeatedCompositeFieldContainer[EvaluationRateReplacementV1]
    def __init__(self, scales: _Optional[_Iterable[_Union[EvaluationRateScaleV1, _Mapping]]] = ..., replacements: _Optional[_Iterable[_Union[EvaluationRateReplacementV1, _Mapping]]] = ...) -> None: ...

class EvaluationRateScaleV1(_message.Message):
    __slots__ = ("dimension_code", "numerator", "denominator")
    DIMENSION_CODE_FIELD_NUMBER: _ClassVar[int]
    NUMERATOR_FIELD_NUMBER: _ClassVar[int]
    DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    dimension_code: str
    numerator: int
    denominator: int
    def __init__(self, dimension_code: _Optional[str] = ..., numerator: _Optional[int] = ..., denominator: _Optional[int] = ...) -> None: ...

class EvaluationRateReplacementV1(_message.Message):
    __slots__ = ("dimension_code", "micros_per_million_tokens")
    DIMENSION_CODE_FIELD_NUMBER: _ClassVar[int]
    MICROS_PER_MILLION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    dimension_code: str
    micros_per_million_tokens: int
    def __init__(self, dimension_code: _Optional[str] = ..., micros_per_million_tokens: _Optional[int] = ...) -> None: ...

class EvaluationRateProvenanceV1(_message.Message):
    __slots__ = ("source_id", "url", "section_id", "fetched_date", "section_sha256", "derivation")
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    FETCHED_DATE_FIELD_NUMBER: _ClassVar[int]
    SECTION_SHA256_FIELD_NUMBER: _ClassVar[int]
    DERIVATION_FIELD_NUMBER: _ClassVar[int]
    source_id: str
    url: str
    section_id: str
    fetched_date: str
    section_sha256: str
    derivation: str
    def __init__(self, source_id: _Optional[str] = ..., url: _Optional[str] = ..., section_id: _Optional[str] = ..., fetched_date: _Optional[str] = ..., section_sha256: _Optional[str] = ..., derivation: _Optional[str] = ...) -> None: ...

class EvaluationTokenAccountingV1(_message.Message):
    __slots__ = ("provider", "cache_tokens_inclusive", "reasoning_tokens_inclusive", "accounting_basis_code")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    CACHE_TOKENS_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    REASONING_TOKENS_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTING_BASIS_CODE_FIELD_NUMBER: _ClassVar[int]
    provider: _agentic_pb2.ProviderNameV1
    cache_tokens_inclusive: bool
    reasoning_tokens_inclusive: bool
    accounting_basis_code: str
    def __init__(self, provider: _Optional[_Union[_agentic_pb2.ProviderNameV1, str]] = ..., cache_tokens_inclusive: _Optional[bool] = ..., reasoning_tokens_inclusive: _Optional[bool] = ..., accounting_basis_code: _Optional[str] = ...) -> None: ...

class EvaluationRateDimensionNoteV1(_message.Message):
    __slots__ = ("dimension_code", "reason_code")
    DIMENSION_CODE_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    dimension_code: str
    reason_code: str
    def __init__(self, dimension_code: _Optional[str] = ..., reason_code: _Optional[str] = ...) -> None: ...

class EvaluationCostAssumptionV1(_message.Message):
    __slots__ = ("assumed_input_tokens_per_call", "assumed_output_tokens_per_call", "input_basis_code", "output_basis_code", "cache_basis_code")
    ASSUMED_INPUT_TOKENS_PER_CALL_FIELD_NUMBER: _ClassVar[int]
    ASSUMED_OUTPUT_TOKENS_PER_CALL_FIELD_NUMBER: _ClassVar[int]
    INPUT_BASIS_CODE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_BASIS_CODE_FIELD_NUMBER: _ClassVar[int]
    CACHE_BASIS_CODE_FIELD_NUMBER: _ClassVar[int]
    assumed_input_tokens_per_call: int
    assumed_output_tokens_per_call: int
    input_basis_code: str
    output_basis_code: str
    cache_basis_code: str
    def __init__(self, assumed_input_tokens_per_call: _Optional[int] = ..., assumed_output_tokens_per_call: _Optional[int] = ..., input_basis_code: _Optional[str] = ..., output_basis_code: _Optional[str] = ..., cache_basis_code: _Optional[str] = ...) -> None: ...

class EvaluationPricingSourceV1(_message.Message):
    __slots__ = ("pricing_source_version", "pricing_snapshot_ref", "model_rates", "effective_date", "registry_digest", "registry_age_days", "rate_staleness", "staleness_threshold_days", "provenance")
    PRICING_SOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    PRICING_SNAPSHOT_REF_FIELD_NUMBER: _ClassVar[int]
    MODEL_RATES_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_DATE_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_DIGEST_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_AGE_DAYS_FIELD_NUMBER: _ClassVar[int]
    RATE_STALENESS_FIELD_NUMBER: _ClassVar[int]
    STALENESS_THRESHOLD_DAYS_FIELD_NUMBER: _ClassVar[int]
    PROVENANCE_FIELD_NUMBER: _ClassVar[int]
    pricing_source_version: str
    pricing_snapshot_ref: str
    model_rates: _containers.RepeatedCompositeFieldContainer[EvaluationModelRateV1]
    effective_date: str
    registry_digest: str
    registry_age_days: int
    rate_staleness: EvaluationRateStalenessV1
    staleness_threshold_days: int
    provenance: _containers.RepeatedCompositeFieldContainer[EvaluationRateProvenanceV1]
    def __init__(self, pricing_source_version: _Optional[str] = ..., pricing_snapshot_ref: _Optional[str] = ..., model_rates: _Optional[_Iterable[_Union[EvaluationModelRateV1, _Mapping]]] = ..., effective_date: _Optional[str] = ..., registry_digest: _Optional[str] = ..., registry_age_days: _Optional[int] = ..., rate_staleness: _Optional[_Union[EvaluationRateStalenessV1, str]] = ..., staleness_threshold_days: _Optional[int] = ..., provenance: _Optional[_Iterable[_Union[EvaluationRateProvenanceV1, _Mapping]]] = ...) -> None: ...

class EvaluationCostReservationV1(_message.Message):
    __slots__ = ("reserved_candidate_cost", "reserved_availability", "budget_ceiling", "pricing_source_version", "assumption")
    RESERVED_CANDIDATE_COST_FIELD_NUMBER: _ClassVar[int]
    RESERVED_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    BUDGET_CEILING_FIELD_NUMBER: _ClassVar[int]
    PRICING_SOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    ASSUMPTION_FIELD_NUMBER: _ClassVar[int]
    reserved_candidate_cost: CostAmountV1
    reserved_availability: MetricAvailabilityV1
    budget_ceiling: CostAmountV1
    pricing_source_version: str
    assumption: EvaluationCostAssumptionV1
    def __init__(self, reserved_candidate_cost: _Optional[_Union[CostAmountV1, _Mapping]] = ..., reserved_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., budget_ceiling: _Optional[_Union[CostAmountV1, _Mapping]] = ..., pricing_source_version: _Optional[str] = ..., assumption: _Optional[_Union[EvaluationCostAssumptionV1, _Mapping]] = ...) -> None: ...

class EvaluationRunLimitsV1(_message.Message):
    __slots__ = ("max_expanded_cells", "preparation_shard_size", "preparation_max_attempts")
    MAX_EXPANDED_CELLS_FIELD_NUMBER: _ClassVar[int]
    PREPARATION_SHARD_SIZE_FIELD_NUMBER: _ClassVar[int]
    PREPARATION_MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    max_expanded_cells: int
    preparation_shard_size: int
    preparation_max_attempts: int
    def __init__(self, max_expanded_cells: _Optional[int] = ..., preparation_shard_size: _Optional[int] = ..., preparation_max_attempts: _Optional[int] = ...) -> None: ...

class EvaluationRunManifestV1(_message.Message):
    __slots__ = ("manifest_schema_version", "definition_revision_id", "definition_content_digest", "cohorts", "total_case_revision_count", "candidates", "scorers", "credentials", "pricing_source", "pricing_source_availability", "execution_policy", "budget", "limits", "trials", "human_review_policy", "decision_policy", "capability_set", "launch_mode", "cost_reservation", "scorer_suite", "frozen_evaluators")
    MANIFEST_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_CONTENT_DIGEST_FIELD_NUMBER: _ClassVar[int]
    COHORTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CASE_REVISION_COUNT_FIELD_NUMBER: _ClassVar[int]
    CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    SCORERS_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    PRICING_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PRICING_SOURCE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    BUDGET_FIELD_NUMBER: _ClassVar[int]
    LIMITS_FIELD_NUMBER: _ClassVar[int]
    TRIALS_FIELD_NUMBER: _ClassVar[int]
    HUMAN_REVIEW_POLICY_FIELD_NUMBER: _ClassVar[int]
    DECISION_POLICY_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_SET_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_MODE_FIELD_NUMBER: _ClassVar[int]
    COST_RESERVATION_FIELD_NUMBER: _ClassVar[int]
    SCORER_SUITE_FIELD_NUMBER: _ClassVar[int]
    FROZEN_EVALUATORS_FIELD_NUMBER: _ClassVar[int]
    manifest_schema_version: int
    definition_revision_id: str
    definition_content_digest: str
    cohorts: _containers.RepeatedCompositeFieldContainer[EvaluationCohortSnapshotV1]
    total_case_revision_count: int
    candidates: _containers.RepeatedCompositeFieldContainer[EvaluationCandidateV1]
    scorers: _containers.RepeatedCompositeFieldContainer[EvaluationScorerVersionSnapshotV1]
    credentials: _containers.RepeatedCompositeFieldContainer[EvaluationCredentialReferenceV1]
    pricing_source: EvaluationPricingSourceV1
    pricing_source_availability: MetricAvailabilityV1
    execution_policy: EvaluationExecutionPolicyV1
    budget: EvaluationBudgetV1
    limits: EvaluationRunLimitsV1
    trials: int
    human_review_policy: EvaluationHumanReviewPolicyV1
    decision_policy: EvaluationDecisionPolicyV1
    capability_set: AgenticEvaluationCapabilitiesV1
    launch_mode: EvaluationLaunchModeV1
    cost_reservation: EvaluationCostReservationV1
    scorer_suite: EvaluationScorerSuiteSnapshotV1
    frozen_evaluators: _containers.RepeatedCompositeFieldContainer[EvaluationFrozenEvaluatorRefV1]
    def __init__(self, manifest_schema_version: _Optional[int] = ..., definition_revision_id: _Optional[str] = ..., definition_content_digest: _Optional[str] = ..., cohorts: _Optional[_Iterable[_Union[EvaluationCohortSnapshotV1, _Mapping]]] = ..., total_case_revision_count: _Optional[int] = ..., candidates: _Optional[_Iterable[_Union[EvaluationCandidateV1, _Mapping]]] = ..., scorers: _Optional[_Iterable[_Union[EvaluationScorerVersionSnapshotV1, _Mapping]]] = ..., credentials: _Optional[_Iterable[_Union[EvaluationCredentialReferenceV1, _Mapping]]] = ..., pricing_source: _Optional[_Union[EvaluationPricingSourceV1, _Mapping]] = ..., pricing_source_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., execution_policy: _Optional[_Union[EvaluationExecutionPolicyV1, _Mapping]] = ..., budget: _Optional[_Union[EvaluationBudgetV1, _Mapping]] = ..., limits: _Optional[_Union[EvaluationRunLimitsV1, _Mapping]] = ..., trials: _Optional[int] = ..., human_review_policy: _Optional[_Union[EvaluationHumanReviewPolicyV1, _Mapping]] = ..., decision_policy: _Optional[_Union[EvaluationDecisionPolicyV1, _Mapping]] = ..., capability_set: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., launch_mode: _Optional[_Union[EvaluationLaunchModeV1, str]] = ..., cost_reservation: _Optional[_Union[EvaluationCostReservationV1, _Mapping]] = ..., scorer_suite: _Optional[_Union[EvaluationScorerSuiteSnapshotV1, _Mapping]] = ..., frozen_evaluators: _Optional[_Iterable[_Union[EvaluationFrozenEvaluatorRefV1, _Mapping]]] = ...) -> None: ...

class EvaluationFrozenEvaluatorRefV1(_message.Message):
    __slots__ = ("score_config_id", "config_key", "evaluator_template_id", "template_version_discriminator", "evaluator_kind", "execution_mode", "evaluator_config_json", "provider_execution_json", "provider", "model_id", "provider_credential_id", "model_rate")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_VERSION_DISCRIMINATOR_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_KIND_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_MODE_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_EXECUTION_JSON_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_CREDENTIAL_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_RATE_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    config_key: str
    evaluator_template_id: str
    template_version_discriminator: str
    evaluator_kind: str
    execution_mode: str
    evaluator_config_json: str
    provider_execution_json: str
    provider: _agentic_pb2.ProviderNameV1
    model_id: str
    provider_credential_id: str
    model_rate: EvaluationModelRateV1
    def __init__(self, score_config_id: _Optional[str] = ..., config_key: _Optional[str] = ..., evaluator_template_id: _Optional[str] = ..., template_version_discriminator: _Optional[str] = ..., evaluator_kind: _Optional[str] = ..., execution_mode: _Optional[str] = ..., evaluator_config_json: _Optional[str] = ..., provider_execution_json: _Optional[str] = ..., provider: _Optional[_Union[_agentic_pb2.ProviderNameV1, str]] = ..., model_id: _Optional[str] = ..., provider_credential_id: _Optional[str] = ..., model_rate: _Optional[_Union[EvaluationModelRateV1, _Mapping]] = ...) -> None: ...

class EvaluationRunProgressV1(_message.Message):
    __slots__ = ("expected_cell_count", "prepared_cell_count", "queued_cell_count", "cancelled_cell_count", "completed_shard_count", "total_shard_count", "execution_progress_availability", "executed_cell_count", "succeeded_cell_count", "failed_cell_count", "scorer_result_count", "awaiting_review_cell_count", "skipped_cell_count", "superseded_result_count")
    EXPECTED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    PREPARED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    QUEUED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_SHARD_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SHARD_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_PROGRESS_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUCCEEDED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    SCORER_RESULT_COUNT_FIELD_NUMBER: _ClassVar[int]
    AWAITING_REVIEW_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUPERSEDED_RESULT_COUNT_FIELD_NUMBER: _ClassVar[int]
    expected_cell_count: int
    prepared_cell_count: int
    queued_cell_count: int
    cancelled_cell_count: int
    completed_shard_count: int
    total_shard_count: int
    execution_progress_availability: MetricAvailabilityV1
    executed_cell_count: int
    succeeded_cell_count: int
    failed_cell_count: int
    scorer_result_count: int
    awaiting_review_cell_count: int
    skipped_cell_count: int
    superseded_result_count: int
    def __init__(self, expected_cell_count: _Optional[int] = ..., prepared_cell_count: _Optional[int] = ..., queued_cell_count: _Optional[int] = ..., cancelled_cell_count: _Optional[int] = ..., completed_shard_count: _Optional[int] = ..., total_shard_count: _Optional[int] = ..., execution_progress_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., executed_cell_count: _Optional[int] = ..., succeeded_cell_count: _Optional[int] = ..., failed_cell_count: _Optional[int] = ..., scorer_result_count: _Optional[int] = ..., awaiting_review_cell_count: _Optional[int] = ..., skipped_cell_count: _Optional[int] = ..., superseded_result_count: _Optional[int] = ...) -> None: ...

class EvaluationRunV1(_message.Message):
    __slots__ = ("evaluation_run_id", "definition_id", "definition_revision_id", "tenant_id", "org_id", "manifest", "state", "progress", "freshness", "launched_by", "accepted_preview_digest", "failure", "allowed_actions", "created_at", "started_at", "finished_at", "idempotency_key", "comparability_availability")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    LAUNCHED_BY_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_PREVIEW_DIGEST_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    COMPARABILITY_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    definition_id: str
    definition_revision_id: str
    tenant_id: str
    org_id: str
    manifest: EvaluationRunManifestV1
    state: EvaluationRunStateV1
    progress: EvaluationRunProgressV1
    freshness: EvaluationFreshnessV1
    launched_by: PrincipalRefV1
    accepted_preview_digest: str
    failure: EvaluationFailureV1
    allowed_actions: _containers.RepeatedCompositeFieldContainer[AllowedActionV1]
    created_at: _timestamp_pb2.Timestamp
    started_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    idempotency_key: str
    comparability_availability: MetricAvailabilityV1
    def __init__(self, evaluation_run_id: _Optional[str] = ..., definition_id: _Optional[str] = ..., definition_revision_id: _Optional[str] = ..., tenant_id: _Optional[str] = ..., org_id: _Optional[str] = ..., manifest: _Optional[_Union[EvaluationRunManifestV1, _Mapping]] = ..., state: _Optional[_Union[EvaluationRunStateV1, str]] = ..., progress: _Optional[_Union[EvaluationRunProgressV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., launched_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., accepted_preview_digest: _Optional[str] = ..., failure: _Optional[_Union[EvaluationFailureV1, _Mapping]] = ..., allowed_actions: _Optional[_Iterable[_Union[AllowedActionV1, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., idempotency_key: _Optional[str] = ..., comparability_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class EvaluationOperationV1(_message.Message):
    __slots__ = ("operation_id", "evaluation_run_id", "tenant_id", "org_id", "kind", "state", "completed_shard_count", "total_shard_count", "expected_cell_count", "expanded_cell_count", "attempt_count", "failure", "idempotency_key", "created_at", "updated_at", "finished_at")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_SHARD_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SHARD_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXPANDED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    evaluation_run_id: str
    tenant_id: str
    org_id: str
    kind: EvaluationOperationKindV1
    state: EvaluationOperationStateV1
    completed_shard_count: int
    total_shard_count: int
    expected_cell_count: int
    expanded_cell_count: int
    attempt_count: int
    failure: EvaluationFailureV1
    idempotency_key: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    def __init__(self, operation_id: _Optional[str] = ..., evaluation_run_id: _Optional[str] = ..., tenant_id: _Optional[str] = ..., org_id: _Optional[str] = ..., kind: _Optional[_Union[EvaluationOperationKindV1, str]] = ..., state: _Optional[_Union[EvaluationOperationStateV1, str]] = ..., completed_shard_count: _Optional[int] = ..., total_shard_count: _Optional[int] = ..., expected_cell_count: _Optional[int] = ..., expanded_cell_count: _Optional[int] = ..., attempt_count: _Optional[int] = ..., failure: _Optional[_Union[EvaluationFailureV1, _Mapping]] = ..., idempotency_key: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EvaluationCohortEstimateV1(_message.Message):
    __slots__ = ("cohort_key", "dataset_version_id", "case_count", "case_count_availability")
    COHORT_KEY_FIELD_NUMBER: _ClassVar[int]
    DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CASE_COUNT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    cohort_key: str
    dataset_version_id: str
    case_count: int
    case_count_availability: MetricAvailabilityV1
    def __init__(self, cohort_key: _Optional[str] = ..., dataset_version_id: _Optional[str] = ..., case_count: _Optional[int] = ..., case_count_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class EvaluationPreviewEstimatesV1(_message.Message):
    __slots__ = ("cohorts", "total_case_count", "candidate_count", "scorer_count", "trials", "candidate_call_count", "scorer_call_count", "max_retry_count", "max_concurrency", "candidate_cost", "candidate_cost_availability", "evaluator_cost", "evaluator_cost_availability", "total_cost", "total_cost_availability", "reserved_budget", "cost_assumption", "cost_breakdown", "budget_ceiling", "budget_ceiling_availability")
    COHORTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SCORER_COUNT_FIELD_NUMBER: _ClassVar[int]
    TRIALS_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_CALL_COUNT_FIELD_NUMBER: _ClassVar[int]
    SCORER_CALL_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_COST_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_COST_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_COST_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_COST_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COST_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COST_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    RESERVED_BUDGET_FIELD_NUMBER: _ClassVar[int]
    COST_ASSUMPTION_FIELD_NUMBER: _ClassVar[int]
    COST_BREAKDOWN_FIELD_NUMBER: _ClassVar[int]
    BUDGET_CEILING_FIELD_NUMBER: _ClassVar[int]
    BUDGET_CEILING_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    cohorts: _containers.RepeatedCompositeFieldContainer[EvaluationCohortEstimateV1]
    total_case_count: int
    candidate_count: int
    scorer_count: int
    trials: int
    candidate_call_count: int
    scorer_call_count: int
    max_retry_count: int
    max_concurrency: int
    candidate_cost: CostAmountV1
    candidate_cost_availability: MetricAvailabilityV1
    evaluator_cost: CostAmountV1
    evaluator_cost_availability: MetricAvailabilityV1
    total_cost: CostAmountV1
    total_cost_availability: MetricAvailabilityV1
    reserved_budget: CostAmountV1
    cost_assumption: EvaluationCostAssumptionV1
    cost_breakdown: CostBreakdownV1
    budget_ceiling: CostAmountV1
    budget_ceiling_availability: MetricAvailabilityV1
    def __init__(self, cohorts: _Optional[_Iterable[_Union[EvaluationCohortEstimateV1, _Mapping]]] = ..., total_case_count: _Optional[int] = ..., candidate_count: _Optional[int] = ..., scorer_count: _Optional[int] = ..., trials: _Optional[int] = ..., candidate_call_count: _Optional[int] = ..., scorer_call_count: _Optional[int] = ..., max_retry_count: _Optional[int] = ..., max_concurrency: _Optional[int] = ..., candidate_cost: _Optional[_Union[CostAmountV1, _Mapping]] = ..., candidate_cost_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., evaluator_cost: _Optional[_Union[CostAmountV1, _Mapping]] = ..., evaluator_cost_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., total_cost: _Optional[_Union[CostAmountV1, _Mapping]] = ..., total_cost_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., reserved_budget: _Optional[_Union[CostAmountV1, _Mapping]] = ..., cost_assumption: _Optional[_Union[EvaluationCostAssumptionV1, _Mapping]] = ..., cost_breakdown: _Optional[_Union[CostBreakdownV1, _Mapping]] = ..., budget_ceiling: _Optional[_Union[CostAmountV1, _Mapping]] = ..., budget_ceiling_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class EvaluationBlastRadiusV1(_message.Message):
    __slots__ = ("case_count", "trials", "estimated_external_calls", "worst_posture", "has_unattested_mutating_candidate", "attestation_enforcement_availability")
    CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TRIALS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_EXTERNAL_CALLS_FIELD_NUMBER: _ClassVar[int]
    WORST_POSTURE_FIELD_NUMBER: _ClassVar[int]
    HAS_UNATTESTED_MUTATING_CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    ATTESTATION_ENFORCEMENT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    case_count: int
    trials: int
    estimated_external_calls: int
    worst_posture: SideEffectPostureV1
    has_unattested_mutating_candidate: bool
    attestation_enforcement_availability: MetricAvailabilityV1
    def __init__(self, case_count: _Optional[int] = ..., trials: _Optional[int] = ..., estimated_external_calls: _Optional[int] = ..., worst_posture: _Optional[_Union[SideEffectPostureV1, str]] = ..., has_unattested_mutating_candidate: _Optional[bool] = ..., attestation_enforcement_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class EvaluationPreviewBlockerV1(_message.Message):
    __slots__ = ("kind", "code", "severity", "resolving_section", "detail", "posture_code")
    KIND_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    RESOLVING_SECTION_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    POSTURE_CODE_FIELD_NUMBER: _ClassVar[int]
    kind: EvaluationPreviewBlockerKindV1
    code: str
    severity: EvaluationBuilderReadinessSeverityV1
    resolving_section: EvaluationBuilderSectionV1
    detail: str
    posture_code: str
    def __init__(self, kind: _Optional[_Union[EvaluationPreviewBlockerKindV1, str]] = ..., code: _Optional[str] = ..., severity: _Optional[_Union[EvaluationBuilderReadinessSeverityV1, str]] = ..., resolving_section: _Optional[_Union[EvaluationBuilderSectionV1, str]] = ..., detail: _Optional[str] = ..., posture_code: _Optional[str] = ...) -> None: ...

class PreviewEvaluationRunRequest(_message.Message):
    __slots__ = ("definition_id", "revision_id")
    DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    definition_id: str
    revision_id: str
    def __init__(self, definition_id: _Optional[str] = ..., revision_id: _Optional[str] = ...) -> None: ...

class PreviewEvaluationRunResponse(_message.Message):
    __slots__ = ("preview_token", "preview_digest", "expires_at", "definition_id", "definition_revision_id", "revision_number", "launch_mode", "estimates", "blast_radius", "resolved_manifest", "blockers", "comparability_availability", "data_quality_availability", "inferred_subject", "launch_allowed", "allowed_actions", "capabilities", "freshness")
    PREVIEW_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_DIGEST_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_MODE_FIELD_NUMBER: _ClassVar[int]
    ESTIMATES_FIELD_NUMBER: _ClassVar[int]
    BLAST_RADIUS_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_MANIFEST_FIELD_NUMBER: _ClassVar[int]
    BLOCKERS_FIELD_NUMBER: _ClassVar[int]
    COMPARABILITY_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    DATA_QUALITY_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    INFERRED_SUBJECT_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    preview_token: str
    preview_digest: str
    expires_at: _timestamp_pb2.Timestamp
    definition_id: str
    definition_revision_id: str
    revision_number: int
    launch_mode: EvaluationLaunchModeV1
    estimates: EvaluationPreviewEstimatesV1
    blast_radius: EvaluationBlastRadiusV1
    resolved_manifest: EvaluationRunManifestV1
    blockers: _containers.RepeatedCompositeFieldContainer[EvaluationPreviewBlockerV1]
    comparability_availability: MetricAvailabilityV1
    data_quality_availability: MetricAvailabilityV1
    inferred_subject: EvaluationBuilderInferredSubjectV1
    launch_allowed: bool
    allowed_actions: _containers.RepeatedCompositeFieldContainer[AllowedActionV1]
    capabilities: AgenticEvaluationCapabilitiesV1
    freshness: EvaluationFreshnessV1
    def __init__(self, preview_token: _Optional[str] = ..., preview_digest: _Optional[str] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., definition_id: _Optional[str] = ..., definition_revision_id: _Optional[str] = ..., revision_number: _Optional[int] = ..., launch_mode: _Optional[_Union[EvaluationLaunchModeV1, str]] = ..., estimates: _Optional[_Union[EvaluationPreviewEstimatesV1, _Mapping]] = ..., blast_radius: _Optional[_Union[EvaluationBlastRadiusV1, _Mapping]] = ..., resolved_manifest: _Optional[_Union[EvaluationRunManifestV1, _Mapping]] = ..., blockers: _Optional[_Iterable[_Union[EvaluationPreviewBlockerV1, _Mapping]]] = ..., comparability_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., data_quality_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., inferred_subject: _Optional[_Union[EvaluationBuilderInferredSubjectV1, _Mapping]] = ..., launch_allowed: _Optional[bool] = ..., allowed_actions: _Optional[_Iterable[_Union[AllowedActionV1, _Mapping]]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class CreateEvaluationRunRequest(_message.Message):
    __slots__ = ("definition_id", "idempotency_key", "preview_token")
    DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_TOKEN_FIELD_NUMBER: _ClassVar[int]
    definition_id: str
    idempotency_key: str
    preview_token: str
    def __init__(self, definition_id: _Optional[str] = ..., idempotency_key: _Optional[str] = ..., preview_token: _Optional[str] = ...) -> None: ...

class CreateEvaluationRunResponse(_message.Message):
    __slots__ = ("run", "operation", "idempotent_replay")
    RUN_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    run: EvaluationRunV1
    operation: EvaluationOperationV1
    idempotent_replay: bool
    def __init__(self, run: _Optional[_Union[EvaluationRunV1, _Mapping]] = ..., operation: _Optional[_Union[EvaluationOperationV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ...) -> None: ...

class EvaluationLaunchRejectionV1(_message.Message):
    __slots__ = ("kind", "expected_digest", "observed_digest", "existing_evaluation_run_id", "recovery", "detail")
    KIND_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_DIGEST_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_DIGEST_FIELD_NUMBER: _ClassVar[int]
    EXISTING_EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    kind: EvaluationLaunchRejectionKindV1
    expected_digest: str
    observed_digest: str
    existing_evaluation_run_id: str
    recovery: RecoveryActionV1
    detail: str
    def __init__(self, kind: _Optional[_Union[EvaluationLaunchRejectionKindV1, str]] = ..., expected_digest: _Optional[str] = ..., observed_digest: _Optional[str] = ..., existing_evaluation_run_id: _Optional[str] = ..., recovery: _Optional[_Union[RecoveryActionV1, str]] = ..., detail: _Optional[str] = ...) -> None: ...

class GetEvaluationOperationRequest(_message.Message):
    __slots__ = ("operation_id", "idempotency_key")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    idempotency_key: str
    def __init__(self, operation_id: _Optional[str] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class GetEvaluationOperationResponse(_message.Message):
    __slots__ = ("operation", "run", "freshness", "capabilities")
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    RUN_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    operation: EvaluationOperationV1
    run: EvaluationRunV1
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, operation: _Optional[_Union[EvaluationOperationV1, _Mapping]] = ..., run: _Optional[_Union[EvaluationRunV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class CancelEvaluationRunRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "reason")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    reason: str
    def __init__(self, evaluation_run_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class CancelEvaluationRunResponse(_message.Message):
    __slots__ = ("run", "operation", "already_cancelled")
    RUN_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    ALREADY_CANCELLED_FIELD_NUMBER: _ClassVar[int]
    run: EvaluationRunV1
    operation: EvaluationOperationV1
    already_cancelled: bool
    def __init__(self, run: _Optional[_Union[EvaluationRunV1, _Mapping]] = ..., operation: _Optional[_Union[EvaluationOperationV1, _Mapping]] = ..., already_cancelled: _Optional[bool] = ...) -> None: ...

class EvaluationCellRefV1(_message.Message):
    __slots__ = ("cohort_key", "candidate_key", "case_revision_id", "trial")
    COHORT_KEY_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    CASE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    TRIAL_FIELD_NUMBER: _ClassVar[int]
    cohort_key: str
    candidate_key: str
    case_revision_id: str
    trial: int
    def __init__(self, cohort_key: _Optional[str] = ..., candidate_key: _Optional[str] = ..., case_revision_id: _Optional[str] = ..., trial: _Optional[int] = ...) -> None: ...

class EvaluationRetryCellStatusV1(_message.Message):
    __slots__ = ("cell", "eligible", "ineligibility", "current_state", "last_failure", "prior_attempt_generation")
    CELL_FIELD_NUMBER: _ClassVar[int]
    ELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    INELIGIBILITY_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STATE_FIELD_NUMBER: _ClassVar[int]
    LAST_FAILURE_FIELD_NUMBER: _ClassVar[int]
    PRIOR_ATTEMPT_GENERATION_FIELD_NUMBER: _ClassVar[int]
    cell: EvaluationCellRefV1
    eligible: bool
    ineligibility: EvaluationRetryIneligibilityV1
    current_state: EvaluationExecutionStateV1
    last_failure: EvaluationFailureV1
    prior_attempt_generation: int
    def __init__(self, cell: _Optional[_Union[EvaluationCellRefV1, _Mapping]] = ..., eligible: _Optional[bool] = ..., ineligibility: _Optional[_Union[EvaluationRetryIneligibilityV1, str]] = ..., current_state: _Optional[_Union[EvaluationExecutionStateV1, str]] = ..., last_failure: _Optional[_Union[EvaluationFailureV1, _Mapping]] = ..., prior_attempt_generation: _Optional[int] = ...) -> None: ...

class EvaluationRetryEstimateV1(_message.Message):
    __slots__ = ("estimated_candidate_cost", "cost_availability", "estimated_external_call_count", "superseded_result_count", "cost_posture", "priced_cell_count", "unpriced_cell_count")
    ESTIMATED_CANDIDATE_COST_FIELD_NUMBER: _ClassVar[int]
    COST_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_EXTERNAL_CALL_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUPERSEDED_RESULT_COUNT_FIELD_NUMBER: _ClassVar[int]
    COST_POSTURE_FIELD_NUMBER: _ClassVar[int]
    PRICED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNPRICED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    estimated_candidate_cost: CostAmountV1
    cost_availability: MetricAvailabilityV1
    estimated_external_call_count: int
    superseded_result_count: int
    cost_posture: CostPostureV1
    priced_cell_count: int
    unpriced_cell_count: int
    def __init__(self, estimated_candidate_cost: _Optional[_Union[CostAmountV1, _Mapping]] = ..., cost_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., estimated_external_call_count: _Optional[int] = ..., superseded_result_count: _Optional[int] = ..., cost_posture: _Optional[_Union[CostPostureV1, str]] = ..., priced_cell_count: _Optional[int] = ..., unpriced_cell_count: _Optional[int] = ...) -> None: ...

class PreviewRetryEvaluationCellsRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "cells")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CELLS_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    cells: _containers.RepeatedCompositeFieldContainer[EvaluationCellRefV1]
    def __init__(self, evaluation_run_id: _Optional[str] = ..., cells: _Optional[_Iterable[_Union[EvaluationCellRefV1, _Mapping]]] = ...) -> None: ...

class PreviewRetryEvaluationCellsResponse(_message.Message):
    __slots__ = ("evaluation_run_id", "cells", "retryable_cell_count", "estimate", "retry_allowed", "blocked_reason_code", "allowed_actions", "capabilities", "freshness", "blocked_posture_code")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CELLS_FIELD_NUMBER: _ClassVar[int]
    RETRYABLE_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    RETRY_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_POSTURE_CODE_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    cells: _containers.RepeatedCompositeFieldContainer[EvaluationRetryCellStatusV1]
    retryable_cell_count: int
    estimate: EvaluationRetryEstimateV1
    retry_allowed: bool
    blocked_reason_code: str
    allowed_actions: _containers.RepeatedCompositeFieldContainer[AllowedActionV1]
    capabilities: AgenticEvaluationCapabilitiesV1
    freshness: EvaluationFreshnessV1
    blocked_posture_code: str
    def __init__(self, evaluation_run_id: _Optional[str] = ..., cells: _Optional[_Iterable[_Union[EvaluationRetryCellStatusV1, _Mapping]]] = ..., retryable_cell_count: _Optional[int] = ..., estimate: _Optional[_Union[EvaluationRetryEstimateV1, _Mapping]] = ..., retry_allowed: _Optional[bool] = ..., blocked_reason_code: _Optional[str] = ..., allowed_actions: _Optional[_Iterable[_Union[AllowedActionV1, _Mapping]]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., blocked_posture_code: _Optional[str] = ...) -> None: ...

class RetryEvaluationCellsRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "cells", "idempotency_key")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CELLS_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    cells: _containers.RepeatedCompositeFieldContainer[EvaluationCellRefV1]
    idempotency_key: str
    def __init__(self, evaluation_run_id: _Optional[str] = ..., cells: _Optional[_Iterable[_Union[EvaluationCellRefV1, _Mapping]]] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class RetryEvaluationCellsResponse(_message.Message):
    __slots__ = ("run", "operation", "accepted_cell_count", "attempt_generation", "superseded_result_count", "rejected", "idempotent_replay")
    RUN_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_GENERATION_FIELD_NUMBER: _ClassVar[int]
    SUPERSEDED_RESULT_COUNT_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    run: EvaluationRunV1
    operation: EvaluationOperationV1
    accepted_cell_count: int
    attempt_generation: int
    superseded_result_count: int
    rejected: _containers.RepeatedCompositeFieldContainer[EvaluationRetryCellStatusV1]
    idempotent_replay: bool
    def __init__(self, run: _Optional[_Union[EvaluationRunV1, _Mapping]] = ..., operation: _Optional[_Union[EvaluationOperationV1, _Mapping]] = ..., accepted_cell_count: _Optional[int] = ..., attempt_generation: _Optional[int] = ..., superseded_result_count: _Optional[int] = ..., rejected: _Optional[_Iterable[_Union[EvaluationRetryCellStatusV1, _Mapping]]] = ..., idempotent_replay: _Optional[bool] = ...) -> None: ...

class EvaluationScorerCoordinateV1(_message.Message):
    __slots__ = ("cell", "score_config_id")
    CELL_FIELD_NUMBER: _ClassVar[int]
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    cell: EvaluationCellRefV1
    score_config_id: str
    def __init__(self, cell: _Optional[_Union[EvaluationCellRefV1, _Mapping]] = ..., score_config_id: _Optional[str] = ...) -> None: ...

class EvaluationScorerRetryStatusV1(_message.Message):
    __slots__ = ("coordinate", "eligible", "ineligibility", "scorer_key", "current_verdict", "prior_scorer_attempt", "derived_suite")
    COORDINATE_FIELD_NUMBER: _ClassVar[int]
    ELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    INELIGIBILITY_FIELD_NUMBER: _ClassVar[int]
    SCORER_KEY_FIELD_NUMBER: _ClassVar[int]
    CURRENT_VERDICT_FIELD_NUMBER: _ClassVar[int]
    PRIOR_SCORER_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    DERIVED_SUITE_FIELD_NUMBER: _ClassVar[int]
    coordinate: EvaluationScorerCoordinateV1
    eligible: bool
    ineligibility: EvaluationScorerRetryIneligibilityV1
    scorer_key: str
    current_verdict: EvaluationVerdictV1
    prior_scorer_attempt: int
    derived_suite: EvaluationDerivedSuiteCoordinateV1
    def __init__(self, coordinate: _Optional[_Union[EvaluationScorerCoordinateV1, _Mapping]] = ..., eligible: _Optional[bool] = ..., ineligibility: _Optional[_Union[EvaluationScorerRetryIneligibilityV1, str]] = ..., scorer_key: _Optional[str] = ..., current_verdict: _Optional[_Union[EvaluationVerdictV1, str]] = ..., prior_scorer_attempt: _Optional[int] = ..., derived_suite: _Optional[_Union[EvaluationDerivedSuiteCoordinateV1, _Mapping]] = ...) -> None: ...

class EvaluationScorerRetryRejectionV1(_message.Message):
    __slots__ = ("reason_code", "requested_coordinate_count", "max_coordinate_count", "detail")
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_COORDINATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_COORDINATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    reason_code: str
    requested_coordinate_count: int
    max_coordinate_count: int
    detail: str
    def __init__(self, reason_code: _Optional[str] = ..., requested_coordinate_count: _Optional[int] = ..., max_coordinate_count: _Optional[int] = ..., detail: _Optional[str] = ...) -> None: ...

class PreviewRetryEvaluationScorersRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "coordinates")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    COORDINATES_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    coordinates: _containers.RepeatedCompositeFieldContainer[EvaluationScorerCoordinateV1]
    def __init__(self, evaluation_run_id: _Optional[str] = ..., coordinates: _Optional[_Iterable[_Union[EvaluationScorerCoordinateV1, _Mapping]]] = ...) -> None: ...

class PreviewRetryEvaluationScorersResponse(_message.Message):
    __slots__ = ("evaluation_run_id", "coordinates", "retryable_coordinate_count", "estimated_external_call_count", "retry_allowed", "blocked_reason_code", "allowed_actions", "capabilities", "freshness", "superseded_evidence_code")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    COORDINATES_FIELD_NUMBER: _ClassVar[int]
    RETRYABLE_COORDINATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_EXTERNAL_CALL_COUNT_FIELD_NUMBER: _ClassVar[int]
    RETRY_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    SUPERSEDED_EVIDENCE_CODE_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    coordinates: _containers.RepeatedCompositeFieldContainer[EvaluationScorerRetryStatusV1]
    retryable_coordinate_count: int
    estimated_external_call_count: int
    retry_allowed: bool
    blocked_reason_code: str
    allowed_actions: _containers.RepeatedCompositeFieldContainer[AllowedActionV1]
    capabilities: AgenticEvaluationCapabilitiesV1
    freshness: EvaluationFreshnessV1
    superseded_evidence_code: str
    def __init__(self, evaluation_run_id: _Optional[str] = ..., coordinates: _Optional[_Iterable[_Union[EvaluationScorerRetryStatusV1, _Mapping]]] = ..., retryable_coordinate_count: _Optional[int] = ..., estimated_external_call_count: _Optional[int] = ..., retry_allowed: _Optional[bool] = ..., blocked_reason_code: _Optional[str] = ..., allowed_actions: _Optional[_Iterable[_Union[AllowedActionV1, _Mapping]]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., superseded_evidence_code: _Optional[str] = ...) -> None: ...

class RetryEvaluationScorersRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "coordinates", "idempotency_key")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    COORDINATES_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    coordinates: _containers.RepeatedCompositeFieldContainer[EvaluationScorerCoordinateV1]
    idempotency_key: str
    def __init__(self, evaluation_run_id: _Optional[str] = ..., coordinates: _Optional[_Iterable[_Union[EvaluationScorerCoordinateV1, _Mapping]]] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class EvaluationScorerRetryAppliedV1(_message.Message):
    __slots__ = ("coordinate", "scorer_key", "prior_verdict", "verdict", "score", "scorer_attempt", "superseded_attempt_count")
    COORDINATE_FIELD_NUMBER: _ClassVar[int]
    SCORER_KEY_FIELD_NUMBER: _ClassVar[int]
    PRIOR_VERDICT_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SCORER_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    SUPERSEDED_ATTEMPT_COUNT_FIELD_NUMBER: _ClassVar[int]
    coordinate: EvaluationScorerCoordinateV1
    scorer_key: str
    prior_verdict: EvaluationVerdictV1
    verdict: EvaluationVerdictV1
    score: float
    scorer_attempt: int
    superseded_attempt_count: int
    def __init__(self, coordinate: _Optional[_Union[EvaluationScorerCoordinateV1, _Mapping]] = ..., scorer_key: _Optional[str] = ..., prior_verdict: _Optional[_Union[EvaluationVerdictV1, str]] = ..., verdict: _Optional[_Union[EvaluationVerdictV1, str]] = ..., score: _Optional[float] = ..., scorer_attempt: _Optional[int] = ..., superseded_attempt_count: _Optional[int] = ...) -> None: ...

class RetryEvaluationScorersResponse(_message.Message):
    __slots__ = ("evaluation_run_id", "applied", "refused", "applied_coordinate_count", "external_calls_issued", "idempotent_replay", "capabilities")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    REFUSED_FIELD_NUMBER: _ClassVar[int]
    APPLIED_COORDINATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CALLS_ISSUED_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    applied: _containers.RepeatedCompositeFieldContainer[EvaluationScorerRetryAppliedV1]
    refused: _containers.RepeatedCompositeFieldContainer[EvaluationScorerRetryStatusV1]
    applied_coordinate_count: int
    external_calls_issued: int
    idempotent_replay: bool
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, evaluation_run_id: _Optional[str] = ..., applied: _Optional[_Iterable[_Union[EvaluationScorerRetryAppliedV1, _Mapping]]] = ..., refused: _Optional[_Iterable[_Union[EvaluationScorerRetryStatusV1, _Mapping]]] = ..., applied_coordinate_count: _Optional[int] = ..., external_calls_issued: _Optional[int] = ..., idempotent_replay: _Optional[bool] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class TokenUsageV1(_message.Message):
    __slots__ = ("input_tokens", "output_tokens", "total_tokens", "cache_read_input_tokens", "cache_creation_input_tokens", "reasoning_tokens", "requested_reasoning_effort", "availability")
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_READ_INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_CREATION_INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    REASONING_TOKENS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_REASONING_EFFORT_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    input_tokens: int
    output_tokens: int
    total_tokens: int
    cache_read_input_tokens: int
    cache_creation_input_tokens: int
    reasoning_tokens: int
    requested_reasoning_effort: _agentic_pb2.ProviderReasoningEffortV1
    availability: MetricAvailabilityV1
    def __init__(self, input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., total_tokens: _Optional[int] = ..., cache_read_input_tokens: _Optional[int] = ..., cache_creation_input_tokens: _Optional[int] = ..., reasoning_tokens: _Optional[int] = ..., requested_reasoning_effort: _Optional[_Union[_agentic_pb2.ProviderReasoningEffortV1, str]] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class ProviderUsageRecordV1(_message.Message):
    __slots__ = ("provider", "model_id", "token_accounting", "fields", "field_count", "preserved_byte_count", "availability", "served_upstream_provider", "echoed_model_id", "echoed_service_tier")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ACCOUNTING_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_COUNT_FIELD_NUMBER: _ClassVar[int]
    PRESERVED_BYTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    SERVED_UPSTREAM_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    ECHOED_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    ECHOED_SERVICE_TIER_FIELD_NUMBER: _ClassVar[int]
    provider: _agentic_pb2.ProviderNameV1
    model_id: str
    token_accounting: EvaluationTokenAccountingV1
    fields: _containers.RepeatedCompositeFieldContainer[ProviderUsageFieldV1]
    field_count: int
    preserved_byte_count: int
    availability: MetricAvailabilityV1
    served_upstream_provider: str
    echoed_model_id: str
    echoed_service_tier: str
    def __init__(self, provider: _Optional[_Union[_agentic_pb2.ProviderNameV1, str]] = ..., model_id: _Optional[str] = ..., token_accounting: _Optional[_Union[EvaluationTokenAccountingV1, _Mapping]] = ..., fields: _Optional[_Iterable[_Union[ProviderUsageFieldV1, _Mapping]]] = ..., field_count: _Optional[int] = ..., preserved_byte_count: _Optional[int] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., served_upstream_provider: _Optional[str] = ..., echoed_model_id: _Optional[str] = ..., echoed_service_tier: _Optional[str] = ...) -> None: ...

class ProviderUsageFieldV1(_message.Message):
    __slots__ = ("path", "integer", "number", "boolean", "text")
    PATH_FIELD_NUMBER: _ClassVar[int]
    INTEGER_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    path: str
    integer: int
    number: float
    boolean: bool
    text: str
    def __init__(self, path: _Optional[str] = ..., integer: _Optional[int] = ..., number: _Optional[float] = ..., boolean: _Optional[bool] = ..., text: _Optional[str] = ...) -> None: ...

class CostLineItemV1(_message.Message):
    __slots__ = ("category", "amount_micros", "currency_code", "posture", "pricing_source_version", "pricing_snapshot_ref", "availability")
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    POSTURE_FIELD_NUMBER: _ClassVar[int]
    PRICING_SOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    PRICING_SNAPSHOT_REF_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    category: CostCategoryV1
    amount_micros: int
    currency_code: str
    posture: CostPostureV1
    pricing_source_version: str
    pricing_snapshot_ref: str
    availability: MetricAvailabilityV1
    def __init__(self, category: _Optional[_Union[CostCategoryV1, str]] = ..., amount_micros: _Optional[int] = ..., currency_code: _Optional[str] = ..., posture: _Optional[_Union[CostPostureV1, str]] = ..., pricing_source_version: _Optional[str] = ..., pricing_snapshot_ref: _Optional[str] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class CostBreakdownV1(_message.Message):
    __slots__ = ("line_items", "total", "total_availability")
    LINE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    line_items: _containers.RepeatedCompositeFieldContainer[CostLineItemV1]
    total: CostAmountV1
    total_availability: MetricAvailabilityV1
    def __init__(self, line_items: _Optional[_Iterable[_Union[CostLineItemV1, _Mapping]]] = ..., total: _Optional[_Union[CostAmountV1, _Mapping]] = ..., total_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class LatencyMetricsV1(_message.Message):
    __slots__ = ("total_micros", "total_availability", "time_to_first_token_micros", "time_to_first_token_availability", "output_tokens_per_second", "output_tokens_per_second_availability")
    TOTAL_MICROS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_FIRST_TOKEN_MICROS_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_FIRST_TOKEN_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_PER_SECOND_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    total_micros: int
    total_availability: MetricAvailabilityV1
    time_to_first_token_micros: int
    time_to_first_token_availability: MetricAvailabilityV1
    output_tokens_per_second: float
    output_tokens_per_second_availability: MetricAvailabilityV1
    def __init__(self, total_micros: _Optional[int] = ..., total_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., time_to_first_token_micros: _Optional[int] = ..., time_to_first_token_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., output_tokens_per_second: _Optional[float] = ..., output_tokens_per_second_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class ProviderStatusV1(_message.Message):
    __slots__ = ("status_class", "http_status", "provider_error_code", "availability")
    STATUS_CLASS_FIELD_NUMBER: _ClassVar[int]
    HTTP_STATUS_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    status_class: ProviderStatusClassV1
    http_status: int
    provider_error_code: str
    availability: MetricAvailabilityV1
    def __init__(self, status_class: _Optional[_Union[ProviderStatusClassV1, str]] = ..., http_status: _Optional[int] = ..., provider_error_code: _Optional[str] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class InstrumentationCompletenessV1(_message.Message):
    __slots__ = ("state", "reason_code", "provenance")
    STATE_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    PROVENANCE_FIELD_NUMBER: _ClassVar[int]
    state: InstrumentationCompletenessStateV1
    reason_code: str
    provenance: SemanticConventionProvenanceV1
    def __init__(self, state: _Optional[_Union[InstrumentationCompletenessStateV1, str]] = ..., reason_code: _Optional[str] = ..., provenance: _Optional[_Union[SemanticConventionProvenanceV1, _Mapping]] = ...) -> None: ...

class ExecutionMetricsV1(_message.Message):
    __slots__ = ("scope", "tokens", "cost", "latency", "retry_count", "attempt_count", "provider_status", "execution_trace_id", "failure", "completeness")
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    LATENCY_FIELD_NUMBER: _ClassVar[int]
    RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_STATUS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    COMPLETENESS_FIELD_NUMBER: _ClassVar[int]
    scope: ExecutionMetricsScopeV1
    tokens: TokenUsageV1
    cost: CostBreakdownV1
    latency: LatencyMetricsV1
    retry_count: int
    attempt_count: int
    provider_status: ProviderStatusV1
    execution_trace_id: str
    failure: EvaluationFailureV1
    completeness: InstrumentationCompletenessV1
    def __init__(self, scope: _Optional[_Union[ExecutionMetricsScopeV1, str]] = ..., tokens: _Optional[_Union[TokenUsageV1, _Mapping]] = ..., cost: _Optional[_Union[CostBreakdownV1, _Mapping]] = ..., latency: _Optional[_Union[LatencyMetricsV1, _Mapping]] = ..., retry_count: _Optional[int] = ..., attempt_count: _Optional[int] = ..., provider_status: _Optional[_Union[ProviderStatusV1, _Mapping]] = ..., execution_trace_id: _Optional[str] = ..., failure: _Optional[_Union[EvaluationFailureV1, _Mapping]] = ..., completeness: _Optional[_Union[InstrumentationCompletenessV1, _Mapping]] = ...) -> None: ...

class EvaluationScorerResultV1(_message.Message):
    __slots__ = ("score_config_id", "config_key", "metric_name", "verdict", "score", "score_availability", "is_blocking_gate", "failure", "metrics")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SCORE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    IS_BLOCKING_GATE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    config_key: str
    metric_name: str
    verdict: EvaluationVerdictV1
    score: float
    score_availability: MetricAvailabilityV1
    is_blocking_gate: bool
    failure: EvaluationFailureV1
    metrics: ExecutionMetricsV1
    def __init__(self, score_config_id: _Optional[str] = ..., config_key: _Optional[str] = ..., metric_name: _Optional[str] = ..., verdict: _Optional[_Union[EvaluationVerdictV1, str]] = ..., score: _Optional[float] = ..., score_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., is_blocking_gate: _Optional[bool] = ..., failure: _Optional[_Union[EvaluationFailureV1, _Mapping]] = ..., metrics: _Optional[_Union[ExecutionMetricsV1, _Mapping]] = ...) -> None: ...

class EvaluationCellResultV1(_message.Message):
    __slots__ = ("evaluation_run_id", "cohort_key", "candidate_key", "case_revision_id", "trial", "state", "candidate_source", "candidate_metrics", "scorer_results", "aggregate_verdict", "failure", "executed_at")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    COHORT_KEY_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    CASE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    TRIAL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_METRICS_FIELD_NUMBER: _ClassVar[int]
    SCORER_RESULTS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_VERDICT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_AT_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    cohort_key: str
    candidate_key: str
    case_revision_id: str
    trial: int
    state: EvaluationExecutionStateV1
    candidate_source: EvaluationCandidateSourceV1
    candidate_metrics: ExecutionMetricsV1
    scorer_results: _containers.RepeatedCompositeFieldContainer[EvaluationScorerResultV1]
    aggregate_verdict: EvaluationVerdictV1
    failure: EvaluationFailureV1
    executed_at: _timestamp_pb2.Timestamp
    def __init__(self, evaluation_run_id: _Optional[str] = ..., cohort_key: _Optional[str] = ..., candidate_key: _Optional[str] = ..., case_revision_id: _Optional[str] = ..., trial: _Optional[int] = ..., state: _Optional[_Union[EvaluationExecutionStateV1, str]] = ..., candidate_source: _Optional[_Union[EvaluationCandidateSourceV1, str]] = ..., candidate_metrics: _Optional[_Union[ExecutionMetricsV1, _Mapping]] = ..., scorer_results: _Optional[_Iterable[_Union[EvaluationScorerResultV1, _Mapping]]] = ..., aggregate_verdict: _Optional[_Union[EvaluationVerdictV1, str]] = ..., failure: _Optional[_Union[EvaluationFailureV1, _Mapping]] = ..., executed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EvaluationVerdictCountsV1(_message.Message):
    __slots__ = ("pass_count", "fail_count", "error_count", "skipped_count", "not_applicable_count", "total_count")
    PASS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAIL_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_COUNT_FIELD_NUMBER: _ClassVar[int]
    NOT_APPLICABLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    pass_count: int
    fail_count: int
    error_count: int
    skipped_count: int
    not_applicable_count: int
    total_count: int
    def __init__(self, pass_count: _Optional[int] = ..., fail_count: _Optional[int] = ..., error_count: _Optional[int] = ..., skipped_count: _Optional[int] = ..., not_applicable_count: _Optional[int] = ..., total_count: _Optional[int] = ...) -> None: ...

class EvaluationScorerRollupV1(_message.Message):
    __slots__ = ("score_config_id", "config_key", "metric_name", "verdicts", "mean_score", "mean_score_availability", "is_blocking_gate", "freshness", "completion", "evaluator_economics")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    VERDICTS_FIELD_NUMBER: _ClassVar[int]
    MEAN_SCORE_FIELD_NUMBER: _ClassVar[int]
    MEAN_SCORE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    IS_BLOCKING_GATE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_ECONOMICS_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    config_key: str
    metric_name: str
    verdicts: EvaluationVerdictCountsV1
    mean_score: float
    mean_score_availability: MetricAvailabilityV1
    is_blocking_gate: bool
    freshness: EvaluationFreshnessV1
    completion: EvaluationScorerCompletionV1
    evaluator_economics: ExecutionMetricsV1
    def __init__(self, score_config_id: _Optional[str] = ..., config_key: _Optional[str] = ..., metric_name: _Optional[str] = ..., verdicts: _Optional[_Union[EvaluationVerdictCountsV1, _Mapping]] = ..., mean_score: _Optional[float] = ..., mean_score_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., is_blocking_gate: _Optional[bool] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., completion: _Optional[_Union[EvaluationScorerCompletionV1, _Mapping]] = ..., evaluator_economics: _Optional[_Union[ExecutionMetricsV1, _Mapping]] = ...) -> None: ...

class EvaluationScorerCompletionV1(_message.Message):
    __slots__ = ("state", "expected_cell_count", "completed_cell_count", "pending_review_cell_count", "not_sampled_cell_count", "reason_code")
    STATE_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    PENDING_REVIEW_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    NOT_SAMPLED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    state: EvaluationScorerCompletionStateV1
    expected_cell_count: int
    completed_cell_count: int
    pending_review_cell_count: int
    not_sampled_cell_count: int
    reason_code: str
    def __init__(self, state: _Optional[_Union[EvaluationScorerCompletionStateV1, str]] = ..., expected_cell_count: _Optional[int] = ..., completed_cell_count: _Optional[int] = ..., pending_review_cell_count: _Optional[int] = ..., not_sampled_cell_count: _Optional[int] = ..., reason_code: _Optional[str] = ...) -> None: ...

class EvaluationFailureStageCountV1(_message.Message):
    __slots__ = ("stage", "code", "count")
    STAGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    stage: EvaluationFailureStageV1
    code: str
    count: int
    def __init__(self, stage: _Optional[_Union[EvaluationFailureStageV1, str]] = ..., code: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class EvaluationRunFailureRollupV1(_message.Message):
    __slots__ = ("candidate_failure_count", "scorer_failure_count", "cancelled_cell_count", "by_stage", "terminal_failure", "by_stage_availability")
    CANDIDATE_FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SCORER_FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    BY_STAGE_FIELD_NUMBER: _ClassVar[int]
    TERMINAL_FAILURE_FIELD_NUMBER: _ClassVar[int]
    BY_STAGE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    candidate_failure_count: int
    scorer_failure_count: int
    cancelled_cell_count: int
    by_stage: _containers.RepeatedCompositeFieldContainer[EvaluationFailureStageCountV1]
    terminal_failure: EvaluationFailureV1
    by_stage_availability: MetricAvailabilityV1
    def __init__(self, candidate_failure_count: _Optional[int] = ..., scorer_failure_count: _Optional[int] = ..., cancelled_cell_count: _Optional[int] = ..., by_stage: _Optional[_Iterable[_Union[EvaluationFailureStageCountV1, _Mapping]]] = ..., terminal_failure: _Optional[_Union[EvaluationFailureV1, _Mapping]] = ..., by_stage_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class EvaluationRunRecoveryV1(_message.Message):
    __slots__ = ("retryable_cell_count", "awaiting_review_cell_count", "budget_blocked_cell_count", "cancelled_cell_count", "superseded_result_count", "attempt_generation", "recommended_action", "availability")
    RETRYABLE_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    AWAITING_REVIEW_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    BUDGET_BLOCKED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUPERSEDED_RESULT_COUNT_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_GENERATION_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_ACTION_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    retryable_cell_count: int
    awaiting_review_cell_count: int
    budget_blocked_cell_count: int
    cancelled_cell_count: int
    superseded_result_count: int
    attempt_generation: int
    recommended_action: RecoveryActionV1
    availability: MetricAvailabilityV1
    def __init__(self, retryable_cell_count: _Optional[int] = ..., awaiting_review_cell_count: _Optional[int] = ..., budget_blocked_cell_count: _Optional[int] = ..., cancelled_cell_count: _Optional[int] = ..., superseded_result_count: _Optional[int] = ..., attempt_generation: _Optional[int] = ..., recommended_action: _Optional[_Union[RecoveryActionV1, str]] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class EvaluationCursorResyncV1(_message.Message):
    __slots__ = ("reason", "restart_required", "detail")
    REASON_FIELD_NUMBER: _ClassVar[int]
    RESTART_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    reason: EvaluationResyncReasonV1
    restart_required: bool
    detail: str
    def __init__(self, reason: _Optional[_Union[EvaluationResyncReasonV1, str]] = ..., restart_required: _Optional[bool] = ..., detail: _Optional[str] = ...) -> None: ...

class EvaluationDecisionDriverV1(_message.Message):
    __slots__ = ("ordinal", "kind", "consequence", "candidate_key", "reference_candidate_key", "score_config_id", "config_key", "metric_name", "is_blocking_gate", "affected_count", "denominator", "matrix_filter_token")
    ORDINAL_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    CONSEQUENCE_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_BLOCKING_GATE_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    MATRIX_FILTER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ordinal: int
    kind: EvaluationDecisionDriverKindV1
    consequence: EvaluationDecisionConsequenceV1
    candidate_key: str
    reference_candidate_key: str
    score_config_id: str
    config_key: str
    metric_name: str
    is_blocking_gate: bool
    affected_count: int
    denominator: int
    matrix_filter_token: str
    def __init__(self, ordinal: _Optional[int] = ..., kind: _Optional[_Union[EvaluationDecisionDriverKindV1, str]] = ..., consequence: _Optional[_Union[EvaluationDecisionConsequenceV1, str]] = ..., candidate_key: _Optional[str] = ..., reference_candidate_key: _Optional[str] = ..., score_config_id: _Optional[str] = ..., config_key: _Optional[str] = ..., metric_name: _Optional[str] = ..., is_blocking_gate: _Optional[bool] = ..., affected_count: _Optional[int] = ..., denominator: _Optional[int] = ..., matrix_filter_token: _Optional[str] = ...) -> None: ...

class EvaluationDecisionDriversV1(_message.Message):
    __slots__ = ("availability", "drivers", "reference_candidate_key", "reason_code", "freshness")
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    DRIVERS_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    availability: MetricAvailabilityV1
    drivers: _containers.RepeatedCompositeFieldContainer[EvaluationDecisionDriverV1]
    reference_candidate_key: str
    reason_code: str
    freshness: EvaluationFreshnessV1
    def __init__(self, availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., drivers: _Optional[_Iterable[_Union[EvaluationDecisionDriverV1, _Mapping]]] = ..., reference_candidate_key: _Optional[str] = ..., reason_code: _Optional[str] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class RepeatSampleCheckV1(_message.Message):
    __slots__ = ("satisfied", "observed_repeat_count", "required_repeat_count", "basis")
    SATISFIED_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_REPEAT_COUNT_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_REPEAT_COUNT_FIELD_NUMBER: _ClassVar[int]
    BASIS_FIELD_NUMBER: _ClassVar[int]
    satisfied: bool
    observed_repeat_count: int
    required_repeat_count: int
    basis: EvaluationRepeatBasisV1
    def __init__(self, satisfied: _Optional[bool] = ..., observed_repeat_count: _Optional[int] = ..., required_repeat_count: _Optional[int] = ..., basis: _Optional[_Union[EvaluationRepeatBasisV1, str]] = ...) -> None: ...

class MinimumDetectableEffectV1(_message.Message):
    __slots__ = ("effect", "alpha", "power", "aligned_pair_count", "discordant_rate", "basis_code")
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    ALPHA_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    ALIGNED_PAIR_COUNT_FIELD_NUMBER: _ClassVar[int]
    DISCORDANT_RATE_FIELD_NUMBER: _ClassVar[int]
    BASIS_CODE_FIELD_NUMBER: _ClassVar[int]
    effect: float
    alpha: float
    power: float
    aligned_pair_count: int
    discordant_rate: float
    basis_code: str
    def __init__(self, effect: _Optional[float] = ..., alpha: _Optional[float] = ..., power: _Optional[float] = ..., aligned_pair_count: _Optional[int] = ..., discordant_rate: _Optional[float] = ..., basis_code: _Optional[str] = ...) -> None: ...

class ComparisonRepeatAlignmentV1(_message.Message):
    __slots__ = ("rule", "reason_code", "repeated_case_count", "split_case_count", "tie_case_count", "instability_rate")
    RULE_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SPLIT_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TIE_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    INSTABILITY_RATE_FIELD_NUMBER: _ClassVar[int]
    rule: ComparisonAlignmentRuleV1
    reason_code: str
    repeated_case_count: int
    split_case_count: int
    tie_case_count: int
    instability_rate: float
    def __init__(self, rule: _Optional[_Union[ComparisonAlignmentRuleV1, str]] = ..., reason_code: _Optional[str] = ..., repeated_case_count: _Optional[int] = ..., split_case_count: _Optional[int] = ..., tie_case_count: _Optional[int] = ..., instability_rate: _Optional[float] = ...) -> None: ...

class MinimumSampleCheckV1(_message.Message):
    __slots__ = ("satisfied", "observed_count", "required_count")
    SATISFIED_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_COUNT_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_COUNT_FIELD_NUMBER: _ClassVar[int]
    satisfied: bool
    observed_count: int
    required_count: int
    def __init__(self, satisfied: _Optional[bool] = ..., observed_count: _Optional[int] = ..., required_count: _Optional[int] = ...) -> None: ...

class ConfidenceIntervalV1(_message.Message):
    __slots__ = ("lower", "upper", "confidence_level")
    LOWER_FIELD_NUMBER: _ClassVar[int]
    UPPER_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    lower: float
    upper: float
    confidence_level: float
    def __init__(self, lower: _Optional[float] = ..., upper: _Optional[float] = ..., confidence_level: _Optional[float] = ...) -> None: ...

class StatisticalResultV1(_message.Message):
    __slots__ = ("test", "p_value", "corrected_p_value", "correction", "effect_size", "confidence_interval", "validity", "significant", "alpha", "minimum_detectable_effect", "minimum_detectable_effect_availability", "effect_size_variance", "effect_size_standard_error")
    TEST_FIELD_NUMBER: _ClassVar[int]
    P_VALUE_FIELD_NUMBER: _ClassVar[int]
    CORRECTED_P_VALUE_FIELD_NUMBER: _ClassVar[int]
    CORRECTION_FIELD_NUMBER: _ClassVar[int]
    EFFECT_SIZE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    VALIDITY_FIELD_NUMBER: _ClassVar[int]
    SIGNIFICANT_FIELD_NUMBER: _ClassVar[int]
    ALPHA_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_DETECTABLE_EFFECT_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_DETECTABLE_EFFECT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    EFFECT_SIZE_VARIANCE_FIELD_NUMBER: _ClassVar[int]
    EFFECT_SIZE_STANDARD_ERROR_FIELD_NUMBER: _ClassVar[int]
    test: StatisticalTestV1
    p_value: float
    corrected_p_value: float
    correction: MultipleComparisonCorrectionV1
    effect_size: float
    confidence_interval: ConfidenceIntervalV1
    validity: StatisticalValidityV1
    significant: bool
    alpha: float
    minimum_detectable_effect: MinimumDetectableEffectV1
    minimum_detectable_effect_availability: MetricAvailabilityV1
    effect_size_variance: float
    effect_size_standard_error: float
    def __init__(self, test: _Optional[_Union[StatisticalTestV1, str]] = ..., p_value: _Optional[float] = ..., corrected_p_value: _Optional[float] = ..., correction: _Optional[_Union[MultipleComparisonCorrectionV1, str]] = ..., effect_size: _Optional[float] = ..., confidence_interval: _Optional[_Union[ConfidenceIntervalV1, _Mapping]] = ..., validity: _Optional[_Union[StatisticalValidityV1, str]] = ..., significant: _Optional[bool] = ..., alpha: _Optional[float] = ..., minimum_detectable_effect: _Optional[_Union[MinimumDetectableEffectV1, _Mapping]] = ..., minimum_detectable_effect_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., effect_size_variance: _Optional[float] = ..., effect_size_standard_error: _Optional[float] = ...) -> None: ...

class CandidatePairComparisonV1(_message.Message):
    __slots__ = ("candidate_key", "score_config_id", "config_key", "metric_name", "is_blocking_gate", "aligned_pair_count", "regressed_count", "improved_count", "unchanged_count", "statistics", "minimum_sample", "repeat_sample", "repeat_alignment", "minimum_detectable_effect", "minimum_detectable_effect_availability")
    CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_BLOCKING_GATE_FIELD_NUMBER: _ClassVar[int]
    ALIGNED_PAIR_COUNT_FIELD_NUMBER: _ClassVar[int]
    REGRESSED_COUNT_FIELD_NUMBER: _ClassVar[int]
    IMPROVED_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNCHANGED_COUNT_FIELD_NUMBER: _ClassVar[int]
    STATISTICS_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_SAMPLE_FIELD_NUMBER: _ClassVar[int]
    REPEAT_SAMPLE_FIELD_NUMBER: _ClassVar[int]
    REPEAT_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_DETECTABLE_EFFECT_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_DETECTABLE_EFFECT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    candidate_key: str
    score_config_id: str
    config_key: str
    metric_name: str
    is_blocking_gate: bool
    aligned_pair_count: int
    regressed_count: int
    improved_count: int
    unchanged_count: int
    statistics: StatisticalResultV1
    minimum_sample: MinimumSampleCheckV1
    repeat_sample: RepeatSampleCheckV1
    repeat_alignment: ComparisonRepeatAlignmentV1
    minimum_detectable_effect: MinimumDetectableEffectV1
    minimum_detectable_effect_availability: MetricAvailabilityV1
    def __init__(self, candidate_key: _Optional[str] = ..., score_config_id: _Optional[str] = ..., config_key: _Optional[str] = ..., metric_name: _Optional[str] = ..., is_blocking_gate: _Optional[bool] = ..., aligned_pair_count: _Optional[int] = ..., regressed_count: _Optional[int] = ..., improved_count: _Optional[int] = ..., unchanged_count: _Optional[int] = ..., statistics: _Optional[_Union[StatisticalResultV1, _Mapping]] = ..., minimum_sample: _Optional[_Union[MinimumSampleCheckV1, _Mapping]] = ..., repeat_sample: _Optional[_Union[RepeatSampleCheckV1, _Mapping]] = ..., repeat_alignment: _Optional[_Union[ComparisonRepeatAlignmentV1, _Mapping]] = ..., minimum_detectable_effect: _Optional[_Union[MinimumDetectableEffectV1, _Mapping]] = ..., minimum_detectable_effect_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class EvaluationCandidateComparisonV1(_message.Message):
    __slots__ = ("reference_candidate_key", "reference_availability", "pairs", "correction", "test_family_size", "availability", "freshness")
    REFERENCE_CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    PAIRS_FIELD_NUMBER: _ClassVar[int]
    CORRECTION_FIELD_NUMBER: _ClassVar[int]
    TEST_FAMILY_SIZE_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    reference_candidate_key: str
    reference_availability: MetricAvailabilityV1
    pairs: _containers.RepeatedCompositeFieldContainer[CandidatePairComparisonV1]
    correction: MultipleComparisonCorrectionV1
    test_family_size: int
    availability: MetricAvailabilityV1
    freshness: EvaluationFreshnessV1
    def __init__(self, reference_candidate_key: _Optional[str] = ..., reference_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., pairs: _Optional[_Iterable[_Union[CandidatePairComparisonV1, _Mapping]]] = ..., correction: _Optional[_Union[MultipleComparisonCorrectionV1, str]] = ..., test_family_size: _Optional[int] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class EvaluationSliceCandidateRowV1(_message.Message):
    __slots__ = ("candidate_key", "verdicts", "mean_score", "mean_score_availability", "scored_result_count")
    CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    VERDICTS_FIELD_NUMBER: _ClassVar[int]
    MEAN_SCORE_FIELD_NUMBER: _ClassVar[int]
    MEAN_SCORE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    SCORED_RESULT_COUNT_FIELD_NUMBER: _ClassVar[int]
    candidate_key: str
    verdicts: EvaluationVerdictCountsV1
    mean_score: float
    mean_score_availability: MetricAvailabilityV1
    scored_result_count: int
    def __init__(self, candidate_key: _Optional[str] = ..., verdicts: _Optional[_Union[EvaluationVerdictCountsV1, _Mapping]] = ..., mean_score: _Optional[float] = ..., mean_score_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., scored_result_count: _Optional[int] = ...) -> None: ...

class EvaluationSliceV1(_message.Message):
    __slots__ = ("slice_key", "case_count", "candidates")
    SLICE_KEY_FIELD_NUMBER: _ClassVar[int]
    CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    slice_key: str
    case_count: int
    candidates: _containers.RepeatedCompositeFieldContainer[EvaluationSliceCandidateRowV1]
    def __init__(self, slice_key: _Optional[str] = ..., case_count: _Optional[int] = ..., candidates: _Optional[_Iterable[_Union[EvaluationSliceCandidateRowV1, _Mapping]]] = ...) -> None: ...

class EvaluationSliceAnalysisV1(_message.Message):
    __slots__ = ("dimension", "slices", "truncated_slice_count", "availability", "freshness")
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    SLICES_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_SLICE_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    dimension: EvaluationSliceDimensionV1
    slices: _containers.RepeatedCompositeFieldContainer[EvaluationSliceV1]
    truncated_slice_count: int
    availability: MetricAvailabilityV1
    freshness: EvaluationFreshnessV1
    def __init__(self, dimension: _Optional[_Union[EvaluationSliceDimensionV1, str]] = ..., slices: _Optional[_Iterable[_Union[EvaluationSliceV1, _Mapping]]] = ..., truncated_slice_count: _Optional[int] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class DataQualityFindingV1(_message.Message):
    __slots__ = ("kind", "severity", "method_name", "method_version", "false_positive_rate", "affected_case_ids", "policy_rule_version", "affected_count", "denominator")
    KIND_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    METHOD_VERSION_FIELD_NUMBER: _ClassVar[int]
    FALSE_POSITIVE_RATE_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_CASE_IDS_FIELD_NUMBER: _ClassVar[int]
    POLICY_RULE_VERSION_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    kind: DataQualityFindingKindV1
    severity: FindingSeverityV1
    method_name: str
    method_version: str
    false_positive_rate: float
    affected_case_ids: _containers.RepeatedScalarFieldContainer[str]
    policy_rule_version: str
    affected_count: int
    denominator: int
    def __init__(self, kind: _Optional[_Union[DataQualityFindingKindV1, str]] = ..., severity: _Optional[_Union[FindingSeverityV1, str]] = ..., method_name: _Optional[str] = ..., method_version: _Optional[str] = ..., false_positive_rate: _Optional[float] = ..., affected_case_ids: _Optional[_Iterable[str]] = ..., policy_rule_version: _Optional[str] = ..., affected_count: _Optional[int] = ..., denominator: _Optional[int] = ...) -> None: ...

class EvaluationDataQualityV1(_message.Message):
    __slots__ = ("findings", "case_count", "duplicate_case_count", "unscored_result_count", "aligned_case_count", "availability", "freshness")
    FINDINGS_FIELD_NUMBER: _ClassVar[int]
    CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    DUPLICATE_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNSCORED_RESULT_COUNT_FIELD_NUMBER: _ClassVar[int]
    ALIGNED_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    findings: _containers.RepeatedCompositeFieldContainer[DataQualityFindingV1]
    case_count: int
    duplicate_case_count: int
    unscored_result_count: int
    aligned_case_count: int
    availability: MetricAvailabilityV1
    freshness: EvaluationFreshnessV1
    def __init__(self, findings: _Optional[_Iterable[_Union[DataQualityFindingV1, _Mapping]]] = ..., case_count: _Optional[int] = ..., duplicate_case_count: _Optional[int] = ..., unscored_result_count: _Optional[int] = ..., aligned_case_count: _Optional[int] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class TotalMatchingV1(_message.Message):
    __slots__ = ("value", "exact")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXACT_FIELD_NUMBER: _ClassVar[int]
    value: int
    exact: bool
    def __init__(self, value: _Optional[int] = ..., exact: _Optional[bool] = ...) -> None: ...

class RegressionSeriesPointV1(_message.Message):
    __slots__ = ("ordinal", "evaluation_run_id", "state", "started_at", "finished_at", "verdicts", "mean_score", "mean_score_availability", "executed_cell_count", "candidate_cost", "is_current_run")
    ORDINAL_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    VERDICTS_FIELD_NUMBER: _ClassVar[int]
    MEAN_SCORE_FIELD_NUMBER: _ClassVar[int]
    MEAN_SCORE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_COST_FIELD_NUMBER: _ClassVar[int]
    IS_CURRENT_RUN_FIELD_NUMBER: _ClassVar[int]
    ordinal: int
    evaluation_run_id: str
    state: EvaluationRunStateV1
    started_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    verdicts: EvaluationVerdictCountsV1
    mean_score: float
    mean_score_availability: MetricAvailabilityV1
    executed_cell_count: int
    candidate_cost: CostAmountV1
    is_current_run: bool
    def __init__(self, ordinal: _Optional[int] = ..., evaluation_run_id: _Optional[str] = ..., state: _Optional[_Union[EvaluationRunStateV1, str]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., verdicts: _Optional[_Union[EvaluationVerdictCountsV1, _Mapping]] = ..., mean_score: _Optional[float] = ..., mean_score_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., executed_cell_count: _Optional[int] = ..., candidate_cost: _Optional[_Union[CostAmountV1, _Mapping]] = ..., is_current_run: _Optional[bool] = ...) -> None: ...

class EvaluationRegressionHistoryV1(_message.Message):
    __slots__ = ("points", "total_matching", "availability", "freshness")
    POINTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MATCHING_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    points: _containers.RepeatedCompositeFieldContainer[RegressionSeriesPointV1]
    total_matching: TotalMatchingV1
    availability: MetricAvailabilityV1
    freshness: EvaluationFreshnessV1
    def __init__(self, points: _Optional[_Iterable[_Union[RegressionSeriesPointV1, _Mapping]]] = ..., total_matching: _Optional[_Union[TotalMatchingV1, _Mapping]] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class DecisionBlockerV1(_message.Message):
    __slots__ = ("kind", "candidate_key", "score_config_id", "observed_value", "threshold_value", "detail")
    KIND_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_VALUE_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_VALUE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    kind: DecisionBlockerKindV1
    candidate_key: str
    score_config_id: str
    observed_value: float
    threshold_value: float
    detail: str
    def __init__(self, kind: _Optional[_Union[DecisionBlockerKindV1, str]] = ..., candidate_key: _Optional[str] = ..., score_config_id: _Optional[str] = ..., observed_value: _Optional[float] = ..., threshold_value: _Optional[float] = ..., detail: _Optional[str] = ...) -> None: ...

class CandidateTradeoffV1(_message.Message):
    __slots__ = ("candidate_key", "quality_delta", "cost_delta", "improved_case_count", "regressed_case_count", "corrected_p_value", "blocked", "instability_rate", "quality_delta_standard_error")
    CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    QUALITY_DELTA_FIELD_NUMBER: _ClassVar[int]
    COST_DELTA_FIELD_NUMBER: _ClassVar[int]
    IMPROVED_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    REGRESSED_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CORRECTED_P_VALUE_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_FIELD_NUMBER: _ClassVar[int]
    INSTABILITY_RATE_FIELD_NUMBER: _ClassVar[int]
    QUALITY_DELTA_STANDARD_ERROR_FIELD_NUMBER: _ClassVar[int]
    candidate_key: str
    quality_delta: float
    cost_delta: CostAmountV1
    improved_case_count: int
    regressed_case_count: int
    corrected_p_value: float
    blocked: bool
    instability_rate: float
    quality_delta_standard_error: float
    def __init__(self, candidate_key: _Optional[str] = ..., quality_delta: _Optional[float] = ..., cost_delta: _Optional[_Union[CostAmountV1, _Mapping]] = ..., improved_case_count: _Optional[int] = ..., regressed_case_count: _Optional[int] = ..., corrected_p_value: _Optional[float] = ..., blocked: _Optional[bool] = ..., instability_rate: _Optional[float] = ..., quality_delta_standard_error: _Optional[float] = ...) -> None: ...

class EvidencePostureV1(_message.Message):
    __slots__ = ("completeness", "aligned_case_count", "expected_case_count", "unscored_result_count", "awaiting_review_cell_count", "availability")
    COMPLETENESS_FIELD_NUMBER: _ClassVar[int]
    ALIGNED_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNSCORED_RESULT_COUNT_FIELD_NUMBER: _ClassVar[int]
    AWAITING_REVIEW_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    completeness: CompletenessStateV1
    aligned_case_count: int
    expected_case_count: int
    unscored_result_count: int
    awaiting_review_cell_count: int
    availability: MetricAvailabilityV1
    def __init__(self, completeness: _Optional[_Union[CompletenessStateV1, str]] = ..., aligned_case_count: _Optional[int] = ..., expected_case_count: _Optional[int] = ..., unscored_result_count: _Optional[int] = ..., awaiting_review_cell_count: _Optional[int] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class EvaluationDecisionV1(_message.Message):
    __slots__ = ("decision_policy_version", "outcome", "recommended_candidate_key", "reference_candidate_key", "tradeoffs", "blockers", "minimum_sample", "statistics", "evidence_posture", "provenance", "algorithm_version", "repeat_sample")
    DECISION_POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    TRADEOFFS_FIELD_NUMBER: _ClassVar[int]
    BLOCKERS_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_SAMPLE_FIELD_NUMBER: _ClassVar[int]
    STATISTICS_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_POSTURE_FIELD_NUMBER: _ClassVar[int]
    PROVENANCE_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_VERSION_FIELD_NUMBER: _ClassVar[int]
    REPEAT_SAMPLE_FIELD_NUMBER: _ClassVar[int]
    decision_policy_version: str
    outcome: EvaluationDecisionOutcomeV1
    recommended_candidate_key: str
    reference_candidate_key: str
    tradeoffs: _containers.RepeatedCompositeFieldContainer[CandidateTradeoffV1]
    blockers: _containers.RepeatedCompositeFieldContainer[DecisionBlockerV1]
    minimum_sample: MinimumSampleCheckV1
    statistics: StatisticalResultV1
    evidence_posture: EvidencePostureV1
    provenance: EvaluationDecisionProvenanceV1
    algorithm_version: str
    repeat_sample: RepeatSampleCheckV1
    def __init__(self, decision_policy_version: _Optional[str] = ..., outcome: _Optional[_Union[EvaluationDecisionOutcomeV1, str]] = ..., recommended_candidate_key: _Optional[str] = ..., reference_candidate_key: _Optional[str] = ..., tradeoffs: _Optional[_Iterable[_Union[CandidateTradeoffV1, _Mapping]]] = ..., blockers: _Optional[_Iterable[_Union[DecisionBlockerV1, _Mapping]]] = ..., minimum_sample: _Optional[_Union[MinimumSampleCheckV1, _Mapping]] = ..., statistics: _Optional[_Union[StatisticalResultV1, _Mapping]] = ..., evidence_posture: _Optional[_Union[EvidencePostureV1, _Mapping]] = ..., provenance: _Optional[_Union[EvaluationDecisionProvenanceV1, str]] = ..., algorithm_version: _Optional[str] = ..., repeat_sample: _Optional[_Union[RepeatSampleCheckV1, _Mapping]] = ...) -> None: ...

class EvaluationDecisionRevisionV1(_message.Message):
    __slots__ = ("id", "evaluation_run_id", "revision_ordinal", "evidence_projection_version", "decision_policy_version", "algorithm_version", "inputs_digest", "decision", "exclusions", "reason", "actor", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_ORDINAL_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_PROJECTION_VERSION_FIELD_NUMBER: _ClassVar[int]
    DECISION_POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_VERSION_FIELD_NUMBER: _ClassVar[int]
    INPUTS_DIGEST_FIELD_NUMBER: _ClassVar[int]
    DECISION_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIONS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    evaluation_run_id: str
    revision_ordinal: int
    evidence_projection_version: int
    decision_policy_version: str
    algorithm_version: str
    inputs_digest: bytes
    decision: EvaluationDecisionV1
    exclusions: _containers.RepeatedCompositeFieldContainer[EvaluationCellRefV1]
    reason: str
    actor: PrincipalRefV1
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., evaluation_run_id: _Optional[str] = ..., revision_ordinal: _Optional[int] = ..., evidence_projection_version: _Optional[int] = ..., decision_policy_version: _Optional[str] = ..., algorithm_version: _Optional[str] = ..., inputs_digest: _Optional[bytes] = ..., decision: _Optional[_Union[EvaluationDecisionV1, _Mapping]] = ..., exclusions: _Optional[_Iterable[_Union[EvaluationCellRefV1, _Mapping]]] = ..., reason: _Optional[str] = ..., actor: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EvaluationAdoptedDecisionV1(_message.Message):
    __slots__ = ("revision", "availability")
    REVISION_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    revision: EvaluationDecisionRevisionV1
    availability: MetricAvailabilityV1
    def __init__(self, revision: _Optional[_Union[EvaluationDecisionRevisionV1, _Mapping]] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class ReleaseAdoptionWarningV1(_message.Message):
    __slots__ = ("prior_revision_adopted_by_release", "release_ids", "availability")
    PRIOR_REVISION_ADOPTED_BY_RELEASE_FIELD_NUMBER: _ClassVar[int]
    RELEASE_IDS_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    prior_revision_adopted_by_release: bool
    release_ids: _containers.RepeatedScalarFieldContainer[str]
    availability: MetricAvailabilityV1
    def __init__(self, prior_revision_adopted_by_release: _Optional[bool] = ..., release_ids: _Optional[_Iterable[str]] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class EvaluationCostDriftV1(_message.Message):
    __slots__ = ("reserved_candidate_cost", "actual_candidate_cost", "drift_micros", "drift_ratio", "availability", "exceeds_reservation", "pricing_source_version", "priced_cell_count", "executed_cell_count", "provider_billed_cost", "billed_drift_micros", "billed_attempt_count", "metered_attempt_count")
    RESERVED_CANDIDATE_COST_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_CANDIDATE_COST_FIELD_NUMBER: _ClassVar[int]
    DRIFT_MICROS_FIELD_NUMBER: _ClassVar[int]
    DRIFT_RATIO_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    EXCEEDS_RESERVATION_FIELD_NUMBER: _ClassVar[int]
    PRICING_SOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    PRICED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_BILLED_COST_FIELD_NUMBER: _ClassVar[int]
    BILLED_DRIFT_MICROS_FIELD_NUMBER: _ClassVar[int]
    BILLED_ATTEMPT_COUNT_FIELD_NUMBER: _ClassVar[int]
    METERED_ATTEMPT_COUNT_FIELD_NUMBER: _ClassVar[int]
    reserved_candidate_cost: CostAmountV1
    actual_candidate_cost: CostAmountV1
    drift_micros: int
    drift_ratio: float
    availability: MetricAvailabilityV1
    exceeds_reservation: bool
    pricing_source_version: str
    priced_cell_count: int
    executed_cell_count: int
    provider_billed_cost: CostAmountV1
    billed_drift_micros: int
    billed_attempt_count: int
    metered_attempt_count: int
    def __init__(self, reserved_candidate_cost: _Optional[_Union[CostAmountV1, _Mapping]] = ..., actual_candidate_cost: _Optional[_Union[CostAmountV1, _Mapping]] = ..., drift_micros: _Optional[int] = ..., drift_ratio: _Optional[float] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., exceeds_reservation: _Optional[bool] = ..., pricing_source_version: _Optional[str] = ..., priced_cell_count: _Optional[int] = ..., executed_cell_count: _Optional[int] = ..., provider_billed_cost: _Optional[_Union[CostAmountV1, _Mapping]] = ..., billed_drift_micros: _Optional[int] = ..., billed_attempt_count: _Optional[int] = ..., metered_attempt_count: _Optional[int] = ...) -> None: ...

class GetEvaluationRunOverviewRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "profile")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    profile: EvaluationRunOverviewProfileV1
    def __init__(self, evaluation_run_id: _Optional[str] = ..., profile: _Optional[_Union[EvaluationRunOverviewProfileV1, str]] = ...) -> None: ...

class GetEvaluationRunOverviewResponse(_message.Message):
    __slots__ = ("run", "profile", "progress", "verdicts", "scorer_rollups", "failures", "decision_drivers", "throughput_availability", "budget_waterfall_availability", "leaderboard_availability", "comparability_availability", "data_quality_availability", "release_posture_availability", "allowed_actions", "capabilities", "freshness", "candidate_metrics_availability", "candidate_economics", "publication_lag_availability", "recovery", "cost_drift", "comparison", "slice_analysis", "data_quality", "regression_history", "adopted_decision", "manifest", "evaluator_economics", "scorer_suite_rollups")
    RUN_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    VERDICTS_FIELD_NUMBER: _ClassVar[int]
    SCORER_ROLLUPS_FIELD_NUMBER: _ClassVar[int]
    FAILURES_FIELD_NUMBER: _ClassVar[int]
    DECISION_DRIVERS_FIELD_NUMBER: _ClassVar[int]
    THROUGHPUT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    BUDGET_WATERFALL_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    LEADERBOARD_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    COMPARABILITY_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    DATA_QUALITY_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    RELEASE_POSTURE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_METRICS_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_ECONOMICS_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_LAG_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_FIELD_NUMBER: _ClassVar[int]
    COST_DRIFT_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_FIELD_NUMBER: _ClassVar[int]
    SLICE_ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    DATA_QUALITY_FIELD_NUMBER: _ClassVar[int]
    REGRESSION_HISTORY_FIELD_NUMBER: _ClassVar[int]
    ADOPTED_DECISION_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_ECONOMICS_FIELD_NUMBER: _ClassVar[int]
    SCORER_SUITE_ROLLUPS_FIELD_NUMBER: _ClassVar[int]
    run: EvaluationRunV1
    profile: EvaluationRunOverviewProfileV1
    progress: EvaluationRunProgressV1
    verdicts: EvaluationVerdictCountsV1
    scorer_rollups: _containers.RepeatedCompositeFieldContainer[EvaluationScorerRollupV1]
    failures: EvaluationRunFailureRollupV1
    decision_drivers: EvaluationDecisionDriversV1
    throughput_availability: MetricAvailabilityV1
    budget_waterfall_availability: MetricAvailabilityV1
    leaderboard_availability: MetricAvailabilityV1
    comparability_availability: MetricAvailabilityV1
    data_quality_availability: MetricAvailabilityV1
    release_posture_availability: MetricAvailabilityV1
    allowed_actions: _containers.RepeatedCompositeFieldContainer[AllowedActionV1]
    capabilities: AgenticEvaluationCapabilitiesV1
    freshness: EvaluationFreshnessV1
    candidate_metrics_availability: MetricAvailabilityV1
    candidate_economics: ExecutionMetricsV1
    publication_lag_availability: MetricAvailabilityV1
    recovery: EvaluationRunRecoveryV1
    cost_drift: EvaluationCostDriftV1
    comparison: EvaluationCandidateComparisonV1
    slice_analysis: EvaluationSliceAnalysisV1
    data_quality: EvaluationDataQualityV1
    regression_history: EvaluationRegressionHistoryV1
    adopted_decision: EvaluationAdoptedDecisionV1
    manifest: EvaluationRunManifestSectionV1
    evaluator_economics: ExecutionMetricsV1
    scorer_suite_rollups: _containers.RepeatedCompositeFieldContainer[EvaluationScorerSuiteRollupV1]
    def __init__(self, run: _Optional[_Union[EvaluationRunV1, _Mapping]] = ..., profile: _Optional[_Union[EvaluationRunOverviewProfileV1, str]] = ..., progress: _Optional[_Union[EvaluationRunProgressV1, _Mapping]] = ..., verdicts: _Optional[_Union[EvaluationVerdictCountsV1, _Mapping]] = ..., scorer_rollups: _Optional[_Iterable[_Union[EvaluationScorerRollupV1, _Mapping]]] = ..., failures: _Optional[_Union[EvaluationRunFailureRollupV1, _Mapping]] = ..., decision_drivers: _Optional[_Union[EvaluationDecisionDriversV1, _Mapping]] = ..., throughput_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., budget_waterfall_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., leaderboard_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., comparability_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., data_quality_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., release_posture_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., allowed_actions: _Optional[_Iterable[_Union[AllowedActionV1, _Mapping]]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., candidate_metrics_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., candidate_economics: _Optional[_Union[ExecutionMetricsV1, _Mapping]] = ..., publication_lag_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., recovery: _Optional[_Union[EvaluationRunRecoveryV1, _Mapping]] = ..., cost_drift: _Optional[_Union[EvaluationCostDriftV1, _Mapping]] = ..., comparison: _Optional[_Union[EvaluationCandidateComparisonV1, _Mapping]] = ..., slice_analysis: _Optional[_Union[EvaluationSliceAnalysisV1, _Mapping]] = ..., data_quality: _Optional[_Union[EvaluationDataQualityV1, _Mapping]] = ..., regression_history: _Optional[_Union[EvaluationRegressionHistoryV1, _Mapping]] = ..., adopted_decision: _Optional[_Union[EvaluationAdoptedDecisionV1, _Mapping]] = ..., manifest: _Optional[_Union[EvaluationRunManifestSectionV1, _Mapping]] = ..., evaluator_economics: _Optional[_Union[ExecutionMetricsV1, _Mapping]] = ..., scorer_suite_rollups: _Optional[_Iterable[_Union[EvaluationScorerSuiteRollupV1, _Mapping]]] = ...) -> None: ...

class PreviewEvaluationDecisionRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "evidence_projection_version", "policy", "exclusions")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_PROJECTION_VERSION_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIONS_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    evidence_projection_version: int
    policy: EvaluationDecisionPolicyV1
    exclusions: _containers.RepeatedCompositeFieldContainer[EvaluationCellRefV1]
    def __init__(self, evaluation_run_id: _Optional[str] = ..., evidence_projection_version: _Optional[int] = ..., policy: _Optional[_Union[EvaluationDecisionPolicyV1, _Mapping]] = ..., exclusions: _Optional[_Iterable[_Union[EvaluationCellRefV1, _Mapping]]] = ...) -> None: ...

class PreviewEvaluationDecisionResponse(_message.Message):
    __slots__ = ("decision", "comparison", "freshness", "capabilities")
    DECISION_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    decision: EvaluationDecisionV1
    comparison: EvaluationCandidateComparisonV1
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, decision: _Optional[_Union[EvaluationDecisionV1, _Mapping]] = ..., comparison: _Optional[_Union[EvaluationCandidateComparisonV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class AdoptEvaluationDecisionRevisionRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "evidence_projection_version", "policy", "exclusions", "reason", "idempotency_key")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_PROJECTION_VERSION_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIONS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    evidence_projection_version: int
    policy: EvaluationDecisionPolicyV1
    exclusions: _containers.RepeatedCompositeFieldContainer[EvaluationCellRefV1]
    reason: str
    idempotency_key: str
    def __init__(self, evaluation_run_id: _Optional[str] = ..., evidence_projection_version: _Optional[int] = ..., policy: _Optional[_Union[EvaluationDecisionPolicyV1, _Mapping]] = ..., exclusions: _Optional[_Iterable[_Union[EvaluationCellRefV1, _Mapping]]] = ..., reason: _Optional[str] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class AdoptEvaluationDecisionRevisionResponse(_message.Message):
    __slots__ = ("revision", "idempotent_replay", "release_adoption_warning")
    REVISION_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    RELEASE_ADOPTION_WARNING_FIELD_NUMBER: _ClassVar[int]
    revision: EvaluationDecisionRevisionV1
    idempotent_replay: bool
    release_adoption_warning: ReleaseAdoptionWarningV1
    def __init__(self, revision: _Optional[_Union[EvaluationDecisionRevisionV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ..., release_adoption_warning: _Optional[_Union[ReleaseAdoptionWarningV1, _Mapping]] = ...) -> None: ...

class EvaluationMatrixFilterV1(_message.Message):
    __slots__ = ("cohort_keys", "candidate_keys", "score_config_ids", "verdicts", "decision_impacts", "evidence_states", "trial", "blocking_gates_only")
    COHORT_KEYS_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_KEYS_FIELD_NUMBER: _ClassVar[int]
    SCORE_CONFIG_IDS_FIELD_NUMBER: _ClassVar[int]
    VERDICTS_FIELD_NUMBER: _ClassVar[int]
    DECISION_IMPACTS_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_STATES_FIELD_NUMBER: _ClassVar[int]
    TRIAL_FIELD_NUMBER: _ClassVar[int]
    BLOCKING_GATES_ONLY_FIELD_NUMBER: _ClassVar[int]
    cohort_keys: _containers.RepeatedScalarFieldContainer[str]
    candidate_keys: _containers.RepeatedScalarFieldContainer[str]
    score_config_ids: _containers.RepeatedScalarFieldContainer[str]
    verdicts: _containers.RepeatedScalarFieldContainer[EvaluationVerdictV1]
    decision_impacts: _containers.RepeatedScalarFieldContainer[EvaluationMatrixDecisionImpactV1]
    evidence_states: _containers.RepeatedScalarFieldContainer[EvaluationMatrixEvidenceStateV1]
    trial: int
    blocking_gates_only: bool
    def __init__(self, cohort_keys: _Optional[_Iterable[str]] = ..., candidate_keys: _Optional[_Iterable[str]] = ..., score_config_ids: _Optional[_Iterable[str]] = ..., verdicts: _Optional[_Iterable[_Union[EvaluationVerdictV1, str]]] = ..., decision_impacts: _Optional[_Iterable[_Union[EvaluationMatrixDecisionImpactV1, str]]] = ..., evidence_states: _Optional[_Iterable[_Union[EvaluationMatrixEvidenceStateV1, str]]] = ..., trial: _Optional[int] = ..., blocking_gates_only: _Optional[bool] = ...) -> None: ...

class EvaluationMatrixCellV1(_message.Message):
    __slots__ = ("candidate_key", "score_config_id", "config_key", "verdict", "score", "score_availability", "reference_verdict", "reference_score", "score_delta", "decision_impact", "evidence_state", "candidate_failure_code", "scorer_failure_code", "attempt_generation", "is_blocking_gate")
    CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SCORE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_VERDICT_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    SCORE_DELTA_FIELD_NUMBER: _ClassVar[int]
    DECISION_IMPACT_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_STATE_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_FAILURE_CODE_FIELD_NUMBER: _ClassVar[int]
    SCORER_FAILURE_CODE_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_GENERATION_FIELD_NUMBER: _ClassVar[int]
    IS_BLOCKING_GATE_FIELD_NUMBER: _ClassVar[int]
    candidate_key: str
    score_config_id: str
    config_key: str
    verdict: EvaluationVerdictV1
    score: float
    score_availability: MetricAvailabilityV1
    reference_verdict: EvaluationVerdictV1
    reference_score: float
    score_delta: float
    decision_impact: EvaluationMatrixDecisionImpactV1
    evidence_state: EvaluationMatrixEvidenceStateV1
    candidate_failure_code: str
    scorer_failure_code: str
    attempt_generation: int
    is_blocking_gate: bool
    def __init__(self, candidate_key: _Optional[str] = ..., score_config_id: _Optional[str] = ..., config_key: _Optional[str] = ..., verdict: _Optional[_Union[EvaluationVerdictV1, str]] = ..., score: _Optional[float] = ..., score_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., reference_verdict: _Optional[_Union[EvaluationVerdictV1, str]] = ..., reference_score: _Optional[float] = ..., score_delta: _Optional[float] = ..., decision_impact: _Optional[_Union[EvaluationMatrixDecisionImpactV1, str]] = ..., evidence_state: _Optional[_Union[EvaluationMatrixEvidenceStateV1, str]] = ..., candidate_failure_code: _Optional[str] = ..., scorer_failure_code: _Optional[str] = ..., attempt_generation: _Optional[int] = ..., is_blocking_gate: _Optional[bool] = ...) -> None: ...

class EvaluationMatrixRowV1(_message.Message):
    __slots__ = ("ordinal", "cohort_key", "case_revision_id", "trial", "decision_impact", "evidence_state", "cells", "result_count", "suite_cells")
    ORDINAL_FIELD_NUMBER: _ClassVar[int]
    COHORT_KEY_FIELD_NUMBER: _ClassVar[int]
    CASE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    TRIAL_FIELD_NUMBER: _ClassVar[int]
    DECISION_IMPACT_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_STATE_FIELD_NUMBER: _ClassVar[int]
    CELLS_FIELD_NUMBER: _ClassVar[int]
    RESULT_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUITE_CELLS_FIELD_NUMBER: _ClassVar[int]
    ordinal: int
    cohort_key: str
    case_revision_id: str
    trial: int
    decision_impact: EvaluationMatrixDecisionImpactV1
    evidence_state: EvaluationMatrixEvidenceStateV1
    cells: _containers.RepeatedCompositeFieldContainer[EvaluationMatrixCellV1]
    result_count: int
    suite_cells: _containers.RepeatedCompositeFieldContainer[EvaluationScorerSuiteCellV1]
    def __init__(self, ordinal: _Optional[int] = ..., cohort_key: _Optional[str] = ..., case_revision_id: _Optional[str] = ..., trial: _Optional[int] = ..., decision_impact: _Optional[_Union[EvaluationMatrixDecisionImpactV1, str]] = ..., evidence_state: _Optional[_Union[EvaluationMatrixEvidenceStateV1, str]] = ..., cells: _Optional[_Iterable[_Union[EvaluationMatrixCellV1, _Mapping]]] = ..., result_count: _Optional[int] = ..., suite_cells: _Optional[_Iterable[_Union[EvaluationScorerSuiteCellV1, _Mapping]]] = ...) -> None: ...

class EvaluationMatrixFacetV1(_message.Message):
    __slots__ = ("kind", "matching_row_count")
    KIND_FIELD_NUMBER: _ClassVar[int]
    MATCHING_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    kind: EvaluationMatrixFacetKindV1
    matching_row_count: int
    def __init__(self, kind: _Optional[_Union[EvaluationMatrixFacetKindV1, str]] = ..., matching_row_count: _Optional[int] = ...) -> None: ...

class EvaluationMatrixAlignmentV1(_message.Message):
    __slots__ = ("has_aligned_cases", "reason_code", "reference_candidate_key", "aligned_row_count", "repeat_sample")
    HAS_ALIGNED_CASES_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    ALIGNED_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    REPEAT_SAMPLE_FIELD_NUMBER: _ClassVar[int]
    has_aligned_cases: bool
    reason_code: str
    reference_candidate_key: str
    aligned_row_count: int
    repeat_sample: RepeatSampleCheckV1
    def __init__(self, has_aligned_cases: _Optional[bool] = ..., reason_code: _Optional[str] = ..., reference_candidate_key: _Optional[str] = ..., aligned_row_count: _Optional[int] = ..., repeat_sample: _Optional[_Union[RepeatSampleCheckV1, _Mapping]] = ...) -> None: ...

class MatrixSelectionExplicitIdsV1(_message.Message):
    __slots__ = ("cells",)
    CELLS_FIELD_NUMBER: _ClassVar[int]
    cells: _containers.RepeatedCompositeFieldContainer[EvaluationCellRefV1]
    def __init__(self, cells: _Optional[_Iterable[_Union[EvaluationCellRefV1, _Mapping]]] = ...) -> None: ...

class MatrixSelectionV1(_message.Message):
    __slots__ = ("explicit_ids", "frozen_filter_token")
    EXPLICIT_IDS_FIELD_NUMBER: _ClassVar[int]
    FROZEN_FILTER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    explicit_ids: MatrixSelectionExplicitIdsV1
    frozen_filter_token: str
    def __init__(self, explicit_ids: _Optional[_Union[MatrixSelectionExplicitIdsV1, _Mapping]] = ..., frozen_filter_token: _Optional[str] = ...) -> None: ...

class ListEvaluationMatrixRowsRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "page_token", "filter", "sort_key", "sort_direction", "page_size", "matrix_filter_token")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    SORT_KEY_FIELD_NUMBER: _ClassVar[int]
    SORT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    MATRIX_FILTER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    page_token: str
    filter: EvaluationMatrixFilterV1
    sort_key: EvaluationMatrixSortKeyV1
    sort_direction: _common_pb2.SortDirectionV1
    page_size: int
    matrix_filter_token: str
    def __init__(self, evaluation_run_id: _Optional[str] = ..., page_token: _Optional[str] = ..., filter: _Optional[_Union[EvaluationMatrixFilterV1, _Mapping]] = ..., sort_key: _Optional[_Union[EvaluationMatrixSortKeyV1, str]] = ..., sort_direction: _Optional[_Union[_common_pb2.SortDirectionV1, str]] = ..., page_size: _Optional[int] = ..., matrix_filter_token: _Optional[str] = ...) -> None: ...

class ListEvaluationMatrixRowsResponse(_message.Message):
    __slots__ = ("rows", "facets", "facets_availability", "total_matching", "next_page_token", "effective_page_size", "selection", "alignment", "resync", "sort_key", "sort_direction", "allowed_actions", "capabilities", "freshness")
    ROWS_FIELD_NUMBER: _ClassVar[int]
    FACETS_FIELD_NUMBER: _ClassVar[int]
    FACETS_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MATCHING_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    SELECTION_FIELD_NUMBER: _ClassVar[int]
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    RESYNC_FIELD_NUMBER: _ClassVar[int]
    SORT_KEY_FIELD_NUMBER: _ClassVar[int]
    SORT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    rows: _containers.RepeatedCompositeFieldContainer[EvaluationMatrixRowV1]
    facets: _containers.RepeatedCompositeFieldContainer[EvaluationMatrixFacetV1]
    facets_availability: MetricAvailabilityV1
    total_matching: TotalMatchingV1
    next_page_token: str
    effective_page_size: int
    selection: MatrixSelectionV1
    alignment: EvaluationMatrixAlignmentV1
    resync: EvaluationCursorResyncV1
    sort_key: EvaluationMatrixSortKeyV1
    sort_direction: _common_pb2.SortDirectionV1
    allowed_actions: _containers.RepeatedCompositeFieldContainer[AllowedActionV1]
    capabilities: AgenticEvaluationCapabilitiesV1
    freshness: EvaluationFreshnessV1
    def __init__(self, rows: _Optional[_Iterable[_Union[EvaluationMatrixRowV1, _Mapping]]] = ..., facets: _Optional[_Iterable[_Union[EvaluationMatrixFacetV1, _Mapping]]] = ..., facets_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., total_matching: _Optional[_Union[TotalMatchingV1, _Mapping]] = ..., next_page_token: _Optional[str] = ..., effective_page_size: _Optional[int] = ..., selection: _Optional[_Union[MatrixSelectionV1, _Mapping]] = ..., alignment: _Optional[_Union[EvaluationMatrixAlignmentV1, _Mapping]] = ..., resync: _Optional[_Union[EvaluationCursorResyncV1, _Mapping]] = ..., sort_key: _Optional[_Union[EvaluationMatrixSortKeyV1, str]] = ..., sort_direction: _Optional[_Union[_common_pb2.SortDirectionV1, str]] = ..., allowed_actions: _Optional[_Iterable[_Union[AllowedActionV1, _Mapping]]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class EvaluationCaseContextV1(_message.Message):
    __slots__ = ("case_revision_id", "dataset_version_id", "cohort_key", "subject_preview", "subject_availability", "expected_outcome_preview", "expected_outcome_availability", "subject_truncated", "expected_outcome_truncated")
    CASE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    COHORT_KEY_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTCOME_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTCOME_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTCOME_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    case_revision_id: str
    dataset_version_id: str
    cohort_key: str
    subject_preview: str
    subject_availability: MetricAvailabilityV1
    expected_outcome_preview: str
    expected_outcome_availability: MetricAvailabilityV1
    subject_truncated: bool
    expected_outcome_truncated: bool
    def __init__(self, case_revision_id: _Optional[str] = ..., dataset_version_id: _Optional[str] = ..., cohort_key: _Optional[str] = ..., subject_preview: _Optional[str] = ..., subject_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., expected_outcome_preview: _Optional[str] = ..., expected_outcome_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., subject_truncated: _Optional[bool] = ..., expected_outcome_truncated: _Optional[bool] = ...) -> None: ...

class EvaluationCandidateAttemptDetailV1(_message.Message):
    __slots__ = ("attempt_ordinal", "state", "failure", "provider_status", "latency_micros", "cost", "tokens", "provider_billed_cost")
    ATTEMPT_ORDINAL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_STATUS_FIELD_NUMBER: _ClassVar[int]
    LATENCY_MICROS_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_BILLED_COST_FIELD_NUMBER: _ClassVar[int]
    attempt_ordinal: int
    state: EvaluationExecutionStateV1
    failure: EvaluationFailureV1
    provider_status: ProviderStatusV1
    latency_micros: int
    cost: CostAmountV1
    tokens: TokenUsageV1
    provider_billed_cost: CostAmountV1
    def __init__(self, attempt_ordinal: _Optional[int] = ..., state: _Optional[_Union[EvaluationExecutionStateV1, str]] = ..., failure: _Optional[_Union[EvaluationFailureV1, _Mapping]] = ..., provider_status: _Optional[_Union[ProviderStatusV1, _Mapping]] = ..., latency_micros: _Optional[int] = ..., cost: _Optional[_Union[CostAmountV1, _Mapping]] = ..., tokens: _Optional[_Union[TokenUsageV1, _Mapping]] = ..., provider_billed_cost: _Optional[_Union[CostAmountV1, _Mapping]] = ...) -> None: ...

class EvaluationCandidateExecutionDetailV1(_message.Message):
    __slots__ = ("candidate_key", "candidate_source", "state", "attempts", "attempt_generation", "failure", "metrics", "availability")
    CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_GENERATION_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    candidate_key: str
    candidate_source: EvaluationCandidateSourceV1
    state: EvaluationExecutionStateV1
    attempts: _containers.RepeatedCompositeFieldContainer[EvaluationCandidateAttemptDetailV1]
    attempt_generation: int
    failure: EvaluationFailureV1
    metrics: ExecutionMetricsV1
    availability: MetricAvailabilityV1
    def __init__(self, candidate_key: _Optional[str] = ..., candidate_source: _Optional[_Union[EvaluationCandidateSourceV1, str]] = ..., state: _Optional[_Union[EvaluationExecutionStateV1, str]] = ..., attempts: _Optional[_Iterable[_Union[EvaluationCandidateAttemptDetailV1, _Mapping]]] = ..., attempt_generation: _Optional[int] = ..., failure: _Optional[_Union[EvaluationFailureV1, _Mapping]] = ..., metrics: _Optional[_Union[ExecutionMetricsV1, _Mapping]] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class EvaluationScorerEvidenceV1(_message.Message):
    __slots__ = ("score_config_id", "config_key", "metric_name", "verdict", "score", "score_availability", "score_reason_code", "is_blocking_gate", "failure", "duration_micros", "attempt_generation", "is_superseded", "evaluator_execution", "attempt_economics", "attempt_economics_total", "attempt_economics_availability")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SCORE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    SCORE_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    IS_BLOCKING_GATE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    DURATION_MICROS_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_GENERATION_FIELD_NUMBER: _ClassVar[int]
    IS_SUPERSEDED_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_ECONOMICS_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_ECONOMICS_TOTAL_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_ECONOMICS_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    config_key: str
    metric_name: str
    verdict: EvaluationVerdictV1
    score: float
    score_availability: MetricAvailabilityV1
    score_reason_code: str
    is_blocking_gate: bool
    failure: EvaluationFailureV1
    duration_micros: int
    attempt_generation: int
    is_superseded: bool
    evaluator_execution: ExecutionMetricsV1
    attempt_economics: _containers.RepeatedCompositeFieldContainer[EvaluationScorerAttemptEconomicsV1]
    attempt_economics_total: CostAmountV1
    attempt_economics_availability: MetricAvailabilityV1
    def __init__(self, score_config_id: _Optional[str] = ..., config_key: _Optional[str] = ..., metric_name: _Optional[str] = ..., verdict: _Optional[_Union[EvaluationVerdictV1, str]] = ..., score: _Optional[float] = ..., score_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., score_reason_code: _Optional[str] = ..., is_blocking_gate: _Optional[bool] = ..., failure: _Optional[_Union[EvaluationFailureV1, _Mapping]] = ..., duration_micros: _Optional[int] = ..., attempt_generation: _Optional[int] = ..., is_superseded: _Optional[bool] = ..., evaluator_execution: _Optional[_Union[ExecutionMetricsV1, _Mapping]] = ..., attempt_economics: _Optional[_Iterable[_Union[EvaluationScorerAttemptEconomicsV1, _Mapping]]] = ..., attempt_economics_total: _Optional[_Union[CostAmountV1, _Mapping]] = ..., attempt_economics_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class EvaluationScorerAttemptEconomicsV1(_message.Message):
    __slots__ = ("scorer_attempt", "origin", "regrade_job_id", "is_superseded", "evaluator_execution", "economics_availability")
    SCORER_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    REGRADE_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    IS_SUPERSEDED_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    ECONOMICS_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    scorer_attempt: int
    origin: EvaluationScorerAttemptOriginV1
    regrade_job_id: str
    is_superseded: bool
    evaluator_execution: ExecutionMetricsV1
    economics_availability: MetricAvailabilityV1
    def __init__(self, scorer_attempt: _Optional[int] = ..., origin: _Optional[_Union[EvaluationScorerAttemptOriginV1, str]] = ..., regrade_job_id: _Optional[str] = ..., is_superseded: _Optional[bool] = ..., evaluator_execution: _Optional[_Union[ExecutionMetricsV1, _Mapping]] = ..., economics_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class EvaluationArtifactSummaryV1(_message.Message):
    __slots__ = ("artifact_id", "media_type", "byte_size", "content_digest", "content_availability")
    ARTIFACT_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
    BYTE_SIZE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DIGEST_FIELD_NUMBER: _ClassVar[int]
    CONTENT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    artifact_id: str
    media_type: str
    byte_size: int
    content_digest: str
    content_availability: MetricAvailabilityV1
    def __init__(self, artifact_id: _Optional[str] = ..., media_type: _Optional[str] = ..., byte_size: _Optional[int] = ..., content_digest: _Optional[str] = ..., content_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class EvaluationCellDetailV1(_message.Message):
    __slots__ = ("cell", "ordinal", "case_context", "candidate_execution", "scorer_evidence", "artifacts", "artifacts_availability", "evidence_state", "freshness")
    CELL_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_FIELD_NUMBER: _ClassVar[int]
    CASE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    SCORER_EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    ARTIFACTS_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_STATE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    cell: EvaluationCellRefV1
    ordinal: int
    case_context: EvaluationCaseContextV1
    candidate_execution: EvaluationCandidateExecutionDetailV1
    scorer_evidence: _containers.RepeatedCompositeFieldContainer[EvaluationScorerEvidenceV1]
    artifacts: _containers.RepeatedCompositeFieldContainer[EvaluationArtifactSummaryV1]
    artifacts_availability: MetricAvailabilityV1
    evidence_state: EvaluationMatrixEvidenceStateV1
    freshness: EvaluationFreshnessV1
    def __init__(self, cell: _Optional[_Union[EvaluationCellRefV1, _Mapping]] = ..., ordinal: _Optional[int] = ..., case_context: _Optional[_Union[EvaluationCaseContextV1, _Mapping]] = ..., candidate_execution: _Optional[_Union[EvaluationCandidateExecutionDetailV1, _Mapping]] = ..., scorer_evidence: _Optional[_Iterable[_Union[EvaluationScorerEvidenceV1, _Mapping]]] = ..., artifacts: _Optional[_Iterable[_Union[EvaluationArtifactSummaryV1, _Mapping]]] = ..., artifacts_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., evidence_state: _Optional[_Union[EvaluationMatrixEvidenceStateV1, str]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class BatchGetEvaluationCellDetailsRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "selection", "candidate_keys")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    SELECTION_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_KEYS_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    selection: MatrixSelectionV1
    candidate_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, evaluation_run_id: _Optional[str] = ..., selection: _Optional[_Union[MatrixSelectionV1, _Mapping]] = ..., candidate_keys: _Optional[_Iterable[str]] = ...) -> None: ...

class BatchGetEvaluationCellDetailsResponse(_message.Message):
    __slots__ = ("cells", "missing", "previous_page_token", "next_page_token", "total_matching", "evidence_source", "fact_plane_availability", "allowed_actions", "capabilities", "freshness")
    CELLS_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MATCHING_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    FACT_PLANE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    cells: _containers.RepeatedCompositeFieldContainer[EvaluationCellDetailV1]
    missing: _containers.RepeatedCompositeFieldContainer[EvaluationCellRefV1]
    previous_page_token: str
    next_page_token: str
    total_matching: TotalMatchingV1
    evidence_source: EvaluationCellEvidenceSourceV1
    fact_plane_availability: MetricAvailabilityV1
    allowed_actions: _containers.RepeatedCompositeFieldContainer[AllowedActionV1]
    capabilities: AgenticEvaluationCapabilitiesV1
    freshness: EvaluationFreshnessV1
    def __init__(self, cells: _Optional[_Iterable[_Union[EvaluationCellDetailV1, _Mapping]]] = ..., missing: _Optional[_Iterable[_Union[EvaluationCellRefV1, _Mapping]]] = ..., previous_page_token: _Optional[str] = ..., next_page_token: _Optional[str] = ..., total_matching: _Optional[_Union[TotalMatchingV1, _Mapping]] = ..., evidence_source: _Optional[_Union[EvaluationCellEvidenceSourceV1, str]] = ..., fact_plane_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., allowed_actions: _Optional[_Iterable[_Union[AllowedActionV1, _Mapping]]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class EvaluationRunProgressChangeV1(_message.Message):
    __slots__ = ("run_state", "projection_version", "expected_cell_count", "executed_cell_count", "succeeded_cell_count", "failed_cell_count", "cancelled_cell_count", "awaiting_review_cell_count")
    RUN_STATE_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUCCEEDED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    AWAITING_REVIEW_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    run_state: EvaluationRunStateV1
    projection_version: int
    expected_cell_count: int
    executed_cell_count: int
    succeeded_cell_count: int
    failed_cell_count: int
    cancelled_cell_count: int
    awaiting_review_cell_count: int
    def __init__(self, run_state: _Optional[_Union[EvaluationRunStateV1, str]] = ..., projection_version: _Optional[int] = ..., expected_cell_count: _Optional[int] = ..., executed_cell_count: _Optional[int] = ..., succeeded_cell_count: _Optional[int] = ..., failed_cell_count: _Optional[int] = ..., cancelled_cell_count: _Optional[int] = ..., awaiting_review_cell_count: _Optional[int] = ...) -> None: ...

class EvaluationCellDeltaV1(_message.Message):
    __slots__ = ("cell", "state", "attempt_generation")
    CELL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_GENERATION_FIELD_NUMBER: _ClassVar[int]
    cell: EvaluationCellRefV1
    state: EvaluationExecutionStateV1
    attempt_generation: int
    def __init__(self, cell: _Optional[_Union[EvaluationCellRefV1, _Mapping]] = ..., state: _Optional[_Union[EvaluationExecutionStateV1, str]] = ..., attempt_generation: _Optional[int] = ...) -> None: ...

class EvaluationCellBatchChangeV1(_message.Message):
    __slots__ = ("deltas", "truncated_by_page_cap")
    DELTAS_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_BY_PAGE_CAP_FIELD_NUMBER: _ClassVar[int]
    deltas: _containers.RepeatedCompositeFieldContainer[EvaluationCellDeltaV1]
    truncated_by_page_cap: bool
    def __init__(self, deltas: _Optional[_Iterable[_Union[EvaluationCellDeltaV1, _Mapping]]] = ..., truncated_by_page_cap: _Optional[bool] = ...) -> None: ...

class EvaluationSectionRefreshedChangeV1(_message.Message):
    __slots__ = ("section_key", "score_config_id", "projection_version")
    SECTION_KEY_FIELD_NUMBER: _ClassVar[int]
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_VERSION_FIELD_NUMBER: _ClassVar[int]
    section_key: str
    score_config_id: str
    projection_version: int
    def __init__(self, section_key: _Optional[str] = ..., score_config_id: _Optional[str] = ..., projection_version: _Optional[int] = ...) -> None: ...

class EvaluationDecisionRevisionChangeV1(_message.Message):
    __slots__ = ("decision_revision_id", "revision_ordinal", "evidence_revision")
    DECISION_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_ORDINAL_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_REVISION_FIELD_NUMBER: _ClassVar[int]
    decision_revision_id: str
    revision_ordinal: int
    evidence_revision: int
    def __init__(self, decision_revision_id: _Optional[str] = ..., revision_ordinal: _Optional[int] = ..., evidence_revision: _Optional[int] = ...) -> None: ...

class EvaluationTerminalChangeV1(_message.Message):
    __slots__ = ("run_state", "executed_cell_count", "succeeded_cell_count", "failed_cell_count", "cancelled_cell_count", "completed_evidence_preserved")
    RUN_STATE_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUCCEEDED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_EVIDENCE_PRESERVED_FIELD_NUMBER: _ClassVar[int]
    run_state: EvaluationRunStateV1
    executed_cell_count: int
    succeeded_cell_count: int
    failed_cell_count: int
    cancelled_cell_count: int
    completed_evidence_preserved: bool
    def __init__(self, run_state: _Optional[_Union[EvaluationRunStateV1, str]] = ..., executed_cell_count: _Optional[int] = ..., succeeded_cell_count: _Optional[int] = ..., failed_cell_count: _Optional[int] = ..., cancelled_cell_count: _Optional[int] = ..., completed_evidence_preserved: _Optional[bool] = ...) -> None: ...

class EvaluationChangeResyncV1(_message.Message):
    __slots__ = ("reason", "reason_code", "pending_change_estimate", "refetch_overview_required")
    REASON_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    PENDING_CHANGE_ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    REFETCH_OVERVIEW_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    reason: EvaluationResyncReasonV1
    reason_code: str
    pending_change_estimate: int
    refetch_overview_required: bool
    def __init__(self, reason: _Optional[_Union[EvaluationResyncReasonV1, str]] = ..., reason_code: _Optional[str] = ..., pending_change_estimate: _Optional[int] = ..., refetch_overview_required: _Optional[bool] = ...) -> None: ...

class EvaluationChangeReplayGapV1(_message.Message):
    __slots__ = ("expected_sequence", "available_from_sequence", "reason_code", "refetch_overview_required")
    EXPECTED_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FROM_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    REFETCH_OVERVIEW_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    expected_sequence: int
    available_from_sequence: int
    reason_code: str
    refetch_overview_required: bool
    def __init__(self, expected_sequence: _Optional[int] = ..., available_from_sequence: _Optional[int] = ..., reason_code: _Optional[str] = ..., refetch_overview_required: _Optional[bool] = ...) -> None: ...

class EvaluationRunChangeV1(_message.Message):
    __slots__ = ("sequence", "recorded_at", "kind", "progress", "cell_batch", "section_refreshed", "decision_revision", "terminal", "resync_required", "replay_gap")
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    RECORDED_AT_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CELL_BATCH_FIELD_NUMBER: _ClassVar[int]
    SECTION_REFRESHED_FIELD_NUMBER: _ClassVar[int]
    DECISION_REVISION_FIELD_NUMBER: _ClassVar[int]
    TERMINAL_FIELD_NUMBER: _ClassVar[int]
    RESYNC_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    REPLAY_GAP_FIELD_NUMBER: _ClassVar[int]
    sequence: int
    recorded_at: _timestamp_pb2.Timestamp
    kind: EvaluationRunChangeKindV1
    progress: EvaluationRunProgressChangeV1
    cell_batch: EvaluationCellBatchChangeV1
    section_refreshed: EvaluationSectionRefreshedChangeV1
    decision_revision: EvaluationDecisionRevisionChangeV1
    terminal: EvaluationTerminalChangeV1
    resync_required: EvaluationChangeResyncV1
    replay_gap: EvaluationChangeReplayGapV1
    def __init__(self, sequence: _Optional[int] = ..., recorded_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., kind: _Optional[_Union[EvaluationRunChangeKindV1, str]] = ..., progress: _Optional[_Union[EvaluationRunProgressChangeV1, _Mapping]] = ..., cell_batch: _Optional[_Union[EvaluationCellBatchChangeV1, _Mapping]] = ..., section_refreshed: _Optional[_Union[EvaluationSectionRefreshedChangeV1, _Mapping]] = ..., decision_revision: _Optional[_Union[EvaluationDecisionRevisionChangeV1, _Mapping]] = ..., terminal: _Optional[_Union[EvaluationTerminalChangeV1, _Mapping]] = ..., resync_required: _Optional[_Union[EvaluationChangeResyncV1, _Mapping]] = ..., replay_gap: _Optional[_Union[EvaluationChangeReplayGapV1, _Mapping]] = ...) -> None: ...

class ListEvaluationRunChangesRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "cursor", "page_size")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    cursor: str
    page_size: int
    def __init__(self, evaluation_run_id: _Optional[str] = ..., cursor: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListEvaluationRunChangesResponse(_message.Message):
    __slots__ = ("changes", "next_cursor", "has_more", "evidence_revision", "run_terminal", "effective_page_size", "allowed_actions", "capabilities", "freshness")
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_REVISION_FIELD_NUMBER: _ClassVar[int]
    RUN_TERMINAL_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[EvaluationRunChangeV1]
    next_cursor: str
    has_more: bool
    evidence_revision: int
    run_terminal: bool
    effective_page_size: int
    allowed_actions: _containers.RepeatedCompositeFieldContainer[AllowedActionV1]
    capabilities: AgenticEvaluationCapabilitiesV1
    freshness: EvaluationFreshnessV1
    def __init__(self, changes: _Optional[_Iterable[_Union[EvaluationRunChangeV1, _Mapping]]] = ..., next_cursor: _Optional[str] = ..., has_more: _Optional[bool] = ..., evidence_revision: _Optional[int] = ..., run_terminal: _Optional[bool] = ..., effective_page_size: _Optional[int] = ..., allowed_actions: _Optional[_Iterable[_Union[AllowedActionV1, _Mapping]]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class EvaluationArtifactContentRefV1(_message.Message):
    __slots__ = ("artifact_id", "content_digest")
    ARTIFACT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DIGEST_FIELD_NUMBER: _ClassVar[int]
    artifact_id: str
    content_digest: str
    def __init__(self, artifact_id: _Optional[str] = ..., content_digest: _Optional[str] = ...) -> None: ...

class EvaluationArtifactRemediationV1(_message.Message):
    __slots__ = ("kind", "reason_code", "detail")
    KIND_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    kind: EvaluationArtifactRemediationKindV1
    reason_code: str
    detail: str
    def __init__(self, kind: _Optional[_Union[EvaluationArtifactRemediationKindV1, str]] = ..., reason_code: _Optional[str] = ..., detail: _Optional[str] = ...) -> None: ...

class EvaluationArtifactContentV1(_message.Message):
    __slots__ = ("artifact_id", "state", "media_type", "content_digest", "byte_size", "content", "truncated", "availability", "remediation")
    ARTIFACT_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DIGEST_FIELD_NUMBER: _ClassVar[int]
    BYTE_SIZE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    REMEDIATION_FIELD_NUMBER: _ClassVar[int]
    artifact_id: str
    state: EvaluationArtifactContentStateV1
    media_type: str
    content_digest: str
    byte_size: int
    content: bytes
    truncated: bool
    availability: MetricAvailabilityV1
    remediation: EvaluationArtifactRemediationV1
    def __init__(self, artifact_id: _Optional[str] = ..., state: _Optional[_Union[EvaluationArtifactContentStateV1, str]] = ..., media_type: _Optional[str] = ..., content_digest: _Optional[str] = ..., byte_size: _Optional[int] = ..., content: _Optional[bytes] = ..., truncated: _Optional[bool] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., remediation: _Optional[_Union[EvaluationArtifactRemediationV1, _Mapping]] = ...) -> None: ...

class GetEvaluationArtifactContentRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "cell", "artifact")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    cell: EvaluationCellRefV1
    artifact: EvaluationArtifactContentRefV1
    def __init__(self, evaluation_run_id: _Optional[str] = ..., cell: _Optional[_Union[EvaluationCellRefV1, _Mapping]] = ..., artifact: _Optional[_Union[EvaluationArtifactContentRefV1, _Mapping]] = ...) -> None: ...

class GetEvaluationArtifactContentResponse(_message.Message):
    __slots__ = ("content", "allowed_actions", "capabilities", "freshness")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    content: EvaluationArtifactContentV1
    allowed_actions: _containers.RepeatedCompositeFieldContainer[AllowedActionV1]
    capabilities: AgenticEvaluationCapabilitiesV1
    freshness: EvaluationFreshnessV1
    def __init__(self, content: _Optional[_Union[EvaluationArtifactContentV1, _Mapping]] = ..., allowed_actions: _Optional[_Iterable[_Union[AllowedActionV1, _Mapping]]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class BatchGetEvaluationArtifactContentsRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "cell", "artifacts")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_FIELD_NUMBER: _ClassVar[int]
    ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    cell: EvaluationCellRefV1
    artifacts: _containers.RepeatedCompositeFieldContainer[EvaluationArtifactContentRefV1]
    def __init__(self, evaluation_run_id: _Optional[str] = ..., cell: _Optional[_Union[EvaluationCellRefV1, _Mapping]] = ..., artifacts: _Optional[_Iterable[_Union[EvaluationArtifactContentRefV1, _Mapping]]] = ...) -> None: ...

class BatchGetEvaluationArtifactContentsResponse(_message.Message):
    __slots__ = ("contents", "total_content_bytes", "byte_budget", "allowed_actions", "capabilities", "freshness")
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CONTENT_BYTES_FIELD_NUMBER: _ClassVar[int]
    BYTE_BUDGET_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    contents: _containers.RepeatedCompositeFieldContainer[EvaluationArtifactContentV1]
    total_content_bytes: int
    byte_budget: int
    allowed_actions: _containers.RepeatedCompositeFieldContainer[AllowedActionV1]
    capabilities: AgenticEvaluationCapabilitiesV1
    freshness: EvaluationFreshnessV1
    def __init__(self, contents: _Optional[_Iterable[_Union[EvaluationArtifactContentV1, _Mapping]]] = ..., total_content_bytes: _Optional[int] = ..., byte_budget: _Optional[int] = ..., allowed_actions: _Optional[_Iterable[_Union[AllowedActionV1, _Mapping]]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class ConfigurationDiffEntryV1(_message.Message):
    __slots__ = ("dimension", "subject_key", "reference_value", "candidate_value", "value_truncated", "reference_value_digest", "candidate_value_digest")
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_KEY_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_VALUE_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_VALUE_DIGEST_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_VALUE_DIGEST_FIELD_NUMBER: _ClassVar[int]
    dimension: ConfigurationDimensionV1
    subject_key: str
    reference_value: MetadataValueV1
    candidate_value: MetadataValueV1
    value_truncated: bool
    reference_value_digest: str
    candidate_value_digest: str
    def __init__(self, dimension: _Optional[_Union[ConfigurationDimensionV1, str]] = ..., subject_key: _Optional[str] = ..., reference_value: _Optional[_Union[MetadataValueV1, _Mapping]] = ..., candidate_value: _Optional[_Union[MetadataValueV1, _Mapping]] = ..., value_truncated: _Optional[bool] = ..., reference_value_digest: _Optional[str] = ..., candidate_value_digest: _Optional[str] = ...) -> None: ...

class EvaluationConfigurationDiffV1(_message.Message):
    __slots__ = ("reference_evaluation_run_id", "reference_definition_revision_id", "entries", "truncated", "total_entry_count", "availability")
    REFERENCE_EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_DEFINITION_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ENTRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    reference_evaluation_run_id: str
    reference_definition_revision_id: str
    entries: _containers.RepeatedCompositeFieldContainer[ConfigurationDiffEntryV1]
    truncated: bool
    total_entry_count: int
    availability: MetricAvailabilityV1
    def __init__(self, reference_evaluation_run_id: _Optional[str] = ..., reference_definition_revision_id: _Optional[str] = ..., entries: _Optional[_Iterable[_Union[ConfigurationDiffEntryV1, _Mapping]]] = ..., truncated: _Optional[bool] = ..., total_entry_count: _Optional[int] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class EvaluationAuditEntryV1(_message.Message):
    __slots__ = ("sequence", "kind", "actor", "occurred_at", "details")
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    sequence: int
    kind: EvaluationAuditEventKindV1
    actor: PrincipalRefV1
    occurred_at: _timestamp_pb2.Timestamp
    details: _containers.RepeatedCompositeFieldContainer[MetadataEntryV1]
    def __init__(self, sequence: _Optional[int] = ..., kind: _Optional[_Union[EvaluationAuditEventKindV1, str]] = ..., actor: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., details: _Optional[_Iterable[_Union[MetadataEntryV1, _Mapping]]] = ...) -> None: ...

class EvaluationRunManifestSectionV1(_message.Message):
    __slots__ = ("definition_revision_id", "definition_content_digest", "manifest_schema_version", "configuration_diff", "scorers", "decision_policy_version", "pricing_source", "pricing_source_availability", "evidence_projection_version", "adopted_decision_revision_id", "release_adoption", "audit", "audit_next_cursor", "audit_has_more", "freshness", "availability")
    DEFINITION_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_CONTENT_DIGEST_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_DIFF_FIELD_NUMBER: _ClassVar[int]
    SCORERS_FIELD_NUMBER: _ClassVar[int]
    DECISION_POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    PRICING_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PRICING_SOURCE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_PROJECTION_VERSION_FIELD_NUMBER: _ClassVar[int]
    ADOPTED_DECISION_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_ADOPTION_FIELD_NUMBER: _ClassVar[int]
    AUDIT_FIELD_NUMBER: _ClassVar[int]
    AUDIT_NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    AUDIT_HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    definition_revision_id: str
    definition_content_digest: str
    manifest_schema_version: int
    configuration_diff: EvaluationConfigurationDiffV1
    scorers: _containers.RepeatedCompositeFieldContainer[EvaluationScorerVersionSnapshotV1]
    decision_policy_version: str
    pricing_source: EvaluationPricingSourceV1
    pricing_source_availability: MetricAvailabilityV1
    evidence_projection_version: int
    adopted_decision_revision_id: str
    release_adoption: ReleaseAdoptionWarningV1
    audit: _containers.RepeatedCompositeFieldContainer[EvaluationAuditEntryV1]
    audit_next_cursor: str
    audit_has_more: bool
    freshness: EvaluationFreshnessV1
    availability: MetricAvailabilityV1
    def __init__(self, definition_revision_id: _Optional[str] = ..., definition_content_digest: _Optional[str] = ..., manifest_schema_version: _Optional[int] = ..., configuration_diff: _Optional[_Union[EvaluationConfigurationDiffV1, _Mapping]] = ..., scorers: _Optional[_Iterable[_Union[EvaluationScorerVersionSnapshotV1, _Mapping]]] = ..., decision_policy_version: _Optional[str] = ..., pricing_source: _Optional[_Union[EvaluationPricingSourceV1, _Mapping]] = ..., pricing_source_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., evidence_projection_version: _Optional[int] = ..., adopted_decision_revision_id: _Optional[str] = ..., release_adoption: _Optional[_Union[ReleaseAdoptionWarningV1, _Mapping]] = ..., audit: _Optional[_Iterable[_Union[EvaluationAuditEntryV1, _Mapping]]] = ..., audit_next_cursor: _Optional[str] = ..., audit_has_more: _Optional[bool] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class EvaluationReviewUnitV1(_message.Message):
    __slots__ = ("review_unit_id", "evaluation_run_id", "cell", "scorer_key", "scorer_version", "completion_state", "adjudication_state", "submitted_count", "required_count", "blocking_effect_code", "blind_posture", "pairwise", "dataset_proposed_case_id")
    REVIEW_UNIT_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_FIELD_NUMBER: _ClassVar[int]
    SCORER_KEY_FIELD_NUMBER: _ClassVar[int]
    SCORER_VERSION_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_STATE_FIELD_NUMBER: _ClassVar[int]
    ADJUDICATION_STATE_FIELD_NUMBER: _ClassVar[int]
    SUBMITTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_COUNT_FIELD_NUMBER: _ClassVar[int]
    BLOCKING_EFFECT_CODE_FIELD_NUMBER: _ClassVar[int]
    BLIND_POSTURE_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_FIELD_NUMBER: _ClassVar[int]
    DATASET_PROPOSED_CASE_ID_FIELD_NUMBER: _ClassVar[int]
    review_unit_id: str
    evaluation_run_id: str
    cell: EvaluationCellRefV1
    scorer_key: str
    scorer_version: str
    completion_state: ReviewUnitCompletionStateV1
    adjudication_state: ReviewAdjudicationStateV1
    submitted_count: int
    required_count: int
    blocking_effect_code: str
    blind_posture: bool
    pairwise: bool
    dataset_proposed_case_id: str
    def __init__(self, review_unit_id: _Optional[str] = ..., evaluation_run_id: _Optional[str] = ..., cell: _Optional[_Union[EvaluationCellRefV1, _Mapping]] = ..., scorer_key: _Optional[str] = ..., scorer_version: _Optional[str] = ..., completion_state: _Optional[_Union[ReviewUnitCompletionStateV1, str]] = ..., adjudication_state: _Optional[_Union[ReviewAdjudicationStateV1, str]] = ..., submitted_count: _Optional[int] = ..., required_count: _Optional[int] = ..., blocking_effect_code: _Optional[str] = ..., blind_posture: _Optional[bool] = ..., pairwise: _Optional[bool] = ..., dataset_proposed_case_id: _Optional[str] = ...) -> None: ...

class EvaluationReviewTaskV1(_message.Message):
    __slots__ = ("review_task_id", "unit", "state", "reservation_state", "reservation_expires_at", "reviewer", "allowed_actions", "created_at", "updated_at", "reservation_token")
    REVIEW_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_STATE_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    REVIEWER_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    review_task_id: str
    unit: EvaluationReviewUnitV1
    state: EvaluationReviewTaskStateV1
    reservation_state: ReviewReservationStateV1
    reservation_expires_at: _timestamp_pb2.Timestamp
    reviewer: PrincipalRefV1
    allowed_actions: _containers.RepeatedCompositeFieldContainer[AllowedActionV1]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    reservation_token: str
    def __init__(self, review_task_id: _Optional[str] = ..., unit: _Optional[_Union[EvaluationReviewUnitV1, _Mapping]] = ..., state: _Optional[_Union[EvaluationReviewTaskStateV1, str]] = ..., reservation_state: _Optional[_Union[ReviewReservationStateV1, str]] = ..., reservation_expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., reviewer: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., allowed_actions: _Optional[_Iterable[_Union[AllowedActionV1, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., reservation_token: _Optional[str] = ...) -> None: ...

class EvaluationReviewSubjectV1(_message.Message):
    __slots__ = ("cohort_key", "case_revision_id", "presented_candidate_keys", "artifact_refs", "availability", "subject_kind", "dataset_proposed_case_id")
    COHORT_KEY_FIELD_NUMBER: _ClassVar[int]
    CASE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    PRESENTED_CANDIDATE_KEYS_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_REFS_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_KIND_FIELD_NUMBER: _ClassVar[int]
    DATASET_PROPOSED_CASE_ID_FIELD_NUMBER: _ClassVar[int]
    cohort_key: str
    case_revision_id: str
    presented_candidate_keys: _containers.RepeatedScalarFieldContainer[str]
    artifact_refs: _containers.RepeatedCompositeFieldContainer[EvaluationArtifactContentRefV1]
    availability: MetricAvailabilityV1
    subject_kind: EvaluationReviewSubjectKindV1
    dataset_proposed_case_id: str
    def __init__(self, cohort_key: _Optional[str] = ..., case_revision_id: _Optional[str] = ..., presented_candidate_keys: _Optional[_Iterable[str]] = ..., artifact_refs: _Optional[_Iterable[_Union[EvaluationArtifactContentRefV1, _Mapping]]] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., subject_kind: _Optional[_Union[EvaluationReviewSubjectKindV1, str]] = ..., dataset_proposed_case_id: _Optional[str] = ...) -> None: ...

class EvaluationReviewRubricFieldV1(_message.Message):
    __slots__ = ("field_key", "required", "value_type_code", "minimum", "maximum")
    FIELD_KEY_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_CODE_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    field_key: str
    required: bool
    value_type_code: str
    minimum: float
    maximum: float
    def __init__(self, field_key: _Optional[str] = ..., required: _Optional[bool] = ..., value_type_code: _Optional[str] = ..., minimum: _Optional[float] = ..., maximum: _Optional[float] = ...) -> None: ...

class EvaluationReviewRubricV1(_message.Message):
    __slots__ = ("rubric_score_config_id", "rubric_version", "fields", "pairwise")
    RUBRIC_SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    RUBRIC_VERSION_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_FIELD_NUMBER: _ClassVar[int]
    rubric_score_config_id: str
    rubric_version: str
    fields: _containers.RepeatedCompositeFieldContainer[EvaluationReviewRubricFieldV1]
    pairwise: bool
    def __init__(self, rubric_score_config_id: _Optional[str] = ..., rubric_version: _Optional[str] = ..., fields: _Optional[_Iterable[_Union[EvaluationReviewRubricFieldV1, _Mapping]]] = ..., pairwise: _Optional[bool] = ...) -> None: ...

class EvaluationReviewSubmissionV1(_message.Message):
    __slots__ = ("submission_id", "review_task_id", "attempt", "reviewer", "field_values", "pairwise_winner", "explanation", "submitted_at", "binding")
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    REVIEW_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    REVIEWER_FIELD_NUMBER: _ClassVar[int]
    FIELD_VALUES_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_WINNER_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
    BINDING_FIELD_NUMBER: _ClassVar[int]
    submission_id: str
    review_task_id: str
    attempt: int
    reviewer: PrincipalRefV1
    field_values: _containers.RepeatedCompositeFieldContainer[MetadataEntryV1]
    pairwise_winner: _agentic_pb2.AnnotationPairwiseWinnerV1
    explanation: str
    submitted_at: _timestamp_pb2.Timestamp
    binding: bool
    def __init__(self, submission_id: _Optional[str] = ..., review_task_id: _Optional[str] = ..., attempt: _Optional[int] = ..., reviewer: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., field_values: _Optional[_Iterable[_Union[MetadataEntryV1, _Mapping]]] = ..., pairwise_winner: _Optional[_Union[_agentic_pb2.AnnotationPairwiseWinnerV1, str]] = ..., explanation: _Optional[str] = ..., submitted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., binding: _Optional[bool] = ...) -> None: ...

class EvaluationReviewRubricFieldErrorV1(_message.Message):
    __slots__ = ("field_key", "error_code")
    FIELD_KEY_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    field_key: str
    error_code: str
    def __init__(self, field_key: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...

class ListEvaluationReviewTasksRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "page", "states", "mine_only")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    MINE_ONLY_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    page: _common_pb2.PageRequestV1
    states: _containers.RepeatedScalarFieldContainer[EvaluationReviewTaskStateV1]
    mine_only: bool
    def __init__(self, evaluation_run_id: _Optional[str] = ..., page: _Optional[_Union[_common_pb2.PageRequestV1, _Mapping]] = ..., states: _Optional[_Iterable[_Union[EvaluationReviewTaskStateV1, str]]] = ..., mine_only: _Optional[bool] = ...) -> None: ...

class ListEvaluationReviewTasksResponse(_message.Message):
    __slots__ = ("tasks", "page", "freshness", "capabilities", "truncated_by_byte_budget", "response_byte_budget")
    TASKS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_BY_BYTE_BUDGET_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_BYTE_BUDGET_FIELD_NUMBER: _ClassVar[int]
    tasks: _containers.RepeatedCompositeFieldContainer[EvaluationReviewTaskV1]
    page: _common_pb2.PageResponseV1
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    truncated_by_byte_budget: bool
    response_byte_budget: int
    def __init__(self, tasks: _Optional[_Iterable[_Union[EvaluationReviewTaskV1, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponseV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., truncated_by_byte_budget: _Optional[bool] = ..., response_byte_budget: _Optional[int] = ...) -> None: ...

class ClaimEvaluationReviewTasksRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "max_tasks", "idempotency_key", "review_task_ids")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_TASKS_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    REVIEW_TASK_IDS_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    max_tasks: int
    idempotency_key: str
    review_task_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, evaluation_run_id: _Optional[str] = ..., max_tasks: _Optional[int] = ..., idempotency_key: _Optional[str] = ..., review_task_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ClaimEvaluationReviewTasksResponse(_message.Message):
    __slots__ = ("tasks", "short_claim_reason_code", "reserved_task_count", "max_simultaneous_reservations", "freshness", "capabilities", "refusals")
    TASKS_FIELD_NUMBER: _ClassVar[int]
    SHORT_CLAIM_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    RESERVED_TASK_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_SIMULTANEOUS_RESERVATIONS_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    REFUSALS_FIELD_NUMBER: _ClassVar[int]
    tasks: _containers.RepeatedCompositeFieldContainer[EvaluationReviewTaskV1]
    short_claim_reason_code: str
    reserved_task_count: int
    max_simultaneous_reservations: int
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    refusals: _containers.RepeatedCompositeFieldContainer[EvaluationReviewTaskRefusalV1]
    def __init__(self, tasks: _Optional[_Iterable[_Union[EvaluationReviewTaskV1, _Mapping]]] = ..., short_claim_reason_code: _Optional[str] = ..., reserved_task_count: _Optional[int] = ..., max_simultaneous_reservations: _Optional[int] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., refusals: _Optional[_Iterable[_Union[EvaluationReviewTaskRefusalV1, _Mapping]]] = ...) -> None: ...

class GetEvaluationReviewTaskRequest(_message.Message):
    __slots__ = ("review_task_id",)
    REVIEW_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    review_task_id: str
    def __init__(self, review_task_id: _Optional[str] = ...) -> None: ...

class GetEvaluationReviewTaskResponse(_message.Message):
    __slots__ = ("task", "subject", "rubric", "own_submission", "own_draft_field_values", "other_submissions", "blind_withheld", "blind_withheld_reason_code", "adjudicator_reveal", "allowed_actions", "freshness", "capabilities")
    TASK_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    RUBRIC_FIELD_NUMBER: _ClassVar[int]
    OWN_SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    OWN_DRAFT_FIELD_VALUES_FIELD_NUMBER: _ClassVar[int]
    OTHER_SUBMISSIONS_FIELD_NUMBER: _ClassVar[int]
    BLIND_WITHHELD_FIELD_NUMBER: _ClassVar[int]
    BLIND_WITHHELD_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    ADJUDICATOR_REVEAL_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    task: EvaluationReviewTaskV1
    subject: EvaluationReviewSubjectV1
    rubric: EvaluationReviewRubricV1
    own_submission: EvaluationReviewSubmissionV1
    own_draft_field_values: _containers.RepeatedCompositeFieldContainer[MetadataEntryV1]
    other_submissions: _containers.RepeatedCompositeFieldContainer[EvaluationReviewSubmissionV1]
    blind_withheld: bool
    blind_withheld_reason_code: str
    adjudicator_reveal: bool
    allowed_actions: _containers.RepeatedCompositeFieldContainer[AllowedActionV1]
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, task: _Optional[_Union[EvaluationReviewTaskV1, _Mapping]] = ..., subject: _Optional[_Union[EvaluationReviewSubjectV1, _Mapping]] = ..., rubric: _Optional[_Union[EvaluationReviewRubricV1, _Mapping]] = ..., own_submission: _Optional[_Union[EvaluationReviewSubmissionV1, _Mapping]] = ..., own_draft_field_values: _Optional[_Iterable[_Union[MetadataEntryV1, _Mapping]]] = ..., other_submissions: _Optional[_Iterable[_Union[EvaluationReviewSubmissionV1, _Mapping]]] = ..., blind_withheld: _Optional[bool] = ..., blind_withheld_reason_code: _Optional[str] = ..., adjudicator_reveal: _Optional[bool] = ..., allowed_actions: _Optional[_Iterable[_Union[AllowedActionV1, _Mapping]]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class SubmitEvaluationReviewRequest(_message.Message):
    __slots__ = ("review_task_id", "reservation_token", "field_values", "pairwise_winner", "explanation", "idempotency_key", "draft_only", "dataset_case_outcome", "merge_target_case_revision_id", "dataset_case_rejection_reason")
    REVIEW_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FIELD_VALUES_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_WINNER_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    DRAFT_ONLY_FIELD_NUMBER: _ClassVar[int]
    DATASET_CASE_OUTCOME_FIELD_NUMBER: _ClassVar[int]
    MERGE_TARGET_CASE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_CASE_REJECTION_REASON_FIELD_NUMBER: _ClassVar[int]
    review_task_id: str
    reservation_token: str
    field_values: _containers.RepeatedCompositeFieldContainer[MetadataEntryV1]
    pairwise_winner: _agentic_pb2.AnnotationPairwiseWinnerV1
    explanation: str
    idempotency_key: str
    draft_only: bool
    dataset_case_outcome: DatasetCaseReviewOutcomeV1
    merge_target_case_revision_id: str
    dataset_case_rejection_reason: DatasetCaseDraftRejectionReasonV1
    def __init__(self, review_task_id: _Optional[str] = ..., reservation_token: _Optional[str] = ..., field_values: _Optional[_Iterable[_Union[MetadataEntryV1, _Mapping]]] = ..., pairwise_winner: _Optional[_Union[_agentic_pb2.AnnotationPairwiseWinnerV1, str]] = ..., explanation: _Optional[str] = ..., idempotency_key: _Optional[str] = ..., draft_only: _Optional[bool] = ..., dataset_case_outcome: _Optional[_Union[DatasetCaseReviewOutcomeV1, str]] = ..., merge_target_case_revision_id: _Optional[str] = ..., dataset_case_rejection_reason: _Optional[_Union[DatasetCaseDraftRejectionReasonV1, str]] = ...) -> None: ...

class SubmitEvaluationReviewResponse(_message.Message):
    __slots__ = ("submission", "unit", "field_errors", "idempotent_replay", "unit_completed", "run_review_completed", "freshness", "capabilities")
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    FIELD_ERRORS_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    UNIT_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    RUN_REVIEW_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    submission: EvaluationReviewSubmissionV1
    unit: EvaluationReviewUnitV1
    field_errors: _containers.RepeatedCompositeFieldContainer[EvaluationReviewRubricFieldErrorV1]
    idempotent_replay: bool
    unit_completed: bool
    run_review_completed: bool
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, submission: _Optional[_Union[EvaluationReviewSubmissionV1, _Mapping]] = ..., unit: _Optional[_Union[EvaluationReviewUnitV1, _Mapping]] = ..., field_errors: _Optional[_Iterable[_Union[EvaluationReviewRubricFieldErrorV1, _Mapping]]] = ..., idempotent_replay: _Optional[bool] = ..., unit_completed: _Optional[bool] = ..., run_review_completed: _Optional[bool] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class EvaluationExportV1(_message.Message):
    __slots__ = ("export_id", "evaluation_run_id", "format", "state", "pinned_projection_version", "pinned_facts_watermark", "requested_by", "byte_size", "content_digest", "failure", "attempt_count", "created_at", "updated_at", "finished_at")
    EXPORT_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PINNED_PROJECTION_VERSION_FIELD_NUMBER: _ClassVar[int]
    PINNED_FACTS_WATERMARK_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    BYTE_SIZE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DIGEST_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    export_id: str
    evaluation_run_id: str
    format: EvaluationExportFormatV1
    state: EvaluationOperationStateV1
    pinned_projection_version: int
    pinned_facts_watermark: str
    requested_by: PrincipalRefV1
    byte_size: int
    content_digest: str
    failure: EvaluationFailureV1
    attempt_count: int
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    def __init__(self, export_id: _Optional[str] = ..., evaluation_run_id: _Optional[str] = ..., format: _Optional[_Union[EvaluationExportFormatV1, str]] = ..., state: _Optional[_Union[EvaluationOperationStateV1, str]] = ..., pinned_projection_version: _Optional[int] = ..., pinned_facts_watermark: _Optional[str] = ..., requested_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., byte_size: _Optional[int] = ..., content_digest: _Optional[str] = ..., failure: _Optional[_Union[EvaluationFailureV1, _Mapping]] = ..., attempt_count: _Optional[int] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateEvaluationExportRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "format", "idempotency_key")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    format: EvaluationExportFormatV1
    idempotency_key: str
    def __init__(self, evaluation_run_id: _Optional[str] = ..., format: _Optional[_Union[EvaluationExportFormatV1, str]] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class CreateEvaluationExportResponse(_message.Message):
    __slots__ = ("export", "idempotent_replay", "capabilities")
    EXPORT_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    export: EvaluationExportV1
    idempotent_replay: bool
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, export: _Optional[_Union[EvaluationExportV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class GetEvaluationExportRequest(_message.Message):
    __slots__ = ("export_id",)
    EXPORT_ID_FIELD_NUMBER: _ClassVar[int]
    export_id: str
    def __init__(self, export_id: _Optional[str] = ...) -> None: ...

class GetEvaluationExportResponse(_message.Message):
    __slots__ = ("export", "allowed_actions", "freshness", "capabilities")
    EXPORT_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    export: EvaluationExportV1
    allowed_actions: _containers.RepeatedCompositeFieldContainer[AllowedActionV1]
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, export: _Optional[_Union[EvaluationExportV1, _Mapping]] = ..., allowed_actions: _Optional[_Iterable[_Union[AllowedActionV1, _Mapping]]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class EvaluationShareV1(_message.Message):
    __slots__ = ("share_id", "evaluation_run_id", "state", "created_by", "created_at", "revoked_at")
    SHARE_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    REVOKED_AT_FIELD_NUMBER: _ClassVar[int]
    share_id: str
    evaluation_run_id: str
    state: EvaluationShareStateV1
    created_by: PrincipalRefV1
    created_at: _timestamp_pb2.Timestamp
    revoked_at: _timestamp_pb2.Timestamp
    def __init__(self, share_id: _Optional[str] = ..., evaluation_run_id: _Optional[str] = ..., state: _Optional[_Union[EvaluationShareStateV1, str]] = ..., created_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., revoked_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateEvaluationShareRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "idempotency_key")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    idempotency_key: str
    def __init__(self, evaluation_run_id: _Optional[str] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class CreateEvaluationShareResponse(_message.Message):
    __slots__ = ("share", "idempotent_replay", "capabilities")
    SHARE_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    share: EvaluationShareV1
    idempotent_replay: bool
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, share: _Optional[_Union[EvaluationShareV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class GetEvaluationShareRequest(_message.Message):
    __slots__ = ("share_id",)
    SHARE_ID_FIELD_NUMBER: _ClassVar[int]
    share_id: str
    def __init__(self, share_id: _Optional[str] = ...) -> None: ...

class GetEvaluationShareResponse(_message.Message):
    __slots__ = ("share", "allowed_actions", "freshness", "capabilities")
    SHARE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    share: EvaluationShareV1
    allowed_actions: _containers.RepeatedCompositeFieldContainer[AllowedActionV1]
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, share: _Optional[_Union[EvaluationShareV1, _Mapping]] = ..., allowed_actions: _Optional[_Iterable[_Union[AllowedActionV1, _Mapping]]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class RevokeEvaluationShareRequest(_message.Message):
    __slots__ = ("share_id", "idempotency_key")
    SHARE_ID_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    share_id: str
    idempotency_key: str
    def __init__(self, share_id: _Optional[str] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class RevokeEvaluationShareResponse(_message.Message):
    __slots__ = ("share", "idempotent_replay", "capabilities")
    SHARE_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    share: EvaluationShareV1
    idempotent_replay: bool
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, share: _Optional[_Union[EvaluationShareV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class EvaluationOperationBoundaryV1(_message.Message):
    __slots__ = ("scope_code", "max_groups", "max_exemplars_per_group", "excluded_dimensions")
    SCOPE_CODE_FIELD_NUMBER: _ClassVar[int]
    MAX_GROUPS_FIELD_NUMBER: _ClassVar[int]
    MAX_EXEMPLARS_PER_GROUP_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    scope_code: str
    max_groups: int
    max_exemplars_per_group: int
    excluded_dimensions: _containers.RepeatedScalarFieldContainer[EvaluationOperationDimensionV1]
    def __init__(self, scope_code: _Optional[str] = ..., max_groups: _Optional[int] = ..., max_exemplars_per_group: _Optional[int] = ..., excluded_dimensions: _Optional[_Iterable[_Union[EvaluationOperationDimensionV1, str]]] = ...) -> None: ...

class EvaluationOperationGroupV1(_message.Message):
    __slots__ = ("kind", "operation_name", "operation_source_code", "call_count", "succeeded_count", "failed_count", "retry_count", "total_latency_micros", "latency_availability", "latency_observed_count", "cost", "cost_posture", "cost_availability", "priced_count", "unpriced_count", "input_tokens", "output_tokens", "cache_read_tokens", "cache_write_tokens", "reasoning_tokens", "token_availability", "cache_explanation", "dominant_failure_code", "dominant_failure_stage", "dominant_failure_count", "exemplar_cells", "regrade_available", "regrade_blocked_reason_code")
    KIND_FIELD_NUMBER: _ClassVar[int]
    OPERATION_NAME_FIELD_NUMBER: _ClassVar[int]
    OPERATION_SOURCE_CODE_FIELD_NUMBER: _ClassVar[int]
    CALL_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUCCEEDED_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_COUNT_FIELD_NUMBER: _ClassVar[int]
    RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LATENCY_MICROS_FIELD_NUMBER: _ClassVar[int]
    LATENCY_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    LATENCY_OBSERVED_COUNT_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    COST_POSTURE_FIELD_NUMBER: _ClassVar[int]
    COST_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    PRICED_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNPRICED_COUNT_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_READ_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_WRITE_TOKENS_FIELD_NUMBER: _ClassVar[int]
    REASONING_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    CACHE_EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    DOMINANT_FAILURE_CODE_FIELD_NUMBER: _ClassVar[int]
    DOMINANT_FAILURE_STAGE_FIELD_NUMBER: _ClassVar[int]
    DOMINANT_FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXEMPLAR_CELLS_FIELD_NUMBER: _ClassVar[int]
    REGRADE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    REGRADE_BLOCKED_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    kind: EvaluationWorkOperationKindV1
    operation_name: str
    operation_source_code: str
    call_count: int
    succeeded_count: int
    failed_count: int
    retry_count: int
    total_latency_micros: int
    latency_availability: MetricAvailabilityV1
    latency_observed_count: int
    cost: CostAmountV1
    cost_posture: CostPostureV1
    cost_availability: MetricAvailabilityV1
    priced_count: int
    unpriced_count: int
    input_tokens: int
    output_tokens: int
    cache_read_tokens: int
    cache_write_tokens: int
    reasoning_tokens: int
    token_availability: MetricAvailabilityV1
    cache_explanation: EvaluationOperationCacheExplanationV1
    dominant_failure_code: str
    dominant_failure_stage: str
    dominant_failure_count: int
    exemplar_cells: _containers.RepeatedCompositeFieldContainer[EvaluationCellRefV1]
    regrade_available: bool
    regrade_blocked_reason_code: str
    def __init__(self, kind: _Optional[_Union[EvaluationWorkOperationKindV1, str]] = ..., operation_name: _Optional[str] = ..., operation_source_code: _Optional[str] = ..., call_count: _Optional[int] = ..., succeeded_count: _Optional[int] = ..., failed_count: _Optional[int] = ..., retry_count: _Optional[int] = ..., total_latency_micros: _Optional[int] = ..., latency_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., latency_observed_count: _Optional[int] = ..., cost: _Optional[_Union[CostAmountV1, _Mapping]] = ..., cost_posture: _Optional[_Union[CostPostureV1, str]] = ..., cost_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., priced_count: _Optional[int] = ..., unpriced_count: _Optional[int] = ..., input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., cache_read_tokens: _Optional[int] = ..., cache_write_tokens: _Optional[int] = ..., reasoning_tokens: _Optional[int] = ..., token_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., cache_explanation: _Optional[_Union[EvaluationOperationCacheExplanationV1, str]] = ..., dominant_failure_code: _Optional[str] = ..., dominant_failure_stage: _Optional[str] = ..., dominant_failure_count: _Optional[int] = ..., exemplar_cells: _Optional[_Iterable[_Union[EvaluationCellRefV1, _Mapping]]] = ..., regrade_available: _Optional[bool] = ..., regrade_blocked_reason_code: _Optional[str] = ...) -> None: ...

class EvaluationOperationTotalsV1(_message.Message):
    __slots__ = ("operation_group_count", "candidate_call_count", "scorer_execution_count", "candidate_cost", "candidate_cost_availability", "candidate_latency_micros", "scorer_latency_micros", "scorer_cost_availability", "time_to_first_token_availability", "regradable_operation_count", "regrade_external_call_count")
    OPERATION_GROUP_COUNT_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_CALL_COUNT_FIELD_NUMBER: _ClassVar[int]
    SCORER_EXECUTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_COST_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_COST_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_LATENCY_MICROS_FIELD_NUMBER: _ClassVar[int]
    SCORER_LATENCY_MICROS_FIELD_NUMBER: _ClassVar[int]
    SCORER_COST_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_FIRST_TOKEN_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    REGRADABLE_OPERATION_COUNT_FIELD_NUMBER: _ClassVar[int]
    REGRADE_EXTERNAL_CALL_COUNT_FIELD_NUMBER: _ClassVar[int]
    operation_group_count: int
    candidate_call_count: int
    scorer_execution_count: int
    candidate_cost: CostAmountV1
    candidate_cost_availability: MetricAvailabilityV1
    candidate_latency_micros: int
    scorer_latency_micros: int
    scorer_cost_availability: MetricAvailabilityV1
    time_to_first_token_availability: MetricAvailabilityV1
    regradable_operation_count: int
    regrade_external_call_count: int
    def __init__(self, operation_group_count: _Optional[int] = ..., candidate_call_count: _Optional[int] = ..., scorer_execution_count: _Optional[int] = ..., candidate_cost: _Optional[_Union[CostAmountV1, _Mapping]] = ..., candidate_cost_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., candidate_latency_micros: _Optional[int] = ..., scorer_latency_micros: _Optional[int] = ..., scorer_cost_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., time_to_first_token_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., regradable_operation_count: _Optional[int] = ..., regrade_external_call_count: _Optional[int] = ...) -> None: ...

class GetEvaluationOperationBreakdownRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "candidate_key", "cohort_key")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    COHORT_KEY_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    candidate_key: str
    cohort_key: str
    def __init__(self, evaluation_run_id: _Optional[str] = ..., candidate_key: _Optional[str] = ..., cohort_key: _Optional[str] = ...) -> None: ...

class GetEvaluationOperationBreakdownResponse(_message.Message):
    __slots__ = ("evaluation_run_id", "groups", "truncated_group_count", "totals", "boundary", "allowed_actions", "freshness", "capabilities")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_GROUP_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTALS_FIELD_NUMBER: _ClassVar[int]
    BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    groups: _containers.RepeatedCompositeFieldContainer[EvaluationOperationGroupV1]
    truncated_group_count: int
    totals: EvaluationOperationTotalsV1
    boundary: EvaluationOperationBoundaryV1
    allowed_actions: _containers.RepeatedCompositeFieldContainer[AllowedActionV1]
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, evaluation_run_id: _Optional[str] = ..., groups: _Optional[_Iterable[_Union[EvaluationOperationGroupV1, _Mapping]]] = ..., truncated_group_count: _Optional[int] = ..., totals: _Optional[_Union[EvaluationOperationTotalsV1, _Mapping]] = ..., boundary: _Optional[_Union[EvaluationOperationBoundaryV1, _Mapping]] = ..., allowed_actions: _Optional[_Iterable[_Union[AllowedActionV1, _Mapping]]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class EvaluationDefinitionRevisionSummaryV1(_message.Message):
    __slots__ = ("revision_id", "definition_id", "revision_number", "content_digest", "draft_schema_version", "draft_byte_size", "created_by", "created_at", "change_summary", "source_revision_id", "is_current")
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DIGEST_FIELD_NUMBER: _ClassVar[int]
    DRAFT_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    DRAFT_BYTE_SIZE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CHANGE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_CURRENT_FIELD_NUMBER: _ClassVar[int]
    revision_id: str
    definition_id: str
    revision_number: int
    content_digest: str
    draft_schema_version: int
    draft_byte_size: int
    created_by: PrincipalRefV1
    created_at: _timestamp_pb2.Timestamp
    change_summary: str
    source_revision_id: str
    is_current: bool
    def __init__(self, revision_id: _Optional[str] = ..., definition_id: _Optional[str] = ..., revision_number: _Optional[int] = ..., content_digest: _Optional[str] = ..., draft_schema_version: _Optional[int] = ..., draft_byte_size: _Optional[int] = ..., created_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., change_summary: _Optional[str] = ..., source_revision_id: _Optional[str] = ..., is_current: _Optional[bool] = ...) -> None: ...

class ListEvaluationDefinitionRevisionsRequest(_message.Message):
    __slots__ = ("definition_id", "page")
    DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    definition_id: str
    page: _common_pb2.PageRequestV1
    def __init__(self, definition_id: _Optional[str] = ..., page: _Optional[_Union[_common_pb2.PageRequestV1, _Mapping]] = ...) -> None: ...

class ListEvaluationDefinitionRevisionsResponse(_message.Message):
    __slots__ = ("revisions", "page", "freshness", "capabilities", "resync")
    REVISIONS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    RESYNC_FIELD_NUMBER: _ClassVar[int]
    revisions: _containers.RepeatedCompositeFieldContainer[EvaluationDefinitionRevisionSummaryV1]
    page: _common_pb2.PageResponseV1
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    resync: EvaluationCursorResyncV1
    def __init__(self, revisions: _Optional[_Iterable[_Union[EvaluationDefinitionRevisionSummaryV1, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponseV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., resync: _Optional[_Union[EvaluationCursorResyncV1, _Mapping]] = ...) -> None: ...

class EvaluationReviewAdjudicationV1(_message.Message):
    __slots__ = ("adjudication_id", "review_unit_id", "evaluation_run_id", "adjudicator", "field_values", "pairwise_winner", "reason", "resolved_submission_ids", "resolved_at", "binding")
    ADJUDICATION_ID_FIELD_NUMBER: _ClassVar[int]
    REVIEW_UNIT_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ADJUDICATOR_FIELD_NUMBER: _ClassVar[int]
    FIELD_VALUES_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_WINNER_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_SUBMISSION_IDS_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_AT_FIELD_NUMBER: _ClassVar[int]
    BINDING_FIELD_NUMBER: _ClassVar[int]
    adjudication_id: str
    review_unit_id: str
    evaluation_run_id: str
    adjudicator: PrincipalRefV1
    field_values: _containers.RepeatedCompositeFieldContainer[MetadataEntryV1]
    pairwise_winner: _agentic_pb2.AnnotationPairwiseWinnerV1
    reason: str
    resolved_submission_ids: _containers.RepeatedScalarFieldContainer[str]
    resolved_at: _timestamp_pb2.Timestamp
    binding: bool
    def __init__(self, adjudication_id: _Optional[str] = ..., review_unit_id: _Optional[str] = ..., evaluation_run_id: _Optional[str] = ..., adjudicator: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., field_values: _Optional[_Iterable[_Union[MetadataEntryV1, _Mapping]]] = ..., pairwise_winner: _Optional[_Union[_agentic_pb2.AnnotationPairwiseWinnerV1, str]] = ..., reason: _Optional[str] = ..., resolved_submission_ids: _Optional[_Iterable[str]] = ..., resolved_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., binding: _Optional[bool] = ...) -> None: ...

class AdjudicateEvaluationReviewConflictRequest(_message.Message):
    __slots__ = ("review_unit_id", "field_values", "pairwise_winner", "reason", "idempotency_key")
    REVIEW_UNIT_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_VALUES_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_WINNER_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    review_unit_id: str
    field_values: _containers.RepeatedCompositeFieldContainer[MetadataEntryV1]
    pairwise_winner: _agentic_pb2.AnnotationPairwiseWinnerV1
    reason: str
    idempotency_key: str
    def __init__(self, review_unit_id: _Optional[str] = ..., field_values: _Optional[_Iterable[_Union[MetadataEntryV1, _Mapping]]] = ..., pairwise_winner: _Optional[_Union[_agentic_pb2.AnnotationPairwiseWinnerV1, str]] = ..., reason: _Optional[str] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class AdjudicateEvaluationReviewConflictResponse(_message.Message):
    __slots__ = ("adjudication", "unit", "resolved_submissions", "refusal", "idempotent_replay", "unit_completed", "run_review_completed", "freshness", "capabilities")
    ADJUDICATION_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_SUBMISSIONS_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    UNIT_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    RUN_REVIEW_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    adjudication: EvaluationReviewAdjudicationV1
    unit: EvaluationReviewUnitV1
    resolved_submissions: _containers.RepeatedCompositeFieldContainer[EvaluationReviewSubmissionV1]
    refusal: EvaluationAdjudicationRefusalV1
    idempotent_replay: bool
    unit_completed: bool
    run_review_completed: bool
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, adjudication: _Optional[_Union[EvaluationReviewAdjudicationV1, _Mapping]] = ..., unit: _Optional[_Union[EvaluationReviewUnitV1, _Mapping]] = ..., resolved_submissions: _Optional[_Iterable[_Union[EvaluationReviewSubmissionV1, _Mapping]]] = ..., refusal: _Optional[_Union[EvaluationAdjudicationRefusalV1, str]] = ..., idempotent_replay: _Optional[bool] = ..., unit_completed: _Optional[bool] = ..., run_review_completed: _Optional[bool] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class EvaluationOrgNegotiatedRateV1(_message.Message):
    __slots__ = ("negotiated_rate_id", "provider", "model_id", "input_micros_per_million_tokens", "output_micros_per_million_tokens", "cache_read_micros_per_million_tokens", "cache_write_5m_micros_per_million_tokens", "cache_write_1h_micros_per_million_tokens", "reasoning_micros_per_million_tokens", "suppressed_modifier_codes", "effective_from_date", "effective_until_date", "source_note", "created_by", "created_at", "state", "voided_at", "void_reason")
    NEGOTIATED_RATE_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_MICROS_PER_MILLION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_MICROS_PER_MILLION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_READ_MICROS_PER_MILLION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_WRITE_5M_MICROS_PER_MILLION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_WRITE_1H_MICROS_PER_MILLION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    REASONING_MICROS_PER_MILLION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    SUPPRESSED_MODIFIER_CODES_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_FROM_DATE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_UNTIL_DATE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NOTE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    VOIDED_AT_FIELD_NUMBER: _ClassVar[int]
    VOID_REASON_FIELD_NUMBER: _ClassVar[int]
    negotiated_rate_id: str
    provider: _agentic_pb2.ProviderNameV1
    model_id: str
    input_micros_per_million_tokens: int
    output_micros_per_million_tokens: int
    cache_read_micros_per_million_tokens: int
    cache_write_5m_micros_per_million_tokens: int
    cache_write_1h_micros_per_million_tokens: int
    reasoning_micros_per_million_tokens: int
    suppressed_modifier_codes: _containers.RepeatedScalarFieldContainer[str]
    effective_from_date: str
    effective_until_date: str
    source_note: str
    created_by: PrincipalRefV1
    created_at: _timestamp_pb2.Timestamp
    state: EvaluationOrgNegotiatedRateStateV1
    voided_at: _timestamp_pb2.Timestamp
    void_reason: str
    def __init__(self, negotiated_rate_id: _Optional[str] = ..., provider: _Optional[_Union[_agentic_pb2.ProviderNameV1, str]] = ..., model_id: _Optional[str] = ..., input_micros_per_million_tokens: _Optional[int] = ..., output_micros_per_million_tokens: _Optional[int] = ..., cache_read_micros_per_million_tokens: _Optional[int] = ..., cache_write_5m_micros_per_million_tokens: _Optional[int] = ..., cache_write_1h_micros_per_million_tokens: _Optional[int] = ..., reasoning_micros_per_million_tokens: _Optional[int] = ..., suppressed_modifier_codes: _Optional[_Iterable[str]] = ..., effective_from_date: _Optional[str] = ..., effective_until_date: _Optional[str] = ..., source_note: _Optional[str] = ..., created_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[EvaluationOrgNegotiatedRateStateV1, str]] = ..., voided_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., void_reason: _Optional[str] = ...) -> None: ...

class RecordEvaluationOrgNegotiatedRateRequest(_message.Message):
    __slots__ = ("provider", "model_id", "input_micros_per_million_tokens", "output_micros_per_million_tokens", "cache_read_micros_per_million_tokens", "cache_write_5m_micros_per_million_tokens", "cache_write_1h_micros_per_million_tokens", "reasoning_micros_per_million_tokens", "suppressed_modifier_codes", "effective_from_date", "source_note", "idempotency_key")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_MICROS_PER_MILLION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_MICROS_PER_MILLION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_READ_MICROS_PER_MILLION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_WRITE_5M_MICROS_PER_MILLION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_WRITE_1H_MICROS_PER_MILLION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    REASONING_MICROS_PER_MILLION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    SUPPRESSED_MODIFIER_CODES_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_FROM_DATE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NOTE_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    provider: _agentic_pb2.ProviderNameV1
    model_id: str
    input_micros_per_million_tokens: int
    output_micros_per_million_tokens: int
    cache_read_micros_per_million_tokens: int
    cache_write_5m_micros_per_million_tokens: int
    cache_write_1h_micros_per_million_tokens: int
    reasoning_micros_per_million_tokens: int
    suppressed_modifier_codes: _containers.RepeatedScalarFieldContainer[str]
    effective_from_date: str
    source_note: str
    idempotency_key: str
    def __init__(self, provider: _Optional[_Union[_agentic_pb2.ProviderNameV1, str]] = ..., model_id: _Optional[str] = ..., input_micros_per_million_tokens: _Optional[int] = ..., output_micros_per_million_tokens: _Optional[int] = ..., cache_read_micros_per_million_tokens: _Optional[int] = ..., cache_write_5m_micros_per_million_tokens: _Optional[int] = ..., cache_write_1h_micros_per_million_tokens: _Optional[int] = ..., reasoning_micros_per_million_tokens: _Optional[int] = ..., suppressed_modifier_codes: _Optional[_Iterable[str]] = ..., effective_from_date: _Optional[str] = ..., source_note: _Optional[str] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class RecordEvaluationOrgNegotiatedRateResponse(_message.Message):
    __slots__ = ("negotiated_rate", "idempotent_replay", "capabilities")
    NEGOTIATED_RATE_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    negotiated_rate: EvaluationOrgNegotiatedRateV1
    idempotent_replay: bool
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, negotiated_rate: _Optional[_Union[EvaluationOrgNegotiatedRateV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class ListEvaluationOrgNegotiatedRatesRequest(_message.Message):
    __slots__ = ("page",)
    PAGE_FIELD_NUMBER: _ClassVar[int]
    page: _common_pb2.PageRequestV1
    def __init__(self, page: _Optional[_Union[_common_pb2.PageRequestV1, _Mapping]] = ...) -> None: ...

class ListEvaluationOrgNegotiatedRatesResponse(_message.Message):
    __slots__ = ("negotiated_rates", "page", "freshness", "capabilities", "resync")
    NEGOTIATED_RATES_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    RESYNC_FIELD_NUMBER: _ClassVar[int]
    negotiated_rates: _containers.RepeatedCompositeFieldContainer[EvaluationOrgNegotiatedRateV1]
    page: _common_pb2.PageResponseV1
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    resync: EvaluationCursorResyncV1
    def __init__(self, negotiated_rates: _Optional[_Iterable[_Union[EvaluationOrgNegotiatedRateV1, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponseV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., resync: _Optional[_Union[EvaluationCursorResyncV1, _Mapping]] = ...) -> None: ...

class EndEvaluationOrgNegotiatedRateRequest(_message.Message):
    __slots__ = ("negotiated_rate_id", "effective_until_date", "idempotency_key")
    NEGOTIATED_RATE_ID_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_UNTIL_DATE_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    negotiated_rate_id: str
    effective_until_date: str
    idempotency_key: str
    def __init__(self, negotiated_rate_id: _Optional[str] = ..., effective_until_date: _Optional[str] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class EndEvaluationOrgNegotiatedRateResponse(_message.Message):
    __slots__ = ("negotiated_rate", "idempotent_replay", "capabilities")
    NEGOTIATED_RATE_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    negotiated_rate: EvaluationOrgNegotiatedRateV1
    idempotent_replay: bool
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, negotiated_rate: _Optional[_Union[EvaluationOrgNegotiatedRateV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class VoidEvaluationOrgNegotiatedRateRequest(_message.Message):
    __slots__ = ("negotiated_rate_id", "void_reason", "idempotency_key")
    NEGOTIATED_RATE_ID_FIELD_NUMBER: _ClassVar[int]
    VOID_REASON_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    negotiated_rate_id: str
    void_reason: str
    idempotency_key: str
    def __init__(self, negotiated_rate_id: _Optional[str] = ..., void_reason: _Optional[str] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class VoidEvaluationOrgNegotiatedRateResponse(_message.Message):
    __slots__ = ("negotiated_rate", "idempotent_replay", "capabilities")
    NEGOTIATED_RATE_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    negotiated_rate: EvaluationOrgNegotiatedRateV1
    idempotent_replay: bool
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, negotiated_rate: _Optional[_Union[EvaluationOrgNegotiatedRateV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class EvaluationSeriesKeyV1(_message.Message):
    __slots__ = ("definition_id", "candidate_key", "cohort_key", "score_config_id", "metric_name")
    DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    COHORT_KEY_FIELD_NUMBER: _ClassVar[int]
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    definition_id: str
    candidate_key: str
    cohort_key: str
    score_config_id: str
    metric_name: str
    def __init__(self, definition_id: _Optional[str] = ..., candidate_key: _Optional[str] = ..., cohort_key: _Optional[str] = ..., score_config_id: _Optional[str] = ..., metric_name: _Optional[str] = ...) -> None: ...

class EvaluationSeriesPointV1(_message.Message):
    __slots__ = ("bucket_start", "mean_score", "pass_rate", "coverage_ratio", "candidate_cost_micros", "candidate_cost_currency", "run_count", "scored_result_count", "expected_cell_count", "executed_cell_count", "verdict_pass_count", "verdict_fail_count", "verdict_error_count", "verdict_skipped_count", "verdict_not_applicable_count", "pending_review_count", "not_sampled_count", "candidate_priced_cell_count", "availability")
    BUCKET_START_FIELD_NUMBER: _ClassVar[int]
    MEAN_SCORE_FIELD_NUMBER: _ClassVar[int]
    PASS_RATE_FIELD_NUMBER: _ClassVar[int]
    COVERAGE_RATIO_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_COST_MICROS_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_COST_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    SCORED_RESULT_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    VERDICT_PASS_COUNT_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FAIL_COUNT_FIELD_NUMBER: _ClassVar[int]
    VERDICT_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    VERDICT_SKIPPED_COUNT_FIELD_NUMBER: _ClassVar[int]
    VERDICT_NOT_APPLICABLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PENDING_REVIEW_COUNT_FIELD_NUMBER: _ClassVar[int]
    NOT_SAMPLED_COUNT_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_PRICED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    bucket_start: _timestamp_pb2.Timestamp
    mean_score: float
    pass_rate: float
    coverage_ratio: float
    candidate_cost_micros: int
    candidate_cost_currency: str
    run_count: int
    scored_result_count: int
    expected_cell_count: int
    executed_cell_count: int
    verdict_pass_count: int
    verdict_fail_count: int
    verdict_error_count: int
    verdict_skipped_count: int
    verdict_not_applicable_count: int
    pending_review_count: int
    not_sampled_count: int
    candidate_priced_cell_count: int
    availability: MetricAvailabilityV1
    def __init__(self, bucket_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., mean_score: _Optional[float] = ..., pass_rate: _Optional[float] = ..., coverage_ratio: _Optional[float] = ..., candidate_cost_micros: _Optional[int] = ..., candidate_cost_currency: _Optional[str] = ..., run_count: _Optional[int] = ..., scored_result_count: _Optional[int] = ..., expected_cell_count: _Optional[int] = ..., executed_cell_count: _Optional[int] = ..., verdict_pass_count: _Optional[int] = ..., verdict_fail_count: _Optional[int] = ..., verdict_error_count: _Optional[int] = ..., verdict_skipped_count: _Optional[int] = ..., verdict_not_applicable_count: _Optional[int] = ..., pending_review_count: _Optional[int] = ..., not_sampled_count: _Optional[int] = ..., candidate_priced_cell_count: _Optional[int] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class EvaluationScoreSeriesV1(_message.Message):
    __slots__ = ("key", "points", "availability")
    KEY_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    key: EvaluationSeriesKeyV1
    points: _containers.RepeatedCompositeFieldContainer[EvaluationSeriesPointV1]
    availability: MetricAvailabilityV1
    def __init__(self, key: _Optional[_Union[EvaluationSeriesKeyV1, _Mapping]] = ..., points: _Optional[_Iterable[_Union[EvaluationSeriesPointV1, _Mapping]]] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class EvaluationSeriesClampV1(_message.Message):
    __slots__ = ("max_series_keys", "max_buckets", "max_points", "effective_series_keys", "effective_buckets", "effective_points", "clamped", "clamp_reason_code", "more_series_available", "effective_window_start", "effective_window_end", "effective_bucket_seconds")
    MAX_SERIES_KEYS_FIELD_NUMBER: _ClassVar[int]
    MAX_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    MAX_POINTS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_SERIES_KEYS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_POINTS_FIELD_NUMBER: _ClassVar[int]
    CLAMPED_FIELD_NUMBER: _ClassVar[int]
    CLAMP_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    MORE_SERIES_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_WINDOW_START_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_WINDOW_END_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_BUCKET_SECONDS_FIELD_NUMBER: _ClassVar[int]
    max_series_keys: int
    max_buckets: int
    max_points: int
    effective_series_keys: int
    effective_buckets: int
    effective_points: int
    clamped: bool
    clamp_reason_code: str
    more_series_available: bool
    effective_window_start: _timestamp_pb2.Timestamp
    effective_window_end: _timestamp_pb2.Timestamp
    effective_bucket_seconds: int
    def __init__(self, max_series_keys: _Optional[int] = ..., max_buckets: _Optional[int] = ..., max_points: _Optional[int] = ..., effective_series_keys: _Optional[int] = ..., effective_buckets: _Optional[int] = ..., effective_points: _Optional[int] = ..., clamped: _Optional[bool] = ..., clamp_reason_code: _Optional[str] = ..., more_series_available: _Optional[bool] = ..., effective_window_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., effective_window_end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., effective_bucket_seconds: _Optional[int] = ...) -> None: ...

class ListEvaluationScoreSeriesRequest(_message.Message):
    __slots__ = ("definition_id", "window_start", "window_end", "bucket_seconds", "grain", "max_series_keys")
    DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    WINDOW_START_FIELD_NUMBER: _ClassVar[int]
    WINDOW_END_FIELD_NUMBER: _ClassVar[int]
    BUCKET_SECONDS_FIELD_NUMBER: _ClassVar[int]
    GRAIN_FIELD_NUMBER: _ClassVar[int]
    MAX_SERIES_KEYS_FIELD_NUMBER: _ClassVar[int]
    definition_id: str
    window_start: _timestamp_pb2.Timestamp
    window_end: _timestamp_pb2.Timestamp
    bucket_seconds: int
    grain: EvaluationSeriesGrainV1
    max_series_keys: int
    def __init__(self, definition_id: _Optional[str] = ..., window_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., window_end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., bucket_seconds: _Optional[int] = ..., grain: _Optional[_Union[EvaluationSeriesGrainV1, str]] = ..., max_series_keys: _Optional[int] = ...) -> None: ...

class ListEvaluationScoreSeriesResponse(_message.Message):
    __slots__ = ("series", "clamp", "answering_plane", "freshness", "capabilities")
    SERIES_FIELD_NUMBER: _ClassVar[int]
    CLAMP_FIELD_NUMBER: _ClassVar[int]
    ANSWERING_PLANE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    series: _containers.RepeatedCompositeFieldContainer[EvaluationScoreSeriesV1]
    clamp: EvaluationSeriesClampV1
    answering_plane: EvaluationSeriesPlaneV1
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, series: _Optional[_Iterable[_Union[EvaluationScoreSeriesV1, _Mapping]]] = ..., clamp: _Optional[_Union[EvaluationSeriesClampV1, _Mapping]] = ..., answering_plane: _Optional[_Union[EvaluationSeriesPlaneV1, str]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class EvaluationCaptureSpanSourceV1(_message.Message):
    __slots__ = ("trace_id", "span_id")
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    trace_id: bytes
    span_id: bytes
    def __init__(self, trace_id: _Optional[bytes] = ..., span_id: _Optional[bytes] = ...) -> None: ...

class EvaluationCaptureCellSourceV1(_message.Message):
    __slots__ = ("evaluation_run_id", "cell")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    cell: EvaluationCellRefV1
    def __init__(self, evaluation_run_id: _Optional[str] = ..., cell: _Optional[_Union[EvaluationCellRefV1, _Mapping]] = ...) -> None: ...

class EvaluationCaptureProvenanceV1(_message.Message):
    __slots__ = ("source_kind", "trace_id", "span_id", "telemetry_availability", "cell", "evaluation_run_id", "source_dataset_version_id", "captured_at")
    SOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    CELL_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    CAPTURED_AT_FIELD_NUMBER: _ClassVar[int]
    source_kind: EvaluationCaptureSourceKindV1
    trace_id: bytes
    span_id: bytes
    telemetry_availability: MetricAvailabilityV1
    cell: EvaluationCellRefV1
    evaluation_run_id: str
    source_dataset_version_id: str
    captured_at: _timestamp_pb2.Timestamp
    def __init__(self, source_kind: _Optional[_Union[EvaluationCaptureSourceKindV1, str]] = ..., trace_id: _Optional[bytes] = ..., span_id: _Optional[bytes] = ..., telemetry_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., cell: _Optional[_Union[EvaluationCellRefV1, _Mapping]] = ..., evaluation_run_id: _Optional[str] = ..., source_dataset_version_id: _Optional[str] = ..., captured_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EvaluationCaptureFieldSelectionV1(_message.Message):
    __slots__ = ("source_path", "target_path", "availability")
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    source_path: str
    target_path: str
    availability: MetricAvailabilityV1
    def __init__(self, source_path: _Optional[str] = ..., target_path: _Optional[str] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class EvaluationProposedCaseV1(_message.Message):
    __slots__ = ("proposed_case_id", "draft_id", "ordinal", "state", "provenance", "selections", "input_availability", "expected_output_availability", "recorded_output_field_path", "recorded_output_availability", "content_digest", "void_reason", "created_at", "source_content_refs", "draft_state")
    PROPOSED_CASE_ID_FIELD_NUMBER: _ClassVar[int]
    DRAFT_ID_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PROVENANCE_FIELD_NUMBER: _ClassVar[int]
    SELECTIONS_FIELD_NUMBER: _ClassVar[int]
    INPUT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    RECORDED_OUTPUT_FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
    RECORDED_OUTPUT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DIGEST_FIELD_NUMBER: _ClassVar[int]
    VOID_REASON_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONTENT_REFS_FIELD_NUMBER: _ClassVar[int]
    DRAFT_STATE_FIELD_NUMBER: _ClassVar[int]
    proposed_case_id: str
    draft_id: str
    ordinal: int
    state: EvaluationProposedCaseStateV1
    provenance: EvaluationCaptureProvenanceV1
    selections: _containers.RepeatedCompositeFieldContainer[EvaluationCaptureFieldSelectionV1]
    input_availability: MetricAvailabilityV1
    expected_output_availability: MetricAvailabilityV1
    recorded_output_field_path: str
    recorded_output_availability: MetricAvailabilityV1
    content_digest: str
    void_reason: str
    created_at: _timestamp_pb2.Timestamp
    source_content_refs: _containers.RepeatedCompositeFieldContainer[EvaluationSpanContentHydrationV1]
    draft_state: DatasetCaseDraftStateV1
    def __init__(self, proposed_case_id: _Optional[str] = ..., draft_id: _Optional[str] = ..., ordinal: _Optional[int] = ..., state: _Optional[_Union[EvaluationProposedCaseStateV1, str]] = ..., provenance: _Optional[_Union[EvaluationCaptureProvenanceV1, _Mapping]] = ..., selections: _Optional[_Iterable[_Union[EvaluationCaptureFieldSelectionV1, _Mapping]]] = ..., input_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., expected_output_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., recorded_output_field_path: _Optional[str] = ..., recorded_output_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., content_digest: _Optional[str] = ..., void_reason: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., source_content_refs: _Optional[_Iterable[_Union[EvaluationSpanContentHydrationV1, _Mapping]]] = ..., draft_state: _Optional[_Union[DatasetCaseDraftStateV1, str]] = ...) -> None: ...

class EvaluationDatasetVersionDraftV1(_message.Message):
    __slots__ = ("draft_id", "dataset_collection_id", "base_dataset_version_id", "state", "proposed_case_count", "voided_case_count", "draft_version", "finalized_dataset_version_id", "created_at", "updated_at")
    DRAFT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    VOIDED_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    DRAFT_VERSION_FIELD_NUMBER: _ClassVar[int]
    FINALIZED_DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    draft_id: str
    dataset_collection_id: str
    base_dataset_version_id: str
    state: EvaluationDatasetDraftStateV1
    proposed_case_count: int
    voided_case_count: int
    draft_version: int
    finalized_dataset_version_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, draft_id: _Optional[str] = ..., dataset_collection_id: _Optional[str] = ..., base_dataset_version_id: _Optional[str] = ..., state: _Optional[_Union[EvaluationDatasetDraftStateV1, str]] = ..., proposed_case_count: _Optional[int] = ..., voided_case_count: _Optional[int] = ..., draft_version: _Optional[int] = ..., finalized_dataset_version_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EvaluationCaptureRefusalV1(_message.Message):
    __slots__ = ("kind", "detail", "missing_target_paths", "recovery", "existing_proposed_case_id")
    KIND_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    MISSING_TARGET_PATHS_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_FIELD_NUMBER: _ClassVar[int]
    EXISTING_PROPOSED_CASE_ID_FIELD_NUMBER: _ClassVar[int]
    kind: EvaluationCaptureRefusalKindV1
    detail: str
    missing_target_paths: _containers.RepeatedScalarFieldContainer[str]
    recovery: RecoveryActionV1
    existing_proposed_case_id: str
    def __init__(self, kind: _Optional[_Union[EvaluationCaptureRefusalKindV1, str]] = ..., detail: _Optional[str] = ..., missing_target_paths: _Optional[_Iterable[str]] = ..., recovery: _Optional[_Union[RecoveryActionV1, str]] = ..., existing_proposed_case_id: _Optional[str] = ...) -> None: ...

class CaptureEvaluationCaseRequest(_message.Message):
    __slots__ = ("dataset_collection_id", "draft_id", "span", "cell", "field_mappings", "recorded_output_field_path", "idempotency_key", "base_dataset_version_id", "expected_content_digest")
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DRAFT_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_FIELD_NUMBER: _ClassVar[int]
    CELL_FIELD_NUMBER: _ClassVar[int]
    FIELD_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    RECORDED_OUTPUT_FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    BASE_DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_CONTENT_DIGEST_FIELD_NUMBER: _ClassVar[int]
    dataset_collection_id: str
    draft_id: str
    span: EvaluationCaptureSpanSourceV1
    cell: EvaluationCaptureCellSourceV1
    field_mappings: _containers.RepeatedCompositeFieldContainer[DatasetFieldMappingV1]
    recorded_output_field_path: str
    idempotency_key: str
    base_dataset_version_id: str
    expected_content_digest: str
    def __init__(self, dataset_collection_id: _Optional[str] = ..., draft_id: _Optional[str] = ..., span: _Optional[_Union[EvaluationCaptureSpanSourceV1, _Mapping]] = ..., cell: _Optional[_Union[EvaluationCaptureCellSourceV1, _Mapping]] = ..., field_mappings: _Optional[_Iterable[_Union[DatasetFieldMappingV1, _Mapping]]] = ..., recorded_output_field_path: _Optional[str] = ..., idempotency_key: _Optional[str] = ..., base_dataset_version_id: _Optional[str] = ..., expected_content_digest: _Optional[str] = ...) -> None: ...

class CaptureEvaluationCaseResponse(_message.Message):
    __slots__ = ("draft", "proposed_case", "idempotent_replay", "capabilities", "freshness")
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_CASE_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    draft: EvaluationDatasetVersionDraftV1
    proposed_case: EvaluationProposedCaseV1
    idempotent_replay: bool
    capabilities: AgenticEvaluationCapabilitiesV1
    freshness: EvaluationFreshnessV1
    def __init__(self, draft: _Optional[_Union[EvaluationDatasetVersionDraftV1, _Mapping]] = ..., proposed_case: _Optional[_Union[EvaluationProposedCaseV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class EvaluationSpanContentHydrationV1(_message.Message):
    __slots__ = ("content_class", "storage_uri", "byte_size", "availability")
    CONTENT_CLASS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_URI_FIELD_NUMBER: _ClassVar[int]
    BYTE_SIZE_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    content_class: EvaluationSpanContentClassV1
    storage_uri: str
    byte_size: int
    availability: MetricAvailabilityV1
    def __init__(self, content_class: _Optional[_Union[EvaluationSpanContentClassV1, str]] = ..., storage_uri: _Optional[str] = ..., byte_size: _Optional[int] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class EvaluationCapturePreviewFieldV1(_message.Message):
    __slots__ = ("target_path", "materialized_json", "byte_size", "availability")
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    MATERIALIZED_JSON_FIELD_NUMBER: _ClassVar[int]
    BYTE_SIZE_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    target_path: str
    materialized_json: str
    byte_size: int
    availability: MetricAvailabilityV1
    def __init__(self, target_path: _Optional[str] = ..., materialized_json: _Optional[str] = ..., byte_size: _Optional[int] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class PreviewEvaluationCaseCaptureRequest(_message.Message):
    __slots__ = ("dataset_collection_id", "span", "cell", "field_mappings", "recorded_output_field_path")
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_FIELD_NUMBER: _ClassVar[int]
    CELL_FIELD_NUMBER: _ClassVar[int]
    FIELD_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    RECORDED_OUTPUT_FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
    dataset_collection_id: str
    span: EvaluationCaptureSpanSourceV1
    cell: EvaluationCaptureCellSourceV1
    field_mappings: _containers.RepeatedCompositeFieldContainer[DatasetFieldMappingV1]
    recorded_output_field_path: str
    def __init__(self, dataset_collection_id: _Optional[str] = ..., span: _Optional[_Union[EvaluationCaptureSpanSourceV1, _Mapping]] = ..., cell: _Optional[_Union[EvaluationCaptureCellSourceV1, _Mapping]] = ..., field_mappings: _Optional[_Iterable[_Union[DatasetFieldMappingV1, _Mapping]]] = ..., recorded_output_field_path: _Optional[str] = ...) -> None: ...

class PreviewEvaluationCaseCaptureResponse(_message.Message):
    __slots__ = ("provenance", "fields", "selections", "content_hydration", "content_digest", "capture_allowed", "refusal", "capabilities", "freshness", "quality")
    PROVENANCE_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    SELECTIONS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_HYDRATION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DIGEST_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    provenance: EvaluationCaptureProvenanceV1
    fields: _containers.RepeatedCompositeFieldContainer[EvaluationCapturePreviewFieldV1]
    selections: _containers.RepeatedCompositeFieldContainer[EvaluationCaptureFieldSelectionV1]
    content_hydration: _containers.RepeatedCompositeFieldContainer[EvaluationSpanContentHydrationV1]
    content_digest: str
    capture_allowed: bool
    refusal: EvaluationCaptureRefusalV1
    capabilities: AgenticEvaluationCapabilitiesV1
    freshness: EvaluationFreshnessV1
    quality: DatasetCaseQualitySignalsV1
    def __init__(self, provenance: _Optional[_Union[EvaluationCaptureProvenanceV1, _Mapping]] = ..., fields: _Optional[_Iterable[_Union[EvaluationCapturePreviewFieldV1, _Mapping]]] = ..., selections: _Optional[_Iterable[_Union[EvaluationCaptureFieldSelectionV1, _Mapping]]] = ..., content_hydration: _Optional[_Iterable[_Union[EvaluationSpanContentHydrationV1, _Mapping]]] = ..., content_digest: _Optional[str] = ..., capture_allowed: _Optional[bool] = ..., refusal: _Optional[_Union[EvaluationCaptureRefusalV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., quality: _Optional[_Union[DatasetCaseQualitySignalsV1, _Mapping]] = ...) -> None: ...

class EvaluationProviderCredentialV1(_message.Message):
    __slots__ = ("credential_id", "credential_key", "provider", "is_default", "created_at", "secret_version_number", "enabled", "disabled_at", "disabled_reason")
    CREDENTIAL_ID_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_KEY_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    SECRET_VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    DISABLED_AT_FIELD_NUMBER: _ClassVar[int]
    DISABLED_REASON_FIELD_NUMBER: _ClassVar[int]
    credential_id: str
    credential_key: str
    provider: _agentic_pb2.ProviderNameV1
    is_default: bool
    created_at: _timestamp_pb2.Timestamp
    secret_version_number: int
    enabled: bool
    disabled_at: _timestamp_pb2.Timestamp
    disabled_reason: str
    def __init__(self, credential_id: _Optional[str] = ..., credential_key: _Optional[str] = ..., provider: _Optional[_Union[_agentic_pb2.ProviderNameV1, str]] = ..., is_default: _Optional[bool] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., secret_version_number: _Optional[int] = ..., enabled: _Optional[bool] = ..., disabled_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., disabled_reason: _Optional[str] = ...) -> None: ...

class EvaluationProviderCredentialRejectionV1(_message.Message):
    __slots__ = ("kind", "reason_code", "registered_credential_count", "max_credential_count", "detail", "recovery")
    KIND_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_CREDENTIAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_CREDENTIAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_FIELD_NUMBER: _ClassVar[int]
    kind: EvaluationProviderCredentialRejectionKindV1
    reason_code: str
    registered_credential_count: int
    max_credential_count: int
    detail: str
    recovery: RecoveryActionV1
    def __init__(self, kind: _Optional[_Union[EvaluationProviderCredentialRejectionKindV1, str]] = ..., reason_code: _Optional[str] = ..., registered_credential_count: _Optional[int] = ..., max_credential_count: _Optional[int] = ..., detail: _Optional[str] = ..., recovery: _Optional[_Union[RecoveryActionV1, str]] = ...) -> None: ...

class RegisterEvaluationProviderCredentialRequest(_message.Message):
    __slots__ = ("credential_key", "provider", "key_material", "is_default", "idempotency_key")
    CREDENTIAL_KEY_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    KEY_MATERIAL_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    credential_key: str
    provider: _agentic_pb2.ProviderNameV1
    key_material: str
    is_default: bool
    idempotency_key: str
    def __init__(self, credential_key: _Optional[str] = ..., provider: _Optional[_Union[_agentic_pb2.ProviderNameV1, str]] = ..., key_material: _Optional[str] = ..., is_default: _Optional[bool] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class RegisterEvaluationProviderCredentialResponse(_message.Message):
    __slots__ = ("credential", "idempotent_replay", "capabilities")
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    credential: EvaluationProviderCredentialV1
    idempotent_replay: bool
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, credential: _Optional[_Union[EvaluationProviderCredentialV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class EvaluationScorerDeterministicSpecV1(_message.Message):
    __slots__ = ("evaluator", "subject_path", "expected_path")
    EVALUATOR_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_PATH_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_PATH_FIELD_NUMBER: _ClassVar[int]
    evaluator: EvaluationScorerEvaluatorV1
    subject_path: str
    expected_path: str
    def __init__(self, evaluator: _Optional[_Union[EvaluationScorerEvaluatorV1, str]] = ..., subject_path: _Optional[str] = ..., expected_path: _Optional[str] = ...) -> None: ...

class EvaluationScorerReviewPolicySpecV1(_message.Message):
    __slots__ = ("reviewers_per_cell", "blind", "claim_size", "reservation_minutes", "adjudication_minimum")
    REVIEWERS_PER_CELL_FIELD_NUMBER: _ClassVar[int]
    BLIND_FIELD_NUMBER: _ClassVar[int]
    CLAIM_SIZE_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_MINUTES_FIELD_NUMBER: _ClassVar[int]
    ADJUDICATION_MINIMUM_FIELD_NUMBER: _ClassVar[int]
    reviewers_per_cell: int
    blind: bool
    claim_size: int
    reservation_minutes: int
    adjudication_minimum: int
    def __init__(self, reviewers_per_cell: _Optional[int] = ..., blind: _Optional[bool] = ..., claim_size: _Optional[int] = ..., reservation_minutes: _Optional[int] = ..., adjudication_minimum: _Optional[int] = ...) -> None: ...

class EvaluationScorerConfigV1(_message.Message):
    __slots__ = ("score_config_id", "config_key", "name", "description", "metric_name", "success_dimension", "version_discriminator", "kind", "weight", "is_blocking_gate", "deterministic", "review_policy", "created_at", "judge")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    VERSION_DISCRIMINATOR_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    IS_BLOCKING_GATE_FIELD_NUMBER: _ClassVar[int]
    DETERMINISTIC_FIELD_NUMBER: _ClassVar[int]
    REVIEW_POLICY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    JUDGE_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    config_key: str
    name: str
    description: str
    metric_name: str
    success_dimension: str
    version_discriminator: str
    kind: EvaluationScorerKindV1
    weight: float
    is_blocking_gate: bool
    deterministic: EvaluationScorerDeterministicSpecV1
    review_policy: EvaluationScorerReviewPolicySpecV1
    created_at: _timestamp_pb2.Timestamp
    judge: EvaluationScorerJudgeSpecV1
    def __init__(self, score_config_id: _Optional[str] = ..., config_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., metric_name: _Optional[str] = ..., success_dimension: _Optional[str] = ..., version_discriminator: _Optional[str] = ..., kind: _Optional[_Union[EvaluationScorerKindV1, str]] = ..., weight: _Optional[float] = ..., is_blocking_gate: _Optional[bool] = ..., deterministic: _Optional[_Union[EvaluationScorerDeterministicSpecV1, _Mapping]] = ..., review_policy: _Optional[_Union[EvaluationScorerReviewPolicySpecV1, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., judge: _Optional[_Union[EvaluationScorerJudgeSpecV1, _Mapping]] = ...) -> None: ...

class EvaluationScorerConfigRejectionV1(_message.Message):
    __slots__ = ("kind", "reason_code", "pinned_run_count", "pinned_run_ids", "detail", "recovery", "review_policy_field", "review_policy_observed_value", "review_policy_bound", "judge_provider")
    KIND_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    PINNED_RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    PINNED_RUN_IDS_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_FIELD_NUMBER: _ClassVar[int]
    REVIEW_POLICY_FIELD_FIELD_NUMBER: _ClassVar[int]
    REVIEW_POLICY_OBSERVED_VALUE_FIELD_NUMBER: _ClassVar[int]
    REVIEW_POLICY_BOUND_FIELD_NUMBER: _ClassVar[int]
    JUDGE_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    kind: EvaluationScorerConfigRejectionKindV1
    reason_code: str
    pinned_run_count: int
    pinned_run_ids: _containers.RepeatedScalarFieldContainer[str]
    detail: str
    recovery: RecoveryActionV1
    review_policy_field: str
    review_policy_observed_value: int
    review_policy_bound: int
    judge_provider: _agentic_pb2.ProviderNameV1
    def __init__(self, kind: _Optional[_Union[EvaluationScorerConfigRejectionKindV1, str]] = ..., reason_code: _Optional[str] = ..., pinned_run_count: _Optional[int] = ..., pinned_run_ids: _Optional[_Iterable[str]] = ..., detail: _Optional[str] = ..., recovery: _Optional[_Union[RecoveryActionV1, str]] = ..., review_policy_field: _Optional[str] = ..., review_policy_observed_value: _Optional[int] = ..., review_policy_bound: _Optional[int] = ..., judge_provider: _Optional[_Union[_agentic_pb2.ProviderNameV1, str]] = ...) -> None: ...

class EvaluationScorerJudgeVerdictMappingV1(_message.Message):
    __slots__ = ("verdict", "mapped_score")
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    MAPPED_SCORE_FIELD_NUMBER: _ClassVar[int]
    verdict: str
    mapped_score: float
    def __init__(self, verdict: _Optional[str] = ..., mapped_score: _Optional[float] = ...) -> None: ...

class EvaluationScorerJudgeRubricV1(_message.Message):
    __slots__ = ("rubric", "instructions", "verdict_mappings", "subject_path")
    RUBRIC_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    VERDICT_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_PATH_FIELD_NUMBER: _ClassVar[int]
    rubric: str
    instructions: str
    verdict_mappings: _containers.RepeatedCompositeFieldContainer[EvaluationScorerJudgeVerdictMappingV1]
    subject_path: str
    def __init__(self, rubric: _Optional[str] = ..., instructions: _Optional[str] = ..., verdict_mappings: _Optional[_Iterable[_Union[EvaluationScorerJudgeVerdictMappingV1, _Mapping]]] = ..., subject_path: _Optional[str] = ...) -> None: ...

class EvaluationScorerJudgeTemplateRefV1(_message.Message):
    __slots__ = ("evaluator_template_id", "template_version_discriminator")
    EVALUATOR_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_VERSION_DISCRIMINATOR_FIELD_NUMBER: _ClassVar[int]
    evaluator_template_id: str
    template_version_discriminator: str
    def __init__(self, evaluator_template_id: _Optional[str] = ..., template_version_discriminator: _Optional[str] = ...) -> None: ...

class EvaluationScorerJudgeProviderExecutionV1(_message.Message):
    __slots__ = ("model", "credential_ref", "request_settings", "provider_endpoint_ref", "reasoning_effort")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_REF_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ENDPOINT_REF_FIELD_NUMBER: _ClassVar[int]
    REASONING_EFFORT_FIELD_NUMBER: _ClassVar[int]
    model: _agentic_pb2.ProviderModelRefV1
    credential_ref: str
    request_settings: _agentic_pb2.ProviderRequestSettingsV1
    provider_endpoint_ref: str
    reasoning_effort: _agentic_pb2.ProviderReasoningEffortV1
    def __init__(self, model: _Optional[_Union[_agentic_pb2.ProviderModelRefV1, _Mapping]] = ..., credential_ref: _Optional[str] = ..., request_settings: _Optional[_Union[_agentic_pb2.ProviderRequestSettingsV1, _Mapping]] = ..., provider_endpoint_ref: _Optional[str] = ..., reasoning_effort: _Optional[_Union[_agentic_pb2.ProviderReasoningEffortV1, str]] = ...) -> None: ...

class EvaluationScorerJudgeSpecV1(_message.Message):
    __slots__ = ("rubric_content", "template_ref", "provider_execution", "pass_threshold")
    RUBRIC_CONTENT_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_REF_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    PASS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    rubric_content: EvaluationScorerJudgeRubricV1
    template_ref: EvaluationScorerJudgeTemplateRefV1
    provider_execution: EvaluationScorerJudgeProviderExecutionV1
    pass_threshold: float
    def __init__(self, rubric_content: _Optional[_Union[EvaluationScorerJudgeRubricV1, _Mapping]] = ..., template_ref: _Optional[_Union[EvaluationScorerJudgeTemplateRefV1, _Mapping]] = ..., provider_execution: _Optional[_Union[EvaluationScorerJudgeProviderExecutionV1, _Mapping]] = ..., pass_threshold: _Optional[float] = ...) -> None: ...

class CreateEvaluationScorerConfigRequest(_message.Message):
    __slots__ = ("config_key", "name", "description", "metric_name", "success_dimension", "kind", "weight", "is_blocking_gate", "deterministic", "review_policy", "idempotency_key", "judge")
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    IS_BLOCKING_GATE_FIELD_NUMBER: _ClassVar[int]
    DETERMINISTIC_FIELD_NUMBER: _ClassVar[int]
    REVIEW_POLICY_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    JUDGE_FIELD_NUMBER: _ClassVar[int]
    config_key: str
    name: str
    description: str
    metric_name: str
    success_dimension: str
    kind: EvaluationScorerKindV1
    weight: float
    is_blocking_gate: bool
    deterministic: EvaluationScorerDeterministicSpecV1
    review_policy: EvaluationScorerReviewPolicySpecV1
    idempotency_key: str
    judge: EvaluationScorerJudgeSpecV1
    def __init__(self, config_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., metric_name: _Optional[str] = ..., success_dimension: _Optional[str] = ..., kind: _Optional[_Union[EvaluationScorerKindV1, str]] = ..., weight: _Optional[float] = ..., is_blocking_gate: _Optional[bool] = ..., deterministic: _Optional[_Union[EvaluationScorerDeterministicSpecV1, _Mapping]] = ..., review_policy: _Optional[_Union[EvaluationScorerReviewPolicySpecV1, _Mapping]] = ..., idempotency_key: _Optional[str] = ..., judge: _Optional[_Union[EvaluationScorerJudgeSpecV1, _Mapping]] = ...) -> None: ...

class CreateEvaluationScorerConfigResponse(_message.Message):
    __slots__ = ("scorer_config", "idempotent_replay", "capabilities")
    SCORER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    scorer_config: EvaluationScorerConfigV1
    idempotent_replay: bool
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, scorer_config: _Optional[_Union[EvaluationScorerConfigV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class EvaluationDatasetCaseAbsenceV1(_message.Message):
    __slots__ = ("line_number", "absence_code")
    LINE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ABSENCE_CODE_FIELD_NUMBER: _ClassVar[int]
    line_number: int
    absence_code: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, line_number: _Optional[int] = ..., absence_code: _Optional[_Iterable[str]] = ...) -> None: ...

class EvaluationDatasetVersionV1(_message.Message):
    __slots__ = ("dataset_version_id", "dataset_collection_id", "collection_name", "version_number", "label", "case_count", "case_count_availability", "schema_fingerprint", "schema_fingerprint_availability", "created_at", "is_pinned", "picker_retired_at")
    DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CASE_COUNT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FINGERPRINT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_PINNED_FIELD_NUMBER: _ClassVar[int]
    PICKER_RETIRED_AT_FIELD_NUMBER: _ClassVar[int]
    dataset_version_id: str
    dataset_collection_id: str
    collection_name: str
    version_number: int
    label: str
    case_count: int
    case_count_availability: MetricAvailabilityV1
    schema_fingerprint: str
    schema_fingerprint_availability: MetricAvailabilityV1
    created_at: _timestamp_pb2.Timestamp
    is_pinned: bool
    picker_retired_at: _timestamp_pb2.Timestamp
    def __init__(self, dataset_version_id: _Optional[str] = ..., dataset_collection_id: _Optional[str] = ..., collection_name: _Optional[str] = ..., version_number: _Optional[int] = ..., label: _Optional[str] = ..., case_count: _Optional[int] = ..., case_count_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., schema_fingerprint: _Optional[str] = ..., schema_fingerprint_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., is_pinned: _Optional[bool] = ..., picker_retired_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EvaluationDatasetRolloverV1(_message.Message):
    __slots__ = ("retired_dataset_version_id", "retired_version_number", "reason_code", "retired_at")
    RETIRED_DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    RETIRED_VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    RETIRED_AT_FIELD_NUMBER: _ClassVar[int]
    retired_dataset_version_id: str
    retired_version_number: int
    reason_code: str
    retired_at: _timestamp_pb2.Timestamp
    def __init__(self, retired_dataset_version_id: _Optional[str] = ..., retired_version_number: _Optional[int] = ..., reason_code: _Optional[str] = ..., retired_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EvaluationDatasetVersionRejectionV1(_message.Message):
    __slots__ = ("kind", "reason_code", "line_number", "observed_count", "max_count", "detail", "recovery")
    KIND_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    LINE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_COUNT_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_FIELD_NUMBER: _ClassVar[int]
    kind: EvaluationDatasetVersionRejectionKindV1
    reason_code: str
    line_number: int
    observed_count: int
    max_count: int
    detail: str
    recovery: RecoveryActionV1
    def __init__(self, kind: _Optional[_Union[EvaluationDatasetVersionRejectionKindV1, str]] = ..., reason_code: _Optional[str] = ..., line_number: _Optional[int] = ..., observed_count: _Optional[int] = ..., max_count: _Optional[int] = ..., detail: _Optional[str] = ..., recovery: _Optional[_Union[RecoveryActionV1, str]] = ...) -> None: ...

class CreateEvaluationDatasetVersionRequest(_message.Message):
    __slots__ = ("dataset_collection_id", "collection_name", "label", "jsonl", "draft_id", "recorded_output_field_path", "expected_draft_version", "idempotency_key", "declared_schema")
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    JSONL_FIELD_NUMBER: _ClassVar[int]
    DRAFT_ID_FIELD_NUMBER: _ClassVar[int]
    RECORDED_OUTPUT_FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_DRAFT_VERSION_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    DECLARED_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    dataset_collection_id: str
    collection_name: str
    label: str
    jsonl: bytes
    draft_id: str
    recorded_output_field_path: str
    expected_draft_version: int
    idempotency_key: str
    declared_schema: DatasetSchemaShapeV1
    def __init__(self, dataset_collection_id: _Optional[str] = ..., collection_name: _Optional[str] = ..., label: _Optional[str] = ..., jsonl: _Optional[bytes] = ..., draft_id: _Optional[str] = ..., recorded_output_field_path: _Optional[str] = ..., expected_draft_version: _Optional[int] = ..., idempotency_key: _Optional[str] = ..., declared_schema: _Optional[_Union[DatasetSchemaShapeV1, _Mapping]] = ...) -> None: ...

class CreateEvaluationDatasetVersionResponse(_message.Message):
    __slots__ = ("version", "case_absences", "rollover", "idempotent_replay", "capabilities")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CASE_ABSENCES_FIELD_NUMBER: _ClassVar[int]
    ROLLOVER_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    version: EvaluationDatasetVersionV1
    case_absences: _containers.RepeatedCompositeFieldContainer[EvaluationDatasetCaseAbsenceV1]
    rollover: EvaluationDatasetRolloverV1
    idempotent_replay: bool
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, version: _Optional[_Union[EvaluationDatasetVersionV1, _Mapping]] = ..., case_absences: _Optional[_Iterable[_Union[EvaluationDatasetCaseAbsenceV1, _Mapping]]] = ..., rollover: _Optional[_Union[EvaluationDatasetRolloverV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class SetEvaluationProviderCredentialEnabledRequest(_message.Message):
    __slots__ = ("credential_id", "enabled", "reason", "idempotency_key")
    CREDENTIAL_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    credential_id: str
    enabled: bool
    reason: str
    idempotency_key: str
    def __init__(self, credential_id: _Optional[str] = ..., enabled: _Optional[bool] = ..., reason: _Optional[str] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class EvaluationCredentialBlastRadiusV1(_message.Message):
    __slots__ = ("evaluator_template_count", "scorer_config_count", "live_judge_regrade_job_count", "live_run_count", "live_run_availability", "evaluation_definition_count", "evaluation_definition_availability", "enforcement_posture_code", "stops_in_flight_work")
    EVALUATOR_TEMPLATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SCORER_CONFIG_COUNT_FIELD_NUMBER: _ClassVar[int]
    LIVE_JUDGE_REGRADE_JOB_COUNT_FIELD_NUMBER: _ClassVar[int]
    LIVE_RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    LIVE_RUN_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_DEFINITION_COUNT_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_DEFINITION_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    ENFORCEMENT_POSTURE_CODE_FIELD_NUMBER: _ClassVar[int]
    STOPS_IN_FLIGHT_WORK_FIELD_NUMBER: _ClassVar[int]
    evaluator_template_count: int
    scorer_config_count: int
    live_judge_regrade_job_count: int
    live_run_count: int
    live_run_availability: MetricAvailabilityV1
    evaluation_definition_count: int
    evaluation_definition_availability: MetricAvailabilityV1
    enforcement_posture_code: str
    stops_in_flight_work: bool
    def __init__(self, evaluator_template_count: _Optional[int] = ..., scorer_config_count: _Optional[int] = ..., live_judge_regrade_job_count: _Optional[int] = ..., live_run_count: _Optional[int] = ..., live_run_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., evaluation_definition_count: _Optional[int] = ..., evaluation_definition_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., enforcement_posture_code: _Optional[str] = ..., stops_in_flight_work: _Optional[bool] = ...) -> None: ...

class SetEvaluationProviderCredentialEnabledResponse(_message.Message):
    __slots__ = ("credential", "idempotent_replay", "state_changed", "capabilities", "blast_radius")
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    STATE_CHANGED_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    BLAST_RADIUS_FIELD_NUMBER: _ClassVar[int]
    credential: EvaluationProviderCredentialV1
    idempotent_replay: bool
    state_changed: bool
    capabilities: AgenticEvaluationCapabilitiesV1
    blast_radius: EvaluationCredentialBlastRadiusV1
    def __init__(self, credential: _Optional[_Union[EvaluationProviderCredentialV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ..., state_changed: _Optional[bool] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., blast_radius: _Optional[_Union[EvaluationCredentialBlastRadiusV1, _Mapping]] = ...) -> None: ...

class EvaluationScorerSuiteMemberRefusalV1(_message.Message):
    __slots__ = ("score_config_id", "config_key", "reason_code", "evaluator_kind", "weight")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_KIND_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    config_key: str
    reason_code: str
    evaluator_kind: str
    weight: float
    def __init__(self, score_config_id: _Optional[str] = ..., config_key: _Optional[str] = ..., reason_code: _Optional[str] = ..., evaluator_kind: _Optional[str] = ..., weight: _Optional[float] = ...) -> None: ...

class EvaluationScorerSuiteRejectionV1(_message.Message):
    __slots__ = ("kind", "reason_code", "member_count", "max_member_count", "unresolved_score_config_ids", "detail", "offending_members")
    KIND_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNRESOLVED_SCORE_CONFIG_IDS_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    OFFENDING_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    kind: EvaluationScorerSuiteRejectionKindV1
    reason_code: str
    member_count: int
    max_member_count: int
    unresolved_score_config_ids: _containers.RepeatedScalarFieldContainer[str]
    detail: str
    offending_members: _containers.RepeatedCompositeFieldContainer[EvaluationScorerSuiteMemberRefusalV1]
    def __init__(self, kind: _Optional[_Union[EvaluationScorerSuiteRejectionKindV1, str]] = ..., reason_code: _Optional[str] = ..., member_count: _Optional[int] = ..., max_member_count: _Optional[int] = ..., unresolved_score_config_ids: _Optional[_Iterable[str]] = ..., detail: _Optional[str] = ..., offending_members: _Optional[_Iterable[_Union[EvaluationScorerSuiteMemberRefusalV1, _Mapping]]] = ...) -> None: ...

class CreateEvaluationScorerSuiteRequest(_message.Message):
    __slots__ = ("suite_key", "name", "combine_rule", "members", "idempotency_key")
    SUITE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMBINE_RULE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    suite_key: str
    name: str
    combine_rule: EvaluationScorerSuiteCombineRuleV1
    members: _containers.RepeatedCompositeFieldContainer[EvaluationScorerSuiteMemberV1]
    idempotency_key: str
    def __init__(self, suite_key: _Optional[str] = ..., name: _Optional[str] = ..., combine_rule: _Optional[_Union[EvaluationScorerSuiteCombineRuleV1, str]] = ..., members: _Optional[_Iterable[_Union[EvaluationScorerSuiteMemberV1, _Mapping]]] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class EvaluationDerivedSuiteCoordinateV1(_message.Message):
    __slots__ = ("scorer_suite_id", "suite_key", "version_discriminator", "member_coordinates", "member_coordinate_count", "omitted_member_coordinate_count")
    SCORER_SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    SUITE_KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_DISCRIMINATOR_FIELD_NUMBER: _ClassVar[int]
    MEMBER_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    MEMBER_COORDINATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    OMITTED_MEMBER_COORDINATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    scorer_suite_id: str
    suite_key: str
    version_discriminator: str
    member_coordinates: _containers.RepeatedCompositeFieldContainer[EvaluationScorerCoordinateV1]
    member_coordinate_count: int
    omitted_member_coordinate_count: int
    def __init__(self, scorer_suite_id: _Optional[str] = ..., suite_key: _Optional[str] = ..., version_discriminator: _Optional[str] = ..., member_coordinates: _Optional[_Iterable[_Union[EvaluationScorerCoordinateV1, _Mapping]]] = ..., member_coordinate_count: _Optional[int] = ..., omitted_member_coordinate_count: _Optional[int] = ...) -> None: ...

class CreateEvaluationScorerSuiteResponse(_message.Message):
    __slots__ = ("scorer_suite", "idempotent_replay", "capabilities")
    SCORER_SUITE_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    scorer_suite: EvaluationScorerSuiteV1
    idempotent_replay: bool
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, scorer_suite: _Optional[_Union[EvaluationScorerSuiteV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class EvaluationJudgeRegradeScorerPinV1(_message.Message):
    __slots__ = ("evaluator", "metric_name", "pass_threshold")
    EVALUATOR_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    PASS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    evaluator: EvaluationFrozenEvaluatorRefV1
    metric_name: str
    pass_threshold: float
    def __init__(self, evaluator: _Optional[_Union[EvaluationFrozenEvaluatorRefV1, _Mapping]] = ..., metric_name: _Optional[str] = ..., pass_threshold: _Optional[float] = ...) -> None: ...

class EvaluationJudgeRegradeCandidateFieldV1(_message.Message):
    __slots__ = ("candidate_key", "dataset_field")
    CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_FIELD_NUMBER: _ClassVar[int]
    candidate_key: str
    dataset_field: str
    def __init__(self, candidate_key: _Optional[str] = ..., dataset_field: _Optional[str] = ...) -> None: ...

class EvaluationJudgeRegradePinV1(_message.Message):
    __slots__ = ("scorers", "candidate_fields")
    SCORERS_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    scorers: _containers.RepeatedCompositeFieldContainer[EvaluationJudgeRegradeScorerPinV1]
    candidate_fields: _containers.RepeatedCompositeFieldContainer[EvaluationJudgeRegradeCandidateFieldV1]
    def __init__(self, scorers: _Optional[_Iterable[_Union[EvaluationJudgeRegradeScorerPinV1, _Mapping]]] = ..., candidate_fields: _Optional[_Iterable[_Union[EvaluationJudgeRegradeCandidateFieldV1, _Mapping]]] = ...) -> None: ...

class EvaluationJudgeRegradeCellStatusV1(_message.Message):
    __slots__ = ("coordinate", "accepted", "ineligibility", "scorer_key", "current_verdict", "prior_scorer_attempt", "derived_suite")
    COORDINATE_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    INELIGIBILITY_FIELD_NUMBER: _ClassVar[int]
    SCORER_KEY_FIELD_NUMBER: _ClassVar[int]
    CURRENT_VERDICT_FIELD_NUMBER: _ClassVar[int]
    PRIOR_SCORER_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    DERIVED_SUITE_FIELD_NUMBER: _ClassVar[int]
    coordinate: EvaluationScorerCoordinateV1
    accepted: bool
    ineligibility: EvaluationJudgeRegradeIneligibilityV1
    scorer_key: str
    current_verdict: EvaluationVerdictV1
    prior_scorer_attempt: int
    derived_suite: EvaluationDerivedSuiteCoordinateV1
    def __init__(self, coordinate: _Optional[_Union[EvaluationScorerCoordinateV1, _Mapping]] = ..., accepted: _Optional[bool] = ..., ineligibility: _Optional[_Union[EvaluationJudgeRegradeIneligibilityV1, str]] = ..., scorer_key: _Optional[str] = ..., current_verdict: _Optional[_Union[EvaluationVerdictV1, str]] = ..., prior_scorer_attempt: _Optional[int] = ..., derived_suite: _Optional[_Union[EvaluationDerivedSuiteCoordinateV1, _Mapping]] = ...) -> None: ...

class EvaluationJudgeRegradeCellProgressV1(_message.Message):
    __slots__ = ("coordinate", "state", "scorer_key", "attempt_count", "max_attempts", "verdict", "score", "scorer_attempt", "evaluator_execution", "failure")
    COORDINATE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SCORER_KEY_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SCORER_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    coordinate: EvaluationScorerCoordinateV1
    state: EvaluationJudgeRegradeCellStateV1
    scorer_key: str
    attempt_count: int
    max_attempts: int
    verdict: EvaluationVerdictV1
    score: float
    scorer_attempt: int
    evaluator_execution: ExecutionMetricsV1
    failure: EvaluationFailureV1
    def __init__(self, coordinate: _Optional[_Union[EvaluationScorerCoordinateV1, _Mapping]] = ..., state: _Optional[_Union[EvaluationJudgeRegradeCellStateV1, str]] = ..., scorer_key: _Optional[str] = ..., attempt_count: _Optional[int] = ..., max_attempts: _Optional[int] = ..., verdict: _Optional[_Union[EvaluationVerdictV1, str]] = ..., score: _Optional[float] = ..., scorer_attempt: _Optional[int] = ..., evaluator_execution: _Optional[_Union[ExecutionMetricsV1, _Mapping]] = ..., failure: _Optional[_Union[EvaluationFailureV1, _Mapping]] = ...) -> None: ...

class EvaluationJudgeRegradeJobV1(_message.Message):
    __slots__ = ("regrade_job_id", "evaluation_run_id", "state", "requested_cell_count", "accepted_cell_count", "completed_cell_count", "failed_cell_count", "created_at", "started_at", "finished_at", "failure", "evaluator_pins", "evaluator_pin_digest", "cancelled_cell_count", "cancellation_requested_at", "cancel_reason")
    REGRADE_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_PINS_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_PIN_DIGEST_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    CANCEL_REASON_FIELD_NUMBER: _ClassVar[int]
    regrade_job_id: str
    evaluation_run_id: str
    state: EvaluationJudgeRegradeJobStateV1
    requested_cell_count: int
    accepted_cell_count: int
    completed_cell_count: int
    failed_cell_count: int
    created_at: _timestamp_pb2.Timestamp
    started_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    failure: EvaluationFailureV1
    evaluator_pins: _containers.RepeatedCompositeFieldContainer[EvaluationJudgeRegradeScorerPinV1]
    evaluator_pin_digest: str
    cancelled_cell_count: int
    cancellation_requested_at: _timestamp_pb2.Timestamp
    cancel_reason: str
    def __init__(self, regrade_job_id: _Optional[str] = ..., evaluation_run_id: _Optional[str] = ..., state: _Optional[_Union[EvaluationJudgeRegradeJobStateV1, str]] = ..., requested_cell_count: _Optional[int] = ..., accepted_cell_count: _Optional[int] = ..., completed_cell_count: _Optional[int] = ..., failed_cell_count: _Optional[int] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., failure: _Optional[_Union[EvaluationFailureV1, _Mapping]] = ..., evaluator_pins: _Optional[_Iterable[_Union[EvaluationJudgeRegradeScorerPinV1, _Mapping]]] = ..., evaluator_pin_digest: _Optional[str] = ..., cancelled_cell_count: _Optional[int] = ..., cancellation_requested_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., cancel_reason: _Optional[str] = ...) -> None: ...

class EvaluationJudgeRegradeRejectionV1(_message.Message):
    __slots__ = ("reason_code", "requested_cell_count", "max_cell_count", "live_job_count", "max_live_job_count", "detail")
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    LIVE_JOB_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_LIVE_JOB_COUNT_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    reason_code: str
    requested_cell_count: int
    max_cell_count: int
    live_job_count: int
    max_live_job_count: int
    detail: str
    def __init__(self, reason_code: _Optional[str] = ..., requested_cell_count: _Optional[int] = ..., max_cell_count: _Optional[int] = ..., live_job_count: _Optional[int] = ..., max_live_job_count: _Optional[int] = ..., detail: _Optional[str] = ...) -> None: ...

class RequestEvaluationJudgeRegradeRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "coordinates", "idempotency_key", "expected_evaluator_pin_digest")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    COORDINATES_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_EVALUATOR_PIN_DIGEST_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    coordinates: _containers.RepeatedCompositeFieldContainer[EvaluationScorerCoordinateV1]
    idempotency_key: str
    expected_evaluator_pin_digest: str
    def __init__(self, evaluation_run_id: _Optional[str] = ..., coordinates: _Optional[_Iterable[_Union[EvaluationScorerCoordinateV1, _Mapping]]] = ..., idempotency_key: _Optional[str] = ..., expected_evaluator_pin_digest: _Optional[str] = ...) -> None: ...

class RequestEvaluationJudgeRegradeResponse(_message.Message):
    __slots__ = ("job", "coordinates", "accepted_cell_count", "external_calls_issued", "idempotent_replay", "superseded_evidence_code", "allowed_actions", "capabilities")
    JOB_FIELD_NUMBER: _ClassVar[int]
    COORDINATES_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CALLS_ISSUED_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    SUPERSEDED_EVIDENCE_CODE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    job: EvaluationJudgeRegradeJobV1
    coordinates: _containers.RepeatedCompositeFieldContainer[EvaluationJudgeRegradeCellStatusV1]
    accepted_cell_count: int
    external_calls_issued: int
    idempotent_replay: bool
    superseded_evidence_code: str
    allowed_actions: _containers.RepeatedCompositeFieldContainer[AllowedActionV1]
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, job: _Optional[_Union[EvaluationJudgeRegradeJobV1, _Mapping]] = ..., coordinates: _Optional[_Iterable[_Union[EvaluationJudgeRegradeCellStatusV1, _Mapping]]] = ..., accepted_cell_count: _Optional[int] = ..., external_calls_issued: _Optional[int] = ..., idempotent_replay: _Optional[bool] = ..., superseded_evidence_code: _Optional[str] = ..., allowed_actions: _Optional[_Iterable[_Union[AllowedActionV1, _Mapping]]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class GetEvaluationJudgeRegradeJobRequest(_message.Message):
    __slots__ = ("regrade_job_id", "idempotency_key")
    REGRADE_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    regrade_job_id: str
    idempotency_key: str
    def __init__(self, regrade_job_id: _Optional[str] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class GetEvaluationJudgeRegradeJobResponse(_message.Message):
    __slots__ = ("job", "cells", "freshness", "capabilities", "queue_depth", "pinned_rates")
    JOB_FIELD_NUMBER: _ClassVar[int]
    CELLS_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    QUEUE_DEPTH_FIELD_NUMBER: _ClassVar[int]
    PINNED_RATES_FIELD_NUMBER: _ClassVar[int]
    job: EvaluationJudgeRegradeJobV1
    cells: _containers.RepeatedCompositeFieldContainer[EvaluationJudgeRegradeCellProgressV1]
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    queue_depth: EvaluationJudgeRegradeQueueDepthV1
    pinned_rates: _containers.RepeatedCompositeFieldContainer[EvaluationJudgeRegradePinnedRateV1]
    def __init__(self, job: _Optional[_Union[EvaluationJudgeRegradeJobV1, _Mapping]] = ..., cells: _Optional[_Iterable[_Union[EvaluationJudgeRegradeCellProgressV1, _Mapping]]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., queue_depth: _Optional[_Union[EvaluationJudgeRegradeQueueDepthV1, _Mapping]] = ..., pinned_rates: _Optional[_Iterable[_Union[EvaluationJudgeRegradePinnedRateV1, _Mapping]]] = ...) -> None: ...

class EvaluationJudgeRegradeEstimateV1(_message.Message):
    __slots__ = ("estimated_external_call_count", "evaluator_cost", "evaluator_cost_availability", "cost_assumption", "priced_coordinate_count", "unpriced_coordinate_count")
    ESTIMATED_EXTERNAL_CALL_COUNT_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_COST_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_COST_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    COST_ASSUMPTION_FIELD_NUMBER: _ClassVar[int]
    PRICED_COORDINATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNPRICED_COORDINATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    estimated_external_call_count: int
    evaluator_cost: CostAmountV1
    evaluator_cost_availability: MetricAvailabilityV1
    cost_assumption: EvaluationCostAssumptionV1
    priced_coordinate_count: int
    unpriced_coordinate_count: int
    def __init__(self, estimated_external_call_count: _Optional[int] = ..., evaluator_cost: _Optional[_Union[CostAmountV1, _Mapping]] = ..., evaluator_cost_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., cost_assumption: _Optional[_Union[EvaluationCostAssumptionV1, _Mapping]] = ..., priced_coordinate_count: _Optional[int] = ..., unpriced_coordinate_count: _Optional[int] = ...) -> None: ...

class PreviewEvaluationJudgeRegradeRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "coordinates")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    COORDINATES_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    coordinates: _containers.RepeatedCompositeFieldContainer[EvaluationScorerCoordinateV1]
    def __init__(self, evaluation_run_id: _Optional[str] = ..., coordinates: _Optional[_Iterable[_Union[EvaluationScorerCoordinateV1, _Mapping]]] = ...) -> None: ...

class PreviewEvaluationJudgeRegradeResponse(_message.Message):
    __slots__ = ("evaluation_run_id", "coordinates", "acceptable_cell_count", "estimate", "regrade_allowed", "blocked_reason_code", "evaluator_pins", "evaluator_pin_digest", "live_job_count", "max_live_job_count", "external_calls_issued", "superseded_evidence_code", "allowed_actions", "capabilities", "freshness", "evaluator_pin_binding_required", "evaluator_pin_binding_code", "pinned_rates")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    COORDINATES_FIELD_NUMBER: _ClassVar[int]
    ACCEPTABLE_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    REGRADE_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_PINS_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_PIN_DIGEST_FIELD_NUMBER: _ClassVar[int]
    LIVE_JOB_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_LIVE_JOB_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CALLS_ISSUED_FIELD_NUMBER: _ClassVar[int]
    SUPERSEDED_EVIDENCE_CODE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_PIN_BINDING_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_PIN_BINDING_CODE_FIELD_NUMBER: _ClassVar[int]
    PINNED_RATES_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    coordinates: _containers.RepeatedCompositeFieldContainer[EvaluationJudgeRegradeCellStatusV1]
    acceptable_cell_count: int
    estimate: EvaluationJudgeRegradeEstimateV1
    regrade_allowed: bool
    blocked_reason_code: str
    evaluator_pins: _containers.RepeatedCompositeFieldContainer[EvaluationJudgeRegradeScorerPinV1]
    evaluator_pin_digest: str
    live_job_count: int
    max_live_job_count: int
    external_calls_issued: int
    superseded_evidence_code: str
    allowed_actions: _containers.RepeatedCompositeFieldContainer[AllowedActionV1]
    capabilities: AgenticEvaluationCapabilitiesV1
    freshness: EvaluationFreshnessV1
    evaluator_pin_binding_required: bool
    evaluator_pin_binding_code: str
    pinned_rates: _containers.RepeatedCompositeFieldContainer[EvaluationJudgeRegradePinnedRateV1]
    def __init__(self, evaluation_run_id: _Optional[str] = ..., coordinates: _Optional[_Iterable[_Union[EvaluationJudgeRegradeCellStatusV1, _Mapping]]] = ..., acceptable_cell_count: _Optional[int] = ..., estimate: _Optional[_Union[EvaluationJudgeRegradeEstimateV1, _Mapping]] = ..., regrade_allowed: _Optional[bool] = ..., blocked_reason_code: _Optional[str] = ..., evaluator_pins: _Optional[_Iterable[_Union[EvaluationJudgeRegradeScorerPinV1, _Mapping]]] = ..., evaluator_pin_digest: _Optional[str] = ..., live_job_count: _Optional[int] = ..., max_live_job_count: _Optional[int] = ..., external_calls_issued: _Optional[int] = ..., superseded_evidence_code: _Optional[str] = ..., allowed_actions: _Optional[_Iterable[_Union[AllowedActionV1, _Mapping]]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., evaluator_pin_binding_required: _Optional[bool] = ..., evaluator_pin_binding_code: _Optional[str] = ..., pinned_rates: _Optional[_Iterable[_Union[EvaluationJudgeRegradePinnedRateV1, _Mapping]]] = ...) -> None: ...

class EvaluationJudgeRegradePinnedRateV1(_message.Message):
    __slots__ = ("score_config_id", "config_key", "model_id", "comparison", "pinned_rate_checked_date", "current_rate_checked_date", "pinned_cost_per_call", "current_cost_per_call", "governance_code")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_FIELD_NUMBER: _ClassVar[int]
    PINNED_RATE_CHECKED_DATE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_RATE_CHECKED_DATE_FIELD_NUMBER: _ClassVar[int]
    PINNED_COST_PER_CALL_FIELD_NUMBER: _ClassVar[int]
    CURRENT_COST_PER_CALL_FIELD_NUMBER: _ClassVar[int]
    GOVERNANCE_CODE_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    config_key: str
    model_id: str
    comparison: EvaluationJudgeRegradeRateComparisonV1
    pinned_rate_checked_date: str
    current_rate_checked_date: str
    pinned_cost_per_call: CostAmountV1
    current_cost_per_call: CostAmountV1
    governance_code: str
    def __init__(self, score_config_id: _Optional[str] = ..., config_key: _Optional[str] = ..., model_id: _Optional[str] = ..., comparison: _Optional[_Union[EvaluationJudgeRegradeRateComparisonV1, str]] = ..., pinned_rate_checked_date: _Optional[str] = ..., current_rate_checked_date: _Optional[str] = ..., pinned_cost_per_call: _Optional[_Union[CostAmountV1, _Mapping]] = ..., current_cost_per_call: _Optional[_Union[CostAmountV1, _Mapping]] = ..., governance_code: _Optional[str] = ...) -> None: ...

class EvaluationJudgeRegradeQueueDepthV1(_message.Message):
    __slots__ = ("pending_cell_count", "leased_cell_count", "cells_ahead_in_org", "position_availability", "depth_scope_code", "wait_estimate_reason_code")
    PENDING_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    LEASED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    CELLS_AHEAD_IN_ORG_FIELD_NUMBER: _ClassVar[int]
    POSITION_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    DEPTH_SCOPE_CODE_FIELD_NUMBER: _ClassVar[int]
    WAIT_ESTIMATE_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    pending_cell_count: int
    leased_cell_count: int
    cells_ahead_in_org: int
    position_availability: MetricAvailabilityV1
    depth_scope_code: str
    wait_estimate_reason_code: str
    def __init__(self, pending_cell_count: _Optional[int] = ..., leased_cell_count: _Optional[int] = ..., cells_ahead_in_org: _Optional[int] = ..., position_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., depth_scope_code: _Optional[str] = ..., wait_estimate_reason_code: _Optional[str] = ...) -> None: ...

class CancelEvaluationJudgeRegradeJobRequest(_message.Message):
    __slots__ = ("regrade_job_id", "idempotency_key", "reason")
    REGRADE_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    regrade_job_id: str
    idempotency_key: str
    reason: str
    def __init__(self, regrade_job_id: _Optional[str] = ..., idempotency_key: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class CancelEvaluationJudgeRegradeJobResponse(_message.Message):
    __slots__ = ("job", "cells", "already_cancelled", "cancelled_cell_count", "in_flight_cell_count", "retained_evaluator_cost", "capabilities")
    JOB_FIELD_NUMBER: _ClassVar[int]
    CELLS_FIELD_NUMBER: _ClassVar[int]
    ALREADY_CANCELLED_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    IN_FLIGHT_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    RETAINED_EVALUATOR_COST_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    job: EvaluationJudgeRegradeJobV1
    cells: _containers.RepeatedCompositeFieldContainer[EvaluationJudgeRegradeCellProgressV1]
    already_cancelled: bool
    cancelled_cell_count: int
    in_flight_cell_count: int
    retained_evaluator_cost: CostAmountV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, job: _Optional[_Union[EvaluationJudgeRegradeJobV1, _Mapping]] = ..., cells: _Optional[_Iterable[_Union[EvaluationJudgeRegradeCellProgressV1, _Mapping]]] = ..., already_cancelled: _Optional[bool] = ..., cancelled_cell_count: _Optional[int] = ..., in_flight_cell_count: _Optional[int] = ..., retained_evaluator_cost: _Optional[_Union[CostAmountV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class EvaluationRunSummaryV1(_message.Message):
    __slots__ = ("evaluation_run_id", "definition_id", "definition_revision_id", "state", "cancellation_requested_at", "launched_by", "created_at", "started_at", "finished_at", "idempotency_key", "accepted_preview_digest", "failure", "expected_cell_count", "prepared_cell_count", "cancelled_cell_count", "projection_availability", "projection_version", "executed_cell_count", "succeeded_cell_count", "failed_cell_count", "candidate_failure_count", "scorer_failure_count", "verdict_pass_count", "verdict_fail_count", "cost_availability", "token_availability", "latency_availability", "instrumentation_availability", "release_marker_availability")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    LAUNCHED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_PREVIEW_DIGEST_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    PREPARED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUCCEEDED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SCORER_FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    VERDICT_PASS_COUNT_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FAIL_COUNT_FIELD_NUMBER: _ClassVar[int]
    COST_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    TOKEN_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    LATENCY_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTATION_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    RELEASE_MARKER_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    definition_id: str
    definition_revision_id: str
    state: EvaluationRunStateV1
    cancellation_requested_at: _timestamp_pb2.Timestamp
    launched_by: PrincipalRefV1
    created_at: _timestamp_pb2.Timestamp
    started_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    idempotency_key: str
    accepted_preview_digest: str
    failure: EvaluationFailureV1
    expected_cell_count: int
    prepared_cell_count: int
    cancelled_cell_count: int
    projection_availability: MetricAvailabilityV1
    projection_version: int
    executed_cell_count: int
    succeeded_cell_count: int
    failed_cell_count: int
    candidate_failure_count: int
    scorer_failure_count: int
    verdict_pass_count: int
    verdict_fail_count: int
    cost_availability: MetricAvailabilityV1
    token_availability: MetricAvailabilityV1
    latency_availability: MetricAvailabilityV1
    instrumentation_availability: MetricAvailabilityV1
    release_marker_availability: MetricAvailabilityV1
    def __init__(self, evaluation_run_id: _Optional[str] = ..., definition_id: _Optional[str] = ..., definition_revision_id: _Optional[str] = ..., state: _Optional[_Union[EvaluationRunStateV1, str]] = ..., cancellation_requested_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., launched_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., idempotency_key: _Optional[str] = ..., accepted_preview_digest: _Optional[str] = ..., failure: _Optional[_Union[EvaluationFailureV1, _Mapping]] = ..., expected_cell_count: _Optional[int] = ..., prepared_cell_count: _Optional[int] = ..., cancelled_cell_count: _Optional[int] = ..., projection_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., projection_version: _Optional[int] = ..., executed_cell_count: _Optional[int] = ..., succeeded_cell_count: _Optional[int] = ..., failed_cell_count: _Optional[int] = ..., candidate_failure_count: _Optional[int] = ..., scorer_failure_count: _Optional[int] = ..., verdict_pass_count: _Optional[int] = ..., verdict_fail_count: _Optional[int] = ..., cost_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., token_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., latency_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., instrumentation_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., release_marker_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class EvaluationRunListFilterV1(_message.Message):
    __slots__ = ("states", "created_after", "created_before")
    STATES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AFTER_FIELD_NUMBER: _ClassVar[int]
    CREATED_BEFORE_FIELD_NUMBER: _ClassVar[int]
    states: _containers.RepeatedScalarFieldContainer[EvaluationRunStateV1]
    created_after: _timestamp_pb2.Timestamp
    created_before: _timestamp_pb2.Timestamp
    def __init__(self, states: _Optional[_Iterable[_Union[EvaluationRunStateV1, str]]] = ..., created_after: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_before: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListEvaluationRunsRequest(_message.Message):
    __slots__ = ("definition_id", "page", "filter")
    DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    definition_id: str
    page: _common_pb2.PageRequestV1
    filter: EvaluationRunListFilterV1
    def __init__(self, definition_id: _Optional[str] = ..., page: _Optional[_Union[_common_pb2.PageRequestV1, _Mapping]] = ..., filter: _Optional[_Union[EvaluationRunListFilterV1, _Mapping]] = ...) -> None: ...

class ListEvaluationRunsResponse(_message.Message):
    __slots__ = ("runs", "page", "freshness", "capabilities", "resync")
    RUNS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    RESYNC_FIELD_NUMBER: _ClassVar[int]
    runs: _containers.RepeatedCompositeFieldContainer[EvaluationRunSummaryV1]
    page: _common_pb2.PageResponseV1
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    resync: EvaluationCursorResyncV1
    def __init__(self, runs: _Optional[_Iterable[_Union[EvaluationRunSummaryV1, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponseV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., resync: _Optional[_Union[EvaluationCursorResyncV1, _Mapping]] = ...) -> None: ...

class EvaluationReviewTaskRefusalV1(_message.Message):
    __slots__ = ("kind", "reason_code", "offending_review_task_ids", "recovery", "detail")
    KIND_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    OFFENDING_REVIEW_TASK_IDS_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    kind: EvaluationReviewTaskRefusalKindV1
    reason_code: str
    offending_review_task_ids: _containers.RepeatedScalarFieldContainer[str]
    recovery: RecoveryActionV1
    detail: str
    def __init__(self, kind: _Optional[_Union[EvaluationReviewTaskRefusalKindV1, str]] = ..., reason_code: _Optional[str] = ..., offending_review_task_ids: _Optional[_Iterable[str]] = ..., recovery: _Optional[_Union[RecoveryActionV1, str]] = ..., detail: _Optional[str] = ...) -> None: ...

class ReleaseEvaluationReviewTasksRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "review_task_ids", "idempotency_key")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    REVIEW_TASK_IDS_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    review_task_ids: _containers.RepeatedScalarFieldContainer[str]
    idempotency_key: str
    def __init__(self, evaluation_run_id: _Optional[str] = ..., review_task_ids: _Optional[_Iterable[str]] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class ReleaseEvaluationReviewTasksResponse(_message.Message):
    __slots__ = ("released_review_task_ids", "already_released_review_task_ids", "freshness", "capabilities")
    RELEASED_REVIEW_TASK_IDS_FIELD_NUMBER: _ClassVar[int]
    ALREADY_RELEASED_REVIEW_TASK_IDS_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    released_review_task_ids: _containers.RepeatedScalarFieldContainer[str]
    already_released_review_task_ids: _containers.RepeatedScalarFieldContainer[str]
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, released_review_task_ids: _Optional[_Iterable[str]] = ..., already_released_review_task_ids: _Optional[_Iterable[str]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class RequeueEvaluationReviewTasksRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "review_task_ids", "reason", "idempotency_key")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    REVIEW_TASK_IDS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    review_task_ids: _containers.RepeatedScalarFieldContainer[str]
    reason: EvaluationReviewRequeueReasonV1
    idempotency_key: str
    def __init__(self, evaluation_run_id: _Optional[str] = ..., review_task_ids: _Optional[_Iterable[str]] = ..., reason: _Optional[_Union[EvaluationReviewRequeueReasonV1, str]] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class RequeueEvaluationReviewTasksResponse(_message.Message):
    __slots__ = ("requeued_review_task_ids", "already_pending_review_task_ids", "freshness", "capabilities")
    REQUEUED_REVIEW_TASK_IDS_FIELD_NUMBER: _ClassVar[int]
    ALREADY_PENDING_REVIEW_TASK_IDS_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    requeued_review_task_ids: _containers.RepeatedScalarFieldContainer[str]
    already_pending_review_task_ids: _containers.RepeatedScalarFieldContainer[str]
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, requeued_review_task_ids: _Optional[_Iterable[str]] = ..., already_pending_review_task_ids: _Optional[_Iterable[str]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class EvaluationScorerTargetRefV1(_message.Message):
    __slots__ = ("score_config_id", "scorer_suite_id")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    SCORER_SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    scorer_suite_id: str
    def __init__(self, score_config_id: _Optional[str] = ..., scorer_suite_id: _Optional[str] = ...) -> None: ...

class ProductionRuleActionConditionV1(_message.Message):
    __slots__ = ("kind", "scorer_key", "threshold", "verdict")
    KIND_FIELD_NUMBER: _ClassVar[int]
    SCORER_KEY_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    kind: ProductionRuleActionConditionKindV1
    scorer_key: str
    threshold: float
    verdict: str
    def __init__(self, kind: _Optional[_Union[ProductionRuleActionConditionKindV1, str]] = ..., scorer_key: _Optional[str] = ..., threshold: _Optional[float] = ..., verdict: _Optional[str] = ...) -> None: ...

class ProductionRuleActionV1(_message.Message):
    __slots__ = ("ordinal", "action_kind", "condition", "idempotency_key_template", "depends_on_ordinals", "target")
    ORDINAL_FIELD_NUMBER: _ClassVar[int]
    ACTION_KIND_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    DEPENDS_ON_ORDINALS_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    ordinal: int
    action_kind: ProductionRuleActionKindV1
    condition: ProductionRuleActionConditionV1
    idempotency_key_template: str
    depends_on_ordinals: _containers.RepeatedScalarFieldContainer[int]
    target: ProductionRuleActionTargetV1
    def __init__(self, ordinal: _Optional[int] = ..., action_kind: _Optional[_Union[ProductionRuleActionKindV1, str]] = ..., condition: _Optional[_Union[ProductionRuleActionConditionV1, _Mapping]] = ..., idempotency_key_template: _Optional[str] = ..., depends_on_ordinals: _Optional[_Iterable[int]] = ..., target: _Optional[_Union[ProductionRuleActionTargetV1, _Mapping]] = ...) -> None: ...

class ProductionRuleBudgetPolicyV1(_message.Message):
    __slots__ = ("candidate_budget_micros", "evaluator_budget_micros", "daily_budget_micros")
    CANDIDATE_BUDGET_MICROS_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_BUDGET_MICROS_FIELD_NUMBER: _ClassVar[int]
    DAILY_BUDGET_MICROS_FIELD_NUMBER: _ClassVar[int]
    candidate_budget_micros: int
    evaluator_budget_micros: int
    daily_budget_micros: int
    def __init__(self, candidate_budget_micros: _Optional[int] = ..., evaluator_budget_micros: _Optional[int] = ..., daily_budget_micros: _Optional[int] = ...) -> None: ...

class ProductionRuleDependencyRefV1(_message.Message):
    __slots__ = ("kind", "dependency_id")
    KIND_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCY_ID_FIELD_NUMBER: _ClassVar[int]
    kind: ProductionRuleDependencyKindV1
    dependency_id: str
    def __init__(self, kind: _Optional[_Union[ProductionRuleDependencyKindV1, str]] = ..., dependency_id: _Optional[str] = ...) -> None: ...

class ProductionRuleVersionDraftV1(_message.Message):
    __slots__ = ("runtime_scope", "scorer_target", "sampling_rate_percent", "idle_timeout_seconds", "actions", "dependencies", "budget", "change_summary")
    RUNTIME_SCOPE_FIELD_NUMBER: _ClassVar[int]
    SCORER_TARGET_FIELD_NUMBER: _ClassVar[int]
    SAMPLING_RATE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    IDLE_TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    BUDGET_FIELD_NUMBER: _ClassVar[int]
    CHANGE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    runtime_scope: ProductionRuleRuntimeScopeV1
    scorer_target: EvaluationScorerTargetRefV1
    sampling_rate_percent: float
    idle_timeout_seconds: int
    actions: _containers.RepeatedCompositeFieldContainer[ProductionRuleActionV1]
    dependencies: _containers.RepeatedCompositeFieldContainer[ProductionRuleDependencyRefV1]
    budget: ProductionRuleBudgetPolicyV1
    change_summary: str
    def __init__(self, runtime_scope: _Optional[_Union[ProductionRuleRuntimeScopeV1, str]] = ..., scorer_target: _Optional[_Union[EvaluationScorerTargetRefV1, _Mapping]] = ..., sampling_rate_percent: _Optional[float] = ..., idle_timeout_seconds: _Optional[int] = ..., actions: _Optional[_Iterable[_Union[ProductionRuleActionV1, _Mapping]]] = ..., dependencies: _Optional[_Iterable[_Union[ProductionRuleDependencyRefV1, _Mapping]]] = ..., budget: _Optional[_Union[ProductionRuleBudgetPolicyV1, _Mapping]] = ..., change_summary: _Optional[str] = ...) -> None: ...

class ProductionRuleVersionV1(_message.Message):
    __slots__ = ("version_id", "rule_id", "version_number", "state", "content", "content_digest", "disabled_reason_code", "created_by", "created_at", "activated_at", "paused_at", "superseded_at", "disabled_at", "archived_at", "last_state_changed_by", "last_state_change_reason", "last_state_changed_at")
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DIGEST_FIELD_NUMBER: _ClassVar[int]
    DISABLED_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ACTIVATED_AT_FIELD_NUMBER: _ClassVar[int]
    PAUSED_AT_FIELD_NUMBER: _ClassVar[int]
    SUPERSEDED_AT_FIELD_NUMBER: _ClassVar[int]
    DISABLED_AT_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_STATE_CHANGED_BY_FIELD_NUMBER: _ClassVar[int]
    LAST_STATE_CHANGE_REASON_FIELD_NUMBER: _ClassVar[int]
    LAST_STATE_CHANGED_AT_FIELD_NUMBER: _ClassVar[int]
    version_id: str
    rule_id: str
    version_number: int
    state: ProductionRuleVersionStateV1
    content: ProductionRuleVersionDraftV1
    content_digest: str
    disabled_reason_code: str
    created_by: PrincipalRefV1
    created_at: _timestamp_pb2.Timestamp
    activated_at: _timestamp_pb2.Timestamp
    paused_at: _timestamp_pb2.Timestamp
    superseded_at: _timestamp_pb2.Timestamp
    disabled_at: _timestamp_pb2.Timestamp
    archived_at: _timestamp_pb2.Timestamp
    last_state_changed_by: PrincipalRefV1
    last_state_change_reason: str
    last_state_changed_at: _timestamp_pb2.Timestamp
    def __init__(self, version_id: _Optional[str] = ..., rule_id: _Optional[str] = ..., version_number: _Optional[int] = ..., state: _Optional[_Union[ProductionRuleVersionStateV1, str]] = ..., content: _Optional[_Union[ProductionRuleVersionDraftV1, _Mapping]] = ..., content_digest: _Optional[str] = ..., disabled_reason_code: _Optional[str] = ..., created_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., activated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., paused_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., superseded_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., disabled_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., archived_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_state_changed_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., last_state_change_reason: _Optional[str] = ..., last_state_changed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ProductionRuleHealthV1(_message.Message):
    __slots__ = ("rule_id", "version_id", "state", "dependency_health", "latest_actionable_error_code", "latest_actionable_error_at", "evaluated_at", "execution_counts_availability", "freshness", "execution_counts", "timings")
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCY_HEALTH_FIELD_NUMBER: _ClassVar[int]
    LATEST_ACTIONABLE_ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    LATEST_ACTIONABLE_ERROR_AT_FIELD_NUMBER: _ClassVar[int]
    EVALUATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_COUNTS_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_COUNTS_FIELD_NUMBER: _ClassVar[int]
    TIMINGS_FIELD_NUMBER: _ClassVar[int]
    rule_id: str
    version_id: str
    state: ProductionRuleHealthStateV1
    dependency_health: ProductionRuleDependencyHealthV1
    latest_actionable_error_code: str
    latest_actionable_error_at: _timestamp_pb2.Timestamp
    evaluated_at: _timestamp_pb2.Timestamp
    execution_counts_availability: MetricAvailabilityV1
    freshness: EvaluationFreshnessV1
    execution_counts: ProductionRuleExecutionCountsV1
    timings: ProductionRuleWorkflowTimingsV1
    def __init__(self, rule_id: _Optional[str] = ..., version_id: _Optional[str] = ..., state: _Optional[_Union[ProductionRuleHealthStateV1, str]] = ..., dependency_health: _Optional[_Union[ProductionRuleDependencyHealthV1, str]] = ..., latest_actionable_error_code: _Optional[str] = ..., latest_actionable_error_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., evaluated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., execution_counts_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., execution_counts: _Optional[_Union[ProductionRuleExecutionCountsV1, _Mapping]] = ..., timings: _Optional[_Union[ProductionRuleWorkflowTimingsV1, _Mapping]] = ...) -> None: ...

class ProductionRuleExecutionCountsV1(_message.Message):
    __slots__ = ("eligible", "matched", "sampled", "scored", "downstream")
    ELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    MATCHED_FIELD_NUMBER: _ClassVar[int]
    SAMPLED_FIELD_NUMBER: _ClassVar[int]
    SCORED_FIELD_NUMBER: _ClassVar[int]
    DOWNSTREAM_FIELD_NUMBER: _ClassVar[int]
    eligible: int
    matched: int
    sampled: int
    scored: int
    downstream: ProductionRuleDownstreamCountsV1
    def __init__(self, eligible: _Optional[int] = ..., matched: _Optional[int] = ..., sampled: _Optional[int] = ..., scored: _Optional[int] = ..., downstream: _Optional[_Union[ProductionRuleDownstreamCountsV1, _Mapping]] = ...) -> None: ...

class ProductionRuleDownstreamCountsV1(_message.Message):
    __slots__ = ("availability", "promoted", "reviewed", "downstream_eval")
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    PROMOTED_FIELD_NUMBER: _ClassVar[int]
    REVIEWED_FIELD_NUMBER: _ClassVar[int]
    DOWNSTREAM_EVAL_FIELD_NUMBER: _ClassVar[int]
    availability: MetricAvailabilityV1
    promoted: int
    reviewed: int
    downstream_eval: int
    def __init__(self, availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., promoted: _Optional[int] = ..., reviewed: _Optional[int] = ..., downstream_eval: _Optional[int] = ...) -> None: ...

class ProductionRuleWorkflowTimingsV1(_message.Message):
    __slots__ = ("last_attempt_at", "last_success_at", "last_failure_at", "next_eligible_work_at", "queue_lag_seconds", "dead_letter_count", "daily_spend_micros", "queue_availability")
    LAST_ATTEMPT_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_SUCCESS_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_FAILURE_AT_FIELD_NUMBER: _ClassVar[int]
    NEXT_ELIGIBLE_WORK_AT_FIELD_NUMBER: _ClassVar[int]
    QUEUE_LAG_SECONDS_FIELD_NUMBER: _ClassVar[int]
    DEAD_LETTER_COUNT_FIELD_NUMBER: _ClassVar[int]
    DAILY_SPEND_MICROS_FIELD_NUMBER: _ClassVar[int]
    QUEUE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    last_attempt_at: _timestamp_pb2.Timestamp
    last_success_at: _timestamp_pb2.Timestamp
    last_failure_at: _timestamp_pb2.Timestamp
    next_eligible_work_at: _timestamp_pb2.Timestamp
    queue_lag_seconds: int
    dead_letter_count: int
    daily_spend_micros: int
    queue_availability: MetricAvailabilityV1
    def __init__(self, last_attempt_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_success_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_failure_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., next_eligible_work_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., queue_lag_seconds: _Optional[int] = ..., dead_letter_count: _Optional[int] = ..., daily_spend_micros: _Optional[int] = ..., queue_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class ProductionRuleV1(_message.Message):
    __slots__ = ("rule_id", "rule_key", "name", "description", "active_version_id", "active_version_number", "created_by", "created_at", "updated_at")
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    rule_id: str
    rule_key: str
    name: str
    description: str
    active_version_id: str
    active_version_number: int
    created_by: PrincipalRefV1
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, rule_id: _Optional[str] = ..., rule_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., active_version_id: _Optional[str] = ..., active_version_number: _Optional[int] = ..., created_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ProductionRuleListItemV1(_message.Message):
    __slots__ = ("rule", "health")
    RULE_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    rule: ProductionRuleV1
    health: ProductionRuleHealthV1
    def __init__(self, rule: _Optional[_Union[ProductionRuleV1, _Mapping]] = ..., health: _Optional[_Union[ProductionRuleHealthV1, _Mapping]] = ...) -> None: ...

class CreateProductionEvaluationRuleRequest(_message.Message):
    __slots__ = ("rule_key", "name", "description", "version", "activate")
    RULE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ACTIVATE_FIELD_NUMBER: _ClassVar[int]
    rule_key: str
    name: str
    description: str
    version: ProductionRuleVersionDraftV1
    activate: bool
    def __init__(self, rule_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., version: _Optional[_Union[ProductionRuleVersionDraftV1, _Mapping]] = ..., activate: _Optional[bool] = ...) -> None: ...

class CreateProductionEvaluationRuleResponse(_message.Message):
    __slots__ = ("rule", "version", "idempotent_replay")
    RULE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    rule: ProductionRuleV1
    version: ProductionRuleVersionV1
    idempotent_replay: bool
    def __init__(self, rule: _Optional[_Union[ProductionRuleV1, _Mapping]] = ..., version: _Optional[_Union[ProductionRuleVersionV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ...) -> None: ...

class CreateProductionEvaluationRuleVersionRequest(_message.Message):
    __slots__ = ("rule_id", "version", "activate")
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ACTIVATE_FIELD_NUMBER: _ClassVar[int]
    rule_id: str
    version: ProductionRuleVersionDraftV1
    activate: bool
    def __init__(self, rule_id: _Optional[str] = ..., version: _Optional[_Union[ProductionRuleVersionDraftV1, _Mapping]] = ..., activate: _Optional[bool] = ...) -> None: ...

class CreateProductionEvaluationRuleVersionResponse(_message.Message):
    __slots__ = ("version", "idempotent_replay")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    version: ProductionRuleVersionV1
    idempotent_replay: bool
    def __init__(self, version: _Optional[_Union[ProductionRuleVersionV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ...) -> None: ...

class SetProductionEvaluationRuleVersionStateRequest(_message.Message):
    __slots__ = ("version_id", "transition", "reason")
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    version_id: str
    transition: ProductionRuleVersionTransitionV1
    reason: str
    def __init__(self, version_id: _Optional[str] = ..., transition: _Optional[_Union[ProductionRuleVersionTransitionV1, str]] = ..., reason: _Optional[str] = ...) -> None: ...

class SetProductionEvaluationRuleVersionStateResponse(_message.Message):
    __slots__ = ("version", "health", "already_in_state")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    ALREADY_IN_STATE_FIELD_NUMBER: _ClassVar[int]
    version: ProductionRuleVersionV1
    health: ProductionRuleHealthV1
    already_in_state: bool
    def __init__(self, version: _Optional[_Union[ProductionRuleVersionV1, _Mapping]] = ..., health: _Optional[_Union[ProductionRuleHealthV1, _Mapping]] = ..., already_in_state: _Optional[bool] = ...) -> None: ...

class ListProductionEvaluationRulesRequest(_message.Message):
    __slots__ = ("limit", "page_token", "health_state")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HEALTH_STATE_FIELD_NUMBER: _ClassVar[int]
    limit: int
    page_token: str
    health_state: ProductionRuleHealthStateV1
    def __init__(self, limit: _Optional[int] = ..., page_token: _Optional[str] = ..., health_state: _Optional[_Union[ProductionRuleHealthStateV1, str]] = ...) -> None: ...

class ListProductionEvaluationRulesResponse(_message.Message):
    __slots__ = ("items", "next_page_token", "has_more", "effective_page_size", "freshness")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ProductionRuleListItemV1]
    next_page_token: str
    has_more: bool
    effective_page_size: int
    freshness: EvaluationFreshnessV1
    def __init__(self, items: _Optional[_Iterable[_Union[ProductionRuleListItemV1, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., has_more: _Optional[bool] = ..., effective_page_size: _Optional[int] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class GetProductionEvaluationRuleRequest(_message.Message):
    __slots__ = ("rule_id",)
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    rule_id: str
    def __init__(self, rule_id: _Optional[str] = ...) -> None: ...

class GetProductionEvaluationRuleResponse(_message.Message):
    __slots__ = ("rule", "active_version", "health", "version_history", "version_history_has_more", "freshness")
    RULE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_VERSION_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    VERSION_HISTORY_FIELD_NUMBER: _ClassVar[int]
    VERSION_HISTORY_HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    rule: ProductionRuleV1
    active_version: ProductionRuleVersionV1
    health: ProductionRuleHealthV1
    version_history: _containers.RepeatedCompositeFieldContainer[ProductionRuleVersionV1]
    version_history_has_more: bool
    freshness: EvaluationFreshnessV1
    def __init__(self, rule: _Optional[_Union[ProductionRuleV1, _Mapping]] = ..., active_version: _Optional[_Union[ProductionRuleVersionV1, _Mapping]] = ..., health: _Optional[_Union[ProductionRuleHealthV1, _Mapping]] = ..., version_history: _Optional[_Iterable[_Union[ProductionRuleVersionV1, _Mapping]]] = ..., version_history_has_more: _Optional[bool] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class ProductionWorkflowScoreOutcomeV1(_message.Message):
    __slots__ = ("scorer_key", "score", "verdict", "scorer_failed", "failure_code", "cost_micros")
    SCORER_KEY_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    SCORER_FAILED_FIELD_NUMBER: _ClassVar[int]
    FAILURE_CODE_FIELD_NUMBER: _ClassVar[int]
    COST_MICROS_FIELD_NUMBER: _ClassVar[int]
    scorer_key: str
    score: float
    verdict: str
    scorer_failed: bool
    failure_code: str
    cost_micros: int
    def __init__(self, scorer_key: _Optional[str] = ..., score: _Optional[float] = ..., verdict: _Optional[str] = ..., scorer_failed: _Optional[bool] = ..., failure_code: _Optional[str] = ..., cost_micros: _Optional[int] = ...) -> None: ...

class ProductionWorkflowCorrelationV1(_message.Message):
    __slots__ = ("correlation_id", "trace_id", "agent_run_id", "root_span_id")
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    correlation_id: str
    trace_id: str
    agent_run_id: str
    root_span_id: str
    def __init__(self, correlation_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., agent_run_id: _Optional[str] = ..., root_span_id: _Optional[str] = ...) -> None: ...

class ProductionWorkflowStepAttemptV1(_message.Message):
    __slots__ = ("attempt_number", "state", "started_at", "finished_at", "error_code", "error_message", "delivery_key", "dispatched")
    ATTEMPT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_KEY_FIELD_NUMBER: _ClassVar[int]
    DISPATCHED_FIELD_NUMBER: _ClassVar[int]
    attempt_number: int
    state: ProductionWorkflowStepStateV1
    started_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    error_code: str
    error_message: str
    delivery_key: str
    dispatched: bool
    def __init__(self, attempt_number: _Optional[int] = ..., state: _Optional[_Union[ProductionWorkflowStepStateV1, str]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error_code: _Optional[str] = ..., error_message: _Optional[str] = ..., delivery_key: _Optional[str] = ..., dispatched: _Optional[bool] = ...) -> None: ...

class ProductionWorkflowStepEffectV1(_message.Message):
    __slots__ = ("production_score_id", "release_block_id", "dataset_proposed_case_id", "review_task_id", "linked_evaluation_run_id", "notification_delivery_id")
    PRODUCTION_SCORE_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_PROPOSED_CASE_ID_FIELD_NUMBER: _ClassVar[int]
    REVIEW_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    LINKED_EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_DELIVERY_ID_FIELD_NUMBER: _ClassVar[int]
    production_score_id: str
    release_block_id: str
    dataset_proposed_case_id: str
    review_task_id: str
    linked_evaluation_run_id: str
    notification_delivery_id: str
    def __init__(self, production_score_id: _Optional[str] = ..., release_block_id: _Optional[str] = ..., dataset_proposed_case_id: _Optional[str] = ..., review_task_id: _Optional[str] = ..., linked_evaluation_run_id: _Optional[str] = ..., notification_delivery_id: _Optional[str] = ...) -> None: ...

class ProductionWorkflowStepV1(_message.Message):
    __slots__ = ("step_id", "ordinal", "action_kind", "state", "skip_reason", "configuration_snapshot", "idempotency_key", "attempt_count", "max_attempts", "next_attempt_at", "latest_error_code", "latest_error_message", "attempts", "attempts_capped", "effect", "created_at", "terminal_at")
    STEP_ID_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_FIELD_NUMBER: _ClassVar[int]
    ACTION_KIND_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SKIP_REASON_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_ATTEMPT_AT_FIELD_NUMBER: _ClassVar[int]
    LATEST_ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    LATEST_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    ATTEMPTS_CAPPED_FIELD_NUMBER: _ClassVar[int]
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    TERMINAL_AT_FIELD_NUMBER: _ClassVar[int]
    step_id: str
    ordinal: int
    action_kind: ProductionRuleActionKindV1
    state: ProductionWorkflowStepStateV1
    skip_reason: ProductionWorkflowStepSkipReasonV1
    configuration_snapshot: ProductionRuleActionV1
    idempotency_key: str
    attempt_count: int
    max_attempts: int
    next_attempt_at: _timestamp_pb2.Timestamp
    latest_error_code: str
    latest_error_message: str
    attempts: _containers.RepeatedCompositeFieldContainer[ProductionWorkflowStepAttemptV1]
    attempts_capped: bool
    effect: ProductionWorkflowStepEffectV1
    created_at: _timestamp_pb2.Timestamp
    terminal_at: _timestamp_pb2.Timestamp
    def __init__(self, step_id: _Optional[str] = ..., ordinal: _Optional[int] = ..., action_kind: _Optional[_Union[ProductionRuleActionKindV1, str]] = ..., state: _Optional[_Union[ProductionWorkflowStepStateV1, str]] = ..., skip_reason: _Optional[_Union[ProductionWorkflowStepSkipReasonV1, str]] = ..., configuration_snapshot: _Optional[_Union[ProductionRuleActionV1, _Mapping]] = ..., idempotency_key: _Optional[str] = ..., attempt_count: _Optional[int] = ..., max_attempts: _Optional[int] = ..., next_attempt_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., latest_error_code: _Optional[str] = ..., latest_error_message: _Optional[str] = ..., attempts: _Optional[_Iterable[_Union[ProductionWorkflowStepAttemptV1, _Mapping]]] = ..., attempts_capped: _Optional[bool] = ..., effect: _Optional[_Union[ProductionWorkflowStepEffectV1, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., terminal_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ProductionWorkflowExecutionV1(_message.Message):
    __slots__ = ("execution_id", "rule_id", "rule_version_id", "rule_version_number", "state", "correlation", "triggered_by", "score_outcome", "match_key", "created_at", "started_at", "terminal_at", "cancellation_reason_code", "spend_micros", "step_count", "steps_succeeded", "steps_failed", "steps_skipped")
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_FIELD_NUMBER: _ClassVar[int]
    TRIGGERED_BY_FIELD_NUMBER: _ClassVar[int]
    SCORE_OUTCOME_FIELD_NUMBER: _ClassVar[int]
    MATCH_KEY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    TERMINAL_AT_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    SPEND_MICROS_FIELD_NUMBER: _ClassVar[int]
    STEP_COUNT_FIELD_NUMBER: _ClassVar[int]
    STEPS_SUCCEEDED_FIELD_NUMBER: _ClassVar[int]
    STEPS_FAILED_FIELD_NUMBER: _ClassVar[int]
    STEPS_SKIPPED_FIELD_NUMBER: _ClassVar[int]
    execution_id: str
    rule_id: str
    rule_version_id: str
    rule_version_number: int
    state: ProductionWorkflowExecutionStateV1
    correlation: ProductionWorkflowCorrelationV1
    triggered_by: PrincipalRefV1
    score_outcome: ProductionWorkflowScoreOutcomeV1
    match_key: str
    created_at: _timestamp_pb2.Timestamp
    started_at: _timestamp_pb2.Timestamp
    terminal_at: _timestamp_pb2.Timestamp
    cancellation_reason_code: str
    spend_micros: int
    step_count: int
    steps_succeeded: int
    steps_failed: int
    steps_skipped: int
    def __init__(self, execution_id: _Optional[str] = ..., rule_id: _Optional[str] = ..., rule_version_id: _Optional[str] = ..., rule_version_number: _Optional[int] = ..., state: _Optional[_Union[ProductionWorkflowExecutionStateV1, str]] = ..., correlation: _Optional[_Union[ProductionWorkflowCorrelationV1, _Mapping]] = ..., triggered_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., score_outcome: _Optional[_Union[ProductionWorkflowScoreOutcomeV1, _Mapping]] = ..., match_key: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., terminal_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., cancellation_reason_code: _Optional[str] = ..., spend_micros: _Optional[int] = ..., step_count: _Optional[int] = ..., steps_succeeded: _Optional[int] = ..., steps_failed: _Optional[int] = ..., steps_skipped: _Optional[int] = ...) -> None: ...

class ProductionReleaseBlockEvidenceRefV1(_message.Message):
    __slots__ = ("kind", "evidence_id")
    KIND_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_ID_FIELD_NUMBER: _ClassVar[int]
    kind: ProductionReleaseBlockEvidenceKindV1
    evidence_id: str
    def __init__(self, kind: _Optional[_Union[ProductionReleaseBlockEvidenceKindV1, str]] = ..., evidence_id: _Optional[str] = ...) -> None: ...

class ProductionReleaseBlockV1(_message.Message):
    __slots__ = ("block_id", "release_key", "state", "rule_id", "rule_version_id", "workflow_execution_id", "workflow_step_id", "block_reason_code", "indeterminate_reason_code", "evidence", "clear_condition", "expires_at", "created_at", "cleared_at", "expired_at", "overridden_by", "override_reason", "override_scope", "overridden_at")
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_KEY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_STEP_ID_FIELD_NUMBER: _ClassVar[int]
    BLOCK_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    INDETERMINATE_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    CLEAR_CONDITION_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CLEARED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_AT_FIELD_NUMBER: _ClassVar[int]
    OVERRIDDEN_BY_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_REASON_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_SCOPE_FIELD_NUMBER: _ClassVar[int]
    OVERRIDDEN_AT_FIELD_NUMBER: _ClassVar[int]
    block_id: str
    release_key: str
    state: ReleaseBlockStateV1
    rule_id: str
    rule_version_id: str
    workflow_execution_id: str
    workflow_step_id: str
    block_reason_code: str
    indeterminate_reason_code: str
    evidence: _containers.RepeatedCompositeFieldContainer[ProductionReleaseBlockEvidenceRefV1]
    clear_condition: ProductionReleaseBlockClearConditionV1
    expires_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    cleared_at: _timestamp_pb2.Timestamp
    expired_at: _timestamp_pb2.Timestamp
    overridden_by: PrincipalRefV1
    override_reason: str
    override_scope: str
    overridden_at: _timestamp_pb2.Timestamp
    def __init__(self, block_id: _Optional[str] = ..., release_key: _Optional[str] = ..., state: _Optional[_Union[ReleaseBlockStateV1, str]] = ..., rule_id: _Optional[str] = ..., rule_version_id: _Optional[str] = ..., workflow_execution_id: _Optional[str] = ..., workflow_step_id: _Optional[str] = ..., block_reason_code: _Optional[str] = ..., indeterminate_reason_code: _Optional[str] = ..., evidence: _Optional[_Iterable[_Union[ProductionReleaseBlockEvidenceRefV1, _Mapping]]] = ..., clear_condition: _Optional[_Union[ProductionReleaseBlockClearConditionV1, str]] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., cleared_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expired_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., overridden_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., override_reason: _Optional[str] = ..., override_scope: _Optional[str] = ..., overridden_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StartProductionEvaluationWorkflowRequest(_message.Message):
    __slots__ = ("rule_id", "match_key", "score_outcome", "correlation", "release_key")
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_KEY_FIELD_NUMBER: _ClassVar[int]
    SCORE_OUTCOME_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_FIELD_NUMBER: _ClassVar[int]
    RELEASE_KEY_FIELD_NUMBER: _ClassVar[int]
    rule_id: str
    match_key: str
    score_outcome: ProductionWorkflowScoreOutcomeV1
    correlation: ProductionWorkflowCorrelationV1
    release_key: str
    def __init__(self, rule_id: _Optional[str] = ..., match_key: _Optional[str] = ..., score_outcome: _Optional[_Union[ProductionWorkflowScoreOutcomeV1, _Mapping]] = ..., correlation: _Optional[_Union[ProductionWorkflowCorrelationV1, _Mapping]] = ..., release_key: _Optional[str] = ...) -> None: ...

class StartProductionEvaluationWorkflowResponse(_message.Message):
    __slots__ = ("admission", "execution", "version_state")
    ADMISSION_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_STATE_FIELD_NUMBER: _ClassVar[int]
    admission: ProductionWorkflowAdmissionV1
    execution: ProductionWorkflowExecutionV1
    version_state: ProductionRuleVersionStateV1
    def __init__(self, admission: _Optional[_Union[ProductionWorkflowAdmissionV1, str]] = ..., execution: _Optional[_Union[ProductionWorkflowExecutionV1, _Mapping]] = ..., version_state: _Optional[_Union[ProductionRuleVersionStateV1, str]] = ...) -> None: ...

class ProductionWorkflowExecutionListFilterV1(_message.Message):
    __slots__ = ("rule_id", "rule_version_id", "state")
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    rule_id: str
    rule_version_id: str
    state: ProductionWorkflowExecutionStateV1
    def __init__(self, rule_id: _Optional[str] = ..., rule_version_id: _Optional[str] = ..., state: _Optional[_Union[ProductionWorkflowExecutionStateV1, str]] = ...) -> None: ...

class ListProductionEvaluationWorkflowExecutionsRequest(_message.Message):
    __slots__ = ("limit", "page_token", "filter")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    limit: int
    page_token: str
    filter: ProductionWorkflowExecutionListFilterV1
    def __init__(self, limit: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[_Union[ProductionWorkflowExecutionListFilterV1, _Mapping]] = ...) -> None: ...

class ListProductionEvaluationWorkflowExecutionsResponse(_message.Message):
    __slots__ = ("items", "next_page_token", "has_more", "effective_page_size", "freshness")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ProductionWorkflowExecutionV1]
    next_page_token: str
    has_more: bool
    effective_page_size: int
    freshness: EvaluationFreshnessV1
    def __init__(self, items: _Optional[_Iterable[_Union[ProductionWorkflowExecutionV1, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., has_more: _Optional[bool] = ..., effective_page_size: _Optional[int] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class GetProductionEvaluationWorkflowExecutionRequest(_message.Message):
    __slots__ = ("execution_id",)
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    execution_id: str
    def __init__(self, execution_id: _Optional[str] = ...) -> None: ...

class GetProductionEvaluationWorkflowExecutionResponse(_message.Message):
    __slots__ = ("execution", "steps", "release_blocks", "freshness")
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    RELEASE_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    execution: ProductionWorkflowExecutionV1
    steps: _containers.RepeatedCompositeFieldContainer[ProductionWorkflowStepV1]
    release_blocks: _containers.RepeatedCompositeFieldContainer[ProductionReleaseBlockV1]
    freshness: EvaluationFreshnessV1
    def __init__(self, execution: _Optional[_Union[ProductionWorkflowExecutionV1, _Mapping]] = ..., steps: _Optional[_Iterable[_Union[ProductionWorkflowStepV1, _Mapping]]] = ..., release_blocks: _Optional[_Iterable[_Union[ProductionReleaseBlockV1, _Mapping]]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class RetryProductionEvaluationWorkflowStepRequest(_message.Message):
    __slots__ = ("step_id",)
    STEP_ID_FIELD_NUMBER: _ClassVar[int]
    step_id: str
    def __init__(self, step_id: _Optional[str] = ...) -> None: ...

class RetryProductionEvaluationWorkflowStepResponse(_message.Message):
    __slots__ = ("step", "execution")
    STEP_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    step: ProductionWorkflowStepV1
    execution: ProductionWorkflowExecutionV1
    def __init__(self, step: _Optional[_Union[ProductionWorkflowStepV1, _Mapping]] = ..., execution: _Optional[_Union[ProductionWorkflowExecutionV1, _Mapping]] = ...) -> None: ...

class ProductionReleaseBlockListFilterV1(_message.Message):
    __slots__ = ("release_key", "state", "rule_id")
    RELEASE_KEY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    release_key: str
    state: ReleaseBlockStateV1
    rule_id: str
    def __init__(self, release_key: _Optional[str] = ..., state: _Optional[_Union[ReleaseBlockStateV1, str]] = ..., rule_id: _Optional[str] = ...) -> None: ...

class ListProductionEvaluationReleaseBlocksRequest(_message.Message):
    __slots__ = ("limit", "page_token", "filter")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    limit: int
    page_token: str
    filter: ProductionReleaseBlockListFilterV1
    def __init__(self, limit: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[_Union[ProductionReleaseBlockListFilterV1, _Mapping]] = ...) -> None: ...

class ListProductionEvaluationReleaseBlocksResponse(_message.Message):
    __slots__ = ("items", "next_page_token", "has_more", "effective_page_size", "release_is_blocked", "freshness")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    RELEASE_IS_BLOCKED_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ProductionReleaseBlockV1]
    next_page_token: str
    has_more: bool
    effective_page_size: int
    release_is_blocked: bool
    freshness: EvaluationFreshnessV1
    def __init__(self, items: _Optional[_Iterable[_Union[ProductionReleaseBlockV1, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., has_more: _Optional[bool] = ..., effective_page_size: _Optional[int] = ..., release_is_blocked: _Optional[bool] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class OverrideProductionEvaluationReleaseBlockRequest(_message.Message):
    __slots__ = ("block_id", "reason", "scope")
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    block_id: str
    reason: str
    scope: str
    def __init__(self, block_id: _Optional[str] = ..., reason: _Optional[str] = ..., scope: _Optional[str] = ...) -> None: ...

class OverrideProductionEvaluationReleaseBlockResponse(_message.Message):
    __slots__ = ("block", "already_overridden")
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    ALREADY_OVERRIDDEN_FIELD_NUMBER: _ClassVar[int]
    block: ProductionReleaseBlockV1
    already_overridden: bool
    def __init__(self, block: _Optional[_Union[ProductionReleaseBlockV1, _Mapping]] = ..., already_overridden: _Optional[bool] = ...) -> None: ...

class ReleaseVerificationOverrideV1(_message.Message):
    __slots__ = ("reason", "reason_note", "actor", "overridden_at")
    REASON_FIELD_NUMBER: _ClassVar[int]
    REASON_NOTE_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    OVERRIDDEN_AT_FIELD_NUMBER: _ClassVar[int]
    reason: ReleaseVerificationOverrideReasonV1
    reason_note: str
    actor: PrincipalRefV1
    overridden_at: _timestamp_pb2.Timestamp
    def __init__(self, reason: _Optional[_Union[ReleaseVerificationOverrideReasonV1, str]] = ..., reason_note: _Optional[str] = ..., actor: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., overridden_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ReleaseTargetV1(_message.Message):
    __slots__ = ("target_key", "environment")
    TARGET_KEY_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    target_key: str
    environment: str
    def __init__(self, target_key: _Optional[str] = ..., environment: _Optional[str] = ...) -> None: ...

class ReleaseSigningKeyRefV1(_message.Message):
    __slots__ = ("key_id", "secret_ref", "state", "activated_at", "not_after")
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_REF_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ACTIVATED_AT_FIELD_NUMBER: _ClassVar[int]
    NOT_AFTER_FIELD_NUMBER: _ClassVar[int]
    key_id: str
    secret_ref: str
    state: ReleaseSigningKeyStateV1
    activated_at: _timestamp_pb2.Timestamp
    not_after: _timestamp_pb2.Timestamp
    def __init__(self, key_id: _Optional[str] = ..., secret_ref: _Optional[str] = ..., state: _Optional[_Union[ReleaseSigningKeyStateV1, str]] = ..., activated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., not_after: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ReleaseIntegrationV1(_message.Message):
    __slots__ = ("integration_id", "display_name", "kind", "target", "destination_url", "allowed_domains", "callback_url_template", "supports_callbacks", "supports_polling", "request_timeout_ms", "signing_keys", "health", "health_observed_at", "health_reason_code", "archived", "archived_at", "created_by", "created_at", "updated_at", "supported_operations", "credential")
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_URL_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_URL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_CALLBACKS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_POLLING_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    SIGNING_KEYS_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    HEALTH_OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    HEALTH_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    integration_id: str
    display_name: str
    kind: ReleaseIntegrationKindV1
    target: ReleaseTargetV1
    destination_url: str
    allowed_domains: _containers.RepeatedScalarFieldContainer[str]
    callback_url_template: str
    supports_callbacks: bool
    supports_polling: bool
    request_timeout_ms: int
    signing_keys: _containers.RepeatedCompositeFieldContainer[ReleaseSigningKeyRefV1]
    health: ReleaseIntegrationHealthV1
    health_observed_at: _timestamp_pb2.Timestamp
    health_reason_code: str
    archived: bool
    archived_at: _timestamp_pb2.Timestamp
    created_by: PrincipalRefV1
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    supported_operations: _containers.RepeatedScalarFieldContainer[ReleaseAdapterOperationV1]
    credential: ReleaseIntegrationCredentialRefV1
    def __init__(self, integration_id: _Optional[str] = ..., display_name: _Optional[str] = ..., kind: _Optional[_Union[ReleaseIntegrationKindV1, str]] = ..., target: _Optional[_Union[ReleaseTargetV1, _Mapping]] = ..., destination_url: _Optional[str] = ..., allowed_domains: _Optional[_Iterable[str]] = ..., callback_url_template: _Optional[str] = ..., supports_callbacks: _Optional[bool] = ..., supports_polling: _Optional[bool] = ..., request_timeout_ms: _Optional[int] = ..., signing_keys: _Optional[_Iterable[_Union[ReleaseSigningKeyRefV1, _Mapping]]] = ..., health: _Optional[_Union[ReleaseIntegrationHealthV1, str]] = ..., health_observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., health_reason_code: _Optional[str] = ..., archived: _Optional[bool] = ..., archived_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., supported_operations: _Optional[_Iterable[_Union[ReleaseAdapterOperationV1, str]]] = ..., credential: _Optional[_Union[ReleaseIntegrationCredentialRefV1, _Mapping]] = ...) -> None: ...

class ReleaseIntegrationCredentialRefV1(_message.Message):
    __slots__ = ("credential_id", "secret_ref", "state", "activated_at")
    CREDENTIAL_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_REF_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ACTIVATED_AT_FIELD_NUMBER: _ClassVar[int]
    credential_id: str
    secret_ref: str
    state: ReleaseIntegrationCredentialStateV1
    activated_at: _timestamp_pb2.Timestamp
    def __init__(self, credential_id: _Optional[str] = ..., secret_ref: _Optional[str] = ..., state: _Optional[_Union[ReleaseIntegrationCredentialStateV1, str]] = ..., activated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ReleaseEvidenceSnapshotV1(_message.Message):
    __slots__ = ("evaluation_run_id", "definition_revision_id", "definition_content_digest", "candidate_key", "decision_revision_id", "decision_revision_ordinal", "evidence_projection_version", "decision_policy_version", "algorithm_version", "decision_outcome", "recommended_candidate_key", "reference_candidate_key", "facts_watermark", "snapshotted_at")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_CONTENT_DIGEST_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    DECISION_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    DECISION_REVISION_ORDINAL_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_PROJECTION_VERSION_FIELD_NUMBER: _ClassVar[int]
    DECISION_POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_VERSION_FIELD_NUMBER: _ClassVar[int]
    DECISION_OUTCOME_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    FACTS_WATERMARK_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOTTED_AT_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    definition_revision_id: str
    definition_content_digest: str
    candidate_key: str
    decision_revision_id: str
    decision_revision_ordinal: int
    evidence_projection_version: int
    decision_policy_version: str
    algorithm_version: str
    decision_outcome: EvaluationDecisionOutcomeV1
    recommended_candidate_key: str
    reference_candidate_key: str
    facts_watermark: str
    snapshotted_at: _timestamp_pb2.Timestamp
    def __init__(self, evaluation_run_id: _Optional[str] = ..., definition_revision_id: _Optional[str] = ..., definition_content_digest: _Optional[str] = ..., candidate_key: _Optional[str] = ..., decision_revision_id: _Optional[str] = ..., decision_revision_ordinal: _Optional[int] = ..., evidence_projection_version: _Optional[int] = ..., decision_policy_version: _Optional[str] = ..., algorithm_version: _Optional[str] = ..., decision_outcome: _Optional[_Union[EvaluationDecisionOutcomeV1, str]] = ..., recommended_candidate_key: _Optional[str] = ..., reference_candidate_key: _Optional[str] = ..., facts_watermark: _Optional[str] = ..., snapshotted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ReleasePolicyV1(_message.Message):
    __slots__ = ("automatic_rollback_enabled", "minimum_sample_size", "minimum_failing_conditions", "verification_timeout_seconds", "max_error_rate", "min_quality_score", "max_latency_p95_ms", "max_cost_micros_per_request", "max_evidence_age_seconds")
    AUTOMATIC_ROLLBACK_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_SAMPLE_SIZE_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_FAILING_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MAX_ERROR_RATE_FIELD_NUMBER: _ClassVar[int]
    MIN_QUALITY_SCORE_FIELD_NUMBER: _ClassVar[int]
    MAX_LATENCY_P95_MS_FIELD_NUMBER: _ClassVar[int]
    MAX_COST_MICROS_PER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    MAX_EVIDENCE_AGE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    automatic_rollback_enabled: bool
    minimum_sample_size: int
    minimum_failing_conditions: int
    verification_timeout_seconds: int
    max_error_rate: float
    min_quality_score: float
    max_latency_p95_ms: int
    max_cost_micros_per_request: int
    max_evidence_age_seconds: int
    def __init__(self, automatic_rollback_enabled: _Optional[bool] = ..., minimum_sample_size: _Optional[int] = ..., minimum_failing_conditions: _Optional[int] = ..., verification_timeout_seconds: _Optional[int] = ..., max_error_rate: _Optional[float] = ..., min_quality_score: _Optional[float] = ..., max_latency_p95_ms: _Optional[int] = ..., max_cost_micros_per_request: _Optional[int] = ..., max_evidence_age_seconds: _Optional[int] = ...) -> None: ...

class ReleaseValidationV1(_message.Message):
    __slots__ = ("kind", "state", "reason_code", "remediation", "gate_blocks", "gate_blocks_capped")
    KIND_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    REMEDIATION_FIELD_NUMBER: _ClassVar[int]
    GATE_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    GATE_BLOCKS_CAPPED_FIELD_NUMBER: _ClassVar[int]
    kind: ReleaseValidationKindV1
    state: ReleaseValidationStateV1
    reason_code: str
    remediation: str
    gate_blocks: _containers.RepeatedCompositeFieldContainer[ProductionReleaseBlockV1]
    gate_blocks_capped: bool
    def __init__(self, kind: _Optional[_Union[ReleaseValidationKindV1, str]] = ..., state: _Optional[_Union[ReleaseValidationStateV1, str]] = ..., reason_code: _Optional[str] = ..., remediation: _Optional[str] = ..., gate_blocks: _Optional[_Iterable[_Union[ProductionReleaseBlockV1, _Mapping]]] = ..., gate_blocks_capped: _Optional[bool] = ...) -> None: ...

class ReleasePostureV1(_message.Message):
    __slots__ = ("stage", "latest_action_id", "latest_action_type", "latest_action_state", "latest_action_at", "observed_integration_health", "integration_health_observed_at", "evidence_freshness", "external_drift", "external_drift_reason_code", "allowed_actions", "blocked_actions", "release_blocked_by_policy", "projection_version", "refreshed_at")
    STAGE_FIELD_NUMBER: _ClassVar[int]
    LATEST_ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    LATEST_ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    LATEST_ACTION_STATE_FIELD_NUMBER: _ClassVar[int]
    LATEST_ACTION_AT_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_INTEGRATION_HEALTH_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_HEALTH_OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DRIFT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DRIFT_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    RELEASE_BLOCKED_BY_POLICY_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_VERSION_FIELD_NUMBER: _ClassVar[int]
    REFRESHED_AT_FIELD_NUMBER: _ClassVar[int]
    stage: ReleaseStageV1
    latest_action_id: str
    latest_action_type: ReleaseActionTypeV1
    latest_action_state: ReleaseActionStateV1
    latest_action_at: _timestamp_pb2.Timestamp
    observed_integration_health: ReleaseIntegrationHealthV1
    integration_health_observed_at: _timestamp_pb2.Timestamp
    evidence_freshness: EvaluationFreshnessV1
    external_drift: bool
    external_drift_reason_code: str
    allowed_actions: _containers.RepeatedScalarFieldContainer[ReleaseActionTypeV1]
    blocked_actions: _containers.RepeatedCompositeFieldContainer[ReleaseBlockedActionV1]
    release_blocked_by_policy: bool
    projection_version: int
    refreshed_at: _timestamp_pb2.Timestamp
    def __init__(self, stage: _Optional[_Union[ReleaseStageV1, str]] = ..., latest_action_id: _Optional[str] = ..., latest_action_type: _Optional[_Union[ReleaseActionTypeV1, str]] = ..., latest_action_state: _Optional[_Union[ReleaseActionStateV1, str]] = ..., latest_action_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., observed_integration_health: _Optional[_Union[ReleaseIntegrationHealthV1, str]] = ..., integration_health_observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., evidence_freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., external_drift: _Optional[bool] = ..., external_drift_reason_code: _Optional[str] = ..., allowed_actions: _Optional[_Iterable[_Union[ReleaseActionTypeV1, str]]] = ..., blocked_actions: _Optional[_Iterable[_Union[ReleaseBlockedActionV1, _Mapping]]] = ..., release_blocked_by_policy: _Optional[bool] = ..., projection_version: _Optional[int] = ..., refreshed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ReleaseBlockedActionV1(_message.Message):
    __slots__ = ("action_type", "reason_code")
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    action_type: ReleaseActionTypeV1
    reason_code: str
    def __init__(self, action_type: _Optional[_Union[ReleaseActionTypeV1, str]] = ..., reason_code: _Optional[str] = ...) -> None: ...

class ReleaseV1(_message.Message):
    __slots__ = ("release_id", "display_name", "release_key", "integration_id", "target", "evidence", "policy", "last_known_good_release_id", "stage", "created_by", "created_at", "updated_at", "posture")
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    RELEASE_KEY_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    LAST_KNOWN_GOOD_RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    POSTURE_FIELD_NUMBER: _ClassVar[int]
    release_id: str
    display_name: str
    release_key: str
    integration_id: str
    target: ReleaseTargetV1
    evidence: ReleaseEvidenceSnapshotV1
    policy: ReleasePolicyV1
    last_known_good_release_id: str
    stage: ReleaseStageV1
    created_by: PrincipalRefV1
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    posture: ReleasePostureV1
    def __init__(self, release_id: _Optional[str] = ..., display_name: _Optional[str] = ..., release_key: _Optional[str] = ..., integration_id: _Optional[str] = ..., target: _Optional[_Union[ReleaseTargetV1, _Mapping]] = ..., evidence: _Optional[_Union[ReleaseEvidenceSnapshotV1, _Mapping]] = ..., policy: _Optional[_Union[ReleasePolicyV1, _Mapping]] = ..., last_known_good_release_id: _Optional[str] = ..., stage: _Optional[_Union[ReleaseStageV1, str]] = ..., created_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., posture: _Optional[_Union[ReleasePostureV1, _Mapping]] = ...) -> None: ...

class ReleaseActionV1(_message.Message):
    __slots__ = ("action_id", "release_id", "action_type", "state", "idempotency_key", "external_request_ref", "reason", "reason_note", "actor", "error_code", "error_message", "requested_at", "dispatched_at", "accepted_at", "observed_at", "verified_at", "target_stage", "attempt_count", "verification_override", "superseded_by_action_id")
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REQUEST_REF_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    REASON_NOTE_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    DISPATCHED_AT_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_AT_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    TARGET_STAGE_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_COUNT_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    SUPERSEDED_BY_ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    action_id: str
    release_id: str
    action_type: ReleaseActionTypeV1
    state: ReleaseActionStateV1
    idempotency_key: str
    external_request_ref: str
    reason: ReleaseActionReasonV1
    reason_note: str
    actor: PrincipalRefV1
    error_code: str
    error_message: str
    requested_at: _timestamp_pb2.Timestamp
    dispatched_at: _timestamp_pb2.Timestamp
    accepted_at: _timestamp_pb2.Timestamp
    observed_at: _timestamp_pb2.Timestamp
    verified_at: _timestamp_pb2.Timestamp
    target_stage: ReleaseStageV1
    attempt_count: int
    verification_override: ReleaseVerificationOverrideV1
    superseded_by_action_id: str
    def __init__(self, action_id: _Optional[str] = ..., release_id: _Optional[str] = ..., action_type: _Optional[_Union[ReleaseActionTypeV1, str]] = ..., state: _Optional[_Union[ReleaseActionStateV1, str]] = ..., idempotency_key: _Optional[str] = ..., external_request_ref: _Optional[str] = ..., reason: _Optional[_Union[ReleaseActionReasonV1, str]] = ..., reason_note: _Optional[str] = ..., actor: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., error_code: _Optional[str] = ..., error_message: _Optional[str] = ..., requested_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dispatched_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., accepted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., verified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., target_stage: _Optional[_Union[ReleaseStageV1, str]] = ..., attempt_count: _Optional[int] = ..., verification_override: _Optional[_Union[ReleaseVerificationOverrideV1, _Mapping]] = ..., superseded_by_action_id: _Optional[str] = ...) -> None: ...

class ReleaseActivityEntryV1(_message.Message):
    __slots__ = ("entry_id", "release_id", "activity_kind", "action_id", "from_stage", "to_stage", "reason_code", "actor", "correlation_id", "occurred_at")
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_KIND_FIELD_NUMBER: _ClassVar[int]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_STAGE_FIELD_NUMBER: _ClassVar[int]
    TO_STAGE_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    entry_id: str
    release_id: str
    activity_kind: str
    action_id: str
    from_stage: ReleaseStageV1
    to_stage: ReleaseStageV1
    reason_code: str
    actor: PrincipalRefV1
    correlation_id: str
    occurred_at: _timestamp_pb2.Timestamp
    def __init__(self, entry_id: _Optional[str] = ..., release_id: _Optional[str] = ..., activity_kind: _Optional[str] = ..., action_id: _Optional[str] = ..., from_stage: _Optional[_Union[ReleaseStageV1, str]] = ..., to_stage: _Optional[_Union[ReleaseStageV1, str]] = ..., reason_code: _Optional[str] = ..., actor: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., correlation_id: _Optional[str] = ..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ReleaseStageHistoryEntryV1(_message.Message):
    __slots__ = ("from_stage", "to_stage", "action_id", "cause_code", "entered_at")
    FROM_STAGE_FIELD_NUMBER: _ClassVar[int]
    TO_STAGE_FIELD_NUMBER: _ClassVar[int]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    CAUSE_CODE_FIELD_NUMBER: _ClassVar[int]
    ENTERED_AT_FIELD_NUMBER: _ClassVar[int]
    from_stage: ReleaseStageV1
    to_stage: ReleaseStageV1
    action_id: str
    cause_code: str
    entered_at: _timestamp_pb2.Timestamp
    def __init__(self, from_stage: _Optional[_Union[ReleaseStageV1, str]] = ..., to_stage: _Optional[_Union[ReleaseStageV1, str]] = ..., action_id: _Optional[str] = ..., cause_code: _Optional[str] = ..., entered_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ReleaseIntegrationDraftV1(_message.Message):
    __slots__ = ("display_name", "kind", "target", "destination_url", "allowed_domains", "callback_url_template", "supports_callbacks", "supports_polling", "request_timeout_ms", "signing_key_id", "signing_secret_ref", "signing_secret_material", "credential_id", "credential_secret_ref", "credential_secret_material")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_URL_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_URL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_CALLBACKS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_POLLING_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    SIGNING_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNING_SECRET_REF_FIELD_NUMBER: _ClassVar[int]
    SIGNING_SECRET_MATERIAL_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_ID_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_SECRET_REF_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_SECRET_MATERIAL_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    kind: ReleaseIntegrationKindV1
    target: ReleaseTargetV1
    destination_url: str
    allowed_domains: _containers.RepeatedScalarFieldContainer[str]
    callback_url_template: str
    supports_callbacks: bool
    supports_polling: bool
    request_timeout_ms: int
    signing_key_id: str
    signing_secret_ref: str
    signing_secret_material: str
    credential_id: str
    credential_secret_ref: str
    credential_secret_material: str
    def __init__(self, display_name: _Optional[str] = ..., kind: _Optional[_Union[ReleaseIntegrationKindV1, str]] = ..., target: _Optional[_Union[ReleaseTargetV1, _Mapping]] = ..., destination_url: _Optional[str] = ..., allowed_domains: _Optional[_Iterable[str]] = ..., callback_url_template: _Optional[str] = ..., supports_callbacks: _Optional[bool] = ..., supports_polling: _Optional[bool] = ..., request_timeout_ms: _Optional[int] = ..., signing_key_id: _Optional[str] = ..., signing_secret_ref: _Optional[str] = ..., signing_secret_material: _Optional[str] = ..., credential_id: _Optional[str] = ..., credential_secret_ref: _Optional[str] = ..., credential_secret_material: _Optional[str] = ...) -> None: ...

class CreateReleaseIntegrationRequest(_message.Message):
    __slots__ = ("draft", "idempotency_key")
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    draft: ReleaseIntegrationDraftV1
    idempotency_key: str
    def __init__(self, draft: _Optional[_Union[ReleaseIntegrationDraftV1, _Mapping]] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class CreateReleaseIntegrationResponse(_message.Message):
    __slots__ = ("integration", "idempotent_replay")
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    integration: ReleaseIntegrationV1
    idempotent_replay: bool
    def __init__(self, integration: _Optional[_Union[ReleaseIntegrationV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ...) -> None: ...

class GetReleaseIntegrationRequest(_message.Message):
    __slots__ = ("integration_id",)
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    integration_id: str
    def __init__(self, integration_id: _Optional[str] = ...) -> None: ...

class GetReleaseIntegrationResponse(_message.Message):
    __slots__ = ("integration", "active_release_count", "freshness")
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_RELEASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    integration: ReleaseIntegrationV1
    active_release_count: int
    freshness: EvaluationFreshnessV1
    def __init__(self, integration: _Optional[_Union[ReleaseIntegrationV1, _Mapping]] = ..., active_release_count: _Optional[int] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class ReleaseIntegrationListFilterV1(_message.Message):
    __slots__ = ("kind", "environment", "include_archived", "health")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    kind: ReleaseIntegrationKindV1
    environment: str
    include_archived: bool
    health: ReleaseIntegrationHealthV1
    def __init__(self, kind: _Optional[_Union[ReleaseIntegrationKindV1, str]] = ..., environment: _Optional[str] = ..., include_archived: _Optional[bool] = ..., health: _Optional[_Union[ReleaseIntegrationHealthV1, str]] = ...) -> None: ...

class ListReleaseIntegrationsRequest(_message.Message):
    __slots__ = ("limit", "page_token", "filter")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    limit: int
    page_token: str
    filter: ReleaseIntegrationListFilterV1
    def __init__(self, limit: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[_Union[ReleaseIntegrationListFilterV1, _Mapping]] = ...) -> None: ...

class ListReleaseIntegrationsResponse(_message.Message):
    __slots__ = ("items", "next_page_token", "has_more", "effective_page_size", "freshness")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ReleaseIntegrationV1]
    next_page_token: str
    has_more: bool
    effective_page_size: int
    freshness: EvaluationFreshnessV1
    def __init__(self, items: _Optional[_Iterable[_Union[ReleaseIntegrationV1, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., has_more: _Optional[bool] = ..., effective_page_size: _Optional[int] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class ReleaseIntegrationPatchV1(_message.Message):
    __slots__ = ("display_name", "destination_url", "allowed_domains", "callback_url_template", "supports_callbacks", "supports_polling", "request_timeout_ms", "rotate_to_signing_key_id", "rotate_to_signing_secret_ref", "rotation_window_seconds", "rotate_to_signing_secret_material", "revoke_signing_key_id", "rotate_to_credential_id", "rotate_to_credential_secret_ref", "rotate_to_credential_secret_material")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_URL_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_URL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_CALLBACKS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_POLLING_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    ROTATE_TO_SIGNING_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    ROTATE_TO_SIGNING_SECRET_REF_FIELD_NUMBER: _ClassVar[int]
    ROTATION_WINDOW_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ROTATE_TO_SIGNING_SECRET_MATERIAL_FIELD_NUMBER: _ClassVar[int]
    REVOKE_SIGNING_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    ROTATE_TO_CREDENTIAL_ID_FIELD_NUMBER: _ClassVar[int]
    ROTATE_TO_CREDENTIAL_SECRET_REF_FIELD_NUMBER: _ClassVar[int]
    ROTATE_TO_CREDENTIAL_SECRET_MATERIAL_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    destination_url: str
    allowed_domains: _containers.RepeatedScalarFieldContainer[str]
    callback_url_template: str
    supports_callbacks: bool
    supports_polling: bool
    request_timeout_ms: int
    rotate_to_signing_key_id: str
    rotate_to_signing_secret_ref: str
    rotation_window_seconds: int
    rotate_to_signing_secret_material: str
    revoke_signing_key_id: str
    rotate_to_credential_id: str
    rotate_to_credential_secret_ref: str
    rotate_to_credential_secret_material: str
    def __init__(self, display_name: _Optional[str] = ..., destination_url: _Optional[str] = ..., allowed_domains: _Optional[_Iterable[str]] = ..., callback_url_template: _Optional[str] = ..., supports_callbacks: _Optional[bool] = ..., supports_polling: _Optional[bool] = ..., request_timeout_ms: _Optional[int] = ..., rotate_to_signing_key_id: _Optional[str] = ..., rotate_to_signing_secret_ref: _Optional[str] = ..., rotation_window_seconds: _Optional[int] = ..., rotate_to_signing_secret_material: _Optional[str] = ..., revoke_signing_key_id: _Optional[str] = ..., rotate_to_credential_id: _Optional[str] = ..., rotate_to_credential_secret_ref: _Optional[str] = ..., rotate_to_credential_secret_material: _Optional[str] = ...) -> None: ...

class UpdateReleaseIntegrationRequest(_message.Message):
    __slots__ = ("integration_id", "patch")
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    integration_id: str
    patch: ReleaseIntegrationPatchV1
    def __init__(self, integration_id: _Optional[str] = ..., patch: _Optional[_Union[ReleaseIntegrationPatchV1, _Mapping]] = ...) -> None: ...

class UpdateReleaseIntegrationResponse(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: ReleaseIntegrationV1
    def __init__(self, integration: _Optional[_Union[ReleaseIntegrationV1, _Mapping]] = ...) -> None: ...

class ArchiveReleaseIntegrationRequest(_message.Message):
    __slots__ = ("integration_id",)
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    integration_id: str
    def __init__(self, integration_id: _Optional[str] = ...) -> None: ...

class ArchiveReleaseIntegrationResponse(_message.Message):
    __slots__ = ("integration", "already_archived", "releases_referencing")
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    ALREADY_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    RELEASES_REFERENCING_FIELD_NUMBER: _ClassVar[int]
    integration: ReleaseIntegrationV1
    already_archived: bool
    releases_referencing: int
    def __init__(self, integration: _Optional[_Union[ReleaseIntegrationV1, _Mapping]] = ..., already_archived: _Optional[bool] = ..., releases_referencing: _Optional[int] = ...) -> None: ...

class ReleaseCandidateRefV1(_message.Message):
    __slots__ = ("evaluation_run_id", "candidate_key", "decision_revision_id")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    DECISION_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    candidate_key: str
    decision_revision_id: str
    def __init__(self, evaluation_run_id: _Optional[str] = ..., candidate_key: _Optional[str] = ..., decision_revision_id: _Optional[str] = ...) -> None: ...

class ReleaseDraftV1(_message.Message):
    __slots__ = ("display_name", "release_key", "integration_id", "candidate", "policy", "last_known_good_release_id")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    RELEASE_KEY_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    LAST_KNOWN_GOOD_RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    release_key: str
    integration_id: str
    candidate: ReleaseCandidateRefV1
    policy: ReleasePolicyV1
    last_known_good_release_id: str
    def __init__(self, display_name: _Optional[str] = ..., release_key: _Optional[str] = ..., integration_id: _Optional[str] = ..., candidate: _Optional[_Union[ReleaseCandidateRefV1, _Mapping]] = ..., policy: _Optional[_Union[ReleasePolicyV1, _Mapping]] = ..., last_known_good_release_id: _Optional[str] = ...) -> None: ...

class CreateReleaseRequest(_message.Message):
    __slots__ = ("draft", "idempotency_key")
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    draft: ReleaseDraftV1
    idempotency_key: str
    def __init__(self, draft: _Optional[_Union[ReleaseDraftV1, _Mapping]] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class CreateReleaseResponse(_message.Message):
    __slots__ = ("release", "idempotent_replay", "validations")
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    VALIDATIONS_FIELD_NUMBER: _ClassVar[int]
    release: ReleaseV1
    idempotent_replay: bool
    validations: _containers.RepeatedCompositeFieldContainer[ReleaseValidationV1]
    def __init__(self, release: _Optional[_Union[ReleaseV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ..., validations: _Optional[_Iterable[_Union[ReleaseValidationV1, _Mapping]]] = ...) -> None: ...

class PreviewReleaseRequest(_message.Message):
    __slots__ = ("release_id", "draft")
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    release_id: str
    draft: ReleaseDraftV1
    def __init__(self, release_id: _Optional[str] = ..., draft: _Optional[_Union[ReleaseDraftV1, _Mapping]] = ...) -> None: ...

class PreviewReleaseResponse(_message.Message):
    __slots__ = ("validations", "evidence", "would_allow_actions", "external_calls_made", "freshness")
    VALIDATIONS_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    WOULD_ALLOW_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CALLS_MADE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    validations: _containers.RepeatedCompositeFieldContainer[ReleaseValidationV1]
    evidence: ReleaseEvidenceSnapshotV1
    would_allow_actions: _containers.RepeatedScalarFieldContainer[ReleaseActionTypeV1]
    external_calls_made: int
    freshness: EvaluationFreshnessV1
    def __init__(self, validations: _Optional[_Iterable[_Union[ReleaseValidationV1, _Mapping]]] = ..., evidence: _Optional[_Union[ReleaseEvidenceSnapshotV1, _Mapping]] = ..., would_allow_actions: _Optional[_Iterable[_Union[ReleaseActionTypeV1, str]]] = ..., external_calls_made: _Optional[int] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class GetReleaseRequest(_message.Message):
    __slots__ = ("release_id",)
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    release_id: str
    def __init__(self, release_id: _Optional[str] = ...) -> None: ...

class GetReleaseResponse(_message.Message):
    __slots__ = ("release", "recent_actions", "recent_actions_capped", "stage_history", "stage_history_capped", "recent_activity", "recent_activity_capped", "activity_next_cursor", "validations", "integration", "last_known_good", "freshness", "recent_health_snapshots", "drift_posture", "verification_overrides")
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    RECENT_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    RECENT_ACTIONS_CAPPED_FIELD_NUMBER: _ClassVar[int]
    STAGE_HISTORY_FIELD_NUMBER: _ClassVar[int]
    STAGE_HISTORY_CAPPED_FIELD_NUMBER: _ClassVar[int]
    RECENT_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    RECENT_ACTIVITY_CAPPED_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    VALIDATIONS_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    LAST_KNOWN_GOOD_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    RECENT_HEALTH_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    DRIFT_POSTURE_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    release: ReleaseV1
    recent_actions: _containers.RepeatedCompositeFieldContainer[ReleaseActionV1]
    recent_actions_capped: bool
    stage_history: _containers.RepeatedCompositeFieldContainer[ReleaseStageHistoryEntryV1]
    stage_history_capped: bool
    recent_activity: _containers.RepeatedCompositeFieldContainer[ReleaseActivityEntryV1]
    recent_activity_capped: bool
    activity_next_cursor: str
    validations: _containers.RepeatedCompositeFieldContainer[ReleaseValidationV1]
    integration: ReleaseIntegrationV1
    last_known_good: ReleaseV1
    freshness: EvaluationFreshnessV1
    recent_health_snapshots: _containers.RepeatedCompositeFieldContainer[ReleaseHealthSnapshotV1]
    drift_posture: ReleaseDriftPostureV1
    verification_overrides: _containers.RepeatedCompositeFieldContainer[ReleaseVerificationOverrideV1]
    def __init__(self, release: _Optional[_Union[ReleaseV1, _Mapping]] = ..., recent_actions: _Optional[_Iterable[_Union[ReleaseActionV1, _Mapping]]] = ..., recent_actions_capped: _Optional[bool] = ..., stage_history: _Optional[_Iterable[_Union[ReleaseStageHistoryEntryV1, _Mapping]]] = ..., stage_history_capped: _Optional[bool] = ..., recent_activity: _Optional[_Iterable[_Union[ReleaseActivityEntryV1, _Mapping]]] = ..., recent_activity_capped: _Optional[bool] = ..., activity_next_cursor: _Optional[str] = ..., validations: _Optional[_Iterable[_Union[ReleaseValidationV1, _Mapping]]] = ..., integration: _Optional[_Union[ReleaseIntegrationV1, _Mapping]] = ..., last_known_good: _Optional[_Union[ReleaseV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., recent_health_snapshots: _Optional[_Iterable[_Union[ReleaseHealthSnapshotV1, _Mapping]]] = ..., drift_posture: _Optional[_Union[ReleaseDriftPostureV1, _Mapping]] = ..., verification_overrides: _Optional[_Iterable[_Union[ReleaseVerificationOverrideV1, _Mapping]]] = ...) -> None: ...

class ReleaseListFilterV1(_message.Message):
    __slots__ = ("integration_id", "stage", "environment", "release_key")
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    RELEASE_KEY_FIELD_NUMBER: _ClassVar[int]
    integration_id: str
    stage: ReleaseStageV1
    environment: str
    release_key: str
    def __init__(self, integration_id: _Optional[str] = ..., stage: _Optional[_Union[ReleaseStageV1, str]] = ..., environment: _Optional[str] = ..., release_key: _Optional[str] = ...) -> None: ...

class ListReleasesRequest(_message.Message):
    __slots__ = ("limit", "page_token", "filter")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    limit: int
    page_token: str
    filter: ReleaseListFilterV1
    def __init__(self, limit: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[_Union[ReleaseListFilterV1, _Mapping]] = ...) -> None: ...

class ListReleasesResponse(_message.Message):
    __slots__ = ("items", "next_page_token", "has_more", "effective_page_size", "external_calls_made", "freshness")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CALLS_MADE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ReleaseV1]
    next_page_token: str
    has_more: bool
    effective_page_size: int
    external_calls_made: int
    freshness: EvaluationFreshnessV1
    def __init__(self, items: _Optional[_Iterable[_Union[ReleaseV1, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., has_more: _Optional[bool] = ..., effective_page_size: _Optional[int] = ..., external_calls_made: _Optional[int] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class StartReleaseCanaryRequest(_message.Message):
    __slots__ = ("release_id", "idempotency_key", "reason", "reason_note", "verification_override")
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    REASON_NOTE_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    release_id: str
    idempotency_key: str
    reason: ReleaseActionReasonV1
    reason_note: str
    verification_override: ReleaseVerificationOverrideV1
    def __init__(self, release_id: _Optional[str] = ..., idempotency_key: _Optional[str] = ..., reason: _Optional[_Union[ReleaseActionReasonV1, str]] = ..., reason_note: _Optional[str] = ..., verification_override: _Optional[_Union[ReleaseVerificationOverrideV1, _Mapping]] = ...) -> None: ...

class StartReleaseCanaryResponse(_message.Message):
    __slots__ = ("action", "release", "idempotent_replay")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    action: ReleaseActionV1
    release: ReleaseV1
    idempotent_replay: bool
    def __init__(self, action: _Optional[_Union[ReleaseActionV1, _Mapping]] = ..., release: _Optional[_Union[ReleaseV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ...) -> None: ...

class PromoteReleaseRequest(_message.Message):
    __slots__ = ("release_id", "idempotency_key", "reason", "reason_note", "verification_override")
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    REASON_NOTE_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    release_id: str
    idempotency_key: str
    reason: ReleaseActionReasonV1
    reason_note: str
    verification_override: ReleaseVerificationOverrideV1
    def __init__(self, release_id: _Optional[str] = ..., idempotency_key: _Optional[str] = ..., reason: _Optional[_Union[ReleaseActionReasonV1, str]] = ..., reason_note: _Optional[str] = ..., verification_override: _Optional[_Union[ReleaseVerificationOverrideV1, _Mapping]] = ...) -> None: ...

class PromoteReleaseResponse(_message.Message):
    __slots__ = ("action", "release", "idempotent_replay")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    action: ReleaseActionV1
    release: ReleaseV1
    idempotent_replay: bool
    def __init__(self, action: _Optional[_Union[ReleaseActionV1, _Mapping]] = ..., release: _Optional[_Union[ReleaseV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ...) -> None: ...

class HoldReleaseRequest(_message.Message):
    __slots__ = ("release_id", "idempotency_key", "reason", "reason_note", "verification_override")
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    REASON_NOTE_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    release_id: str
    idempotency_key: str
    reason: ReleaseActionReasonV1
    reason_note: str
    verification_override: ReleaseVerificationOverrideV1
    def __init__(self, release_id: _Optional[str] = ..., idempotency_key: _Optional[str] = ..., reason: _Optional[_Union[ReleaseActionReasonV1, str]] = ..., reason_note: _Optional[str] = ..., verification_override: _Optional[_Union[ReleaseVerificationOverrideV1, _Mapping]] = ...) -> None: ...

class HoldReleaseResponse(_message.Message):
    __slots__ = ("action", "release", "idempotent_replay")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    action: ReleaseActionV1
    release: ReleaseV1
    idempotent_replay: bool
    def __init__(self, action: _Optional[_Union[ReleaseActionV1, _Mapping]] = ..., release: _Optional[_Union[ReleaseV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ...) -> None: ...

class AbortReleaseRequest(_message.Message):
    __slots__ = ("release_id", "idempotency_key", "reason", "reason_note", "verification_override")
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    REASON_NOTE_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    release_id: str
    idempotency_key: str
    reason: ReleaseActionReasonV1
    reason_note: str
    verification_override: ReleaseVerificationOverrideV1
    def __init__(self, release_id: _Optional[str] = ..., idempotency_key: _Optional[str] = ..., reason: _Optional[_Union[ReleaseActionReasonV1, str]] = ..., reason_note: _Optional[str] = ..., verification_override: _Optional[_Union[ReleaseVerificationOverrideV1, _Mapping]] = ...) -> None: ...

class AbortReleaseResponse(_message.Message):
    __slots__ = ("action", "release", "idempotent_replay")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    action: ReleaseActionV1
    release: ReleaseV1
    idempotent_replay: bool
    def __init__(self, action: _Optional[_Union[ReleaseActionV1, _Mapping]] = ..., release: _Optional[_Union[ReleaseV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ...) -> None: ...

class RollbackReleaseRequest(_message.Message):
    __slots__ = ("release_id", "idempotency_key", "reason", "reason_note", "verification_override")
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    REASON_NOTE_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    release_id: str
    idempotency_key: str
    reason: ReleaseActionReasonV1
    reason_note: str
    verification_override: ReleaseVerificationOverrideV1
    def __init__(self, release_id: _Optional[str] = ..., idempotency_key: _Optional[str] = ..., reason: _Optional[_Union[ReleaseActionReasonV1, str]] = ..., reason_note: _Optional[str] = ..., verification_override: _Optional[_Union[ReleaseVerificationOverrideV1, _Mapping]] = ...) -> None: ...

class RollbackReleaseResponse(_message.Message):
    __slots__ = ("action", "release", "idempotent_replay", "rollback_target_release_id", "rollback_target_verdict")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    ROLLBACK_TARGET_RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    ROLLBACK_TARGET_VERDICT_FIELD_NUMBER: _ClassVar[int]
    action: ReleaseActionV1
    release: ReleaseV1
    idempotent_replay: bool
    rollback_target_release_id: str
    rollback_target_verdict: ReleaseValidationV1
    def __init__(self, action: _Optional[_Union[ReleaseActionV1, _Mapping]] = ..., release: _Optional[_Union[ReleaseV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ..., rollback_target_release_id: _Optional[str] = ..., rollback_target_verdict: _Optional[_Union[ReleaseValidationV1, _Mapping]] = ...) -> None: ...

class GetReleaseActionRequest(_message.Message):
    __slots__ = ("action_id",)
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    action_id: str
    def __init__(self, action_id: _Optional[str] = ...) -> None: ...

class GetReleaseActionResponse(_message.Message):
    __slots__ = ("action", "release", "observations", "observations_next_cursor")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    OBSERVATIONS_FIELD_NUMBER: _ClassVar[int]
    OBSERVATIONS_NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    action: ReleaseActionV1
    release: ReleaseV1
    observations: _containers.RepeatedCompositeFieldContainer[ReleaseObservationV1]
    observations_next_cursor: str
    def __init__(self, action: _Optional[_Union[ReleaseActionV1, _Mapping]] = ..., release: _Optional[_Union[ReleaseV1, _Mapping]] = ..., observations: _Optional[_Iterable[_Union[ReleaseObservationV1, _Mapping]]] = ..., observations_next_cursor: _Optional[str] = ...) -> None: ...

class ReleaseActionListFilterV1(_message.Message):
    __slots__ = ("release_id", "action_type", "state")
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    release_id: str
    action_type: ReleaseActionTypeV1
    state: ReleaseActionStateV1
    def __init__(self, release_id: _Optional[str] = ..., action_type: _Optional[_Union[ReleaseActionTypeV1, str]] = ..., state: _Optional[_Union[ReleaseActionStateV1, str]] = ...) -> None: ...

class ListReleaseActionsRequest(_message.Message):
    __slots__ = ("limit", "page_token", "filter")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    limit: int
    page_token: str
    filter: ReleaseActionListFilterV1
    def __init__(self, limit: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[_Union[ReleaseActionListFilterV1, _Mapping]] = ...) -> None: ...

class ListReleaseActionsResponse(_message.Message):
    __slots__ = ("items", "next_page_token", "has_more", "effective_page_size", "freshness")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ReleaseActionV1]
    next_page_token: str
    has_more: bool
    effective_page_size: int
    freshness: EvaluationFreshnessV1
    def __init__(self, items: _Optional[_Iterable[_Union[ReleaseActionV1, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., has_more: _Optional[bool] = ..., effective_page_size: _Optional[int] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class ReleaseHealthConditionV1(_message.Message):
    __slots__ = ("condition_key", "availability", "observed_value", "threshold_value", "failing", "reason_code")
    CONDITION_KEY_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_VALUE_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_VALUE_FIELD_NUMBER: _ClassVar[int]
    FAILING_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    condition_key: str
    availability: MetricAvailabilityV1
    observed_value: float
    threshold_value: float
    failing: bool
    reason_code: str
    def __init__(self, condition_key: _Optional[str] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., observed_value: _Optional[float] = ..., threshold_value: _Optional[float] = ..., failing: _Optional[bool] = ..., reason_code: _Optional[str] = ...) -> None: ...

class ReleaseHealthSnapshotV1(_message.Message):
    __slots__ = ("snapshot_id", "release_id", "stage", "window_start", "window_end", "sample_size", "minimum_sample_met", "conditions", "failing_condition_count", "triggering_condition_keys", "preventing_condition_keys", "automatic_action_id", "observed_at", "decision_code", "last_known_good_posture", "last_known_good_reason_code", "automatic_rollback_enabled", "required_failing_condition_count")
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    WINDOW_START_FIELD_NUMBER: _ClassVar[int]
    WINDOW_END_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_SIZE_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_SAMPLE_MET_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    FAILING_CONDITION_COUNT_FIELD_NUMBER: _ClassVar[int]
    TRIGGERING_CONDITION_KEYS_FIELD_NUMBER: _ClassVar[int]
    PREVENTING_CONDITION_KEYS_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    DECISION_CODE_FIELD_NUMBER: _ClassVar[int]
    LAST_KNOWN_GOOD_POSTURE_FIELD_NUMBER: _ClassVar[int]
    LAST_KNOWN_GOOD_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_ROLLBACK_ENABLED_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FAILING_CONDITION_COUNT_FIELD_NUMBER: _ClassVar[int]
    snapshot_id: str
    release_id: str
    stage: ReleaseStageV1
    window_start: _timestamp_pb2.Timestamp
    window_end: _timestamp_pb2.Timestamp
    sample_size: int
    minimum_sample_met: bool
    conditions: _containers.RepeatedCompositeFieldContainer[ReleaseHealthConditionV1]
    failing_condition_count: int
    triggering_condition_keys: _containers.RepeatedScalarFieldContainer[str]
    preventing_condition_keys: _containers.RepeatedScalarFieldContainer[str]
    automatic_action_id: str
    observed_at: _timestamp_pb2.Timestamp
    decision_code: str
    last_known_good_posture: str
    last_known_good_reason_code: str
    automatic_rollback_enabled: bool
    required_failing_condition_count: int
    def __init__(self, snapshot_id: _Optional[str] = ..., release_id: _Optional[str] = ..., stage: _Optional[_Union[ReleaseStageV1, str]] = ..., window_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., window_end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., sample_size: _Optional[int] = ..., minimum_sample_met: _Optional[bool] = ..., conditions: _Optional[_Iterable[_Union[ReleaseHealthConditionV1, _Mapping]]] = ..., failing_condition_count: _Optional[int] = ..., triggering_condition_keys: _Optional[_Iterable[str]] = ..., preventing_condition_keys: _Optional[_Iterable[str]] = ..., automatic_action_id: _Optional[str] = ..., observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., decision_code: _Optional[str] = ..., last_known_good_posture: _Optional[str] = ..., last_known_good_reason_code: _Optional[str] = ..., automatic_rollback_enabled: _Optional[bool] = ..., required_failing_condition_count: _Optional[int] = ...) -> None: ...

class ReleaseDriftPostureV1(_message.Message):
    __slots__ = ("drift_detected", "drift_reason_code", "externally_observed_stage", "external_state_label", "detected_at", "availability", "drift_materiality", "drift_observation_id")
    DRIFT_DETECTED_FIELD_NUMBER: _ClassVar[int]
    DRIFT_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    EXTERNALLY_OBSERVED_STAGE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_STATE_LABEL_FIELD_NUMBER: _ClassVar[int]
    DETECTED_AT_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    DRIFT_MATERIALITY_FIELD_NUMBER: _ClassVar[int]
    DRIFT_OBSERVATION_ID_FIELD_NUMBER: _ClassVar[int]
    drift_detected: bool
    drift_reason_code: str
    externally_observed_stage: ReleaseStageV1
    external_state_label: str
    detected_at: _timestamp_pb2.Timestamp
    availability: MetricAvailabilityV1
    drift_materiality: str
    drift_observation_id: str
    def __init__(self, drift_detected: _Optional[bool] = ..., drift_reason_code: _Optional[str] = ..., externally_observed_stage: _Optional[_Union[ReleaseStageV1, str]] = ..., external_state_label: _Optional[str] = ..., detected_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., drift_materiality: _Optional[str] = ..., drift_observation_id: _Optional[str] = ...) -> None: ...

class ReleaseObservationV1(_message.Message):
    __slots__ = ("observation_id", "action_id", "source", "external_event_id", "provider_sequence", "provider_observed_at", "reported_action_state", "reported_stage", "applied", "not_applied_reason_code", "received_at", "disposition", "drift_materiality", "correlation_confidence")
    OBSERVATION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    REPORTED_ACTION_STATE_FIELD_NUMBER: _ClassVar[int]
    REPORTED_STAGE_FIELD_NUMBER: _ClassVar[int]
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    NOT_APPLIED_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    DRIFT_MATERIALITY_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    observation_id: str
    action_id: str
    source: str
    external_event_id: str
    provider_sequence: int
    provider_observed_at: _timestamp_pb2.Timestamp
    reported_action_state: ReleaseActionStateV1
    reported_stage: ReleaseStageV1
    applied: bool
    not_applied_reason_code: str
    received_at: _timestamp_pb2.Timestamp
    disposition: str
    drift_materiality: str
    correlation_confidence: ReleaseObservationConfidenceV1
    def __init__(self, observation_id: _Optional[str] = ..., action_id: _Optional[str] = ..., source: _Optional[str] = ..., external_event_id: _Optional[str] = ..., provider_sequence: _Optional[int] = ..., provider_observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., reported_action_state: _Optional[_Union[ReleaseActionStateV1, str]] = ..., reported_stage: _Optional[_Union[ReleaseStageV1, str]] = ..., applied: _Optional[bool] = ..., not_applied_reason_code: _Optional[str] = ..., received_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., disposition: _Optional[str] = ..., drift_materiality: _Optional[str] = ..., correlation_confidence: _Optional[_Union[ReleaseObservationConfidenceV1, str]] = ...) -> None: ...

class ProductionRuleActionTargetV1(_message.Message):
    __slots__ = ("dataset_draft", "review", "linked_evaluation", "notify")
    DATASET_DRAFT_FIELD_NUMBER: _ClassVar[int]
    REVIEW_FIELD_NUMBER: _ClassVar[int]
    LINKED_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_FIELD_NUMBER: _ClassVar[int]
    dataset_draft: ProductionRuleDatasetDraftTargetV1
    review: ProductionRuleReviewTargetV1
    linked_evaluation: ProductionRuleLinkedEvaluationTargetV1
    notify: ProductionRuleNotifyTargetV1
    def __init__(self, dataset_draft: _Optional[_Union[ProductionRuleDatasetDraftTargetV1, _Mapping]] = ..., review: _Optional[_Union[ProductionRuleReviewTargetV1, _Mapping]] = ..., linked_evaluation: _Optional[_Union[ProductionRuleLinkedEvaluationTargetV1, _Mapping]] = ..., notify: _Optional[_Union[ProductionRuleNotifyTargetV1, _Mapping]] = ...) -> None: ...

class ProductionRuleDatasetDraftTargetV1(_message.Message):
    __slots__ = ("dataset_collection_id", "field_mappings", "recorded_output_field_path")
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    RECORDED_OUTPUT_FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
    dataset_collection_id: str
    field_mappings: _containers.RepeatedCompositeFieldContainer[DatasetFieldMappingV1]
    recorded_output_field_path: str
    def __init__(self, dataset_collection_id: _Optional[str] = ..., field_mappings: _Optional[_Iterable[_Union[DatasetFieldMappingV1, _Mapping]]] = ..., recorded_output_field_path: _Optional[str] = ...) -> None: ...

class ProductionRuleReviewTargetV1(_message.Message):
    __slots__ = ("reviewer_principal_id",)
    REVIEWER_PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    reviewer_principal_id: str
    def __init__(self, reviewer_principal_id: _Optional[str] = ...) -> None: ...

class ProductionRuleLinkedEvaluationTargetV1(_message.Message):
    __slots__ = ("evaluation_definition_id", "evaluation_definition_revision_id")
    EVALUATION_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_DEFINITION_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    evaluation_definition_id: str
    evaluation_definition_revision_id: str
    def __init__(self, evaluation_definition_id: _Optional[str] = ..., evaluation_definition_revision_id: _Optional[str] = ...) -> None: ...

class ProductionRuleNotifyTargetV1(_message.Message):
    __slots__ = ("alert_destination_id",)
    ALERT_DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    alert_destination_id: str
    def __init__(self, alert_destination_id: _Optional[str] = ...) -> None: ...

class DatasetRedactionOutcomeV1(_message.Message):
    __slots__ = ("target_path", "outcome", "detector_kinds", "match_count", "reason_code")
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_KINDS_FIELD_NUMBER: _ClassVar[int]
    MATCH_COUNT_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    target_path: str
    outcome: DatasetRedactionOutcomeKindV1
    detector_kinds: _containers.RepeatedScalarFieldContainer[DatasetRedactionDetectorKindV1]
    match_count: int
    reason_code: str
    def __init__(self, target_path: _Optional[str] = ..., outcome: _Optional[_Union[DatasetRedactionOutcomeKindV1, str]] = ..., detector_kinds: _Optional[_Iterable[_Union[DatasetRedactionDetectorKindV1, str]]] = ..., match_count: _Optional[int] = ..., reason_code: _Optional[str] = ...) -> None: ...

class DatasetRedactionSectionV1(_message.Message):
    __slots__ = ("policy_id", "policy_version", "method_name", "method_version", "outcomes", "verdict", "blocks_draft_creation", "max_scan_bytes", "availability")
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    METHOD_VERSION_FIELD_NUMBER: _ClassVar[int]
    OUTCOMES_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    BLOCKS_DRAFT_CREATION_FIELD_NUMBER: _ClassVar[int]
    MAX_SCAN_BYTES_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    policy_id: str
    policy_version: int
    method_name: str
    method_version: str
    outcomes: _containers.RepeatedCompositeFieldContainer[DatasetRedactionOutcomeV1]
    verdict: DatasetRedactionOutcomeKindV1
    blocks_draft_creation: bool
    max_scan_bytes: int
    availability: MetricAvailabilityV1
    def __init__(self, policy_id: _Optional[str] = ..., policy_version: _Optional[int] = ..., method_name: _Optional[str] = ..., method_version: _Optional[str] = ..., outcomes: _Optional[_Iterable[_Union[DatasetRedactionOutcomeV1, _Mapping]]] = ..., verdict: _Optional[_Union[DatasetRedactionOutcomeKindV1, str]] = ..., blocks_draft_creation: _Optional[bool] = ..., max_scan_bytes: _Optional[int] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class DatasetDuplicationCandidateV1(_message.Message):
    __slots__ = ("subject_id", "subject_kind", "verdict", "similarity", "hamming_distance", "expected_output_conflicts", "dataset_version_id")
    SUBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_KIND_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    SIMILARITY_FIELD_NUMBER: _ClassVar[int]
    HAMMING_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUT_CONFLICTS_FIELD_NUMBER: _ClassVar[int]
    DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    subject_id: str
    subject_kind: DatasetDedupeSubjectKindV1
    verdict: DatasetDuplicationVerdictV1
    similarity: float
    hamming_distance: int
    expected_output_conflicts: bool
    dataset_version_id: str
    def __init__(self, subject_id: _Optional[str] = ..., subject_kind: _Optional[_Union[DatasetDedupeSubjectKindV1, str]] = ..., verdict: _Optional[_Union[DatasetDuplicationVerdictV1, str]] = ..., similarity: _Optional[float] = ..., hamming_distance: _Optional[int] = ..., expected_output_conflicts: _Optional[bool] = ..., dataset_version_id: _Optional[str] = ...) -> None: ...

class DatasetDuplicationSectionV1(_message.Message):
    __slots__ = ("verdict", "input_fingerprint", "expected_fingerprint", "method_name", "method_version", "near_method_name", "near_duplicate_max_hamming", "simhash_bands", "candidates", "truncated_candidate_count", "indexed_subject_count", "version_case_count", "permits_publish", "caveat_code", "max_candidates_returned", "max_candidates_scanned", "availability")
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    INPUT_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    METHOD_VERSION_FIELD_NUMBER: _ClassVar[int]
    NEAR_METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    NEAR_DUPLICATE_MAX_HAMMING_FIELD_NUMBER: _ClassVar[int]
    SIMHASH_BANDS_FIELD_NUMBER: _ClassVar[int]
    CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_CANDIDATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    INDEXED_SUBJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
    VERSION_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PERMITS_PUBLISH_FIELD_NUMBER: _ClassVar[int]
    CAVEAT_CODE_FIELD_NUMBER: _ClassVar[int]
    MAX_CANDIDATES_RETURNED_FIELD_NUMBER: _ClassVar[int]
    MAX_CANDIDATES_SCANNED_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    verdict: DatasetDuplicationVerdictV1
    input_fingerprint: str
    expected_fingerprint: str
    method_name: str
    method_version: str
    near_method_name: str
    near_duplicate_max_hamming: int
    simhash_bands: int
    candidates: _containers.RepeatedCompositeFieldContainer[DatasetDuplicationCandidateV1]
    truncated_candidate_count: int
    indexed_subject_count: int
    version_case_count: int
    permits_publish: bool
    caveat_code: str
    max_candidates_returned: int
    max_candidates_scanned: int
    availability: MetricAvailabilityV1
    def __init__(self, verdict: _Optional[_Union[DatasetDuplicationVerdictV1, str]] = ..., input_fingerprint: _Optional[str] = ..., expected_fingerprint: _Optional[str] = ..., method_name: _Optional[str] = ..., method_version: _Optional[str] = ..., near_method_name: _Optional[str] = ..., near_duplicate_max_hamming: _Optional[int] = ..., simhash_bands: _Optional[int] = ..., candidates: _Optional[_Iterable[_Union[DatasetDuplicationCandidateV1, _Mapping]]] = ..., truncated_candidate_count: _Optional[int] = ..., indexed_subject_count: _Optional[int] = ..., version_case_count: _Optional[int] = ..., permits_publish: _Optional[bool] = ..., caveat_code: _Optional[str] = ..., max_candidates_returned: _Optional[int] = ..., max_candidates_scanned: _Optional[int] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class DedupeResolutionV1(_message.Message):
    __slots__ = ("proposed_case_id", "resolution", "matched_case_revision_id", "method_name", "method_version", "similarity", "threshold_in_force", "resolved_by_user_id", "audited_override_reason", "resolved_at")
    PROPOSED_CASE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    MATCHED_CASE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    METHOD_VERSION_FIELD_NUMBER: _ClassVar[int]
    SIMILARITY_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_IN_FORCE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    AUDITED_OVERRIDE_REASON_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_AT_FIELD_NUMBER: _ClassVar[int]
    proposed_case_id: str
    resolution: DatasetDedupeResolutionKindV1
    matched_case_revision_id: str
    method_name: str
    method_version: str
    similarity: float
    threshold_in_force: int
    resolved_by_user_id: str
    audited_override_reason: str
    resolved_at: _timestamp_pb2.Timestamp
    def __init__(self, proposed_case_id: _Optional[str] = ..., resolution: _Optional[_Union[DatasetDedupeResolutionKindV1, str]] = ..., matched_case_revision_id: _Optional[str] = ..., method_name: _Optional[str] = ..., method_version: _Optional[str] = ..., similarity: _Optional[float] = ..., threshold_in_force: _Optional[int] = ..., resolved_by_user_id: _Optional[str] = ..., audited_override_reason: _Optional[str] = ..., resolved_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DatasetLeakageSourceSignalV1(_message.Message):
    __slots__ = ("source", "verdict", "matched_count", "denominator", "affected_case_ids", "method_name", "method_version", "false_positive_rate", "caveat_code", "availability")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    MATCHED_COUNT_FIELD_NUMBER: _ClassVar[int]
    DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_CASE_IDS_FIELD_NUMBER: _ClassVar[int]
    METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    METHOD_VERSION_FIELD_NUMBER: _ClassVar[int]
    FALSE_POSITIVE_RATE_FIELD_NUMBER: _ClassVar[int]
    CAVEAT_CODE_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    source: DatasetLeakageSourceKindV1
    verdict: DatasetLeakageVerdictV1
    matched_count: int
    denominator: int
    affected_case_ids: _containers.RepeatedScalarFieldContainer[str]
    method_name: str
    method_version: str
    false_positive_rate: float
    caveat_code: str
    availability: MetricAvailabilityV1
    def __init__(self, source: _Optional[_Union[DatasetLeakageSourceKindV1, str]] = ..., verdict: _Optional[_Union[DatasetLeakageVerdictV1, str]] = ..., matched_count: _Optional[int] = ..., denominator: _Optional[int] = ..., affected_case_ids: _Optional[_Iterable[str]] = ..., method_name: _Optional[str] = ..., method_version: _Optional[str] = ..., false_positive_rate: _Optional[float] = ..., caveat_code: _Optional[str] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class DatasetLeakageSectionV1(_message.Message):
    __slots__ = ("sources", "verdict", "max_sources_scanned", "availability")
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    MAX_SOURCES_SCANNED_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    sources: _containers.RepeatedCompositeFieldContainer[DatasetLeakageSourceSignalV1]
    verdict: DatasetLeakageVerdictV1
    max_sources_scanned: int
    availability: MetricAvailabilityV1
    def __init__(self, sources: _Optional[_Iterable[_Union[DatasetLeakageSourceSignalV1, _Mapping]]] = ..., verdict: _Optional[_Union[DatasetLeakageVerdictV1, str]] = ..., max_sources_scanned: _Optional[int] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class DatasetSliceObservationV1(_message.Message):
    __slots__ = ("dimension_key", "slice_value", "flag", "dataset_count", "dataset_denominator", "dataset_share", "production_availability", "availability")
    DIMENSION_KEY_FIELD_NUMBER: _ClassVar[int]
    SLICE_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    DATASET_COUNT_FIELD_NUMBER: _ClassVar[int]
    DATASET_DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    DATASET_SHARE_FIELD_NUMBER: _ClassVar[int]
    PRODUCTION_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    dimension_key: str
    slice_value: str
    flag: DatasetSliceFlagV1
    dataset_count: int
    dataset_denominator: int
    dataset_share: float
    production_availability: MetricAvailabilityV1
    availability: MetricAvailabilityV1
    def __init__(self, dimension_key: _Optional[str] = ..., slice_value: _Optional[str] = ..., flag: _Optional[_Union[DatasetSliceFlagV1, str]] = ..., dataset_count: _Optional[int] = ..., dataset_denominator: _Optional[int] = ..., dataset_share: _Optional[float] = ..., production_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class DatasetSliceSectionV1(_message.Message):
    __slots__ = ("dimension_source", "schema_revision_id", "schema_fingerprint", "observations", "truncated_slice_value_count", "slice_policy_version", "underrepresented_below", "overrepresented_above", "max_slice_values_per_dimension", "availability")
    DIMENSION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    OBSERVATIONS_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_SLICE_VALUE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SLICE_POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    UNDERREPRESENTED_BELOW_FIELD_NUMBER: _ClassVar[int]
    OVERREPRESENTED_ABOVE_FIELD_NUMBER: _ClassVar[int]
    MAX_SLICE_VALUES_PER_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    dimension_source: DatasetSliceDimensionSourceV1
    schema_revision_id: str
    schema_fingerprint: str
    observations: _containers.RepeatedCompositeFieldContainer[DatasetSliceObservationV1]
    truncated_slice_value_count: int
    slice_policy_version: int
    underrepresented_below: float
    overrepresented_above: float
    max_slice_values_per_dimension: int
    availability: MetricAvailabilityV1
    def __init__(self, dimension_source: _Optional[_Union[DatasetSliceDimensionSourceV1, str]] = ..., schema_revision_id: _Optional[str] = ..., schema_fingerprint: _Optional[str] = ..., observations: _Optional[_Iterable[_Union[DatasetSliceObservationV1, _Mapping]]] = ..., truncated_slice_value_count: _Optional[int] = ..., slice_policy_version: _Optional[int] = ..., underrepresented_below: _Optional[float] = ..., overrepresented_above: _Optional[float] = ..., max_slice_values_per_dimension: _Optional[int] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class DatasetCaseQualitySignalsV1(_message.Message):
    __slots__ = ("redaction", "duplication", "leakage", "slices")
    REDACTION_FIELD_NUMBER: _ClassVar[int]
    DUPLICATION_FIELD_NUMBER: _ClassVar[int]
    LEAKAGE_FIELD_NUMBER: _ClassVar[int]
    SLICES_FIELD_NUMBER: _ClassVar[int]
    redaction: DatasetRedactionSectionV1
    duplication: DatasetDuplicationSectionV1
    leakage: DatasetLeakageSectionV1
    slices: DatasetSliceSectionV1
    def __init__(self, redaction: _Optional[_Union[DatasetRedactionSectionV1, _Mapping]] = ..., duplication: _Optional[_Union[DatasetDuplicationSectionV1, _Mapping]] = ..., leakage: _Optional[_Union[DatasetLeakageSectionV1, _Mapping]] = ..., slices: _Optional[_Union[DatasetSliceSectionV1, _Mapping]] = ...) -> None: ...

class ChangesetQualitySignalsV1(_message.Message):
    __slots__ = ("redaction", "duplication", "leakage", "slices", "case_count", "conflicted_case_count", "blocked_case_count", "duplicate_case_count", "findings", "permits_publish")
    REDACTION_FIELD_NUMBER: _ClassVar[int]
    DUPLICATION_FIELD_NUMBER: _ClassVar[int]
    LEAKAGE_FIELD_NUMBER: _ClassVar[int]
    SLICES_FIELD_NUMBER: _ClassVar[int]
    CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONFLICTED_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    DUPLICATE_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FINDINGS_FIELD_NUMBER: _ClassVar[int]
    PERMITS_PUBLISH_FIELD_NUMBER: _ClassVar[int]
    redaction: DatasetRedactionSectionV1
    duplication: DatasetDuplicationSectionV1
    leakage: DatasetLeakageSectionV1
    slices: DatasetSliceSectionV1
    case_count: int
    conflicted_case_count: int
    blocked_case_count: int
    duplicate_case_count: int
    findings: _containers.RepeatedCompositeFieldContainer[DataQualityFindingV1]
    permits_publish: bool
    def __init__(self, redaction: _Optional[_Union[DatasetRedactionSectionV1, _Mapping]] = ..., duplication: _Optional[_Union[DatasetDuplicationSectionV1, _Mapping]] = ..., leakage: _Optional[_Union[DatasetLeakageSectionV1, _Mapping]] = ..., slices: _Optional[_Union[DatasetSliceSectionV1, _Mapping]] = ..., case_count: _Optional[int] = ..., conflicted_case_count: _Optional[int] = ..., blocked_case_count: _Optional[int] = ..., duplicate_case_count: _Optional[int] = ..., findings: _Optional[_Iterable[_Union[DataQualityFindingV1, _Mapping]]] = ..., permits_publish: _Optional[bool] = ...) -> None: ...

class DatasetSchemaFieldV1(_message.Message):
    __slots__ = ("path", "value_kind", "required", "display_name")
    PATH_FIELD_NUMBER: _ClassVar[int]
    VALUE_KIND_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    path: str
    value_kind: DatasetSchemaValueKindV1
    required: bool
    display_name: str
    def __init__(self, path: _Optional[str] = ..., value_kind: _Optional[_Union[DatasetSchemaValueKindV1, str]] = ..., required: _Optional[bool] = ..., display_name: _Optional[str] = ...) -> None: ...

class DatasetSliceDimensionV1(_message.Message):
    __slots__ = ("dimension_key", "display_name", "value_kind", "source_metadata_key", "filterable", "required", "allowed_values")
    DIMENSION_KEY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_KIND_FIELD_NUMBER: _ClassVar[int]
    SOURCE_METADATA_KEY_FIELD_NUMBER: _ClassVar[int]
    FILTERABLE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_VALUES_FIELD_NUMBER: _ClassVar[int]
    dimension_key: str
    display_name: str
    value_kind: DatasetSchemaValueKindV1
    source_metadata_key: str
    filterable: bool
    required: bool
    allowed_values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, dimension_key: _Optional[str] = ..., display_name: _Optional[str] = ..., value_kind: _Optional[_Union[DatasetSchemaValueKindV1, str]] = ..., source_metadata_key: _Optional[str] = ..., filterable: _Optional[bool] = ..., required: _Optional[bool] = ..., allowed_values: _Optional[_Iterable[str]] = ...) -> None: ...

class DatasetSchemaMetadataKeyV1(_message.Message):
    __slots__ = ("key", "value_kind", "required")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_KIND_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    key: str
    value_kind: DatasetSchemaValueKindV1
    required: bool
    def __init__(self, key: _Optional[str] = ..., value_kind: _Optional[_Union[DatasetSchemaValueKindV1, str]] = ..., required: _Optional[bool] = ...) -> None: ...

class DatasetSchemaMappingRuleV1(_message.Message):
    __slots__ = ("target_path", "source_selector")
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    target_path: str
    source_selector: str
    def __init__(self, target_path: _Optional[str] = ..., source_selector: _Optional[str] = ...) -> None: ...

class DatasetSchemaShapeV1(_message.Message):
    __slots__ = ("compatibility_policy", "input_fields", "expected_output_fields", "slice_dimensions", "metadata_keys", "mapping_rules", "display_name", "description")
    COMPATIBILITY_POLICY_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELDS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUT_FIELDS_FIELD_NUMBER: _ClassVar[int]
    SLICE_DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    METADATA_KEYS_FIELD_NUMBER: _ClassVar[int]
    MAPPING_RULES_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    compatibility_policy: DatasetSchemaCompatibilityPolicyV1
    input_fields: _containers.RepeatedCompositeFieldContainer[DatasetSchemaFieldV1]
    expected_output_fields: _containers.RepeatedCompositeFieldContainer[DatasetSchemaFieldV1]
    slice_dimensions: _containers.RepeatedCompositeFieldContainer[DatasetSliceDimensionV1]
    metadata_keys: _containers.RepeatedCompositeFieldContainer[DatasetSchemaMetadataKeyV1]
    mapping_rules: _containers.RepeatedCompositeFieldContainer[DatasetSchemaMappingRuleV1]
    display_name: str
    description: str
    def __init__(self, compatibility_policy: _Optional[_Union[DatasetSchemaCompatibilityPolicyV1, str]] = ..., input_fields: _Optional[_Iterable[_Union[DatasetSchemaFieldV1, _Mapping]]] = ..., expected_output_fields: _Optional[_Iterable[_Union[DatasetSchemaFieldV1, _Mapping]]] = ..., slice_dimensions: _Optional[_Iterable[_Union[DatasetSliceDimensionV1, _Mapping]]] = ..., metadata_keys: _Optional[_Iterable[_Union[DatasetSchemaMetadataKeyV1, _Mapping]]] = ..., mapping_rules: _Optional[_Iterable[_Union[DatasetSchemaMappingRuleV1, _Mapping]]] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class DatasetSchemaRevisionV1(_message.Message):
    __slots__ = ("schema_revision_id", "dataset_collection_id", "revision_number", "schema_fingerprint", "fingerprint_algorithm", "shape", "is_active", "created_at")
    SCHEMA_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    FINGERPRINT_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    schema_revision_id: str
    dataset_collection_id: str
    revision_number: int
    schema_fingerprint: str
    fingerprint_algorithm: str
    shape: DatasetSchemaShapeV1
    is_active: bool
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, schema_revision_id: _Optional[str] = ..., dataset_collection_id: _Optional[str] = ..., revision_number: _Optional[int] = ..., schema_fingerprint: _Optional[str] = ..., fingerprint_algorithm: _Optional[str] = ..., shape: _Optional[_Union[DatasetSchemaShapeV1, _Mapping]] = ..., is_active: _Optional[bool] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DatasetSchemaChangeV1(_message.Message):
    __slots__ = ("kind", "path", "from_value_kind", "to_value_kind", "removed_values")
    KIND_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    FROM_VALUE_KIND_FIELD_NUMBER: _ClassVar[int]
    TO_VALUE_KIND_FIELD_NUMBER: _ClassVar[int]
    REMOVED_VALUES_FIELD_NUMBER: _ClassVar[int]
    kind: DatasetSchemaChangeKindV1
    path: str
    from_value_kind: DatasetSchemaValueKindV1
    to_value_kind: DatasetSchemaValueKindV1
    removed_values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, kind: _Optional[_Union[DatasetSchemaChangeKindV1, str]] = ..., path: _Optional[str] = ..., from_value_kind: _Optional[_Union[DatasetSchemaValueKindV1, str]] = ..., to_value_kind: _Optional[_Union[DatasetSchemaValueKindV1, str]] = ..., removed_values: _Optional[_Iterable[str]] = ...) -> None: ...

class DatasetSchemaCompatibilityVerdictV1(_message.Message):
    __slots__ = ("verdict", "policy_applied", "base_schema_revision_id", "target_schema_revision_id", "base_schema_fingerprint", "target_schema_fingerprint", "changes", "blocking_reason_codes")
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    POLICY_APPLIED_FIELD_NUMBER: _ClassVar[int]
    BASE_SCHEMA_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_SCHEMA_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_SCHEMA_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    TARGET_SCHEMA_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    BLOCKING_REASON_CODES_FIELD_NUMBER: _ClassVar[int]
    verdict: DatasetSchemaCompatibilityVerdictKindV1
    policy_applied: DatasetSchemaCompatibilityPolicyV1
    base_schema_revision_id: str
    target_schema_revision_id: str
    base_schema_fingerprint: str
    target_schema_fingerprint: str
    changes: _containers.RepeatedCompositeFieldContainer[DatasetSchemaChangeV1]
    blocking_reason_codes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, verdict: _Optional[_Union[DatasetSchemaCompatibilityVerdictKindV1, str]] = ..., policy_applied: _Optional[_Union[DatasetSchemaCompatibilityPolicyV1, str]] = ..., base_schema_revision_id: _Optional[str] = ..., target_schema_revision_id: _Optional[str] = ..., base_schema_fingerprint: _Optional[str] = ..., target_schema_fingerprint: _Optional[str] = ..., changes: _Optional[_Iterable[_Union[DatasetSchemaChangeV1, _Mapping]]] = ..., blocking_reason_codes: _Optional[_Iterable[str]] = ...) -> None: ...

class DatasetCaseRecentPerformanceV1(_message.Message):
    __slots__ = ("availability", "runs_observed", "latest_run_id", "latest_run_at", "latest_score", "previous_score", "latest_result", "regression", "freshness")
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    RUNS_OBSERVED_FIELD_NUMBER: _ClassVar[int]
    LATEST_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    LATEST_RUN_AT_FIELD_NUMBER: _ClassVar[int]
    LATEST_SCORE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_SCORE_FIELD_NUMBER: _ClassVar[int]
    LATEST_RESULT_FIELD_NUMBER: _ClassVar[int]
    REGRESSION_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    availability: MetricAvailabilityV1
    runs_observed: int
    latest_run_id: str
    latest_run_at: _timestamp_pb2.Timestamp
    latest_score: float
    previous_score: float
    latest_result: DatasetCaseResultPostureV1
    regression: DatasetCaseRegressionPostureV1
    freshness: EvaluationFreshnessV1
    def __init__(self, availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., runs_observed: _Optional[int] = ..., latest_run_id: _Optional[str] = ..., latest_run_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., latest_score: _Optional[float] = ..., previous_score: _Optional[float] = ..., latest_result: _Optional[_Union[DatasetCaseResultPostureV1, str]] = ..., regression: _Optional[_Union[DatasetCaseRegressionPostureV1, str]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class DatasetCaseContentRefV1(_message.Message):
    __slots__ = ("content_class", "storage_uri", "byte_size", "availability")
    CONTENT_CLASS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_URI_FIELD_NUMBER: _ClassVar[int]
    BYTE_SIZE_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    content_class: str
    storage_uri: str
    byte_size: int
    availability: MetricAvailabilityV1
    def __init__(self, content_class: _Optional[str] = ..., storage_uri: _Optional[str] = ..., byte_size: _Optional[int] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class DatasetCaseLineageV1(_message.Message):
    __slots__ = ("anchor_kind", "anchor_availability", "anchor_reason_code", "source_proposed_case_id", "source_draft_id", "content_refs", "anchor_trace_id", "anchor_span_id", "anchor_evaluation_run_id", "anchor_rule_version_id", "anchor_workflow_step_id")
    ANCHOR_KIND_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROPOSED_CASE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DRAFT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_REFS_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_RULE_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_WORKFLOW_STEP_ID_FIELD_NUMBER: _ClassVar[int]
    anchor_kind: DatasetCaseLineageAnchorKindV1
    anchor_availability: DatasetLineageAnchorAvailabilityV1
    anchor_reason_code: str
    source_proposed_case_id: str
    source_draft_id: str
    content_refs: _containers.RepeatedCompositeFieldContainer[DatasetCaseContentRefV1]
    anchor_trace_id: str
    anchor_span_id: str
    anchor_evaluation_run_id: str
    anchor_rule_version_id: str
    anchor_workflow_step_id: str
    def __init__(self, anchor_kind: _Optional[_Union[DatasetCaseLineageAnchorKindV1, str]] = ..., anchor_availability: _Optional[_Union[DatasetLineageAnchorAvailabilityV1, str]] = ..., anchor_reason_code: _Optional[str] = ..., source_proposed_case_id: _Optional[str] = ..., source_draft_id: _Optional[str] = ..., content_refs: _Optional[_Iterable[_Union[DatasetCaseContentRefV1, _Mapping]]] = ..., anchor_trace_id: _Optional[str] = ..., anchor_span_id: _Optional[str] = ..., anchor_evaluation_run_id: _Optional[str] = ..., anchor_rule_version_id: _Optional[str] = ..., anchor_workflow_step_id: _Optional[str] = ...) -> None: ...

class DatasetCaseArtifactSourceCoverageV1(_message.Message):
    __slots__ = ("source_kind", "availability")
    SOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    source_kind: str
    availability: MetricAvailabilityV1
    def __init__(self, source_kind: _Optional[str] = ..., availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class DatasetCaseArtifactSummaryV1(_message.Message):
    __slots__ = ("link_id", "artifact_id", "artifact_type", "role", "relation", "lifecycle_status", "conflict_posture", "source_kind", "media_type", "filename", "storage_system", "observed_at")
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_ID_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_STATUS_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_POSTURE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
    MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    STORAGE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    link_id: bytes
    artifact_id: str
    artifact_type: str
    role: str
    relation: str
    lifecycle_status: str
    conflict_posture: str
    source_kind: str
    media_type: str
    filename: str
    storage_system: str
    observed_at: _timestamp_pb2.Timestamp
    def __init__(self, link_id: _Optional[bytes] = ..., artifact_id: _Optional[str] = ..., artifact_type: _Optional[str] = ..., role: _Optional[str] = ..., relation: _Optional[str] = ..., lifecycle_status: _Optional[str] = ..., conflict_posture: _Optional[str] = ..., source_kind: _Optional[str] = ..., media_type: _Optional[str] = ..., filename: _Optional[str] = ..., storage_system: _Optional[str] = ..., observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DatasetCaseArtifactPostureV1(_message.Message):
    __slots__ = ("source_coverage", "artifacts", "resolver_posture", "truncated_artifact_count")
    SOURCE_COVERAGE_FIELD_NUMBER: _ClassVar[int]
    ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    RESOLVER_POSTURE_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_ARTIFACT_COUNT_FIELD_NUMBER: _ClassVar[int]
    source_coverage: _containers.RepeatedCompositeFieldContainer[DatasetCaseArtifactSourceCoverageV1]
    artifacts: _containers.RepeatedCompositeFieldContainer[DatasetCaseArtifactSummaryV1]
    resolver_posture: str
    truncated_artifact_count: int
    def __init__(self, source_coverage: _Optional[_Iterable[_Union[DatasetCaseArtifactSourceCoverageV1, _Mapping]]] = ..., artifacts: _Optional[_Iterable[_Union[DatasetCaseArtifactSummaryV1, _Mapping]]] = ..., resolver_posture: _Optional[str] = ..., truncated_artifact_count: _Optional[int] = ...) -> None: ...

class DatasetCaseSummaryV1(_message.Message):
    __slots__ = ("case_id", "case_revision_id", "revision_number", "ordinal", "source_kind", "completeness", "content_digest", "schema_revision_id", "slice_metadata_json", "tags", "absences", "review_state_code", "review_availability", "recent_performance", "anchor_availability", "created_at")
    CASE_ID_FIELD_NUMBER: _ClassVar[int]
    CASE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
    COMPLETENESS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DIGEST_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    SLICE_METADATA_JSON_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ABSENCES_FIELD_NUMBER: _ClassVar[int]
    REVIEW_STATE_CODE_FIELD_NUMBER: _ClassVar[int]
    REVIEW_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    RECENT_PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    case_id: str
    case_revision_id: str
    revision_number: int
    ordinal: int
    source_kind: EvaluationCaptureSourceKindV1
    completeness: DatasetCaseCompletenessStateV1
    content_digest: str
    schema_revision_id: str
    slice_metadata_json: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    absences: _containers.RepeatedCompositeFieldContainer[EvaluationDatasetCaseAbsenceV1]
    review_state_code: str
    review_availability: MetricAvailabilityV1
    recent_performance: DatasetCaseRecentPerformanceV1
    anchor_availability: DatasetLineageAnchorAvailabilityV1
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, case_id: _Optional[str] = ..., case_revision_id: _Optional[str] = ..., revision_number: _Optional[int] = ..., ordinal: _Optional[int] = ..., source_kind: _Optional[_Union[EvaluationCaptureSourceKindV1, str]] = ..., completeness: _Optional[_Union[DatasetCaseCompletenessStateV1, str]] = ..., content_digest: _Optional[str] = ..., schema_revision_id: _Optional[str] = ..., slice_metadata_json: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., absences: _Optional[_Iterable[_Union[EvaluationDatasetCaseAbsenceV1, _Mapping]]] = ..., review_state_code: _Optional[str] = ..., review_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., recent_performance: _Optional[_Union[DatasetCaseRecentPerformanceV1, _Mapping]] = ..., anchor_availability: _Optional[_Union[DatasetLineageAnchorAvailabilityV1, str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DatasetCaseMembershipV1(_message.Message):
    __slots__ = ("dataset_version_id", "ordinal", "created_at")
    DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    dataset_version_id: str
    ordinal: int
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, dataset_version_id: _Optional[str] = ..., ordinal: _Optional[int] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DatasetCaseV1(_message.Message):
    __slots__ = ("summary", "dataset_collection_id", "identity_key", "identity_source", "revision_count", "input_payload_json", "expected_output_json", "correction_payload_json", "original_context_json", "recorded_output_field_path", "mapping", "lineage", "artifact_posture", "memberships", "schema_revision", "schema_availability")
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_KEY_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    REVISION_COUNT_FIELD_NUMBER: _ClassVar[int]
    INPUT_PAYLOAD_JSON_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUT_JSON_FIELD_NUMBER: _ClassVar[int]
    CORRECTION_PAYLOAD_JSON_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_CONTEXT_JSON_FIELD_NUMBER: _ClassVar[int]
    RECORDED_OUTPUT_FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
    MAPPING_FIELD_NUMBER: _ClassVar[int]
    LINEAGE_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_POSTURE_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIPS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_REVISION_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    summary: DatasetCaseSummaryV1
    dataset_collection_id: str
    identity_key: str
    identity_source: DatasetCaseIdentitySourceV1
    revision_count: int
    input_payload_json: str
    expected_output_json: str
    correction_payload_json: str
    original_context_json: str
    recorded_output_field_path: str
    mapping: _containers.RepeatedCompositeFieldContainer[DatasetFieldMappingV1]
    lineage: DatasetCaseLineageV1
    artifact_posture: DatasetCaseArtifactPostureV1
    memberships: _containers.RepeatedCompositeFieldContainer[DatasetCaseMembershipV1]
    schema_revision: DatasetSchemaRevisionV1
    schema_availability: MetricAvailabilityV1
    def __init__(self, summary: _Optional[_Union[DatasetCaseSummaryV1, _Mapping]] = ..., dataset_collection_id: _Optional[str] = ..., identity_key: _Optional[str] = ..., identity_source: _Optional[_Union[DatasetCaseIdentitySourceV1, str]] = ..., revision_count: _Optional[int] = ..., input_payload_json: _Optional[str] = ..., expected_output_json: _Optional[str] = ..., correction_payload_json: _Optional[str] = ..., original_context_json: _Optional[str] = ..., recorded_output_field_path: _Optional[str] = ..., mapping: _Optional[_Iterable[_Union[DatasetFieldMappingV1, _Mapping]]] = ..., lineage: _Optional[_Union[DatasetCaseLineageV1, _Mapping]] = ..., artifact_posture: _Optional[_Union[DatasetCaseArtifactPostureV1, _Mapping]] = ..., memberships: _Optional[_Iterable[_Union[DatasetCaseMembershipV1, _Mapping]]] = ..., schema_revision: _Optional[_Union[DatasetSchemaRevisionV1, _Mapping]] = ..., schema_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class DatasetQualitySliceCoverageV1(_message.Message):
    __slots__ = ("dimension_key", "covered_cases", "missing_cases", "distinct_values")
    DIMENSION_KEY_FIELD_NUMBER: _ClassVar[int]
    COVERED_CASES_FIELD_NUMBER: _ClassVar[int]
    MISSING_CASES_FIELD_NUMBER: _ClassVar[int]
    DISTINCT_VALUES_FIELD_NUMBER: _ClassVar[int]
    dimension_key: str
    covered_cases: int
    missing_cases: int
    distinct_values: int
    def __init__(self, dimension_key: _Optional[str] = ..., covered_cases: _Optional[int] = ..., missing_cases: _Optional[int] = ..., distinct_values: _Optional[int] = ...) -> None: ...

class DatasetQualityProjectionV1(_message.Message):
    __slots__ = ("dataset_collection_id", "dataset_version_id", "schema_revision_id", "case_count", "slice_coverage", "slice_coverage_availability", "missing_ground_truth_count", "missing_ground_truth_availability", "duplicate_case_count", "conflict_case_count", "duplicate_density_availability", "production_drift_score", "production_drift_availability", "leakage_finding_count", "leakage_availability", "source_complete_count", "source_incomplete_count", "source_completeness_availability", "freshness")
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SLICE_COVERAGE_FIELD_NUMBER: _ClassVar[int]
    SLICE_COVERAGE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    MISSING_GROUND_TRUTH_COUNT_FIELD_NUMBER: _ClassVar[int]
    MISSING_GROUND_TRUTH_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    DUPLICATE_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    DUPLICATE_DENSITY_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    PRODUCTION_DRIFT_SCORE_FIELD_NUMBER: _ClassVar[int]
    PRODUCTION_DRIFT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    LEAKAGE_FINDING_COUNT_FIELD_NUMBER: _ClassVar[int]
    LEAKAGE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_COMPLETE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INCOMPLETE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_COMPLETENESS_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    dataset_collection_id: str
    dataset_version_id: str
    schema_revision_id: str
    case_count: int
    slice_coverage: _containers.RepeatedCompositeFieldContainer[DatasetQualitySliceCoverageV1]
    slice_coverage_availability: MetricAvailabilityV1
    missing_ground_truth_count: int
    missing_ground_truth_availability: MetricAvailabilityV1
    duplicate_case_count: int
    conflict_case_count: int
    duplicate_density_availability: MetricAvailabilityV1
    production_drift_score: float
    production_drift_availability: MetricAvailabilityV1
    leakage_finding_count: int
    leakage_availability: MetricAvailabilityV1
    source_complete_count: int
    source_incomplete_count: int
    source_completeness_availability: MetricAvailabilityV1
    freshness: EvaluationFreshnessV1
    def __init__(self, dataset_collection_id: _Optional[str] = ..., dataset_version_id: _Optional[str] = ..., schema_revision_id: _Optional[str] = ..., case_count: _Optional[int] = ..., slice_coverage: _Optional[_Iterable[_Union[DatasetQualitySliceCoverageV1, _Mapping]]] = ..., slice_coverage_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., missing_ground_truth_count: _Optional[int] = ..., missing_ground_truth_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., duplicate_case_count: _Optional[int] = ..., conflict_case_count: _Optional[int] = ..., duplicate_density_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., production_drift_score: _Optional[float] = ..., production_drift_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., leakage_finding_count: _Optional[int] = ..., leakage_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., source_complete_count: _Optional[int] = ..., source_incomplete_count: _Optional[int] = ..., source_completeness_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class DatasetVersionSummaryV1(_message.Message):
    __slots__ = ("dataset_version_id", "version_number", "label", "case_count", "member_count", "is_pinned", "picker_retired_at", "picker_retired_reason", "schema_revision_id", "created_at")
    DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_PINNED_FIELD_NUMBER: _ClassVar[int]
    PICKER_RETIRED_AT_FIELD_NUMBER: _ClassVar[int]
    PICKER_RETIRED_REASON_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    dataset_version_id: str
    version_number: int
    label: str
    case_count: int
    member_count: int
    is_pinned: bool
    picker_retired_at: _timestamp_pb2.Timestamp
    picker_retired_reason: str
    schema_revision_id: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, dataset_version_id: _Optional[str] = ..., version_number: _Optional[int] = ..., label: _Optional[str] = ..., case_count: _Optional[int] = ..., member_count: _Optional[int] = ..., is_pinned: _Optional[bool] = ..., picker_retired_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., picker_retired_reason: _Optional[str] = ..., schema_revision_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DatasetUsageRowV1(_message.Message):
    __slots__ = ("evaluation_run_id", "dataset_version_id", "cohort_key", "prepared_case_count", "first_prepared_at")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    COHORT_KEY_FIELD_NUMBER: _ClassVar[int]
    PREPARED_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FIRST_PREPARED_AT_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    dataset_version_id: str
    cohort_key: str
    prepared_case_count: int
    first_prepared_at: _timestamp_pb2.Timestamp
    def __init__(self, evaluation_run_id: _Optional[str] = ..., dataset_version_id: _Optional[str] = ..., cohort_key: _Optional[str] = ..., prepared_case_count: _Optional[int] = ..., first_prepared_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetDatasetSchemaRevisionRequest(_message.Message):
    __slots__ = ("schema_revision_id",)
    SCHEMA_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    schema_revision_id: str
    def __init__(self, schema_revision_id: _Optional[str] = ...) -> None: ...

class GetDatasetSchemaRevisionResponse(_message.Message):
    __slots__ = ("revision", "compatibility_with_active", "capabilities")
    REVISION_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_WITH_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    revision: DatasetSchemaRevisionV1
    compatibility_with_active: DatasetSchemaCompatibilityVerdictV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, revision: _Optional[_Union[DatasetSchemaRevisionV1, _Mapping]] = ..., compatibility_with_active: _Optional[_Union[DatasetSchemaCompatibilityVerdictV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class ListDatasetCasesRequest(_message.Message):
    __slots__ = ("dataset_version_id", "after_ordinal", "limit")
    DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    AFTER_ORDINAL_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    dataset_version_id: str
    after_ordinal: int
    limit: int
    def __init__(self, dataset_version_id: _Optional[str] = ..., after_ordinal: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class ListDatasetCasesResponse(_message.Message):
    __slots__ = ("cases", "total_count", "next_after_ordinal", "freshness", "capabilities")
    CASES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    NEXT_AFTER_ORDINAL_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    cases: _containers.RepeatedCompositeFieldContainer[DatasetCaseSummaryV1]
    total_count: int
    next_after_ordinal: int
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, cases: _Optional[_Iterable[_Union[DatasetCaseSummaryV1, _Mapping]]] = ..., total_count: _Optional[int] = ..., next_after_ordinal: _Optional[int] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class GetDatasetCaseRequest(_message.Message):
    __slots__ = ("case_revision_id",)
    CASE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    case_revision_id: str
    def __init__(self, case_revision_id: _Optional[str] = ...) -> None: ...

class GetDatasetCaseResponse(_message.Message):
    __slots__ = ("dataset_case", "freshness", "capabilities")
    DATASET_CASE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    dataset_case: DatasetCaseV1
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, dataset_case: _Optional[_Union[DatasetCaseV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class GetDatasetOverviewRequest(_message.Message):
    __slots__ = ("dataset_collection_id",)
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    dataset_collection_id: str
    def __init__(self, dataset_collection_id: _Optional[str] = ...) -> None: ...

class GetDatasetOverviewResponse(_message.Message):
    __slots__ = ("dataset_collection_id", "active_version", "active_version_availability", "schema_revision", "schema_availability", "quality", "quality_availability", "freshness", "capabilities", "name", "description", "created_at", "is_archived")
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_VERSION_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_VERSION_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_REVISION_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    QUALITY_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    dataset_collection_id: str
    active_version: DatasetVersionSummaryV1
    active_version_availability: MetricAvailabilityV1
    schema_revision: DatasetSchemaRevisionV1
    schema_availability: MetricAvailabilityV1
    quality: DatasetQualityProjectionV1
    quality_availability: MetricAvailabilityV1
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    name: str
    description: str
    created_at: _timestamp_pb2.Timestamp
    is_archived: bool
    def __init__(self, dataset_collection_id: _Optional[str] = ..., active_version: _Optional[_Union[DatasetVersionSummaryV1, _Mapping]] = ..., active_version_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., schema_revision: _Optional[_Union[DatasetSchemaRevisionV1, _Mapping]] = ..., schema_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., quality: _Optional[_Union[DatasetQualityProjectionV1, _Mapping]] = ..., quality_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., is_archived: _Optional[bool] = ...) -> None: ...

class ListEvaluationDatasetVersionsRequest(_message.Message):
    __slots__ = ("dataset_collection_id", "before_version_number", "limit")
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    dataset_collection_id: str
    before_version_number: int
    limit: int
    def __init__(self, dataset_collection_id: _Optional[str] = ..., before_version_number: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class ListEvaluationDatasetVersionsResponse(_message.Message):
    __slots__ = ("versions", "total_count", "next_before_version_number", "freshness", "capabilities")
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    NEXT_BEFORE_VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    versions: _containers.RepeatedCompositeFieldContainer[DatasetVersionSummaryV1]
    total_count: int
    next_before_version_number: int
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, versions: _Optional[_Iterable[_Union[DatasetVersionSummaryV1, _Mapping]]] = ..., total_count: _Optional[int] = ..., next_before_version_number: _Optional[int] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class ListDatasetUsageRequest(_message.Message):
    __slots__ = ("dataset_collection_id", "after_evaluation_run_id", "limit")
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    AFTER_EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    dataset_collection_id: str
    after_evaluation_run_id: str
    limit: int
    def __init__(self, dataset_collection_id: _Optional[str] = ..., after_evaluation_run_id: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ListDatasetUsageResponse(_message.Message):
    __slots__ = ("usage", "total_count", "next_after_evaluation_run_id", "freshness", "capabilities")
    USAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    NEXT_AFTER_EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    usage: _containers.RepeatedCompositeFieldContainer[DatasetUsageRowV1]
    total_count: int
    next_after_evaluation_run_id: str
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, usage: _Optional[_Iterable[_Union[DatasetUsageRowV1, _Mapping]]] = ..., total_count: _Optional[int] = ..., next_after_evaluation_run_id: _Optional[str] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class DatasetCaseDraftConflictV1(_message.Message):
    __slots__ = ("current_draft_version", "changed_fields", "current_state")
    CURRENT_DRAFT_VERSION_FIELD_NUMBER: _ClassVar[int]
    CHANGED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STATE_FIELD_NUMBER: _ClassVar[int]
    current_draft_version: int
    changed_fields: _containers.RepeatedScalarFieldContainer[str]
    current_state: DatasetCaseDraftStateV1
    def __init__(self, current_draft_version: _Optional[int] = ..., changed_fields: _Optional[_Iterable[str]] = ..., current_state: _Optional[_Union[DatasetCaseDraftStateV1, str]] = ...) -> None: ...

class DatasetDraftRefusalV1(_message.Message):
    __slots__ = ("kind", "reason_code", "detail", "recovery", "conflict", "from_state", "to_state")
    KIND_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_FIELD_NUMBER: _ClassVar[int]
    FROM_STATE_FIELD_NUMBER: _ClassVar[int]
    TO_STATE_FIELD_NUMBER: _ClassVar[int]
    kind: DatasetDraftRefusalKindV1
    reason_code: str
    detail: str
    recovery: RecoveryActionV1
    conflict: DatasetCaseDraftConflictV1
    from_state: DatasetCaseDraftStateV1
    to_state: DatasetCaseDraftStateV1
    def __init__(self, kind: _Optional[_Union[DatasetDraftRefusalKindV1, str]] = ..., reason_code: _Optional[str] = ..., detail: _Optional[str] = ..., recovery: _Optional[_Union[RecoveryActionV1, str]] = ..., conflict: _Optional[_Union[DatasetCaseDraftConflictV1, _Mapping]] = ..., from_state: _Optional[_Union[DatasetCaseDraftStateV1, str]] = ..., to_state: _Optional[_Union[DatasetCaseDraftStateV1, str]] = ...) -> None: ...

class DatasetCaseDraftLineageV1(_message.Message):
    __slots__ = ("provenance", "promotion_source_reference", "source_availability", "source_content_refs", "selections", "content_digest", "draft_id")
    PROVENANCE_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_SOURCE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONTENT_REFS_FIELD_NUMBER: _ClassVar[int]
    SELECTIONS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DIGEST_FIELD_NUMBER: _ClassVar[int]
    DRAFT_ID_FIELD_NUMBER: _ClassVar[int]
    provenance: EvaluationCaptureProvenanceV1
    promotion_source_reference: str
    source_availability: MetricAvailabilityV1
    source_content_refs: _containers.RepeatedCompositeFieldContainer[EvaluationSpanContentHydrationV1]
    selections: _containers.RepeatedCompositeFieldContainer[EvaluationCaptureFieldSelectionV1]
    content_digest: str
    draft_id: str
    def __init__(self, provenance: _Optional[_Union[EvaluationCaptureProvenanceV1, _Mapping]] = ..., promotion_source_reference: _Optional[str] = ..., source_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., source_content_refs: _Optional[_Iterable[_Union[EvaluationSpanContentHydrationV1, _Mapping]]] = ..., selections: _Optional[_Iterable[_Union[EvaluationCaptureFieldSelectionV1, _Mapping]]] = ..., content_digest: _Optional[str] = ..., draft_id: _Optional[str] = ...) -> None: ...

class DatasetCaseDraftV1(_message.Message):
    __slots__ = ("proposed_case_id", "dataset_collection_id", "changeset_id", "ordinal", "state", "draft_version", "source_kind", "lineage", "input_availability", "expected_output_availability", "recorded_output_availability", "recorded_output_field_path", "input_payload_json", "expected_output_json", "correction_payload_json", "original_context_json", "reviewer", "review_task_id", "reservation_expires_at", "review_outcome", "rejection_reason", "changes_requested_note", "merged_into_case_revision_id", "superseded_by_proposed_case_id", "published_dataset_version_id", "published_case_revision_id", "quality", "reviewed_at", "published_at", "state_changed_at", "created_at")
    PROPOSED_CASE_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    CHANGESET_ID_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DRAFT_VERSION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
    LINEAGE_FIELD_NUMBER: _ClassVar[int]
    INPUT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    RECORDED_OUTPUT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    RECORDED_OUTPUT_FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
    INPUT_PAYLOAD_JSON_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUT_JSON_FIELD_NUMBER: _ClassVar[int]
    CORRECTION_PAYLOAD_JSON_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_CONTEXT_JSON_FIELD_NUMBER: _ClassVar[int]
    REVIEWER_FIELD_NUMBER: _ClassVar[int]
    REVIEW_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    REVIEW_OUTCOME_FIELD_NUMBER: _ClassVar[int]
    REJECTION_REASON_FIELD_NUMBER: _ClassVar[int]
    CHANGES_REQUESTED_NOTE_FIELD_NUMBER: _ClassVar[int]
    MERGED_INTO_CASE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    SUPERSEDED_BY_PROPOSED_CASE_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_CASE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    REVIEWED_AT_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    STATE_CHANGED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    proposed_case_id: str
    dataset_collection_id: str
    changeset_id: str
    ordinal: int
    state: DatasetCaseDraftStateV1
    draft_version: int
    source_kind: EvaluationCaptureSourceKindV1
    lineage: DatasetCaseDraftLineageV1
    input_availability: MetricAvailabilityV1
    expected_output_availability: MetricAvailabilityV1
    recorded_output_availability: MetricAvailabilityV1
    recorded_output_field_path: str
    input_payload_json: str
    expected_output_json: str
    correction_payload_json: str
    original_context_json: str
    reviewer: PrincipalRefV1
    review_task_id: str
    reservation_expires_at: _timestamp_pb2.Timestamp
    review_outcome: DatasetCaseReviewOutcomeV1
    rejection_reason: DatasetCaseDraftRejectionReasonV1
    changes_requested_note: str
    merged_into_case_revision_id: str
    superseded_by_proposed_case_id: str
    published_dataset_version_id: str
    published_case_revision_id: str
    quality: DatasetCaseQualitySignalsV1
    reviewed_at: _timestamp_pb2.Timestamp
    published_at: _timestamp_pb2.Timestamp
    state_changed_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, proposed_case_id: _Optional[str] = ..., dataset_collection_id: _Optional[str] = ..., changeset_id: _Optional[str] = ..., ordinal: _Optional[int] = ..., state: _Optional[_Union[DatasetCaseDraftStateV1, str]] = ..., draft_version: _Optional[int] = ..., source_kind: _Optional[_Union[EvaluationCaptureSourceKindV1, str]] = ..., lineage: _Optional[_Union[DatasetCaseDraftLineageV1, _Mapping]] = ..., input_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., expected_output_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., recorded_output_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., recorded_output_field_path: _Optional[str] = ..., input_payload_json: _Optional[str] = ..., expected_output_json: _Optional[str] = ..., correction_payload_json: _Optional[str] = ..., original_context_json: _Optional[str] = ..., reviewer: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., review_task_id: _Optional[str] = ..., reservation_expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., review_outcome: _Optional[_Union[DatasetCaseReviewOutcomeV1, str]] = ..., rejection_reason: _Optional[_Union[DatasetCaseDraftRejectionReasonV1, str]] = ..., changes_requested_note: _Optional[str] = ..., merged_into_case_revision_id: _Optional[str] = ..., superseded_by_proposed_case_id: _Optional[str] = ..., published_dataset_version_id: _Optional[str] = ..., published_case_revision_id: _Optional[str] = ..., quality: _Optional[_Union[DatasetCaseQualitySignalsV1, _Mapping]] = ..., reviewed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., state_changed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DatasetChangesetV1(_message.Message):
    __slots__ = ("changeset_id", "dataset_collection_id", "state", "base_dataset_version_id", "changeset_version", "proposed_case_count", "voided_case_count", "preview_digest", "preview_computed_at", "schema_revision_id", "failure_reason_code", "failure_detail", "committed_dataset_version_id", "created_at", "updated_at")
    CHANGESET_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    BASE_DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    CHANGESET_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    VOIDED_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_DIGEST_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_COMPUTED_AT_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_DETAIL_FIELD_NUMBER: _ClassVar[int]
    COMMITTED_DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    changeset_id: str
    dataset_collection_id: str
    state: DatasetChangesetStateV1
    base_dataset_version_id: str
    changeset_version: int
    proposed_case_count: int
    voided_case_count: int
    preview_digest: str
    preview_computed_at: _timestamp_pb2.Timestamp
    schema_revision_id: str
    failure_reason_code: str
    failure_detail: str
    committed_dataset_version_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, changeset_id: _Optional[str] = ..., dataset_collection_id: _Optional[str] = ..., state: _Optional[_Union[DatasetChangesetStateV1, str]] = ..., base_dataset_version_id: _Optional[str] = ..., changeset_version: _Optional[int] = ..., proposed_case_count: _Optional[int] = ..., voided_case_count: _Optional[int] = ..., preview_digest: _Optional[str] = ..., preview_computed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., schema_revision_id: _Optional[str] = ..., failure_reason_code: _Optional[str] = ..., failure_detail: _Optional[str] = ..., committed_dataset_version_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DatasetPublishLinkedEvaluationV1(_message.Message):
    __slots__ = ("evaluation_definition_id", "evaluation_definition_revision_id", "definition_name", "dispatch_idempotency_key")
    EVALUATION_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_DEFINITION_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    evaluation_definition_id: str
    evaluation_definition_revision_id: str
    definition_name: str
    dispatch_idempotency_key: str
    def __init__(self, evaluation_definition_id: _Optional[str] = ..., evaluation_definition_revision_id: _Optional[str] = ..., definition_name: _Optional[str] = ..., dispatch_idempotency_key: _Optional[str] = ...) -> None: ...

class DatasetChangesetPreviewV1(_message.Message):
    __slots__ = ("changeset", "active_dataset_version_id", "base_version_moved", "schema_compatibility", "approved_proposed_case_ids", "unapproved_proposed_case_ids", "dedupe_resolutions", "conflicts", "linked_evaluation_plan", "preview_digest", "publishable", "quality")
    CHANGESET_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_VERSION_MOVED_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_COMPATIBILITY_FIELD_NUMBER: _ClassVar[int]
    APPROVED_PROPOSED_CASE_IDS_FIELD_NUMBER: _ClassVar[int]
    UNAPPROVED_PROPOSED_CASE_IDS_FIELD_NUMBER: _ClassVar[int]
    DEDUPE_RESOLUTIONS_FIELD_NUMBER: _ClassVar[int]
    CONFLICTS_FIELD_NUMBER: _ClassVar[int]
    LINKED_EVALUATION_PLAN_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_DIGEST_FIELD_NUMBER: _ClassVar[int]
    PUBLISHABLE_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    changeset: DatasetChangesetV1
    active_dataset_version_id: str
    base_version_moved: bool
    schema_compatibility: DatasetSchemaCompatibilityVerdictV1
    approved_proposed_case_ids: _containers.RepeatedScalarFieldContainer[str]
    unapproved_proposed_case_ids: _containers.RepeatedScalarFieldContainer[str]
    dedupe_resolutions: _containers.RepeatedCompositeFieldContainer[DedupeResolutionV1]
    conflicts: _containers.RepeatedCompositeFieldContainer[DataQualityFindingV1]
    linked_evaluation_plan: _containers.RepeatedCompositeFieldContainer[DatasetPublishLinkedEvaluationV1]
    preview_digest: str
    publishable: bool
    quality: ChangesetQualitySignalsV1
    def __init__(self, changeset: _Optional[_Union[DatasetChangesetV1, _Mapping]] = ..., active_dataset_version_id: _Optional[str] = ..., base_version_moved: _Optional[bool] = ..., schema_compatibility: _Optional[_Union[DatasetSchemaCompatibilityVerdictV1, _Mapping]] = ..., approved_proposed_case_ids: _Optional[_Iterable[str]] = ..., unapproved_proposed_case_ids: _Optional[_Iterable[str]] = ..., dedupe_resolutions: _Optional[_Iterable[_Union[DedupeResolutionV1, _Mapping]]] = ..., conflicts: _Optional[_Iterable[_Union[DataQualityFindingV1, _Mapping]]] = ..., linked_evaluation_plan: _Optional[_Iterable[_Union[DatasetPublishLinkedEvaluationV1, _Mapping]]] = ..., preview_digest: _Optional[str] = ..., publishable: _Optional[bool] = ..., quality: _Optional[_Union[ChangesetQualitySignalsV1, _Mapping]] = ...) -> None: ...

class DatasetPublishResultV1(_message.Message):
    __slots__ = ("version", "changeset", "published_case_count", "reused_revision_count", "dispatch_obligations", "rollover")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CHANGESET_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    REUSED_REVISION_COUNT_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_OBLIGATIONS_FIELD_NUMBER: _ClassVar[int]
    ROLLOVER_FIELD_NUMBER: _ClassVar[int]
    version: EvaluationDatasetVersionV1
    changeset: DatasetChangesetV1
    published_case_count: int
    reused_revision_count: int
    dispatch_obligations: _containers.RepeatedCompositeFieldContainer[DatasetPublishLinkedEvaluationV1]
    rollover: EvaluationDatasetRolloverV1
    def __init__(self, version: _Optional[_Union[EvaluationDatasetVersionV1, _Mapping]] = ..., changeset: _Optional[_Union[DatasetChangesetV1, _Mapping]] = ..., published_case_count: _Optional[int] = ..., reused_revision_count: _Optional[int] = ..., dispatch_obligations: _Optional[_Iterable[_Union[DatasetPublishLinkedEvaluationV1, _Mapping]]] = ..., rollover: _Optional[_Union[EvaluationDatasetRolloverV1, _Mapping]] = ...) -> None: ...

class GetDatasetCaseDraftRequest(_message.Message):
    __slots__ = ("proposed_case_id",)
    PROPOSED_CASE_ID_FIELD_NUMBER: _ClassVar[int]
    proposed_case_id: str
    def __init__(self, proposed_case_id: _Optional[str] = ...) -> None: ...

class GetDatasetCaseDraftResponse(_message.Message):
    __slots__ = ("draft", "freshness", "capabilities")
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    draft: DatasetCaseDraftV1
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, draft: _Optional[_Union[DatasetCaseDraftV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class ListDatasetCaseDraftsRequest(_message.Message):
    __slots__ = ("dataset_collection_id", "changeset_id", "states", "reviewer_principal_id", "page_size", "offset")
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    CHANGESET_ID_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    REVIEWER_PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    dataset_collection_id: str
    changeset_id: str
    states: _containers.RepeatedScalarFieldContainer[DatasetCaseDraftStateV1]
    reviewer_principal_id: str
    page_size: int
    offset: int
    def __init__(self, dataset_collection_id: _Optional[str] = ..., changeset_id: _Optional[str] = ..., states: _Optional[_Iterable[_Union[DatasetCaseDraftStateV1, str]]] = ..., reviewer_principal_id: _Optional[str] = ..., page_size: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListDatasetCaseDraftsResponse(_message.Message):
    __slots__ = ("drafts", "total_count", "next_offset", "freshness", "capabilities")
    DRAFTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    NEXT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    drafts: _containers.RepeatedCompositeFieldContainer[DatasetCaseDraftV1]
    total_count: int
    next_offset: int
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, drafts: _Optional[_Iterable[_Union[DatasetCaseDraftV1, _Mapping]]] = ..., total_count: _Optional[int] = ..., next_offset: _Optional[int] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class UpdateDatasetCaseDraftRequest(_message.Message):
    __slots__ = ("proposed_case_id", "expected_draft_version", "expected_output_json", "expected_output_absence_reason", "correction_payload_json", "needs_ground_truth", "idempotency_key")
    PROPOSED_CASE_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_DRAFT_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUT_JSON_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUT_ABSENCE_REASON_FIELD_NUMBER: _ClassVar[int]
    CORRECTION_PAYLOAD_JSON_FIELD_NUMBER: _ClassVar[int]
    NEEDS_GROUND_TRUTH_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    proposed_case_id: str
    expected_draft_version: int
    expected_output_json: str
    expected_output_absence_reason: str
    correction_payload_json: str
    needs_ground_truth: bool
    idempotency_key: str
    def __init__(self, proposed_case_id: _Optional[str] = ..., expected_draft_version: _Optional[int] = ..., expected_output_json: _Optional[str] = ..., expected_output_absence_reason: _Optional[str] = ..., correction_payload_json: _Optional[str] = ..., needs_ground_truth: _Optional[bool] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class UpdateDatasetCaseDraftResponse(_message.Message):
    __slots__ = ("draft", "capabilities")
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    draft: DatasetCaseDraftV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, draft: _Optional[_Union[DatasetCaseDraftV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class ApproveDatasetCaseDraftRequest(_message.Message):
    __slots__ = ("proposed_case_id", "expected_draft_version", "note", "idempotency_key")
    PROPOSED_CASE_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_DRAFT_VERSION_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    proposed_case_id: str
    expected_draft_version: int
    note: str
    idempotency_key: str
    def __init__(self, proposed_case_id: _Optional[str] = ..., expected_draft_version: _Optional[int] = ..., note: _Optional[str] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class ApproveDatasetCaseDraftResponse(_message.Message):
    __slots__ = ("draft", "changeset", "capabilities")
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    CHANGESET_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    draft: DatasetCaseDraftV1
    changeset: DatasetChangesetV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, draft: _Optional[_Union[DatasetCaseDraftV1, _Mapping]] = ..., changeset: _Optional[_Union[DatasetChangesetV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class RejectDatasetCaseDraftRequest(_message.Message):
    __slots__ = ("proposed_case_id", "expected_draft_version", "reason", "note", "idempotency_key")
    PROPOSED_CASE_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_DRAFT_VERSION_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    proposed_case_id: str
    expected_draft_version: int
    reason: DatasetCaseDraftRejectionReasonV1
    note: str
    idempotency_key: str
    def __init__(self, proposed_case_id: _Optional[str] = ..., expected_draft_version: _Optional[int] = ..., reason: _Optional[_Union[DatasetCaseDraftRejectionReasonV1, str]] = ..., note: _Optional[str] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class RejectDatasetCaseDraftResponse(_message.Message):
    __slots__ = ("draft", "capabilities")
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    draft: DatasetCaseDraftV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, draft: _Optional[_Union[DatasetCaseDraftV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class MergeDatasetCaseDraftRequest(_message.Message):
    __slots__ = ("proposed_case_id", "expected_draft_version", "target_case_revision_id", "note", "idempotency_key")
    PROPOSED_CASE_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_DRAFT_VERSION_FIELD_NUMBER: _ClassVar[int]
    TARGET_CASE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    proposed_case_id: str
    expected_draft_version: int
    target_case_revision_id: str
    note: str
    idempotency_key: str
    def __init__(self, proposed_case_id: _Optional[str] = ..., expected_draft_version: _Optional[int] = ..., target_case_revision_id: _Optional[str] = ..., note: _Optional[str] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class MergeDatasetCaseDraftResponse(_message.Message):
    __slots__ = ("draft", "capabilities")
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    draft: DatasetCaseDraftV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, draft: _Optional[_Union[DatasetCaseDraftV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class PreviewPublishDatasetChangesetRequest(_message.Message):
    __slots__ = ("changeset_id",)
    CHANGESET_ID_FIELD_NUMBER: _ClassVar[int]
    changeset_id: str
    def __init__(self, changeset_id: _Optional[str] = ...) -> None: ...

class PreviewPublishDatasetChangesetResponse(_message.Message):
    __slots__ = ("preview", "freshness", "capabilities")
    PREVIEW_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    preview: DatasetChangesetPreviewV1
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, preview: _Optional[_Union[DatasetChangesetPreviewV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class PublishDatasetCaseDraftsRequest(_message.Message):
    __slots__ = ("changeset_id", "preview_digest", "label", "idempotency_key")
    CHANGESET_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_DIGEST_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    changeset_id: str
    preview_digest: str
    label: str
    idempotency_key: str
    def __init__(self, changeset_id: _Optional[str] = ..., preview_digest: _Optional[str] = ..., label: _Optional[str] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class PublishDatasetCaseDraftsResponse(_message.Message):
    __slots__ = ("result", "idempotent_replay", "capabilities")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    result: DatasetPublishResultV1
    idempotent_replay: bool
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, result: _Optional[_Union[DatasetPublishResultV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class PreviewProductionEvaluationRuleRequest(_message.Message):
    __slots__ = ("version_id", "draft", "sample_window_seconds", "max_candidates")
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_WINDOW_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MAX_CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    version_id: str
    draft: ProductionRulePreviewDraftSubjectV1
    sample_window_seconds: int
    max_candidates: int
    def __init__(self, version_id: _Optional[str] = ..., draft: _Optional[_Union[ProductionRulePreviewDraftSubjectV1, _Mapping]] = ..., sample_window_seconds: _Optional[int] = ..., max_candidates: _Optional[int] = ...) -> None: ...

class ProductionRulePreviewDraftSubjectV1(_message.Message):
    __slots__ = ("rule_id", "version", "assumed_state")
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ASSUMED_STATE_FIELD_NUMBER: _ClassVar[int]
    rule_id: str
    version: ProductionRuleVersionDraftV1
    assumed_state: ProductionRuleVersionStateV1
    def __init__(self, rule_id: _Optional[str] = ..., version: _Optional[_Union[ProductionRuleVersionDraftV1, _Mapping]] = ..., assumed_state: _Optional[_Union[ProductionRuleVersionStateV1, str]] = ...) -> None: ...

class ProductionRulePreviewWindowV1(_message.Message):
    __slots__ = ("window_start", "window_end", "sample_window_seconds", "effective_max_candidates", "observation_basis", "population_completeness", "population_incomplete_reason_code", "cumulative_counts", "truncated", "observed_offer_count")
    WINDOW_START_FIELD_NUMBER: _ClassVar[int]
    WINDOW_END_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_WINDOW_SECONDS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_MAX_CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_BASIS_FIELD_NUMBER: _ClassVar[int]
    POPULATION_COMPLETENESS_FIELD_NUMBER: _ClassVar[int]
    POPULATION_INCOMPLETE_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    CUMULATIVE_COUNTS_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_OFFER_COUNT_FIELD_NUMBER: _ClassVar[int]
    window_start: _timestamp_pb2.Timestamp
    window_end: _timestamp_pb2.Timestamp
    sample_window_seconds: int
    effective_max_candidates: int
    observation_basis: ProductionRulePreviewObservationBasisV1
    population_completeness: CompletenessStateV1
    population_incomplete_reason_code: str
    cumulative_counts: ProductionRulePreviewCumulativeCountsV1
    truncated: bool
    observed_offer_count: int
    def __init__(self, window_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., window_end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., sample_window_seconds: _Optional[int] = ..., effective_max_candidates: _Optional[int] = ..., observation_basis: _Optional[_Union[ProductionRulePreviewObservationBasisV1, str]] = ..., population_completeness: _Optional[_Union[CompletenessStateV1, str]] = ..., population_incomplete_reason_code: _Optional[str] = ..., cumulative_counts: _Optional[_Union[ProductionRulePreviewCumulativeCountsV1, _Mapping]] = ..., truncated: _Optional[bool] = ..., observed_offer_count: _Optional[int] = ...) -> None: ...

class ProductionRulePreviewCumulativeCountsV1(_message.Message):
    __slots__ = ("eligible", "matched", "sampled")
    ELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    MATCHED_FIELD_NUMBER: _ClassVar[int]
    SAMPLED_FIELD_NUMBER: _ClassVar[int]
    eligible: int
    matched: int
    sampled: int
    def __init__(self, eligible: _Optional[int] = ..., matched: _Optional[int] = ..., sampled: _Optional[int] = ...) -> None: ...

class ProductionRulePreviewBucketV1(_message.Message):
    __slots__ = ("count", "inclusion_reason_codes", "exclusion_reason_codes")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    INCLUSION_REASON_CODES_FIELD_NUMBER: _ClassVar[int]
    EXCLUSION_REASON_CODES_FIELD_NUMBER: _ClassVar[int]
    count: int
    inclusion_reason_codes: _containers.RepeatedScalarFieldContainer[str]
    exclusion_reason_codes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, count: _Optional[int] = ..., inclusion_reason_codes: _Optional[_Iterable[str]] = ..., exclusion_reason_codes: _Optional[_Iterable[str]] = ...) -> None: ...

class ProductionRulePreviewIdleBucketV1(_message.Message):
    __slots__ = ("availability", "count", "configured_idle_timeout_seconds")
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_IDLE_TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    availability: MetricAvailabilityV1
    count: int
    configured_idle_timeout_seconds: int
    def __init__(self, availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., count: _Optional[int] = ..., configured_idle_timeout_seconds: _Optional[int] = ...) -> None: ...

class ProductionRulePreviewBucketsV1(_message.Message):
    __slots__ = ("eligible", "matched", "sampled", "sampled_out", "budget_blocked", "already_executed", "idle")
    ELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    MATCHED_FIELD_NUMBER: _ClassVar[int]
    SAMPLED_FIELD_NUMBER: _ClassVar[int]
    SAMPLED_OUT_FIELD_NUMBER: _ClassVar[int]
    BUDGET_BLOCKED_FIELD_NUMBER: _ClassVar[int]
    ALREADY_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    IDLE_FIELD_NUMBER: _ClassVar[int]
    eligible: ProductionRulePreviewBucketV1
    matched: ProductionRulePreviewBucketV1
    sampled: ProductionRulePreviewBucketV1
    sampled_out: ProductionRulePreviewBucketV1
    budget_blocked: ProductionRulePreviewBucketV1
    already_executed: ProductionRulePreviewBucketV1
    idle: ProductionRulePreviewIdleBucketV1
    def __init__(self, eligible: _Optional[_Union[ProductionRulePreviewBucketV1, _Mapping]] = ..., matched: _Optional[_Union[ProductionRulePreviewBucketV1, _Mapping]] = ..., sampled: _Optional[_Union[ProductionRulePreviewBucketV1, _Mapping]] = ..., sampled_out: _Optional[_Union[ProductionRulePreviewBucketV1, _Mapping]] = ..., budget_blocked: _Optional[_Union[ProductionRulePreviewBucketV1, _Mapping]] = ..., already_executed: _Optional[_Union[ProductionRulePreviewBucketV1, _Mapping]] = ..., idle: _Optional[_Union[ProductionRulePreviewIdleBucketV1, _Mapping]] = ...) -> None: ...

class ProductionRulePreviewEstimateV1(_message.Message):
    __slots__ = ("estimated_scorer_executions", "scorer_count", "evaluator_cost", "evaluator_cost_availability", "cost_assumption", "priced_scorer_count", "unpriced_scorer_count", "observed_cost_micros_in_window")
    ESTIMATED_SCORER_EXECUTIONS_FIELD_NUMBER: _ClassVar[int]
    SCORER_COUNT_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_COST_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_COST_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    COST_ASSUMPTION_FIELD_NUMBER: _ClassVar[int]
    PRICED_SCORER_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNPRICED_SCORER_COUNT_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_COST_MICROS_IN_WINDOW_FIELD_NUMBER: _ClassVar[int]
    estimated_scorer_executions: int
    scorer_count: int
    evaluator_cost: CostAmountV1
    evaluator_cost_availability: MetricAvailabilityV1
    cost_assumption: EvaluationCostAssumptionV1
    priced_scorer_count: int
    unpriced_scorer_count: int
    observed_cost_micros_in_window: int
    def __init__(self, estimated_scorer_executions: _Optional[int] = ..., scorer_count: _Optional[int] = ..., evaluator_cost: _Optional[_Union[CostAmountV1, _Mapping]] = ..., evaluator_cost_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., cost_assumption: _Optional[_Union[EvaluationCostAssumptionV1, _Mapping]] = ..., priced_scorer_count: _Optional[int] = ..., unpriced_scorer_count: _Optional[int] = ..., observed_cost_micros_in_window: _Optional[int] = ...) -> None: ...

class ProductionRulePreviewBudgetPostureV1(_message.Message):
    __slots__ = ("admits_today", "daily_budget_micros", "daily_spend_micros_today", "spend_date_is_today", "remaining_micros_today", "posture_code")
    ADMITS_TODAY_FIELD_NUMBER: _ClassVar[int]
    DAILY_BUDGET_MICROS_FIELD_NUMBER: _ClassVar[int]
    DAILY_SPEND_MICROS_TODAY_FIELD_NUMBER: _ClassVar[int]
    SPEND_DATE_IS_TODAY_FIELD_NUMBER: _ClassVar[int]
    REMAINING_MICROS_TODAY_FIELD_NUMBER: _ClassVar[int]
    POSTURE_CODE_FIELD_NUMBER: _ClassVar[int]
    admits_today: bool
    daily_budget_micros: int
    daily_spend_micros_today: int
    spend_date_is_today: bool
    remaining_micros_today: int
    posture_code: str
    def __init__(self, admits_today: _Optional[bool] = ..., daily_budget_micros: _Optional[int] = ..., daily_spend_micros_today: _Optional[int] = ..., spend_date_is_today: _Optional[bool] = ..., remaining_micros_today: _Optional[int] = ..., posture_code: _Optional[str] = ...) -> None: ...

class ProductionRulePreviewPromotionImplicationV1(_message.Message):
    __slots__ = ("dataset_collection_id", "collection_resolves", "field_mapping_count", "dedupe_key_template", "dedupe_seam_code", "redaction_posture", "redaction_absence_reason_code", "review_implication_code")
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_RESOLVES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MAPPING_COUNT_FIELD_NUMBER: _ClassVar[int]
    DEDUPE_KEY_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    DEDUPE_SEAM_CODE_FIELD_NUMBER: _ClassVar[int]
    REDACTION_POSTURE_FIELD_NUMBER: _ClassVar[int]
    REDACTION_ABSENCE_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    REVIEW_IMPLICATION_CODE_FIELD_NUMBER: _ClassVar[int]
    dataset_collection_id: str
    collection_resolves: bool
    field_mapping_count: int
    dedupe_key_template: str
    dedupe_seam_code: str
    redaction_posture: ProductionRulePreviewRedactionPostureV1
    redaction_absence_reason_code: str
    review_implication_code: str
    def __init__(self, dataset_collection_id: _Optional[str] = ..., collection_resolves: _Optional[bool] = ..., field_mapping_count: _Optional[int] = ..., dedupe_key_template: _Optional[str] = ..., dedupe_seam_code: _Optional[str] = ..., redaction_posture: _Optional[_Union[ProductionRulePreviewRedactionPostureV1, str]] = ..., redaction_absence_reason_code: _Optional[str] = ..., review_implication_code: _Optional[str] = ...) -> None: ...

class ProductionRulePreviewReviewImplicationV1(_message.Message):
    __slots__ = ("reviewer_principal_id", "reviewer_is_member", "subject_source_code", "subject_available")
    REVIEWER_PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    REVIEWER_IS_MEMBER_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_SOURCE_CODE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    reviewer_principal_id: str
    reviewer_is_member: bool
    subject_source_code: str
    subject_available: bool
    def __init__(self, reviewer_principal_id: _Optional[str] = ..., reviewer_is_member: _Optional[bool] = ..., subject_source_code: _Optional[str] = ..., subject_available: _Optional[bool] = ...) -> None: ...

class ProductionRulePreviewLinkedEvaluationImplicationV1(_message.Message):
    __slots__ = ("evaluation_definition_id", "definition_resolves", "revision_pin", "evaluation_definition_revision_id", "charge_basis_code", "candidate_cost_availability", "candidate_cost")
    EVALUATION_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_RESOLVES_FIELD_NUMBER: _ClassVar[int]
    REVISION_PIN_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_DEFINITION_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    CHARGE_BASIS_CODE_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_COST_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_COST_FIELD_NUMBER: _ClassVar[int]
    evaluation_definition_id: str
    definition_resolves: bool
    revision_pin: ProductionRulePreviewRevisionPinV1
    evaluation_definition_revision_id: str
    charge_basis_code: str
    candidate_cost_availability: MetricAvailabilityV1
    candidate_cost: CostAmountV1
    def __init__(self, evaluation_definition_id: _Optional[str] = ..., definition_resolves: _Optional[bool] = ..., revision_pin: _Optional[_Union[ProductionRulePreviewRevisionPinV1, str]] = ..., evaluation_definition_revision_id: _Optional[str] = ..., charge_basis_code: _Optional[str] = ..., candidate_cost_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., candidate_cost: _Optional[_Union[CostAmountV1, _Mapping]] = ...) -> None: ...

class ProductionRulePreviewNotifyImplicationV1(_message.Message):
    __slots__ = ("alert_destination_id", "destination_resolves", "delivery_semantics_code")
    ALERT_DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_RESOLVES_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_SEMANTICS_CODE_FIELD_NUMBER: _ClassVar[int]
    alert_destination_id: str
    destination_resolves: bool
    delivery_semantics_code: str
    def __init__(self, alert_destination_id: _Optional[str] = ..., destination_resolves: _Optional[bool] = ..., delivery_semantics_code: _Optional[str] = ...) -> None: ...

class ProductionRulePreviewReleaseBlockImplicationV1(_message.Message):
    __slots__ = ("block_reason_code", "clear_condition", "ttl_days", "indeterminate_reason_codes", "affected_release_keys", "affected_release_keys_truncated", "release_key_source_code")
    BLOCK_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    CLEAR_CONDITION_FIELD_NUMBER: _ClassVar[int]
    TTL_DAYS_FIELD_NUMBER: _ClassVar[int]
    INDETERMINATE_REASON_CODES_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_RELEASE_KEYS_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_RELEASE_KEYS_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    RELEASE_KEY_SOURCE_CODE_FIELD_NUMBER: _ClassVar[int]
    block_reason_code: str
    clear_condition: ProductionReleaseBlockClearConditionV1
    ttl_days: int
    indeterminate_reason_codes: _containers.RepeatedScalarFieldContainer[str]
    affected_release_keys: _containers.RepeatedScalarFieldContainer[str]
    affected_release_keys_truncated: bool
    release_key_source_code: str
    def __init__(self, block_reason_code: _Optional[str] = ..., clear_condition: _Optional[_Union[ProductionReleaseBlockClearConditionV1, str]] = ..., ttl_days: _Optional[int] = ..., indeterminate_reason_codes: _Optional[_Iterable[str]] = ..., affected_release_keys: _Optional[_Iterable[str]] = ..., affected_release_keys_truncated: _Optional[bool] = ..., release_key_source_code: _Optional[str] = ...) -> None: ...

class ProductionRulePreviewActionCandidateV1(_message.Message):
    __slots__ = ("ordinal", "action_kind", "condition", "target", "target_resolution", "target_resolution_reason_code", "dispatch_count_availability", "estimated_dispatch_count", "promotion", "review", "linked_evaluation", "notify", "release_block")
    ORDINAL_FIELD_NUMBER: _ClassVar[int]
    ACTION_KIND_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    TARGET_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    TARGET_RESOLUTION_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_COUNT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_DISPATCH_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_FIELD_NUMBER: _ClassVar[int]
    REVIEW_FIELD_NUMBER: _ClassVar[int]
    LINKED_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_FIELD_NUMBER: _ClassVar[int]
    RELEASE_BLOCK_FIELD_NUMBER: _ClassVar[int]
    ordinal: int
    action_kind: ProductionRuleActionKindV1
    condition: ProductionRuleActionConditionV1
    target: ProductionRuleActionTargetV1
    target_resolution: ProductionRulePreviewTargetResolutionV1
    target_resolution_reason_code: str
    dispatch_count_availability: MetricAvailabilityV1
    estimated_dispatch_count: int
    promotion: ProductionRulePreviewPromotionImplicationV1
    review: ProductionRulePreviewReviewImplicationV1
    linked_evaluation: ProductionRulePreviewLinkedEvaluationImplicationV1
    notify: ProductionRulePreviewNotifyImplicationV1
    release_block: ProductionRulePreviewReleaseBlockImplicationV1
    def __init__(self, ordinal: _Optional[int] = ..., action_kind: _Optional[_Union[ProductionRuleActionKindV1, str]] = ..., condition: _Optional[_Union[ProductionRuleActionConditionV1, _Mapping]] = ..., target: _Optional[_Union[ProductionRuleActionTargetV1, _Mapping]] = ..., target_resolution: _Optional[_Union[ProductionRulePreviewTargetResolutionV1, str]] = ..., target_resolution_reason_code: _Optional[str] = ..., dispatch_count_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., estimated_dispatch_count: _Optional[int] = ..., promotion: _Optional[_Union[ProductionRulePreviewPromotionImplicationV1, _Mapping]] = ..., review: _Optional[_Union[ProductionRulePreviewReviewImplicationV1, _Mapping]] = ..., linked_evaluation: _Optional[_Union[ProductionRulePreviewLinkedEvaluationImplicationV1, _Mapping]] = ..., notify: _Optional[_Union[ProductionRulePreviewNotifyImplicationV1, _Mapping]] = ..., release_block: _Optional[_Union[ProductionRulePreviewReleaseBlockImplicationV1, _Mapping]] = ...) -> None: ...

class ProductionRulePreviewZeroMatchV1(_message.Message):
    __slots__ = ("is_zero_match", "reason", "detail")
    IS_ZERO_MATCH_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    is_zero_match: bool
    reason: ProductionRulePreviewZeroMatchReasonV1
    detail: str
    def __init__(self, is_zero_match: _Optional[bool] = ..., reason: _Optional[_Union[ProductionRulePreviewZeroMatchReasonV1, str]] = ..., detail: _Optional[str] = ...) -> None: ...

class ProductionRulePreviewWarningV1(_message.Message):
    __slots__ = ("reason_code", "detail", "action_ordinal", "action_kind")
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    ACTION_ORDINAL_FIELD_NUMBER: _ClassVar[int]
    ACTION_KIND_FIELD_NUMBER: _ClassVar[int]
    reason_code: str
    detail: str
    action_ordinal: int
    action_kind: ProductionRuleActionKindV1
    def __init__(self, reason_code: _Optional[str] = ..., detail: _Optional[str] = ..., action_ordinal: _Optional[int] = ..., action_kind: _Optional[_Union[ProductionRuleActionKindV1, str]] = ...) -> None: ...

class ProductionRulePreviewSubjectV1(_message.Message):
    __slots__ = ("rule_id", "version_id", "version_number", "evaluated_state", "is_draft", "draft_content_digest", "effective_sampling_rate_percent")
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    EVALUATED_STATE_FIELD_NUMBER: _ClassVar[int]
    IS_DRAFT_FIELD_NUMBER: _ClassVar[int]
    DRAFT_CONTENT_DIGEST_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_SAMPLING_RATE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    rule_id: str
    version_id: str
    version_number: int
    evaluated_state: ProductionRuleVersionStateV1
    is_draft: bool
    draft_content_digest: str
    effective_sampling_rate_percent: float
    def __init__(self, rule_id: _Optional[str] = ..., version_id: _Optional[str] = ..., version_number: _Optional[int] = ..., evaluated_state: _Optional[_Union[ProductionRuleVersionStateV1, str]] = ..., is_draft: _Optional[bool] = ..., draft_content_digest: _Optional[str] = ..., effective_sampling_rate_percent: _Optional[float] = ...) -> None: ...

class ProductionRulePreviewOfferV1(_message.Message):
    __slots__ = ("match_key", "predicted_admission", "reason_code", "sampling_bucket_percent", "observed_at")
    MATCH_KEY_FIELD_NUMBER: _ClassVar[int]
    PREDICTED_ADMISSION_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    SAMPLING_BUCKET_PERCENT_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    match_key: str
    predicted_admission: ProductionWorkflowAdmissionV1
    reason_code: str
    sampling_bucket_percent: float
    observed_at: _timestamp_pb2.Timestamp
    def __init__(self, match_key: _Optional[str] = ..., predicted_admission: _Optional[_Union[ProductionWorkflowAdmissionV1, str]] = ..., reason_code: _Optional[str] = ..., sampling_bucket_percent: _Optional[float] = ..., observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PreviewProductionEvaluationRuleResponse(_message.Message):
    __slots__ = ("subject", "window", "buckets", "estimate", "budget_posture", "action_candidates", "zero_match", "warnings", "offers", "freshness", "capabilities")
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    BUCKETS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    BUDGET_POSTURE_FIELD_NUMBER: _ClassVar[int]
    ACTION_CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    ZERO_MATCH_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    OFFERS_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    subject: ProductionRulePreviewSubjectV1
    window: ProductionRulePreviewWindowV1
    buckets: ProductionRulePreviewBucketsV1
    estimate: ProductionRulePreviewEstimateV1
    budget_posture: ProductionRulePreviewBudgetPostureV1
    action_candidates: _containers.RepeatedCompositeFieldContainer[ProductionRulePreviewActionCandidateV1]
    zero_match: ProductionRulePreviewZeroMatchV1
    warnings: _containers.RepeatedCompositeFieldContainer[ProductionRulePreviewWarningV1]
    offers: _containers.RepeatedCompositeFieldContainer[ProductionRulePreviewOfferV1]
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, subject: _Optional[_Union[ProductionRulePreviewSubjectV1, _Mapping]] = ..., window: _Optional[_Union[ProductionRulePreviewWindowV1, _Mapping]] = ..., buckets: _Optional[_Union[ProductionRulePreviewBucketsV1, _Mapping]] = ..., estimate: _Optional[_Union[ProductionRulePreviewEstimateV1, _Mapping]] = ..., budget_posture: _Optional[_Union[ProductionRulePreviewBudgetPostureV1, _Mapping]] = ..., action_candidates: _Optional[_Iterable[_Union[ProductionRulePreviewActionCandidateV1, _Mapping]]] = ..., zero_match: _Optional[_Union[ProductionRulePreviewZeroMatchV1, _Mapping]] = ..., warnings: _Optional[_Iterable[_Union[ProductionRulePreviewWarningV1, _Mapping]]] = ..., offers: _Optional[_Iterable[_Union[ProductionRulePreviewOfferV1, _Mapping]]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class ProductionRulePreviewRefusalV1(_message.Message):
    __slots__ = ("kind", "reason_code", "recovery", "detail", "action_ordinal", "limit_value")
    KIND_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    ACTION_ORDINAL_FIELD_NUMBER: _ClassVar[int]
    LIMIT_VALUE_FIELD_NUMBER: _ClassVar[int]
    kind: ProductionRulePreviewRefusalKindV1
    reason_code: str
    recovery: RecoveryActionV1
    detail: str
    action_ordinal: int
    limit_value: int
    def __init__(self, kind: _Optional[_Union[ProductionRulePreviewRefusalKindV1, str]] = ..., reason_code: _Optional[str] = ..., recovery: _Optional[_Union[RecoveryActionV1, str]] = ..., detail: _Optional[str] = ..., action_ordinal: _Optional[int] = ..., limit_value: _Optional[int] = ...) -> None: ...

class MachinePrincipalV1(_message.Message):
    __slots__ = ("machine_principal_id", "tenant_id", "org_id", "display_name", "description", "scopes", "state", "created_by", "created_at", "updated_at", "last_used_at")
    MACHINE_PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_AT_FIELD_NUMBER: _ClassVar[int]
    machine_principal_id: str
    tenant_id: str
    org_id: str
    display_name: str
    description: str
    scopes: _containers.RepeatedScalarFieldContainer[MachinePrincipalScopeV1]
    state: MachinePrincipalStateV1
    created_by: PrincipalRefV1
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    last_used_at: _timestamp_pb2.Timestamp
    def __init__(self, machine_principal_id: _Optional[str] = ..., tenant_id: _Optional[str] = ..., org_id: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., scopes: _Optional[_Iterable[_Union[MachinePrincipalScopeV1, str]]] = ..., state: _Optional[_Union[MachinePrincipalStateV1, str]] = ..., created_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_used_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MachineCredentialV1(_message.Message):
    __slots__ = ("credential_id", "machine_principal_id", "tenant_id", "org_id", "secret_ref", "token_prefix", "version_number", "state", "expires_at", "created_by", "created_at", "revoked_by", "revoked_at", "revoke_reason")
    CREDENTIAL_ID_FIELD_NUMBER: _ClassVar[int]
    MACHINE_PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_REF_FIELD_NUMBER: _ClassVar[int]
    TOKEN_PREFIX_FIELD_NUMBER: _ClassVar[int]
    VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    REVOKED_BY_FIELD_NUMBER: _ClassVar[int]
    REVOKED_AT_FIELD_NUMBER: _ClassVar[int]
    REVOKE_REASON_FIELD_NUMBER: _ClassVar[int]
    credential_id: str
    machine_principal_id: str
    tenant_id: str
    org_id: str
    secret_ref: str
    token_prefix: str
    version_number: int
    state: MachineCredentialStateV1
    expires_at: _timestamp_pb2.Timestamp
    created_by: PrincipalRefV1
    created_at: _timestamp_pb2.Timestamp
    revoked_by: PrincipalRefV1
    revoked_at: _timestamp_pb2.Timestamp
    revoke_reason: str
    def __init__(self, credential_id: _Optional[str] = ..., machine_principal_id: _Optional[str] = ..., tenant_id: _Optional[str] = ..., org_id: _Optional[str] = ..., secret_ref: _Optional[str] = ..., token_prefix: _Optional[str] = ..., version_number: _Optional[int] = ..., state: _Optional[_Union[MachineCredentialStateV1, str]] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., revoked_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., revoked_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., revoke_reason: _Optional[str] = ...) -> None: ...

class CreateMachinePrincipalRequest(_message.Message):
    __slots__ = ("display_name", "description", "scopes")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    description: str
    scopes: _containers.RepeatedScalarFieldContainer[MachinePrincipalScopeV1]
    def __init__(self, display_name: _Optional[str] = ..., description: _Optional[str] = ..., scopes: _Optional[_Iterable[_Union[MachinePrincipalScopeV1, str]]] = ...) -> None: ...

class CreateMachinePrincipalResponse(_message.Message):
    __slots__ = ("principal",)
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    principal: MachinePrincipalV1
    def __init__(self, principal: _Optional[_Union[MachinePrincipalV1, _Mapping]] = ...) -> None: ...

class ListMachinePrincipalsRequest(_message.Message):
    __slots__ = ("page_size", "page_token")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class MachinePrincipalWithCredentialsV1(_message.Message):
    __slots__ = ("principal", "credentials")
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    principal: MachinePrincipalV1
    credentials: _containers.RepeatedCompositeFieldContainer[MachineCredentialV1]
    def __init__(self, principal: _Optional[_Union[MachinePrincipalV1, _Mapping]] = ..., credentials: _Optional[_Iterable[_Union[MachineCredentialV1, _Mapping]]] = ...) -> None: ...

class ListMachinePrincipalsResponse(_message.Message):
    __slots__ = ("principals", "next_page_token")
    PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    principals: _containers.RepeatedCompositeFieldContainer[MachinePrincipalWithCredentialsV1]
    next_page_token: str
    def __init__(self, principals: _Optional[_Iterable[_Union[MachinePrincipalWithCredentialsV1, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateMachineCredentialRequest(_message.Message):
    __slots__ = ("machine_principal_id", "description", "expires_at")
    MACHINE_PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    machine_principal_id: str
    description: str
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, machine_principal_id: _Optional[str] = ..., description: _Optional[str] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateMachineCredentialResponse(_message.Message):
    __slots__ = ("credential", "plaintext_token_once")
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    PLAINTEXT_TOKEN_ONCE_FIELD_NUMBER: _ClassVar[int]
    credential: MachineCredentialV1
    plaintext_token_once: str
    def __init__(self, credential: _Optional[_Union[MachineCredentialV1, _Mapping]] = ..., plaintext_token_once: _Optional[str] = ...) -> None: ...

class RevokeMachineCredentialRequest(_message.Message):
    __slots__ = ("credential_id", "revoke_reason")
    CREDENTIAL_ID_FIELD_NUMBER: _ClassVar[int]
    REVOKE_REASON_FIELD_NUMBER: _ClassVar[int]
    credential_id: str
    revoke_reason: str
    def __init__(self, credential_id: _Optional[str] = ..., revoke_reason: _Optional[str] = ...) -> None: ...

class RevokeMachineCredentialResponse(_message.Message):
    __slots__ = ("credential",)
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    credential: MachineCredentialV1
    def __init__(self, credential: _Optional[_Union[MachineCredentialV1, _Mapping]] = ...) -> None: ...

class RevokeMachinePrincipalRequest(_message.Message):
    __slots__ = ("machine_principal_id", "revoke_reason")
    MACHINE_PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    REVOKE_REASON_FIELD_NUMBER: _ClassVar[int]
    machine_principal_id: str
    revoke_reason: str
    def __init__(self, machine_principal_id: _Optional[str] = ..., revoke_reason: _Optional[str] = ...) -> None: ...

class RevokeMachinePrincipalResponse(_message.Message):
    __slots__ = ("principal", "revoked_credentials")
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    REVOKED_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    principal: MachinePrincipalV1
    revoked_credentials: _containers.RepeatedCompositeFieldContainer[MachineCredentialV1]
    def __init__(self, principal: _Optional[_Union[MachinePrincipalV1, _Mapping]] = ..., revoked_credentials: _Optional[_Iterable[_Union[MachineCredentialV1, _Mapping]]] = ...) -> None: ...

class GetCallerPrincipalRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCallerPrincipalResponse(_message.Message):
    __slots__ = ("caller", "tenant_id", "org_id", "machine_principal", "credential")
    CALLER_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    MACHINE_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    caller: PrincipalRefV1
    tenant_id: str
    org_id: str
    machine_principal: MachinePrincipalV1
    credential: MachineCredentialV1
    def __init__(self, caller: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., tenant_id: _Optional[str] = ..., org_id: _Optional[str] = ..., machine_principal: _Optional[_Union[MachinePrincipalV1, _Mapping]] = ..., credential: _Optional[_Union[MachineCredentialV1, _Mapping]] = ...) -> None: ...

class ExternalCaseLeaseV1(_message.Message):
    __slots__ = ("lease_id", "lease_token", "expires_at", "renewals_used", "renewals_remaining", "case_count")
    LEASE_ID_FIELD_NUMBER: _ClassVar[int]
    LEASE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    RENEWALS_USED_FIELD_NUMBER: _ClassVar[int]
    RENEWALS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    lease_id: str
    lease_token: str
    expires_at: _timestamp_pb2.Timestamp
    renewals_used: int
    renewals_remaining: int
    case_count: int
    def __init__(self, lease_id: _Optional[str] = ..., lease_token: _Optional[str] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., renewals_used: _Optional[int] = ..., renewals_remaining: _Optional[int] = ..., case_count: _Optional[int] = ...) -> None: ...

class LeasedEvaluationCaseV1(_message.Message):
    __slots__ = ("cohort_key", "candidate_key", "case_revision_id", "trial", "attempt_generation", "input_payload_json", "expected_output_json", "submission_deadline_at")
    COHORT_KEY_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    CASE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    TRIAL_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_GENERATION_FIELD_NUMBER: _ClassVar[int]
    INPUT_PAYLOAD_JSON_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUT_JSON_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_DEADLINE_AT_FIELD_NUMBER: _ClassVar[int]
    cohort_key: str
    candidate_key: str
    case_revision_id: str
    trial: int
    attempt_generation: int
    input_payload_json: str
    expected_output_json: str
    submission_deadline_at: _timestamp_pb2.Timestamp
    def __init__(self, cohort_key: _Optional[str] = ..., candidate_key: _Optional[str] = ..., case_revision_id: _Optional[str] = ..., trial: _Optional[int] = ..., attempt_generation: _Optional[int] = ..., input_payload_json: _Optional[str] = ..., expected_output_json: _Optional[str] = ..., submission_deadline_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ExternalCaseFailureV1(_message.Message):
    __slots__ = ("code", "sanitized_message")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SANITIZED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: str
    sanitized_message: str
    def __init__(self, code: _Optional[str] = ..., sanitized_message: _Optional[str] = ...) -> None: ...

class ExternalCaseUsageV1(_message.Message):
    __slots__ = ("input_tokens", "output_tokens", "total_tokens", "latency_micros", "retry_count", "reported_cost_micros")
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TOKENS_FIELD_NUMBER: _ClassVar[int]
    LATENCY_MICROS_FIELD_NUMBER: _ClassVar[int]
    RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    REPORTED_COST_MICROS_FIELD_NUMBER: _ClassVar[int]
    input_tokens: int
    output_tokens: int
    total_tokens: int
    latency_micros: int
    retry_count: int
    reported_cost_micros: int
    def __init__(self, input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., total_tokens: _Optional[int] = ..., latency_micros: _Optional[int] = ..., retry_count: _Optional[int] = ..., reported_cost_micros: _Optional[int] = ...) -> None: ...

class ExternalCaseOutputV1(_message.Message):
    __slots__ = ("cohort_key", "candidate_key", "case_revision_id", "trial", "attempt_generation", "output_payload_json", "failure", "usage")
    COHORT_KEY_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    CASE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    TRIAL_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_GENERATION_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_PAYLOAD_JSON_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    cohort_key: str
    candidate_key: str
    case_revision_id: str
    trial: int
    attempt_generation: int
    output_payload_json: str
    failure: ExternalCaseFailureV1
    usage: ExternalCaseUsageV1
    def __init__(self, cohort_key: _Optional[str] = ..., candidate_key: _Optional[str] = ..., case_revision_id: _Optional[str] = ..., trial: _Optional[int] = ..., attempt_generation: _Optional[int] = ..., output_payload_json: _Optional[str] = ..., failure: _Optional[_Union[ExternalCaseFailureV1, _Mapping]] = ..., usage: _Optional[_Union[ExternalCaseUsageV1, _Mapping]] = ...) -> None: ...

class ExternalCaseOutputAckV1(_message.Message):
    __slots__ = ("cohort_key", "candidate_key", "case_revision_id", "trial", "kind", "observed_state", "rejection")
    COHORT_KEY_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    CASE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    TRIAL_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_STATE_FIELD_NUMBER: _ClassVar[int]
    REJECTION_FIELD_NUMBER: _ClassVar[int]
    cohort_key: str
    candidate_key: str
    case_revision_id: str
    trial: int
    kind: ExternalSubmissionAckKindV1
    observed_state: EvaluationExecutionStateV1
    rejection: EvaluationFailureV1
    def __init__(self, cohort_key: _Optional[str] = ..., candidate_key: _Optional[str] = ..., case_revision_id: _Optional[str] = ..., trial: _Optional[int] = ..., kind: _Optional[_Union[ExternalSubmissionAckKindV1, str]] = ..., observed_state: _Optional[_Union[EvaluationExecutionStateV1, str]] = ..., rejection: _Optional[_Union[EvaluationFailureV1, _Mapping]] = ...) -> None: ...

class ExternalLeaseRefusalV1(_message.Message):
    __slots__ = ("kind", "message", "missing_scope", "recovery")
    KIND_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MISSING_SCOPE_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_FIELD_NUMBER: _ClassVar[int]
    kind: ExternalLeaseRefusalKindV1
    message: str
    missing_scope: str
    recovery: RecoveryActionV1
    def __init__(self, kind: _Optional[_Union[ExternalLeaseRefusalKindV1, str]] = ..., message: _Optional[str] = ..., missing_scope: _Optional[str] = ..., recovery: _Optional[_Union[RecoveryActionV1, str]] = ...) -> None: ...

class LeaseEvaluationCasesRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "candidate_key", "runtime_key", "max_cases", "lease_seconds")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_KEY_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_KEY_FIELD_NUMBER: _ClassVar[int]
    MAX_CASES_FIELD_NUMBER: _ClassVar[int]
    LEASE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    candidate_key: str
    runtime_key: str
    max_cases: int
    lease_seconds: int
    def __init__(self, evaluation_run_id: _Optional[str] = ..., candidate_key: _Optional[str] = ..., runtime_key: _Optional[str] = ..., max_cases: _Optional[int] = ..., lease_seconds: _Optional[int] = ...) -> None: ...

class LeaseEvaluationCasesResponse(_message.Message):
    __slots__ = ("lease", "cases", "remaining_unleased_case_count", "refusal", "capabilities", "freshness")
    LEASE_FIELD_NUMBER: _ClassVar[int]
    CASES_FIELD_NUMBER: _ClassVar[int]
    REMAINING_UNLEASED_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    lease: ExternalCaseLeaseV1
    cases: _containers.RepeatedCompositeFieldContainer[LeasedEvaluationCaseV1]
    remaining_unleased_case_count: int
    refusal: ExternalLeaseRefusalV1
    capabilities: AgenticEvaluationCapabilitiesV1
    freshness: EvaluationFreshnessV1
    def __init__(self, lease: _Optional[_Union[ExternalCaseLeaseV1, _Mapping]] = ..., cases: _Optional[_Iterable[_Union[LeasedEvaluationCaseV1, _Mapping]]] = ..., remaining_unleased_case_count: _Optional[int] = ..., refusal: _Optional[_Union[ExternalLeaseRefusalV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class RenewEvaluationCaseLeaseRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "lease_id", "lease_token", "lease_seconds")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    LEASE_ID_FIELD_NUMBER: _ClassVar[int]
    LEASE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LEASE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    lease_id: str
    lease_token: str
    lease_seconds: int
    def __init__(self, evaluation_run_id: _Optional[str] = ..., lease_id: _Optional[str] = ..., lease_token: _Optional[str] = ..., lease_seconds: _Optional[int] = ...) -> None: ...

class RenewEvaluationCaseLeaseResponse(_message.Message):
    __slots__ = ("lease", "refusal", "capabilities")
    LEASE_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    lease: ExternalCaseLeaseV1
    refusal: ExternalLeaseRefusalV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, lease: _Optional[_Union[ExternalCaseLeaseV1, _Mapping]] = ..., refusal: _Optional[_Union[ExternalLeaseRefusalV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class SubmitEvaluationCaseOutputsRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "lease_id", "lease_token", "outputs", "idempotency_key")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    LEASE_ID_FIELD_NUMBER: _ClassVar[int]
    LEASE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    lease_id: str
    lease_token: str
    outputs: _containers.RepeatedCompositeFieldContainer[ExternalCaseOutputV1]
    idempotency_key: str
    def __init__(self, evaluation_run_id: _Optional[str] = ..., lease_id: _Optional[str] = ..., lease_token: _Optional[str] = ..., outputs: _Optional[_Iterable[_Union[ExternalCaseOutputV1, _Mapping]]] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class SubmitEvaluationCaseOutputsResponse(_message.Message):
    __slots__ = ("acks", "accepted_count", "already_submitted_count", "rejected_count", "lease", "remaining_leased_case_count", "refusal", "capabilities")
    ACKS_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    ALREADY_SUBMITTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    REJECTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    LEASE_FIELD_NUMBER: _ClassVar[int]
    REMAINING_LEASED_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    acks: _containers.RepeatedCompositeFieldContainer[ExternalCaseOutputAckV1]
    accepted_count: int
    already_submitted_count: int
    rejected_count: int
    lease: ExternalCaseLeaseV1
    remaining_leased_case_count: int
    refusal: ExternalLeaseRefusalV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, acks: _Optional[_Iterable[_Union[ExternalCaseOutputAckV1, _Mapping]]] = ..., accepted_count: _Optional[int] = ..., already_submitted_count: _Optional[int] = ..., rejected_count: _Optional[int] = ..., lease: _Optional[_Union[ExternalCaseLeaseV1, _Mapping]] = ..., remaining_leased_case_count: _Optional[int] = ..., refusal: _Optional[_Union[ExternalLeaseRefusalV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class ReleaseEvaluationCaseLeaseRequest(_message.Message):
    __slots__ = ("evaluation_run_id", "lease_id", "lease_token")
    EVALUATION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    LEASE_ID_FIELD_NUMBER: _ClassVar[int]
    LEASE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    evaluation_run_id: str
    lease_id: str
    lease_token: str
    def __init__(self, evaluation_run_id: _Optional[str] = ..., lease_id: _Optional[str] = ..., lease_token: _Optional[str] = ...) -> None: ...

class ReleaseEvaluationCaseLeaseResponse(_message.Message):
    __slots__ = ("released_case_count", "refusal", "capabilities")
    RELEASED_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    released_case_count: int
    refusal: ExternalLeaseRefusalV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, released_case_count: _Optional[int] = ..., refusal: _Optional[_Union[ExternalLeaseRefusalV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class PlatformAnnotationLinkV1(_message.Message):
    __slots__ = ("kind", "ref")
    KIND_FIELD_NUMBER: _ClassVar[int]
    REF_FIELD_NUMBER: _ClassVar[int]
    kind: PlatformAnnotationLinkKindV1
    ref: str
    def __init__(self, kind: _Optional[_Union[PlatformAnnotationLinkKindV1, str]] = ..., ref: _Optional[str] = ...) -> None: ...

class PlatformAnnotationAttributeV1(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class PlatformAnnotationV1(_message.Message):
    __slots__ = ("annotation_id", "org_id", "kind", "title", "start_at", "end_at", "attributes", "links", "recorded_by", "recorded_at", "idempotency_key")
    ANNOTATION_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    START_AT_FIELD_NUMBER: _ClassVar[int]
    END_AT_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    RECORDED_BY_FIELD_NUMBER: _ClassVar[int]
    RECORDED_AT_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    annotation_id: str
    org_id: str
    kind: PlatformAnnotationKindV1
    title: str
    start_at: _timestamp_pb2.Timestamp
    end_at: _timestamp_pb2.Timestamp
    attributes: _containers.RepeatedCompositeFieldContainer[PlatformAnnotationAttributeV1]
    links: _containers.RepeatedCompositeFieldContainer[PlatformAnnotationLinkV1]
    recorded_by: PrincipalRefV1
    recorded_at: _timestamp_pb2.Timestamp
    idempotency_key: str
    def __init__(self, annotation_id: _Optional[str] = ..., org_id: _Optional[str] = ..., kind: _Optional[_Union[PlatformAnnotationKindV1, str]] = ..., title: _Optional[str] = ..., start_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., attributes: _Optional[_Iterable[_Union[PlatformAnnotationAttributeV1, _Mapping]]] = ..., links: _Optional[_Iterable[_Union[PlatformAnnotationLinkV1, _Mapping]]] = ..., recorded_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., recorded_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class PlatformAnnotationRejectionV1(_message.Message):
    __slots__ = ("reason", "field", "limit_value", "supported_kinds")
    REASON_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    LIMIT_VALUE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_KINDS_FIELD_NUMBER: _ClassVar[int]
    reason: PlatformAnnotationRejectionReasonV1
    field: str
    limit_value: int
    supported_kinds: _containers.RepeatedScalarFieldContainer[PlatformAnnotationKindV1]
    def __init__(self, reason: _Optional[_Union[PlatformAnnotationRejectionReasonV1, str]] = ..., field: _Optional[str] = ..., limit_value: _Optional[int] = ..., supported_kinds: _Optional[_Iterable[_Union[PlatformAnnotationKindV1, str]]] = ...) -> None: ...

class RecordPlatformAnnotationRequest(_message.Message):
    __slots__ = ("kind", "title", "start_at", "end_at", "attributes", "links", "idempotency_key")
    KIND_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    START_AT_FIELD_NUMBER: _ClassVar[int]
    END_AT_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    kind: PlatformAnnotationKindV1
    title: str
    start_at: _timestamp_pb2.Timestamp
    end_at: _timestamp_pb2.Timestamp
    attributes: _containers.RepeatedCompositeFieldContainer[PlatformAnnotationAttributeV1]
    links: _containers.RepeatedCompositeFieldContainer[PlatformAnnotationLinkV1]
    idempotency_key: str
    def __init__(self, kind: _Optional[_Union[PlatformAnnotationKindV1, str]] = ..., title: _Optional[str] = ..., start_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., attributes: _Optional[_Iterable[_Union[PlatformAnnotationAttributeV1, _Mapping]]] = ..., links: _Optional[_Iterable[_Union[PlatformAnnotationLinkV1, _Mapping]]] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class RecordPlatformAnnotationResponse(_message.Message):
    __slots__ = ("annotation", "idempotent_replay", "capabilities")
    ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    annotation: PlatformAnnotationV1
    idempotent_replay: bool
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, annotation: _Optional[_Union[PlatformAnnotationV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class ListPlatformAnnotationsRequest(_message.Message):
    __slots__ = ("window_start", "window_end", "kinds", "page")
    WINDOW_START_FIELD_NUMBER: _ClassVar[int]
    WINDOW_END_FIELD_NUMBER: _ClassVar[int]
    KINDS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    window_start: _timestamp_pb2.Timestamp
    window_end: _timestamp_pb2.Timestamp
    kinds: _containers.RepeatedScalarFieldContainer[PlatformAnnotationKindV1]
    page: _common_pb2.PageRequestV1
    def __init__(self, window_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., window_end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., kinds: _Optional[_Iterable[_Union[PlatformAnnotationKindV1, str]]] = ..., page: _Optional[_Union[_common_pb2.PageRequestV1, _Mapping]] = ...) -> None: ...

class ListPlatformAnnotationsResponse(_message.Message):
    __slots__ = ("annotations", "page", "capabilities", "resync")
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    RESYNC_FIELD_NUMBER: _ClassVar[int]
    annotations: _containers.RepeatedCompositeFieldContainer[PlatformAnnotationV1]
    page: _common_pb2.PageResponseV1
    capabilities: AgenticEvaluationCapabilitiesV1
    resync: EvaluationCursorResyncV1
    def __init__(self, annotations: _Optional[_Iterable[_Union[PlatformAnnotationV1, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponseV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., resync: _Optional[_Union[EvaluationCursorResyncV1, _Mapping]] = ...) -> None: ...

class EvaluationScorerConfigSummaryV1(_message.Message):
    __slots__ = ("score_config_id", "config_key", "name", "description", "metric_name", "success_dimension", "kind", "version_discriminator", "version_count", "version_count_availability", "weight", "is_blocking_gate", "is_archived", "archived_at", "authored_on_this_surface", "created_at", "updated_at", "created_by")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    VERSION_DISCRIMINATOR_FIELD_NUMBER: _ClassVar[int]
    VERSION_COUNT_FIELD_NUMBER: _ClassVar[int]
    VERSION_COUNT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    IS_BLOCKING_GATE_FIELD_NUMBER: _ClassVar[int]
    IS_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_AT_FIELD_NUMBER: _ClassVar[int]
    AUTHORED_ON_THIS_SURFACE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    config_key: str
    name: str
    description: str
    metric_name: str
    success_dimension: str
    kind: EvaluationScorerKindV1
    version_discriminator: str
    version_count: int
    version_count_availability: MetricAvailabilityV1
    weight: float
    is_blocking_gate: bool
    is_archived: bool
    archived_at: _timestamp_pb2.Timestamp
    authored_on_this_surface: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    created_by: PrincipalRefV1
    def __init__(self, score_config_id: _Optional[str] = ..., config_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., metric_name: _Optional[str] = ..., success_dimension: _Optional[str] = ..., kind: _Optional[_Union[EvaluationScorerKindV1, str]] = ..., version_discriminator: _Optional[str] = ..., version_count: _Optional[int] = ..., version_count_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., weight: _Optional[float] = ..., is_blocking_gate: _Optional[bool] = ..., is_archived: _Optional[bool] = ..., archived_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., authored_on_this_surface: _Optional[bool] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ...) -> None: ...

class ListEvaluationScorerConfigsRequest(_message.Message):
    __slots__ = ("page", "kind_filter", "archived_filter")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    KIND_FILTER_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FILTER_FIELD_NUMBER: _ClassVar[int]
    page: _common_pb2.PageRequestV1
    kind_filter: _containers.RepeatedScalarFieldContainer[EvaluationScorerKindV1]
    archived_filter: EvaluationScorerArchivedFilterV1
    def __init__(self, page: _Optional[_Union[_common_pb2.PageRequestV1, _Mapping]] = ..., kind_filter: _Optional[_Iterable[_Union[EvaluationScorerKindV1, str]]] = ..., archived_filter: _Optional[_Union[EvaluationScorerArchivedFilterV1, str]] = ...) -> None: ...

class ListEvaluationScorerConfigsResponse(_message.Message):
    __slots__ = ("scorer_configs", "page", "freshness", "capabilities", "resync")
    SCORER_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    RESYNC_FIELD_NUMBER: _ClassVar[int]
    scorer_configs: _containers.RepeatedCompositeFieldContainer[EvaluationScorerConfigSummaryV1]
    page: _common_pb2.PageResponseV1
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    resync: EvaluationCursorResyncV1
    def __init__(self, scorer_configs: _Optional[_Iterable[_Union[EvaluationScorerConfigSummaryV1, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponseV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., resync: _Optional[_Union[EvaluationCursorResyncV1, _Mapping]] = ...) -> None: ...

class EvaluationScorerJudgeEffectiveSettingsV1(_message.Message):
    __slots__ = ("max_output_tokens", "temperature", "top_p", "anthropic_version")
    MAX_OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TOP_P_FIELD_NUMBER: _ClassVar[int]
    ANTHROPIC_VERSION_FIELD_NUMBER: _ClassVar[int]
    max_output_tokens: int
    temperature: float
    top_p: float
    anthropic_version: str
    def __init__(self, max_output_tokens: _Optional[int] = ..., temperature: _Optional[float] = ..., top_p: _Optional[float] = ..., anthropic_version: _Optional[str] = ...) -> None: ...

class EvaluationScorerJudgeResolvedExecutionV1(_message.Message):
    __slots__ = ("provider", "model_id", "credential_ref", "provider_endpoint_ref", "reasoning_enabled", "effective_request_settings")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_REF_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ENDPOINT_REF_FIELD_NUMBER: _ClassVar[int]
    REASONING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_REQUEST_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    provider: _agentic_pb2.ProviderNameV1
    model_id: str
    credential_ref: str
    provider_endpoint_ref: str
    reasoning_enabled: bool
    effective_request_settings: EvaluationScorerJudgeEffectiveSettingsV1
    def __init__(self, provider: _Optional[_Union[_agentic_pb2.ProviderNameV1, str]] = ..., model_id: _Optional[str] = ..., credential_ref: _Optional[str] = ..., provider_endpoint_ref: _Optional[str] = ..., reasoning_enabled: _Optional[bool] = ..., effective_request_settings: _Optional[_Union[EvaluationScorerJudgeEffectiveSettingsV1, _Mapping]] = ...) -> None: ...

class EvaluationScorerJudgeDetailV1(_message.Message):
    __slots__ = ("rubric_content", "provider_execution", "pass_threshold")
    RUBRIC_CONTENT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    PASS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    rubric_content: EvaluationScorerJudgeRubricV1
    provider_execution: EvaluationScorerJudgeResolvedExecutionV1
    pass_threshold: float
    def __init__(self, rubric_content: _Optional[_Union[EvaluationScorerJudgeRubricV1, _Mapping]] = ..., provider_execution: _Optional[_Union[EvaluationScorerJudgeResolvedExecutionV1, _Mapping]] = ..., pass_threshold: _Optional[float] = ...) -> None: ...

class EvaluationScorerConfigDetailV1(_message.Message):
    __slots__ = ("score_config_id", "config_key", "name", "description", "metric_name", "success_dimension", "kind", "version_discriminator", "weight", "is_blocking_gate", "is_archived", "archived_at", "deterministic", "review_policy", "judge", "pass_threshold", "authored_on_this_surface", "version_count", "version_count_availability", "evaluator_template_id", "created_at", "updated_at", "created_by", "pinned_run_count", "pinned_run_id")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    VERSION_DISCRIMINATOR_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    IS_BLOCKING_GATE_FIELD_NUMBER: _ClassVar[int]
    IS_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_AT_FIELD_NUMBER: _ClassVar[int]
    DETERMINISTIC_FIELD_NUMBER: _ClassVar[int]
    REVIEW_POLICY_FIELD_NUMBER: _ClassVar[int]
    JUDGE_FIELD_NUMBER: _ClassVar[int]
    PASS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    AUTHORED_ON_THIS_SURFACE_FIELD_NUMBER: _ClassVar[int]
    VERSION_COUNT_FIELD_NUMBER: _ClassVar[int]
    VERSION_COUNT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    PINNED_RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    PINNED_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    config_key: str
    name: str
    description: str
    metric_name: str
    success_dimension: str
    kind: EvaluationScorerKindV1
    version_discriminator: str
    weight: float
    is_blocking_gate: bool
    is_archived: bool
    archived_at: _timestamp_pb2.Timestamp
    deterministic: EvaluationScorerDeterministicSpecV1
    review_policy: EvaluationScorerReviewPolicySpecV1
    judge: EvaluationScorerJudgeDetailV1
    pass_threshold: float
    authored_on_this_surface: bool
    version_count: int
    version_count_availability: MetricAvailabilityV1
    evaluator_template_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    created_by: PrincipalRefV1
    pinned_run_count: int
    pinned_run_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, score_config_id: _Optional[str] = ..., config_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., metric_name: _Optional[str] = ..., success_dimension: _Optional[str] = ..., kind: _Optional[_Union[EvaluationScorerKindV1, str]] = ..., version_discriminator: _Optional[str] = ..., weight: _Optional[float] = ..., is_blocking_gate: _Optional[bool] = ..., is_archived: _Optional[bool] = ..., archived_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., deterministic: _Optional[_Union[EvaluationScorerDeterministicSpecV1, _Mapping]] = ..., review_policy: _Optional[_Union[EvaluationScorerReviewPolicySpecV1, _Mapping]] = ..., judge: _Optional[_Union[EvaluationScorerJudgeDetailV1, _Mapping]] = ..., pass_threshold: _Optional[float] = ..., authored_on_this_surface: _Optional[bool] = ..., version_count: _Optional[int] = ..., version_count_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., evaluator_template_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., pinned_run_count: _Optional[int] = ..., pinned_run_id: _Optional[_Iterable[str]] = ...) -> None: ...

class EvaluationScorerConfigUsageV1(_message.Message):
    __slots__ = ("suite", "suite_count", "suite_availability", "pinned_run_count", "pinned_run_id", "pinned_run_availability", "definition_count", "definition_availability", "production_rule_count", "production_rule_availability")
    SUITE_FIELD_NUMBER: _ClassVar[int]
    SUITE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUITE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    PINNED_RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    PINNED_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    PINNED_RUN_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_COUNT_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    PRODUCTION_RULE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PRODUCTION_RULE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    suite: _containers.RepeatedCompositeFieldContainer[EvaluationScorerSuiteRefV1]
    suite_count: int
    suite_availability: MetricAvailabilityV1
    pinned_run_count: int
    pinned_run_id: _containers.RepeatedScalarFieldContainer[str]
    pinned_run_availability: MetricAvailabilityV1
    definition_count: int
    definition_availability: MetricAvailabilityV1
    production_rule_count: int
    production_rule_availability: MetricAvailabilityV1
    def __init__(self, suite: _Optional[_Iterable[_Union[EvaluationScorerSuiteRefV1, _Mapping]]] = ..., suite_count: _Optional[int] = ..., suite_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., pinned_run_count: _Optional[int] = ..., pinned_run_id: _Optional[_Iterable[str]] = ..., pinned_run_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., definition_count: _Optional[int] = ..., definition_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., production_rule_count: _Optional[int] = ..., production_rule_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class EvaluationScorerSuiteRefV1(_message.Message):
    __slots__ = ("scorer_suite_id", "suite_key", "is_archived", "is_blocking_gate", "weight")
    SCORER_SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    SUITE_KEY_FIELD_NUMBER: _ClassVar[int]
    IS_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    IS_BLOCKING_GATE_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    scorer_suite_id: str
    suite_key: str
    is_archived: bool
    is_blocking_gate: bool
    weight: float
    def __init__(self, scorer_suite_id: _Optional[str] = ..., suite_key: _Optional[str] = ..., is_archived: _Optional[bool] = ..., is_blocking_gate: _Optional[bool] = ..., weight: _Optional[float] = ...) -> None: ...

class GetEvaluationScorerConfigRequest(_message.Message):
    __slots__ = ("score_config_id", "config_key", "version_discriminator")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_DISCRIMINATOR_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    config_key: str
    version_discriminator: str
    def __init__(self, score_config_id: _Optional[str] = ..., config_key: _Optional[str] = ..., version_discriminator: _Optional[str] = ...) -> None: ...

class GetEvaluationScorerConfigResponse(_message.Message):
    __slots__ = ("scorer_config", "usage", "freshness", "capabilities")
    SCORER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    scorer_config: EvaluationScorerConfigDetailV1
    usage: EvaluationScorerConfigUsageV1
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, scorer_config: _Optional[_Union[EvaluationScorerConfigDetailV1, _Mapping]] = ..., usage: _Optional[_Union[EvaluationScorerConfigUsageV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class EvaluationScorerConfigVersionV1(_message.Message):
    __slots__ = ("evaluator_template_id", "version_discriminator", "name", "evaluator_kind", "execution_mode", "is_current", "rubric_bytes", "verdict_mapping_count", "created_at", "created_by")
    EVALUATOR_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_DISCRIMINATOR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_KIND_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_CURRENT_FIELD_NUMBER: _ClassVar[int]
    RUBRIC_BYTES_FIELD_NUMBER: _ClassVar[int]
    VERDICT_MAPPING_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    evaluator_template_id: str
    version_discriminator: str
    name: str
    evaluator_kind: str
    execution_mode: str
    is_current: bool
    rubric_bytes: int
    verdict_mapping_count: int
    created_at: _timestamp_pb2.Timestamp
    created_by: PrincipalRefV1
    def __init__(self, evaluator_template_id: _Optional[str] = ..., version_discriminator: _Optional[str] = ..., name: _Optional[str] = ..., evaluator_kind: _Optional[str] = ..., execution_mode: _Optional[str] = ..., is_current: _Optional[bool] = ..., rubric_bytes: _Optional[int] = ..., verdict_mapping_count: _Optional[int] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ...) -> None: ...

class ListEvaluationScorerConfigVersionsRequest(_message.Message):
    __slots__ = ("score_config_id", "config_key", "page")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    config_key: str
    page: _common_pb2.PageRequestV1
    def __init__(self, score_config_id: _Optional[str] = ..., config_key: _Optional[str] = ..., page: _Optional[_Union[_common_pb2.PageRequestV1, _Mapping]] = ...) -> None: ...

class ListEvaluationScorerConfigVersionsResponse(_message.Message):
    __slots__ = ("versions", "page", "history_availability", "freshness", "capabilities", "resync")
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    HISTORY_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    RESYNC_FIELD_NUMBER: _ClassVar[int]
    versions: _containers.RepeatedCompositeFieldContainer[EvaluationScorerConfigVersionV1]
    page: _common_pb2.PageResponseV1
    history_availability: MetricAvailabilityV1
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    resync: EvaluationCursorResyncV1
    def __init__(self, versions: _Optional[_Iterable[_Union[EvaluationScorerConfigVersionV1, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponseV1, _Mapping]] = ..., history_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., resync: _Optional[_Union[EvaluationCursorResyncV1, _Mapping]] = ...) -> None: ...

class EvaluationScorerSuiteSummaryV1(_message.Message):
    __slots__ = ("scorer_suite_id", "suite_key", "name", "version_discriminator", "combine_rule", "member_count", "blocking_gate_count", "archived_member_count", "is_archived", "archived_at", "created_at", "updated_at", "created_by")
    SCORER_SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    SUITE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_DISCRIMINATOR_FIELD_NUMBER: _ClassVar[int]
    COMBINE_RULE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    BLOCKING_GATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    scorer_suite_id: str
    suite_key: str
    name: str
    version_discriminator: str
    combine_rule: EvaluationScorerSuiteCombineRuleV1
    member_count: int
    blocking_gate_count: int
    archived_member_count: int
    is_archived: bool
    archived_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    created_by: PrincipalRefV1
    def __init__(self, scorer_suite_id: _Optional[str] = ..., suite_key: _Optional[str] = ..., name: _Optional[str] = ..., version_discriminator: _Optional[str] = ..., combine_rule: _Optional[_Union[EvaluationScorerSuiteCombineRuleV1, str]] = ..., member_count: _Optional[int] = ..., blocking_gate_count: _Optional[int] = ..., archived_member_count: _Optional[int] = ..., is_archived: _Optional[bool] = ..., archived_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ...) -> None: ...

class EvaluationScorerSuiteMemberDetailV1(_message.Message):
    __slots__ = ("score_config_id", "config_key", "name", "kind", "version_discriminator", "weight", "is_blocking_gate", "is_archived", "authored_on_this_surface")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    VERSION_DISCRIMINATOR_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    IS_BLOCKING_GATE_FIELD_NUMBER: _ClassVar[int]
    IS_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    AUTHORED_ON_THIS_SURFACE_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    config_key: str
    name: str
    kind: EvaluationScorerKindV1
    version_discriminator: str
    weight: float
    is_blocking_gate: bool
    is_archived: bool
    authored_on_this_surface: bool
    def __init__(self, score_config_id: _Optional[str] = ..., config_key: _Optional[str] = ..., name: _Optional[str] = ..., kind: _Optional[_Union[EvaluationScorerKindV1, str]] = ..., version_discriminator: _Optional[str] = ..., weight: _Optional[float] = ..., is_blocking_gate: _Optional[bool] = ..., is_archived: _Optional[bool] = ..., authored_on_this_surface: _Optional[bool] = ...) -> None: ...

class EvaluationScorerSuiteDetailV1(_message.Message):
    __slots__ = ("scorer_suite_id", "suite_key", "name", "version_discriminator", "combine_rule", "members", "is_archived", "archived_at", "created_at", "updated_at", "created_by", "revision_history_availability")
    SCORER_SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    SUITE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_DISCRIMINATOR_FIELD_NUMBER: _ClassVar[int]
    COMBINE_RULE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    IS_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    REVISION_HISTORY_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    scorer_suite_id: str
    suite_key: str
    name: str
    version_discriminator: str
    combine_rule: EvaluationScorerSuiteCombineRuleV1
    members: _containers.RepeatedCompositeFieldContainer[EvaluationScorerSuiteMemberDetailV1]
    is_archived: bool
    archived_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    created_by: PrincipalRefV1
    revision_history_availability: MetricAvailabilityV1
    def __init__(self, scorer_suite_id: _Optional[str] = ..., suite_key: _Optional[str] = ..., name: _Optional[str] = ..., version_discriminator: _Optional[str] = ..., combine_rule: _Optional[_Union[EvaluationScorerSuiteCombineRuleV1, str]] = ..., members: _Optional[_Iterable[_Union[EvaluationScorerSuiteMemberDetailV1, _Mapping]]] = ..., is_archived: _Optional[bool] = ..., archived_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[_Union[PrincipalRefV1, _Mapping]] = ..., revision_history_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class ListEvaluationScorerSuitesRequest(_message.Message):
    __slots__ = ("page", "archived_filter")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FILTER_FIELD_NUMBER: _ClassVar[int]
    page: _common_pb2.PageRequestV1
    archived_filter: EvaluationScorerArchivedFilterV1
    def __init__(self, page: _Optional[_Union[_common_pb2.PageRequestV1, _Mapping]] = ..., archived_filter: _Optional[_Union[EvaluationScorerArchivedFilterV1, str]] = ...) -> None: ...

class ListEvaluationScorerSuitesResponse(_message.Message):
    __slots__ = ("scorer_suites", "page", "freshness", "capabilities", "resync")
    SCORER_SUITES_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    RESYNC_FIELD_NUMBER: _ClassVar[int]
    scorer_suites: _containers.RepeatedCompositeFieldContainer[EvaluationScorerSuiteSummaryV1]
    page: _common_pb2.PageResponseV1
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    resync: EvaluationCursorResyncV1
    def __init__(self, scorer_suites: _Optional[_Iterable[_Union[EvaluationScorerSuiteSummaryV1, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponseV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., resync: _Optional[_Union[EvaluationCursorResyncV1, _Mapping]] = ...) -> None: ...

class GetEvaluationScorerSuiteRequest(_message.Message):
    __slots__ = ("scorer_suite_id", "suite_key")
    SCORER_SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    SUITE_KEY_FIELD_NUMBER: _ClassVar[int]
    scorer_suite_id: str
    suite_key: str
    def __init__(self, scorer_suite_id: _Optional[str] = ..., suite_key: _Optional[str] = ...) -> None: ...

class GetEvaluationScorerSuiteResponse(_message.Message):
    __slots__ = ("scorer_suite", "freshness", "capabilities")
    SCORER_SUITE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    scorer_suite: EvaluationScorerSuiteDetailV1
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, scorer_suite: _Optional[_Union[EvaluationScorerSuiteDetailV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class ArchiveEvaluationScorerConfigRequest(_message.Message):
    __slots__ = ("score_config_id", "config_key")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    config_key: str
    def __init__(self, score_config_id: _Optional[str] = ..., config_key: _Optional[str] = ...) -> None: ...

class ArchiveEvaluationScorerConfigResponse(_message.Message):
    __slots__ = ("scorer_config", "already_archived", "standing_references", "capabilities")
    SCORER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ALREADY_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    STANDING_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    scorer_config: EvaluationScorerConfigSummaryV1
    already_archived: bool
    standing_references: EvaluationScorerConfigUsageV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, scorer_config: _Optional[_Union[EvaluationScorerConfigSummaryV1, _Mapping]] = ..., already_archived: _Optional[bool] = ..., standing_references: _Optional[_Union[EvaluationScorerConfigUsageV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class ArchiveEvaluationScorerSuiteRequest(_message.Message):
    __slots__ = ("scorer_suite_id", "suite_key")
    SCORER_SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    SUITE_KEY_FIELD_NUMBER: _ClassVar[int]
    scorer_suite_id: str
    suite_key: str
    def __init__(self, scorer_suite_id: _Optional[str] = ..., suite_key: _Optional[str] = ...) -> None: ...

class ArchiveEvaluationScorerSuiteResponse(_message.Message):
    __slots__ = ("scorer_suite", "already_archived", "production_rule_count", "production_rule_availability", "capabilities")
    SCORER_SUITE_FIELD_NUMBER: _ClassVar[int]
    ALREADY_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    PRODUCTION_RULE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PRODUCTION_RULE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    scorer_suite: EvaluationScorerSuiteSummaryV1
    already_archived: bool
    production_rule_count: int
    production_rule_availability: MetricAvailabilityV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, scorer_suite: _Optional[_Union[EvaluationScorerSuiteSummaryV1, _Mapping]] = ..., already_archived: _Optional[bool] = ..., production_rule_count: _Optional[int] = ..., production_rule_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class DatasetCollectionSummaryV1(_message.Message):
    __slots__ = ("dataset_collection_id", "name", "description", "is_archived", "created_at", "updated_at", "active_version", "active_version_availability", "version_count", "open_changeset_count")
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_VERSION_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_VERSION_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    VERSION_COUNT_FIELD_NUMBER: _ClassVar[int]
    OPEN_CHANGESET_COUNT_FIELD_NUMBER: _ClassVar[int]
    dataset_collection_id: str
    name: str
    description: str
    is_archived: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    active_version: DatasetVersionSummaryV1
    active_version_availability: MetricAvailabilityV1
    version_count: int
    open_changeset_count: int
    def __init__(self, dataset_collection_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_archived: _Optional[bool] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., active_version: _Optional[_Union[DatasetVersionSummaryV1, _Mapping]] = ..., active_version_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., version_count: _Optional[int] = ..., open_changeset_count: _Optional[int] = ...) -> None: ...

class ListEvaluationDatasetCollectionsRequest(_message.Message):
    __slots__ = ("page_token", "limit", "include_archived", "name_filter")
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    NAME_FILTER_FIELD_NUMBER: _ClassVar[int]
    page_token: str
    limit: int
    include_archived: bool
    name_filter: str
    def __init__(self, page_token: _Optional[str] = ..., limit: _Optional[int] = ..., include_archived: _Optional[bool] = ..., name_filter: _Optional[str] = ...) -> None: ...

class ListEvaluationDatasetCollectionsResponse(_message.Message):
    __slots__ = ("collections", "total_count", "next_page_token", "freshness", "capabilities", "resync")
    COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    RESYNC_FIELD_NUMBER: _ClassVar[int]
    collections: _containers.RepeatedCompositeFieldContainer[DatasetCollectionSummaryV1]
    total_count: int
    next_page_token: str
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    resync: EvaluationCursorResyncV1
    def __init__(self, collections: _Optional[_Iterable[_Union[DatasetCollectionSummaryV1, _Mapping]]] = ..., total_count: _Optional[int] = ..., next_page_token: _Optional[str] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., resync: _Optional[_Union[EvaluationCursorResyncV1, _Mapping]] = ...) -> None: ...

class GetDatasetChangesetRequest(_message.Message):
    __slots__ = ("changeset_id",)
    CHANGESET_ID_FIELD_NUMBER: _ClassVar[int]
    changeset_id: str
    def __init__(self, changeset_id: _Optional[str] = ...) -> None: ...

class GetDatasetChangesetResponse(_message.Message):
    __slots__ = ("changeset", "active_dataset_version_id", "base_version_moved", "base_version_moved_availability", "freshness", "capabilities")
    CHANGESET_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_VERSION_MOVED_FIELD_NUMBER: _ClassVar[int]
    BASE_VERSION_MOVED_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    changeset: DatasetChangesetV1
    active_dataset_version_id: str
    base_version_moved: bool
    base_version_moved_availability: MetricAvailabilityV1
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, changeset: _Optional[_Union[DatasetChangesetV1, _Mapping]] = ..., active_dataset_version_id: _Optional[str] = ..., base_version_moved: _Optional[bool] = ..., base_version_moved_availability: _Optional[_Union[MetricAvailabilityV1, _Mapping]] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...

class ListDatasetChangesetsRequest(_message.Message):
    __slots__ = ("dataset_collection_id", "states", "page_size", "offset")
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    dataset_collection_id: str
    states: _containers.RepeatedScalarFieldContainer[DatasetChangesetStateV1]
    page_size: int
    offset: int
    def __init__(self, dataset_collection_id: _Optional[str] = ..., states: _Optional[_Iterable[_Union[DatasetChangesetStateV1, str]]] = ..., page_size: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListDatasetChangesetsResponse(_message.Message):
    __slots__ = ("changesets", "total_count", "next_offset", "freshness", "capabilities")
    CHANGESETS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    NEXT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    changesets: _containers.RepeatedCompositeFieldContainer[DatasetChangesetV1]
    total_count: int
    next_offset: int
    freshness: EvaluationFreshnessV1
    capabilities: AgenticEvaluationCapabilitiesV1
    def __init__(self, changesets: _Optional[_Iterable[_Union[DatasetChangesetV1, _Mapping]]] = ..., total_count: _Optional[int] = ..., next_offset: _Optional[int] = ..., freshness: _Optional[_Union[EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...
