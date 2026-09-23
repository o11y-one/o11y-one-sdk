import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from o11y_one.agentic.v1 import evaluation_pb2 as _evaluation_pb2
from o11y_one.agentic.v1 import agent_run_pb2 as _agent_run_pb2
from o11y_one.agentic.v1 import artifact_pb2 as _artifact_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TraceOperationKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRACE_OPERATION_KIND_V1_UNSPECIFIED: _ClassVar[TraceOperationKindV1]
    TRACE_OPERATION_KIND_V1_LLM: _ClassVar[TraceOperationKindV1]
    TRACE_OPERATION_KIND_V1_TOOL: _ClassVar[TraceOperationKindV1]
    TRACE_OPERATION_KIND_V1_DB: _ClassVar[TraceOperationKindV1]
    TRACE_OPERATION_KIND_V1_HTTP: _ClassVar[TraceOperationKindV1]
    TRACE_OPERATION_KIND_V1_RETRIEVAL: _ClassVar[TraceOperationKindV1]
    TRACE_OPERATION_KIND_V1_OTHER: _ClassVar[TraceOperationKindV1]

class TraceSpanStatusV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRACE_SPAN_STATUS_V1_UNSPECIFIED: _ClassVar[TraceSpanStatusV1]
    TRACE_SPAN_STATUS_V1_UNSET: _ClassVar[TraceSpanStatusV1]
    TRACE_SPAN_STATUS_V1_OK: _ClassVar[TraceSpanStatusV1]
    TRACE_SPAN_STATUS_V1_ERROR: _ClassVar[TraceSpanStatusV1]

class TraceAttentionKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRACE_ATTENTION_KIND_V1_UNSPECIFIED: _ClassVar[TraceAttentionKindV1]
    TRACE_ATTENTION_KIND_V1_ERROR: _ClassVar[TraceAttentionKindV1]
    TRACE_ATTENTION_KIND_V1_WARN: _ClassVar[TraceAttentionKindV1]
    TRACE_ATTENTION_KIND_V1_SLOW_OUTLIER: _ClassVar[TraceAttentionKindV1]

class TraceFaultCategoryV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRACE_FAULT_CATEGORY_V1_UNSPECIFIED: _ClassVar[TraceFaultCategoryV1]
    TRACE_FAULT_CATEGORY_V1_TIMEOUT: _ClassVar[TraceFaultCategoryV1]
    TRACE_FAULT_CATEGORY_V1_AUTH: _ClassVar[TraceFaultCategoryV1]
    TRACE_FAULT_CATEGORY_V1_RATE_LIMIT: _ClassVar[TraceFaultCategoryV1]
    TRACE_FAULT_CATEGORY_V1_NOT_FOUND: _ClassVar[TraceFaultCategoryV1]
    TRACE_FAULT_CATEGORY_V1_BAD_REQUEST: _ClassVar[TraceFaultCategoryV1]
    TRACE_FAULT_CATEGORY_V1_CONFLICT: _ClassVar[TraceFaultCategoryV1]
    TRACE_FAULT_CATEGORY_V1_UNAVAILABLE: _ClassVar[TraceFaultCategoryV1]
    TRACE_FAULT_CATEGORY_V1_DATA_LOSS: _ClassVar[TraceFaultCategoryV1]
    TRACE_FAULT_CATEGORY_V1_SERVER_ERROR: _ClassVar[TraceFaultCategoryV1]
    TRACE_FAULT_CATEGORY_V1_NETWORK: _ClassVar[TraceFaultCategoryV1]
    TRACE_FAULT_CATEGORY_V1_CLIENT_ERROR: _ClassVar[TraceFaultCategoryV1]
    TRACE_FAULT_CATEGORY_V1_APPLICATION: _ClassVar[TraceFaultCategoryV1]
    TRACE_FAULT_CATEGORY_V1_UNKNOWN: _ClassVar[TraceFaultCategoryV1]
    TRACE_FAULT_CATEGORY_V1_UNCLASSIFIED: _ClassVar[TraceFaultCategoryV1]

class TraceSpanCostProvenanceV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRACE_SPAN_COST_PROVENANCE_V1_UNSPECIFIED: _ClassVar[TraceSpanCostProvenanceV1]
    TRACE_SPAN_COST_PROVENANCE_V1_CLIENT_STATED: _ClassVar[TraceSpanCostProvenanceV1]
    TRACE_SPAN_COST_PROVENANCE_V1_LIST_RATE_ESTIMATE: _ClassVar[TraceSpanCostProvenanceV1]

class TraceReadRefusalKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRACE_READ_REFUSAL_KIND_V1_UNSPECIFIED: _ClassVar[TraceReadRefusalKindV1]
    TRACE_READ_REFUSAL_KIND_V1_TRACE_NOT_FOUND: _ClassVar[TraceReadRefusalKindV1]
    TRACE_READ_REFUSAL_KIND_V1_SPAN_POPULATION_EXCEEDS_CAP: _ClassVar[TraceReadRefusalKindV1]
    TRACE_READ_REFUSAL_KIND_V1_TRACE_ROOT_NOT_IN_POPULATION: _ClassVar[TraceReadRefusalKindV1]
    TRACE_READ_REFUSAL_KIND_V1_WINDOW_OUTSIDE_RETAINED_LOOKBACK: _ClassVar[TraceReadRefusalKindV1]
    TRACE_READ_REFUSAL_KIND_V1_READ_BUDGET_EXHAUSTED: _ClassVar[TraceReadRefusalKindV1]

class AgentRunOutcomeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_RUN_OUTCOME_V1_UNSPECIFIED: _ClassVar[AgentRunOutcomeV1]
    AGENT_RUN_OUTCOME_V1_UNKNOWN: _ClassVar[AgentRunOutcomeV1]
    AGENT_RUN_OUTCOME_V1_SUCCEEDED: _ClassVar[AgentRunOutcomeV1]
    AGENT_RUN_OUTCOME_V1_DEGRADED: _ClassVar[AgentRunOutcomeV1]
    AGENT_RUN_OUTCOME_V1_FAILED: _ClassVar[AgentRunOutcomeV1]
    AGENT_RUN_OUTCOME_V1_POLICY_FAILED: _ClassVar[AgentRunOutcomeV1]

class AgentRunOutcomeInputKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_RUN_OUTCOME_INPUT_KIND_V1_UNSPECIFIED: _ClassVar[AgentRunOutcomeInputKindV1]
    AGENT_RUN_OUTCOME_INPUT_KIND_V1_CONVERSATION_COMPLETENESS: _ClassVar[AgentRunOutcomeInputKindV1]
    AGENT_RUN_OUTCOME_INPUT_KIND_V1_PRODUCTION_RULE_VERDICT: _ClassVar[AgentRunOutcomeInputKindV1]
    AGENT_RUN_OUTCOME_INPUT_KIND_V1_MEMBER_SPAN_FAILURE: _ClassVar[AgentRunOutcomeInputKindV1]
    AGENT_RUN_OUTCOME_INPUT_KIND_V1_MEMBER_SPAN_WARNING: _ClassVar[AgentRunOutcomeInputKindV1]
    AGENT_RUN_OUTCOME_INPUT_KIND_V1_MEMBER_SPAN_STATUS: _ClassVar[AgentRunOutcomeInputKindV1]

class AgentRunCoverageVerdictV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_RUN_COVERAGE_VERDICT_V1_UNSPECIFIED: _ClassVar[AgentRunCoverageVerdictV1]
    AGENT_RUN_COVERAGE_VERDICT_V1_UNKNOWN: _ClassVar[AgentRunCoverageVerdictV1]
    AGENT_RUN_COVERAGE_VERDICT_V1_NOT_COVERED: _ClassVar[AgentRunCoverageVerdictV1]
    AGENT_RUN_COVERAGE_VERDICT_V1_COVERED_BY_DATASET: _ClassVar[AgentRunCoverageVerdictV1]
    AGENT_RUN_COVERAGE_VERDICT_V1_COVERED_BY_EVALUATION: _ClassVar[AgentRunCoverageVerdictV1]

class AgentRunTimelineModeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_RUN_TIMELINE_MODE_V1_UNSPECIFIED: _ClassVar[AgentRunTimelineModeV1]
    AGENT_RUN_TIMELINE_MODE_V1_SUMMARY: _ClassVar[AgentRunTimelineModeV1]
    AGENT_RUN_TIMELINE_MODE_V1_FAILURES_ONLY: _ClassVar[AgentRunTimelineModeV1]
    AGENT_RUN_TIMELINE_MODE_V1_CRITICAL_PATH: _ClassVar[AgentRunTimelineModeV1]

class AgentRunEventKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_RUN_EVENT_KIND_V1_UNSPECIFIED: _ClassVar[AgentRunEventKindV1]
    AGENT_RUN_EVENT_KIND_V1_MODEL: _ClassVar[AgentRunEventKindV1]
    AGENT_RUN_EVENT_KIND_V1_TOOL: _ClassVar[AgentRunEventKindV1]
    AGENT_RUN_EVENT_KIND_V1_RETRIEVAL: _ClassVar[AgentRunEventKindV1]
    AGENT_RUN_EVENT_KIND_V1_DOWNSTREAM: _ClassVar[AgentRunEventKindV1]
    AGENT_RUN_EVENT_KIND_V1_ERROR: _ClassVar[AgentRunEventKindV1]
    AGENT_RUN_EVENT_KIND_V1_GENERIC: _ClassVar[AgentRunEventKindV1]

class AgentRunEventDeliveryV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_RUN_EVENT_DELIVERY_V1_UNSPECIFIED: _ClassVar[AgentRunEventDeliveryV1]
    AGENT_RUN_EVENT_DELIVERY_V1_APPEND: _ClassVar[AgentRunEventDeliveryV1]
    AGENT_RUN_EVENT_DELIVERY_V1_UPSERT: _ClassVar[AgentRunEventDeliveryV1]

class AgentRunAttributeSourceV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_RUN_ATTRIBUTE_SOURCE_V1_UNSPECIFIED: _ClassVar[AgentRunAttributeSourceV1]
    AGENT_RUN_ATTRIBUTE_SOURCE_V1_CANONICAL: _ClassVar[AgentRunAttributeSourceV1]
    AGENT_RUN_ATTRIBUTE_SOURCE_V1_LEGACY_ALIAS: _ClassVar[AgentRunAttributeSourceV1]
    AGENT_RUN_ATTRIBUTE_SOURCE_V1_BOTH_EQUAL: _ClassVar[AgentRunAttributeSourceV1]
    AGENT_RUN_ATTRIBUTE_SOURCE_V1_CONFLICT: _ClassVar[AgentRunAttributeSourceV1]
