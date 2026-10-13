import datetime

from o11y_one.agentic.v1 import environment_pb2 as _environment_pb2
from o11y_one.common.v1 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoopTrainerFrameworkV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOOP_TRAINER_FRAMEWORK_V1_UNSPECIFIED: _ClassVar[LoopTrainerFrameworkV1]
    LOOP_TRAINER_FRAMEWORK_V1_TINKER: _ClassVar[LoopTrainerFrameworkV1]
    LOOP_TRAINER_FRAMEWORK_V1_VERL: _ClassVar[LoopTrainerFrameworkV1]
    LOOP_TRAINER_FRAMEWORK_V1_TRL: _ClassVar[LoopTrainerFrameworkV1]
    LOOP_TRAINER_FRAMEWORK_V1_OPENRLHF: _ClassVar[LoopTrainerFrameworkV1]
    LOOP_TRAINER_FRAMEWORK_V1_OTHER: _ClassVar[LoopTrainerFrameworkV1]

class LoopRunStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOOP_RUN_STATE_V1_UNSPECIFIED: _ClassVar[LoopRunStateV1]
    LOOP_RUN_STATE_V1_STOPPED: _ClassVar[LoopRunStateV1]
    LOOP_RUN_STATE_V1_ABANDONED: _ClassVar[LoopRunStateV1]
    LOOP_RUN_STATE_V1_FINISHED: _ClassVar[LoopRunStateV1]
    LOOP_RUN_STATE_V1_PAUSED: _ClassVar[LoopRunStateV1]
    LOOP_RUN_STATE_V1_WAITING: _ClassVar[LoopRunStateV1]
    LOOP_RUN_STATE_V1_AT_SPEND_CAP: _ClassVar[LoopRunStateV1]
    LOOP_RUN_STATE_V1_CREDENTIAL_REVOKED: _ClassVar[LoopRunStateV1]
    LOOP_RUN_STATE_V1_SILENT: _ClassVar[LoopRunStateV1]
    LOOP_RUN_STATE_V1_AT_ENVIRONMENT_LIMIT: _ClassVar[LoopRunStateV1]
    LOOP_RUN_STATE_V1_IDLE: _ClassVar[LoopRunStateV1]
    LOOP_RUN_STATE_V1_RUNNING: _ClassVar[LoopRunStateV1]

class LoopFailureClassV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOOP_FAILURE_CLASS_V1_UNSPECIFIED: _ClassVar[LoopFailureClassV1]
    LOOP_FAILURE_CLASS_V1_TASK: _ClassVar[LoopFailureClassV1]
    LOOP_FAILURE_CLASS_V1_VERIFIER: _ClassVar[LoopFailureClassV1]
    LOOP_FAILURE_CLASS_V1_INFRASTRUCTURE: _ClassVar[LoopFailureClassV1]
    LOOP_FAILURE_CLASS_V1_CANCELLED: _ClassVar[LoopFailureClassV1]

class LoopVerdictV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOOP_VERDICT_V1_UNSPECIFIED: _ClassVar[LoopVerdictV1]
    LOOP_VERDICT_V1_PASS: _ClassVar[LoopVerdictV1]
    LOOP_VERDICT_V1_FAIL: _ClassVar[LoopVerdictV1]
    LOOP_VERDICT_V1_PARTIAL: _ClassVar[LoopVerdictV1]

class LoopRewardDeterminismV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOOP_REWARD_DETERMINISM_V1_UNSPECIFIED: _ClassVar[LoopRewardDeterminismV1]
    LOOP_REWARD_DETERMINISM_V1_OFFLINE_PINNED: _ClassVar[LoopRewardDeterminismV1]

class LoopRolloutStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOOP_ROLLOUT_STATE_V1_UNSPECIFIED: _ClassVar[LoopRolloutStateV1]
    LOOP_ROLLOUT_STATE_V1_STARTING: _ClassVar[LoopRolloutStateV1]
    LOOP_ROLLOUT_STATE_V1_RUNNING: _ClassVar[LoopRolloutStateV1]
    LOOP_ROLLOUT_STATE_V1_CLOSING: _ClassVar[LoopRolloutStateV1]
    LOOP_ROLLOUT_STATE_V1_REWARDED: _ClassVar[LoopRolloutStateV1]
    LOOP_ROLLOUT_STATE_V1_FAILED: _ClassVar[LoopRolloutStateV1]
    LOOP_ROLLOUT_STATE_V1_CANCELLED: _ClassVar[LoopRolloutStateV1]

class LoopToolEntryKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOOP_TOOL_ENTRY_KIND_V1_UNSPECIFIED: _ClassVar[LoopToolEntryKindV1]
    LOOP_TOOL_ENTRY_KIND_V1_FILE: _ClassVar[LoopToolEntryKindV1]
    LOOP_TOOL_ENTRY_KIND_V1_DIRECTORY: _ClassVar[LoopToolEntryKindV1]
    LOOP_TOOL_ENTRY_KIND_V1_SYMLINK: _ClassVar[LoopToolEntryKindV1]
    LOOP_TOOL_ENTRY_KIND_V1_OTHER: _ClassVar[LoopToolEntryKindV1]

class LoopRolloutGroupFilterV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOOP_ROLLOUT_GROUP_FILTER_V1_UNSPECIFIED: _ClassVar[LoopRolloutGroupFilterV1]
    LOOP_ROLLOUT_GROUP_FILTER_V1_OPEN: _ClassVar[LoopRolloutGroupFilterV1]
    LOOP_ROLLOUT_GROUP_FILTER_V1_WITHOUT_SPREAD: _ClassVar[LoopRolloutGroupFilterV1]
    LOOP_ROLLOUT_GROUP_FILTER_V1_WITH_FAILURES: _ClassVar[LoopRolloutGroupFilterV1]

class LoopChangeKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOOP_CHANGE_KIND_V1_UNSPECIFIED: _ClassVar[LoopChangeKindV1]
    LOOP_CHANGE_KIND_V1_FILE: _ClassVar[LoopChangeKindV1]
    LOOP_CHANGE_KIND_V1_DIRECTORY: _ClassVar[LoopChangeKindV1]
    LOOP_CHANGE_KIND_V1_SYMLINK: _ClassVar[LoopChangeKindV1]
    LOOP_CHANGE_KIND_V1_WHITEOUT: _ClassVar[LoopChangeKindV1]
    LOOP_CHANGE_KIND_V1_OTHER: _ClassVar[LoopChangeKindV1]
    LOOP_CHANGE_KIND_V1_OPAQUE_DIRECTORY: _ClassVar[LoopChangeKindV1]

class LoopRunStepBucketV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOOP_RUN_STEP_BUCKET_V1_UNSPECIFIED: _ClassVar[LoopRunStepBucketV1]
    LOOP_RUN_STEP_BUCKET_V1_TRAINER_STEP: _ClassVar[LoopRunStepBucketV1]
    LOOP_RUN_STEP_BUCKET_V1_MINUTE: _ClassVar[LoopRunStepBucketV1]
    LOOP_RUN_STEP_BUCKET_V1_FIVE_MINUTES: _ClassVar[LoopRunStepBucketV1]
