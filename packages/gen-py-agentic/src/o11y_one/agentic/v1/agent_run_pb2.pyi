import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from o11y_one.agentic.v1 import evaluation_pb2 as _evaluation_pb2
from o11y_one.agentic.v1 import artifact_pb2 as _artifact_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AgentRunGroupingConfidenceV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_RUN_GROUPING_CONFIDENCE_V1_UNSPECIFIED: _ClassVar[AgentRunGroupingConfidenceV1]
    AGENT_RUN_GROUPING_CONFIDENCE_V1_EXPLICIT: _ClassVar[AgentRunGroupingConfidenceV1]
    AGENT_RUN_GROUPING_CONFIDENCE_V1_EXPLICIT_PARTIAL: _ClassVar[AgentRunGroupingConfidenceV1]
    AGENT_RUN_GROUPING_CONFIDENCE_V1_DERIVED: _ClassVar[AgentRunGroupingConfidenceV1]
    AGENT_RUN_GROUPING_CONFIDENCE_V1_PROVISIONAL: _ClassVar[AgentRunGroupingConfidenceV1]
    AGENT_RUN_GROUPING_CONFIDENCE_V1_UNGROUPED: _ClassVar[AgentRunGroupingConfidenceV1]
    AGENT_RUN_GROUPING_CONFIDENCE_V1_CONFIRMED: _ClassVar[AgentRunGroupingConfidenceV1]

class AgentRunGroupingStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_RUN_GROUPING_STATE_V1_UNSPECIFIED: _ClassVar[AgentRunGroupingStateV1]
    AGENT_RUN_GROUPING_STATE_V1_CURRENT: _ClassVar[AgentRunGroupingStateV1]
    AGENT_RUN_GROUPING_STATE_V1_MERGED_AWAY: _ClassVar[AgentRunGroupingStateV1]
    AGENT_RUN_GROUPING_STATE_V1_SPLIT_AWAY: _ClassVar[AgentRunGroupingStateV1]
    AGENT_RUN_GROUPING_STATE_V1_REDIRECTED: _ClassVar[AgentRunGroupingStateV1]

class ConversationCompletenessStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONVERSATION_COMPLETENESS_STATE_V1_UNSPECIFIED: _ClassVar[ConversationCompletenessStateV1]
    CONVERSATION_COMPLETENESS_STATE_V1_OPEN: _ClassVar[ConversationCompletenessStateV1]
    CONVERSATION_COMPLETENESS_STATE_V1_INACTIVE: _ClassVar[ConversationCompletenessStateV1]
    CONVERSATION_COMPLETENESS_STATE_V1_COMPLETE: _ClassVar[ConversationCompletenessStateV1]
    CONVERSATION_COMPLETENESS_STATE_V1_REOPENED: _ClassVar[ConversationCompletenessStateV1]

class AgentRunGroupingSignalKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_RUN_GROUPING_SIGNAL_KIND_V1_UNSPECIFIED: _ClassVar[AgentRunGroupingSignalKindV1]
    AGENT_RUN_GROUPING_SIGNAL_KIND_V1_OFFICIAL_CONVERSATION_ID: _ClassVar[AgentRunGroupingSignalKindV1]
    AGENT_RUN_GROUPING_SIGNAL_KIND_V1_SPAN_LINK: _ClassVar[AgentRunGroupingSignalKindV1]
    AGENT_RUN_GROUPING_SIGNAL_KIND_V1_CONTROL_PLANE_CONVERSATION_ID: _ClassVar[AgentRunGroupingSignalKindV1]
    AGENT_RUN_GROUPING_SIGNAL_KIND_V1_BOUNDED_HEURISTIC: _ClassVar[AgentRunGroupingSignalKindV1]
    AGENT_RUN_GROUPING_SIGNAL_KIND_V1_NO_IDENTITY: _ClassVar[AgentRunGroupingSignalKindV1]

class AgentRunGroupingRedirectReasonV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_RUN_GROUPING_REDIRECT_REASON_V1_UNSPECIFIED: _ClassVar[AgentRunGroupingRedirectReasonV1]
    AGENT_RUN_GROUPING_REDIRECT_REASON_V1_LATE_EXPLICIT_IDENTITY_MERGE: _ClassVar[AgentRunGroupingRedirectReasonV1]
    AGENT_RUN_GROUPING_REDIRECT_REASON_V1_LATE_EXPLICIT_IDENTITY_SPLIT: _ClassVar[AgentRunGroupingRedirectReasonV1]
    AGENT_RUN_GROUPING_REDIRECT_REASON_V1_BOUND_BREACH_SPLIT: _ClassVar[AgentRunGroupingRedirectReasonV1]
    AGENT_RUN_GROUPING_REDIRECT_REASON_V1_HEURISTIC_REGROUPED: _ClassVar[AgentRunGroupingRedirectReasonV1]