TRACE_OPERATION_KIND_V1_UNSPECIFIED: TraceOperationKindV1
TRACE_OPERATION_KIND_V1_LLM: TraceOperationKindV1
TRACE_OPERATION_KIND_V1_TOOL: TraceOperationKindV1
TRACE_OPERATION_KIND_V1_DB: TraceOperationKindV1
TRACE_OPERATION_KIND_V1_HTTP: TraceOperationKindV1
TRACE_OPERATION_KIND_V1_RETRIEVAL: TraceOperationKindV1
TRACE_OPERATION_KIND_V1_OTHER: TraceOperationKindV1
TRACE_SPAN_STATUS_V1_UNSPECIFIED: TraceSpanStatusV1
TRACE_SPAN_STATUS_V1_UNSET: TraceSpanStatusV1
TRACE_SPAN_STATUS_V1_OK: TraceSpanStatusV1
TRACE_SPAN_STATUS_V1_ERROR: TraceSpanStatusV1
TRACE_ATTENTION_KIND_V1_UNSPECIFIED: TraceAttentionKindV1
TRACE_ATTENTION_KIND_V1_ERROR: TraceAttentionKindV1
TRACE_ATTENTION_KIND_V1_WARN: TraceAttentionKindV1
TRACE_ATTENTION_KIND_V1_SLOW_OUTLIER: TraceAttentionKindV1
TRACE_FAULT_CATEGORY_V1_UNSPECIFIED: TraceFaultCategoryV1
TRACE_FAULT_CATEGORY_V1_TIMEOUT: TraceFaultCategoryV1
TRACE_FAULT_CATEGORY_V1_AUTH: TraceFaultCategoryV1
TRACE_FAULT_CATEGORY_V1_RATE_LIMIT: TraceFaultCategoryV1
TRACE_FAULT_CATEGORY_V1_NOT_FOUND: TraceFaultCategoryV1
TRACE_FAULT_CATEGORY_V1_BAD_REQUEST: TraceFaultCategoryV1
TRACE_FAULT_CATEGORY_V1_CONFLICT: TraceFaultCategoryV1
TRACE_FAULT_CATEGORY_V1_UNAVAILABLE: TraceFaultCategoryV1
TRACE_FAULT_CATEGORY_V1_DATA_LOSS: TraceFaultCategoryV1
TRACE_FAULT_CATEGORY_V1_SERVER_ERROR: TraceFaultCategoryV1
TRACE_FAULT_CATEGORY_V1_NETWORK: TraceFaultCategoryV1
TRACE_FAULT_CATEGORY_V1_CLIENT_ERROR: TraceFaultCategoryV1
TRACE_FAULT_CATEGORY_V1_APPLICATION: TraceFaultCategoryV1
TRACE_FAULT_CATEGORY_V1_UNKNOWN: TraceFaultCategoryV1
TRACE_FAULT_CATEGORY_V1_UNCLASSIFIED: TraceFaultCategoryV1
TRACE_SPAN_COST_PROVENANCE_V1_UNSPECIFIED: TraceSpanCostProvenanceV1
TRACE_SPAN_COST_PROVENANCE_V1_CLIENT_STATED: TraceSpanCostProvenanceV1
TRACE_SPAN_COST_PROVENANCE_V1_LIST_RATE_ESTIMATE: TraceSpanCostProvenanceV1
TRACE_READ_REFUSAL_KIND_V1_UNSPECIFIED: TraceReadRefusalKindV1
TRACE_READ_REFUSAL_KIND_V1_TRACE_NOT_FOUND: TraceReadRefusalKindV1
TRACE_READ_REFUSAL_KIND_V1_SPAN_POPULATION_EXCEEDS_CAP: TraceReadRefusalKindV1
TRACE_READ_REFUSAL_KIND_V1_TRACE_ROOT_NOT_IN_POPULATION: TraceReadRefusalKindV1
TRACE_READ_REFUSAL_KIND_V1_WINDOW_OUTSIDE_RETAINED_LOOKBACK: TraceReadRefusalKindV1
TRACE_READ_REFUSAL_KIND_V1_READ_BUDGET_EXHAUSTED: TraceReadRefusalKindV1
AGENT_RUN_OUTCOME_V1_UNSPECIFIED: AgentRunOutcomeV1
AGENT_RUN_OUTCOME_V1_UNKNOWN: AgentRunOutcomeV1
AGENT_RUN_OUTCOME_V1_SUCCEEDED: AgentRunOutcomeV1
AGENT_RUN_OUTCOME_V1_DEGRADED: AgentRunOutcomeV1
AGENT_RUN_OUTCOME_V1_FAILED: AgentRunOutcomeV1
AGENT_RUN_OUTCOME_V1_POLICY_FAILED: AgentRunOutcomeV1
AGENT_RUN_OUTCOME_INPUT_KIND_V1_UNSPECIFIED: AgentRunOutcomeInputKindV1
AGENT_RUN_OUTCOME_INPUT_KIND_V1_CONVERSATION_COMPLETENESS: AgentRunOutcomeInputKindV1
AGENT_RUN_OUTCOME_INPUT_KIND_V1_PRODUCTION_RULE_VERDICT: AgentRunOutcomeInputKindV1
AGENT_RUN_OUTCOME_INPUT_KIND_V1_MEMBER_SPAN_FAILURE: AgentRunOutcomeInputKindV1
AGENT_RUN_OUTCOME_INPUT_KIND_V1_MEMBER_SPAN_WARNING: AgentRunOutcomeInputKindV1
AGENT_RUN_OUTCOME_INPUT_KIND_V1_MEMBER_SPAN_STATUS: AgentRunOutcomeInputKindV1
AGENT_RUN_COVERAGE_VERDICT_V1_UNSPECIFIED: AgentRunCoverageVerdictV1
AGENT_RUN_COVERAGE_VERDICT_V1_UNKNOWN: AgentRunCoverageVerdictV1
AGENT_RUN_COVERAGE_VERDICT_V1_NOT_COVERED: AgentRunCoverageVerdictV1
AGENT_RUN_COVERAGE_VERDICT_V1_COVERED_BY_DATASET: AgentRunCoverageVerdictV1
AGENT_RUN_COVERAGE_VERDICT_V1_COVERED_BY_EVALUATION: AgentRunCoverageVerdictV1
AGENT_RUN_TIMELINE_MODE_V1_UNSPECIFIED: AgentRunTimelineModeV1
AGENT_RUN_TIMELINE_MODE_V1_SUMMARY: AgentRunTimelineModeV1
AGENT_RUN_TIMELINE_MODE_V1_FAILURES_ONLY: AgentRunTimelineModeV1
AGENT_RUN_TIMELINE_MODE_V1_CRITICAL_PATH: AgentRunTimelineModeV1
AGENT_RUN_EVENT_KIND_V1_UNSPECIFIED: AgentRunEventKindV1
AGENT_RUN_EVENT_KIND_V1_MODEL: AgentRunEventKindV1
AGENT_RUN_EVENT_KIND_V1_TOOL: AgentRunEventKindV1
AGENT_RUN_EVENT_KIND_V1_RETRIEVAL: AgentRunEventKindV1
AGENT_RUN_EVENT_KIND_V1_DOWNSTREAM: AgentRunEventKindV1
AGENT_RUN_EVENT_KIND_V1_ERROR: AgentRunEventKindV1
AGENT_RUN_EVENT_KIND_V1_GENERIC: AgentRunEventKindV1
AGENT_RUN_EVENT_DELIVERY_V1_UNSPECIFIED: AgentRunEventDeliveryV1
AGENT_RUN_EVENT_DELIVERY_V1_APPEND: AgentRunEventDeliveryV1
AGENT_RUN_EVENT_DELIVERY_V1_UPSERT: AgentRunEventDeliveryV1
AGENT_RUN_ATTRIBUTE_SOURCE_V1_UNSPECIFIED: AgentRunAttributeSourceV1
AGENT_RUN_ATTRIBUTE_SOURCE_V1_CANONICAL: AgentRunAttributeSourceV1
AGENT_RUN_ATTRIBUTE_SOURCE_V1_LEGACY_ALIAS: AgentRunAttributeSourceV1
AGENT_RUN_ATTRIBUTE_SOURCE_V1_BOTH_EQUAL: AgentRunAttributeSourceV1
AGENT_RUN_ATTRIBUTE_SOURCE_V1_CONFLICT: AgentRunAttributeSourceV1

class TraceSpanPopulationBoundaryV1(_message.Message):
    __slots__ = ("dimension", "scope_code", "max_spans")
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    SCOPE_CODE_FIELD_NUMBER: _ClassVar[int]
    MAX_SPANS_FIELD_NUMBER: _ClassVar[int]
    dimension: _evaluation_pb2.EvaluationOperationDimensionV1
    scope_code: str
    max_spans: int
    def __init__(self, dimension: _Optional[_Union[_evaluation_pb2.EvaluationOperationDimensionV1, str]] = ..., scope_code: _Optional[str] = ..., max_spans: _Optional[int] = ...) -> None: ...

class TraceWindowV1(_message.Message):
    __slots__ = ("start", "end", "clamped", "clamp_reason_code")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    CLAMPED_FIELD_NUMBER: _ClassVar[int]
    CLAMP_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    clamped: bool
    clamp_reason_code: str
    def __init__(self, start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., clamped: _Optional[bool] = ..., clamp_reason_code: _Optional[str] = ...) -> None: ...

class TraceReadRefusalV1(_message.Message):
    __slots__ = ("kind", "reason_code", "detail", "recovery_action", "observed_span_count", "cap")
    KIND_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_ACTION_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_SPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    CAP_FIELD_NUMBER: _ClassVar[int]
    kind: TraceReadRefusalKindV1
    reason_code: str
    detail: str
    recovery_action: _evaluation_pb2.RecoveryActionV1
    observed_span_count: int
    cap: int
    def __init__(self, kind: _Optional[_Union[TraceReadRefusalKindV1, str]] = ..., reason_code: _Optional[str] = ..., detail: _Optional[str] = ..., recovery_action: _Optional[_Union[_evaluation_pb2.RecoveryActionV1, str]] = ..., observed_span_count: _Optional[int] = ..., cap: _Optional[int] = ...) -> None: ...

class TraceFaultCategoryCountV1(_message.Message):
    __slots__ = ("category", "span_count")
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    category: TraceFaultCategoryV1
    span_count: int
    def __init__(self, category: _Optional[_Union[TraceFaultCategoryV1, str]] = ..., span_count: _Optional[int] = ...) -> None: ...

class TraceFaultStatusCountV1(_message.Message):
    __slots__ = ("status", "span_count")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    status: TraceSpanStatusV1
    span_count: int
    def __init__(self, status: _Optional[_Union[TraceSpanStatusV1, str]] = ..., span_count: _Optional[int] = ...) -> None: ...