LOOP_TRAINER_FRAMEWORK_V1_UNSPECIFIED: LoopTrainerFrameworkV1
LOOP_TRAINER_FRAMEWORK_V1_TINKER: LoopTrainerFrameworkV1
LOOP_TRAINER_FRAMEWORK_V1_VERL: LoopTrainerFrameworkV1
LOOP_TRAINER_FRAMEWORK_V1_TRL: LoopTrainerFrameworkV1
LOOP_TRAINER_FRAMEWORK_V1_OPENRLHF: LoopTrainerFrameworkV1
LOOP_TRAINER_FRAMEWORK_V1_OTHER: LoopTrainerFrameworkV1
LOOP_RUN_STATE_V1_UNSPECIFIED: LoopRunStateV1
LOOP_RUN_STATE_V1_STOPPED: LoopRunStateV1
LOOP_RUN_STATE_V1_ABANDONED: LoopRunStateV1
LOOP_RUN_STATE_V1_FINISHED: LoopRunStateV1
LOOP_RUN_STATE_V1_PAUSED: LoopRunStateV1
LOOP_RUN_STATE_V1_WAITING: LoopRunStateV1
LOOP_RUN_STATE_V1_AT_SPEND_CAP: LoopRunStateV1
LOOP_RUN_STATE_V1_CREDENTIAL_REVOKED: LoopRunStateV1
LOOP_RUN_STATE_V1_SILENT: LoopRunStateV1
LOOP_RUN_STATE_V1_AT_ENVIRONMENT_LIMIT: LoopRunStateV1
LOOP_RUN_STATE_V1_IDLE: LoopRunStateV1
LOOP_RUN_STATE_V1_RUNNING: LoopRunStateV1
LOOP_FAILURE_CLASS_V1_UNSPECIFIED: LoopFailureClassV1
LOOP_FAILURE_CLASS_V1_TASK: LoopFailureClassV1
LOOP_FAILURE_CLASS_V1_VERIFIER: LoopFailureClassV1
LOOP_FAILURE_CLASS_V1_INFRASTRUCTURE: LoopFailureClassV1
LOOP_FAILURE_CLASS_V1_CANCELLED: LoopFailureClassV1
LOOP_VERDICT_V1_UNSPECIFIED: LoopVerdictV1
LOOP_VERDICT_V1_PASS: LoopVerdictV1
LOOP_VERDICT_V1_FAIL: LoopVerdictV1
LOOP_VERDICT_V1_PARTIAL: LoopVerdictV1
LOOP_REWARD_DETERMINISM_V1_UNSPECIFIED: LoopRewardDeterminismV1
LOOP_REWARD_DETERMINISM_V1_OFFLINE_PINNED: LoopRewardDeterminismV1
LOOP_ROLLOUT_STATE_V1_UNSPECIFIED: LoopRolloutStateV1
LOOP_ROLLOUT_STATE_V1_STARTING: LoopRolloutStateV1
LOOP_ROLLOUT_STATE_V1_RUNNING: LoopRolloutStateV1
LOOP_ROLLOUT_STATE_V1_CLOSING: LoopRolloutStateV1
LOOP_ROLLOUT_STATE_V1_REWARDED: LoopRolloutStateV1
LOOP_ROLLOUT_STATE_V1_FAILED: LoopRolloutStateV1
LOOP_ROLLOUT_STATE_V1_CANCELLED: LoopRolloutStateV1
LOOP_TOOL_ENTRY_KIND_V1_UNSPECIFIED: LoopToolEntryKindV1
LOOP_TOOL_ENTRY_KIND_V1_FILE: LoopToolEntryKindV1
LOOP_TOOL_ENTRY_KIND_V1_DIRECTORY: LoopToolEntryKindV1
LOOP_TOOL_ENTRY_KIND_V1_SYMLINK: LoopToolEntryKindV1
LOOP_TOOL_ENTRY_KIND_V1_OTHER: LoopToolEntryKindV1
LOOP_ROLLOUT_GROUP_FILTER_V1_UNSPECIFIED: LoopRolloutGroupFilterV1
LOOP_ROLLOUT_GROUP_FILTER_V1_OPEN: LoopRolloutGroupFilterV1
LOOP_ROLLOUT_GROUP_FILTER_V1_WITHOUT_SPREAD: LoopRolloutGroupFilterV1
LOOP_ROLLOUT_GROUP_FILTER_V1_WITH_FAILURES: LoopRolloutGroupFilterV1
LOOP_CHANGE_KIND_V1_UNSPECIFIED: LoopChangeKindV1
LOOP_CHANGE_KIND_V1_FILE: LoopChangeKindV1
LOOP_CHANGE_KIND_V1_DIRECTORY: LoopChangeKindV1
LOOP_CHANGE_KIND_V1_SYMLINK: LoopChangeKindV1
LOOP_CHANGE_KIND_V1_WHITEOUT: LoopChangeKindV1
LOOP_CHANGE_KIND_V1_OTHER: LoopChangeKindV1
LOOP_CHANGE_KIND_V1_OPAQUE_DIRECTORY: LoopChangeKindV1
LOOP_RUN_STEP_BUCKET_V1_UNSPECIFIED: LoopRunStepBucketV1
LOOP_RUN_STEP_BUCKET_V1_TRAINER_STEP: LoopRunStepBucketV1
LOOP_RUN_STEP_BUCKET_V1_MINUTE: LoopRunStepBucketV1
LOOP_RUN_STEP_BUCKET_V1_FIVE_MINUTES: LoopRunStepBucketV1