class AgentRunGroupingConfirmationReasonV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_RUN_GROUPING_CONFIRMATION_REASON_V1_UNSPECIFIED: _ClassVar[AgentRunGroupingConfirmationReasonV1]
    AGENT_RUN_GROUPING_CONFIRMATION_REASON_V1_OPERATOR_VERIFIED_SAME_CONVERSATION: _ClassVar[AgentRunGroupingConfirmationReasonV1]
    AGENT_RUN_GROUPING_CONFIRMATION_REASON_V1_INSTRUMENTATION_GAP_ACKNOWLEDGED: _ClassVar[AgentRunGroupingConfirmationReasonV1]
    AGENT_RUN_GROUPING_CONFIRMATION_REASON_V1_INCIDENT_INVESTIGATION: _ClassVar[AgentRunGroupingConfirmationReasonV1]

class AgentRunAuthorityCapabilityV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_RUN_AUTHORITY_CAPABILITY_V1_UNSPECIFIED: _ClassVar[AgentRunAuthorityCapabilityV1]
    AGENT_RUN_AUTHORITY_CAPABILITY_V1_RENDER: _ClassVar[AgentRunAuthorityCapabilityV1]
    AGENT_RUN_AUTHORITY_CAPABILITY_V1_MANUAL_DRAFT_SELECTION: _ClassVar[AgentRunAuthorityCapabilityV1]
    AGENT_RUN_AUTHORITY_CAPABILITY_V1_AUTOMATIC_LINEAGE: _ClassVar[AgentRunAuthorityCapabilityV1]
    AGENT_RUN_AUTHORITY_CAPABILITY_V1_PRODUCTION_RULE_TRIGGER: _ClassVar[AgentRunAuthorityCapabilityV1]
    AGENT_RUN_AUTHORITY_CAPABILITY_V1_CONVERSATION_SUBJECT_SCORING: _ClassVar[AgentRunAuthorityCapabilityV1]
    AGENT_RUN_AUTHORITY_CAPABILITY_V1_RELEASE_EVIDENCE: _ClassVar[AgentRunAuthorityCapabilityV1]