class TraceFaultBreakdownV1(_message.Message):
    __slots__ = ("exception_event_span_count", "exception_event_count", "exception_event_count_availability", "warned_span_count", "category_counts", "status_counts", "fault_share_basis_points", "fault_share_availability")
    EXCEPTION_EVENT_SPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_EVENT_COUNT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    WARNED_SPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_COUNTS_FIELD_NUMBER: _ClassVar[int]
    STATUS_COUNTS_FIELD_NUMBER: _ClassVar[int]
    FAULT_SHARE_BASIS_POINTS_FIELD_NUMBER: _ClassVar[int]
    FAULT_SHARE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    exception_event_span_count: int
    exception_event_count: int
    exception_event_count_availability: _evaluation_pb2.MetricAvailabilityV1
    warned_span_count: int
    category_counts: _containers.RepeatedCompositeFieldContainer[TraceFaultCategoryCountV1]
    status_counts: _containers.RepeatedCompositeFieldContainer[TraceFaultStatusCountV1]
    fault_share_basis_points: int
    fault_share_availability: _evaluation_pb2.MetricAvailabilityV1
    def __init__(self, exception_event_span_count: _Optional[int] = ..., exception_event_count: _Optional[int] = ..., exception_event_count_availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ..., warned_span_count: _Optional[int] = ..., category_counts: _Optional[_Iterable[_Union[TraceFaultCategoryCountV1, _Mapping]]] = ..., status_counts: _Optional[_Iterable[_Union[TraceFaultStatusCountV1, _Mapping]]] = ..., fault_share_basis_points: _Optional[int] = ..., fault_share_availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class TraceFirstFailureV1(_message.Message):
    __slots__ = ("span_id", "span_name", "category", "started_at", "duration_micros", "error_type", "error_message")
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    DURATION_MICROS_FIELD_NUMBER: _ClassVar[int]
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    span_id: str
    span_name: str
    category: TraceFaultCategoryV1
    started_at: _timestamp_pb2.Timestamp
    duration_micros: int
    error_type: str
    error_message: str
    def __init__(self, span_id: _Optional[str] = ..., span_name: _Optional[str] = ..., category: _Optional[_Union[TraceFaultCategoryV1, str]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., duration_micros: _Optional[int] = ..., error_type: _Optional[str] = ..., error_message: _Optional[str] = ...) -> None: ...

class TraceSpanRateBasisV1(_message.Message):
    __slots__ = ("model_id", "registry_version", "registry_effective_date", "rate_checked_at", "staleness_threshold_days", "input_micros_per_million_tokens", "output_micros_per_million_tokens", "token_accounting", "dimension_notes")
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_VERSION_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_EFFECTIVE_DATE_FIELD_NUMBER: _ClassVar[int]
    RATE_CHECKED_AT_FIELD_NUMBER: _ClassVar[int]
    STALENESS_THRESHOLD_DAYS_FIELD_NUMBER: _ClassVar[int]
    INPUT_MICROS_PER_MILLION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_MICROS_PER_MILLION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ACCOUNTING_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_NOTES_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    registry_version: str
    registry_effective_date: str
    rate_checked_at: str
    staleness_threshold_days: int
    input_micros_per_million_tokens: int
    output_micros_per_million_tokens: int
    token_accounting: _evaluation_pb2.EvaluationTokenAccountingV1
    dimension_notes: _containers.RepeatedCompositeFieldContainer[_evaluation_pb2.EvaluationRateDimensionNoteV1]
    def __init__(self, model_id: _Optional[str] = ..., registry_version: _Optional[str] = ..., registry_effective_date: _Optional[str] = ..., rate_checked_at: _Optional[str] = ..., staleness_threshold_days: _Optional[int] = ..., input_micros_per_million_tokens: _Optional[int] = ..., output_micros_per_million_tokens: _Optional[int] = ..., token_accounting: _Optional[_Union[_evaluation_pb2.EvaluationTokenAccountingV1, _Mapping]] = ..., dimension_notes: _Optional[_Iterable[_Union[_evaluation_pb2.EvaluationRateDimensionNoteV1, _Mapping]]] = ...) -> None: ...

class TraceSpanCostV1(_message.Message):
    __slots__ = ("provenance", "amount", "client_stated_amount_verbatim", "rate_basis", "availability", "currency_availability")
    PROVENANCE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_STATED_AMOUNT_VERBATIM_FIELD_NUMBER: _ClassVar[int]
    RATE_BASIS_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    provenance: TraceSpanCostProvenanceV1
    amount: _evaluation_pb2.CostAmountV1
    client_stated_amount_verbatim: str
    rate_basis: TraceSpanRateBasisV1
    availability: _evaluation_pb2.MetricAvailabilityV1
    currency_availability: _evaluation_pb2.MetricAvailabilityV1
    def __init__(self, provenance: _Optional[_Union[TraceSpanCostProvenanceV1, str]] = ..., amount: _Optional[_Union[_evaluation_pb2.CostAmountV1, _Mapping]] = ..., client_stated_amount_verbatim: _Optional[str] = ..., rate_basis: _Optional[_Union[TraceSpanRateBasisV1, _Mapping]] = ..., availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ..., currency_availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class TraceSpanCostRollupV1(_message.Message):
    __slots__ = ("total", "availability", "client_stated_span_count", "list_rate_estimate_span_count", "uncosted_span_count", "mixes_stated_and_estimated")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_STATED_SPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    LIST_RATE_ESTIMATE_SPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNCOSTED_SPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    MIXES_STATED_AND_ESTIMATED_FIELD_NUMBER: _ClassVar[int]
    total: _evaluation_pb2.CostAmountV1
    availability: _evaluation_pb2.MetricAvailabilityV1
    client_stated_span_count: int
    list_rate_estimate_span_count: int
    uncosted_span_count: int
    mixes_stated_and_estimated: bool
    def __init__(self, total: _Optional[_Union[_evaluation_pb2.CostAmountV1, _Mapping]] = ..., availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ..., client_stated_span_count: _Optional[int] = ..., list_rate_estimate_span_count: _Optional[int] = ..., uncosted_span_count: _Optional[int] = ..., mixes_stated_and_estimated: _Optional[bool] = ...) -> None: ...

class TraceSpanOutlierV1(_message.Message):
    __slots__ = ("span_id", "span_name", "duration_micros")
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_NAME_FIELD_NUMBER: _ClassVar[int]
    DURATION_MICROS_FIELD_NUMBER: _ClassVar[int]
    span_id: str
    span_name: str
    duration_micros: int
    def __init__(self, span_id: _Optional[str] = ..., span_name: _Optional[str] = ..., duration_micros: _Optional[int] = ...) -> None: ...

class TraceOperationGroupV1(_message.Message):
    __slots__ = ("kind", "target", "collapsed_count", "failure_count", "total_duration_micros", "p95_duration_micros", "p95_availability", "outliers", "omitted_outlier_count", "faults", "cost")
    KIND_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    COLLAPSED_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DURATION_MICROS_FIELD_NUMBER: _ClassVar[int]
    P95_DURATION_MICROS_FIELD_NUMBER: _ClassVar[int]
    P95_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    OUTLIERS_FIELD_NUMBER: _ClassVar[int]
    OMITTED_OUTLIER_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAULTS_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    kind: TraceOperationKindV1
    target: str
    collapsed_count: int
    failure_count: int
    total_duration_micros: int
    p95_duration_micros: int
    p95_availability: _evaluation_pb2.MetricAvailabilityV1
    outliers: _containers.RepeatedCompositeFieldContainer[TraceSpanOutlierV1]
    omitted_outlier_count: int
    faults: TraceFaultBreakdownV1
    cost: TraceSpanCostRollupV1
    def __init__(self, kind: _Optional[_Union[TraceOperationKindV1, str]] = ..., target: _Optional[str] = ..., collapsed_count: _Optional[int] = ..., failure_count: _Optional[int] = ..., total_duration_micros: _Optional[int] = ..., p95_duration_micros: _Optional[int] = ..., p95_availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ..., outliers: _Optional[_Iterable[_Union[TraceSpanOutlierV1, _Mapping]]] = ..., omitted_outlier_count: _Optional[int] = ..., faults: _Optional[_Union[TraceFaultBreakdownV1, _Mapping]] = ..., cost: _Optional[_Union[TraceSpanCostRollupV1, _Mapping]] = ...) -> None: ...

class TraceStepSummaryV1(_message.Message):
    __slots__ = ("step_id", "step_name", "agent_name", "agent_id", "started_at", "ended_at", "wall_time_micros", "wall_time_share_basis_points", "wall_time_share_availability", "operation_count", "failure_count", "operation_groups", "omitted_operation_group_count", "faults", "first_failure", "cost")
    STEP_ID_FIELD_NUMBER: _ClassVar[int]
    STEP_NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    WALL_TIME_MICROS_FIELD_NUMBER: _ClassVar[int]
    WALL_TIME_SHARE_BASIS_POINTS_FIELD_NUMBER: _ClassVar[int]
    WALL_TIME_SHARE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    OPERATION_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    OPERATION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    OMITTED_OPERATION_GROUP_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAULTS_FIELD_NUMBER: _ClassVar[int]
    FIRST_FAILURE_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    step_id: str
    step_name: str
    agent_name: str
    agent_id: str
    started_at: _timestamp_pb2.Timestamp
    ended_at: _timestamp_pb2.Timestamp
    wall_time_micros: int
    wall_time_share_basis_points: int
    wall_time_share_availability: _evaluation_pb2.MetricAvailabilityV1
    operation_count: int
    failure_count: int
    operation_groups: _containers.RepeatedCompositeFieldContainer[TraceOperationGroupV1]
    omitted_operation_group_count: int
    faults: TraceFaultBreakdownV1
    first_failure: TraceFirstFailureV1
    cost: TraceSpanCostRollupV1
    def __init__(self, step_id: _Optional[str] = ..., step_name: _Optional[str] = ..., agent_name: _Optional[str] = ..., agent_id: _Optional[str] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ended_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., wall_time_micros: _Optional[int] = ..., wall_time_share_basis_points: _Optional[int] = ..., wall_time_share_availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ..., operation_count: _Optional[int] = ..., failure_count: _Optional[int] = ..., operation_groups: _Optional[_Iterable[_Union[TraceOperationGroupV1, _Mapping]]] = ..., omitted_operation_group_count: _Optional[int] = ..., faults: _Optional[_Union[TraceFaultBreakdownV1, _Mapping]] = ..., first_failure: _Optional[_Union[TraceFirstFailureV1, _Mapping]] = ..., cost: _Optional[_Union[TraceSpanCostRollupV1, _Mapping]] = ...) -> None: ...

class TraceCriticalPathStepV1(_message.Message):
    __slots__ = ("span_id", "span_name", "kind", "duration_micros", "self_duration_micros", "depth", "step_id")
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    DURATION_MICROS_FIELD_NUMBER: _ClassVar[int]
    SELF_DURATION_MICROS_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    STEP_ID_FIELD_NUMBER: _ClassVar[int]
    span_id: str
    span_name: str
    kind: TraceOperationKindV1
    duration_micros: int
    self_duration_micros: int
    depth: int
    step_id: str
    def __init__(self, span_id: _Optional[str] = ..., span_name: _Optional[str] = ..., kind: _Optional[_Union[TraceOperationKindV1, str]] = ..., duration_micros: _Optional[int] = ..., self_duration_micros: _Optional[int] = ..., depth: _Optional[int] = ..., step_id: _Optional[str] = ...) -> None: ...

class TraceCriticalPathV1(_message.Message):
    __slots__ = ("steps", "total_duration_micros", "availability", "method_code")
    STEPS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DURATION_MICROS_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    METHOD_CODE_FIELD_NUMBER: _ClassVar[int]
    steps: _containers.RepeatedCompositeFieldContainer[TraceCriticalPathStepV1]
    total_duration_micros: int
    availability: _evaluation_pb2.MetricAvailabilityV1
    method_code: str
    def __init__(self, steps: _Optional[_Iterable[_Union[TraceCriticalPathStepV1, _Mapping]]] = ..., total_duration_micros: _Optional[int] = ..., availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ..., method_code: _Optional[str] = ...) -> None: ...

class TraceAttentionItemV1(_message.Message):
    __slots__ = ("span_id", "span_name", "kind", "reason_code", "detail", "duration_micros", "step_id")
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    DURATION_MICROS_FIELD_NUMBER: _ClassVar[int]
    STEP_ID_FIELD_NUMBER: _ClassVar[int]
    span_id: str
    span_name: str
    kind: TraceAttentionKindV1
    reason_code: str
    detail: str
    duration_micros: int
    step_id: str
    def __init__(self, span_id: _Optional[str] = ..., span_name: _Optional[str] = ..., kind: _Optional[_Union[TraceAttentionKindV1, str]] = ..., reason_code: _Optional[str] = ..., detail: _Optional[str] = ..., duration_micros: _Optional[int] = ..., step_id: _Optional[str] = ...) -> None: ...

class TraceNeedsAttentionSetV1(_message.Message):
    __slots__ = ("items", "error_count", "warn_count", "slow_outlier_count", "omitted_item_count")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    WARN_COUNT_FIELD_NUMBER: _ClassVar[int]
    SLOW_OUTLIER_COUNT_FIELD_NUMBER: _ClassVar[int]
    OMITTED_ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[TraceAttentionItemV1]
    error_count: int
    warn_count: int
    slow_outlier_count: int
    omitted_item_count: int
    def __init__(self, items: _Optional[_Iterable[_Union[TraceAttentionItemV1, _Mapping]]] = ..., error_count: _Optional[int] = ..., warn_count: _Optional[int] = ..., slow_outlier_count: _Optional[int] = ..., omitted_item_count: _Optional[int] = ...) -> None: ...

class AgentTraceHeaderV1(_message.Message):
    __slots__ = ("trace_id", "started_at", "ended_at", "wall_time_micros", "span_count", "step_count", "unattributed_span_count", "step_availability", "cost", "retried_span_count")
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    WALL_TIME_MICROS_FIELD_NUMBER: _ClassVar[int]
    SPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    STEP_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNATTRIBUTED_SPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    STEP_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    RETRIED_SPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    trace_id: str
    started_at: _timestamp_pb2.Timestamp
    ended_at: _timestamp_pb2.Timestamp
    wall_time_micros: int
    span_count: int
    step_count: int
    unattributed_span_count: int
    step_availability: _evaluation_pb2.MetricAvailabilityV1
    cost: TraceSpanCostRollupV1
    retried_span_count: int
    def __init__(self, trace_id: _Optional[str] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ended_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., wall_time_micros: _Optional[int] = ..., span_count: _Optional[int] = ..., step_count: _Optional[int] = ..., unattributed_span_count: _Optional[int] = ..., step_availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ..., cost: _Optional[_Union[TraceSpanCostRollupV1, _Mapping]] = ..., retried_span_count: _Optional[int] = ...) -> None: ...

class TraceSpanContentRefV1(_message.Message):
    __slots__ = ("content_class", "storage_uri")
    CONTENT_CLASS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_URI_FIELD_NUMBER: _ClassVar[int]
    content_class: str
    storage_uri: str
    def __init__(self, content_class: _Optional[str] = ..., storage_uri: _Optional[str] = ...) -> None: ...

class TraceSpanRetryV1(_message.Message):
    __slots__ = ("chain_id", "attempt_index", "attempt_count")
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_INDEX_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_COUNT_FIELD_NUMBER: _ClassVar[int]
    chain_id: str
    attempt_index: int
    attempt_count: int
    def __init__(self, chain_id: _Optional[str] = ..., attempt_index: _Optional[int] = ..., attempt_count: _Optional[int] = ...) -> None: ...

class TraceSpanV1(_message.Message):
    __slots__ = ("span_id", "parent_span_id", "step_id", "name", "kind", "target", "service_name", "started_at", "ended_at", "duration_micros", "status", "is_error", "error_type", "error_message", "has_exception_event", "verbatim_usage", "time_to_first_token_availability", "content_refs", "cost", "retry")
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    STEP_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    DURATION_MICROS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    HAS_EXCEPTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    VERBATIM_USAGE_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_FIRST_TOKEN_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    CONTENT_REFS_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    RETRY_FIELD_NUMBER: _ClassVar[int]
    span_id: str
    parent_span_id: str
    step_id: str
    name: str
    kind: TraceOperationKindV1
    target: str
    service_name: str
    started_at: _timestamp_pb2.Timestamp
    ended_at: _timestamp_pb2.Timestamp
    duration_micros: int
    status: TraceSpanStatusV1
    is_error: bool
    error_type: str
    error_message: str
    has_exception_event: bool
    verbatim_usage: _evaluation_pb2.ProviderUsageRecordV1
    time_to_first_token_availability: _evaluation_pb2.MetricAvailabilityV1
    content_refs: _containers.RepeatedCompositeFieldContainer[TraceSpanContentRefV1]
    cost: TraceSpanCostV1
    retry: TraceSpanRetryV1
    def __init__(self, span_id: _Optional[str] = ..., parent_span_id: _Optional[str] = ..., step_id: _Optional[str] = ..., name: _Optional[str] = ..., kind: _Optional[_Union[TraceOperationKindV1, str]] = ..., target: _Optional[str] = ..., service_name: _Optional[str] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ended_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., duration_micros: _Optional[int] = ..., status: _Optional[_Union[TraceSpanStatusV1, str]] = ..., is_error: _Optional[bool] = ..., error_type: _Optional[str] = ..., error_message: _Optional[str] = ..., has_exception_event: _Optional[bool] = ..., verbatim_usage: _Optional[_Union[_evaluation_pb2.ProviderUsageRecordV1, _Mapping]] = ..., time_to_first_token_availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ..., content_refs: _Optional[_Iterable[_Union[TraceSpanContentRefV1, _Mapping]]] = ..., cost: _Optional[_Union[TraceSpanCostV1, _Mapping]] = ..., retry: _Optional[_Union[TraceSpanRetryV1, _Mapping]] = ...) -> None: ...

class GetAgentTraceDetailRequest(_message.Message):
    __slots__ = ("trace_id", "start", "end")
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    trace_id: str
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    def __init__(self, trace_id: _Optional[str] = ..., start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetAgentTraceDetailResponse(_message.Message):
    __slots__ = ("header", "steps", "critical_path", "needs_attention", "boundary", "window", "freshness", "capabilities", "refusal")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_PATH_FIELD_NUMBER: _ClassVar[int]
    NEEDS_ATTENTION_FIELD_NUMBER: _ClassVar[int]
    BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    header: AgentTraceHeaderV1
    steps: _containers.RepeatedCompositeFieldContainer[TraceStepSummaryV1]
    critical_path: TraceCriticalPathV1
    needs_attention: TraceNeedsAttentionSetV1
    boundary: TraceSpanPopulationBoundaryV1
    window: TraceWindowV1
    freshness: _evaluation_pb2.EvaluationFreshnessV1
    capabilities: _evaluation_pb2.AgenticEvaluationCapabilitiesV1
    refusal: TraceReadRefusalV1
    def __init__(self, header: _Optional[_Union[AgentTraceHeaderV1, _Mapping]] = ..., steps: _Optional[_Iterable[_Union[TraceStepSummaryV1, _Mapping]]] = ..., critical_path: _Optional[_Union[TraceCriticalPathV1, _Mapping]] = ..., needs_attention: _Optional[_Union[TraceNeedsAttentionSetV1, _Mapping]] = ..., boundary: _Optional[_Union[TraceSpanPopulationBoundaryV1, _Mapping]] = ..., window: _Optional[_Union[TraceWindowV1, _Mapping]] = ..., freshness: _Optional[_Union[_evaluation_pb2.EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[_evaluation_pb2.AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., refusal: _Optional[_Union[TraceReadRefusalV1, _Mapping]] = ...) -> None: ...

class ListAgentTraceSpansRequest(_message.Message):
    __slots__ = ("trace_id", "start", "end", "limit", "offset", "step_id", "attention_filter")
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    STEP_ID_FIELD_NUMBER: _ClassVar[int]
    ATTENTION_FILTER_FIELD_NUMBER: _ClassVar[int]
    trace_id: str
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    limit: int
    offset: int
    step_id: str
    attention_filter: TraceAttentionKindV1
    def __init__(self, trace_id: _Optional[str] = ..., start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ..., step_id: _Optional[str] = ..., attention_filter: _Optional[_Union[TraceAttentionKindV1, str]] = ...) -> None: ...

class ListAgentTraceSpansResponse(_message.Message):
    __slots__ = ("spans", "total_matching_span_count", "has_more", "boundary", "window", "freshness", "refusal")
    SPANS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MATCHING_SPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    spans: _containers.RepeatedCompositeFieldContainer[TraceSpanV1]
    total_matching_span_count: int
    has_more: bool
    boundary: TraceSpanPopulationBoundaryV1
    window: TraceWindowV1
    freshness: _evaluation_pb2.EvaluationFreshnessV1
    refusal: TraceReadRefusalV1
    def __init__(self, spans: _Optional[_Iterable[_Union[TraceSpanV1, _Mapping]]] = ..., total_matching_span_count: _Optional[int] = ..., has_more: _Optional[bool] = ..., boundary: _Optional[_Union[TraceSpanPopulationBoundaryV1, _Mapping]] = ..., window: _Optional[_Union[TraceWindowV1, _Mapping]] = ..., freshness: _Optional[_Union[_evaluation_pb2.EvaluationFreshnessV1, _Mapping]] = ..., refusal: _Optional[_Union[TraceReadRefusalV1, _Mapping]] = ...) -> None: ...

class AgentRunOutcomeInputV1(_message.Message):
    __slots__ = ("kind", "observed_count", "contributed")
    KIND_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONTRIBUTED_FIELD_NUMBER: _ClassVar[int]
    kind: AgentRunOutcomeInputKindV1
    observed_count: int
    contributed: bool
    def __init__(self, kind: _Optional[_Union[AgentRunOutcomeInputKindV1, str]] = ..., observed_count: _Optional[int] = ..., contributed: _Optional[bool] = ...) -> None: ...

class AgentRunOutcomeAssessmentV1(_message.Message):
    __slots__ = ("outcome", "inputs", "method_code", "outcome_unknown_reason_code")
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    METHOD_CODE_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_UNKNOWN_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    outcome: AgentRunOutcomeV1
    inputs: _containers.RepeatedCompositeFieldContainer[AgentRunOutcomeInputV1]
    method_code: str
    outcome_unknown_reason_code: str
    def __init__(self, outcome: _Optional[_Union[AgentRunOutcomeV1, str]] = ..., inputs: _Optional[_Iterable[_Union[AgentRunOutcomeInputV1, _Mapping]]] = ..., method_code: _Optional[str] = ..., outcome_unknown_reason_code: _Optional[str] = ...) -> None: ...

class AgentRunCostLineItemV1(_message.Message):
    __slots__ = ("kind", "target", "span_count", "rollup")
    KIND_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    SPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    ROLLUP_FIELD_NUMBER: _ClassVar[int]
    kind: TraceOperationKindV1
    target: str
    span_count: int
    rollup: TraceSpanCostRollupV1
    def __init__(self, kind: _Optional[_Union[TraceOperationKindV1, str]] = ..., target: _Optional[str] = ..., span_count: _Optional[int] = ..., rollup: _Optional[_Union[TraceSpanCostRollupV1, _Mapping]] = ...) -> None: ...

class AgentRunUsageTotalsV1(_message.Message):
    __slots__ = ("input_tokens", "output_tokens", "total_tokens", "cache_read_input_tokens", "cache_creation_input_tokens", "reasoning_tokens", "contributing_span_count", "availability", "token_accounting")
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_READ_INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_CREATION_INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    REASONING_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CONTRIBUTING_SPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ACCOUNTING_FIELD_NUMBER: _ClassVar[int]
    input_tokens: int
    output_tokens: int
    total_tokens: int
    cache_read_input_tokens: int
    cache_creation_input_tokens: int
    reasoning_tokens: int
    contributing_span_count: int
    availability: _evaluation_pb2.MetricAvailabilityV1
    token_accounting: _evaluation_pb2.EvaluationTokenAccountingV1
    def __init__(self, input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., total_tokens: _Optional[int] = ..., cache_read_input_tokens: _Optional[int] = ..., cache_creation_input_tokens: _Optional[int] = ..., reasoning_tokens: _Optional[int] = ..., contributing_span_count: _Optional[int] = ..., availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ..., token_accounting: _Optional[_Union[_evaluation_pb2.EvaluationTokenAccountingV1, _Mapping]] = ...) -> None: ...

class AgentRunScorePostureV1(_message.Message):
    __slots__ = ("score_count", "scored_member_trace_count", "worst_score_value", "failing_rule_verdict_count", "passing_rule_verdict_count", "rule_scorer_failure_count", "availability")
    SCORE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SCORED_MEMBER_TRACE_COUNT_FIELD_NUMBER: _ClassVar[int]
    WORST_SCORE_VALUE_FIELD_NUMBER: _ClassVar[int]
    FAILING_RULE_VERDICT_COUNT_FIELD_NUMBER: _ClassVar[int]
    PASSING_RULE_VERDICT_COUNT_FIELD_NUMBER: _ClassVar[int]
    RULE_SCORER_FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    score_count: int
    scored_member_trace_count: int
    worst_score_value: float
    failing_rule_verdict_count: int
    passing_rule_verdict_count: int
    rule_scorer_failure_count: int
    availability: _evaluation_pb2.MetricAvailabilityV1
    def __init__(self, score_count: _Optional[int] = ..., scored_member_trace_count: _Optional[int] = ..., worst_score_value: _Optional[float] = ..., failing_rule_verdict_count: _Optional[int] = ..., passing_rule_verdict_count: _Optional[int] = ..., rule_scorer_failure_count: _Optional[int] = ..., availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class AgentRunDimensionV1(_message.Message):
    __slots__ = ("value", "distinct_count", "availability")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DISTINCT_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    value: str
    distinct_count: int
    availability: _evaluation_pb2.MetricAvailabilityV1
    def __init__(self, value: _Optional[str] = ..., distinct_count: _Optional[int] = ..., availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class AgentRunVersionContextV1(_message.Message):
    __slots__ = ("prompt_version", "model_version", "tool_version", "retrieval_version_availability")
    PROMPT_VERSION_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
    TOOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    RETRIEVAL_VERSION_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    prompt_version: AgentRunDimensionV1
    model_version: AgentRunDimensionV1
    tool_version: AgentRunDimensionV1
    retrieval_version_availability: _evaluation_pb2.MetricAvailabilityV1
    def __init__(self, prompt_version: _Optional[_Union[AgentRunDimensionV1, _Mapping]] = ..., model_version: _Optional[_Union[AgentRunDimensionV1, _Mapping]] = ..., tool_version: _Optional[_Union[AgentRunDimensionV1, _Mapping]] = ..., retrieval_version_availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class AgentRunReleaseContextV1(_message.Message):
    __slots__ = ("release_keys", "release_count", "active_release_block_count", "availability")
    RELEASE_KEYS_FIELD_NUMBER: _ClassVar[int]
    RELEASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_RELEASE_BLOCK_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    release_keys: _containers.RepeatedScalarFieldContainer[str]
    release_count: int
    active_release_block_count: int
    availability: _evaluation_pb2.MetricAvailabilityV1
    def __init__(self, release_keys: _Optional[_Iterable[str]] = ..., release_count: _Optional[int] = ..., active_release_block_count: _Optional[int] = ..., availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class AgentRunCoverageReferenceV1(_message.Message):
    __slots__ = ("reference_kind", "reference_id", "member_trace_id")
    REFERENCE_KIND_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    reference_kind: str
    reference_id: str
    member_trace_id: str
    def __init__(self, reference_kind: _Optional[str] = ..., reference_id: _Optional[str] = ..., member_trace_id: _Optional[str] = ...) -> None: ...

class AgentRunEvaluationCoverageV1(_message.Message):
    __slots__ = ("verdict", "references", "covering_reference_count", "omitted_reference_count", "unknown_reason_code", "availability")
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    REFERENCES_FIELD_NUMBER: _ClassVar[int]
    COVERING_REFERENCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    OMITTED_REFERENCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    verdict: AgentRunCoverageVerdictV1
    references: _containers.RepeatedCompositeFieldContainer[AgentRunCoverageReferenceV1]
    covering_reference_count: int
    omitted_reference_count: int
    unknown_reason_code: str
    availability: _evaluation_pb2.MetricAvailabilityV1
    def __init__(self, verdict: _Optional[_Union[AgentRunCoverageVerdictV1, str]] = ..., references: _Optional[_Iterable[_Union[AgentRunCoverageReferenceV1, _Mapping]]] = ..., covering_reference_count: _Optional[int] = ..., omitted_reference_count: _Optional[int] = ..., unknown_reason_code: _Optional[str] = ..., availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class AgentRunInstrumentationCompletenessV1(_message.Message):
    __slots__ = ("state", "unattributed_span_count", "refused_member_trace_count", "refused_member_observed_span_count", "unread_member_trace_count", "retry_count_availability", "handoff_count_availability", "guardrail_count_availability", "memory_operation_count_availability", "time_to_first_token_availability", "counts_availability")
    STATE_FIELD_NUMBER: _ClassVar[int]
    UNATTRIBUTED_SPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    REFUSED_MEMBER_TRACE_COUNT_FIELD_NUMBER: _ClassVar[int]
    REFUSED_MEMBER_OBSERVED_SPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNREAD_MEMBER_TRACE_COUNT_FIELD_NUMBER: _ClassVar[int]
    RETRY_COUNT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    HANDOFF_COUNT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    GUARDRAIL_COUNT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    MEMORY_OPERATION_COUNT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_FIRST_TOKEN_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    COUNTS_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    state: _evaluation_pb2.CompletenessStateV1
    unattributed_span_count: int
    refused_member_trace_count: int
    refused_member_observed_span_count: int
    unread_member_trace_count: int
    retry_count_availability: _evaluation_pb2.MetricAvailabilityV1
    handoff_count_availability: _evaluation_pb2.MetricAvailabilityV1
    guardrail_count_availability: _evaluation_pb2.MetricAvailabilityV1
    memory_operation_count_availability: _evaluation_pb2.MetricAvailabilityV1
    time_to_first_token_availability: _evaluation_pb2.MetricAvailabilityV1
    counts_availability: _evaluation_pb2.MetricAvailabilityV1
    def __init__(self, state: _Optional[_Union[_evaluation_pb2.CompletenessStateV1, str]] = ..., unattributed_span_count: _Optional[int] = ..., refused_member_trace_count: _Optional[int] = ..., refused_member_observed_span_count: _Optional[int] = ..., unread_member_trace_count: _Optional[int] = ..., retry_count_availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ..., handoff_count_availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ..., guardrail_count_availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ..., memory_operation_count_availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ..., time_to_first_token_availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ..., counts_availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class AgentRunSummaryV1(_message.Message):
    __slots__ = ("agent_run_id", "grouping", "completeness", "outcome", "started_at", "ended_at", "last_seen_at", "trace_count", "folded_trace_count", "span_count", "span_event_count", "span_event_count_availability", "agent_count", "model_count", "tool_count", "retrieval_span_count", "mcp_span_count", "hard_failure_count", "degraded_failure_count", "faults", "first_failure", "critical_path_latency_micros", "critical_path_availability", "critical_path_method_code", "critical_path_trace_id", "cost_line_items", "omitted_cost_line_item_count", "usage", "score_posture", "customer", "deployment", "versions", "release_context", "instrumentation", "projection_version", "facts_watermark", "refreshed_at", "freshness")
    AGENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    GROUPING_FIELD_NUMBER: _ClassVar[int]
    COMPLETENESS_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    TRACE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FOLDED_TRACE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    SPAN_EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    SPAN_EVENT_COUNT_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    AGENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    MODEL_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOOL_COUNT_FIELD_NUMBER: _ClassVar[int]
    RETRIEVAL_SPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    MCP_SPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    HARD_FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    DEGRADED_FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAULTS_FIELD_NUMBER: _ClassVar[int]
    FIRST_FAILURE_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_PATH_LATENCY_MICROS_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_PATH_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_PATH_METHOD_CODE_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_PATH_TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    COST_LINE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    OMITTED_COST_LINE_ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    SCORE_POSTURE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    RELEASE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTATION_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_VERSION_FIELD_NUMBER: _ClassVar[int]
    FACTS_WATERMARK_FIELD_NUMBER: _ClassVar[int]
    REFRESHED_AT_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    agent_run_id: str
    grouping: _agent_run_pb2.AgentRunGroupingV1
    completeness: _agent_run_pb2.ConversationCompletenessV1
    outcome: AgentRunOutcomeAssessmentV1
    started_at: _timestamp_pb2.Timestamp
    ended_at: _timestamp_pb2.Timestamp
    last_seen_at: _timestamp_pb2.Timestamp
    trace_count: int
    folded_trace_count: int
    span_count: int
    span_event_count: int
    span_event_count_availability: _evaluation_pb2.MetricAvailabilityV1
    agent_count: int
    model_count: int
    tool_count: int
    retrieval_span_count: int
    mcp_span_count: int
    hard_failure_count: int
    degraded_failure_count: int
    faults: TraceFaultBreakdownV1
    first_failure: TraceFirstFailureV1
    critical_path_latency_micros: int
    critical_path_availability: _evaluation_pb2.MetricAvailabilityV1
    critical_path_method_code: str
    critical_path_trace_id: str
    cost_line_items: _containers.RepeatedCompositeFieldContainer[AgentRunCostLineItemV1]
    omitted_cost_line_item_count: int
    usage: AgentRunUsageTotalsV1
    score_posture: AgentRunScorePostureV1
    customer: AgentRunDimensionV1
    deployment: AgentRunDimensionV1
    versions: AgentRunVersionContextV1
    release_context: AgentRunReleaseContextV1
    instrumentation: AgentRunInstrumentationCompletenessV1
    projection_version: int
    facts_watermark: str
    refreshed_at: _timestamp_pb2.Timestamp
    freshness: _evaluation_pb2.EvaluationFreshnessV1
    def __init__(self, agent_run_id: _Optional[str] = ..., grouping: _Optional[_Union[_agent_run_pb2.AgentRunGroupingV1, _Mapping]] = ..., completeness: _Optional[_Union[_agent_run_pb2.ConversationCompletenessV1, _Mapping]] = ..., outcome: _Optional[_Union[AgentRunOutcomeAssessmentV1, _Mapping]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ended_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., trace_count: _Optional[int] = ..., folded_trace_count: _Optional[int] = ..., span_count: _Optional[int] = ..., span_event_count: _Optional[int] = ..., span_event_count_availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ..., agent_count: _Optional[int] = ..., model_count: _Optional[int] = ..., tool_count: _Optional[int] = ..., retrieval_span_count: _Optional[int] = ..., mcp_span_count: _Optional[int] = ..., hard_failure_count: _Optional[int] = ..., degraded_failure_count: _Optional[int] = ..., faults: _Optional[_Union[TraceFaultBreakdownV1, _Mapping]] = ..., first_failure: _Optional[_Union[TraceFirstFailureV1, _Mapping]] = ..., critical_path_latency_micros: _Optional[int] = ..., critical_path_availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ..., critical_path_method_code: _Optional[str] = ..., critical_path_trace_id: _Optional[str] = ..., cost_line_items: _Optional[_Iterable[_Union[AgentRunCostLineItemV1, _Mapping]]] = ..., omitted_cost_line_item_count: _Optional[int] = ..., usage: _Optional[_Union[AgentRunUsageTotalsV1, _Mapping]] = ..., score_posture: _Optional[_Union[AgentRunScorePostureV1, _Mapping]] = ..., customer: _Optional[_Union[AgentRunDimensionV1, _Mapping]] = ..., deployment: _Optional[_Union[AgentRunDimensionV1, _Mapping]] = ..., versions: _Optional[_Union[AgentRunVersionContextV1, _Mapping]] = ..., release_context: _Optional[_Union[AgentRunReleaseContextV1, _Mapping]] = ..., instrumentation: _Optional[_Union[AgentRunInstrumentationCompletenessV1, _Mapping]] = ..., projection_version: _Optional[int] = ..., facts_watermark: _Optional[str] = ..., refreshed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., freshness: _Optional[_Union[_evaluation_pb2.EvaluationFreshnessV1, _Mapping]] = ...) -> None: ...

class AgentRunListFilterV1(_message.Message):
    __slots__ = ("customer_id", "deployment_id", "outcomes", "grouping_confidences", "completeness_states", "instrumentation_states", "prompt_version", "model_version", "tool_version", "exclude_ungrouped")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    OUTCOMES_FIELD_NUMBER: _ClassVar[int]
    GROUPING_CONFIDENCES_FIELD_NUMBER: _ClassVar[int]
    COMPLETENESS_STATES_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTATION_STATES_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
    TOOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_UNGROUPED_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    deployment_id: str
    outcomes: _containers.RepeatedScalarFieldContainer[AgentRunOutcomeV1]
    grouping_confidences: _containers.RepeatedScalarFieldContainer[_agent_run_pb2.AgentRunGroupingConfidenceV1]
    completeness_states: _containers.RepeatedScalarFieldContainer[_agent_run_pb2.ConversationCompletenessStateV1]
    instrumentation_states: _containers.RepeatedScalarFieldContainer[_evaluation_pb2.CompletenessStateV1]
    prompt_version: str
    model_version: str
    tool_version: str
    exclude_ungrouped: bool
    def __init__(self, customer_id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., outcomes: _Optional[_Iterable[_Union[AgentRunOutcomeV1, str]]] = ..., grouping_confidences: _Optional[_Iterable[_Union[_agent_run_pb2.AgentRunGroupingConfidenceV1, str]]] = ..., completeness_states: _Optional[_Iterable[_Union[_agent_run_pb2.ConversationCompletenessStateV1, str]]] = ..., instrumentation_states: _Optional[_Iterable[_Union[_evaluation_pb2.CompletenessStateV1, str]]] = ..., prompt_version: _Optional[str] = ..., model_version: _Optional[str] = ..., tool_version: _Optional[str] = ..., exclude_ungrouped: _Optional[bool] = ...) -> None: ...

class ListAgentRunsRequest(_message.Message):
    __slots__ = ("start", "end", "filter", "limit", "page_token")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    filter: AgentRunListFilterV1
    limit: int
    page_token: str
    def __init__(self, start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., filter: _Optional[_Union[AgentRunListFilterV1, _Mapping]] = ..., limit: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAgentRunsResponse(_message.Message):
    __slots__ = ("runs", "next_page_token", "has_more", "hidden_ungrouped_run_count", "window", "boundary", "cursor_semantics_code", "freshness", "capabilities", "refusal")
    RUNS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_UNGROUPED_RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    CURSOR_SEMANTICS_CODE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    runs: _containers.RepeatedCompositeFieldContainer[AgentRunSummaryV1]
    next_page_token: str
    has_more: bool
    hidden_ungrouped_run_count: int
    window: TraceWindowV1
    boundary: TraceSpanPopulationBoundaryV1
    cursor_semantics_code: str
    freshness: _evaluation_pb2.EvaluationFreshnessV1
    capabilities: _evaluation_pb2.AgenticEvaluationCapabilitiesV1
    refusal: TraceReadRefusalV1
    def __init__(self, runs: _Optional[_Iterable[_Union[AgentRunSummaryV1, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., has_more: _Optional[bool] = ..., hidden_ungrouped_run_count: _Optional[int] = ..., window: _Optional[_Union[TraceWindowV1, _Mapping]] = ..., boundary: _Optional[_Union[TraceSpanPopulationBoundaryV1, _Mapping]] = ..., cursor_semantics_code: _Optional[str] = ..., freshness: _Optional[_Union[_evaluation_pb2.EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[_evaluation_pb2.AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., refusal: _Optional[_Union[TraceReadRefusalV1, _Mapping]] = ...) -> None: ...

class GetAgentRunRequest(_message.Message):
    __slots__ = ("agent_run_id",)
    AGENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    agent_run_id: str
    def __init__(self, agent_run_id: _Optional[str] = ...) -> None: ...

class GetAgentRunResponse(_message.Message):
    __slots__ = ("summary", "evaluation_coverage", "window", "boundary", "freshness", "capabilities", "refusal")
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_COVERAGE_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    summary: AgentRunSummaryV1
    evaluation_coverage: AgentRunEvaluationCoverageV1
    window: TraceWindowV1
    boundary: TraceSpanPopulationBoundaryV1
    freshness: _evaluation_pb2.EvaluationFreshnessV1
    capabilities: _evaluation_pb2.AgenticEvaluationCapabilitiesV1
    refusal: TraceReadRefusalV1
    def __init__(self, summary: _Optional[_Union[AgentRunSummaryV1, _Mapping]] = ..., evaluation_coverage: _Optional[_Union[AgentRunEvaluationCoverageV1, _Mapping]] = ..., window: _Optional[_Union[TraceWindowV1, _Mapping]] = ..., boundary: _Optional[_Union[TraceSpanPopulationBoundaryV1, _Mapping]] = ..., freshness: _Optional[_Union[_evaluation_pb2.EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[_evaluation_pb2.AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., refusal: _Optional[_Union[TraceReadRefusalV1, _Mapping]] = ...) -> None: ...

class AgentRunEventKindCoverageV1(_message.Message):
    __slots__ = ("kind", "availability")
    KIND_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    kind: str
    availability: _evaluation_pb2.MetricAvailabilityV1
    def __init__(self, kind: _Optional[str] = ..., availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class AgentRunArtifactSourceCoverageV1(_message.Message):
    __slots__ = ("source_kind", "availability")
    SOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    source_kind: _artifact_pb2.ArtifactLinkSourceKindV1
    availability: _evaluation_pb2.MetricAvailabilityV1
    def __init__(self, source_kind: _Optional[_Union[_artifact_pb2.ArtifactLinkSourceKindV1, str]] = ..., availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class AgentRunEventAttributeProvenanceV1(_message.Message):
    __slots__ = ("canonical_field", "source", "legacy_name", "discarded_legacy_value")
    CANONICAL_FIELD_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    LEGACY_NAME_FIELD_NUMBER: _ClassVar[int]
    DISCARDED_LEGACY_VALUE_FIELD_NUMBER: _ClassVar[int]
    canonical_field: str
    source: AgentRunAttributeSourceV1
    legacy_name: str
    discarded_legacy_value: str
    def __init__(self, canonical_field: _Optional[str] = ..., source: _Optional[_Union[AgentRunAttributeSourceV1, str]] = ..., legacy_name: _Optional[str] = ..., discarded_legacy_value: _Optional[str] = ...) -> None: ...

class AgentRunEventUsageV1(_message.Message):
    __slots__ = ("input_tokens", "output_tokens", "total_tokens", "cache_read_input_tokens", "cache_creation_input_tokens", "reasoning_tokens", "availability")
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_READ_INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_CREATION_INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    REASONING_TOKENS_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    input_tokens: int
    output_tokens: int
    total_tokens: int
    cache_read_input_tokens: int
    cache_creation_input_tokens: int
    reasoning_tokens: int
    availability: _evaluation_pb2.MetricAvailabilityV1
    def __init__(self, input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., total_tokens: _Optional[int] = ..., cache_read_input_tokens: _Optional[int] = ..., cache_creation_input_tokens: _Optional[int] = ..., reasoning_tokens: _Optional[int] = ..., availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class AgentRunEventGenerationV1(_message.Message):
    __slots__ = ("request_model", "response_model")
    REQUEST_MODEL_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_MODEL_FIELD_NUMBER: _ClassVar[int]
    request_model: str
    response_model: str
    def __init__(self, request_model: _Optional[str] = ..., response_model: _Optional[str] = ...) -> None: ...

class AgentRunLaneV1(_message.Message):
    __slots__ = ("lane_id", "display_name", "event_count")
    LANE_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    lane_id: str
    display_name: str
    event_count: int
    def __init__(self, lane_id: _Optional[str] = ..., display_name: _Optional[str] = ..., event_count: _Optional[int] = ...) -> None: ...

class AgentRunChildSummaryV1(_message.Message):
    __slots__ = ("event_id", "name", "kind", "duration_micros", "is_error")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    DURATION_MICROS_FIELD_NUMBER: _ClassVar[int]
    IS_ERROR_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    name: str
    kind: AgentRunEventKindV1
    duration_micros: int
    is_error: bool
    def __init__(self, event_id: _Optional[str] = ..., name: _Optional[str] = ..., kind: _Optional[_Union[AgentRunEventKindV1, str]] = ..., duration_micros: _Optional[int] = ..., is_error: _Optional[bool] = ...) -> None: ...

class AgentRunArtifactSummaryV1(_message.Message):
    __slots__ = ("link_id", "artifact_id", "artifact_type", "role", "relation", "status", "conflict_posture", "resolver_posture", "source_kind", "fallback_reason", "media_type", "filename", "storage_system", "resolver_key", "correction_sequence", "rejection_reason_code", "observed_at", "anchor")
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_ID_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_POSTURE_FIELD_NUMBER: _ClassVar[int]
    RESOLVER_POSTURE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_REASON_FIELD_NUMBER: _ClassVar[int]
    MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    STORAGE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    RESOLVER_KEY_FIELD_NUMBER: _ClassVar[int]
    CORRECTION_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    REJECTION_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_FIELD_NUMBER: _ClassVar[int]
    link_id: bytes
    artifact_id: str
    artifact_type: _artifact_pb2.ArtifactTypeV1
    role: _artifact_pb2.ArtifactRoleV1
    relation: _artifact_pb2.ArtifactRelationV1
    status: _artifact_pb2.ArtifactLinkStatusV1
    conflict_posture: _artifact_pb2.ArtifactLinkConflictPostureV1
    resolver_posture: _artifact_pb2.ArtifactResolverPostureV1
    source_kind: _artifact_pb2.ArtifactLinkSourceKindV1
    fallback_reason: _artifact_pb2.ArtifactLinkFallbackReasonV1
    media_type: str
    filename: str
    storage_system: str
    resolver_key: str
    correction_sequence: int
    rejection_reason_code: str
    observed_at: _timestamp_pb2.Timestamp
    anchor: _artifact_pb2.EvidenceAnchorV1
    def __init__(self, link_id: _Optional[bytes] = ..., artifact_id: _Optional[str] = ..., artifact_type: _Optional[_Union[_artifact_pb2.ArtifactTypeV1, str]] = ..., role: _Optional[_Union[_artifact_pb2.ArtifactRoleV1, str]] = ..., relation: _Optional[_Union[_artifact_pb2.ArtifactRelationV1, str]] = ..., status: _Optional[_Union[_artifact_pb2.ArtifactLinkStatusV1, str]] = ..., conflict_posture: _Optional[_Union[_artifact_pb2.ArtifactLinkConflictPostureV1, str]] = ..., resolver_posture: _Optional[_Union[_artifact_pb2.ArtifactResolverPostureV1, str]] = ..., source_kind: _Optional[_Union[_artifact_pb2.ArtifactLinkSourceKindV1, str]] = ..., fallback_reason: _Optional[_Union[_artifact_pb2.ArtifactLinkFallbackReasonV1, str]] = ..., media_type: _Optional[str] = ..., filename: _Optional[str] = ..., storage_system: _Optional[str] = ..., resolver_key: _Optional[str] = ..., correction_sequence: _Optional[int] = ..., rejection_reason_code: _Optional[str] = ..., observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., anchor: _Optional[_Union[_artifact_pb2.EvidenceAnchorV1, _Mapping]] = ...) -> None: ...

class AgentRunArtifactDiagnosticV1(_message.Message):
    __slots__ = ("reason_code", "occurrence_count")
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    OCCURRENCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    reason_code: str
    occurrence_count: int
    def __init__(self, reason_code: _Optional[str] = ..., occurrence_count: _Optional[int] = ...) -> None: ...

class AgentRunNestedCapsV1(_message.Message):
    __slots__ = ("children_omitted", "artifacts_omitted", "content_refs_omitted", "attribute_provenance_omitted")
    CHILDREN_OMITTED_FIELD_NUMBER: _ClassVar[int]
    ARTIFACTS_OMITTED_FIELD_NUMBER: _ClassVar[int]
    CONTENT_REFS_OMITTED_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_PROVENANCE_OMITTED_FIELD_NUMBER: _ClassVar[int]
    children_omitted: int
    artifacts_omitted: int
    content_refs_omitted: int
    attribute_provenance_omitted: int
    def __init__(self, children_omitted: _Optional[int] = ..., artifacts_omitted: _Optional[int] = ..., content_refs_omitted: _Optional[int] = ..., attribute_provenance_omitted: _Optional[int] = ...) -> None: ...

class AgentRunEventV1(_message.Message):
    __slots__ = ("event_id", "delivery", "lane_id", "agent_name", "agent_id", "kind", "operation_kind", "subject", "name", "trace_id", "span_id", "parent_span_id", "parent_event_id", "step_id", "conversation_id", "observation_id_availability", "observation_id", "started_at", "ended_at", "duration_micros", "status", "is_error", "has_exception_event", "fault_category", "error_type", "error_message", "on_critical_path", "generation", "usage", "cost", "content_refs", "attribute_provenance", "children", "artifacts", "nested_caps")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_FIELD_NUMBER: _ClassVar[int]
    LANE_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    OPERATION_KIND_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    STEP_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_ID_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    DURATION_MICROS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_ERROR_FIELD_NUMBER: _ClassVar[int]
    HAS_EXCEPTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    FAULT_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ON_CRITICAL_PATH_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    CONTENT_REFS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_PROVENANCE_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    NESTED_CAPS_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    delivery: AgentRunEventDeliveryV1
    lane_id: str
    agent_name: str
    agent_id: str
    kind: AgentRunEventKindV1
    operation_kind: TraceOperationKindV1
    subject: str
    name: str
    trace_id: str
    span_id: str
    parent_span_id: str
    parent_event_id: str
    step_id: str
    conversation_id: str
    observation_id_availability: _evaluation_pb2.MetricAvailabilityV1
    observation_id: str
    started_at: _timestamp_pb2.Timestamp
    ended_at: _timestamp_pb2.Timestamp
    duration_micros: int
    status: TraceSpanStatusV1
    is_error: bool
    has_exception_event: bool
    fault_category: TraceFaultCategoryV1
    error_type: str
    error_message: str
    on_critical_path: bool
    generation: AgentRunEventGenerationV1
    usage: AgentRunEventUsageV1
    cost: TraceSpanCostV1
    content_refs: _containers.RepeatedCompositeFieldContainer[TraceSpanContentRefV1]
    attribute_provenance: _containers.RepeatedCompositeFieldContainer[AgentRunEventAttributeProvenanceV1]
    children: _containers.RepeatedCompositeFieldContainer[AgentRunChildSummaryV1]
    artifacts: _containers.RepeatedCompositeFieldContainer[AgentRunArtifactSummaryV1]
    nested_caps: AgentRunNestedCapsV1
    def __init__(self, event_id: _Optional[str] = ..., delivery: _Optional[_Union[AgentRunEventDeliveryV1, str]] = ..., lane_id: _Optional[str] = ..., agent_name: _Optional[str] = ..., agent_id: _Optional[str] = ..., kind: _Optional[_Union[AgentRunEventKindV1, str]] = ..., operation_kind: _Optional[_Union[TraceOperationKindV1, str]] = ..., subject: _Optional[str] = ..., name: _Optional[str] = ..., trace_id: _Optional[str] = ..., span_id: _Optional[str] = ..., parent_span_id: _Optional[str] = ..., parent_event_id: _Optional[str] = ..., step_id: _Optional[str] = ..., conversation_id: _Optional[str] = ..., observation_id_availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ..., observation_id: _Optional[str] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ended_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., duration_micros: _Optional[int] = ..., status: _Optional[_Union[TraceSpanStatusV1, str]] = ..., is_error: _Optional[bool] = ..., has_exception_event: _Optional[bool] = ..., fault_category: _Optional[_Union[TraceFaultCategoryV1, str]] = ..., error_type: _Optional[str] = ..., error_message: _Optional[str] = ..., on_critical_path: _Optional[bool] = ..., generation: _Optional[_Union[AgentRunEventGenerationV1, _Mapping]] = ..., usage: _Optional[_Union[AgentRunEventUsageV1, _Mapping]] = ..., cost: _Optional[_Union[TraceSpanCostV1, _Mapping]] = ..., content_refs: _Optional[_Iterable[_Union[TraceSpanContentRefV1, _Mapping]]] = ..., attribute_provenance: _Optional[_Iterable[_Union[AgentRunEventAttributeProvenanceV1, _Mapping]]] = ..., children: _Optional[_Iterable[_Union[AgentRunChildSummaryV1, _Mapping]]] = ..., artifacts: _Optional[_Iterable[_Union[AgentRunArtifactSummaryV1, _Mapping]]] = ..., nested_caps: _Optional[_Union[AgentRunNestedCapsV1, _Mapping]] = ...) -> None: ...

class AgentRunTimelineModeEffectV1(_message.Message):
    __slots__ = ("mode", "applied", "reason_code", "population_count", "retained_count")
    MODE_FIELD_NUMBER: _ClassVar[int]
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    POPULATION_COUNT_FIELD_NUMBER: _ClassVar[int]
    RETAINED_COUNT_FIELD_NUMBER: _ClassVar[int]
    mode: AgentRunTimelineModeV1
    applied: bool
    reason_code: str
    population_count: int
    retained_count: int
    def __init__(self, mode: _Optional[_Union[AgentRunTimelineModeV1, str]] = ..., applied: _Optional[bool] = ..., reason_code: _Optional[str] = ..., population_count: _Optional[int] = ..., retained_count: _Optional[int] = ...) -> None: ...

class AgentRunTimelineCursorV1(_message.Message):
    __slots__ = ("next_page_token", "resync_required", "projection_version", "stopped_on_byte_ceiling", "total_event_count")
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RESYNC_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_VERSION_FIELD_NUMBER: _ClassVar[int]
    STOPPED_ON_BYTE_CEILING_FIELD_NUMBER: _ClassVar[int]
    TOTAL_EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    next_page_token: str
    resync_required: bool
    projection_version: int
    stopped_on_byte_ceiling: bool
    total_event_count: int
    def __init__(self, next_page_token: _Optional[str] = ..., resync_required: _Optional[bool] = ..., projection_version: _Optional[int] = ..., stopped_on_byte_ceiling: _Optional[bool] = ..., total_event_count: _Optional[int] = ...) -> None: ...

class AgentRunTimelineCostDriverV1(_message.Message):
    __slots__ = ("event_id", "cost", "availability")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    cost: TraceSpanCostV1
    availability: _evaluation_pb2.MetricAvailabilityV1
    def __init__(self, event_id: _Optional[str] = ..., cost: _Optional[_Union[TraceSpanCostV1, _Mapping]] = ..., availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class ListAgentRunEventsRequest(_message.Message):
    __slots__ = ("agent_run_id", "mode", "page_token", "page_size")
    AGENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    agent_run_id: str
    mode: AgentRunTimelineModeV1
    page_token: str
    page_size: int
    def __init__(self, agent_run_id: _Optional[str] = ..., mode: _Optional[_Union[AgentRunTimelineModeV1, str]] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListAgentRunEventsResponse(_message.Message):
    __slots__ = ("agent_run_id", "redirect", "events", "lanes", "mode_effect", "cursor", "completeness", "event_kind_coverage", "artifact_source_coverage", "artifact_diagnostics", "event_score_availability", "downstream_reference_availability", "first_failure", "cost_driver", "window", "boundary", "freshness", "capabilities", "refusal", "run_artifacts")
    AGENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    LANES_FIELD_NUMBER: _ClassVar[int]
    MODE_EFFECT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    COMPLETENESS_FIELD_NUMBER: _ClassVar[int]
    EVENT_KIND_COVERAGE_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_SOURCE_COVERAGE_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    EVENT_SCORE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    DOWNSTREAM_REFERENCE_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    FIRST_FAILURE_FIELD_NUMBER: _ClassVar[int]
    COST_DRIVER_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    RUN_ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    agent_run_id: str
    redirect: _agent_run_pb2.GroupingRedirectV1
    events: _containers.RepeatedCompositeFieldContainer[AgentRunEventV1]
    lanes: _containers.RepeatedCompositeFieldContainer[AgentRunLaneV1]
    mode_effect: AgentRunTimelineModeEffectV1
    cursor: AgentRunTimelineCursorV1
    completeness: _agent_run_pb2.ConversationCompletenessV1
    event_kind_coverage: _containers.RepeatedCompositeFieldContainer[AgentRunEventKindCoverageV1]
    artifact_source_coverage: _containers.RepeatedCompositeFieldContainer[AgentRunArtifactSourceCoverageV1]
    artifact_diagnostics: _containers.RepeatedCompositeFieldContainer[AgentRunArtifactDiagnosticV1]
    event_score_availability: _evaluation_pb2.MetricAvailabilityV1
    downstream_reference_availability: _evaluation_pb2.MetricAvailabilityV1
    first_failure: TraceFirstFailureV1
    cost_driver: AgentRunTimelineCostDriverV1
    window: TraceWindowV1
    boundary: TraceSpanPopulationBoundaryV1
    freshness: _evaluation_pb2.EvaluationFreshnessV1
    capabilities: _evaluation_pb2.AgenticEvaluationCapabilitiesV1
    refusal: TraceReadRefusalV1
    run_artifacts: _containers.RepeatedCompositeFieldContainer[AgentRunArtifactSummaryV1]
    def __init__(self, agent_run_id: _Optional[str] = ..., redirect: _Optional[_Union[_agent_run_pb2.GroupingRedirectV1, _Mapping]] = ..., events: _Optional[_Iterable[_Union[AgentRunEventV1, _Mapping]]] = ..., lanes: _Optional[_Iterable[_Union[AgentRunLaneV1, _Mapping]]] = ..., mode_effect: _Optional[_Union[AgentRunTimelineModeEffectV1, _Mapping]] = ..., cursor: _Optional[_Union[AgentRunTimelineCursorV1, _Mapping]] = ..., completeness: _Optional[_Union[_agent_run_pb2.ConversationCompletenessV1, _Mapping]] = ..., event_kind_coverage: _Optional[_Iterable[_Union[AgentRunEventKindCoverageV1, _Mapping]]] = ..., artifact_source_coverage: _Optional[_Iterable[_Union[AgentRunArtifactSourceCoverageV1, _Mapping]]] = ..., artifact_diagnostics: _Optional[_Iterable[_Union[AgentRunArtifactDiagnosticV1, _Mapping]]] = ..., event_score_availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ..., downstream_reference_availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ..., first_failure: _Optional[_Union[TraceFirstFailureV1, _Mapping]] = ..., cost_driver: _Optional[_Union[AgentRunTimelineCostDriverV1, _Mapping]] = ..., window: _Optional[_Union[TraceWindowV1, _Mapping]] = ..., boundary: _Optional[_Union[TraceSpanPopulationBoundaryV1, _Mapping]] = ..., freshness: _Optional[_Union[_evaluation_pb2.EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[_evaluation_pb2.AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., refusal: _Optional[_Union[TraceReadRefusalV1, _Mapping]] = ..., run_artifacts: _Optional[_Iterable[_Union[AgentRunArtifactSummaryV1, _Mapping]]] = ...) -> None: ...

class RevokeExternalArtifactLinkRequest(_message.Message):
    __slots__ = ("principal", "link_id", "reason_code", "idempotency_key")
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    principal: _evaluation_pb2.PrincipalRefV1
    link_id: bytes
    reason_code: str
    idempotency_key: str
    def __init__(self, principal: _Optional[_Union[_evaluation_pb2.PrincipalRefV1, _Mapping]] = ..., link_id: _Optional[bytes] = ..., reason_code: _Optional[str] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class RevokeExternalArtifactLinkResponse(_message.Message):
    __slots__ = ("link", "correction_sequence", "rejection_reason_code")
    LINK_FIELD_NUMBER: _ClassVar[int]
    CORRECTION_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    REJECTION_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    link: _artifact_pb2.ArtifactLinkV1
    correction_sequence: int
    rejection_reason_code: str
    def __init__(self, link: _Optional[_Union[_artifact_pb2.ArtifactLinkV1, _Mapping]] = ..., correction_sequence: _Optional[int] = ..., rejection_reason_code: _Optional[str] = ...) -> None: ...

class ResolveExternalArtifactLinkRequest(_message.Message):
    __slots__ = ("principal", "link_id")
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    principal: _evaluation_pb2.PrincipalRefV1
    link_id: bytes
    def __init__(self, principal: _Optional[_Union[_evaluation_pb2.PrincipalRefV1, _Mapping]] = ..., link_id: _Optional[bytes] = ...) -> None: ...

class ResolveExternalArtifactLinkResponse(_message.Message):
    __slots__ = ("posture", "reason_code", "attempted_at")
    POSTURE_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    ATTEMPTED_AT_FIELD_NUMBER: _ClassVar[int]
    posture: _artifact_pb2.ArtifactResolverPostureV1
    reason_code: str
    attempted_at: _timestamp_pb2.Timestamp
    def __init__(self, posture: _Optional[_Union[_artifact_pb2.ArtifactResolverPostureV1, str]] = ..., reason_code: _Optional[str] = ..., attempted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AgentTraceRowV1(_message.Message):
    __slots__ = ("trace_id", "started_at", "ended_at", "wall_time_micros", "span_count", "error_count", "agent_count", "model_count", "tool_count", "customer", "deployment", "versions", "agent_run_id")
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    WALL_TIME_MICROS_FIELD_NUMBER: _ClassVar[int]
    SPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    AGENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    MODEL_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOOL_COUNT_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    AGENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    trace_id: str
    started_at: _timestamp_pb2.Timestamp
    ended_at: _timestamp_pb2.Timestamp
    wall_time_micros: int
    span_count: int
    error_count: int
    agent_count: int
    model_count: int
    tool_count: int
    customer: AgentRunDimensionV1
    deployment: AgentRunDimensionV1
    versions: AgentRunVersionContextV1
    agent_run_id: str
    def __init__(self, trace_id: _Optional[str] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ended_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., wall_time_micros: _Optional[int] = ..., span_count: _Optional[int] = ..., error_count: _Optional[int] = ..., agent_count: _Optional[int] = ..., model_count: _Optional[int] = ..., tool_count: _Optional[int] = ..., customer: _Optional[_Union[AgentRunDimensionV1, _Mapping]] = ..., deployment: _Optional[_Union[AgentRunDimensionV1, _Mapping]] = ..., versions: _Optional[_Union[AgentRunVersionContextV1, _Mapping]] = ..., agent_run_id: _Optional[str] = ...) -> None: ...

class ListAgentTracesRequest(_message.Message):
    __slots__ = ("start", "end", "filter", "limit", "page_token")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    filter: _evaluation_pb2.AgentTraceListFilterV1
    limit: int
    page_token: str
    def __init__(self, start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., filter: _Optional[_Union[_evaluation_pb2.AgentTraceListFilterV1, _Mapping]] = ..., limit: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAgentTracesResponse(_message.Message):
    __slots__ = ("traces", "next_page_token", "has_more", "window", "boundary", "cursor_semantics_code", "freshness", "capabilities", "refusal")
    TRACES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    CURSOR_SEMANTICS_CODE_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    REFUSAL_FIELD_NUMBER: _ClassVar[int]
    traces: _containers.RepeatedCompositeFieldContainer[AgentTraceRowV1]
    next_page_token: str
    has_more: bool
    window: TraceWindowV1
    boundary: TraceSpanPopulationBoundaryV1
    cursor_semantics_code: str
    freshness: _evaluation_pb2.EvaluationFreshnessV1
    capabilities: _evaluation_pb2.AgenticEvaluationCapabilitiesV1
    refusal: TraceReadRefusalV1
    def __init__(self, traces: _Optional[_Iterable[_Union[AgentTraceRowV1, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., has_more: _Optional[bool] = ..., window: _Optional[_Union[TraceWindowV1, _Mapping]] = ..., boundary: _Optional[_Union[TraceSpanPopulationBoundaryV1, _Mapping]] = ..., cursor_semantics_code: _Optional[str] = ..., freshness: _Optional[_Union[_evaluation_pb2.EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[_evaluation_pb2.AgenticEvaluationCapabilitiesV1, _Mapping]] = ..., refusal: _Optional[_Union[TraceReadRefusalV1, _Mapping]] = ...) -> None: ...

class TraceInvestigationUnavailableReasonV1(_message.Message):
    __slots__ = ("section", "reason_code", "message", "retryable")
    SECTION_FIELD_NUMBER: _ClassVar[int]
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RETRYABLE_FIELD_NUMBER: _ClassVar[int]
    section: str
    reason_code: str
    message: str
    retryable: bool
    def __init__(self, section: _Optional[str] = ..., reason_code: _Optional[str] = ..., message: _Optional[str] = ..., retryable: _Optional[bool] = ...) -> None: ...

class TraceInvestigationEvidenceLinkV1(_message.Message):
    __slots__ = ("evidence_type", "evidence_id", "trace_id", "span_id", "label")
    EVIDENCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    evidence_type: str
    evidence_id: str
    trace_id: str
    span_id: str
    label: str
    def __init__(self, evidence_type: _Optional[str] = ..., evidence_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., span_id: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...

class AgenticEvidenceGraphNodeV1(_message.Message):
    __slots__ = ("node_id", "node_type", "label", "status", "metadata_json", "evidence_links")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    METADATA_JSON_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_LINKS_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    node_type: str
    label: str
    status: str
    metadata_json: str
    evidence_links: _containers.RepeatedCompositeFieldContainer[TraceInvestigationEvidenceLinkV1]
    def __init__(self, node_id: _Optional[str] = ..., node_type: _Optional[str] = ..., label: _Optional[str] = ..., status: _Optional[str] = ..., metadata_json: _Optional[str] = ..., evidence_links: _Optional[_Iterable[_Union[TraceInvestigationEvidenceLinkV1, _Mapping]]] = ...) -> None: ...

class AgenticEvidenceGraphEdgeV1(_message.Message):
    __slots__ = ("source_node_id", "target_node_id", "relationship")
    SOURCE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    source_node_id: str
    target_node_id: str
    relationship: str
    def __init__(self, source_node_id: _Optional[str] = ..., target_node_id: _Optional[str] = ..., relationship: _Optional[str] = ...) -> None: ...

class AgenticEvidenceGraphV1(_message.Message):
    __slots__ = ("nodes", "edges", "truncated", "unavailable_reasons")
    NODES_FIELD_NUMBER: _ClassVar[int]
    EDGES_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE_REASONS_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[AgenticEvidenceGraphNodeV1]
    edges: _containers.RepeatedCompositeFieldContainer[AgenticEvidenceGraphEdgeV1]
    truncated: bool
    unavailable_reasons: _containers.RepeatedCompositeFieldContainer[TraceInvestigationUnavailableReasonV1]
    def __init__(self, nodes: _Optional[_Iterable[_Union[AgenticEvidenceGraphNodeV1, _Mapping]]] = ..., edges: _Optional[_Iterable[_Union[AgenticEvidenceGraphEdgeV1, _Mapping]]] = ..., truncated: _Optional[bool] = ..., unavailable_reasons: _Optional[_Iterable[_Union[TraceInvestigationUnavailableReasonV1, _Mapping]]] = ...) -> None: ...

class GetAgentEvidenceGraphRequest(_message.Message):
    __slots__ = ("trace_id", "agent_run_id", "node_limit")
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    trace_id: str
    agent_run_id: str
    node_limit: int
    def __init__(self, trace_id: _Optional[str] = ..., agent_run_id: _Optional[str] = ..., node_limit: _Optional[int] = ...) -> None: ...

class GetAgentEvidenceGraphResponse(_message.Message):
    __slots__ = ("graph",)
    GRAPH_FIELD_NUMBER: _ClassVar[int]
    graph: AgenticEvidenceGraphV1
    def __init__(self, graph: _Optional[_Union[AgenticEvidenceGraphV1, _Mapping]] = ...) -> None: ...