class LoopClientV1(_message.Message):
    __slots__ = ("sdk_version", "adapter", "adapter_version", "framework_version", "session_id")
    SDK_VERSION_FIELD_NUMBER: _ClassVar[int]
    ADAPTER_FIELD_NUMBER: _ClassVar[int]
    ADAPTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    FRAMEWORK_VERSION_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    sdk_version: str
    adapter: str
    adapter_version: str
    framework_version: str
    session_id: str
    def __init__(self, sdk_version: _Optional[str] = ..., adapter: _Optional[str] = ..., adapter_version: _Optional[str] = ..., framework_version: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class LoopRunV1(_message.Message):
    __slots__ = ("run_id", "name", "framework", "environment_id", "environment_version", "dataset_version_id", "group_size", "environment_limit", "spend_cap_cents", "state", "experiment_name", "client", "base_snapshot_id", "credential_prefix", "client_sessions", "created_at", "first_reset_at", "first_group_start_millis", "first_reward_at", "first_reward", "last_call_at", "paused_at", "ended_at", "environment_name", "dataset_name", "dataset_version")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FRAMEWORK_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_SIZE_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    SPEND_CAP_CENTS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    BASE_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_PREFIX_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    FIRST_RESET_AT_FIELD_NUMBER: _ClassVar[int]
    FIRST_GROUP_START_MILLIS_FIELD_NUMBER: _ClassVar[int]
    FIRST_REWARD_AT_FIELD_NUMBER: _ClassVar[int]
    FIRST_REWARD_FIELD_NUMBER: _ClassVar[int]
    LAST_CALL_AT_FIELD_NUMBER: _ClassVar[int]
    PAUSED_AT_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    DATASET_NAME_FIELD_NUMBER: _ClassVar[int]
    DATASET_VERSION_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    name: str
    framework: LoopTrainerFrameworkV1
    environment_id: str
    environment_version: int
    dataset_version_id: str
    group_size: int
    environment_limit: int
    spend_cap_cents: int
    state: LoopRunStateV1
    experiment_name: str
    client: LoopClientV1
    base_snapshot_id: bytes
    credential_prefix: str
    client_sessions: int
    created_at: _timestamp_pb2.Timestamp
    first_reset_at: _timestamp_pb2.Timestamp
    first_group_start_millis: int
    first_reward_at: _timestamp_pb2.Timestamp
    first_reward: float
    last_call_at: _timestamp_pb2.Timestamp
    paused_at: _timestamp_pb2.Timestamp
    ended_at: _timestamp_pb2.Timestamp
    environment_name: str
    dataset_name: str
    dataset_version: int
    def __init__(self, run_id: _Optional[str] = ..., name: _Optional[str] = ..., framework: _Optional[_Union[LoopTrainerFrameworkV1, str]] = ..., environment_id: _Optional[str] = ..., environment_version: _Optional[int] = ..., dataset_version_id: _Optional[str] = ..., group_size: _Optional[int] = ..., environment_limit: _Optional[int] = ..., spend_cap_cents: _Optional[int] = ..., state: _Optional[_Union[LoopRunStateV1, str]] = ..., experiment_name: _Optional[str] = ..., client: _Optional[_Union[LoopClientV1, _Mapping]] = ..., base_snapshot_id: _Optional[bytes] = ..., credential_prefix: _Optional[str] = ..., client_sessions: _Optional[int] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., first_reset_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., first_group_start_millis: _Optional[int] = ..., first_reward_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., first_reward: _Optional[float] = ..., last_call_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., paused_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ended_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., environment_name: _Optional[str] = ..., dataset_name: _Optional[str] = ..., dataset_version: _Optional[int] = ...) -> None: ...

class LoopEnvironmentUsageV1(_message.Message):
    __slots__ = ("open", "plan_limit")
    OPEN_FIELD_NUMBER: _ClassVar[int]
    PLAN_LIMIT_FIELD_NUMBER: _ClassVar[int]
    open: int
    plan_limit: int
    def __init__(self, open: _Optional[int] = ..., plan_limit: _Optional[int] = ...) -> None: ...

class LoopRolloutFailureV1(_message.Message):
    __slots__ = ("failure_class", "code")
    FAILURE_CLASS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    failure_class: LoopFailureClassV1
    code: str
    def __init__(self, failure_class: _Optional[_Union[LoopFailureClassV1, str]] = ..., code: _Optional[str] = ...) -> None: ...

class LoopFailureCountsV1(_message.Message):
    __slots__ = ("task", "verifier", "infrastructure", "cancelled", "infrastructure_retried")
    TASK_FIELD_NUMBER: _ClassVar[int]
    VERIFIER_FIELD_NUMBER: _ClassVar[int]
    INFRASTRUCTURE_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_FIELD_NUMBER: _ClassVar[int]
    INFRASTRUCTURE_RETRIED_FIELD_NUMBER: _ClassVar[int]
    task: int
    verifier: int
    infrastructure: int
    cancelled: int
    infrastructure_retried: int
    def __init__(self, task: _Optional[int] = ..., verifier: _Optional[int] = ..., infrastructure: _Optional[int] = ..., cancelled: _Optional[int] = ..., infrastructure_retried: _Optional[int] = ...) -> None: ...

class LoopFailureCodeCountV1(_message.Message):
    __slots__ = ("failure_class", "code", "count")
    FAILURE_CLASS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    failure_class: LoopFailureClassV1
    code: str
    count: int
    def __init__(self, failure_class: _Optional[_Union[LoopFailureClassV1, str]] = ..., code: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class LoopRewardV1(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: float
    def __init__(self, name: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...

class LoopHistogramV1(_message.Message):
    __slots__ = ("edges", "counts")
    EDGES_FIELD_NUMBER: _ClassVar[int]
    COUNTS_FIELD_NUMBER: _ClassVar[int]
    edges: _containers.RepeatedScalarFieldContainer[float]
    counts: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, edges: _Optional[_Iterable[float]] = ..., counts: _Optional[_Iterable[int]] = ...) -> None: ...

class LoopRewardStatsV1(_message.Message):
    __slots__ = ("name", "count", "mean", "p50", "min", "max", "determinism", "histogram")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    MEAN_FIELD_NUMBER: _ClassVar[int]
    P50_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    DETERMINISM_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
    name: str
    count: int
    mean: float
    p50: float
    min: float
    max: float
    determinism: LoopRewardDeterminismV1
    histogram: LoopHistogramV1
    def __init__(self, name: _Optional[str] = ..., count: _Optional[int] = ..., mean: _Optional[float] = ..., p50: _Optional[float] = ..., min: _Optional[float] = ..., max: _Optional[float] = ..., determinism: _Optional[_Union[LoopRewardDeterminismV1, str]] = ..., histogram: _Optional[_Union[LoopHistogramV1, _Mapping]] = ...) -> None: ...

class LoopLatencyV1(_message.Message):
    __slots__ = ("reset_p50_millis", "reset_p99_millis", "step_overhead_p50_micros", "step_overhead_p99_micros", "group_start_p50_millis", "group_start_p99_millis")
    RESET_P50_MILLIS_FIELD_NUMBER: _ClassVar[int]
    RESET_P99_MILLIS_FIELD_NUMBER: _ClassVar[int]
    STEP_OVERHEAD_P50_MICROS_FIELD_NUMBER: _ClassVar[int]
    STEP_OVERHEAD_P99_MICROS_FIELD_NUMBER: _ClassVar[int]
    GROUP_START_P50_MILLIS_FIELD_NUMBER: _ClassVar[int]
    GROUP_START_P99_MILLIS_FIELD_NUMBER: _ClassVar[int]
    reset_p50_millis: int
    reset_p99_millis: int
    step_overhead_p50_micros: int
    step_overhead_p99_micros: int
    group_start_p50_millis: int
    group_start_p99_millis: int
    def __init__(self, reset_p50_millis: _Optional[int] = ..., reset_p99_millis: _Optional[int] = ..., step_overhead_p50_micros: _Optional[int] = ..., step_overhead_p99_micros: _Optional[int] = ..., group_start_p50_millis: _Optional[int] = ..., group_start_p99_millis: _Optional[int] = ...) -> None: ...

class LoopTimeSplitV1(_message.Message):
    __slots__ = ("trainer_millis", "tool_millis", "verifier_millis", "reset_millis", "step_overhead_millis", "reward_wait_millis")
    TRAINER_MILLIS_FIELD_NUMBER: _ClassVar[int]
    TOOL_MILLIS_FIELD_NUMBER: _ClassVar[int]
    VERIFIER_MILLIS_FIELD_NUMBER: _ClassVar[int]
    RESET_MILLIS_FIELD_NUMBER: _ClassVar[int]
    STEP_OVERHEAD_MILLIS_FIELD_NUMBER: _ClassVar[int]
    REWARD_WAIT_MILLIS_FIELD_NUMBER: _ClassVar[int]
    trainer_millis: int
    tool_millis: int
    verifier_millis: int
    reset_millis: int
    step_overhead_millis: int
    reward_wait_millis: int
    def __init__(self, trainer_millis: _Optional[int] = ..., tool_millis: _Optional[int] = ..., verifier_millis: _Optional[int] = ..., reset_millis: _Optional[int] = ..., step_overhead_millis: _Optional[int] = ..., reward_wait_millis: _Optional[int] = ...) -> None: ...

class LoopRolloutStatsV1(_message.Message):
    __slots__ = ("computed_at", "rollouts", "rollouts_open", "rollouts_rewarded", "rollouts_per_minute", "groups", "groups_open", "groups_without_spread", "passed", "failed", "partial", "failures", "failures_by_code", "primary_reward", "rewards", "billed_unit_seconds", "our_unit_seconds", "spend_cents", "trainer_step", "trainer_total_steps", "mean_reward_first_step", "latency", "time_split", "dropped_spans", "groups_with_failures", "resets_waiting", "cap_reached_at", "recent_step_means")
    COMPUTED_AT_FIELD_NUMBER: _ClassVar[int]
    ROLLOUTS_FIELD_NUMBER: _ClassVar[int]
    ROLLOUTS_OPEN_FIELD_NUMBER: _ClassVar[int]
    ROLLOUTS_REWARDED_FIELD_NUMBER: _ClassVar[int]
    ROLLOUTS_PER_MINUTE_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_OPEN_FIELD_NUMBER: _ClassVar[int]
    GROUPS_WITHOUT_SPREAD_FIELD_NUMBER: _ClassVar[int]
    PASSED_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FIELD_NUMBER: _ClassVar[int]
    FAILURES_FIELD_NUMBER: _ClassVar[int]
    FAILURES_BY_CODE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_REWARD_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    BILLED_UNIT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    OUR_UNIT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SPEND_CENTS_FIELD_NUMBER: _ClassVar[int]
    TRAINER_STEP_FIELD_NUMBER: _ClassVar[int]
    TRAINER_TOTAL_STEPS_FIELD_NUMBER: _ClassVar[int]
    MEAN_REWARD_FIRST_STEP_FIELD_NUMBER: _ClassVar[int]
    LATENCY_FIELD_NUMBER: _ClassVar[int]
    TIME_SPLIT_FIELD_NUMBER: _ClassVar[int]
    DROPPED_SPANS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_WITH_FAILURES_FIELD_NUMBER: _ClassVar[int]
    RESETS_WAITING_FIELD_NUMBER: _ClassVar[int]
    CAP_REACHED_AT_FIELD_NUMBER: _ClassVar[int]
    RECENT_STEP_MEANS_FIELD_NUMBER: _ClassVar[int]
    computed_at: _timestamp_pb2.Timestamp
    rollouts: int
    rollouts_open: int
    rollouts_rewarded: int
    rollouts_per_minute: float
    groups: int
    groups_open: int
    groups_without_spread: int
    passed: int
    failed: int
    partial: int
    failures: LoopFailureCountsV1
    failures_by_code: _containers.RepeatedCompositeFieldContainer[LoopFailureCodeCountV1]
    primary_reward: str
    rewards: _containers.RepeatedCompositeFieldContainer[LoopRewardStatsV1]
    billed_unit_seconds: int
    our_unit_seconds: int
    spend_cents: int
    trainer_step: int
    trainer_total_steps: int
    mean_reward_first_step: float
    latency: LoopLatencyV1
    time_split: LoopTimeSplitV1
    dropped_spans: int
    groups_with_failures: int
    resets_waiting: int
    cap_reached_at: _timestamp_pb2.Timestamp
    recent_step_means: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, computed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., rollouts: _Optional[int] = ..., rollouts_open: _Optional[int] = ..., rollouts_rewarded: _Optional[int] = ..., rollouts_per_minute: _Optional[float] = ..., groups: _Optional[int] = ..., groups_open: _Optional[int] = ..., groups_without_spread: _Optional[int] = ..., passed: _Optional[int] = ..., failed: _Optional[int] = ..., partial: _Optional[int] = ..., failures: _Optional[_Union[LoopFailureCountsV1, _Mapping]] = ..., failures_by_code: _Optional[_Iterable[_Union[LoopFailureCodeCountV1, _Mapping]]] = ..., primary_reward: _Optional[str] = ..., rewards: _Optional[_Iterable[_Union[LoopRewardStatsV1, _Mapping]]] = ..., billed_unit_seconds: _Optional[int] = ..., our_unit_seconds: _Optional[int] = ..., spend_cents: _Optional[int] = ..., trainer_step: _Optional[int] = ..., trainer_total_steps: _Optional[int] = ..., mean_reward_first_step: _Optional[float] = ..., latency: _Optional[_Union[LoopLatencyV1, _Mapping]] = ..., time_split: _Optional[_Union[LoopTimeSplitV1, _Mapping]] = ..., dropped_spans: _Optional[int] = ..., groups_with_failures: _Optional[int] = ..., resets_waiting: _Optional[int] = ..., cap_reached_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., recent_step_means: _Optional[_Iterable[float]] = ...) -> None: ...

class LoopTaskV1(_message.Message):
    __slots__ = ("case_revision_id", "title")
    CASE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    case_revision_id: str
    title: str
    def __init__(self, case_revision_id: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class LoopFinalStateV1(_message.Message):
    __slots__ = ("entries", "bytes", "oversized")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    OVERSIZED_FIELD_NUMBER: _ClassVar[int]
    entries: int
    bytes: int
    oversized: bool
    def __init__(self, entries: _Optional[int] = ..., bytes: _Optional[int] = ..., oversized: _Optional[bool] = ...) -> None: ...

class LoopRolloutV1(_message.Message):
    __slots__ = ("rollout_id", "run_id", "group_id", "group_index", "group_size", "task", "state", "failure", "rewards", "verdict", "determinism", "environment_id", "environment_version", "profile", "base_snapshot_id", "restore_snapshot_id", "parent_rollout_id", "parent_step", "trace_id", "step_count", "trainer_step", "final_state", "infrastructure_retries", "created_at", "ready_at", "closed_at", "verifier_started_at", "ended_at", "credential_prefix")
    ROLLOUT_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_INDEX_FIELD_NUMBER: _ClassVar[int]
    GROUP_SIZE_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    DETERMINISM_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    BASE_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ROLLOUT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_STEP_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    STEP_COUNT_FIELD_NUMBER: _ClassVar[int]
    TRAINER_STEP_FIELD_NUMBER: _ClassVar[int]
    FINAL_STATE_FIELD_NUMBER: _ClassVar[int]
    INFRASTRUCTURE_RETRIES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    READY_AT_FIELD_NUMBER: _ClassVar[int]
    CLOSED_AT_FIELD_NUMBER: _ClassVar[int]
    VERIFIER_STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_PREFIX_FIELD_NUMBER: _ClassVar[int]
    rollout_id: str
    run_id: str
    group_id: str
    group_index: int
    group_size: int
    task: LoopTaskV1
    state: LoopRolloutStateV1
    failure: LoopRolloutFailureV1
    rewards: _containers.RepeatedCompositeFieldContainer[LoopRewardV1]
    verdict: LoopVerdictV1
    determinism: LoopRewardDeterminismV1
    environment_id: str
    environment_version: int
    profile: _environment_pb2.LoopEnvironmentProfileRefV1
    base_snapshot_id: bytes
    restore_snapshot_id: bytes
    parent_rollout_id: str
    parent_step: int
    trace_id: bytes
    step_count: int
    trainer_step: int
    final_state: LoopFinalStateV1
    infrastructure_retries: int
    created_at: _timestamp_pb2.Timestamp
    ready_at: _timestamp_pb2.Timestamp
    closed_at: _timestamp_pb2.Timestamp
    verifier_started_at: _timestamp_pb2.Timestamp
    ended_at: _timestamp_pb2.Timestamp
    credential_prefix: str
    def __init__(self, rollout_id: _Optional[str] = ..., run_id: _Optional[str] = ..., group_id: _Optional[str] = ..., group_index: _Optional[int] = ..., group_size: _Optional[int] = ..., task: _Optional[_Union[LoopTaskV1, _Mapping]] = ..., state: _Optional[_Union[LoopRolloutStateV1, str]] = ..., failure: _Optional[_Union[LoopRolloutFailureV1, _Mapping]] = ..., rewards: _Optional[_Iterable[_Union[LoopRewardV1, _Mapping]]] = ..., verdict: _Optional[_Union[LoopVerdictV1, str]] = ..., determinism: _Optional[_Union[LoopRewardDeterminismV1, str]] = ..., environment_id: _Optional[str] = ..., environment_version: _Optional[int] = ..., profile: _Optional[_Union[_environment_pb2.LoopEnvironmentProfileRefV1, _Mapping]] = ..., base_snapshot_id: _Optional[bytes] = ..., restore_snapshot_id: _Optional[bytes] = ..., parent_rollout_id: _Optional[str] = ..., parent_step: _Optional[int] = ..., trace_id: _Optional[bytes] = ..., step_count: _Optional[int] = ..., trainer_step: _Optional[int] = ..., final_state: _Optional[_Union[LoopFinalStateV1, _Mapping]] = ..., infrastructure_retries: _Optional[int] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ready_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., closed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., verifier_started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ended_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., credential_prefix: _Optional[str] = ...) -> None: ...

class LoopToolExecV1(_message.Message):
    __slots__ = ("argv", "output_cap_bytes")
    ARGV_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CAP_BYTES_FIELD_NUMBER: _ClassVar[int]
    argv: _containers.RepeatedScalarFieldContainer[str]
    output_cap_bytes: int
    def __init__(self, argv: _Optional[_Iterable[str]] = ..., output_cap_bytes: _Optional[int] = ...) -> None: ...

class LoopToolShellV1(_message.Message):
    __slots__ = ("script", "output_cap_bytes")
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CAP_BYTES_FIELD_NUMBER: _ClassVar[int]
    script: str
    output_cap_bytes: int
    def __init__(self, script: _Optional[str] = ..., output_cap_bytes: _Optional[int] = ...) -> None: ...

class LoopToolReadFileV1(_message.Message):
    __slots__ = ("path", "offset", "length")
    PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    path: str
    offset: int
    length: int
    def __init__(self, path: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class LoopToolWriteFileV1(_message.Message):
    __slots__ = ("path", "data", "append")
    PATH_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    APPEND_FIELD_NUMBER: _ClassVar[int]
    path: str
    data: bytes
    append: bool
    def __init__(self, path: _Optional[str] = ..., data: _Optional[bytes] = ..., append: _Optional[bool] = ...) -> None: ...

class LoopToolPatchV1(_message.Message):
    __slots__ = ("path", "old", "new", "count")
    PATH_FIELD_NUMBER: _ClassVar[int]
    OLD_FIELD_NUMBER: _ClassVar[int]
    NEW_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    path: str
    old: bytes
    new: bytes
    count: int
    def __init__(self, path: _Optional[str] = ..., old: _Optional[bytes] = ..., new: _Optional[bytes] = ..., count: _Optional[int] = ...) -> None: ...

class LoopToolListV1(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class LoopToolSetEnvV1(_message.Message):
    __slots__ = ("env",)
    ENV_FIELD_NUMBER: _ClassVar[int]
    env: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, env: _Optional[_Iterable[str]] = ...) -> None: ...

class LoopToolCallV1(_message.Message):
    __slots__ = ("timeout_millis", "uid", "exec", "shell", "read_file", "write_file", "patch", "list", "set_env")
    TIMEOUT_MILLIS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    EXEC_FIELD_NUMBER: _ClassVar[int]
    SHELL_FIELD_NUMBER: _ClassVar[int]
    READ_FILE_FIELD_NUMBER: _ClassVar[int]
    WRITE_FILE_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    SET_ENV_FIELD_NUMBER: _ClassVar[int]
    timeout_millis: int
    uid: int
    exec: LoopToolExecV1
    shell: LoopToolShellV1
    read_file: LoopToolReadFileV1
    write_file: LoopToolWriteFileV1
    patch: LoopToolPatchV1
    list: LoopToolListV1
    set_env: LoopToolSetEnvV1
    def __init__(self, timeout_millis: _Optional[int] = ..., uid: _Optional[int] = ..., exec: _Optional[_Union[LoopToolExecV1, _Mapping]] = ..., shell: _Optional[_Union[LoopToolShellV1, _Mapping]] = ..., read_file: _Optional[_Union[LoopToolReadFileV1, _Mapping]] = ..., write_file: _Optional[_Union[LoopToolWriteFileV1, _Mapping]] = ..., patch: _Optional[_Union[LoopToolPatchV1, _Mapping]] = ..., list: _Optional[_Union[LoopToolListV1, _Mapping]] = ..., set_env: _Optional[_Union[LoopToolSetEnvV1, _Mapping]] = ...) -> None: ...

class LoopToolEntryV1(_message.Message):
    __slots__ = ("name", "kind", "size")
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    name: str
    kind: LoopToolEntryKindV1
    size: int
    def __init__(self, name: _Optional[str] = ..., kind: _Optional[_Union[LoopToolEntryKindV1, str]] = ..., size: _Optional[int] = ...) -> None: ...

class LoopToolResultV1(_message.Message):
    __slots__ = ("exit_code", "signal", "done", "error", "timed_out", "stdout", "stderr", "file", "entries", "truncated", "duration_millis", "stdout_bytes", "stderr_bytes", "file_bytes")
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_FIELD_NUMBER: _ClassVar[int]
    DONE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TIMED_OUT_FIELD_NUMBER: _ClassVar[int]
    STDOUT_FIELD_NUMBER: _ClassVar[int]
    STDERR_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    DURATION_MILLIS_FIELD_NUMBER: _ClassVar[int]
    STDOUT_BYTES_FIELD_NUMBER: _ClassVar[int]
    STDERR_BYTES_FIELD_NUMBER: _ClassVar[int]
    FILE_BYTES_FIELD_NUMBER: _ClassVar[int]
    exit_code: int
    signal: int
    done: bool
    error: str
    timed_out: bool
    stdout: bytes
    stderr: bytes
    file: bytes
    entries: _containers.RepeatedCompositeFieldContainer[LoopToolEntryV1]
    truncated: bool
    duration_millis: int
    stdout_bytes: int
    stderr_bytes: int
    file_bytes: int
    def __init__(self, exit_code: _Optional[int] = ..., signal: _Optional[int] = ..., done: _Optional[bool] = ..., error: _Optional[str] = ..., timed_out: _Optional[bool] = ..., stdout: _Optional[bytes] = ..., stderr: _Optional[bytes] = ..., file: _Optional[bytes] = ..., entries: _Optional[_Iterable[_Union[LoopToolEntryV1, _Mapping]]] = ..., truncated: _Optional[bool] = ..., duration_millis: _Optional[int] = ..., stdout_bytes: _Optional[int] = ..., stderr_bytes: _Optional[int] = ..., file_bytes: _Optional[int] = ...) -> None: ...

class CreateLoopRunRequest(_message.Message):
    __slots__ = ("name", "framework", "environment_id", "environment_version", "dataset_version_id", "group_size", "environment_limit", "spend_cap_cents", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FRAMEWORK_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_SIZE_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    SPEND_CAP_CENTS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    framework: LoopTrainerFrameworkV1
    environment_id: str
    environment_version: int
    dataset_version_id: str
    group_size: int
    environment_limit: int
    spend_cap_cents: int
    request_id: str
    def __init__(self, name: _Optional[str] = ..., framework: _Optional[_Union[LoopTrainerFrameworkV1, str]] = ..., environment_id: _Optional[str] = ..., environment_version: _Optional[int] = ..., dataset_version_id: _Optional[str] = ..., group_size: _Optional[int] = ..., environment_limit: _Optional[int] = ..., spend_cap_cents: _Optional[int] = ..., request_id: _Optional[str] = ...) -> None: ...

class CreateLoopRunResponse(_message.Message):
    __slots__ = ("run",)
    RUN_FIELD_NUMBER: _ClassVar[int]
    run: LoopRunV1
    def __init__(self, run: _Optional[_Union[LoopRunV1, _Mapping]] = ...) -> None: ...

class GetLoopRunRequest(_message.Message):
    __slots__ = ("run_id",)
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class GetLoopRunResponse(_message.Message):
    __slots__ = ("run", "stats", "usage")
    RUN_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    run: LoopRunV1
    stats: LoopRolloutStatsV1
    usage: LoopEnvironmentUsageV1
    def __init__(self, run: _Optional[_Union[LoopRunV1, _Mapping]] = ..., stats: _Optional[_Union[LoopRolloutStatsV1, _Mapping]] = ..., usage: _Optional[_Union[LoopEnvironmentUsageV1, _Mapping]] = ...) -> None: ...

class ListLoopRunsRequest(_message.Message):
    __slots__ = ("page", "environment_id", "environment_version", "since")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    page: _common_pb2.PageRequestV1
    environment_id: str
    environment_version: int
    since: _timestamp_pb2.Timestamp
    def __init__(self, page: _Optional[_Union[_common_pb2.PageRequestV1, _Mapping]] = ..., environment_id: _Optional[str] = ..., environment_version: _Optional[int] = ..., since: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class LoopRunSummaryV1(_message.Message):
    __slots__ = ("run", "stats")
    RUN_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    run: LoopRunV1
    stats: LoopRolloutStatsV1
    def __init__(self, run: _Optional[_Union[LoopRunV1, _Mapping]] = ..., stats: _Optional[_Union[LoopRolloutStatsV1, _Mapping]] = ...) -> None: ...

class ListLoopRunsResponse(_message.Message):
    __slots__ = ("runs", "page", "usage", "organization_rollouts_per_minute")
    RUNS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ROLLOUTS_PER_MINUTE_FIELD_NUMBER: _ClassVar[int]
    runs: _containers.RepeatedCompositeFieldContainer[LoopRunSummaryV1]
    page: _common_pb2.PageResponseV1
    usage: LoopEnvironmentUsageV1
    organization_rollouts_per_minute: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, runs: _Optional[_Iterable[_Union[LoopRunSummaryV1, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponseV1, _Mapping]] = ..., usage: _Optional[_Union[LoopEnvironmentUsageV1, _Mapping]] = ..., organization_rollouts_per_minute: _Optional[_Iterable[int]] = ...) -> None: ...

class UpdateLoopRunRequest(_message.Message):
    __slots__ = ("run_id", "spend_cap_cents", "environment_limit")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    SPEND_CAP_CENTS_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    spend_cap_cents: int
    environment_limit: int
    def __init__(self, run_id: _Optional[str] = ..., spend_cap_cents: _Optional[int] = ..., environment_limit: _Optional[int] = ...) -> None: ...

class UpdateLoopRunResponse(_message.Message):
    __slots__ = ("run",)
    RUN_FIELD_NUMBER: _ClassVar[int]
    run: LoopRunV1
    def __init__(self, run: _Optional[_Union[LoopRunV1, _Mapping]] = ...) -> None: ...

class PauseLoopRunRequest(_message.Message):
    __slots__ = ("run_id",)
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class PauseLoopRunResponse(_message.Message):
    __slots__ = ("run",)
    RUN_FIELD_NUMBER: _ClassVar[int]
    run: LoopRunV1
    def __init__(self, run: _Optional[_Union[LoopRunV1, _Mapping]] = ...) -> None: ...

class ResumeLoopRunRequest(_message.Message):
    __slots__ = ("run_id",)
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class ResumeLoopRunResponse(_message.Message):
    __slots__ = ("run",)
    RUN_FIELD_NUMBER: _ClassVar[int]
    run: LoopRunV1
    def __init__(self, run: _Optional[_Union[LoopRunV1, _Mapping]] = ...) -> None: ...

class StopLoopRunRequest(_message.Message):
    __slots__ = ("run_id", "close_in_flight")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CLOSE_IN_FLIGHT_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    close_in_flight: bool
    def __init__(self, run_id: _Optional[str] = ..., close_in_flight: _Optional[bool] = ...) -> None: ...

class StopLoopRunResponse(_message.Message):
    __slots__ = ("run",)
    RUN_FIELD_NUMBER: _ClassVar[int]
    run: LoopRunV1
    def __init__(self, run: _Optional[_Union[LoopRunV1, _Mapping]] = ...) -> None: ...

class ResetLoopRolloutRequest(_message.Message):
    __slots__ = ("run_id", "request_id", "group_id", "group_index", "group_size", "case_revision_id", "trainer_step", "trainer_total_steps", "experiment_name", "client")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_INDEX_FIELD_NUMBER: _ClassVar[int]
    GROUP_SIZE_FIELD_NUMBER: _ClassVar[int]
    CASE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    TRAINER_STEP_FIELD_NUMBER: _ClassVar[int]
    TRAINER_TOTAL_STEPS_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    request_id: str
    group_id: str
    group_index: int
    group_size: int
    case_revision_id: str
    trainer_step: int
    trainer_total_steps: int
    experiment_name: str
    client: LoopClientV1
    def __init__(self, run_id: _Optional[str] = ..., request_id: _Optional[str] = ..., group_id: _Optional[str] = ..., group_index: _Optional[int] = ..., group_size: _Optional[int] = ..., case_revision_id: _Optional[str] = ..., trainer_step: _Optional[int] = ..., trainer_total_steps: _Optional[int] = ..., experiment_name: _Optional[str] = ..., client: _Optional[_Union[LoopClientV1, _Mapping]] = ...) -> None: ...

class ResetLoopRolloutResponse(_message.Message):
    __slots__ = ("rollout",)
    ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    rollout: LoopRolloutV1
    def __init__(self, rollout: _Optional[_Union[LoopRolloutV1, _Mapping]] = ...) -> None: ...

class StepLoopRolloutRequest(_message.Message):
    __slots__ = ("rollout_id", "calls", "model_message_json")
    ROLLOUT_ID_FIELD_NUMBER: _ClassVar[int]
    CALLS_FIELD_NUMBER: _ClassVar[int]
    MODEL_MESSAGE_JSON_FIELD_NUMBER: _ClassVar[int]
    rollout_id: str
    calls: _containers.RepeatedCompositeFieldContainer[LoopToolCallV1]
    model_message_json: str
    def __init__(self, rollout_id: _Optional[str] = ..., calls: _Optional[_Iterable[_Union[LoopToolCallV1, _Mapping]]] = ..., model_message_json: _Optional[str] = ...) -> None: ...

class StepLoopRolloutResponse(_message.Message):
    __slots__ = ("step", "results")
    STEP_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    step: int
    results: _containers.RepeatedCompositeFieldContainer[LoopToolResultV1]
    def __init__(self, step: _Optional[int] = ..., results: _Optional[_Iterable[_Union[LoopToolResultV1, _Mapping]]] = ...) -> None: ...

class CloseLoopRolloutRequest(_message.Message):
    __slots__ = ("rollout_id",)
    ROLLOUT_ID_FIELD_NUMBER: _ClassVar[int]
    rollout_id: str
    def __init__(self, rollout_id: _Optional[str] = ...) -> None: ...

class CloseLoopRolloutResponse(_message.Message):
    __slots__ = ("rollout", "pending")
    ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    PENDING_FIELD_NUMBER: _ClassVar[int]
    rollout: LoopRolloutV1
    pending: bool
    def __init__(self, rollout: _Optional[_Union[LoopRolloutV1, _Mapping]] = ..., pending: _Optional[bool] = ...) -> None: ...

class ForkLoopRolloutRequest(_message.Message):
    __slots__ = ("rollout_id", "copies", "request_id")
    ROLLOUT_ID_FIELD_NUMBER: _ClassVar[int]
    COPIES_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    rollout_id: str
    copies: int
    request_id: str
    def __init__(self, rollout_id: _Optional[str] = ..., copies: _Optional[int] = ..., request_id: _Optional[str] = ...) -> None: ...

class ForkLoopRolloutResponse(_message.Message):
    __slots__ = ("rollouts",)
    ROLLOUTS_FIELD_NUMBER: _ClassVar[int]
    rollouts: _containers.RepeatedCompositeFieldContainer[LoopRolloutV1]
    def __init__(self, rollouts: _Optional[_Iterable[_Union[LoopRolloutV1, _Mapping]]] = ...) -> None: ...

class GetLoopRolloutRequest(_message.Message):
    __slots__ = ("rollout_id",)
    ROLLOUT_ID_FIELD_NUMBER: _ClassVar[int]
    rollout_id: str
    def __init__(self, rollout_id: _Optional[str] = ...) -> None: ...

class GetLoopRolloutResponse(_message.Message):
    __slots__ = ("rollout",)
    ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    rollout: LoopRolloutV1
    def __init__(self, rollout: _Optional[_Union[LoopRolloutV1, _Mapping]] = ...) -> None: ...

class ListLoopRolloutsRequest(_message.Message):
    __slots__ = ("run_id", "group_id", "trainer_step", "state", "failure_class", "page")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    TRAINER_STEP_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_CLASS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    group_id: str
    trainer_step: int
    state: LoopRolloutStateV1
    failure_class: LoopFailureClassV1
    page: _common_pb2.PageRequestV1
    def __init__(self, run_id: _Optional[str] = ..., group_id: _Optional[str] = ..., trainer_step: _Optional[int] = ..., state: _Optional[_Union[LoopRolloutStateV1, str]] = ..., failure_class: _Optional[_Union[LoopFailureClassV1, str]] = ..., page: _Optional[_Union[_common_pb2.PageRequestV1, _Mapping]] = ...) -> None: ...

class ListLoopRolloutsResponse(_message.Message):
    __slots__ = ("rollouts", "page")
    ROLLOUTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    rollouts: _containers.RepeatedCompositeFieldContainer[LoopRolloutV1]
    page: _common_pb2.PageResponseV1
    def __init__(self, rollouts: _Optional[_Iterable[_Union[LoopRolloutV1, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponseV1, _Mapping]] = ...) -> None: ...

class ListLoopRolloutGroupsRequest(_message.Message):
    __slots__ = ("run_id", "filter", "page")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    filter: LoopRolloutGroupFilterV1
    page: _common_pb2.PageRequestV1
    def __init__(self, run_id: _Optional[str] = ..., filter: _Optional[_Union[LoopRolloutGroupFilterV1, str]] = ..., page: _Optional[_Union[_common_pb2.PageRequestV1, _Mapping]] = ...) -> None: ...

class LoopRolloutBriefV1(_message.Message):
    __slots__ = ("rollout_id", "group_index", "state", "failure_class", "primary_reward", "infrastructure_retries")
    ROLLOUT_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_INDEX_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_CLASS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_REWARD_FIELD_NUMBER: _ClassVar[int]
    INFRASTRUCTURE_RETRIES_FIELD_NUMBER: _ClassVar[int]
    rollout_id: str
    group_index: int
    state: LoopRolloutStateV1
    failure_class: LoopFailureClassV1
    primary_reward: float
    infrastructure_retries: int
    def __init__(self, rollout_id: _Optional[str] = ..., group_index: _Optional[int] = ..., state: _Optional[_Union[LoopRolloutStateV1, str]] = ..., failure_class: _Optional[_Union[LoopFailureClassV1, str]] = ..., primary_reward: _Optional[float] = ..., infrastructure_retries: _Optional[int] = ...) -> None: ...

class LoopRolloutGroupV1(_message.Message):
    __slots__ = ("group_id", "task", "size", "rewarded", "open", "mean", "spread", "start_millis", "trainer_step", "created_at", "rollouts")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    REWARDED_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    MEAN_FIELD_NUMBER: _ClassVar[int]
    SPREAD_FIELD_NUMBER: _ClassVar[int]
    START_MILLIS_FIELD_NUMBER: _ClassVar[int]
    TRAINER_STEP_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ROLLOUTS_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    task: LoopTaskV1
    size: int
    rewarded: int
    open: int
    mean: float
    spread: float
    start_millis: int
    trainer_step: int
    created_at: _timestamp_pb2.Timestamp
    rollouts: _containers.RepeatedCompositeFieldContainer[LoopRolloutBriefV1]
    def __init__(self, group_id: _Optional[str] = ..., task: _Optional[_Union[LoopTaskV1, _Mapping]] = ..., size: _Optional[int] = ..., rewarded: _Optional[int] = ..., open: _Optional[int] = ..., mean: _Optional[float] = ..., spread: _Optional[float] = ..., start_millis: _Optional[int] = ..., trainer_step: _Optional[int] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., rollouts: _Optional[_Iterable[_Union[LoopRolloutBriefV1, _Mapping]]] = ...) -> None: ...

class ListLoopRolloutGroupsResponse(_message.Message):
    __slots__ = ("groups", "page")
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[LoopRolloutGroupV1]
    page: _common_pb2.PageResponseV1
    def __init__(self, groups: _Optional[_Iterable[_Union[LoopRolloutGroupV1, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponseV1, _Mapping]] = ...) -> None: ...

class GetLoopRolloutChangeListRequest(_message.Message):
    __slots__ = ("rollout_id", "page")
    ROLLOUT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    rollout_id: str
    page: _common_pb2.PageRequestV1
    def __init__(self, rollout_id: _Optional[str] = ..., page: _Optional[_Union[_common_pb2.PageRequestV1, _Mapping]] = ...) -> None: ...

class LoopChangeEntryV1(_message.Message):
    __slots__ = ("path", "kind", "size", "sha256", "symlink_target", "mode")
    PATH_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    SYMLINK_TARGET_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    path: bytes
    kind: LoopChangeKindV1
    size: int
    sha256: bytes
    symlink_target: bytes
    mode: int
    def __init__(self, path: _Optional[bytes] = ..., kind: _Optional[_Union[LoopChangeKindV1, str]] = ..., size: _Optional[int] = ..., sha256: _Optional[bytes] = ..., symlink_target: _Optional[bytes] = ..., mode: _Optional[int] = ...) -> None: ...

class GetLoopRolloutChangeListResponse(_message.Message):
    __slots__ = ("entries", "missing", "put_back", "removed", "page")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    PUT_BACK_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[LoopChangeEntryV1]
    missing: _containers.RepeatedScalarFieldContainer[str]
    put_back: _containers.RepeatedScalarFieldContainer[bytes]
    removed: _containers.RepeatedScalarFieldContainer[bytes]
    page: _common_pb2.PageResponseV1
    def __init__(self, entries: _Optional[_Iterable[_Union[LoopChangeEntryV1, _Mapping]]] = ..., missing: _Optional[_Iterable[str]] = ..., put_back: _Optional[_Iterable[bytes]] = ..., removed: _Optional[_Iterable[bytes]] = ..., page: _Optional[_Union[_common_pb2.PageResponseV1, _Mapping]] = ...) -> None: ...

class LoopEnvironmentVersionRefV1(_message.Message):
    __slots__ = ("environment_id", "version")
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    environment_id: str
    version: int
    def __init__(self, environment_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class GetLoopRolloutStatsRequest(_message.Message):
    __slots__ = ("run_id", "environment_version", "since")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    environment_version: LoopEnvironmentVersionRefV1
    since: _timestamp_pb2.Timestamp
    def __init__(self, run_id: _Optional[str] = ..., environment_version: _Optional[_Union[LoopEnvironmentVersionRefV1, _Mapping]] = ..., since: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetLoopRolloutStatsResponse(_message.Message):
    __slots__ = ("stats",)
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: LoopRolloutStatsV1
    def __init__(self, stats: _Optional[_Union[LoopRolloutStatsV1, _Mapping]] = ...) -> None: ...

class ListLoopRunStepsRequest(_message.Message):
    __slots__ = ("run_id", "bucket", "since", "page")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    bucket: LoopRunStepBucketV1
    since: _timestamp_pb2.Timestamp
    page: _common_pb2.PageRequestV1
    def __init__(self, run_id: _Optional[str] = ..., bucket: _Optional[_Union[LoopRunStepBucketV1, str]] = ..., since: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., page: _Optional[_Union[_common_pb2.PageRequestV1, _Mapping]] = ...) -> None: ...

class LoopRunStepV1(_message.Message):
    __slots__ = ("trainer_step", "start", "rollouts", "rewarded", "mean", "p10", "p90", "stddev", "best_group_mean", "groups", "groups_without_spread", "failures", "spend_cents", "open_max", "organization_open_max", "reconnected", "wait_millis", "wall_millis")
    TRAINER_STEP_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    ROLLOUTS_FIELD_NUMBER: _ClassVar[int]
    REWARDED_FIELD_NUMBER: _ClassVar[int]
    MEAN_FIELD_NUMBER: _ClassVar[int]
    P10_FIELD_NUMBER: _ClassVar[int]
    P90_FIELD_NUMBER: _ClassVar[int]
    STDDEV_FIELD_NUMBER: _ClassVar[int]
    BEST_GROUP_MEAN_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_WITHOUT_SPREAD_FIELD_NUMBER: _ClassVar[int]
    FAILURES_FIELD_NUMBER: _ClassVar[int]
    SPEND_CENTS_FIELD_NUMBER: _ClassVar[int]
    OPEN_MAX_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_OPEN_MAX_FIELD_NUMBER: _ClassVar[int]
    RECONNECTED_FIELD_NUMBER: _ClassVar[int]
    WAIT_MILLIS_FIELD_NUMBER: _ClassVar[int]
    WALL_MILLIS_FIELD_NUMBER: _ClassVar[int]
    trainer_step: int
    start: _timestamp_pb2.Timestamp
    rollouts: int
    rewarded: int
    mean: float
    p10: float
    p90: float
    stddev: float
    best_group_mean: float
    groups: int
    groups_without_spread: int
    failures: LoopFailureCountsV1
    spend_cents: int
    open_max: int
    organization_open_max: int
    reconnected: bool
    wait_millis: int
    wall_millis: int
    def __init__(self, trainer_step: _Optional[int] = ..., start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., rollouts: _Optional[int] = ..., rewarded: _Optional[int] = ..., mean: _Optional[float] = ..., p10: _Optional[float] = ..., p90: _Optional[float] = ..., stddev: _Optional[float] = ..., best_group_mean: _Optional[float] = ..., groups: _Optional[int] = ..., groups_without_spread: _Optional[int] = ..., failures: _Optional[_Union[LoopFailureCountsV1, _Mapping]] = ..., spend_cents: _Optional[int] = ..., open_max: _Optional[int] = ..., organization_open_max: _Optional[int] = ..., reconnected: _Optional[bool] = ..., wait_millis: _Optional[int] = ..., wall_millis: _Optional[int] = ...) -> None: ...

class ListLoopRunStepsResponse(_message.Message):
    __slots__ = ("steps", "page")
    STEPS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    steps: _containers.RepeatedCompositeFieldContainer[LoopRunStepV1]
    page: _common_pb2.PageResponseV1
    def __init__(self, steps: _Optional[_Iterable[_Union[LoopRunStepV1, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponseV1, _Mapping]] = ...) -> None: ...

class LoopRolloutRejectionV1(_message.Message):
    __slots__ = ("reason_code", "retry_after_millis", "limit")
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    RETRY_AFTER_MILLIS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    reason_code: str
    retry_after_millis: int
    limit: int
    def __init__(self, reason_code: _Optional[str] = ..., retry_after_millis: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...