AGENT_RUN_GROUPING_CONFIDENCE_V1_UNSPECIFIED: AgentRunGroupingConfidenceV1
AGENT_RUN_GROUPING_CONFIDENCE_V1_EXPLICIT: AgentRunGroupingConfidenceV1
AGENT_RUN_GROUPING_CONFIDENCE_V1_EXPLICIT_PARTIAL: AgentRunGroupingConfidenceV1
AGENT_RUN_GROUPING_CONFIDENCE_V1_DERIVED: AgentRunGroupingConfidenceV1
AGENT_RUN_GROUPING_CONFIDENCE_V1_PROVISIONAL: AgentRunGroupingConfidenceV1
AGENT_RUN_GROUPING_CONFIDENCE_V1_UNGROUPED: AgentRunGroupingConfidenceV1
AGENT_RUN_GROUPING_CONFIDENCE_V1_CONFIRMED: AgentRunGroupingConfidenceV1
AGENT_RUN_GROUPING_STATE_V1_UNSPECIFIED: AgentRunGroupingStateV1
AGENT_RUN_GROUPING_STATE_V1_CURRENT: AgentRunGroupingStateV1
AGENT_RUN_GROUPING_STATE_V1_MERGED_AWAY: AgentRunGroupingStateV1
AGENT_RUN_GROUPING_STATE_V1_SPLIT_AWAY: AgentRunGroupingStateV1
AGENT_RUN_GROUPING_STATE_V1_REDIRECTED: AgentRunGroupingStateV1
CONVERSATION_COMPLETENESS_STATE_V1_UNSPECIFIED: ConversationCompletenessStateV1
CONVERSATION_COMPLETENESS_STATE_V1_OPEN: ConversationCompletenessStateV1
CONVERSATION_COMPLETENESS_STATE_V1_INACTIVE: ConversationCompletenessStateV1
CONVERSATION_COMPLETENESS_STATE_V1_COMPLETE: ConversationCompletenessStateV1
CONVERSATION_COMPLETENESS_STATE_V1_REOPENED: ConversationCompletenessStateV1
AGENT_RUN_GROUPING_SIGNAL_KIND_V1_UNSPECIFIED: AgentRunGroupingSignalKindV1
AGENT_RUN_GROUPING_SIGNAL_KIND_V1_OFFICIAL_CONVERSATION_ID: AgentRunGroupingSignalKindV1
AGENT_RUN_GROUPING_SIGNAL_KIND_V1_SPAN_LINK: AgentRunGroupingSignalKindV1
AGENT_RUN_GROUPING_SIGNAL_KIND_V1_CONTROL_PLANE_CONVERSATION_ID: AgentRunGroupingSignalKindV1
AGENT_RUN_GROUPING_SIGNAL_KIND_V1_BOUNDED_HEURISTIC: AgentRunGroupingSignalKindV1
AGENT_RUN_GROUPING_SIGNAL_KIND_V1_NO_IDENTITY: AgentRunGroupingSignalKindV1
AGENT_RUN_GROUPING_REDIRECT_REASON_V1_UNSPECIFIED: AgentRunGroupingRedirectReasonV1
AGENT_RUN_GROUPING_REDIRECT_REASON_V1_LATE_EXPLICIT_IDENTITY_MERGE: AgentRunGroupingRedirectReasonV1
AGENT_RUN_GROUPING_REDIRECT_REASON_V1_LATE_EXPLICIT_IDENTITY_SPLIT: AgentRunGroupingRedirectReasonV1
AGENT_RUN_GROUPING_REDIRECT_REASON_V1_BOUND_BREACH_SPLIT: AgentRunGroupingRedirectReasonV1
AGENT_RUN_GROUPING_REDIRECT_REASON_V1_HEURISTIC_REGROUPED: AgentRunGroupingRedirectReasonV1
AGENT_RUN_GROUPING_CONFIRMATION_REASON_V1_UNSPECIFIED: AgentRunGroupingConfirmationReasonV1
AGENT_RUN_GROUPING_CONFIRMATION_REASON_V1_OPERATOR_VERIFIED_SAME_CONVERSATION: AgentRunGroupingConfirmationReasonV1
AGENT_RUN_GROUPING_CONFIRMATION_REASON_V1_INSTRUMENTATION_GAP_ACKNOWLEDGED: AgentRunGroupingConfirmationReasonV1
AGENT_RUN_GROUPING_CONFIRMATION_REASON_V1_INCIDENT_INVESTIGATION: AgentRunGroupingConfirmationReasonV1
AGENT_RUN_AUTHORITY_CAPABILITY_V1_UNSPECIFIED: AgentRunAuthorityCapabilityV1
AGENT_RUN_AUTHORITY_CAPABILITY_V1_RENDER: AgentRunAuthorityCapabilityV1
AGENT_RUN_AUTHORITY_CAPABILITY_V1_MANUAL_DRAFT_SELECTION: AgentRunAuthorityCapabilityV1
AGENT_RUN_AUTHORITY_CAPABILITY_V1_AUTOMATIC_LINEAGE: AgentRunAuthorityCapabilityV1
AGENT_RUN_AUTHORITY_CAPABILITY_V1_PRODUCTION_RULE_TRIGGER: AgentRunAuthorityCapabilityV1
AGENT_RUN_AUTHORITY_CAPABILITY_V1_CONVERSATION_SUBJECT_SCORING: AgentRunAuthorityCapabilityV1
AGENT_RUN_AUTHORITY_CAPABILITY_V1_RELEASE_EVIDENCE: AgentRunAuthorityCapabilityV1

class GroupingConfidenceInputV1(_message.Message):
    __slots__ = ("signal_kind", "observed_on_member_count", "total_member_count", "contributed_rung", "availability")
    SIGNAL_KIND_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_ON_MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONTRIBUTED_RUNG_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    signal_kind: AgentRunGroupingSignalKindV1
    observed_on_member_count: int
    total_member_count: int
    contributed_rung: AgentRunGroupingConfidenceV1
    availability: _evaluation_pb2.MetricAvailabilityV1
    def __init__(self, signal_kind: _Optional[_Union[AgentRunGroupingSignalKindV1, str]] = ..., observed_on_member_count: _Optional[int] = ..., total_member_count: _Optional[int] = ..., contributed_rung: _Optional[_Union[AgentRunGroupingConfidenceV1, str]] = ..., availability: _Optional[_Union[_evaluation_pb2.MetricAvailabilityV1, _Mapping]] = ...) -> None: ...

class GroupingRedirectV1(_message.Message):
    __slots__ = ("from_id", "to_ids", "reason", "revision", "occurred_at")
    FROM_ID_FIELD_NUMBER: _ClassVar[int]
    TO_IDS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    from_id: str
    to_ids: _containers.RepeatedScalarFieldContainer[str]
    reason: AgentRunGroupingRedirectReasonV1
    revision: int
    occurred_at: _timestamp_pb2.Timestamp
    def __init__(self, from_id: _Optional[str] = ..., to_ids: _Optional[_Iterable[str]] = ..., reason: _Optional[_Union[AgentRunGroupingRedirectReasonV1, str]] = ..., revision: _Optional[int] = ..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AgentRunGroupingBoundsV1(_message.Message):
    __slots__ = ("max_member_traces", "max_wall_clock_seconds", "max_inactivity_gap_seconds", "max_lookback_hours", "max_spans_per_member_trace", "max_member_span_ceiling")
    MAX_MEMBER_TRACES_FIELD_NUMBER: _ClassVar[int]
    MAX_WALL_CLOCK_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MAX_INACTIVITY_GAP_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MAX_LOOKBACK_HOURS_FIELD_NUMBER: _ClassVar[int]
    MAX_SPANS_PER_MEMBER_TRACE_FIELD_NUMBER: _ClassVar[int]
    MAX_MEMBER_SPAN_CEILING_FIELD_NUMBER: _ClassVar[int]
    max_member_traces: int
    max_wall_clock_seconds: int
    max_inactivity_gap_seconds: int
    max_lookback_hours: int
    max_spans_per_member_trace: int
    max_member_span_ceiling: int
    def __init__(self, max_member_traces: _Optional[int] = ..., max_wall_clock_seconds: _Optional[int] = ..., max_inactivity_gap_seconds: _Optional[int] = ..., max_lookback_hours: _Optional[int] = ..., max_spans_per_member_trace: _Optional[int] = ..., max_member_span_ceiling: _Optional[int] = ...) -> None: ...

class AgentRunGroupingConfirmationV1(_message.Message):
    __slots__ = ("confirmed_by", "reason", "reason_note", "confirmed_at", "revision")
    CONFIRMED_BY_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    REASON_NOTE_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_AT_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    confirmed_by: _evaluation_pb2.PrincipalRefV1
    reason: AgentRunGroupingConfirmationReasonV1
    reason_note: str
    confirmed_at: _timestamp_pb2.Timestamp
    revision: int
    def __init__(self, confirmed_by: _Optional[_Union[_evaluation_pb2.PrincipalRefV1, _Mapping]] = ..., reason: _Optional[_Union[AgentRunGroupingConfirmationReasonV1, str]] = ..., reason_note: _Optional[str] = ..., confirmed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., revision: _Optional[int] = ...) -> None: ...

class AgentRunAnchorRebindV1(_message.Message):
    __slots__ = ("anchor", "original_agent_run_id", "agent_run_id", "revision", "reason", "occurred_at")
    ANCHOR_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_AGENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    anchor: _artifact_pb2.EvidenceAnchorV1
    original_agent_run_id: str
    agent_run_id: str
    revision: int
    reason: AgentRunGroupingRedirectReasonV1
    occurred_at: _timestamp_pb2.Timestamp
    def __init__(self, anchor: _Optional[_Union[_artifact_pb2.EvidenceAnchorV1, _Mapping]] = ..., original_agent_run_id: _Optional[str] = ..., agent_run_id: _Optional[str] = ..., revision: _Optional[int] = ..., reason: _Optional[_Union[AgentRunGroupingRedirectReasonV1, str]] = ..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AgentRunGroupingV1(_message.Message):
    __slots__ = ("agent_run_id", "state", "confidence", "attached_rung", "revision", "confidence_inputs", "conversation_id", "member_trace_count", "bounds", "redirect", "confirmation", "projection_version", "anchor_rebinds")
    AGENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_RUNG_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_INPUTS_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_TRACE_COUNT_FIELD_NUMBER: _ClassVar[int]
    BOUNDS_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_FIELD_NUMBER: _ClassVar[int]
    CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_VERSION_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_REBINDS_FIELD_NUMBER: _ClassVar[int]
    agent_run_id: str
    state: AgentRunGroupingStateV1
    confidence: AgentRunGroupingConfidenceV1
    attached_rung: int
    revision: int
    confidence_inputs: _containers.RepeatedCompositeFieldContainer[GroupingConfidenceInputV1]
    conversation_id: str
    member_trace_count: int
    bounds: AgentRunGroupingBoundsV1
    redirect: GroupingRedirectV1
    confirmation: AgentRunGroupingConfirmationV1
    projection_version: int
    anchor_rebinds: _containers.RepeatedCompositeFieldContainer[AgentRunAnchorRebindV1]
    def __init__(self, agent_run_id: _Optional[str] = ..., state: _Optional[_Union[AgentRunGroupingStateV1, str]] = ..., confidence: _Optional[_Union[AgentRunGroupingConfidenceV1, str]] = ..., attached_rung: _Optional[int] = ..., revision: _Optional[int] = ..., confidence_inputs: _Optional[_Iterable[_Union[GroupingConfidenceInputV1, _Mapping]]] = ..., conversation_id: _Optional[str] = ..., member_trace_count: _Optional[int] = ..., bounds: _Optional[_Union[AgentRunGroupingBoundsV1, _Mapping]] = ..., redirect: _Optional[_Union[GroupingRedirectV1, _Mapping]] = ..., confirmation: _Optional[_Union[AgentRunGroupingConfirmationV1, _Mapping]] = ..., projection_version: _Optional[int] = ..., anchor_rebinds: _Optional[_Iterable[_Union[AgentRunAnchorRebindV1, _Mapping]]] = ...) -> None: ...

class ConversationCompletenessV1(_message.Message):
    __slots__ = ("state", "epoch", "last_seen_at", "inactivity_window_seconds", "late_arrival_grace_seconds", "superseded_eligible", "evaluated_at")
    STATE_FIELD_NUMBER: _ClassVar[int]
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    INACTIVITY_WINDOW_SECONDS_FIELD_NUMBER: _ClassVar[int]
    LATE_ARRIVAL_GRACE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SUPERSEDED_ELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    EVALUATED_AT_FIELD_NUMBER: _ClassVar[int]
    state: ConversationCompletenessStateV1
    epoch: int
    last_seen_at: _timestamp_pb2.Timestamp
    inactivity_window_seconds: int
    late_arrival_grace_seconds: int
    superseded_eligible: bool
    evaluated_at: _timestamp_pb2.Timestamp
    def __init__(self, state: _Optional[_Union[ConversationCompletenessStateV1, str]] = ..., epoch: _Optional[int] = ..., last_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., inactivity_window_seconds: _Optional[int] = ..., late_arrival_grace_seconds: _Optional[int] = ..., superseded_eligible: _Optional[bool] = ..., evaluated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ConfirmAgentRunGroupingRequest(_message.Message):
    __slots__ = ("agent_run_id", "reason", "reason_note", "idempotency_key")
    AGENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    REASON_NOTE_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    agent_run_id: str
    reason: AgentRunGroupingConfirmationReasonV1
    reason_note: str
    idempotency_key: str
    def __init__(self, agent_run_id: _Optional[str] = ..., reason: _Optional[_Union[AgentRunGroupingConfirmationReasonV1, str]] = ..., reason_note: _Optional[str] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class ConfirmAgentRunGroupingResponse(_message.Message):
    __slots__ = ("grouping", "idempotent_replay", "completeness", "freshness", "capabilities")
    GROUPING_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENT_REPLAY_FIELD_NUMBER: _ClassVar[int]
    COMPLETENESS_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    grouping: AgentRunGroupingV1
    idempotent_replay: bool
    completeness: ConversationCompletenessV1
    freshness: _evaluation_pb2.EvaluationFreshnessV1
    capabilities: _evaluation_pb2.AgenticEvaluationCapabilitiesV1
    def __init__(self, grouping: _Optional[_Union[AgentRunGroupingV1, _Mapping]] = ..., idempotent_replay: _Optional[bool] = ..., completeness: _Optional[_Union[ConversationCompletenessV1, _Mapping]] = ..., freshness: _Optional[_Union[_evaluation_pb2.EvaluationFreshnessV1, _Mapping]] = ..., capabilities: _Optional[_Union[_evaluation_pb2.AgenticEvaluationCapabilitiesV1, _Mapping]] = ...) -> None: ...
