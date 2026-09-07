import datetime

from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from o11y_one.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScoreSourceV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCORE_SOURCE_V1_UNSPECIFIED: _ClassVar[ScoreSourceV1]
    SCORE_SOURCE_V1_SDK: _ClassVar[ScoreSourceV1]
    SCORE_SOURCE_V1_ONLINE: _ClassVar[ScoreSourceV1]
    SCORE_SOURCE_V1_OFFLINE: _ClassVar[ScoreSourceV1]
    SCORE_SOURCE_V1_ANNOTATION: _ClassVar[ScoreSourceV1]
    SCORE_SOURCE_V1_API: _ClassVar[ScoreSourceV1]

class FeedbackSourceTypeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FEEDBACK_SOURCE_TYPE_V1_UNSPECIFIED: _ClassVar[FeedbackSourceTypeV1]
    FEEDBACK_SOURCE_TYPE_V1_USER: _ClassVar[FeedbackSourceTypeV1]
    FEEDBACK_SOURCE_TYPE_V1_REVIEWER: _ClassVar[FeedbackSourceTypeV1]
    FEEDBACK_SOURCE_TYPE_V1_API: _ClassVar[FeedbackSourceTypeV1]
    FEEDBACK_SOURCE_TYPE_V1_EVALUATOR: _ClassVar[FeedbackSourceTypeV1]
    FEEDBACK_SOURCE_TYPE_V1_SYSTEM: _ClassVar[FeedbackSourceTypeV1]

class FeedbackApprovalStatusV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FEEDBACK_APPROVAL_STATUS_V1_UNSPECIFIED: _ClassVar[FeedbackApprovalStatusV1]
    FEEDBACK_APPROVAL_STATUS_V1_NOT_APPLICABLE: _ClassVar[FeedbackApprovalStatusV1]
    FEEDBACK_APPROVAL_STATUS_V1_PENDING: _ClassVar[FeedbackApprovalStatusV1]
    FEEDBACK_APPROVAL_STATUS_V1_APPROVED: _ClassVar[FeedbackApprovalStatusV1]
    FEEDBACK_APPROVAL_STATUS_V1_REJECTED: _ClassVar[FeedbackApprovalStatusV1]

class DatasetItemSourceKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_ITEM_SOURCE_KIND_V1_UNSPECIFIED: _ClassVar[DatasetItemSourceKindV1]
    DATASET_ITEM_SOURCE_KIND_V1_TRACE: _ClassVar[DatasetItemSourceKindV1]
    DATASET_ITEM_SOURCE_KIND_V1_SPAN: _ClassVar[DatasetItemSourceKindV1]
    DATASET_ITEM_SOURCE_KIND_V1_OBSERVATION: _ClassVar[DatasetItemSourceKindV1]
    DATASET_ITEM_SOURCE_KIND_V1_SESSION: _ClassVar[DatasetItemSourceKindV1]
    DATASET_ITEM_SOURCE_KIND_V1_MANUAL: _ClassVar[DatasetItemSourceKindV1]

class DatasetImportFormatV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_IMPORT_FORMAT_V1_UNSPECIFIED: _ClassVar[DatasetImportFormatV1]
    DATASET_IMPORT_FORMAT_V1_CSV: _ClassVar[DatasetImportFormatV1]
    DATASET_IMPORT_FORMAT_V1_TSV: _ClassVar[DatasetImportFormatV1]
    DATASET_IMPORT_FORMAT_V1_JSON: _ClassVar[DatasetImportFormatV1]
    DATASET_IMPORT_FORMAT_V1_JSONL: _ClassVar[DatasetImportFormatV1]

class DatasetItemSplitV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_ITEM_SPLIT_V1_UNSPECIFIED: _ClassVar[DatasetItemSplitV1]
    DATASET_ITEM_SPLIT_V1_TRAIN: _ClassVar[DatasetItemSplitV1]
    DATASET_ITEM_SPLIT_V1_EVAL: _ClassVar[DatasetItemSplitV1]
    DATASET_ITEM_SPLIT_V1_GOLDEN: _ClassVar[DatasetItemSplitV1]
    DATASET_ITEM_SPLIT_V1_REGRESSION: _ClassVar[DatasetItemSplitV1]
    DATASET_ITEM_SPLIT_V1_CANARY: _ClassVar[DatasetItemSplitV1]

class AnnotationRoutingReasonV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ANNOTATION_ROUTING_REASON_V1_UNSPECIFIED: _ClassVar[AnnotationRoutingReasonV1]
    ANNOTATION_ROUTING_REASON_V1_NEGATIVE_EXPLICIT_FEEDBACK: _ClassVar[AnnotationRoutingReasonV1]
    ANNOTATION_ROUTING_REASON_V1_BAD_IMPLICIT_OUTCOME: _ClassVar[AnnotationRoutingReasonV1]
    ANNOTATION_ROUTING_REASON_V1_EVALUATOR_DISAGREEMENT: _ClassVar[AnnotationRoutingReasonV1]
    ANNOTATION_ROUTING_REASON_V1_HIGH_COST_FAILURE: _ClassVar[AnnotationRoutingReasonV1]
    ANNOTATION_ROUTING_REASON_V1_STRATEGIC_CUSTOMER: _ClassVar[AnnotationRoutingReasonV1]

class AnnotationTaskStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ANNOTATION_TASK_STATE_V1_UNSPECIFIED: _ClassVar[AnnotationTaskStateV1]
    ANNOTATION_TASK_STATE_V1_OPEN: _ClassVar[AnnotationTaskStateV1]
    ANNOTATION_TASK_STATE_V1_CLAIMED: _ClassVar[AnnotationTaskStateV1]
    ANNOTATION_TASK_STATE_V1_COMPLETED: _ClassVar[AnnotationTaskStateV1]
    ANNOTATION_TASK_STATE_V1_APPROVED: _ClassVar[AnnotationTaskStateV1]
    ANNOTATION_TASK_STATE_V1_REJECTED: _ClassVar[AnnotationTaskStateV1]

class AnnotationTaskModeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ANNOTATION_TASK_MODE_V1_UNSPECIFIED: _ClassVar[AnnotationTaskModeV1]
    ANNOTATION_TASK_MODE_V1_SINGLE: _ClassVar[AnnotationTaskModeV1]
    ANNOTATION_TASK_MODE_V1_PAIRWISE: _ClassVar[AnnotationTaskModeV1]

class AnnotationPairwiseWinnerV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ANNOTATION_PAIRWISE_WINNER_V1_UNSPECIFIED: _ClassVar[AnnotationPairwiseWinnerV1]
    ANNOTATION_PAIRWISE_WINNER_V1_BASELINE: _ClassVar[AnnotationPairwiseWinnerV1]
    ANNOTATION_PAIRWISE_WINNER_V1_CANDIDATE: _ClassVar[AnnotationPairwiseWinnerV1]
    ANNOTATION_PAIRWISE_WINNER_V1_TIE: _ClassVar[AnnotationPairwiseWinnerV1]

class PromptEnvironmentV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROMPT_ENVIRONMENT_V1_UNSPECIFIED: _ClassVar[PromptEnvironmentV1]
    PROMPT_ENVIRONMENT_V1_DRAFT: _ClassVar[PromptEnvironmentV1]
    PROMPT_ENVIRONMENT_V1_PROD: _ClassVar[PromptEnvironmentV1]
    PROMPT_ENVIRONMENT_V1_CANDIDATE: _ClassVar[PromptEnvironmentV1]
    PROMPT_ENVIRONMENT_V1_EXPERIMENT: _ClassVar[PromptEnvironmentV1]

class EvaluatorExecutionModeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATOR_EXECUTION_MODE_V1_UNSPECIFIED: _ClassVar[EvaluatorExecutionModeV1]
    EVALUATOR_EXECUTION_MODE_V1_DETERMINISTIC: _ClassVar[EvaluatorExecutionModeV1]
    EVALUATOR_EXECUTION_MODE_V1_ASYNC: _ClassVar[EvaluatorExecutionModeV1]

class ProviderExecutionModeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROVIDER_EXECUTION_MODE_V1_UNSPECIFIED: _ClassVar[ProviderExecutionModeV1]
    PROVIDER_EXECUTION_MODE_V1_BYO_PROVIDER_KEY_PROXY: _ClassVar[ProviderExecutionModeV1]
    PROVIDER_EXECUTION_MODE_V1_PLATFORM_MANAGED_PROXY: _ClassVar[ProviderExecutionModeV1]
    PROVIDER_EXECUTION_MODE_V1_CUSTOMER_HOSTED_ENDPOINT: _ClassVar[ProviderExecutionModeV1]
    PROVIDER_EXECUTION_MODE_V1_SELF_HOSTED_LOCAL_MODEL: _ClassVar[ProviderExecutionModeV1]
    PROVIDER_EXECUTION_MODE_V1_DETERMINISTIC_LOCAL_EXECUTOR: _ClassVar[ProviderExecutionModeV1]

class ProviderNameV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROVIDER_NAME_V1_UNSPECIFIED: _ClassVar[ProviderNameV1]
    PROVIDER_NAME_V1_OPENAI: _ClassVar[ProviderNameV1]
    PROVIDER_NAME_V1_ANTHROPIC: _ClassVar[ProviderNameV1]
    PROVIDER_NAME_V1_GOOGLE: _ClassVar[ProviderNameV1]
    PROVIDER_NAME_V1_XAI: _ClassVar[ProviderNameV1]
    PROVIDER_NAME_V1_MOONSHOT: _ClassVar[ProviderNameV1]
    PROVIDER_NAME_V1_DEEPSEEK: _ClassVar[ProviderNameV1]
    PROVIDER_NAME_V1_OPENROUTER: _ClassVar[ProviderNameV1]

class ProviderKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROVIDER_KIND_V1_UNSPECIFIED: _ClassVar[ProviderKindV1]
    PROVIDER_KIND_V1_LAB: _ClassVar[ProviderKindV1]
    PROVIDER_KIND_V1_ROUTER: _ClassVar[ProviderKindV1]

class ProviderCostModeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROVIDER_COST_MODE_V1_UNSPECIFIED: _ClassVar[ProviderCostModeV1]
    PROVIDER_COST_MODE_V1_DISABLED: _ClassVar[ProviderCostModeV1]
    PROVIDER_COST_MODE_V1_FIXED_USD: _ClassVar[ProviderCostModeV1]
    PROVIDER_COST_MODE_V1_TOKEN_RATES: _ClassVar[ProviderCostModeV1]

class ProviderToolChoiceV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROVIDER_TOOL_CHOICE_V1_UNSPECIFIED: _ClassVar[ProviderToolChoiceV1]
    PROVIDER_TOOL_CHOICE_V1_AUTO: _ClassVar[ProviderToolChoiceV1]
    PROVIDER_TOOL_CHOICE_V1_NONE: _ClassVar[ProviderToolChoiceV1]
    PROVIDER_TOOL_CHOICE_V1_REQUIRED: _ClassVar[ProviderToolChoiceV1]

class ProviderReasoningEffortV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROVIDER_REASONING_EFFORT_V1_UNSPECIFIED: _ClassVar[ProviderReasoningEffortV1]
    PROVIDER_REASONING_EFFORT_V1_NONE: _ClassVar[ProviderReasoningEffortV1]
    PROVIDER_REASONING_EFFORT_V1_MINIMAL: _ClassVar[ProviderReasoningEffortV1]
    PROVIDER_REASONING_EFFORT_V1_LOW: _ClassVar[ProviderReasoningEffortV1]
    PROVIDER_REASONING_EFFORT_V1_MEDIUM: _ClassVar[ProviderReasoningEffortV1]
    PROVIDER_REASONING_EFFORT_V1_HIGH: _ClassVar[ProviderReasoningEffortV1]
    PROVIDER_REASONING_EFFORT_V1_XHIGH: _ClassVar[ProviderReasoningEffortV1]

class ProviderVerbosityV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROVIDER_VERBOSITY_V1_UNSPECIFIED: _ClassVar[ProviderVerbosityV1]
    PROVIDER_VERBOSITY_V1_DEFAULT: _ClassVar[ProviderVerbosityV1]
    PROVIDER_VERBOSITY_V1_LOW: _ClassVar[ProviderVerbosityV1]
    PROVIDER_VERBOSITY_V1_MEDIUM: _ClassVar[ProviderVerbosityV1]
    PROVIDER_VERBOSITY_V1_HIGH: _ClassVar[ProviderVerbosityV1]

class ProviderTruncationV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROVIDER_TRUNCATION_V1_UNSPECIFIED: _ClassVar[ProviderTruncationV1]
    PROVIDER_TRUNCATION_V1_AUTO: _ClassVar[ProviderTruncationV1]
    PROVIDER_TRUNCATION_V1_DISABLED: _ClassVar[ProviderTruncationV1]

class ProviderPromptCacheRetentionV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROVIDER_PROMPT_CACHE_RETENTION_V1_UNSPECIFIED: _ClassVar[ProviderPromptCacheRetentionV1]
    PROVIDER_PROMPT_CACHE_RETENTION_V1_IN_MEMORY: _ClassVar[ProviderPromptCacheRetentionV1]
    PROVIDER_PROMPT_CACHE_RETENTION_V1_TWENTY_FOUR_HOURS: _ClassVar[ProviderPromptCacheRetentionV1]

class ProviderServiceTierV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROVIDER_SERVICE_TIER_V1_UNSPECIFIED: _ClassVar[ProviderServiceTierV1]
    PROVIDER_SERVICE_TIER_V1_AUTO: _ClassVar[ProviderServiceTierV1]
    PROVIDER_SERVICE_TIER_V1_DEFAULT: _ClassVar[ProviderServiceTierV1]
    PROVIDER_SERVICE_TIER_V1_FLEX: _ClassVar[ProviderServiceTierV1]
    PROVIDER_SERVICE_TIER_V1_PRIORITY: _ClassVar[ProviderServiceTierV1]
    PROVIDER_SERVICE_TIER_V1_STANDARD_ONLY: _ClassVar[ProviderServiceTierV1]

class BaselineStrategyV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BASELINE_STRATEGY_V1_UNSPECIFIED: _ClassVar[BaselineStrategyV1]
    BASELINE_STRATEGY_V1_REQUIRE_EXPLICIT: _ClassVar[BaselineStrategyV1]
    BASELINE_STRATEGY_V1_ALLOW_ROLLING_HISTORICAL: _ClassVar[BaselineStrategyV1]
    BASELINE_STRATEGY_V1_ALLOW_LAST_GOOD_CANDIDATE: _ClassVar[BaselineStrategyV1]

class EvaluatorOutputSchemaModeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATOR_OUTPUT_SCHEMA_MODE_V1_UNSPECIFIED: _ClassVar[EvaluatorOutputSchemaModeV1]
    EVALUATOR_OUTPUT_SCHEMA_MODE_V1_JSON_OBJECT: _ClassVar[EvaluatorOutputSchemaModeV1]
    EVALUATOR_OUTPUT_SCHEMA_MODE_V1_STRUCTURED_VERDICT: _ClassVar[EvaluatorOutputSchemaModeV1]
    EVALUATOR_OUTPUT_SCHEMA_MODE_V1_TEXT: _ClassVar[EvaluatorOutputSchemaModeV1]

class ProviderResponseParsingModeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROVIDER_RESPONSE_PARSING_MODE_V1_UNSPECIFIED: _ClassVar[ProviderResponseParsingModeV1]
    PROVIDER_RESPONSE_PARSING_MODE_V1_STRICT_JSON: _ClassVar[ProviderResponseParsingModeV1]
    PROVIDER_RESPONSE_PARSING_MODE_V1_RELAXED_JSON: _ClassVar[ProviderResponseParsingModeV1]
    PROVIDER_RESPONSE_PARSING_MODE_V1_TEXT: _ClassVar[ProviderResponseParsingModeV1]

class ScoreAggregationModeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCORE_AGGREGATION_MODE_V1_UNSPECIFIED: _ClassVar[ScoreAggregationModeV1]
    SCORE_AGGREGATION_MODE_V1_SINGLE: _ClassVar[ScoreAggregationModeV1]
    SCORE_AGGREGATION_MODE_V1_MEAN: _ClassVar[ScoreAggregationModeV1]
    SCORE_AGGREGATION_MODE_V1_MEDIAN: _ClassVar[ScoreAggregationModeV1]
    SCORE_AGGREGATION_MODE_V1_MAJORITY: _ClassVar[ScoreAggregationModeV1]

class ScoreConfidencePolicyV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCORE_CONFIDENCE_POLICY_V1_UNSPECIFIED: _ClassVar[ScoreConfidencePolicyV1]
    SCORE_CONFIDENCE_POLICY_V1_IGNORE: _ClassVar[ScoreConfidencePolicyV1]
    SCORE_CONFIDENCE_POLICY_V1_REQUIRE_PRESENT: _ClassVar[ScoreConfidencePolicyV1]
    SCORE_CONFIDENCE_POLICY_V1_REQUIRE_THRESHOLD: _ClassVar[ScoreConfidencePolicyV1]

class ScorerStarterKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCORER_STARTER_KIND_V1_UNSPECIFIED: _ClassVar[ScorerStarterKindV1]
    SCORER_STARTER_KIND_V1_LLM_JUDGE: _ClassVar[ScorerStarterKindV1]
    SCORER_STARTER_KIND_V1_DETERMINISTIC: _ClassVar[ScorerStarterKindV1]
    SCORER_STARTER_KIND_V1_CODE: _ClassVar[ScorerStarterKindV1]

class DatasetExportFormatV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_EXPORT_FORMAT_V1_UNSPECIFIED: _ClassVar[DatasetExportFormatV1]
    DATASET_EXPORT_FORMAT_V1_JSONL: _ClassVar[DatasetExportFormatV1]
    DATASET_EXPORT_FORMAT_V1_CSV: _ClassVar[DatasetExportFormatV1]

class OpenAiTextModelV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPEN_AI_TEXT_MODEL_V1_UNSPECIFIED: _ClassVar[OpenAiTextModelV1]
    OPEN_AI_TEXT_MODEL_V1_GPT_5_5: _ClassVar[OpenAiTextModelV1]
    OPEN_AI_TEXT_MODEL_V1_GPT_5_5_PRO: _ClassVar[OpenAiTextModelV1]
    OPEN_AI_TEXT_MODEL_V1_GPT_5_4: _ClassVar[OpenAiTextModelV1]
    OPEN_AI_TEXT_MODEL_V1_GPT_5_4_PRO: _ClassVar[OpenAiTextModelV1]
    OPEN_AI_TEXT_MODEL_V1_GPT_5_4_MINI: _ClassVar[OpenAiTextModelV1]
    OPEN_AI_TEXT_MODEL_V1_GPT_5_4_NANO: _ClassVar[OpenAiTextModelV1]
    OPEN_AI_TEXT_MODEL_V1_GPT_5: _ClassVar[OpenAiTextModelV1]
    OPEN_AI_TEXT_MODEL_V1_GPT_5_PRO: _ClassVar[OpenAiTextModelV1]
    OPEN_AI_TEXT_MODEL_V1_GPT_5_MINI: _ClassVar[OpenAiTextModelV1]
    OPEN_AI_TEXT_MODEL_V1_GPT_5_NANO: _ClassVar[OpenAiTextModelV1]
    OPEN_AI_TEXT_MODEL_V1_GPT_4_1: _ClassVar[OpenAiTextModelV1]
    OPEN_AI_TEXT_MODEL_V1_GPT_4_1_MINI: _ClassVar[OpenAiTextModelV1]
    OPEN_AI_TEXT_MODEL_V1_GPT_4O: _ClassVar[OpenAiTextModelV1]
    OPEN_AI_TEXT_MODEL_V1_GPT_4O_MINI: _ClassVar[OpenAiTextModelV1]
    OPEN_AI_TEXT_MODEL_V1_O3_PRO: _ClassVar[OpenAiTextModelV1]
    OPEN_AI_TEXT_MODEL_V1_O3: _ClassVar[OpenAiTextModelV1]
    OPEN_AI_TEXT_MODEL_V1_GPT_4: _ClassVar[OpenAiTextModelV1]

class AnthropicTextModelV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ANTHROPIC_TEXT_MODEL_V1_UNSPECIFIED: _ClassVar[AnthropicTextModelV1]
    ANTHROPIC_TEXT_MODEL_V1_OPUS_4_7: _ClassVar[AnthropicTextModelV1]
    ANTHROPIC_TEXT_MODEL_V1_OPUS_4_6: _ClassVar[AnthropicTextModelV1]
    ANTHROPIC_TEXT_MODEL_V1_OPUS_4_5_20251101: _ClassVar[AnthropicTextModelV1]
    ANTHROPIC_TEXT_MODEL_V1_OPUS_4_1_20250805: _ClassVar[AnthropicTextModelV1]
    ANTHROPIC_TEXT_MODEL_V1_SONNET_4_6: _ClassVar[AnthropicTextModelV1]
    ANTHROPIC_TEXT_MODEL_V1_SONNET_4_5_20250929: _ClassVar[AnthropicTextModelV1]
    ANTHROPIC_TEXT_MODEL_V1_HAIKU_4_5_20251001: _ClassVar[AnthropicTextModelV1]

class GoogleTextModelV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GOOGLE_TEXT_MODEL_V1_UNSPECIFIED: _ClassVar[GoogleTextModelV1]
    GOOGLE_TEXT_MODEL_V1_GEMINI_3_PRO: _ClassVar[GoogleTextModelV1]
    GOOGLE_TEXT_MODEL_V1_GEMINI_2_5_PRO: _ClassVar[GoogleTextModelV1]
    GOOGLE_TEXT_MODEL_V1_GEMINI_2_5_FLASH: _ClassVar[GoogleTextModelV1]

class XaiTextModelV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    XAI_TEXT_MODEL_V1_UNSPECIFIED: _ClassVar[XaiTextModelV1]
    XAI_TEXT_MODEL_V1_GROK_4: _ClassVar[XaiTextModelV1]
    XAI_TEXT_MODEL_V1_GROK_4_FAST: _ClassVar[XaiTextModelV1]
    XAI_TEXT_MODEL_V1_GROK_3: _ClassVar[XaiTextModelV1]

class MoonshotTextModelV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MOONSHOT_TEXT_MODEL_V1_UNSPECIFIED: _ClassVar[MoonshotTextModelV1]
    MOONSHOT_TEXT_MODEL_V1_KIMI_K2_THINKING: _ClassVar[MoonshotTextModelV1]
    MOONSHOT_TEXT_MODEL_V1_KIMI_K2_0905_PREVIEW: _ClassVar[MoonshotTextModelV1]

class DeepSeekTextModelV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEEP_SEEK_TEXT_MODEL_V1_UNSPECIFIED: _ClassVar[DeepSeekTextModelV1]
    DEEP_SEEK_TEXT_MODEL_V1_DEEPSEEK_REASONER: _ClassVar[DeepSeekTextModelV1]
    DEEP_SEEK_TEXT_MODEL_V1_DEEPSEEK_CHAT: _ClassVar[DeepSeekTextModelV1]

class OpenRouterTextModelV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPEN_ROUTER_TEXT_MODEL_V1_UNSPECIFIED: _ClassVar[OpenRouterTextModelV1]
    OPEN_ROUTER_TEXT_MODEL_V1_ANTHROPIC_CLAUDE_SONNET_4_6: _ClassVar[OpenRouterTextModelV1]
    OPEN_ROUTER_TEXT_MODEL_V1_OPENAI_GPT_5_5: _ClassVar[OpenRouterTextModelV1]
    OPEN_ROUTER_TEXT_MODEL_V1_MOONSHOTAI_KIMI_K2_THINKING: _ClassVar[OpenRouterTextModelV1]

class EvaluatorComparisonModeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATOR_COMPARISON_MODE_V1_UNSPECIFIED: _ClassVar[EvaluatorComparisonModeV1]
    EVALUATOR_COMPARISON_MODE_V1_EXACT: _ClassVar[EvaluatorComparisonModeV1]
    EVALUATOR_COMPARISON_MODE_V1_CONTAINS: _ClassVar[EvaluatorComparisonModeV1]
    EVALUATOR_COMPARISON_MODE_V1_NUMERIC_GTE: _ClassVar[EvaluatorComparisonModeV1]

class EvalJobStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVAL_JOB_STATE_V1_UNSPECIFIED: _ClassVar[EvalJobStateV1]
    EVAL_JOB_STATE_V1_PENDING: _ClassVar[EvalJobStateV1]
    EVAL_JOB_STATE_V1_RUNNING: _ClassVar[EvalJobStateV1]
    EVAL_JOB_STATE_V1_RETRYABLE: _ClassVar[EvalJobStateV1]
    EVAL_JOB_STATE_V1_SUCCEEDED: _ClassVar[EvalJobStateV1]
    EVAL_JOB_STATE_V1_FAILED: _ClassVar[EvalJobStateV1]
    EVAL_JOB_STATE_V1_DEAD_LETTER: _ClassVar[EvalJobStateV1]

class ExperimentRunStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXPERIMENT_RUN_STATE_V1_UNSPECIFIED: _ClassVar[ExperimentRunStateV1]
    EXPERIMENT_RUN_STATE_V1_PENDING: _ClassVar[ExperimentRunStateV1]
    EXPERIMENT_RUN_STATE_V1_RUNNING: _ClassVar[ExperimentRunStateV1]
    EXPERIMENT_RUN_STATE_V1_SUCCEEDED: _ClassVar[ExperimentRunStateV1]
    EXPERIMENT_RUN_STATE_V1_FAILED: _ClassVar[ExperimentRunStateV1]

class ExperimentRunAggregateStatusV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXPERIMENT_RUN_AGGREGATE_STATUS_V1_UNSPECIFIED: _ClassVar[ExperimentRunAggregateStatusV1]
    EXPERIMENT_RUN_AGGREGATE_STATUS_V1_PENDING: _ClassVar[ExperimentRunAggregateStatusV1]
    EXPERIMENT_RUN_AGGREGATE_STATUS_V1_RUNNING: _ClassVar[ExperimentRunAggregateStatusV1]
    EXPERIMENT_RUN_AGGREGATE_STATUS_V1_PASSED: _ClassVar[ExperimentRunAggregateStatusV1]
    EXPERIMENT_RUN_AGGREGATE_STATUS_V1_FAILED: _ClassVar[ExperimentRunAggregateStatusV1]
    EXPERIMENT_RUN_AGGREGATE_STATUS_V1_BLOCKED: _ClassVar[ExperimentRunAggregateStatusV1]
    EXPERIMENT_RUN_AGGREGATE_STATUS_V1_INCOMPLETE: _ClassVar[ExperimentRunAggregateStatusV1]

class ExperimentTargetModeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXPERIMENT_TARGET_MODE_V1_UNSPECIFIED: _ClassVar[ExperimentTargetModeV1]
    EXPERIMENT_TARGET_MODE_V1_RECORDED_OUTPUT: _ClassVar[ExperimentTargetModeV1]
    EXPERIMENT_TARGET_MODE_V1_HTTP_JSON_ENDPOINT: _ClassVar[ExperimentTargetModeV1]
    EXPERIMENT_TARGET_MODE_V1_PROVIDER_PROXY_PROMPT: _ClassVar[ExperimentTargetModeV1]

class ExperimentRunRoleV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXPERIMENT_RUN_ROLE_V1_UNSPECIFIED: _ClassVar[ExperimentRunRoleV1]
    EXPERIMENT_RUN_ROLE_V1_STANDALONE: _ClassVar[ExperimentRunRoleV1]
    EXPERIMENT_RUN_ROLE_V1_BASELINE: _ClassVar[ExperimentRunRoleV1]
    EXPERIMENT_RUN_ROLE_V1_CANDIDATE: _ClassVar[ExperimentRunRoleV1]
    EXPERIMENT_RUN_ROLE_V1_PAIRWISE: _ClassVar[ExperimentRunRoleV1]

class ExperimentRunFailureStageV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXPERIMENT_RUN_FAILURE_STAGE_V1_UNSPECIFIED: _ClassVar[ExperimentRunFailureStageV1]
    EXPERIMENT_RUN_FAILURE_STAGE_V1_TARGET_EXECUTION: _ClassVar[ExperimentRunFailureStageV1]
    EXPERIMENT_RUN_FAILURE_STAGE_V1_EVALUATOR_EXECUTION: _ClassVar[ExperimentRunFailureStageV1]

class ReleaseGateDecisionV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELEASE_GATE_DECISION_V1_UNSPECIFIED: _ClassVar[ReleaseGateDecisionV1]
    RELEASE_GATE_DECISION_V1_PASS: _ClassVar[ReleaseGateDecisionV1]
    RELEASE_GATE_DECISION_V1_FAIL: _ClassVar[ReleaseGateDecisionV1]
    RELEASE_GATE_DECISION_V1_INSUFFICIENT_DATA: _ClassVar[ReleaseGateDecisionV1]

class ReleaseDestinationChannelKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELEASE_DESTINATION_CHANNEL_KIND_V1_UNSPECIFIED: _ClassVar[ReleaseDestinationChannelKindV1]
    RELEASE_DESTINATION_CHANNEL_KIND_V1_EMAIL: _ClassVar[ReleaseDestinationChannelKindV1]
    RELEASE_DESTINATION_CHANNEL_KIND_V1_WEBHOOK: _ClassVar[ReleaseDestinationChannelKindV1]

class ReleaseAlertDeliveryStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELEASE_ALERT_DELIVERY_STATE_V1_UNSPECIFIED: _ClassVar[ReleaseAlertDeliveryStateV1]
    RELEASE_ALERT_DELIVERY_STATE_V1_PENDING: _ClassVar[ReleaseAlertDeliveryStateV1]
    RELEASE_ALERT_DELIVERY_STATE_V1_DELIVERED: _ClassVar[ReleaseAlertDeliveryStateV1]
    RELEASE_ALERT_DELIVERY_STATE_V1_RETRYABLE: _ClassVar[ReleaseAlertDeliveryStateV1]
    RELEASE_ALERT_DELIVERY_STATE_V1_FAILED: _ClassVar[ReleaseAlertDeliveryStateV1]
    RELEASE_ALERT_DELIVERY_STATE_V1_ACKNOWLEDGED: _ClassVar[ReleaseAlertDeliveryStateV1]
    RELEASE_ALERT_DELIVERY_STATE_V1_ESCALATED: _ClassVar[ReleaseAlertDeliveryStateV1]
    RELEASE_ALERT_DELIVERY_STATE_V1_SUPPRESSED: _ClassVar[ReleaseAlertDeliveryStateV1]

class RoutingPriorityTierV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROUTING_PRIORITY_TIER_V1_UNSPECIFIED: _ClassVar[RoutingPriorityTierV1]
    ROUTING_PRIORITY_TIER_V1_CRITICAL: _ClassVar[RoutingPriorityTierV1]
    ROUTING_PRIORITY_TIER_V1_STANDARD: _ClassVar[RoutingPriorityTierV1]
    ROUTING_PRIORITY_TIER_V1_BULK: _ClassVar[RoutingPriorityTierV1]

class RoutingSignalStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROUTING_SIGNAL_STATE_V1_UNSPECIFIED: _ClassVar[RoutingSignalStateV1]
    ROUTING_SIGNAL_STATE_V1_CAPTURED: _ClassVar[RoutingSignalStateV1]
    ROUTING_SIGNAL_STATE_V1_DISPATCHED: _ClassVar[RoutingSignalStateV1]
    ROUTING_SIGNAL_STATE_V1_PROCESSING: _ClassVar[RoutingSignalStateV1]
    ROUTING_SIGNAL_STATE_V1_MATERIALIZED: _ClassVar[RoutingSignalStateV1]
    ROUTING_SIGNAL_STATE_V1_SKIPPED: _ClassVar[RoutingSignalStateV1]
    ROUTING_SIGNAL_STATE_V1_RETRYABLE: _ClassVar[RoutingSignalStateV1]
    ROUTING_SIGNAL_STATE_V1_DEAD_LETTER: _ClassVar[RoutingSignalStateV1]

class RoutingSignalTypeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROUTING_SIGNAL_TYPE_V1_UNSPECIFIED: _ClassVar[RoutingSignalTypeV1]
    ROUTING_SIGNAL_TYPE_V1_SCORE: _ClassVar[RoutingSignalTypeV1]
    ROUTING_SIGNAL_TYPE_V1_FEEDBACK_EVENT: _ClassVar[RoutingSignalTypeV1]
    ROUTING_SIGNAL_TYPE_V1_OUTCOME_EVENT: _ClassVar[RoutingSignalTypeV1]
    ROUTING_SIGNAL_TYPE_V1_RELEASE_GATE_EVALUATION: _ClassVar[RoutingSignalTypeV1]

class RoutingAuditActionV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROUTING_AUDIT_ACTION_V1_UNSPECIFIED: _ClassVar[RoutingAuditActionV1]
    ROUTING_AUDIT_ACTION_V1_CAPTURED: _ClassVar[RoutingAuditActionV1]
    ROUTING_AUDIT_ACTION_V1_PUBLISHED: _ClassVar[RoutingAuditActionV1]
    ROUTING_AUDIT_ACTION_V1_CLAIMED: _ClassVar[RoutingAuditActionV1]
    ROUTING_AUDIT_ACTION_V1_POLICY_LOADED: _ClassVar[RoutingAuditActionV1]
    ROUTING_AUDIT_ACTION_V1_QUEUE_MATCHED: _ClassVar[RoutingAuditActionV1]
    ROUTING_AUDIT_ACTION_V1_QUEUE_SKIPPED: _ClassVar[RoutingAuditActionV1]
    ROUTING_AUDIT_ACTION_V1_TASK_MATERIALIZED: _ClassVar[RoutingAuditActionV1]
    ROUTING_AUDIT_ACTION_V1_SUPPRESSED: _ClassVar[RoutingAuditActionV1]
    ROUTING_AUDIT_ACTION_V1_RETRY_SCHEDULED: _ClassVar[RoutingAuditActionV1]
    ROUTING_AUDIT_ACTION_V1_DEAD_LETTERED: _ClassVar[RoutingAuditActionV1]
    ROUTING_AUDIT_ACTION_V1_REPLAYED: _ClassVar[RoutingAuditActionV1]

class AgenticDispatchKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENTIC_DISPATCH_KIND_V1_UNSPECIFIED: _ClassVar[AgenticDispatchKindV1]
    AGENTIC_DISPATCH_KIND_V1_EVAL_JOB: _ClassVar[AgenticDispatchKindV1]
    AGENTIC_DISPATCH_KIND_V1_ROUTING_SIGNAL: _ClassVar[AgenticDispatchKindV1]
    AGENTIC_DISPATCH_KIND_V1_EXPERIMENT_RUN_EXPANSION: _ClassVar[AgenticDispatchKindV1]

class AgenticDispatchStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENTIC_DISPATCH_STATE_V1_UNSPECIFIED: _ClassVar[AgenticDispatchStateV1]
    AGENTIC_DISPATCH_STATE_V1_PENDING: _ClassVar[AgenticDispatchStateV1]
    AGENTIC_DISPATCH_STATE_V1_DISPATCHED: _ClassVar[AgenticDispatchStateV1]
    AGENTIC_DISPATCH_STATE_V1_RETRYABLE: _ClassVar[AgenticDispatchStateV1]
    AGENTIC_DISPATCH_STATE_V1_DEAD_LETTER: _ClassVar[AgenticDispatchStateV1]

class ScorerAggregationModeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCORER_AGGREGATION_MODE_V1_UNSPECIFIED: _ClassVar[ScorerAggregationModeV1]
    SCORER_AGGREGATION_MODE_V1_WEIGHTED_MEAN: _ClassVar[ScorerAggregationModeV1]
    SCORER_AGGREGATION_MODE_V1_ALL_REQUIRED_PASS: _ClassVar[ScorerAggregationModeV1]
    SCORER_AGGREGATION_MODE_V1_ANY_FAIL_FAILS: _ClassVar[ScorerAggregationModeV1]
    SCORER_AGGREGATION_MODE_V1_MIN_SCORE: _ClassVar[ScorerAggregationModeV1]

class ScorerTargetRoleV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCORER_TARGET_ROLE_V1_UNSPECIFIED: _ClassVar[ScorerTargetRoleV1]
    SCORER_TARGET_ROLE_V1_USER: _ClassVar[ScorerTargetRoleV1]
    SCORER_TARGET_ROLE_V1_AGENT: _ClassVar[ScorerTargetRoleV1]
    SCORER_TARGET_ROLE_V1_TOOL: _ClassVar[ScorerTargetRoleV1]
    SCORER_TARGET_ROLE_V1_AGENT_WITH_TOOL_CALLS: _ClassVar[ScorerTargetRoleV1]
    SCORER_TARGET_ROLE_V1_SYSTEM: _ClassVar[ScorerTargetRoleV1]
    SCORER_TARGET_ROLE_V1_ANY: _ClassVar[ScorerTargetRoleV1]

class ScorerTurnSelectionModeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCORER_TURN_SELECTION_MODE_V1_UNSPECIFIED: _ClassVar[ScorerTurnSelectionModeV1]
    SCORER_TURN_SELECTION_MODE_V1_FIRST: _ClassVar[ScorerTurnSelectionModeV1]
    SCORER_TURN_SELECTION_MODE_V1_LAST: _ClassVar[ScorerTurnSelectionModeV1]
    SCORER_TURN_SELECTION_MODE_V1_NTH: _ClassVar[ScorerTurnSelectionModeV1]
    SCORER_TURN_SELECTION_MODE_V1_ALL: _ClassVar[ScorerTurnSelectionModeV1]
    SCORER_TURN_SELECTION_MODE_V1_JSON_PATH: _ClassVar[ScorerTurnSelectionModeV1]
    SCORER_TURN_SELECTION_MODE_V1_SPAN_FILTER: _ClassVar[ScorerTurnSelectionModeV1]

class ScorerReasoningModeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCORER_REASONING_MODE_V1_UNSPECIFIED: _ClassVar[ScorerReasoningModeV1]
    SCORER_REASONING_MODE_V1_OFF: _ClassVar[ScorerReasoningModeV1]
    SCORER_REASONING_MODE_V1_BRIEF_EXPLANATION: _ClassVar[ScorerReasoningModeV1]
    SCORER_REASONING_MODE_V1_EVIDENCE_SUMMARY: _ClassVar[ScorerReasoningModeV1]
    SCORER_REASONING_MODE_V1_REASONING_ENABLED: _ClassVar[ScorerReasoningModeV1]

class ScorerAutomationRuntimeScopeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCORER_AUTOMATION_RUNTIME_SCOPE_V1_UNSPECIFIED: _ClassVar[ScorerAutomationRuntimeScopeV1]
    SCORER_AUTOMATION_RUNTIME_SCOPE_V1_TRACE: _ClassVar[ScorerAutomationRuntimeScopeV1]
    SCORER_AUTOMATION_RUNTIME_SCOPE_V1_SESSION: _ClassVar[ScorerAutomationRuntimeScopeV1]
    SCORER_AUTOMATION_RUNTIME_SCOPE_V1_SPAN: _ClassVar[ScorerAutomationRuntimeScopeV1]

class ScorerAutomationExecutionStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCORER_AUTOMATION_EXECUTION_STATE_V1_UNSPECIFIED: _ClassVar[ScorerAutomationExecutionStateV1]
    SCORER_AUTOMATION_EXECUTION_STATE_V1_PENDING: _ClassVar[ScorerAutomationExecutionStateV1]
    SCORER_AUTOMATION_EXECUTION_STATE_V1_QUEUED: _ClassVar[ScorerAutomationExecutionStateV1]
    SCORER_AUTOMATION_EXECUTION_STATE_V1_SUCCEEDED: _ClassVar[ScorerAutomationExecutionStateV1]
    SCORER_AUTOMATION_EXECUTION_STATE_V1_FAILED: _ClassVar[ScorerAutomationExecutionStateV1]
    SCORER_AUTOMATION_EXECUTION_STATE_V1_SKIPPED: _ClassVar[ScorerAutomationExecutionStateV1]

class ExperimentRunExpansionStatusV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXPERIMENT_RUN_EXPANSION_STATUS_V1_UNSPECIFIED: _ClassVar[ExperimentRunExpansionStatusV1]
    EXPERIMENT_RUN_EXPANSION_STATUS_V1_NOT_REQUIRED: _ClassVar[ExperimentRunExpansionStatusV1]
    EXPERIMENT_RUN_EXPANSION_STATUS_V1_PENDING: _ClassVar[ExperimentRunExpansionStatusV1]
    EXPERIMENT_RUN_EXPANSION_STATUS_V1_RUNNING: _ClassVar[ExperimentRunExpansionStatusV1]
    EXPERIMENT_RUN_EXPANSION_STATUS_V1_RETRYABLE: _ClassVar[ExperimentRunExpansionStatusV1]
    EXPERIMENT_RUN_EXPANSION_STATUS_V1_SUCCEEDED: _ClassVar[ExperimentRunExpansionStatusV1]
    EXPERIMENT_RUN_EXPANSION_STATUS_V1_FAILED: _ClassVar[ExperimentRunExpansionStatusV1]

class ExperimentRunItemSortKeyV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXPERIMENT_RUN_ITEM_SORT_KEY_V1_UNSPECIFIED: _ClassVar[ExperimentRunItemSortKeyV1]
    EXPERIMENT_RUN_ITEM_SORT_KEY_V1_CREATED_AT: _ClassVar[ExperimentRunItemSortKeyV1]
    EXPERIMENT_RUN_ITEM_SORT_KEY_V1_STATE: _ClassVar[ExperimentRunItemSortKeyV1]
    EXPERIMENT_RUN_ITEM_SORT_KEY_V1_SCORE_VALUE: _ClassVar[ExperimentRunItemSortKeyV1]
    EXPERIMENT_RUN_ITEM_SORT_KEY_V1_EXECUTION_COST_USD: _ClassVar[ExperimentRunItemSortKeyV1]
    EXPERIMENT_RUN_ITEM_SORT_KEY_V1_DATASET_ITEM_ID: _ClassVar[ExperimentRunItemSortKeyV1]

class ExperimentRunTokenUsageCompletenessV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXPERIMENT_RUN_TOKEN_USAGE_COMPLETENESS_V1_UNSPECIFIED: _ClassVar[ExperimentRunTokenUsageCompletenessV1]
    EXPERIMENT_RUN_TOKEN_USAGE_COMPLETENESS_V1_EXACT: _ClassVar[ExperimentRunTokenUsageCompletenessV1]
    EXPERIMENT_RUN_TOKEN_USAGE_COMPLETENESS_V1_ESTIMATED_LEGACY_PREVIEW: _ClassVar[ExperimentRunTokenUsageCompletenessV1]
    EXPERIMENT_RUN_TOKEN_USAGE_COMPLETENESS_V1_ESTIMATED_INCOMPLETE: _ClassVar[ExperimentRunTokenUsageCompletenessV1]
    EXPERIMENT_RUN_TOKEN_USAGE_COMPLETENESS_V1_NOT_RECORDED: _ClassVar[ExperimentRunTokenUsageCompletenessV1]

class ExperimentRunComparisonAlignmentV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXPERIMENT_RUN_COMPARISON_ALIGNMENT_V1_UNSPECIFIED: _ClassVar[ExperimentRunComparisonAlignmentV1]
    EXPERIMENT_RUN_COMPARISON_ALIGNMENT_V1_ALIGNED: _ClassVar[ExperimentRunComparisonAlignmentV1]
    EXPERIMENT_RUN_COMPARISON_ALIGNMENT_V1_LEGACY_UNALIGNED_SUBJECTS: _ClassVar[ExperimentRunComparisonAlignmentV1]

class InvestigationModeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVESTIGATION_MODE_V1_UNSPECIFIED: _ClassVar[InvestigationModeV1]
    INVESTIGATION_MODE_V1_OVERVIEW: _ClassVar[InvestigationModeV1]
    INVESTIGATION_MODE_V1_FAILING_JUDGE_SCORE: _ClassVar[InvestigationModeV1]
    INVESTIGATION_MODE_V1_NEGATIVE_FEEDBACK: _ClassVar[InvestigationModeV1]
    INVESTIGATION_MODE_V1_BAD_OUTCOME: _ClassVar[InvestigationModeV1]
    INVESTIGATION_MODE_V1_COST_LATENCY: _ClassVar[InvestigationModeV1]
    INVESTIGATION_MODE_V1_TOOL_OR_MCP_ERROR: _ClassVar[InvestigationModeV1]
    INVESTIGATION_MODE_V1_CUSTOMER_IMPACT: _ClassVar[InvestigationModeV1]
    INVESTIGATION_MODE_V1_RELEASE_EVIDENCE: _ClassVar[InvestigationModeV1]
    INVESTIGATION_MODE_V1_DATASET_CANDIDATE: _ClassVar[InvestigationModeV1]

class TraceInvestigationSortKeyV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRACE_INVESTIGATION_SORT_KEY_V1_UNSPECIFIED: _ClassVar[TraceInvestigationSortKeyV1]
    TRACE_INVESTIGATION_SORT_KEY_V1_BACKEND_RANK: _ClassVar[TraceInvestigationSortKeyV1]
    TRACE_INVESTIGATION_SORT_KEY_V1_URGENCY: _ClassVar[TraceInvestigationSortKeyV1]
    TRACE_INVESTIGATION_SORT_KEY_V1_STARTED_AT: _ClassVar[TraceInvestigationSortKeyV1]
    TRACE_INVESTIGATION_SORT_KEY_V1_SCORE: _ClassVar[TraceInvestigationSortKeyV1]
    TRACE_INVESTIGATION_SORT_KEY_V1_COST: _ClassVar[TraceInvestigationSortKeyV1]
    TRACE_INVESTIGATION_SORT_KEY_V1_LATENCY: _ClassVar[TraceInvestigationSortKeyV1]
    TRACE_INVESTIGATION_SORT_KEY_V1_FEEDBACK_COUNT: _ClassVar[TraceInvestigationSortKeyV1]
    TRACE_INVESTIGATION_SORT_KEY_V1_REVIEW_TASK_COUNT: _ClassVar[TraceInvestigationSortKeyV1]
    TRACE_INVESTIGATION_SORT_KEY_V1_RELEASE_IMPACT: _ClassVar[TraceInvestigationSortKeyV1]

class TraceInvestigationFacetDimensionV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRACE_INVESTIGATION_FACET_DIMENSION_V1_UNSPECIFIED: _ClassVar[TraceInvestigationFacetDimensionV1]
    TRACE_INVESTIGATION_FACET_DIMENSION_V1_CUSTOMER: _ClassVar[TraceInvestigationFacetDimensionV1]
    TRACE_INVESTIGATION_FACET_DIMENSION_V1_DEPLOYMENT: _ClassVar[TraceInvestigationFacetDimensionV1]
    TRACE_INVESTIGATION_FACET_DIMENSION_V1_PROMPT_VERSION: _ClassVar[TraceInvestigationFacetDimensionV1]
    TRACE_INVESTIGATION_FACET_DIMENSION_V1_TOOL_VERSION: _ClassVar[TraceInvestigationFacetDimensionV1]
    TRACE_INVESTIGATION_FACET_DIMENSION_V1_MODEL_VERSION: _ClassVar[TraceInvestigationFacetDimensionV1]
    TRACE_INVESTIGATION_FACET_DIMENSION_V1_PROVIDER: _ClassVar[TraceInvestigationFacetDimensionV1]
    TRACE_INVESTIGATION_FACET_DIMENSION_V1_MCP_METHOD: _ClassVar[TraceInvestigationFacetDimensionV1]
    TRACE_INVESTIGATION_FACET_DIMENSION_V1_URGENCY: _ClassVar[TraceInvestigationFacetDimensionV1]
    TRACE_INVESTIGATION_FACET_DIMENSION_V1_REVIEW_STATE: _ClassVar[TraceInvestigationFacetDimensionV1]
    TRACE_INVESTIGATION_FACET_DIMENSION_V1_DATASET_STATE: _ClassVar[TraceInvestigationFacetDimensionV1]

class TraceInvestigationDetailPreviewLevelV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRACE_INVESTIGATION_DETAIL_PREVIEW_LEVEL_V1_UNSPECIFIED: _ClassVar[TraceInvestigationDetailPreviewLevelV1]
    TRACE_INVESTIGATION_DETAIL_PREVIEW_LEVEL_V1_NONE: _ClassVar[TraceInvestigationDetailPreviewLevelV1]
    TRACE_INVESTIGATION_DETAIL_PREVIEW_LEVEL_V1_COMPACT: _ClassVar[TraceInvestigationDetailPreviewLevelV1]
    TRACE_INVESTIGATION_DETAIL_PREVIEW_LEVEL_V1_FULL: _ClassVar[TraceInvestigationDetailPreviewLevelV1]

class RcaConfidenceV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RCA_CONFIDENCE_V1_UNSPECIFIED: _ClassVar[RcaConfidenceV1]
    RCA_CONFIDENCE_V1_LOW: _ClassVar[RcaConfidenceV1]
    RCA_CONFIDENCE_V1_MEDIUM: _ClassVar[RcaConfidenceV1]
    RCA_CONFIDENCE_V1_HIGH: _ClassVar[RcaConfidenceV1]

class TraceInvestigationActionKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRACE_INVESTIGATION_ACTION_KIND_V1_UNSPECIFIED: _ClassVar[TraceInvestigationActionKindV1]
    TRACE_INVESTIGATION_ACTION_KIND_V1_REVIEW_TASK: _ClassVar[TraceInvestigationActionKindV1]
    TRACE_INVESTIGATION_ACTION_KIND_V1_DATASET_ITEM: _ClassVar[TraceInvestigationActionKindV1]
    TRACE_INVESTIGATION_ACTION_KIND_V1_EVAL_CANDIDATE: _ClassVar[TraceInvestigationActionKindV1]
    TRACE_INVESTIGATION_ACTION_KIND_V1_RELEASE_EVIDENCE: _ClassVar[TraceInvestigationActionKindV1]
    TRACE_INVESTIGATION_ACTION_KIND_V1_ALERT: _ClassVar[TraceInvestigationActionKindV1]

class TraceInvestigationActionStatusV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRACE_INVESTIGATION_ACTION_STATUS_V1_UNSPECIFIED: _ClassVar[TraceInvestigationActionStatusV1]
    TRACE_INVESTIGATION_ACTION_STATUS_V1_CREATED: _ClassVar[TraceInvestigationActionStatusV1]
    TRACE_INVESTIGATION_ACTION_STATUS_V1_REPLAYED: _ClassVar[TraceInvestigationActionStatusV1]
    TRACE_INVESTIGATION_ACTION_STATUS_V1_PENDING: _ClassVar[TraceInvestigationActionStatusV1]
    TRACE_INVESTIGATION_ACTION_STATUS_V1_FAILED: _ClassVar[TraceInvestigationActionStatusV1]

class TraceInvestigationActionResourceKindV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRACE_INVESTIGATION_ACTION_RESOURCE_KIND_V1_UNSPECIFIED: _ClassVar[TraceInvestigationActionResourceKindV1]
    TRACE_INVESTIGATION_ACTION_RESOURCE_KIND_V1_ANNOTATION_TASK: _ClassVar[TraceInvestigationActionResourceKindV1]
    TRACE_INVESTIGATION_ACTION_RESOURCE_KIND_V1_DATASET_ITEM: _ClassVar[TraceInvestigationActionResourceKindV1]
    TRACE_INVESTIGATION_ACTION_RESOURCE_KIND_V1_DATASET_COLLECTION: _ClassVar[TraceInvestigationActionResourceKindV1]
    TRACE_INVESTIGATION_ACTION_RESOURCE_KIND_V1_DATASET_VERSION: _ClassVar[TraceInvestigationActionResourceKindV1]
    TRACE_INVESTIGATION_ACTION_RESOURCE_KIND_V1_EVAL_JOB: _ClassVar[TraceInvestigationActionResourceKindV1]
    TRACE_INVESTIGATION_ACTION_RESOURCE_KIND_V1_RELEASE_EVIDENCE: _ClassVar[TraceInvestigationActionResourceKindV1]
    TRACE_INVESTIGATION_ACTION_RESOURCE_KIND_V1_ALERT: _ClassVar[TraceInvestigationActionResourceKindV1]
    TRACE_INVESTIGATION_ACTION_RESOURCE_KIND_V1_EXPERIMENT_RUN: _ClassVar[TraceInvestigationActionResourceKindV1]
    TRACE_INVESTIGATION_ACTION_RESOURCE_KIND_V1_MONITOR: _ClassVar[TraceInvestigationActionResourceKindV1]

class TraceInvestigationDatasetIncludeV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRACE_INVESTIGATION_DATASET_INCLUDE_V1_UNSPECIFIED: _ClassVar[TraceInvestigationDatasetIncludeV1]
    TRACE_INVESTIGATION_DATASET_INCLUDE_V1_MESSAGES: _ClassVar[TraceInvestigationDatasetIncludeV1]
    TRACE_INVESTIGATION_DATASET_INCLUDE_V1_SPANS: _ClassVar[TraceInvestigationDatasetIncludeV1]
    TRACE_INVESTIGATION_DATASET_INCLUDE_V1_SCORES: _ClassVar[TraceInvestigationDatasetIncludeV1]
    TRACE_INVESTIGATION_DATASET_INCLUDE_V1_FEEDBACK: _ClassVar[TraceInvestigationDatasetIncludeV1]
    TRACE_INVESTIGATION_DATASET_INCLUDE_V1_OUTCOMES: _ClassVar[TraceInvestigationDatasetIncludeV1]
    TRACE_INVESTIGATION_DATASET_INCLUDE_V1_RAW_PAYLOADS: _ClassVar[TraceInvestigationDatasetIncludeV1]

class TraceInvestigationActionDestinationV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRACE_INVESTIGATION_ACTION_DESTINATION_V1_UNSPECIFIED: _ClassVar[TraceInvestigationActionDestinationV1]
    TRACE_INVESTIGATION_ACTION_DESTINATION_V1_REVIEW_QUEUE: _ClassVar[TraceInvestigationActionDestinationV1]
    TRACE_INVESTIGATION_ACTION_DESTINATION_V1_RELEASE_GOVERNANCE: _ClassVar[TraceInvestigationActionDestinationV1]
    TRACE_INVESTIGATION_ACTION_DESTINATION_V1_WEBHOOK: _ClassVar[TraceInvestigationActionDestinationV1]
    TRACE_INVESTIGATION_ACTION_DESTINATION_V1_ALERTS: _ClassVar[TraceInvestigationActionDestinationV1]

class TraceInvestigationAlertStateV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRACE_INVESTIGATION_ALERT_STATE_V1_UNSPECIFIED: _ClassVar[TraceInvestigationAlertStateV1]
    TRACE_INVESTIGATION_ALERT_STATE_V1_ACTIVE: _ClassVar[TraceInvestigationAlertStateV1]
    TRACE_INVESTIGATION_ALERT_STATE_V1_PAUSED: _ClassVar[TraceInvestigationAlertStateV1]
    TRACE_INVESTIGATION_ALERT_STATE_V1_DISABLED: _ClassVar[TraceInvestigationAlertStateV1]

class TraceInvestigationFilterOpV1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRACE_INVESTIGATION_FILTER_OP_V1_UNSPECIFIED: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_EQ: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_NE: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_GT: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_GE: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_LT: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_LE: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_LIKE: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_IN: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_NOT_IN: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_EXISTS: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_NOT_EXISTS: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_CONTAINS: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_NOT_CONTAINS: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_REGEX: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_NOT_REGEX: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_IS_NULL: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_IS_NOT_NULL: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_STARTS_WITH: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_NOT_STARTS_WITH: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_ENDS_WITH: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_NOT_ENDS_WITH: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_IEQ: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_INE: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_IS_EMPTY: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_IS_NOT_EMPTY: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_BETWEEN: _ClassVar[TraceInvestigationFilterOpV1]
    TRACE_INVESTIGATION_FILTER_OP_V1_NOT_BETWEEN: _ClassVar[TraceInvestigationFilterOpV1]
SCORE_SOURCE_V1_UNSPECIFIED: ScoreSourceV1
SCORE_SOURCE_V1_SDK: ScoreSourceV1
SCORE_SOURCE_V1_ONLINE: ScoreSourceV1
SCORE_SOURCE_V1_OFFLINE: ScoreSourceV1
SCORE_SOURCE_V1_ANNOTATION: ScoreSourceV1
SCORE_SOURCE_V1_API: ScoreSourceV1
FEEDBACK_SOURCE_TYPE_V1_UNSPECIFIED: FeedbackSourceTypeV1
FEEDBACK_SOURCE_TYPE_V1_USER: FeedbackSourceTypeV1
FEEDBACK_SOURCE_TYPE_V1_REVIEWER: FeedbackSourceTypeV1
FEEDBACK_SOURCE_TYPE_V1_API: FeedbackSourceTypeV1
FEEDBACK_SOURCE_TYPE_V1_EVALUATOR: FeedbackSourceTypeV1
FEEDBACK_SOURCE_TYPE_V1_SYSTEM: FeedbackSourceTypeV1
FEEDBACK_APPROVAL_STATUS_V1_UNSPECIFIED: FeedbackApprovalStatusV1
FEEDBACK_APPROVAL_STATUS_V1_NOT_APPLICABLE: FeedbackApprovalStatusV1
FEEDBACK_APPROVAL_STATUS_V1_PENDING: FeedbackApprovalStatusV1
FEEDBACK_APPROVAL_STATUS_V1_APPROVED: FeedbackApprovalStatusV1
FEEDBACK_APPROVAL_STATUS_V1_REJECTED: FeedbackApprovalStatusV1
DATASET_ITEM_SOURCE_KIND_V1_UNSPECIFIED: DatasetItemSourceKindV1
DATASET_ITEM_SOURCE_KIND_V1_TRACE: DatasetItemSourceKindV1
DATASET_ITEM_SOURCE_KIND_V1_SPAN: DatasetItemSourceKindV1
DATASET_ITEM_SOURCE_KIND_V1_OBSERVATION: DatasetItemSourceKindV1
DATASET_ITEM_SOURCE_KIND_V1_SESSION: DatasetItemSourceKindV1
DATASET_ITEM_SOURCE_KIND_V1_MANUAL: DatasetItemSourceKindV1
DATASET_IMPORT_FORMAT_V1_UNSPECIFIED: DatasetImportFormatV1
DATASET_IMPORT_FORMAT_V1_CSV: DatasetImportFormatV1
DATASET_IMPORT_FORMAT_V1_TSV: DatasetImportFormatV1
DATASET_IMPORT_FORMAT_V1_JSON: DatasetImportFormatV1
DATASET_IMPORT_FORMAT_V1_JSONL: DatasetImportFormatV1
DATASET_ITEM_SPLIT_V1_UNSPECIFIED: DatasetItemSplitV1
DATASET_ITEM_SPLIT_V1_TRAIN: DatasetItemSplitV1
DATASET_ITEM_SPLIT_V1_EVAL: DatasetItemSplitV1
DATASET_ITEM_SPLIT_V1_GOLDEN: DatasetItemSplitV1
DATASET_ITEM_SPLIT_V1_REGRESSION: DatasetItemSplitV1
DATASET_ITEM_SPLIT_V1_CANARY: DatasetItemSplitV1
ANNOTATION_ROUTING_REASON_V1_UNSPECIFIED: AnnotationRoutingReasonV1
ANNOTATION_ROUTING_REASON_V1_NEGATIVE_EXPLICIT_FEEDBACK: AnnotationRoutingReasonV1
ANNOTATION_ROUTING_REASON_V1_BAD_IMPLICIT_OUTCOME: AnnotationRoutingReasonV1
ANNOTATION_ROUTING_REASON_V1_EVALUATOR_DISAGREEMENT: AnnotationRoutingReasonV1
ANNOTATION_ROUTING_REASON_V1_HIGH_COST_FAILURE: AnnotationRoutingReasonV1
ANNOTATION_ROUTING_REASON_V1_STRATEGIC_CUSTOMER: AnnotationRoutingReasonV1
ANNOTATION_TASK_STATE_V1_UNSPECIFIED: AnnotationTaskStateV1
ANNOTATION_TASK_STATE_V1_OPEN: AnnotationTaskStateV1
ANNOTATION_TASK_STATE_V1_CLAIMED: AnnotationTaskStateV1
ANNOTATION_TASK_STATE_V1_COMPLETED: AnnotationTaskStateV1
ANNOTATION_TASK_STATE_V1_APPROVED: AnnotationTaskStateV1
ANNOTATION_TASK_STATE_V1_REJECTED: AnnotationTaskStateV1
ANNOTATION_TASK_MODE_V1_UNSPECIFIED: AnnotationTaskModeV1
ANNOTATION_TASK_MODE_V1_SINGLE: AnnotationTaskModeV1
ANNOTATION_TASK_MODE_V1_PAIRWISE: AnnotationTaskModeV1
ANNOTATION_PAIRWISE_WINNER_V1_UNSPECIFIED: AnnotationPairwiseWinnerV1
ANNOTATION_PAIRWISE_WINNER_V1_BASELINE: AnnotationPairwiseWinnerV1
ANNOTATION_PAIRWISE_WINNER_V1_CANDIDATE: AnnotationPairwiseWinnerV1
ANNOTATION_PAIRWISE_WINNER_V1_TIE: AnnotationPairwiseWinnerV1
PROMPT_ENVIRONMENT_V1_UNSPECIFIED: PromptEnvironmentV1
PROMPT_ENVIRONMENT_V1_DRAFT: PromptEnvironmentV1
PROMPT_ENVIRONMENT_V1_PROD: PromptEnvironmentV1
PROMPT_ENVIRONMENT_V1_CANDIDATE: PromptEnvironmentV1
PROMPT_ENVIRONMENT_V1_EXPERIMENT: PromptEnvironmentV1
EVALUATOR_EXECUTION_MODE_V1_UNSPECIFIED: EvaluatorExecutionModeV1
EVALUATOR_EXECUTION_MODE_V1_DETERMINISTIC: EvaluatorExecutionModeV1
EVALUATOR_EXECUTION_MODE_V1_ASYNC: EvaluatorExecutionModeV1
PROVIDER_EXECUTION_MODE_V1_UNSPECIFIED: ProviderExecutionModeV1
PROVIDER_EXECUTION_MODE_V1_BYO_PROVIDER_KEY_PROXY: ProviderExecutionModeV1
PROVIDER_EXECUTION_MODE_V1_PLATFORM_MANAGED_PROXY: ProviderExecutionModeV1
PROVIDER_EXECUTION_MODE_V1_CUSTOMER_HOSTED_ENDPOINT: ProviderExecutionModeV1
PROVIDER_EXECUTION_MODE_V1_SELF_HOSTED_LOCAL_MODEL: ProviderExecutionModeV1
PROVIDER_EXECUTION_MODE_V1_DETERMINISTIC_LOCAL_EXECUTOR: ProviderExecutionModeV1
PROVIDER_NAME_V1_UNSPECIFIED: ProviderNameV1
PROVIDER_NAME_V1_OPENAI: ProviderNameV1
PROVIDER_NAME_V1_ANTHROPIC: ProviderNameV1
PROVIDER_NAME_V1_GOOGLE: ProviderNameV1
PROVIDER_NAME_V1_XAI: ProviderNameV1
PROVIDER_NAME_V1_MOONSHOT: ProviderNameV1
PROVIDER_NAME_V1_DEEPSEEK: ProviderNameV1
PROVIDER_NAME_V1_OPENROUTER: ProviderNameV1
PROVIDER_KIND_V1_UNSPECIFIED: ProviderKindV1
PROVIDER_KIND_V1_LAB: ProviderKindV1
PROVIDER_KIND_V1_ROUTER: ProviderKindV1
PROVIDER_COST_MODE_V1_UNSPECIFIED: ProviderCostModeV1
PROVIDER_COST_MODE_V1_DISABLED: ProviderCostModeV1
PROVIDER_COST_MODE_V1_FIXED_USD: ProviderCostModeV1
PROVIDER_COST_MODE_V1_TOKEN_RATES: ProviderCostModeV1
PROVIDER_TOOL_CHOICE_V1_UNSPECIFIED: ProviderToolChoiceV1
PROVIDER_TOOL_CHOICE_V1_AUTO: ProviderToolChoiceV1
PROVIDER_TOOL_CHOICE_V1_NONE: ProviderToolChoiceV1
PROVIDER_TOOL_CHOICE_V1_REQUIRED: ProviderToolChoiceV1
PROVIDER_REASONING_EFFORT_V1_UNSPECIFIED: ProviderReasoningEffortV1
PROVIDER_REASONING_EFFORT_V1_NONE: ProviderReasoningEffortV1
PROVIDER_REASONING_EFFORT_V1_MINIMAL: ProviderReasoningEffortV1
PROVIDER_REASONING_EFFORT_V1_LOW: ProviderReasoningEffortV1
PROVIDER_REASONING_EFFORT_V1_MEDIUM: ProviderReasoningEffortV1
PROVIDER_REASONING_EFFORT_V1_HIGH: ProviderReasoningEffortV1
PROVIDER_REASONING_EFFORT_V1_XHIGH: ProviderReasoningEffortV1
PROVIDER_VERBOSITY_V1_UNSPECIFIED: ProviderVerbosityV1
PROVIDER_VERBOSITY_V1_DEFAULT: ProviderVerbosityV1
PROVIDER_VERBOSITY_V1_LOW: ProviderVerbosityV1
PROVIDER_VERBOSITY_V1_MEDIUM: ProviderVerbosityV1
PROVIDER_VERBOSITY_V1_HIGH: ProviderVerbosityV1
PROVIDER_TRUNCATION_V1_UNSPECIFIED: ProviderTruncationV1
PROVIDER_TRUNCATION_V1_AUTO: ProviderTruncationV1
PROVIDER_TRUNCATION_V1_DISABLED: ProviderTruncationV1
PROVIDER_PROMPT_CACHE_RETENTION_V1_UNSPECIFIED: ProviderPromptCacheRetentionV1
PROVIDER_PROMPT_CACHE_RETENTION_V1_IN_MEMORY: ProviderPromptCacheRetentionV1
PROVIDER_PROMPT_CACHE_RETENTION_V1_TWENTY_FOUR_HOURS: ProviderPromptCacheRetentionV1
PROVIDER_SERVICE_TIER_V1_UNSPECIFIED: ProviderServiceTierV1
PROVIDER_SERVICE_TIER_V1_AUTO: ProviderServiceTierV1
PROVIDER_SERVICE_TIER_V1_DEFAULT: ProviderServiceTierV1
PROVIDER_SERVICE_TIER_V1_FLEX: ProviderServiceTierV1
PROVIDER_SERVICE_TIER_V1_PRIORITY: ProviderServiceTierV1
PROVIDER_SERVICE_TIER_V1_STANDARD_ONLY: ProviderServiceTierV1
BASELINE_STRATEGY_V1_UNSPECIFIED: BaselineStrategyV1
BASELINE_STRATEGY_V1_REQUIRE_EXPLICIT: BaselineStrategyV1
BASELINE_STRATEGY_V1_ALLOW_ROLLING_HISTORICAL: BaselineStrategyV1
BASELINE_STRATEGY_V1_ALLOW_LAST_GOOD_CANDIDATE: BaselineStrategyV1
EVALUATOR_OUTPUT_SCHEMA_MODE_V1_UNSPECIFIED: EvaluatorOutputSchemaModeV1
EVALUATOR_OUTPUT_SCHEMA_MODE_V1_JSON_OBJECT: EvaluatorOutputSchemaModeV1
EVALUATOR_OUTPUT_SCHEMA_MODE_V1_STRUCTURED_VERDICT: EvaluatorOutputSchemaModeV1
EVALUATOR_OUTPUT_SCHEMA_MODE_V1_TEXT: EvaluatorOutputSchemaModeV1
PROVIDER_RESPONSE_PARSING_MODE_V1_UNSPECIFIED: ProviderResponseParsingModeV1
PROVIDER_RESPONSE_PARSING_MODE_V1_STRICT_JSON: ProviderResponseParsingModeV1
PROVIDER_RESPONSE_PARSING_MODE_V1_RELAXED_JSON: ProviderResponseParsingModeV1
PROVIDER_RESPONSE_PARSING_MODE_V1_TEXT: ProviderResponseParsingModeV1
SCORE_AGGREGATION_MODE_V1_UNSPECIFIED: ScoreAggregationModeV1
SCORE_AGGREGATION_MODE_V1_SINGLE: ScoreAggregationModeV1
SCORE_AGGREGATION_MODE_V1_MEAN: ScoreAggregationModeV1
SCORE_AGGREGATION_MODE_V1_MEDIAN: ScoreAggregationModeV1
SCORE_AGGREGATION_MODE_V1_MAJORITY: ScoreAggregationModeV1
SCORE_CONFIDENCE_POLICY_V1_UNSPECIFIED: ScoreConfidencePolicyV1
SCORE_CONFIDENCE_POLICY_V1_IGNORE: ScoreConfidencePolicyV1
SCORE_CONFIDENCE_POLICY_V1_REQUIRE_PRESENT: ScoreConfidencePolicyV1
SCORE_CONFIDENCE_POLICY_V1_REQUIRE_THRESHOLD: ScoreConfidencePolicyV1
SCORER_STARTER_KIND_V1_UNSPECIFIED: ScorerStarterKindV1
SCORER_STARTER_KIND_V1_LLM_JUDGE: ScorerStarterKindV1
SCORER_STARTER_KIND_V1_DETERMINISTIC: ScorerStarterKindV1
SCORER_STARTER_KIND_V1_CODE: ScorerStarterKindV1
DATASET_EXPORT_FORMAT_V1_UNSPECIFIED: DatasetExportFormatV1
DATASET_EXPORT_FORMAT_V1_JSONL: DatasetExportFormatV1
DATASET_EXPORT_FORMAT_V1_CSV: DatasetExportFormatV1
OPEN_AI_TEXT_MODEL_V1_UNSPECIFIED: OpenAiTextModelV1
OPEN_AI_TEXT_MODEL_V1_GPT_5_5: OpenAiTextModelV1
OPEN_AI_TEXT_MODEL_V1_GPT_5_5_PRO: OpenAiTextModelV1
OPEN_AI_TEXT_MODEL_V1_GPT_5_4: OpenAiTextModelV1
OPEN_AI_TEXT_MODEL_V1_GPT_5_4_PRO: OpenAiTextModelV1
OPEN_AI_TEXT_MODEL_V1_GPT_5_4_MINI: OpenAiTextModelV1
OPEN_AI_TEXT_MODEL_V1_GPT_5_4_NANO: OpenAiTextModelV1
OPEN_AI_TEXT_MODEL_V1_GPT_5: OpenAiTextModelV1
OPEN_AI_TEXT_MODEL_V1_GPT_5_PRO: OpenAiTextModelV1
OPEN_AI_TEXT_MODEL_V1_GPT_5_MINI: OpenAiTextModelV1
OPEN_AI_TEXT_MODEL_V1_GPT_5_NANO: OpenAiTextModelV1
OPEN_AI_TEXT_MODEL_V1_GPT_4_1: OpenAiTextModelV1
OPEN_AI_TEXT_MODEL_V1_GPT_4_1_MINI: OpenAiTextModelV1
OPEN_AI_TEXT_MODEL_V1_GPT_4O: OpenAiTextModelV1
OPEN_AI_TEXT_MODEL_V1_GPT_4O_MINI: OpenAiTextModelV1
OPEN_AI_TEXT_MODEL_V1_O3_PRO: OpenAiTextModelV1
OPEN_AI_TEXT_MODEL_V1_O3: OpenAiTextModelV1
OPEN_AI_TEXT_MODEL_V1_GPT_4: OpenAiTextModelV1
ANTHROPIC_TEXT_MODEL_V1_UNSPECIFIED: AnthropicTextModelV1
ANTHROPIC_TEXT_MODEL_V1_OPUS_4_7: AnthropicTextModelV1
ANTHROPIC_TEXT_MODEL_V1_OPUS_4_6: AnthropicTextModelV1
ANTHROPIC_TEXT_MODEL_V1_OPUS_4_5_20251101: AnthropicTextModelV1
ANTHROPIC_TEXT_MODEL_V1_OPUS_4_1_20250805: AnthropicTextModelV1
ANTHROPIC_TEXT_MODEL_V1_SONNET_4_6: AnthropicTextModelV1
ANTHROPIC_TEXT_MODEL_V1_SONNET_4_5_20250929: AnthropicTextModelV1
ANTHROPIC_TEXT_MODEL_V1_HAIKU_4_5_20251001: AnthropicTextModelV1
GOOGLE_TEXT_MODEL_V1_UNSPECIFIED: GoogleTextModelV1
GOOGLE_TEXT_MODEL_V1_GEMINI_3_PRO: GoogleTextModelV1
GOOGLE_TEXT_MODEL_V1_GEMINI_2_5_PRO: GoogleTextModelV1
GOOGLE_TEXT_MODEL_V1_GEMINI_2_5_FLASH: GoogleTextModelV1
XAI_TEXT_MODEL_V1_UNSPECIFIED: XaiTextModelV1
XAI_TEXT_MODEL_V1_GROK_4: XaiTextModelV1
XAI_TEXT_MODEL_V1_GROK_4_FAST: XaiTextModelV1
XAI_TEXT_MODEL_V1_GROK_3: XaiTextModelV1
MOONSHOT_TEXT_MODEL_V1_UNSPECIFIED: MoonshotTextModelV1
MOONSHOT_TEXT_MODEL_V1_KIMI_K2_THINKING: MoonshotTextModelV1
MOONSHOT_TEXT_MODEL_V1_KIMI_K2_0905_PREVIEW: MoonshotTextModelV1
DEEP_SEEK_TEXT_MODEL_V1_UNSPECIFIED: DeepSeekTextModelV1
DEEP_SEEK_TEXT_MODEL_V1_DEEPSEEK_REASONER: DeepSeekTextModelV1
DEEP_SEEK_TEXT_MODEL_V1_DEEPSEEK_CHAT: DeepSeekTextModelV1
OPEN_ROUTER_TEXT_MODEL_V1_UNSPECIFIED: OpenRouterTextModelV1
OPEN_ROUTER_TEXT_MODEL_V1_ANTHROPIC_CLAUDE_SONNET_4_6: OpenRouterTextModelV1
OPEN_ROUTER_TEXT_MODEL_V1_OPENAI_GPT_5_5: OpenRouterTextModelV1
OPEN_ROUTER_TEXT_MODEL_V1_MOONSHOTAI_KIMI_K2_THINKING: OpenRouterTextModelV1
EVALUATOR_COMPARISON_MODE_V1_UNSPECIFIED: EvaluatorComparisonModeV1
EVALUATOR_COMPARISON_MODE_V1_EXACT: EvaluatorComparisonModeV1
EVALUATOR_COMPARISON_MODE_V1_CONTAINS: EvaluatorComparisonModeV1
EVALUATOR_COMPARISON_MODE_V1_NUMERIC_GTE: EvaluatorComparisonModeV1
EVAL_JOB_STATE_V1_UNSPECIFIED: EvalJobStateV1
EVAL_JOB_STATE_V1_PENDING: EvalJobStateV1
EVAL_JOB_STATE_V1_RUNNING: EvalJobStateV1
EVAL_JOB_STATE_V1_RETRYABLE: EvalJobStateV1
EVAL_JOB_STATE_V1_SUCCEEDED: EvalJobStateV1
EVAL_JOB_STATE_V1_FAILED: EvalJobStateV1
EVAL_JOB_STATE_V1_DEAD_LETTER: EvalJobStateV1
EXPERIMENT_RUN_STATE_V1_UNSPECIFIED: ExperimentRunStateV1
EXPERIMENT_RUN_STATE_V1_PENDING: ExperimentRunStateV1
EXPERIMENT_RUN_STATE_V1_RUNNING: ExperimentRunStateV1
EXPERIMENT_RUN_STATE_V1_SUCCEEDED: ExperimentRunStateV1
EXPERIMENT_RUN_STATE_V1_FAILED: ExperimentRunStateV1
EXPERIMENT_RUN_AGGREGATE_STATUS_V1_UNSPECIFIED: ExperimentRunAggregateStatusV1
EXPERIMENT_RUN_AGGREGATE_STATUS_V1_PENDING: ExperimentRunAggregateStatusV1
EXPERIMENT_RUN_AGGREGATE_STATUS_V1_RUNNING: ExperimentRunAggregateStatusV1
EXPERIMENT_RUN_AGGREGATE_STATUS_V1_PASSED: ExperimentRunAggregateStatusV1
EXPERIMENT_RUN_AGGREGATE_STATUS_V1_FAILED: ExperimentRunAggregateStatusV1
EXPERIMENT_RUN_AGGREGATE_STATUS_V1_BLOCKED: ExperimentRunAggregateStatusV1
EXPERIMENT_RUN_AGGREGATE_STATUS_V1_INCOMPLETE: ExperimentRunAggregateStatusV1
EXPERIMENT_TARGET_MODE_V1_UNSPECIFIED: ExperimentTargetModeV1
EXPERIMENT_TARGET_MODE_V1_RECORDED_OUTPUT: ExperimentTargetModeV1
EXPERIMENT_TARGET_MODE_V1_HTTP_JSON_ENDPOINT: ExperimentTargetModeV1
EXPERIMENT_TARGET_MODE_V1_PROVIDER_PROXY_PROMPT: ExperimentTargetModeV1
EXPERIMENT_RUN_ROLE_V1_UNSPECIFIED: ExperimentRunRoleV1
EXPERIMENT_RUN_ROLE_V1_STANDALONE: ExperimentRunRoleV1
EXPERIMENT_RUN_ROLE_V1_BASELINE: ExperimentRunRoleV1
EXPERIMENT_RUN_ROLE_V1_CANDIDATE: ExperimentRunRoleV1
EXPERIMENT_RUN_ROLE_V1_PAIRWISE: ExperimentRunRoleV1
EXPERIMENT_RUN_FAILURE_STAGE_V1_UNSPECIFIED: ExperimentRunFailureStageV1
EXPERIMENT_RUN_FAILURE_STAGE_V1_TARGET_EXECUTION: ExperimentRunFailureStageV1
EXPERIMENT_RUN_FAILURE_STAGE_V1_EVALUATOR_EXECUTION: ExperimentRunFailureStageV1
RELEASE_GATE_DECISION_V1_UNSPECIFIED: ReleaseGateDecisionV1
RELEASE_GATE_DECISION_V1_PASS: ReleaseGateDecisionV1
RELEASE_GATE_DECISION_V1_FAIL: ReleaseGateDecisionV1
RELEASE_GATE_DECISION_V1_INSUFFICIENT_DATA: ReleaseGateDecisionV1
RELEASE_DESTINATION_CHANNEL_KIND_V1_UNSPECIFIED: ReleaseDestinationChannelKindV1
RELEASE_DESTINATION_CHANNEL_KIND_V1_EMAIL: ReleaseDestinationChannelKindV1
RELEASE_DESTINATION_CHANNEL_KIND_V1_WEBHOOK: ReleaseDestinationChannelKindV1
RELEASE_ALERT_DELIVERY_STATE_V1_UNSPECIFIED: ReleaseAlertDeliveryStateV1
RELEASE_ALERT_DELIVERY_STATE_V1_PENDING: ReleaseAlertDeliveryStateV1
RELEASE_ALERT_DELIVERY_STATE_V1_DELIVERED: ReleaseAlertDeliveryStateV1
RELEASE_ALERT_DELIVERY_STATE_V1_RETRYABLE: ReleaseAlertDeliveryStateV1
RELEASE_ALERT_DELIVERY_STATE_V1_FAILED: ReleaseAlertDeliveryStateV1
RELEASE_ALERT_DELIVERY_STATE_V1_ACKNOWLEDGED: ReleaseAlertDeliveryStateV1
RELEASE_ALERT_DELIVERY_STATE_V1_ESCALATED: ReleaseAlertDeliveryStateV1
RELEASE_ALERT_DELIVERY_STATE_V1_SUPPRESSED: ReleaseAlertDeliveryStateV1
ROUTING_PRIORITY_TIER_V1_UNSPECIFIED: RoutingPriorityTierV1
ROUTING_PRIORITY_TIER_V1_CRITICAL: RoutingPriorityTierV1
ROUTING_PRIORITY_TIER_V1_STANDARD: RoutingPriorityTierV1
ROUTING_PRIORITY_TIER_V1_BULK: RoutingPriorityTierV1
ROUTING_SIGNAL_STATE_V1_UNSPECIFIED: RoutingSignalStateV1
ROUTING_SIGNAL_STATE_V1_CAPTURED: RoutingSignalStateV1
ROUTING_SIGNAL_STATE_V1_DISPATCHED: RoutingSignalStateV1
ROUTING_SIGNAL_STATE_V1_PROCESSING: RoutingSignalStateV1
ROUTING_SIGNAL_STATE_V1_MATERIALIZED: RoutingSignalStateV1
ROUTING_SIGNAL_STATE_V1_SKIPPED: RoutingSignalStateV1
ROUTING_SIGNAL_STATE_V1_RETRYABLE: RoutingSignalStateV1
ROUTING_SIGNAL_STATE_V1_DEAD_LETTER: RoutingSignalStateV1
ROUTING_SIGNAL_TYPE_V1_UNSPECIFIED: RoutingSignalTypeV1
ROUTING_SIGNAL_TYPE_V1_SCORE: RoutingSignalTypeV1
ROUTING_SIGNAL_TYPE_V1_FEEDBACK_EVENT: RoutingSignalTypeV1
ROUTING_SIGNAL_TYPE_V1_OUTCOME_EVENT: RoutingSignalTypeV1
ROUTING_SIGNAL_TYPE_V1_RELEASE_GATE_EVALUATION: RoutingSignalTypeV1
ROUTING_AUDIT_ACTION_V1_UNSPECIFIED: RoutingAuditActionV1
ROUTING_AUDIT_ACTION_V1_CAPTURED: RoutingAuditActionV1
ROUTING_AUDIT_ACTION_V1_PUBLISHED: RoutingAuditActionV1
ROUTING_AUDIT_ACTION_V1_CLAIMED: RoutingAuditActionV1
ROUTING_AUDIT_ACTION_V1_POLICY_LOADED: RoutingAuditActionV1
ROUTING_AUDIT_ACTION_V1_QUEUE_MATCHED: RoutingAuditActionV1
ROUTING_AUDIT_ACTION_V1_QUEUE_SKIPPED: RoutingAuditActionV1
ROUTING_AUDIT_ACTION_V1_TASK_MATERIALIZED: RoutingAuditActionV1
ROUTING_AUDIT_ACTION_V1_SUPPRESSED: RoutingAuditActionV1
ROUTING_AUDIT_ACTION_V1_RETRY_SCHEDULED: RoutingAuditActionV1
ROUTING_AUDIT_ACTION_V1_DEAD_LETTERED: RoutingAuditActionV1
ROUTING_AUDIT_ACTION_V1_REPLAYED: RoutingAuditActionV1
AGENTIC_DISPATCH_KIND_V1_UNSPECIFIED: AgenticDispatchKindV1
AGENTIC_DISPATCH_KIND_V1_EVAL_JOB: AgenticDispatchKindV1
AGENTIC_DISPATCH_KIND_V1_ROUTING_SIGNAL: AgenticDispatchKindV1
AGENTIC_DISPATCH_KIND_V1_EXPERIMENT_RUN_EXPANSION: AgenticDispatchKindV1
AGENTIC_DISPATCH_STATE_V1_UNSPECIFIED: AgenticDispatchStateV1
AGENTIC_DISPATCH_STATE_V1_PENDING: AgenticDispatchStateV1
AGENTIC_DISPATCH_STATE_V1_DISPATCHED: AgenticDispatchStateV1
AGENTIC_DISPATCH_STATE_V1_RETRYABLE: AgenticDispatchStateV1
AGENTIC_DISPATCH_STATE_V1_DEAD_LETTER: AgenticDispatchStateV1
SCORER_AGGREGATION_MODE_V1_UNSPECIFIED: ScorerAggregationModeV1
SCORER_AGGREGATION_MODE_V1_WEIGHTED_MEAN: ScorerAggregationModeV1
SCORER_AGGREGATION_MODE_V1_ALL_REQUIRED_PASS: ScorerAggregationModeV1
SCORER_AGGREGATION_MODE_V1_ANY_FAIL_FAILS: ScorerAggregationModeV1
SCORER_AGGREGATION_MODE_V1_MIN_SCORE: ScorerAggregationModeV1
SCORER_TARGET_ROLE_V1_UNSPECIFIED: ScorerTargetRoleV1
SCORER_TARGET_ROLE_V1_USER: ScorerTargetRoleV1
SCORER_TARGET_ROLE_V1_AGENT: ScorerTargetRoleV1
SCORER_TARGET_ROLE_V1_TOOL: ScorerTargetRoleV1
SCORER_TARGET_ROLE_V1_AGENT_WITH_TOOL_CALLS: ScorerTargetRoleV1
SCORER_TARGET_ROLE_V1_SYSTEM: ScorerTargetRoleV1
SCORER_TARGET_ROLE_V1_ANY: ScorerTargetRoleV1
SCORER_TURN_SELECTION_MODE_V1_UNSPECIFIED: ScorerTurnSelectionModeV1
SCORER_TURN_SELECTION_MODE_V1_FIRST: ScorerTurnSelectionModeV1
SCORER_TURN_SELECTION_MODE_V1_LAST: ScorerTurnSelectionModeV1
SCORER_TURN_SELECTION_MODE_V1_NTH: ScorerTurnSelectionModeV1
SCORER_TURN_SELECTION_MODE_V1_ALL: ScorerTurnSelectionModeV1
SCORER_TURN_SELECTION_MODE_V1_JSON_PATH: ScorerTurnSelectionModeV1
SCORER_TURN_SELECTION_MODE_V1_SPAN_FILTER: ScorerTurnSelectionModeV1
SCORER_REASONING_MODE_V1_UNSPECIFIED: ScorerReasoningModeV1
SCORER_REASONING_MODE_V1_OFF: ScorerReasoningModeV1
SCORER_REASONING_MODE_V1_BRIEF_EXPLANATION: ScorerReasoningModeV1
SCORER_REASONING_MODE_V1_EVIDENCE_SUMMARY: ScorerReasoningModeV1
SCORER_REASONING_MODE_V1_REASONING_ENABLED: ScorerReasoningModeV1
SCORER_AUTOMATION_RUNTIME_SCOPE_V1_UNSPECIFIED: ScorerAutomationRuntimeScopeV1
SCORER_AUTOMATION_RUNTIME_SCOPE_V1_TRACE: ScorerAutomationRuntimeScopeV1
SCORER_AUTOMATION_RUNTIME_SCOPE_V1_SESSION: ScorerAutomationRuntimeScopeV1
SCORER_AUTOMATION_RUNTIME_SCOPE_V1_SPAN: ScorerAutomationRuntimeScopeV1
SCORER_AUTOMATION_EXECUTION_STATE_V1_UNSPECIFIED: ScorerAutomationExecutionStateV1
SCORER_AUTOMATION_EXECUTION_STATE_V1_PENDING: ScorerAutomationExecutionStateV1
SCORER_AUTOMATION_EXECUTION_STATE_V1_QUEUED: ScorerAutomationExecutionStateV1
SCORER_AUTOMATION_EXECUTION_STATE_V1_SUCCEEDED: ScorerAutomationExecutionStateV1
SCORER_AUTOMATION_EXECUTION_STATE_V1_FAILED: ScorerAutomationExecutionStateV1
SCORER_AUTOMATION_EXECUTION_STATE_V1_SKIPPED: ScorerAutomationExecutionStateV1
EXPERIMENT_RUN_EXPANSION_STATUS_V1_UNSPECIFIED: ExperimentRunExpansionStatusV1
EXPERIMENT_RUN_EXPANSION_STATUS_V1_NOT_REQUIRED: ExperimentRunExpansionStatusV1
EXPERIMENT_RUN_EXPANSION_STATUS_V1_PENDING: ExperimentRunExpansionStatusV1
EXPERIMENT_RUN_EXPANSION_STATUS_V1_RUNNING: ExperimentRunExpansionStatusV1
EXPERIMENT_RUN_EXPANSION_STATUS_V1_RETRYABLE: ExperimentRunExpansionStatusV1
EXPERIMENT_RUN_EXPANSION_STATUS_V1_SUCCEEDED: ExperimentRunExpansionStatusV1
EXPERIMENT_RUN_EXPANSION_STATUS_V1_FAILED: ExperimentRunExpansionStatusV1
EXPERIMENT_RUN_ITEM_SORT_KEY_V1_UNSPECIFIED: ExperimentRunItemSortKeyV1
EXPERIMENT_RUN_ITEM_SORT_KEY_V1_CREATED_AT: ExperimentRunItemSortKeyV1
EXPERIMENT_RUN_ITEM_SORT_KEY_V1_STATE: ExperimentRunItemSortKeyV1
EXPERIMENT_RUN_ITEM_SORT_KEY_V1_SCORE_VALUE: ExperimentRunItemSortKeyV1
EXPERIMENT_RUN_ITEM_SORT_KEY_V1_EXECUTION_COST_USD: ExperimentRunItemSortKeyV1
EXPERIMENT_RUN_ITEM_SORT_KEY_V1_DATASET_ITEM_ID: ExperimentRunItemSortKeyV1
EXPERIMENT_RUN_TOKEN_USAGE_COMPLETENESS_V1_UNSPECIFIED: ExperimentRunTokenUsageCompletenessV1
EXPERIMENT_RUN_TOKEN_USAGE_COMPLETENESS_V1_EXACT: ExperimentRunTokenUsageCompletenessV1
EXPERIMENT_RUN_TOKEN_USAGE_COMPLETENESS_V1_ESTIMATED_LEGACY_PREVIEW: ExperimentRunTokenUsageCompletenessV1
EXPERIMENT_RUN_TOKEN_USAGE_COMPLETENESS_V1_ESTIMATED_INCOMPLETE: ExperimentRunTokenUsageCompletenessV1
EXPERIMENT_RUN_TOKEN_USAGE_COMPLETENESS_V1_NOT_RECORDED: ExperimentRunTokenUsageCompletenessV1
EXPERIMENT_RUN_COMPARISON_ALIGNMENT_V1_UNSPECIFIED: ExperimentRunComparisonAlignmentV1
EXPERIMENT_RUN_COMPARISON_ALIGNMENT_V1_ALIGNED: ExperimentRunComparisonAlignmentV1
EXPERIMENT_RUN_COMPARISON_ALIGNMENT_V1_LEGACY_UNALIGNED_SUBJECTS: ExperimentRunComparisonAlignmentV1
INVESTIGATION_MODE_V1_UNSPECIFIED: InvestigationModeV1
INVESTIGATION_MODE_V1_OVERVIEW: InvestigationModeV1
INVESTIGATION_MODE_V1_FAILING_JUDGE_SCORE: InvestigationModeV1
INVESTIGATION_MODE_V1_NEGATIVE_FEEDBACK: InvestigationModeV1
INVESTIGATION_MODE_V1_BAD_OUTCOME: InvestigationModeV1
INVESTIGATION_MODE_V1_COST_LATENCY: InvestigationModeV1
INVESTIGATION_MODE_V1_TOOL_OR_MCP_ERROR: InvestigationModeV1
INVESTIGATION_MODE_V1_CUSTOMER_IMPACT: InvestigationModeV1
INVESTIGATION_MODE_V1_RELEASE_EVIDENCE: InvestigationModeV1
INVESTIGATION_MODE_V1_DATASET_CANDIDATE: InvestigationModeV1
TRACE_INVESTIGATION_SORT_KEY_V1_UNSPECIFIED: TraceInvestigationSortKeyV1
TRACE_INVESTIGATION_SORT_KEY_V1_BACKEND_RANK: TraceInvestigationSortKeyV1
TRACE_INVESTIGATION_SORT_KEY_V1_URGENCY: TraceInvestigationSortKeyV1
TRACE_INVESTIGATION_SORT_KEY_V1_STARTED_AT: TraceInvestigationSortKeyV1
TRACE_INVESTIGATION_SORT_KEY_V1_SCORE: TraceInvestigationSortKeyV1
TRACE_INVESTIGATION_SORT_KEY_V1_COST: TraceInvestigationSortKeyV1
TRACE_INVESTIGATION_SORT_KEY_V1_LATENCY: TraceInvestigationSortKeyV1
TRACE_INVESTIGATION_SORT_KEY_V1_FEEDBACK_COUNT: TraceInvestigationSortKeyV1
TRACE_INVESTIGATION_SORT_KEY_V1_REVIEW_TASK_COUNT: TraceInvestigationSortKeyV1
TRACE_INVESTIGATION_SORT_KEY_V1_RELEASE_IMPACT: TraceInvestigationSortKeyV1
TRACE_INVESTIGATION_FACET_DIMENSION_V1_UNSPECIFIED: TraceInvestigationFacetDimensionV1
TRACE_INVESTIGATION_FACET_DIMENSION_V1_CUSTOMER: TraceInvestigationFacetDimensionV1
TRACE_INVESTIGATION_FACET_DIMENSION_V1_DEPLOYMENT: TraceInvestigationFacetDimensionV1
TRACE_INVESTIGATION_FACET_DIMENSION_V1_PROMPT_VERSION: TraceInvestigationFacetDimensionV1
TRACE_INVESTIGATION_FACET_DIMENSION_V1_TOOL_VERSION: TraceInvestigationFacetDimensionV1
TRACE_INVESTIGATION_FACET_DIMENSION_V1_MODEL_VERSION: TraceInvestigationFacetDimensionV1
TRACE_INVESTIGATION_FACET_DIMENSION_V1_PROVIDER: TraceInvestigationFacetDimensionV1
TRACE_INVESTIGATION_FACET_DIMENSION_V1_MCP_METHOD: TraceInvestigationFacetDimensionV1
TRACE_INVESTIGATION_FACET_DIMENSION_V1_URGENCY: TraceInvestigationFacetDimensionV1
TRACE_INVESTIGATION_FACET_DIMENSION_V1_REVIEW_STATE: TraceInvestigationFacetDimensionV1
TRACE_INVESTIGATION_FACET_DIMENSION_V1_DATASET_STATE: TraceInvestigationFacetDimensionV1
TRACE_INVESTIGATION_DETAIL_PREVIEW_LEVEL_V1_UNSPECIFIED: TraceInvestigationDetailPreviewLevelV1
TRACE_INVESTIGATION_DETAIL_PREVIEW_LEVEL_V1_NONE: TraceInvestigationDetailPreviewLevelV1
TRACE_INVESTIGATION_DETAIL_PREVIEW_LEVEL_V1_COMPACT: TraceInvestigationDetailPreviewLevelV1
TRACE_INVESTIGATION_DETAIL_PREVIEW_LEVEL_V1_FULL: TraceInvestigationDetailPreviewLevelV1
RCA_CONFIDENCE_V1_UNSPECIFIED: RcaConfidenceV1
RCA_CONFIDENCE_V1_LOW: RcaConfidenceV1
RCA_CONFIDENCE_V1_MEDIUM: RcaConfidenceV1
RCA_CONFIDENCE_V1_HIGH: RcaConfidenceV1
TRACE_INVESTIGATION_ACTION_KIND_V1_UNSPECIFIED: TraceInvestigationActionKindV1
TRACE_INVESTIGATION_ACTION_KIND_V1_REVIEW_TASK: TraceInvestigationActionKindV1
TRACE_INVESTIGATION_ACTION_KIND_V1_DATASET_ITEM: TraceInvestigationActionKindV1
TRACE_INVESTIGATION_ACTION_KIND_V1_EVAL_CANDIDATE: TraceInvestigationActionKindV1
TRACE_INVESTIGATION_ACTION_KIND_V1_RELEASE_EVIDENCE: TraceInvestigationActionKindV1
TRACE_INVESTIGATION_ACTION_KIND_V1_ALERT: TraceInvestigationActionKindV1
TRACE_INVESTIGATION_ACTION_STATUS_V1_UNSPECIFIED: TraceInvestigationActionStatusV1
TRACE_INVESTIGATION_ACTION_STATUS_V1_CREATED: TraceInvestigationActionStatusV1
TRACE_INVESTIGATION_ACTION_STATUS_V1_REPLAYED: TraceInvestigationActionStatusV1
TRACE_INVESTIGATION_ACTION_STATUS_V1_PENDING: TraceInvestigationActionStatusV1
TRACE_INVESTIGATION_ACTION_STATUS_V1_FAILED: TraceInvestigationActionStatusV1
TRACE_INVESTIGATION_ACTION_RESOURCE_KIND_V1_UNSPECIFIED: TraceInvestigationActionResourceKindV1
TRACE_INVESTIGATION_ACTION_RESOURCE_KIND_V1_ANNOTATION_TASK: TraceInvestigationActionResourceKindV1
TRACE_INVESTIGATION_ACTION_RESOURCE_KIND_V1_DATASET_ITEM: TraceInvestigationActionResourceKindV1
TRACE_INVESTIGATION_ACTION_RESOURCE_KIND_V1_DATASET_COLLECTION: TraceInvestigationActionResourceKindV1
TRACE_INVESTIGATION_ACTION_RESOURCE_KIND_V1_DATASET_VERSION: TraceInvestigationActionResourceKindV1
TRACE_INVESTIGATION_ACTION_RESOURCE_KIND_V1_EVAL_JOB: TraceInvestigationActionResourceKindV1
TRACE_INVESTIGATION_ACTION_RESOURCE_KIND_V1_RELEASE_EVIDENCE: TraceInvestigationActionResourceKindV1
TRACE_INVESTIGATION_ACTION_RESOURCE_KIND_V1_ALERT: TraceInvestigationActionResourceKindV1
TRACE_INVESTIGATION_ACTION_RESOURCE_KIND_V1_EXPERIMENT_RUN: TraceInvestigationActionResourceKindV1
TRACE_INVESTIGATION_ACTION_RESOURCE_KIND_V1_MONITOR: TraceInvestigationActionResourceKindV1
TRACE_INVESTIGATION_DATASET_INCLUDE_V1_UNSPECIFIED: TraceInvestigationDatasetIncludeV1
TRACE_INVESTIGATION_DATASET_INCLUDE_V1_MESSAGES: TraceInvestigationDatasetIncludeV1
TRACE_INVESTIGATION_DATASET_INCLUDE_V1_SPANS: TraceInvestigationDatasetIncludeV1
TRACE_INVESTIGATION_DATASET_INCLUDE_V1_SCORES: TraceInvestigationDatasetIncludeV1
TRACE_INVESTIGATION_DATASET_INCLUDE_V1_FEEDBACK: TraceInvestigationDatasetIncludeV1
TRACE_INVESTIGATION_DATASET_INCLUDE_V1_OUTCOMES: TraceInvestigationDatasetIncludeV1
TRACE_INVESTIGATION_DATASET_INCLUDE_V1_RAW_PAYLOADS: TraceInvestigationDatasetIncludeV1
TRACE_INVESTIGATION_ACTION_DESTINATION_V1_UNSPECIFIED: TraceInvestigationActionDestinationV1
TRACE_INVESTIGATION_ACTION_DESTINATION_V1_REVIEW_QUEUE: TraceInvestigationActionDestinationV1
TRACE_INVESTIGATION_ACTION_DESTINATION_V1_RELEASE_GOVERNANCE: TraceInvestigationActionDestinationV1
TRACE_INVESTIGATION_ACTION_DESTINATION_V1_WEBHOOK: TraceInvestigationActionDestinationV1
TRACE_INVESTIGATION_ACTION_DESTINATION_V1_ALERTS: TraceInvestigationActionDestinationV1
TRACE_INVESTIGATION_ALERT_STATE_V1_UNSPECIFIED: TraceInvestigationAlertStateV1
TRACE_INVESTIGATION_ALERT_STATE_V1_ACTIVE: TraceInvestigationAlertStateV1
TRACE_INVESTIGATION_ALERT_STATE_V1_PAUSED: TraceInvestigationAlertStateV1
TRACE_INVESTIGATION_ALERT_STATE_V1_DISABLED: TraceInvestigationAlertStateV1
TRACE_INVESTIGATION_FILTER_OP_V1_UNSPECIFIED: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_EQ: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_NE: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_GT: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_GE: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_LT: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_LE: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_LIKE: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_IN: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_NOT_IN: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_EXISTS: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_NOT_EXISTS: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_CONTAINS: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_NOT_CONTAINS: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_REGEX: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_NOT_REGEX: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_IS_NULL: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_IS_NOT_NULL: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_STARTS_WITH: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_NOT_STARTS_WITH: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_ENDS_WITH: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_NOT_ENDS_WITH: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_IEQ: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_INE: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_IS_EMPTY: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_IS_NOT_EMPTY: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_BETWEEN: TraceInvestigationFilterOpV1
TRACE_INVESTIGATION_FILTER_OP_V1_NOT_BETWEEN: TraceInvestigationFilterOpV1

class CorrelationContextV1(_message.Message):
    __slots__ = ("trace_id", "span_id", "observation_id", "conversation_id", "user_id", "account_id", "customer_id", "feature_id", "deployment_id", "prompt_version", "model_version", "tool_version", "release_id", "source_turn_id")
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    FEATURE_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
    TOOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TURN_ID_FIELD_NUMBER: _ClassVar[int]
    trace_id: str
    span_id: str
    observation_id: str
    conversation_id: str
    user_id: str
    account_id: str
    customer_id: str
    feature_id: str
    deployment_id: str
    prompt_version: str
    model_version: str
    tool_version: str
    release_id: str
    source_turn_id: str
    def __init__(self, trace_id: _Optional[str] = ..., span_id: _Optional[str] = ..., observation_id: _Optional[str] = ..., conversation_id: _Optional[str] = ..., user_id: _Optional[str] = ..., account_id: _Optional[str] = ..., customer_id: _Optional[str] = ..., feature_id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., prompt_version: _Optional[str] = ..., model_version: _Optional[str] = ..., tool_version: _Optional[str] = ..., release_id: _Optional[str] = ..., source_turn_id: _Optional[str] = ...) -> None: ...

class ProviderModelRefV1(_message.Message):
    __slots__ = ("openai", "anthropic", "google", "xai", "moonshot", "deepseek", "openrouter")
    OPENAI_FIELD_NUMBER: _ClassVar[int]
    ANTHROPIC_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_FIELD_NUMBER: _ClassVar[int]
    XAI_FIELD_NUMBER: _ClassVar[int]
    MOONSHOT_FIELD_NUMBER: _ClassVar[int]
    DEEPSEEK_FIELD_NUMBER: _ClassVar[int]
    OPENROUTER_FIELD_NUMBER: _ClassVar[int]
    openai: OpenAiTextModelV1
    anthropic: AnthropicTextModelV1
    google: GoogleTextModelV1
    xai: XaiTextModelV1
    moonshot: MoonshotTextModelV1
    deepseek: DeepSeekTextModelV1
    openrouter: OpenRouterTextModelV1
    def __init__(self, openai: _Optional[_Union[OpenAiTextModelV1, str]] = ..., anthropic: _Optional[_Union[AnthropicTextModelV1, str]] = ..., google: _Optional[_Union[GoogleTextModelV1, str]] = ..., xai: _Optional[_Union[XaiTextModelV1, str]] = ..., moonshot: _Optional[_Union[MoonshotTextModelV1, str]] = ..., deepseek: _Optional[_Union[DeepSeekTextModelV1, str]] = ..., openrouter: _Optional[_Union[OpenRouterTextModelV1, str]] = ...) -> None: ...

class AnnotationAuditEntryV1(_message.Message):
    __slots__ = ("state", "actor_user_id", "occurred_at", "note")
    STATE_FIELD_NUMBER: _ClassVar[int]
    ACTOR_USER_ID_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    state: AnnotationTaskStateV1
    actor_user_id: str
    occurred_at: _timestamp_pb2.Timestamp
    note: str
    def __init__(self, state: _Optional[_Union[AnnotationTaskStateV1, str]] = ..., actor_user_id: _Optional[str] = ..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., note: _Optional[str] = ...) -> None: ...

class AnnotationPairwiseRefsV1(_message.Message):
    __slots__ = ("baseline_experiment_run_id", "baseline_experiment_run_item_id", "candidate_experiment_run_id", "candidate_experiment_run_item_id", "baseline_output", "candidate_output", "baseline_label", "candidate_label")
    BASELINE_EXPERIMENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    BASELINE_EXPERIMENT_RUN_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_EXPERIMENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_EXPERIMENT_RUN_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    BASELINE_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    BASELINE_LABEL_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_LABEL_FIELD_NUMBER: _ClassVar[int]
    baseline_experiment_run_id: str
    baseline_experiment_run_item_id: str
    candidate_experiment_run_id: str
    candidate_experiment_run_item_id: str
    baseline_output: _struct_pb2.Struct
    candidate_output: _struct_pb2.Struct
    baseline_label: str
    candidate_label: str
    def __init__(self, baseline_experiment_run_id: _Optional[str] = ..., baseline_experiment_run_item_id: _Optional[str] = ..., candidate_experiment_run_id: _Optional[str] = ..., candidate_experiment_run_item_id: _Optional[str] = ..., baseline_output: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., candidate_output: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., baseline_label: _Optional[str] = ..., candidate_label: _Optional[str] = ...) -> None: ...

class AnnotationQueueV1(_message.Message):
    __slots__ = ("queue_id", "queue_key", "name", "description", "routing_reason", "routing_config", "is_system_managed", "created_at", "updated_at")
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    QUEUE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ROUTING_REASON_FIELD_NUMBER: _ClassVar[int]
    ROUTING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IS_SYSTEM_MANAGED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    queue_id: str
    queue_key: str
    name: str
    description: str
    routing_reason: AnnotationRoutingReasonV1
    routing_config: _struct_pb2.Struct
    is_system_managed: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, queue_id: _Optional[str] = ..., queue_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., routing_reason: _Optional[_Union[AnnotationRoutingReasonV1, str]] = ..., routing_config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., is_system_managed: _Optional[bool] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AnnotationTaskV1(_message.Message):
    __slots__ = ("task_id", "queue_id", "queue_key", "queue_name", "routing_reason", "state", "task_key", "title", "summary", "source_feedback_event_id", "source_outcome_event_id", "source_score_id", "correlation", "evidence", "correction_payload", "resolution_notes", "claimed_by_user_id", "claimed_at", "completed_by_user_id", "completed_at", "approved_by_user_id", "approved_at", "rejected_by_user_id", "rejected_at", "audit_entries", "created_at", "updated_at", "task_mode", "priority_tier", "assigned_user_id", "due_at", "experiment_run_id", "experiment_run_item_id", "pairwise_refs", "pairwise_winner")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    QUEUE_KEY_FIELD_NUMBER: _ClassVar[int]
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    ROUTING_REASON_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TASK_KEY_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FEEDBACK_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_OUTCOME_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SCORE_ID_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    CORRECTION_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_NOTES_FIELD_NUMBER: _ClassVar[int]
    CLAIMED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CLAIMED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    APPROVED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    APPROVED_AT_FIELD_NUMBER: _ClassVar[int]
    REJECTED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    REJECTED_AT_FIELD_NUMBER: _ClassVar[int]
    AUDIT_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    TASK_MODE_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_TIER_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_USER_ID_FIELD_NUMBER: _ClassVar[int]
    DUE_AT_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_RUN_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_REFS_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_WINNER_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    queue_id: str
    queue_key: str
    queue_name: str
    routing_reason: AnnotationRoutingReasonV1
    state: AnnotationTaskStateV1
    task_key: str
    title: str
    summary: str
    source_feedback_event_id: str
    source_outcome_event_id: str
    source_score_id: str
    correlation: CorrelationContextV1
    evidence: _struct_pb2.Struct
    correction_payload: _struct_pb2.Struct
    resolution_notes: str
    claimed_by_user_id: str
    claimed_at: _timestamp_pb2.Timestamp
    completed_by_user_id: str
    completed_at: _timestamp_pb2.Timestamp
    approved_by_user_id: str
    approved_at: _timestamp_pb2.Timestamp
    rejected_by_user_id: str
    rejected_at: _timestamp_pb2.Timestamp
    audit_entries: _containers.RepeatedCompositeFieldContainer[AnnotationAuditEntryV1]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    task_mode: AnnotationTaskModeV1
    priority_tier: RoutingPriorityTierV1
    assigned_user_id: str
    due_at: _timestamp_pb2.Timestamp
    experiment_run_id: str
    experiment_run_item_id: str
    pairwise_refs: AnnotationPairwiseRefsV1
    pairwise_winner: AnnotationPairwiseWinnerV1
    def __init__(self, task_id: _Optional[str] = ..., queue_id: _Optional[str] = ..., queue_key: _Optional[str] = ..., queue_name: _Optional[str] = ..., routing_reason: _Optional[_Union[AnnotationRoutingReasonV1, str]] = ..., state: _Optional[_Union[AnnotationTaskStateV1, str]] = ..., task_key: _Optional[str] = ..., title: _Optional[str] = ..., summary: _Optional[str] = ..., source_feedback_event_id: _Optional[str] = ..., source_outcome_event_id: _Optional[str] = ..., source_score_id: _Optional[str] = ..., correlation: _Optional[_Union[CorrelationContextV1, _Mapping]] = ..., evidence: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., correction_payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., resolution_notes: _Optional[str] = ..., claimed_by_user_id: _Optional[str] = ..., claimed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., completed_by_user_id: _Optional[str] = ..., completed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., approved_by_user_id: _Optional[str] = ..., approved_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., rejected_by_user_id: _Optional[str] = ..., rejected_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., audit_entries: _Optional[_Iterable[_Union[AnnotationAuditEntryV1, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., task_mode: _Optional[_Union[AnnotationTaskModeV1, str]] = ..., priority_tier: _Optional[_Union[RoutingPriorityTierV1, str]] = ..., assigned_user_id: _Optional[str] = ..., due_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., experiment_run_id: _Optional[str] = ..., experiment_run_item_id: _Optional[str] = ..., pairwise_refs: _Optional[_Union[AnnotationPairwiseRefsV1, _Mapping]] = ..., pairwise_winner: _Optional[_Union[AnnotationPairwiseWinnerV1, str]] = ...) -> None: ...

class RoutingPolicyV1(_message.Message):
    __slots__ = ("routing_policy_id", "policy_key", "name", "description", "is_default", "enabled", "version", "rules_json", "created_by_user_id", "created_at", "updated_at")
    ROUTING_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    RULES_JSON_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    routing_policy_id: str
    policy_key: str
    name: str
    description: str
    is_default: bool
    enabled: bool
    version: int
    rules_json: _struct_pb2.Struct
    created_by_user_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, routing_policy_id: _Optional[str] = ..., policy_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_default: _Optional[bool] = ..., enabled: _Optional[bool] = ..., version: _Optional[int] = ..., rules_json: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., created_by_user_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CustomerPriorityPolicyV1(_message.Message):
    __slots__ = ("customer_priority_policy_id", "policy_key", "name", "description", "is_default", "enabled", "version", "cohorts_json", "created_by_user_id", "created_at", "updated_at")
    CUSTOMER_PRIORITY_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    COHORTS_JSON_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    customer_priority_policy_id: str
    policy_key: str
    name: str
    description: str
    is_default: bool
    enabled: bool
    version: int
    cohorts_json: _struct_pb2.Struct
    created_by_user_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, customer_priority_policy_id: _Optional[str] = ..., policy_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_default: _Optional[bool] = ..., enabled: _Optional[bool] = ..., version: _Optional[int] = ..., cohorts_json: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., created_by_user_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RoutingPolicyComparisonV1(_message.Message):
    __slots__ = ("baseline_policy", "comparison_policy", "version_delta", "same_policy_key", "name_changed", "description_changed", "enabled_changed", "default_changed", "added_rule_keys", "removed_rule_keys", "changed_rule_keys")
    BASELINE_POLICY_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_POLICY_FIELD_NUMBER: _ClassVar[int]
    VERSION_DELTA_FIELD_NUMBER: _ClassVar[int]
    SAME_POLICY_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_CHANGED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_CHANGED_FIELD_NUMBER: _ClassVar[int]
    ENABLED_CHANGED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CHANGED_FIELD_NUMBER: _ClassVar[int]
    ADDED_RULE_KEYS_FIELD_NUMBER: _ClassVar[int]
    REMOVED_RULE_KEYS_FIELD_NUMBER: _ClassVar[int]
    CHANGED_RULE_KEYS_FIELD_NUMBER: _ClassVar[int]
    baseline_policy: RoutingPolicyV1
    comparison_policy: RoutingPolicyV1
    version_delta: int
    same_policy_key: bool
    name_changed: bool
    description_changed: bool
    enabled_changed: bool
    default_changed: bool
    added_rule_keys: _containers.RepeatedScalarFieldContainer[str]
    removed_rule_keys: _containers.RepeatedScalarFieldContainer[str]
    changed_rule_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, baseline_policy: _Optional[_Union[RoutingPolicyV1, _Mapping]] = ..., comparison_policy: _Optional[_Union[RoutingPolicyV1, _Mapping]] = ..., version_delta: _Optional[int] = ..., same_policy_key: _Optional[bool] = ..., name_changed: _Optional[bool] = ..., description_changed: _Optional[bool] = ..., enabled_changed: _Optional[bool] = ..., default_changed: _Optional[bool] = ..., added_rule_keys: _Optional[_Iterable[str]] = ..., removed_rule_keys: _Optional[_Iterable[str]] = ..., changed_rule_keys: _Optional[_Iterable[str]] = ...) -> None: ...

class CustomerPriorityPolicyComparisonV1(_message.Message):
    __slots__ = ("baseline_policy", "comparison_policy", "version_delta", "same_policy_key", "name_changed", "description_changed", "enabled_changed", "default_changed", "added_cohort_keys", "removed_cohort_keys", "changed_cohort_keys")
    BASELINE_POLICY_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_POLICY_FIELD_NUMBER: _ClassVar[int]
    VERSION_DELTA_FIELD_NUMBER: _ClassVar[int]
    SAME_POLICY_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_CHANGED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_CHANGED_FIELD_NUMBER: _ClassVar[int]
    ENABLED_CHANGED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CHANGED_FIELD_NUMBER: _ClassVar[int]
    ADDED_COHORT_KEYS_FIELD_NUMBER: _ClassVar[int]
    REMOVED_COHORT_KEYS_FIELD_NUMBER: _ClassVar[int]
    CHANGED_COHORT_KEYS_FIELD_NUMBER: _ClassVar[int]
    baseline_policy: CustomerPriorityPolicyV1
    comparison_policy: CustomerPriorityPolicyV1
    version_delta: int
    same_policy_key: bool
    name_changed: bool
    description_changed: bool
    enabled_changed: bool
    default_changed: bool
    added_cohort_keys: _containers.RepeatedScalarFieldContainer[str]
    removed_cohort_keys: _containers.RepeatedScalarFieldContainer[str]
    changed_cohort_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, baseline_policy: _Optional[_Union[CustomerPriorityPolicyV1, _Mapping]] = ..., comparison_policy: _Optional[_Union[CustomerPriorityPolicyV1, _Mapping]] = ..., version_delta: _Optional[int] = ..., same_policy_key: _Optional[bool] = ..., name_changed: _Optional[bool] = ..., description_changed: _Optional[bool] = ..., enabled_changed: _Optional[bool] = ..., default_changed: _Optional[bool] = ..., added_cohort_keys: _Optional[_Iterable[str]] = ..., removed_cohort_keys: _Optional[_Iterable[str]] = ..., changed_cohort_keys: _Optional[_Iterable[str]] = ...) -> None: ...

class RoutingSignalV1(_message.Message):
    __slots__ = ("routing_signal_id", "signal_type", "routing_reason_candidates", "priority_tier", "state", "routing_policy_id", "customer_priority_policy_id", "source_score_id", "source_feedback_event_id", "source_outcome_event_id", "source_release_gate_evaluation_id", "correlation", "evidence", "dispatch_key", "task_materialization_count", "attempts", "next_attempt_at", "worker_id", "last_error", "created_by_user_id", "created_at", "updated_at")
    ROUTING_SIGNAL_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROUTING_REASON_CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_TIER_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ROUTING_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_PRIORITY_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SCORE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FEEDBACK_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_OUTCOME_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_RELEASE_GATE_EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_KEY_FIELD_NUMBER: _ClassVar[int]
    TASK_MATERIALIZATION_COUNT_FIELD_NUMBER: _ClassVar[int]
    ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_ATTEMPT_AT_FIELD_NUMBER: _ClassVar[int]
    WORKER_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    routing_signal_id: str
    signal_type: RoutingSignalTypeV1
    routing_reason_candidates: _containers.RepeatedScalarFieldContainer[AnnotationRoutingReasonV1]
    priority_tier: RoutingPriorityTierV1
    state: RoutingSignalStateV1
    routing_policy_id: str
    customer_priority_policy_id: str
    source_score_id: str
    source_feedback_event_id: str
    source_outcome_event_id: str
    source_release_gate_evaluation_id: str
    correlation: CorrelationContextV1
    evidence: _struct_pb2.Struct
    dispatch_key: str
    task_materialization_count: int
    attempts: int
    next_attempt_at: _timestamp_pb2.Timestamp
    worker_id: str
    last_error: str
    created_by_user_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, routing_signal_id: _Optional[str] = ..., signal_type: _Optional[_Union[RoutingSignalTypeV1, str]] = ..., routing_reason_candidates: _Optional[_Iterable[_Union[AnnotationRoutingReasonV1, str]]] = ..., priority_tier: _Optional[_Union[RoutingPriorityTierV1, str]] = ..., state: _Optional[_Union[RoutingSignalStateV1, str]] = ..., routing_policy_id: _Optional[str] = ..., customer_priority_policy_id: _Optional[str] = ..., source_score_id: _Optional[str] = ..., source_feedback_event_id: _Optional[str] = ..., source_outcome_event_id: _Optional[str] = ..., source_release_gate_evaluation_id: _Optional[str] = ..., correlation: _Optional[_Union[CorrelationContextV1, _Mapping]] = ..., evidence: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., dispatch_key: _Optional[str] = ..., task_materialization_count: _Optional[int] = ..., attempts: _Optional[int] = ..., next_attempt_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., worker_id: _Optional[str] = ..., last_error: _Optional[str] = ..., created_by_user_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RoutingAuditV1(_message.Message):
    __slots__ = ("routing_audit_id", "routing_signal_id", "annotation_task_id", "action", "routing_reason", "queue_id", "queue_key", "priority_tier", "worker_id", "note", "details", "occurred_at")
    ROUTING_AUDIT_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTING_SIGNAL_ID_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ROUTING_REASON_FIELD_NUMBER: _ClassVar[int]
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    QUEUE_KEY_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_TIER_FIELD_NUMBER: _ClassVar[int]
    WORKER_ID_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    routing_audit_id: str
    routing_signal_id: str
    annotation_task_id: str
    action: RoutingAuditActionV1
    routing_reason: AnnotationRoutingReasonV1
    queue_id: str
    queue_key: str
    priority_tier: RoutingPriorityTierV1
    worker_id: str
    note: str
    details: _struct_pb2.Struct
    occurred_at: _timestamp_pb2.Timestamp
    def __init__(self, routing_audit_id: _Optional[str] = ..., routing_signal_id: _Optional[str] = ..., annotation_task_id: _Optional[str] = ..., action: _Optional[_Union[RoutingAuditActionV1, str]] = ..., routing_reason: _Optional[_Union[AnnotationRoutingReasonV1, str]] = ..., queue_id: _Optional[str] = ..., queue_key: _Optional[str] = ..., priority_tier: _Optional[_Union[RoutingPriorityTierV1, str]] = ..., worker_id: _Optional[str] = ..., note: _Optional[str] = ..., details: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AgenticDispatchOutboxEntryV1(_message.Message):
    __slots__ = ("dispatch_entry_id", "dispatch_kind", "priority_tier", "dispatch_key", "payload", "state", "attempts", "next_attempt_at", "last_error", "created_at", "updated_at")
    DISPATCH_ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_KIND_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_TIER_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_KEY_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_ATTEMPT_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    dispatch_entry_id: str
    dispatch_kind: AgenticDispatchKindV1
    priority_tier: str
    dispatch_key: str
    payload: _struct_pb2.Struct
    state: AgenticDispatchStateV1
    attempts: int
    next_attempt_at: _timestamp_pb2.Timestamp
    last_error: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, dispatch_entry_id: _Optional[str] = ..., dispatch_kind: _Optional[_Union[AgenticDispatchKindV1, str]] = ..., priority_tier: _Optional[str] = ..., dispatch_key: _Optional[str] = ..., payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., state: _Optional[_Union[AgenticDispatchStateV1, str]] = ..., attempts: _Optional[int] = ..., next_attempt_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_error: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ProviderExecutionConfigV1(_message.Message):
    __slots__ = ("provider_mode", "provider_name", "provider_model_id", "provider_endpoint_ref", "provider_key_ref", "provider_request_params", "provider_cost_mode", "provider_request_settings", "provider_model")
    PROVIDER_MODE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ENDPOINT_REF_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_KEY_REF_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_COST_MODE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_REQUEST_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_MODEL_FIELD_NUMBER: _ClassVar[int]
    provider_mode: ProviderExecutionModeV1
    provider_name: ProviderNameV1
    provider_model_id: str
    provider_endpoint_ref: str
    provider_key_ref: str
    provider_request_params: _struct_pb2.Struct
    provider_cost_mode: ProviderCostModeV1
    provider_request_settings: ProviderRequestSettingsV1
    provider_model: ProviderModelRefV1
    def __init__(self, provider_mode: _Optional[_Union[ProviderExecutionModeV1, str]] = ..., provider_name: _Optional[_Union[ProviderNameV1, str]] = ..., provider_model_id: _Optional[str] = ..., provider_endpoint_ref: _Optional[str] = ..., provider_key_ref: _Optional[str] = ..., provider_request_params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., provider_cost_mode: _Optional[_Union[ProviderCostModeV1, str]] = ..., provider_request_settings: _Optional[_Union[ProviderRequestSettingsV1, _Mapping]] = ..., provider_model: _Optional[_Union[ProviderModelRefV1, _Mapping]] = ...) -> None: ...

class ProviderRequestSettingsV1(_message.Message):
    __slots__ = ("max_output_tokens", "fixed_cost_usd", "input_token_rate_usd", "output_token_rate_usd", "budget_limit_usd", "anthropic_version", "reasoning_effort", "reasoning_budget_tokens", "temperature", "top_p", "frequency_penalty", "presence_penalty", "stop_sequences", "tool_choice", "reasoning_effort_mode", "verbosity", "max_tool_calls", "parallel_tool_calls", "truncation", "prompt_cache_key", "prompt_cache_retention", "safety_identifier", "service_tier", "top_logprobs", "top_k", "anthropic_metadata_user_id", "provider_metadata", "tool_choice_name")
    class ProviderMetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MAX_OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    FIXED_COST_USD_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKEN_RATE_USD_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKEN_RATE_USD_FIELD_NUMBER: _ClassVar[int]
    BUDGET_LIMIT_USD_FIELD_NUMBER: _ClassVar[int]
    ANTHROPIC_VERSION_FIELD_NUMBER: _ClassVar[int]
    REASONING_EFFORT_FIELD_NUMBER: _ClassVar[int]
    REASONING_BUDGET_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TOP_P_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_PENALTY_FIELD_NUMBER: _ClassVar[int]
    PRESENCE_PENALTY_FIELD_NUMBER: _ClassVar[int]
    STOP_SEQUENCES_FIELD_NUMBER: _ClassVar[int]
    TOOL_CHOICE_FIELD_NUMBER: _ClassVar[int]
    REASONING_EFFORT_MODE_FIELD_NUMBER: _ClassVar[int]
    VERBOSITY_FIELD_NUMBER: _ClassVar[int]
    MAX_TOOL_CALLS_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_TOOL_CALLS_FIELD_NUMBER: _ClassVar[int]
    TRUNCATION_FIELD_NUMBER: _ClassVar[int]
    PROMPT_CACHE_KEY_FIELD_NUMBER: _ClassVar[int]
    PROMPT_CACHE_RETENTION_FIELD_NUMBER: _ClassVar[int]
    SAFETY_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TIER_FIELD_NUMBER: _ClassVar[int]
    TOP_LOGPROBS_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    ANTHROPIC_METADATA_USER_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_METADATA_FIELD_NUMBER: _ClassVar[int]
    TOOL_CHOICE_NAME_FIELD_NUMBER: _ClassVar[int]
    max_output_tokens: int
    fixed_cost_usd: float
    input_token_rate_usd: float
    output_token_rate_usd: float
    budget_limit_usd: float
    anthropic_version: str
    reasoning_effort: str
    reasoning_budget_tokens: int
    temperature: float
    top_p: float
    frequency_penalty: float
    presence_penalty: float
    stop_sequences: _containers.RepeatedScalarFieldContainer[str]
    tool_choice: ProviderToolChoiceV1
    reasoning_effort_mode: ProviderReasoningEffortV1
    verbosity: ProviderVerbosityV1
    max_tool_calls: int
    parallel_tool_calls: bool
    truncation: ProviderTruncationV1
    prompt_cache_key: str
    prompt_cache_retention: ProviderPromptCacheRetentionV1
    safety_identifier: str
    service_tier: ProviderServiceTierV1
    top_logprobs: int
    top_k: int
    anthropic_metadata_user_id: str
    provider_metadata: _containers.ScalarMap[str, str]
    tool_choice_name: str
    def __init__(self, max_output_tokens: _Optional[int] = ..., fixed_cost_usd: _Optional[float] = ..., input_token_rate_usd: _Optional[float] = ..., output_token_rate_usd: _Optional[float] = ..., budget_limit_usd: _Optional[float] = ..., anthropic_version: _Optional[str] = ..., reasoning_effort: _Optional[str] = ..., reasoning_budget_tokens: _Optional[int] = ..., temperature: _Optional[float] = ..., top_p: _Optional[float] = ..., frequency_penalty: _Optional[float] = ..., presence_penalty: _Optional[float] = ..., stop_sequences: _Optional[_Iterable[str]] = ..., tool_choice: _Optional[_Union[ProviderToolChoiceV1, str]] = ..., reasoning_effort_mode: _Optional[_Union[ProviderReasoningEffortV1, str]] = ..., verbosity: _Optional[_Union[ProviderVerbosityV1, str]] = ..., max_tool_calls: _Optional[int] = ..., parallel_tool_calls: _Optional[bool] = ..., truncation: _Optional[_Union[ProviderTruncationV1, str]] = ..., prompt_cache_key: _Optional[str] = ..., prompt_cache_retention: _Optional[_Union[ProviderPromptCacheRetentionV1, str]] = ..., safety_identifier: _Optional[str] = ..., service_tier: _Optional[_Union[ProviderServiceTierV1, str]] = ..., top_logprobs: _Optional[int] = ..., top_k: _Optional[int] = ..., anthropic_metadata_user_id: _Optional[str] = ..., provider_metadata: _Optional[_Mapping[str, str]] = ..., tool_choice_name: _Optional[str] = ...) -> None: ...

class ProviderCredentialV1(_message.Message):
    __slots__ = ("provider_credential_id", "provider_name", "credential_key", "auth_ref", "key_ref", "is_default", "created_by_user_id", "created_at", "updated_at")
    PROVIDER_CREDENTIAL_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_KEY_FIELD_NUMBER: _ClassVar[int]
    AUTH_REF_FIELD_NUMBER: _ClassVar[int]
    KEY_REF_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    provider_credential_id: str
    provider_name: ProviderNameV1
    credential_key: str
    auth_ref: str
    key_ref: str
    is_default: bool
    created_by_user_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, provider_credential_id: _Optional[str] = ..., provider_name: _Optional[_Union[ProviderNameV1, str]] = ..., credential_key: _Optional[str] = ..., auth_ref: _Optional[str] = ..., key_ref: _Optional[str] = ..., is_default: _Optional[bool] = ..., created_by_user_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ProviderCredentialSecretV1(_message.Message):
    __slots__ = ("provider_credential_secret_id", "provider_credential_id", "credential_key", "secret_ref", "version_number", "is_active", "created_by_user_id", "created_at", "revoked_by_user_id", "revoked_at", "revoke_reason")
    PROVIDER_CREDENTIAL_SECRET_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_CREDENTIAL_ID_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_KEY_FIELD_NUMBER: _ClassVar[int]
    SECRET_REF_FIELD_NUMBER: _ClassVar[int]
    VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    REVOKED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    REVOKED_AT_FIELD_NUMBER: _ClassVar[int]
    REVOKE_REASON_FIELD_NUMBER: _ClassVar[int]
    provider_credential_secret_id: str
    provider_credential_id: str
    credential_key: str
    secret_ref: str
    version_number: int
    is_active: bool
    created_by_user_id: str
    created_at: _timestamp_pb2.Timestamp
    revoked_by_user_id: str
    revoked_at: _timestamp_pb2.Timestamp
    revoke_reason: str
    def __init__(self, provider_credential_secret_id: _Optional[str] = ..., provider_credential_id: _Optional[str] = ..., credential_key: _Optional[str] = ..., secret_ref: _Optional[str] = ..., version_number: _Optional[int] = ..., is_active: _Optional[bool] = ..., created_by_user_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., revoked_by_user_id: _Optional[str] = ..., revoked_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., revoke_reason: _Optional[str] = ...) -> None: ...

class PromptTemplateV1(_message.Message):
    __slots__ = ("prompt_template_id", "template_key", "name", "description", "labels", "is_archived", "archived_at", "archived_by_user_id", "created_by_user_id", "created_at", "updated_at", "latest_prompt_version_id", "latest_version_number", "latest_version_label", "latest_version_ref", "latest_environments", "latest_prompt_text_preview", "latest_has_system_prompt", "latest_prompt_updated_at")
    PROMPT_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    IS_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_AT_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    LATEST_PROMPT_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    LATEST_VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LATEST_VERSION_LABEL_FIELD_NUMBER: _ClassVar[int]
    LATEST_VERSION_REF_FIELD_NUMBER: _ClassVar[int]
    LATEST_ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    LATEST_PROMPT_TEXT_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    LATEST_HAS_SYSTEM_PROMPT_FIELD_NUMBER: _ClassVar[int]
    LATEST_PROMPT_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    prompt_template_id: str
    template_key: str
    name: str
    description: str
    labels: _struct_pb2.Struct
    is_archived: bool
    archived_at: _timestamp_pb2.Timestamp
    archived_by_user_id: str
    created_by_user_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    latest_prompt_version_id: str
    latest_version_number: int
    latest_version_label: str
    latest_version_ref: str
    latest_environments: _containers.RepeatedScalarFieldContainer[PromptEnvironmentV1]
    latest_prompt_text_preview: str
    latest_has_system_prompt: bool
    latest_prompt_updated_at: _timestamp_pb2.Timestamp
    def __init__(self, prompt_template_id: _Optional[str] = ..., template_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., labels: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., is_archived: _Optional[bool] = ..., archived_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., archived_by_user_id: _Optional[str] = ..., created_by_user_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., latest_prompt_version_id: _Optional[str] = ..., latest_version_number: _Optional[int] = ..., latest_version_label: _Optional[str] = ..., latest_version_ref: _Optional[str] = ..., latest_environments: _Optional[_Iterable[_Union[PromptEnvironmentV1, str]]] = ..., latest_prompt_text_preview: _Optional[str] = ..., latest_has_system_prompt: _Optional[bool] = ..., latest_prompt_updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PromptVersionV1(_message.Message):
    __slots__ = ("prompt_version_id", "prompt_template_id", "version_number", "version_label", "environments", "version_ref", "prompt_text", "system_prompt", "metadata", "is_archived", "archived_at", "archived_by_user_id", "created_by_user_id", "created_at", "updated_at")
    PROMPT_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    VERSION_LABEL_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    VERSION_REF_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TEXT_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_PROMPT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    IS_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_AT_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    prompt_version_id: str
    prompt_template_id: str
    version_number: int
    version_label: str
    environments: _containers.RepeatedScalarFieldContainer[PromptEnvironmentV1]
    version_ref: str
    prompt_text: str
    system_prompt: str
    metadata: _struct_pb2.Struct
    is_archived: bool
    archived_at: _timestamp_pb2.Timestamp
    archived_by_user_id: str
    created_by_user_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, prompt_version_id: _Optional[str] = ..., prompt_template_id: _Optional[str] = ..., version_number: _Optional[int] = ..., version_label: _Optional[str] = ..., environments: _Optional[_Iterable[_Union[PromptEnvironmentV1, str]]] = ..., version_ref: _Optional[str] = ..., prompt_text: _Optional[str] = ..., system_prompt: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., is_archived: _Optional[bool] = ..., archived_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., archived_by_user_id: _Optional[str] = ..., created_by_user_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EvaluatorTemplateV1(_message.Message):
    __slots__ = ("template_id", "template_key", "name", "evaluator_kind", "execution_mode", "config", "created_by_user_id", "created_at", "updated_at", "provider_execution", "settings", "is_archived", "archived_at", "archived_by_user_id", "prompt_template_id", "prompt_version_id", "description", "metadata")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_KIND_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_MODE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    IS_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_AT_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    template_key: str
    name: str
    evaluator_kind: str
    execution_mode: EvaluatorExecutionModeV1
    config: _struct_pb2.Struct
    created_by_user_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    provider_execution: ProviderExecutionConfigV1
    settings: EvaluatorTemplateSettingsV1
    is_archived: bool
    archived_at: _timestamp_pb2.Timestamp
    archived_by_user_id: str
    prompt_template_id: str
    prompt_version_id: str
    description: str
    metadata: _struct_pb2.Struct
    def __init__(self, template_id: _Optional[str] = ..., template_key: _Optional[str] = ..., name: _Optional[str] = ..., evaluator_kind: _Optional[str] = ..., execution_mode: _Optional[_Union[EvaluatorExecutionModeV1, str]] = ..., config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., created_by_user_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., provider_execution: _Optional[_Union[ProviderExecutionConfigV1, _Mapping]] = ..., settings: _Optional[_Union[EvaluatorTemplateSettingsV1, _Mapping]] = ..., is_archived: _Optional[bool] = ..., archived_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., archived_by_user_id: _Optional[str] = ..., prompt_template_id: _Optional[str] = ..., prompt_version_id: _Optional[str] = ..., description: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class EvaluatorRubricSectionV1(_message.Message):
    __slots__ = ("section_key", "title", "instructions", "weight")
    SECTION_KEY_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    section_key: str
    title: str
    instructions: str
    weight: float
    def __init__(self, section_key: _Optional[str] = ..., title: _Optional[str] = ..., instructions: _Optional[str] = ..., weight: _Optional[float] = ...) -> None: ...

class EvaluatorTemplateSettingsV1(_message.Message):
    __slots__ = ("comparison_mode", "subject_path", "expected_path", "instructions", "rubric", "execution_cost_usd", "output_schema_mode", "rubric_sections", "structured_response_schema", "retry_max_attempts", "timeout_seconds", "provider_response_parsing_mode")
    COMPARISON_MODE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_PATH_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_PATH_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    RUBRIC_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_COST_USD_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SCHEMA_MODE_FIELD_NUMBER: _ClassVar[int]
    RUBRIC_SECTIONS_FIELD_NUMBER: _ClassVar[int]
    STRUCTURED_RESPONSE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    RETRY_MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_RESPONSE_PARSING_MODE_FIELD_NUMBER: _ClassVar[int]
    comparison_mode: EvaluatorComparisonModeV1
    subject_path: str
    expected_path: str
    instructions: str
    rubric: str
    execution_cost_usd: float
    output_schema_mode: EvaluatorOutputSchemaModeV1
    rubric_sections: _containers.RepeatedCompositeFieldContainer[EvaluatorRubricSectionV1]
    structured_response_schema: _struct_pb2.Struct
    retry_max_attempts: int
    timeout_seconds: int
    provider_response_parsing_mode: ProviderResponseParsingModeV1
    def __init__(self, comparison_mode: _Optional[_Union[EvaluatorComparisonModeV1, str]] = ..., subject_path: _Optional[str] = ..., expected_path: _Optional[str] = ..., instructions: _Optional[str] = ..., rubric: _Optional[str] = ..., execution_cost_usd: _Optional[float] = ..., output_schema_mode: _Optional[_Union[EvaluatorOutputSchemaModeV1, str]] = ..., rubric_sections: _Optional[_Iterable[_Union[EvaluatorRubricSectionV1, _Mapping]]] = ..., structured_response_schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., retry_max_attempts: _Optional[int] = ..., timeout_seconds: _Optional[int] = ..., provider_response_parsing_mode: _Optional[_Union[ProviderResponseParsingModeV1, str]] = ...) -> None: ...

class ScoreConfigV1(_message.Message):
    __slots__ = ("score_config_id", "config_key", "name", "metric_name", "score_source", "evaluator_template_id", "pass_label", "fail_label", "pass_threshold", "max_attempts", "retry_backoff_seconds", "config", "created_by_user_id", "created_at", "updated_at", "provider_execution", "settings", "is_archived", "archived_at", "archived_by_user_id", "description", "metadata")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    SCORE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PASS_LABEL_FIELD_NUMBER: _ClassVar[int]
    FAIL_LABEL_FIELD_NUMBER: _ClassVar[int]
    PASS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    RETRY_BACKOFF_SECONDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    IS_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_AT_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    config_key: str
    name: str
    metric_name: str
    score_source: ScoreSourceV1
    evaluator_template_id: str
    pass_label: str
    fail_label: str
    pass_threshold: float
    max_attempts: int
    retry_backoff_seconds: int
    config: _struct_pb2.Struct
    created_by_user_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    provider_execution: ProviderExecutionConfigV1
    settings: ScoreConfigSettingsV1
    is_archived: bool
    archived_at: _timestamp_pb2.Timestamp
    archived_by_user_id: str
    description: str
    metadata: _struct_pb2.Struct
    def __init__(self, score_config_id: _Optional[str] = ..., config_key: _Optional[str] = ..., name: _Optional[str] = ..., metric_name: _Optional[str] = ..., score_source: _Optional[_Union[ScoreSourceV1, str]] = ..., evaluator_template_id: _Optional[str] = ..., pass_label: _Optional[str] = ..., fail_label: _Optional[str] = ..., pass_threshold: _Optional[float] = ..., max_attempts: _Optional[int] = ..., retry_backoff_seconds: _Optional[int] = ..., config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., created_by_user_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., provider_execution: _Optional[_Union[ProviderExecutionConfigV1, _Mapping]] = ..., settings: _Optional[_Union[ScoreConfigSettingsV1, _Mapping]] = ..., is_archived: _Optional[bool] = ..., archived_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., archived_by_user_id: _Optional[str] = ..., description: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ExperimentRunScorerTargetV1(_message.Message):
    __slots__ = ("score_config_id", "scorer_suite_id")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    SCORER_SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    scorer_suite_id: str
    def __init__(self, score_config_id: _Optional[str] = ..., scorer_suite_id: _Optional[str] = ...) -> None: ...

class ScorerTargetSelectorV1(_message.Message):
    __slots__ = ("role", "selection_mode", "turn_index", "input_path", "subject_path", "expected_path", "tool_name", "mcp_method_name", "span_filters", "options")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    SELECTION_MODE_FIELD_NUMBER: _ClassVar[int]
    TURN_INDEX_FIELD_NUMBER: _ClassVar[int]
    INPUT_PATH_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_PATH_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_PATH_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    MCP_METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    SPAN_FILTERS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    role: ScorerTargetRoleV1
    selection_mode: ScorerTurnSelectionModeV1
    turn_index: int
    input_path: str
    subject_path: str
    expected_path: str
    tool_name: str
    mcp_method_name: str
    span_filters: _containers.RepeatedCompositeFieldContainer[TraceInvestigationTraceFilterV1]
    options: _struct_pb2.Struct
    def __init__(self, role: _Optional[_Union[ScorerTargetRoleV1, str]] = ..., selection_mode: _Optional[_Union[ScorerTurnSelectionModeV1, str]] = ..., turn_index: _Optional[int] = ..., input_path: _Optional[str] = ..., subject_path: _Optional[str] = ..., expected_path: _Optional[str] = ..., tool_name: _Optional[str] = ..., mcp_method_name: _Optional[str] = ..., span_filters: _Optional[_Iterable[_Union[TraceInvestigationTraceFilterV1, _Mapping]]] = ..., options: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ScorerTargetEvidenceRefV1(_message.Message):
    __slots__ = ("turn_id", "role", "trace_id", "span_id", "session_id", "source_path", "content_class", "tool_name", "mcp_method_name")
    TURN_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_CLASS_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    MCP_METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    turn_id: str
    role: ScorerTargetRoleV1
    trace_id: str
    span_id: str
    session_id: str
    source_path: str
    content_class: str
    tool_name: str
    mcp_method_name: str
    def __init__(self, turn_id: _Optional[str] = ..., role: _Optional[_Union[ScorerTargetRoleV1, str]] = ..., trace_id: _Optional[str] = ..., span_id: _Optional[str] = ..., session_id: _Optional[str] = ..., source_path: _Optional[str] = ..., content_class: _Optional[str] = ..., tool_name: _Optional[str] = ..., mcp_method_name: _Optional[str] = ...) -> None: ...

class AgenticMessageTurnV1(_message.Message):
    __slots__ = ("turn_id", "role", "trace_id", "span_id", "session_id", "content", "source_path", "content_class", "tool_name", "mcp_method_name", "evidence_refs", "metadata")
    TURN_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_CLASS_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    MCP_METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_REFS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    turn_id: str
    role: ScorerTargetRoleV1
    trace_id: str
    span_id: str
    session_id: str
    content: _struct_pb2.Value
    source_path: str
    content_class: str
    tool_name: str
    mcp_method_name: str
    evidence_refs: _containers.RepeatedCompositeFieldContainer[ScorerTargetEvidenceRefV1]
    metadata: _struct_pb2.Struct
    def __init__(self, turn_id: _Optional[str] = ..., role: _Optional[_Union[ScorerTargetRoleV1, str]] = ..., trace_id: _Optional[str] = ..., span_id: _Optional[str] = ..., session_id: _Optional[str] = ..., content: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., source_path: _Optional[str] = ..., content_class: _Optional[str] = ..., tool_name: _Optional[str] = ..., mcp_method_name: _Optional[str] = ..., evidence_refs: _Optional[_Iterable[_Union[ScorerTargetEvidenceRefV1, _Mapping]]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ResolvedScorerTargetV1(_message.Message):
    __slots__ = ("input_payload", "subject_output", "expected_output", "selected_turns", "evidence_refs", "warnings", "selector", "debug_metadata")
    INPUT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    SELECTED_TURNS_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_REFS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    SELECTOR_FIELD_NUMBER: _ClassVar[int]
    DEBUG_METADATA_FIELD_NUMBER: _ClassVar[int]
    input_payload: _struct_pb2.Value
    subject_output: _struct_pb2.Value
    expected_output: _struct_pb2.Value
    selected_turns: _containers.RepeatedCompositeFieldContainer[AgenticMessageTurnV1]
    evidence_refs: _containers.RepeatedCompositeFieldContainer[ScorerTargetEvidenceRefV1]
    warnings: _containers.RepeatedScalarFieldContainer[str]
    selector: ScorerTargetSelectorV1
    debug_metadata: _struct_pb2.Struct
    def __init__(self, input_payload: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., subject_output: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., expected_output: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., selected_turns: _Optional[_Iterable[_Union[AgenticMessageTurnV1, _Mapping]]] = ..., evidence_refs: _Optional[_Iterable[_Union[ScorerTargetEvidenceRefV1, _Mapping]]] = ..., warnings: _Optional[_Iterable[str]] = ..., selector: _Optional[_Union[ScorerTargetSelectorV1, _Mapping]] = ..., debug_metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ScorerSuiteItemDraftV1(_message.Message):
    __slots__ = ("score_config_id", "weight", "required", "enabled", "display_order", "target_selector", "metadata", "reasoning_mode")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_ORDER_FIELD_NUMBER: _ClassVar[int]
    TARGET_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    REASONING_MODE_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    weight: float
    required: bool
    enabled: bool
    display_order: int
    target_selector: ScorerTargetSelectorV1
    metadata: _struct_pb2.Struct
    reasoning_mode: ScorerReasoningModeV1
    def __init__(self, score_config_id: _Optional[str] = ..., weight: _Optional[float] = ..., required: _Optional[bool] = ..., enabled: _Optional[bool] = ..., display_order: _Optional[int] = ..., target_selector: _Optional[_Union[ScorerTargetSelectorV1, _Mapping]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., reasoning_mode: _Optional[_Union[ScorerReasoningModeV1, str]] = ...) -> None: ...

class ScorerSuiteItemV1(_message.Message):
    __slots__ = ("scorer_suite_item_id", "score_config_id", "scorer_bundle", "weight", "required", "enabled", "display_order", "target_selector", "metadata", "reasoning_mode")
    SCORER_SUITE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    SCORER_BUNDLE_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_ORDER_FIELD_NUMBER: _ClassVar[int]
    TARGET_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    REASONING_MODE_FIELD_NUMBER: _ClassVar[int]
    scorer_suite_item_id: str
    score_config_id: str
    scorer_bundle: ScorerBundleV1
    weight: float
    required: bool
    enabled: bool
    display_order: int
    target_selector: ScorerTargetSelectorV1
    metadata: _struct_pb2.Struct
    reasoning_mode: ScorerReasoningModeV1
    def __init__(self, scorer_suite_item_id: _Optional[str] = ..., score_config_id: _Optional[str] = ..., scorer_bundle: _Optional[_Union[ScorerBundleV1, _Mapping]] = ..., weight: _Optional[float] = ..., required: _Optional[bool] = ..., enabled: _Optional[bool] = ..., display_order: _Optional[int] = ..., target_selector: _Optional[_Union[ScorerTargetSelectorV1, _Mapping]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., reasoning_mode: _Optional[_Union[ScorerReasoningModeV1, str]] = ...) -> None: ...

class ScorerSuiteV1(_message.Message):
    __slots__ = ("scorer_suite_id", "suite_key", "name", "description", "aggregation_mode", "pass_threshold", "items", "metadata", "is_archived", "archived_at", "archived_by_user_id", "created_by_user_id", "created_at", "updated_at", "default_reasoning_mode")
    SCORER_SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    SUITE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_MODE_FIELD_NUMBER: _ClassVar[int]
    PASS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    IS_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_AT_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_REASONING_MODE_FIELD_NUMBER: _ClassVar[int]
    scorer_suite_id: str
    suite_key: str
    name: str
    description: str
    aggregation_mode: ScorerAggregationModeV1
    pass_threshold: float
    items: _containers.RepeatedCompositeFieldContainer[ScorerSuiteItemV1]
    metadata: _struct_pb2.Struct
    is_archived: bool
    archived_at: _timestamp_pb2.Timestamp
    archived_by_user_id: str
    created_by_user_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    default_reasoning_mode: ScorerReasoningModeV1
    def __init__(self, scorer_suite_id: _Optional[str] = ..., suite_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., aggregation_mode: _Optional[_Union[ScorerAggregationModeV1, str]] = ..., pass_threshold: _Optional[float] = ..., items: _Optional[_Iterable[_Union[ScorerSuiteItemV1, _Mapping]]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., is_archived: _Optional[bool] = ..., archived_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., archived_by_user_id: _Optional[str] = ..., created_by_user_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., default_reasoning_mode: _Optional[_Union[ScorerReasoningModeV1, str]] = ...) -> None: ...

class ScoreVerdictMappingV1(_message.Message):
    __slots__ = ("verdict", "mapped_score")
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    MAPPED_SCORE_FIELD_NUMBER: _ClassVar[int]
    verdict: str
    mapped_score: float
    def __init__(self, verdict: _Optional[str] = ..., mapped_score: _Optional[float] = ...) -> None: ...

class ScorePairwiseWinnerMappingV1(_message.Message):
    __slots__ = ("baseline_label", "candidate_label", "tie_label")
    BASELINE_LABEL_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_LABEL_FIELD_NUMBER: _ClassVar[int]
    TIE_LABEL_FIELD_NUMBER: _ClassVar[int]
    baseline_label: str
    candidate_label: str
    tie_label: str
    def __init__(self, baseline_label: _Optional[str] = ..., candidate_label: _Optional[str] = ..., tie_label: _Optional[str] = ...) -> None: ...

class ScoreConfigSettingsV1(_message.Message):
    __slots__ = ("instructions", "verdict_mappings", "confidence_policy", "minimum_confidence", "aggregation_mode", "pairwise_winner_mapping", "budget_limit_usd")
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    VERDICT_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_POLICY_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_MODE_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_WINNER_MAPPING_FIELD_NUMBER: _ClassVar[int]
    BUDGET_LIMIT_USD_FIELD_NUMBER: _ClassVar[int]
    instructions: str
    verdict_mappings: _containers.RepeatedCompositeFieldContainer[ScoreVerdictMappingV1]
    confidence_policy: ScoreConfidencePolicyV1
    minimum_confidence: float
    aggregation_mode: ScoreAggregationModeV1
    pairwise_winner_mapping: ScorePairwiseWinnerMappingV1
    budget_limit_usd: float
    def __init__(self, instructions: _Optional[str] = ..., verdict_mappings: _Optional[_Iterable[_Union[ScoreVerdictMappingV1, _Mapping]]] = ..., confidence_policy: _Optional[_Union[ScoreConfidencePolicyV1, str]] = ..., minimum_confidence: _Optional[float] = ..., aggregation_mode: _Optional[_Union[ScoreAggregationModeV1, str]] = ..., pairwise_winner_mapping: _Optional[_Union[ScorePairwiseWinnerMappingV1, _Mapping]] = ..., budget_limit_usd: _Optional[float] = ...) -> None: ...

class EvalJobV1(_message.Message):
    __slots__ = ("job_id", "score_config_id", "evaluator_template_id", "experiment_run_id", "experiment_run_item_id", "dataset_item_id", "state", "attempts", "max_attempts", "retry_backoff_seconds", "worker_id", "last_error", "score_id", "execution_trace_id", "execution_cost_usd", "available_at", "started_at", "finished_at", "correlation", "input_payload", "subject_output", "expected_output", "metadata", "created_by_user_id", "created_at", "updated_at", "provider_execution", "scorer_suite_item_id")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_RUN_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    RETRY_BACKOFF_SECONDS_FIELD_NUMBER: _ClassVar[int]
    WORKER_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_FIELD_NUMBER: _ClassVar[int]
    SCORE_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_COST_USD_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_AT_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_FIELD_NUMBER: _ClassVar[int]
    INPUT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    SCORER_SUITE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    score_config_id: str
    evaluator_template_id: str
    experiment_run_id: str
    experiment_run_item_id: str
    dataset_item_id: str
    state: EvalJobStateV1
    attempts: int
    max_attempts: int
    retry_backoff_seconds: int
    worker_id: str
    last_error: str
    score_id: str
    execution_trace_id: str
    execution_cost_usd: float
    available_at: _timestamp_pb2.Timestamp
    started_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    correlation: CorrelationContextV1
    input_payload: _struct_pb2.Struct
    subject_output: _struct_pb2.Struct
    expected_output: _struct_pb2.Struct
    metadata: _struct_pb2.Struct
    created_by_user_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    provider_execution: ProviderExecutionConfigV1
    scorer_suite_item_id: str
    def __init__(self, job_id: _Optional[str] = ..., score_config_id: _Optional[str] = ..., evaluator_template_id: _Optional[str] = ..., experiment_run_id: _Optional[str] = ..., experiment_run_item_id: _Optional[str] = ..., dataset_item_id: _Optional[str] = ..., state: _Optional[_Union[EvalJobStateV1, str]] = ..., attempts: _Optional[int] = ..., max_attempts: _Optional[int] = ..., retry_backoff_seconds: _Optional[int] = ..., worker_id: _Optional[str] = ..., last_error: _Optional[str] = ..., score_id: _Optional[str] = ..., execution_trace_id: _Optional[str] = ..., execution_cost_usd: _Optional[float] = ..., available_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., correlation: _Optional[_Union[CorrelationContextV1, _Mapping]] = ..., input_payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., subject_output: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., expected_output: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., created_by_user_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., provider_execution: _Optional[_Union[ProviderExecutionConfigV1, _Mapping]] = ..., scorer_suite_item_id: _Optional[str] = ...) -> None: ...

class ExecutionArtifactRefV1(_message.Message):
    __slots__ = ("artifact_ref_id", "eval_job_id", "experiment_run_id", "experiment_run_item_id", "score_id", "content_manifest_id", "artifact_role", "artifact_class", "artifact_index", "canonical_storage_uri", "canonical_checksum_sha256", "body_format", "is_query_indexed", "is_replay_required", "created_at")
    ARTIFACT_REF_ID_FIELD_NUMBER: _ClassVar[int]
    EVAL_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_RUN_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_MANIFEST_ID_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_ROLE_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_CLASS_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_INDEX_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_STORAGE_URI_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_CHECKSUM_SHA256_FIELD_NUMBER: _ClassVar[int]
    BODY_FORMAT_FIELD_NUMBER: _ClassVar[int]
    IS_QUERY_INDEXED_FIELD_NUMBER: _ClassVar[int]
    IS_REPLAY_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    artifact_ref_id: str
    eval_job_id: str
    experiment_run_id: str
    experiment_run_item_id: str
    score_id: str
    content_manifest_id: str
    artifact_role: str
    artifact_class: str
    artifact_index: int
    canonical_storage_uri: str
    canonical_checksum_sha256: str
    body_format: str
    is_query_indexed: bool
    is_replay_required: bool
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, artifact_ref_id: _Optional[str] = ..., eval_job_id: _Optional[str] = ..., experiment_run_id: _Optional[str] = ..., experiment_run_item_id: _Optional[str] = ..., score_id: _Optional[str] = ..., content_manifest_id: _Optional[str] = ..., artifact_role: _Optional[str] = ..., artifact_class: _Optional[str] = ..., artifact_index: _Optional[int] = ..., canonical_storage_uri: _Optional[str] = ..., canonical_checksum_sha256: _Optional[str] = ..., body_format: _Optional[str] = ..., is_query_indexed: _Optional[bool] = ..., is_replay_required: _Optional[bool] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ExecutionArtifactPreviewV1(_message.Message):
    __slots__ = ("artifact_ref_id", "artifact_role", "artifact_class", "body_format", "content_preview", "truncated", "preview_bytes", "canonical_storage_uri")
    ARTIFACT_REF_ID_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_ROLE_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_CLASS_FIELD_NUMBER: _ClassVar[int]
    BODY_FORMAT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_BYTES_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_STORAGE_URI_FIELD_NUMBER: _ClassVar[int]
    artifact_ref_id: str
    artifact_role: str
    artifact_class: str
    body_format: str
    content_preview: str
    truncated: bool
    preview_bytes: int
    canonical_storage_uri: str
    def __init__(self, artifact_ref_id: _Optional[str] = ..., artifact_role: _Optional[str] = ..., artifact_class: _Optional[str] = ..., body_format: _Optional[str] = ..., content_preview: _Optional[str] = ..., truncated: _Optional[bool] = ..., preview_bytes: _Optional[int] = ..., canonical_storage_uri: _Optional[str] = ...) -> None: ...

class EvalExecutionEvidenceV1(_message.Message):
    __slots__ = ("target_prompt", "target_request", "target_response", "candidate_output", "prompt", "provider_request", "provider_response", "verdict", "explanation", "execution_metadata")
    TARGET_PROMPT_FIELD_NUMBER: _ClassVar[int]
    TARGET_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TARGET_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_METADATA_FIELD_NUMBER: _ClassVar[int]
    target_prompt: ExecutionArtifactPreviewV1
    target_request: ExecutionArtifactPreviewV1
    target_response: ExecutionArtifactPreviewV1
    candidate_output: ExecutionArtifactPreviewV1
    prompt: ExecutionArtifactPreviewV1
    provider_request: ExecutionArtifactPreviewV1
    provider_response: ExecutionArtifactPreviewV1
    verdict: ExecutionArtifactPreviewV1
    explanation: ExecutionArtifactPreviewV1
    execution_metadata: ExecutionArtifactPreviewV1
    def __init__(self, target_prompt: _Optional[_Union[ExecutionArtifactPreviewV1, _Mapping]] = ..., target_request: _Optional[_Union[ExecutionArtifactPreviewV1, _Mapping]] = ..., target_response: _Optional[_Union[ExecutionArtifactPreviewV1, _Mapping]] = ..., candidate_output: _Optional[_Union[ExecutionArtifactPreviewV1, _Mapping]] = ..., prompt: _Optional[_Union[ExecutionArtifactPreviewV1, _Mapping]] = ..., provider_request: _Optional[_Union[ExecutionArtifactPreviewV1, _Mapping]] = ..., provider_response: _Optional[_Union[ExecutionArtifactPreviewV1, _Mapping]] = ..., verdict: _Optional[_Union[ExecutionArtifactPreviewV1, _Mapping]] = ..., explanation: _Optional[_Union[ExecutionArtifactPreviewV1, _Mapping]] = ..., execution_metadata: _Optional[_Union[ExecutionArtifactPreviewV1, _Mapping]] = ...) -> None: ...

class ExecutionArtifactRoleSummaryV1(_message.Message):
    __slots__ = ("artifact_role", "artifact_count", "query_indexed_count", "replay_required_count", "artifact_classes")
    ARTIFACT_ROLE_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_COUNT_FIELD_NUMBER: _ClassVar[int]
    QUERY_INDEXED_COUNT_FIELD_NUMBER: _ClassVar[int]
    REPLAY_REQUIRED_COUNT_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_CLASSES_FIELD_NUMBER: _ClassVar[int]
    artifact_role: str
    artifact_count: int
    query_indexed_count: int
    replay_required_count: int
    artifact_classes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, artifact_role: _Optional[str] = ..., artifact_count: _Optional[int] = ..., query_indexed_count: _Optional[int] = ..., replay_required_count: _Optional[int] = ..., artifact_classes: _Optional[_Iterable[str]] = ...) -> None: ...

class ExperimentRunArtifactSummaryV1(_message.Message):
    __slots__ = ("total_artifacts", "query_indexed_artifacts", "replay_required_artifacts", "total_content_bytes", "by_role")
    TOTAL_ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    QUERY_INDEXED_ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    REPLAY_REQUIRED_ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CONTENT_BYTES_FIELD_NUMBER: _ClassVar[int]
    BY_ROLE_FIELD_NUMBER: _ClassVar[int]
    total_artifacts: int
    query_indexed_artifacts: int
    replay_required_artifacts: int
    total_content_bytes: int
    by_role: _containers.RepeatedCompositeFieldContainer[ExecutionArtifactRoleSummaryV1]
    def __init__(self, total_artifacts: _Optional[int] = ..., query_indexed_artifacts: _Optional[int] = ..., replay_required_artifacts: _Optional[int] = ..., total_content_bytes: _Optional[int] = ..., by_role: _Optional[_Iterable[_Union[ExecutionArtifactRoleSummaryV1, _Mapping]]] = ...) -> None: ...

class ExecutionArtifactScopeV1(_message.Message):
    __slots__ = ("eval_job_id", "experiment_run_id", "experiment_run_item_id")
    EVAL_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_RUN_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    eval_job_id: str
    experiment_run_id: str
    experiment_run_item_id: str
    def __init__(self, eval_job_id: _Optional[str] = ..., experiment_run_id: _Optional[str] = ..., experiment_run_item_id: _Optional[str] = ...) -> None: ...

class ExecutionArtifactRoleComparisonV1(_message.Message):
    __slots__ = ("artifact_role", "baseline_count", "comparison_count", "count_delta", "baseline_artifact_classes", "comparison_artifact_classes", "baseline_query_indexed_count", "comparison_query_indexed_count", "baseline_replay_required_count", "comparison_replay_required_count")
    ARTIFACT_ROLE_FIELD_NUMBER: _ClassVar[int]
    BASELINE_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_COUNT_FIELD_NUMBER: _ClassVar[int]
    COUNT_DELTA_FIELD_NUMBER: _ClassVar[int]
    BASELINE_ARTIFACT_CLASSES_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_ARTIFACT_CLASSES_FIELD_NUMBER: _ClassVar[int]
    BASELINE_QUERY_INDEXED_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_QUERY_INDEXED_COUNT_FIELD_NUMBER: _ClassVar[int]
    BASELINE_REPLAY_REQUIRED_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_REPLAY_REQUIRED_COUNT_FIELD_NUMBER: _ClassVar[int]
    artifact_role: str
    baseline_count: int
    comparison_count: int
    count_delta: int
    baseline_artifact_classes: _containers.RepeatedScalarFieldContainer[str]
    comparison_artifact_classes: _containers.RepeatedScalarFieldContainer[str]
    baseline_query_indexed_count: int
    comparison_query_indexed_count: int
    baseline_replay_required_count: int
    comparison_replay_required_count: int
    def __init__(self, artifact_role: _Optional[str] = ..., baseline_count: _Optional[int] = ..., comparison_count: _Optional[int] = ..., count_delta: _Optional[int] = ..., baseline_artifact_classes: _Optional[_Iterable[str]] = ..., comparison_artifact_classes: _Optional[_Iterable[str]] = ..., baseline_query_indexed_count: _Optional[int] = ..., comparison_query_indexed_count: _Optional[int] = ..., baseline_replay_required_count: _Optional[int] = ..., comparison_replay_required_count: _Optional[int] = ...) -> None: ...

class ExecutionArtifactComparisonV1(_message.Message):
    __slots__ = ("baseline_scope", "comparison_scope", "baseline_total_artifacts", "comparison_total_artifacts", "total_artifact_delta", "added_roles", "removed_roles", "role_comparisons")
    BASELINE_SCOPE_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_SCOPE_FIELD_NUMBER: _ClassVar[int]
    BASELINE_TOTAL_ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_TOTAL_ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ARTIFACT_DELTA_FIELD_NUMBER: _ClassVar[int]
    ADDED_ROLES_FIELD_NUMBER: _ClassVar[int]
    REMOVED_ROLES_FIELD_NUMBER: _ClassVar[int]
    ROLE_COMPARISONS_FIELD_NUMBER: _ClassVar[int]
    baseline_scope: ExecutionArtifactScopeV1
    comparison_scope: ExecutionArtifactScopeV1
    baseline_total_artifacts: int
    comparison_total_artifacts: int
    total_artifact_delta: int
    added_roles: _containers.RepeatedScalarFieldContainer[str]
    removed_roles: _containers.RepeatedScalarFieldContainer[str]
    role_comparisons: _containers.RepeatedCompositeFieldContainer[ExecutionArtifactRoleComparisonV1]
    def __init__(self, baseline_scope: _Optional[_Union[ExecutionArtifactScopeV1, _Mapping]] = ..., comparison_scope: _Optional[_Union[ExecutionArtifactScopeV1, _Mapping]] = ..., baseline_total_artifacts: _Optional[int] = ..., comparison_total_artifacts: _Optional[int] = ..., total_artifact_delta: _Optional[int] = ..., added_roles: _Optional[_Iterable[str]] = ..., removed_roles: _Optional[_Iterable[str]] = ..., role_comparisons: _Optional[_Iterable[_Union[ExecutionArtifactRoleComparisonV1, _Mapping]]] = ...) -> None: ...

class ExperimentRunV1(_message.Message):
    __slots__ = ("experiment_run_id", "run_key", "name", "experiment_input_id", "dataset_version_id", "score_config_id", "state", "execution_trace_id", "summary", "created_by_user_id", "created_at", "started_at", "finished_at", "updated_at", "experiment_target_id", "comparison_role", "baseline_experiment_run_id", "candidate_experiment_run_id", "scorer_target", "expansion_status", "expected_scorer_count", "expected_job_count", "expansion_error", "scorer_breakdowns", "aggregate_score", "aggregate_passed", "aggregate_status", "aggregate_pass_threshold", "missing_required_scorer_count", "failed_required_scorer_count", "failed_optional_scorer_count")
    EXPERIMENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_INPUT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_ROLE_FIELD_NUMBER: _ClassVar[int]
    BASELINE_EXPERIMENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_EXPERIMENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    SCORER_TARGET_FIELD_NUMBER: _ClassVar[int]
    EXPANSION_STATUS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SCORER_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_JOB_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXPANSION_ERROR_FIELD_NUMBER: _ClassVar[int]
    SCORER_BREAKDOWNS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_SCORE_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_PASSED_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_STATUS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_PASS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    MISSING_REQUIRED_SCORER_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_REQUIRED_SCORER_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_OPTIONAL_SCORER_COUNT_FIELD_NUMBER: _ClassVar[int]
    experiment_run_id: str
    run_key: str
    name: str
    experiment_input_id: str
    dataset_version_id: str
    score_config_id: str
    state: ExperimentRunStateV1
    execution_trace_id: str
    summary: _struct_pb2.Struct
    created_by_user_id: str
    created_at: _timestamp_pb2.Timestamp
    started_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    experiment_target_id: str
    comparison_role: ExperimentRunRoleV1
    baseline_experiment_run_id: str
    candidate_experiment_run_id: str
    scorer_target: ExperimentRunScorerTargetV1
    expansion_status: ExperimentRunExpansionStatusV1
    expected_scorer_count: int
    expected_job_count: int
    expansion_error: str
    scorer_breakdowns: _containers.RepeatedCompositeFieldContainer[ExperimentRunScorerBreakdownV1]
    aggregate_score: float
    aggregate_passed: bool
    aggregate_status: ExperimentRunAggregateStatusV1
    aggregate_pass_threshold: float
    missing_required_scorer_count: int
    failed_required_scorer_count: int
    failed_optional_scorer_count: int
    def __init__(self, experiment_run_id: _Optional[str] = ..., run_key: _Optional[str] = ..., name: _Optional[str] = ..., experiment_input_id: _Optional[str] = ..., dataset_version_id: _Optional[str] = ..., score_config_id: _Optional[str] = ..., state: _Optional[_Union[ExperimentRunStateV1, str]] = ..., execution_trace_id: _Optional[str] = ..., summary: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., created_by_user_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., experiment_target_id: _Optional[str] = ..., comparison_role: _Optional[_Union[ExperimentRunRoleV1, str]] = ..., baseline_experiment_run_id: _Optional[str] = ..., candidate_experiment_run_id: _Optional[str] = ..., scorer_target: _Optional[_Union[ExperimentRunScorerTargetV1, _Mapping]] = ..., expansion_status: _Optional[_Union[ExperimentRunExpansionStatusV1, str]] = ..., expected_scorer_count: _Optional[int] = ..., expected_job_count: _Optional[int] = ..., expansion_error: _Optional[str] = ..., scorer_breakdowns: _Optional[_Iterable[_Union[ExperimentRunScorerBreakdownV1, _Mapping]]] = ..., aggregate_score: _Optional[float] = ..., aggregate_passed: _Optional[bool] = ..., aggregate_status: _Optional[_Union[ExperimentRunAggregateStatusV1, str]] = ..., aggregate_pass_threshold: _Optional[float] = ..., missing_required_scorer_count: _Optional[int] = ..., failed_required_scorer_count: _Optional[int] = ..., failed_optional_scorer_count: _Optional[int] = ...) -> None: ...

class ExperimentRunItemV1(_message.Message):
    __slots__ = ("experiment_run_item_id", "experiment_run_id", "dataset_item_id", "state", "score_id", "execution_trace_id", "execution_cost_usd", "last_error", "created_at", "updated_at", "failure_stage", "scorer_breakdowns", "aggregate_score", "aggregate_passed", "aggregate_status", "missing_required_scorer_count", "failed_required_scorer_count", "failed_optional_scorer_count")
    EXPERIMENT_RUN_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SCORE_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_COST_USD_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_STAGE_FIELD_NUMBER: _ClassVar[int]
    SCORER_BREAKDOWNS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_SCORE_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_PASSED_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_STATUS_FIELD_NUMBER: _ClassVar[int]
    MISSING_REQUIRED_SCORER_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_REQUIRED_SCORER_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_OPTIONAL_SCORER_COUNT_FIELD_NUMBER: _ClassVar[int]
    experiment_run_item_id: str
    experiment_run_id: str
    dataset_item_id: str
    state: EvalJobStateV1
    score_id: str
    execution_trace_id: str
    execution_cost_usd: float
    last_error: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    failure_stage: ExperimentRunFailureStageV1
    scorer_breakdowns: _containers.RepeatedCompositeFieldContainer[ExperimentRunItemScorerBreakdownV1]
    aggregate_score: float
    aggregate_passed: bool
    aggregate_status: ExperimentRunAggregateStatusV1
    missing_required_scorer_count: int
    failed_required_scorer_count: int
    failed_optional_scorer_count: int
    def __init__(self, experiment_run_item_id: _Optional[str] = ..., experiment_run_id: _Optional[str] = ..., dataset_item_id: _Optional[str] = ..., state: _Optional[_Union[EvalJobStateV1, str]] = ..., score_id: _Optional[str] = ..., execution_trace_id: _Optional[str] = ..., execution_cost_usd: _Optional[float] = ..., last_error: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., failure_stage: _Optional[_Union[ExperimentRunFailureStageV1, str]] = ..., scorer_breakdowns: _Optional[_Iterable[_Union[ExperimentRunItemScorerBreakdownV1, _Mapping]]] = ..., aggregate_score: _Optional[float] = ..., aggregate_passed: _Optional[bool] = ..., aggregate_status: _Optional[_Union[ExperimentRunAggregateStatusV1, str]] = ..., missing_required_scorer_count: _Optional[int] = ..., failed_required_scorer_count: _Optional[int] = ..., failed_optional_scorer_count: _Optional[int] = ...) -> None: ...

class ExperimentRunScorerBreakdownV1(_message.Message):
    __slots__ = ("scorer_suite_item_id", "scorer_suite_id", "score_config_id", "evaluator_template_id", "metric_name", "display_name", "weight", "required", "state", "expected_item_count", "pending_item_count", "running_item_count", "succeeded_item_count", "failed_item_count", "dead_letter_item_count", "scored_item_count", "avg_score_value", "pass_count", "fail_count", "avg_execution_cost_usd", "last_error", "target_selector", "reasoning_mode", "pass_threshold", "normalized_weight")
    SCORER_SUITE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    SCORER_SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    PENDING_ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    RUNNING_ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUCCEEDED_ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    DEAD_LETTER_ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    SCORED_ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVG_SCORE_VALUE_FIELD_NUMBER: _ClassVar[int]
    PASS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAIL_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVG_EXECUTION_COST_USD_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_FIELD_NUMBER: _ClassVar[int]
    TARGET_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    REASONING_MODE_FIELD_NUMBER: _ClassVar[int]
    PASS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    NORMALIZED_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    scorer_suite_item_id: str
    scorer_suite_id: str
    score_config_id: str
    evaluator_template_id: str
    metric_name: str
    display_name: str
    weight: float
    required: bool
    state: EvalJobStateV1
    expected_item_count: int
    pending_item_count: int
    running_item_count: int
    succeeded_item_count: int
    failed_item_count: int
    dead_letter_item_count: int
    scored_item_count: int
    avg_score_value: float
    pass_count: int
    fail_count: int
    avg_execution_cost_usd: float
    last_error: str
    target_selector: ScorerTargetSelectorV1
    reasoning_mode: ScorerReasoningModeV1
    pass_threshold: float
    normalized_weight: float
    def __init__(self, scorer_suite_item_id: _Optional[str] = ..., scorer_suite_id: _Optional[str] = ..., score_config_id: _Optional[str] = ..., evaluator_template_id: _Optional[str] = ..., metric_name: _Optional[str] = ..., display_name: _Optional[str] = ..., weight: _Optional[float] = ..., required: _Optional[bool] = ..., state: _Optional[_Union[EvalJobStateV1, str]] = ..., expected_item_count: _Optional[int] = ..., pending_item_count: _Optional[int] = ..., running_item_count: _Optional[int] = ..., succeeded_item_count: _Optional[int] = ..., failed_item_count: _Optional[int] = ..., dead_letter_item_count: _Optional[int] = ..., scored_item_count: _Optional[int] = ..., avg_score_value: _Optional[float] = ..., pass_count: _Optional[int] = ..., fail_count: _Optional[int] = ..., avg_execution_cost_usd: _Optional[float] = ..., last_error: _Optional[str] = ..., target_selector: _Optional[_Union[ScorerTargetSelectorV1, _Mapping]] = ..., reasoning_mode: _Optional[_Union[ScorerReasoningModeV1, str]] = ..., pass_threshold: _Optional[float] = ..., normalized_weight: _Optional[float] = ...) -> None: ...

class ExperimentRunItemScorerBreakdownV1(_message.Message):
    __slots__ = ("scorer_suite_item_id", "scorer_suite_id", "score_config_id", "evaluator_template_id", "metric_name", "display_name", "weight", "required", "state", "eval_job_id", "score_id", "score_value", "score_label", "execution_trace_id", "execution_cost_usd", "last_error", "target_selector", "reasoning_mode", "pass_threshold", "normalized_weight", "explanation", "explanation_artifact_ref_ids", "evidence_artifact_ref_ids")
    SCORER_SUITE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    SCORER_SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    EVAL_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_VALUE_FIELD_NUMBER: _ClassVar[int]
    SCORE_LABEL_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_COST_USD_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_FIELD_NUMBER: _ClassVar[int]
    TARGET_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    REASONING_MODE_FIELD_NUMBER: _ClassVar[int]
    PASS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    NORMALIZED_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_ARTIFACT_REF_IDS_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_ARTIFACT_REF_IDS_FIELD_NUMBER: _ClassVar[int]
    scorer_suite_item_id: str
    scorer_suite_id: str
    score_config_id: str
    evaluator_template_id: str
    metric_name: str
    display_name: str
    weight: float
    required: bool
    state: EvalJobStateV1
    eval_job_id: str
    score_id: str
    score_value: float
    score_label: str
    execution_trace_id: str
    execution_cost_usd: float
    last_error: str
    target_selector: ScorerTargetSelectorV1
    reasoning_mode: ScorerReasoningModeV1
    pass_threshold: float
    normalized_weight: float
    explanation: str
    explanation_artifact_ref_ids: _containers.RepeatedScalarFieldContainer[str]
    evidence_artifact_ref_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, scorer_suite_item_id: _Optional[str] = ..., scorer_suite_id: _Optional[str] = ..., score_config_id: _Optional[str] = ..., evaluator_template_id: _Optional[str] = ..., metric_name: _Optional[str] = ..., display_name: _Optional[str] = ..., weight: _Optional[float] = ..., required: _Optional[bool] = ..., state: _Optional[_Union[EvalJobStateV1, str]] = ..., eval_job_id: _Optional[str] = ..., score_id: _Optional[str] = ..., score_value: _Optional[float] = ..., score_label: _Optional[str] = ..., execution_trace_id: _Optional[str] = ..., execution_cost_usd: _Optional[float] = ..., last_error: _Optional[str] = ..., target_selector: _Optional[_Union[ScorerTargetSelectorV1, _Mapping]] = ..., reasoning_mode: _Optional[_Union[ScorerReasoningModeV1, str]] = ..., pass_threshold: _Optional[float] = ..., normalized_weight: _Optional[float] = ..., explanation: _Optional[str] = ..., explanation_artifact_ref_ids: _Optional[_Iterable[str]] = ..., evidence_artifact_ref_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class EvalScoreResultV1(_message.Message):
    __slots__ = ("score_id", "metric_name", "score_value", "score_label", "explanation", "evaluator_name", "evaluator_kind", "occurred_at")
    SCORE_ID_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    SCORE_VALUE_FIELD_NUMBER: _ClassVar[int]
    SCORE_LABEL_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_KIND_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    score_id: str
    metric_name: str
    score_value: float
    score_label: str
    explanation: str
    evaluator_name: str
    evaluator_kind: str
    occurred_at: _timestamp_pb2.Timestamp
    def __init__(self, score_id: _Optional[str] = ..., metric_name: _Optional[str] = ..., score_value: _Optional[float] = ..., score_label: _Optional[str] = ..., explanation: _Optional[str] = ..., evaluator_name: _Optional[str] = ..., evaluator_kind: _Optional[str] = ..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ExperimentRunItemDetailV1(_message.Message):
    __slots__ = ("item", "eval_job", "dataset_item", "subject_output", "expected_output", "score", "artifact_refs", "artifact_previews", "execution_evidence", "computed_summary")
    ITEM_FIELD_NUMBER: _ClassVar[int]
    EVAL_JOB_FIELD_NUMBER: _ClassVar[int]
    DATASET_ITEM_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_REFS_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_PREVIEWS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    COMPUTED_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    item: ExperimentRunItemV1
    eval_job: EvalJobV1
    dataset_item: DatasetItemV1
    subject_output: _struct_pb2.Struct
    expected_output: _struct_pb2.Struct
    score: EvalScoreResultV1
    artifact_refs: _containers.RepeatedCompositeFieldContainer[ExecutionArtifactRefV1]
    artifact_previews: _containers.RepeatedCompositeFieldContainer[ExecutionArtifactPreviewV1]
    execution_evidence: EvalExecutionEvidenceV1
    computed_summary: ExperimentRunItemComputedSummaryV1
    def __init__(self, item: _Optional[_Union[ExperimentRunItemV1, _Mapping]] = ..., eval_job: _Optional[_Union[EvalJobV1, _Mapping]] = ..., dataset_item: _Optional[_Union[DatasetItemV1, _Mapping]] = ..., subject_output: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., expected_output: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., score: _Optional[_Union[EvalScoreResultV1, _Mapping]] = ..., artifact_refs: _Optional[_Iterable[_Union[ExecutionArtifactRefV1, _Mapping]]] = ..., artifact_previews: _Optional[_Iterable[_Union[ExecutionArtifactPreviewV1, _Mapping]]] = ..., execution_evidence: _Optional[_Union[EvalExecutionEvidenceV1, _Mapping]] = ..., computed_summary: _Optional[_Union[ExperimentRunItemComputedSummaryV1, _Mapping]] = ...) -> None: ...

class ExperimentRunItemComparisonV1(_message.Message):
    __slots__ = ("dataset_item_id", "baseline", "comparison", "score_delta", "execution_cost_delta_usd", "verdict_changed")
    DATASET_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    BASELINE_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_FIELD_NUMBER: _ClassVar[int]
    SCORE_DELTA_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_COST_DELTA_USD_FIELD_NUMBER: _ClassVar[int]
    VERDICT_CHANGED_FIELD_NUMBER: _ClassVar[int]
    dataset_item_id: str
    baseline: ExperimentRunItemDetailV1
    comparison: ExperimentRunItemDetailV1
    score_delta: float
    execution_cost_delta_usd: float
    verdict_changed: bool
    def __init__(self, dataset_item_id: _Optional[str] = ..., baseline: _Optional[_Union[ExperimentRunItemDetailV1, _Mapping]] = ..., comparison: _Optional[_Union[ExperimentRunItemDetailV1, _Mapping]] = ..., score_delta: _Optional[float] = ..., execution_cost_delta_usd: _Optional[float] = ..., verdict_changed: _Optional[bool] = ...) -> None: ...

class ExperimentRunItemSortV1(_message.Message):
    __slots__ = ("sort_key", "descending")
    SORT_KEY_FIELD_NUMBER: _ClassVar[int]
    DESCENDING_FIELD_NUMBER: _ClassVar[int]
    sort_key: ExperimentRunItemSortKeyV1
    descending: bool
    def __init__(self, sort_key: _Optional[_Union[ExperimentRunItemSortKeyV1, str]] = ..., descending: _Optional[bool] = ...) -> None: ...

class ExperimentRunItemFilterV1(_message.Message):
    __slots__ = ("states", "min_score_value", "max_score_value", "score_label", "dataset_tags", "error_query", "customer_id", "deployment_id", "prompt_version", "feature_id", "model_version", "tool_version")
    STATES_FIELD_NUMBER: _ClassVar[int]
    MIN_SCORE_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_SCORE_VALUE_FIELD_NUMBER: _ClassVar[int]
    SCORE_LABEL_FIELD_NUMBER: _ClassVar[int]
    DATASET_TAGS_FIELD_NUMBER: _ClassVar[int]
    ERROR_QUERY_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_FIELD_NUMBER: _ClassVar[int]
    FEATURE_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
    TOOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    states: _containers.RepeatedScalarFieldContainer[EvalJobStateV1]
    min_score_value: float
    max_score_value: float
    score_label: str
    dataset_tags: _containers.RepeatedScalarFieldContainer[str]
    error_query: str
    customer_id: str
    deployment_id: str
    prompt_version: str
    feature_id: str
    model_version: str
    tool_version: str
    def __init__(self, states: _Optional[_Iterable[_Union[EvalJobStateV1, str]]] = ..., min_score_value: _Optional[float] = ..., max_score_value: _Optional[float] = ..., score_label: _Optional[str] = ..., dataset_tags: _Optional[_Iterable[str]] = ..., error_query: _Optional[str] = ..., customer_id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., prompt_version: _Optional[str] = ..., feature_id: _Optional[str] = ..., model_version: _Optional[str] = ..., tool_version: _Optional[str] = ...) -> None: ...

class ReleaseGateCohortFiltersV1(_message.Message):
    __slots__ = ("customer_ids", "account_ids", "deployment_ids", "prompt_versions", "model_versions", "tool_versions", "feature_ids")
    CUSTOMER_IDS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_IDS_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_IDS_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    TOOL_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    FEATURE_IDS_FIELD_NUMBER: _ClassVar[int]
    customer_ids: _containers.RepeatedScalarFieldContainer[str]
    account_ids: _containers.RepeatedScalarFieldContainer[str]
    deployment_ids: _containers.RepeatedScalarFieldContainer[str]
    prompt_versions: _containers.RepeatedScalarFieldContainer[str]
    model_versions: _containers.RepeatedScalarFieldContainer[str]
    tool_versions: _containers.RepeatedScalarFieldContainer[str]
    feature_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, customer_ids: _Optional[_Iterable[str]] = ..., account_ids: _Optional[_Iterable[str]] = ..., deployment_ids: _Optional[_Iterable[str]] = ..., prompt_versions: _Optional[_Iterable[str]] = ..., model_versions: _Optional[_Iterable[str]] = ..., tool_versions: _Optional[_Iterable[str]] = ..., feature_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ReleaseGateRolloutBudgetV1(_message.Message):
    __slots__ = ("max_failed_scores", "max_bad_outcomes", "max_impacted_customers", "max_impacted_users", "max_impact_score")
    MAX_FAILED_SCORES_FIELD_NUMBER: _ClassVar[int]
    MAX_BAD_OUTCOMES_FIELD_NUMBER: _ClassVar[int]
    MAX_IMPACTED_CUSTOMERS_FIELD_NUMBER: _ClassVar[int]
    MAX_IMPACTED_USERS_FIELD_NUMBER: _ClassVar[int]
    MAX_IMPACT_SCORE_FIELD_NUMBER: _ClassVar[int]
    max_failed_scores: int
    max_bad_outcomes: int
    max_impacted_customers: int
    max_impacted_users: int
    max_impact_score: float
    def __init__(self, max_failed_scores: _Optional[int] = ..., max_bad_outcomes: _Optional[int] = ..., max_impacted_customers: _Optional[int] = ..., max_impacted_users: _Optional[int] = ..., max_impact_score: _Optional[float] = ...) -> None: ...

class ReleaseGateServiceImpactPolicyV1(_message.Message):
    __slots__ = ("max_service_error_rate_delta_pct", "max_service_latency_delta_ms", "deployment_lookback_days")
    MAX_SERVICE_ERROR_RATE_DELTA_PCT_FIELD_NUMBER: _ClassVar[int]
    MAX_SERVICE_LATENCY_DELTA_MS_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_LOOKBACK_DAYS_FIELD_NUMBER: _ClassVar[int]
    max_service_error_rate_delta_pct: float
    max_service_latency_delta_ms: float
    deployment_lookback_days: int
    def __init__(self, max_service_error_rate_delta_pct: _Optional[float] = ..., max_service_latency_delta_ms: _Optional[float] = ..., deployment_lookback_days: _Optional[int] = ...) -> None: ...

class ReleaseGateDeliveryPolicyV1(_message.Message):
    __slots__ = ("max_attempts", "retry_backoff_seconds", "escalate_on_retry_exhaustion", "escalation_impact_score_threshold")
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    RETRY_BACKOFF_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ESCALATE_ON_RETRY_EXHAUSTION_FIELD_NUMBER: _ClassVar[int]
    ESCALATION_IMPACT_SCORE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    max_attempts: int
    retry_backoff_seconds: int
    escalate_on_retry_exhaustion: bool
    escalation_impact_score_threshold: float
    def __init__(self, max_attempts: _Optional[int] = ..., retry_backoff_seconds: _Optional[int] = ..., escalate_on_retry_exhaustion: _Optional[bool] = ..., escalation_impact_score_threshold: _Optional[float] = ...) -> None: ...

class ReleaseGatePolicyV1(_message.Message):
    __slots__ = ("baseline_strategy", "cohort_filters", "rollout_budget", "service_impact", "delivery_policy")
    BASELINE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    COHORT_FILTERS_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_BUDGET_FIELD_NUMBER: _ClassVar[int]
    SERVICE_IMPACT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_POLICY_FIELD_NUMBER: _ClassVar[int]
    baseline_strategy: BaselineStrategyV1
    cohort_filters: ReleaseGateCohortFiltersV1
    rollout_budget: ReleaseGateRolloutBudgetV1
    service_impact: ReleaseGateServiceImpactPolicyV1
    delivery_policy: ReleaseGateDeliveryPolicyV1
    def __init__(self, baseline_strategy: _Optional[_Union[BaselineStrategyV1, str]] = ..., cohort_filters: _Optional[_Union[ReleaseGateCohortFiltersV1, _Mapping]] = ..., rollout_budget: _Optional[_Union[ReleaseGateRolloutBudgetV1, _Mapping]] = ..., service_impact: _Optional[_Union[ReleaseGateServiceImpactPolicyV1, _Mapping]] = ..., delivery_policy: _Optional[_Union[ReleaseGateDeliveryPolicyV1, _Mapping]] = ...) -> None: ...

class ReleaseGateDeliverySummaryV1(_message.Message):
    __slots__ = ("pending", "delivered", "retryable", "failed", "acknowledged", "escalated", "suppressed", "latest_delivery_id")
    PENDING_FIELD_NUMBER: _ClassVar[int]
    DELIVERED_FIELD_NUMBER: _ClassVar[int]
    RETRYABLE_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGED_FIELD_NUMBER: _ClassVar[int]
    ESCALATED_FIELD_NUMBER: _ClassVar[int]
    SUPPRESSED_FIELD_NUMBER: _ClassVar[int]
    LATEST_DELIVERY_ID_FIELD_NUMBER: _ClassVar[int]
    pending: int
    delivered: int
    retryable: int
    failed: int
    acknowledged: int
    escalated: int
    suppressed: int
    latest_delivery_id: str
    def __init__(self, pending: _Optional[int] = ..., delivered: _Optional[int] = ..., retryable: _Optional[int] = ..., failed: _Optional[int] = ..., acknowledged: _Optional[int] = ..., escalated: _Optional[int] = ..., suppressed: _Optional[int] = ..., latest_delivery_id: _Optional[str] = ...) -> None: ...

class ReleaseGateV1(_message.Message):
    __slots__ = ("gate_id", "gate_key", "name", "metric_name", "deployment_id", "baseline_deployment_id", "evaluation_window_hours", "min_samples", "max_score_regression", "max_avg_cost_usd", "max_bad_outcomes", "config", "created_by_user_id", "created_at", "updated_at", "destination_ids", "customer_priority_policy_id", "service_name", "namespace", "environment", "policy")
    GATE_ID_FIELD_NUMBER: _ClassVar[int]
    GATE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    BASELINE_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_WINDOW_HOURS_FIELD_NUMBER: _ClassVar[int]
    MIN_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    MAX_SCORE_REGRESSION_FIELD_NUMBER: _ClassVar[int]
    MAX_AVG_COST_USD_FIELD_NUMBER: _ClassVar[int]
    MAX_BAD_OUTCOMES_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_IDS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_PRIORITY_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    gate_id: str
    gate_key: str
    name: str
    metric_name: str
    deployment_id: str
    baseline_deployment_id: str
    evaluation_window_hours: int
    min_samples: int
    max_score_regression: float
    max_avg_cost_usd: float
    max_bad_outcomes: int
    config: _struct_pb2.Struct
    created_by_user_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    destination_ids: _containers.RepeatedScalarFieldContainer[str]
    customer_priority_policy_id: str
    service_name: str
    namespace: str
    environment: str
    policy: ReleaseGatePolicyV1
    def __init__(self, gate_id: _Optional[str] = ..., gate_key: _Optional[str] = ..., name: _Optional[str] = ..., metric_name: _Optional[str] = ..., deployment_id: _Optional[str] = ..., baseline_deployment_id: _Optional[str] = ..., evaluation_window_hours: _Optional[int] = ..., min_samples: _Optional[int] = ..., max_score_regression: _Optional[float] = ..., max_avg_cost_usd: _Optional[float] = ..., max_bad_outcomes: _Optional[int] = ..., config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., created_by_user_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., destination_ids: _Optional[_Iterable[str]] = ..., customer_priority_policy_id: _Optional[str] = ..., service_name: _Optional[str] = ..., namespace: _Optional[str] = ..., environment: _Optional[str] = ..., policy: _Optional[_Union[ReleaseGatePolicyV1, _Mapping]] = ...) -> None: ...

class ReleaseGateEvaluationV1(_message.Message):
    __slots__ = ("evaluation_id", "gate_id", "decision", "summary", "deployment_id", "baseline_deployment_id", "metric_name", "current_avg_score", "baseline_avg_score", "avg_score_delta", "current_sample_count", "baseline_sample_count", "current_avg_cost_usd", "bad_outcomes_count", "impact_summary", "created_by_user_id", "created_at", "used_fallback_baseline", "baseline_source", "failure_reasons", "destination_delivery_ids", "baseline_strategy", "simulated")
    EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    GATE_ID_FIELD_NUMBER: _ClassVar[int]
    DECISION_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    BASELINE_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENT_AVG_SCORE_FIELD_NUMBER: _ClassVar[int]
    BASELINE_AVG_SCORE_FIELD_NUMBER: _ClassVar[int]
    AVG_SCORE_DELTA_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    BASELINE_SAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CURRENT_AVG_COST_USD_FIELD_NUMBER: _ClassVar[int]
    BAD_OUTCOMES_COUNT_FIELD_NUMBER: _ClassVar[int]
    IMPACT_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    USED_FALLBACK_BASELINE_FIELD_NUMBER: _ClassVar[int]
    BASELINE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASONS_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_DELIVERY_IDS_FIELD_NUMBER: _ClassVar[int]
    BASELINE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    SIMULATED_FIELD_NUMBER: _ClassVar[int]
    evaluation_id: str
    gate_id: str
    decision: ReleaseGateDecisionV1
    summary: str
    deployment_id: str
    baseline_deployment_id: str
    metric_name: str
    current_avg_score: float
    baseline_avg_score: float
    avg_score_delta: float
    current_sample_count: int
    baseline_sample_count: int
    current_avg_cost_usd: float
    bad_outcomes_count: int
    impact_summary: _struct_pb2.Struct
    created_by_user_id: str
    created_at: _timestamp_pb2.Timestamp
    used_fallback_baseline: bool
    baseline_source: str
    failure_reasons: _containers.RepeatedScalarFieldContainer[str]
    destination_delivery_ids: _containers.RepeatedScalarFieldContainer[str]
    baseline_strategy: BaselineStrategyV1
    simulated: bool
    def __init__(self, evaluation_id: _Optional[str] = ..., gate_id: _Optional[str] = ..., decision: _Optional[_Union[ReleaseGateDecisionV1, str]] = ..., summary: _Optional[str] = ..., deployment_id: _Optional[str] = ..., baseline_deployment_id: _Optional[str] = ..., metric_name: _Optional[str] = ..., current_avg_score: _Optional[float] = ..., baseline_avg_score: _Optional[float] = ..., avg_score_delta: _Optional[float] = ..., current_sample_count: _Optional[int] = ..., baseline_sample_count: _Optional[int] = ..., current_avg_cost_usd: _Optional[float] = ..., bad_outcomes_count: _Optional[int] = ..., impact_summary: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., created_by_user_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., used_fallback_baseline: _Optional[bool] = ..., baseline_source: _Optional[str] = ..., failure_reasons: _Optional[_Iterable[str]] = ..., destination_delivery_ids: _Optional[_Iterable[str]] = ..., baseline_strategy: _Optional[_Union[BaselineStrategyV1, str]] = ..., simulated: _Optional[bool] = ...) -> None: ...

class ReleaseGateEvaluationComparisonV1(_message.Message):
    __slots__ = ("gate", "baseline_evaluation", "comparison_evaluation", "decision_changed", "current_avg_score_delta", "avg_score_delta_change", "current_sample_count_delta", "baseline_sample_count_delta", "current_avg_cost_usd_delta", "bad_outcomes_count_delta", "added_failure_reasons", "removed_failure_reasons", "used_fallback_baseline_changed", "baseline_source_changed")
    GATE_FIELD_NUMBER: _ClassVar[int]
    BASELINE_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    DECISION_CHANGED_FIELD_NUMBER: _ClassVar[int]
    CURRENT_AVG_SCORE_DELTA_FIELD_NUMBER: _ClassVar[int]
    AVG_SCORE_DELTA_CHANGE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SAMPLE_COUNT_DELTA_FIELD_NUMBER: _ClassVar[int]
    BASELINE_SAMPLE_COUNT_DELTA_FIELD_NUMBER: _ClassVar[int]
    CURRENT_AVG_COST_USD_DELTA_FIELD_NUMBER: _ClassVar[int]
    BAD_OUTCOMES_COUNT_DELTA_FIELD_NUMBER: _ClassVar[int]
    ADDED_FAILURE_REASONS_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FAILURE_REASONS_FIELD_NUMBER: _ClassVar[int]
    USED_FALLBACK_BASELINE_CHANGED_FIELD_NUMBER: _ClassVar[int]
    BASELINE_SOURCE_CHANGED_FIELD_NUMBER: _ClassVar[int]
    gate: ReleaseGateV1
    baseline_evaluation: ReleaseGateEvaluationV1
    comparison_evaluation: ReleaseGateEvaluationV1
    decision_changed: bool
    current_avg_score_delta: float
    avg_score_delta_change: float
    current_sample_count_delta: int
    baseline_sample_count_delta: int
    current_avg_cost_usd_delta: float
    bad_outcomes_count_delta: int
    added_failure_reasons: _containers.RepeatedScalarFieldContainer[str]
    removed_failure_reasons: _containers.RepeatedScalarFieldContainer[str]
    used_fallback_baseline_changed: bool
    baseline_source_changed: bool
    def __init__(self, gate: _Optional[_Union[ReleaseGateV1, _Mapping]] = ..., baseline_evaluation: _Optional[_Union[ReleaseGateEvaluationV1, _Mapping]] = ..., comparison_evaluation: _Optional[_Union[ReleaseGateEvaluationV1, _Mapping]] = ..., decision_changed: _Optional[bool] = ..., current_avg_score_delta: _Optional[float] = ..., avg_score_delta_change: _Optional[float] = ..., current_sample_count_delta: _Optional[int] = ..., baseline_sample_count_delta: _Optional[int] = ..., current_avg_cost_usd_delta: _Optional[float] = ..., bad_outcomes_count_delta: _Optional[int] = ..., added_failure_reasons: _Optional[_Iterable[str]] = ..., removed_failure_reasons: _Optional[_Iterable[str]] = ..., used_fallback_baseline_changed: _Optional[bool] = ..., baseline_source_changed: _Optional[bool] = ...) -> None: ...

class ExperimentRunSummaryV1(_message.Message):
    __slots__ = ("total_items", "pending_items", "running_items", "succeeded_items", "failed_items", "dead_letter_items", "scored_items", "avg_score_value", "pass_count", "fail_count", "avg_execution_cost_usd")
    TOTAL_ITEMS_FIELD_NUMBER: _ClassVar[int]
    PENDING_ITEMS_FIELD_NUMBER: _ClassVar[int]
    RUNNING_ITEMS_FIELD_NUMBER: _ClassVar[int]
    SUCCEEDED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    FAILED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    DEAD_LETTER_ITEMS_FIELD_NUMBER: _ClassVar[int]
    SCORED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    AVG_SCORE_VALUE_FIELD_NUMBER: _ClassVar[int]
    PASS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAIL_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVG_EXECUTION_COST_USD_FIELD_NUMBER: _ClassVar[int]
    total_items: int
    pending_items: int
    running_items: int
    succeeded_items: int
    failed_items: int
    dead_letter_items: int
    scored_items: int
    avg_score_value: float
    pass_count: int
    fail_count: int
    avg_execution_cost_usd: float
    def __init__(self, total_items: _Optional[int] = ..., pending_items: _Optional[int] = ..., running_items: _Optional[int] = ..., succeeded_items: _Optional[int] = ..., failed_items: _Optional[int] = ..., dead_letter_items: _Optional[int] = ..., scored_items: _Optional[int] = ..., avg_score_value: _Optional[float] = ..., pass_count: _Optional[int] = ..., fail_count: _Optional[int] = ..., avg_execution_cost_usd: _Optional[float] = ...) -> None: ...

class ExperimentRunTokenUsageSummaryV1(_message.Message):
    __slots__ = ("input_tokens", "output_tokens", "total_tokens", "cache_read_input_tokens", "cache_creation_input_tokens", "reasoning_tokens", "completeness")
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_READ_INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_CREATION_INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    REASONING_TOKENS_FIELD_NUMBER: _ClassVar[int]
    COMPLETENESS_FIELD_NUMBER: _ClassVar[int]
    input_tokens: int
    output_tokens: int
    total_tokens: int
    cache_read_input_tokens: int
    cache_creation_input_tokens: int
    reasoning_tokens: int
    completeness: ExperimentRunTokenUsageCompletenessV1
    def __init__(self, input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., total_tokens: _Optional[int] = ..., cache_read_input_tokens: _Optional[int] = ..., cache_creation_input_tokens: _Optional[int] = ..., reasoning_tokens: _Optional[int] = ..., completeness: _Optional[_Union[ExperimentRunTokenUsageCompletenessV1, str]] = ...) -> None: ...

class ExperimentRunItemComputedSummaryV1(_message.Message):
    __slots__ = ("computed_decision", "decision_reason", "risk_score", "execution_cost_usd", "token_usage", "input_preview", "subject_output_preview", "expected_output_preview", "has_artifacts", "candidate_token_usage", "evaluator_token_usage")
    COMPUTED_DECISION_FIELD_NUMBER: _ClassVar[int]
    DECISION_REASON_FIELD_NUMBER: _ClassVar[int]
    RISK_SCORE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_COST_USD_FIELD_NUMBER: _ClassVar[int]
    TOKEN_USAGE_FIELD_NUMBER: _ClassVar[int]
    INPUT_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_OUTPUT_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUT_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    HAS_ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_TOKEN_USAGE_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_TOKEN_USAGE_FIELD_NUMBER: _ClassVar[int]
    computed_decision: str
    decision_reason: str
    risk_score: float
    execution_cost_usd: float
    token_usage: ExperimentRunTokenUsageSummaryV1
    input_preview: str
    subject_output_preview: str
    expected_output_preview: str
    has_artifacts: bool
    candidate_token_usage: ExperimentRunTokenUsageSummaryV1
    evaluator_token_usage: ExperimentRunTokenUsageSummaryV1
    def __init__(self, computed_decision: _Optional[str] = ..., decision_reason: _Optional[str] = ..., risk_score: _Optional[float] = ..., execution_cost_usd: _Optional[float] = ..., token_usage: _Optional[_Union[ExperimentRunTokenUsageSummaryV1, _Mapping]] = ..., input_preview: _Optional[str] = ..., subject_output_preview: _Optional[str] = ..., expected_output_preview: _Optional[str] = ..., has_artifacts: _Optional[bool] = ..., candidate_token_usage: _Optional[_Union[ExperimentRunTokenUsageSummaryV1, _Mapping]] = ..., evaluator_token_usage: _Optional[_Union[ExperimentRunTokenUsageSummaryV1, _Mapping]] = ...) -> None: ...

class ExperimentRunRichSummaryV1(_message.Message):
    __slots__ = ("computed_decision", "decision_reason", "risk_score", "total_execution_cost_usd", "avg_execution_cost_usd", "token_usage", "primary_input_preview", "primary_subject_output_preview", "primary_expected_output_preview", "artifact_count", "has_comparisons", "candidate_token_usage", "evaluator_token_usage", "comparison_alignment", "comparison_alignment_reason")
    COMPUTED_DECISION_FIELD_NUMBER: _ClassVar[int]
    DECISION_REASON_FIELD_NUMBER: _ClassVar[int]
    RISK_SCORE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_EXECUTION_COST_USD_FIELD_NUMBER: _ClassVar[int]
    AVG_EXECUTION_COST_USD_FIELD_NUMBER: _ClassVar[int]
    TOKEN_USAGE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_INPUT_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_SUBJECT_OUTPUT_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_EXPECTED_OUTPUT_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_COUNT_FIELD_NUMBER: _ClassVar[int]
    HAS_COMPARISONS_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_TOKEN_USAGE_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_TOKEN_USAGE_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_ALIGNMENT_REASON_FIELD_NUMBER: _ClassVar[int]
    computed_decision: str
    decision_reason: str
    risk_score: float
    total_execution_cost_usd: float
    avg_execution_cost_usd: float
    token_usage: ExperimentRunTokenUsageSummaryV1
    primary_input_preview: str
    primary_subject_output_preview: str
    primary_expected_output_preview: str
    artifact_count: int
    has_comparisons: bool
    candidate_token_usage: ExperimentRunTokenUsageSummaryV1
    evaluator_token_usage: ExperimentRunTokenUsageSummaryV1
    comparison_alignment: ExperimentRunComparisonAlignmentV1
    comparison_alignment_reason: str
    def __init__(self, computed_decision: _Optional[str] = ..., decision_reason: _Optional[str] = ..., risk_score: _Optional[float] = ..., total_execution_cost_usd: _Optional[float] = ..., avg_execution_cost_usd: _Optional[float] = ..., token_usage: _Optional[_Union[ExperimentRunTokenUsageSummaryV1, _Mapping]] = ..., primary_input_preview: _Optional[str] = ..., primary_subject_output_preview: _Optional[str] = ..., primary_expected_output_preview: _Optional[str] = ..., artifact_count: _Optional[int] = ..., has_comparisons: _Optional[bool] = ..., candidate_token_usage: _Optional[_Union[ExperimentRunTokenUsageSummaryV1, _Mapping]] = ..., evaluator_token_usage: _Optional[_Union[ExperimentRunTokenUsageSummaryV1, _Mapping]] = ..., comparison_alignment: _Optional[_Union[ExperimentRunComparisonAlignmentV1, str]] = ..., comparison_alignment_reason: _Optional[str] = ...) -> None: ...

class ExperimentRunComparisonV1(_message.Message):
    __slots__ = ("baseline_run", "comparison_run", "baseline_summary", "comparison_summary", "total_items_delta", "succeeded_items_delta", "failed_items_delta", "dead_letter_items_delta", "avg_score_value_delta", "avg_execution_cost_usd_delta", "same_experiment_input", "same_score_config", "same_dataset_version", "comparison_alignment", "comparison_alignment_reason")
    BASELINE_RUN_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_RUN_FIELD_NUMBER: _ClassVar[int]
    BASELINE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ITEMS_DELTA_FIELD_NUMBER: _ClassVar[int]
    SUCCEEDED_ITEMS_DELTA_FIELD_NUMBER: _ClassVar[int]
    FAILED_ITEMS_DELTA_FIELD_NUMBER: _ClassVar[int]
    DEAD_LETTER_ITEMS_DELTA_FIELD_NUMBER: _ClassVar[int]
    AVG_SCORE_VALUE_DELTA_FIELD_NUMBER: _ClassVar[int]
    AVG_EXECUTION_COST_USD_DELTA_FIELD_NUMBER: _ClassVar[int]
    SAME_EXPERIMENT_INPUT_FIELD_NUMBER: _ClassVar[int]
    SAME_SCORE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SAME_DATASET_VERSION_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_ALIGNMENT_REASON_FIELD_NUMBER: _ClassVar[int]
    baseline_run: ExperimentRunV1
    comparison_run: ExperimentRunV1
    baseline_summary: ExperimentRunSummaryV1
    comparison_summary: ExperimentRunSummaryV1
    total_items_delta: int
    succeeded_items_delta: int
    failed_items_delta: int
    dead_letter_items_delta: int
    avg_score_value_delta: float
    avg_execution_cost_usd_delta: float
    same_experiment_input: bool
    same_score_config: bool
    same_dataset_version: bool
    comparison_alignment: ExperimentRunComparisonAlignmentV1
    comparison_alignment_reason: str
    def __init__(self, baseline_run: _Optional[_Union[ExperimentRunV1, _Mapping]] = ..., comparison_run: _Optional[_Union[ExperimentRunV1, _Mapping]] = ..., baseline_summary: _Optional[_Union[ExperimentRunSummaryV1, _Mapping]] = ..., comparison_summary: _Optional[_Union[ExperimentRunSummaryV1, _Mapping]] = ..., total_items_delta: _Optional[int] = ..., succeeded_items_delta: _Optional[int] = ..., failed_items_delta: _Optional[int] = ..., dead_letter_items_delta: _Optional[int] = ..., avg_score_value_delta: _Optional[float] = ..., avg_execution_cost_usd_delta: _Optional[float] = ..., same_experiment_input: _Optional[bool] = ..., same_score_config: _Optional[bool] = ..., same_dataset_version: _Optional[bool] = ..., comparison_alignment: _Optional[_Union[ExperimentRunComparisonAlignmentV1, str]] = ..., comparison_alignment_reason: _Optional[str] = ...) -> None: ...

class TraceAgenticSummaryV1(_message.Message):
    __slots__ = ("trace_id", "score_count", "feedback_count", "outcome_count", "content_manifest_count", "dataset_lineage_count", "metric_names", "feedback_keys", "outcome_types", "content_classes", "dataset_collection_names")
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_COUNT_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_MANIFEST_COUNT_FIELD_NUMBER: _ClassVar[int]
    DATASET_LINEAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAMES_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_KEYS_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_TYPES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_CLASSES_FIELD_NUMBER: _ClassVar[int]
    DATASET_COLLECTION_NAMES_FIELD_NUMBER: _ClassVar[int]
    trace_id: str
    score_count: int
    feedback_count: int
    outcome_count: int
    content_manifest_count: int
    dataset_lineage_count: int
    metric_names: _containers.RepeatedScalarFieldContainer[str]
    feedback_keys: _containers.RepeatedScalarFieldContainer[str]
    outcome_types: _containers.RepeatedScalarFieldContainer[str]
    content_classes: _containers.RepeatedScalarFieldContainer[str]
    dataset_collection_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, trace_id: _Optional[str] = ..., score_count: _Optional[int] = ..., feedback_count: _Optional[int] = ..., outcome_count: _Optional[int] = ..., content_manifest_count: _Optional[int] = ..., dataset_lineage_count: _Optional[int] = ..., metric_names: _Optional[_Iterable[str]] = ..., feedback_keys: _Optional[_Iterable[str]] = ..., outcome_types: _Optional[_Iterable[str]] = ..., content_classes: _Optional[_Iterable[str]] = ..., dataset_collection_names: _Optional[_Iterable[str]] = ...) -> None: ...

class TraceAgenticComparisonV1(_message.Message):
    __slots__ = ("baseline_summary", "comparison_summary", "score_count_delta", "feedback_count_delta", "outcome_count_delta", "content_manifest_count_delta", "dataset_lineage_count_delta", "added_metric_names", "removed_metric_names", "added_feedback_keys", "removed_feedback_keys", "added_outcome_types", "removed_outcome_types", "added_content_classes", "removed_content_classes", "added_dataset_collection_names", "removed_dataset_collection_names")
    BASELINE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SCORE_COUNT_DELTA_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_COUNT_DELTA_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_COUNT_DELTA_FIELD_NUMBER: _ClassVar[int]
    CONTENT_MANIFEST_COUNT_DELTA_FIELD_NUMBER: _ClassVar[int]
    DATASET_LINEAGE_COUNT_DELTA_FIELD_NUMBER: _ClassVar[int]
    ADDED_METRIC_NAMES_FIELD_NUMBER: _ClassVar[int]
    REMOVED_METRIC_NAMES_FIELD_NUMBER: _ClassVar[int]
    ADDED_FEEDBACK_KEYS_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FEEDBACK_KEYS_FIELD_NUMBER: _ClassVar[int]
    ADDED_OUTCOME_TYPES_FIELD_NUMBER: _ClassVar[int]
    REMOVED_OUTCOME_TYPES_FIELD_NUMBER: _ClassVar[int]
    ADDED_CONTENT_CLASSES_FIELD_NUMBER: _ClassVar[int]
    REMOVED_CONTENT_CLASSES_FIELD_NUMBER: _ClassVar[int]
    ADDED_DATASET_COLLECTION_NAMES_FIELD_NUMBER: _ClassVar[int]
    REMOVED_DATASET_COLLECTION_NAMES_FIELD_NUMBER: _ClassVar[int]
    baseline_summary: TraceAgenticSummaryV1
    comparison_summary: TraceAgenticSummaryV1
    score_count_delta: int
    feedback_count_delta: int
    outcome_count_delta: int
    content_manifest_count_delta: int
    dataset_lineage_count_delta: int
    added_metric_names: _containers.RepeatedScalarFieldContainer[str]
    removed_metric_names: _containers.RepeatedScalarFieldContainer[str]
    added_feedback_keys: _containers.RepeatedScalarFieldContainer[str]
    removed_feedback_keys: _containers.RepeatedScalarFieldContainer[str]
    added_outcome_types: _containers.RepeatedScalarFieldContainer[str]
    removed_outcome_types: _containers.RepeatedScalarFieldContainer[str]
    added_content_classes: _containers.RepeatedScalarFieldContainer[str]
    removed_content_classes: _containers.RepeatedScalarFieldContainer[str]
    added_dataset_collection_names: _containers.RepeatedScalarFieldContainer[str]
    removed_dataset_collection_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, baseline_summary: _Optional[_Union[TraceAgenticSummaryV1, _Mapping]] = ..., comparison_summary: _Optional[_Union[TraceAgenticSummaryV1, _Mapping]] = ..., score_count_delta: _Optional[int] = ..., feedback_count_delta: _Optional[int] = ..., outcome_count_delta: _Optional[int] = ..., content_manifest_count_delta: _Optional[int] = ..., dataset_lineage_count_delta: _Optional[int] = ..., added_metric_names: _Optional[_Iterable[str]] = ..., removed_metric_names: _Optional[_Iterable[str]] = ..., added_feedback_keys: _Optional[_Iterable[str]] = ..., removed_feedback_keys: _Optional[_Iterable[str]] = ..., added_outcome_types: _Optional[_Iterable[str]] = ..., removed_outcome_types: _Optional[_Iterable[str]] = ..., added_content_classes: _Optional[_Iterable[str]] = ..., removed_content_classes: _Optional[_Iterable[str]] = ..., added_dataset_collection_names: _Optional[_Iterable[str]] = ..., removed_dataset_collection_names: _Optional[_Iterable[str]] = ...) -> None: ...

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

class TraceInvestigationReasonV1(_message.Message):
    __slots__ = ("reason_code", "title", "summary", "confidence", "evidence_links")
    REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_LINKS_FIELD_NUMBER: _ClassVar[int]
    reason_code: str
    title: str
    summary: str
    confidence: RcaConfidenceV1
    evidence_links: _containers.RepeatedCompositeFieldContainer[TraceInvestigationEvidenceLinkV1]
    def __init__(self, reason_code: _Optional[str] = ..., title: _Optional[str] = ..., summary: _Optional[str] = ..., confidence: _Optional[_Union[RcaConfidenceV1, str]] = ..., evidence_links: _Optional[_Iterable[_Union[TraceInvestigationEvidenceLinkV1, _Mapping]]] = ...) -> None: ...

class TraceInvestigationRootCauseCandidateV1(_message.Message):
    __slots__ = ("candidate_id", "title", "summary", "confidence", "evidence_links", "status")
    CANDIDATE_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_LINKS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    candidate_id: str
    title: str
    summary: str
    confidence: RcaConfidenceV1
    evidence_links: _containers.RepeatedCompositeFieldContainer[TraceInvestigationEvidenceLinkV1]
    status: str
    def __init__(self, candidate_id: _Optional[str] = ..., title: _Optional[str] = ..., summary: _Optional[str] = ..., confidence: _Optional[_Union[RcaConfidenceV1, str]] = ..., evidence_links: _Optional[_Iterable[_Union[TraceInvestigationEvidenceLinkV1, _Mapping]]] = ..., status: _Optional[str] = ...) -> None: ...

class TraceInvestigationRegressionComparisonV1(_message.Message):
    __slots__ = ("comparison_key", "title", "baseline_label", "current_label", "baseline_value", "current_value", "delta", "percent_delta", "confidence", "evidence_links", "unavailable_reasons")
    COMPARISON_KEY_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BASELINE_LABEL_FIELD_NUMBER: _ClassVar[int]
    CURRENT_LABEL_FIELD_NUMBER: _ClassVar[int]
    BASELINE_VALUE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DELTA_FIELD_NUMBER: _ClassVar[int]
    PERCENT_DELTA_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_LINKS_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE_REASONS_FIELD_NUMBER: _ClassVar[int]
    comparison_key: str
    title: str
    baseline_label: str
    current_label: str
    baseline_value: float
    current_value: float
    delta: float
    percent_delta: float
    confidence: RcaConfidenceV1
    evidence_links: _containers.RepeatedCompositeFieldContainer[TraceInvestigationEvidenceLinkV1]
    unavailable_reasons: _containers.RepeatedCompositeFieldContainer[TraceInvestigationUnavailableReasonV1]
    def __init__(self, comparison_key: _Optional[str] = ..., title: _Optional[str] = ..., baseline_label: _Optional[str] = ..., current_label: _Optional[str] = ..., baseline_value: _Optional[float] = ..., current_value: _Optional[float] = ..., delta: _Optional[float] = ..., percent_delta: _Optional[float] = ..., confidence: _Optional[_Union[RcaConfidenceV1, str]] = ..., evidence_links: _Optional[_Iterable[_Union[TraceInvestigationEvidenceLinkV1, _Mapping]]] = ..., unavailable_reasons: _Optional[_Iterable[_Union[TraceInvestigationUnavailableReasonV1, _Mapping]]] = ...) -> None: ...

class TraceInvestigationTimelineEventV1(_message.Message):
    __slots__ = ("timestamp", "event_type", "label", "status", "duration_ms", "evidence_links")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_LINKS_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    event_type: str
    label: str
    status: str
    duration_ms: float
    evidence_links: _containers.RepeatedCompositeFieldContainer[TraceInvestigationEvidenceLinkV1]
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., event_type: _Optional[str] = ..., label: _Optional[str] = ..., status: _Optional[str] = ..., duration_ms: _Optional[float] = ..., evidence_links: _Optional[_Iterable[_Union[TraceInvestigationEvidenceLinkV1, _Mapping]]] = ...) -> None: ...

class TraceInvestigationThreadMessagePreviewV1(_message.Message):
    __slots__ = ("role", "content_class", "redaction_state", "content_preview", "content_ref", "truncated")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_CLASS_FIELD_NUMBER: _ClassVar[int]
    REDACTION_STATE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    CONTENT_REF_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    role: str
    content_class: str
    redaction_state: str
    content_preview: str
    content_ref: str
    truncated: bool
    def __init__(self, role: _Optional[str] = ..., content_class: _Optional[str] = ..., redaction_state: _Optional[str] = ..., content_preview: _Optional[str] = ..., content_ref: _Optional[str] = ..., truncated: _Optional[bool] = ...) -> None: ...

class TraceInvestigationThreadPreviewV1(_message.Message):
    __slots__ = ("messages", "truncated", "unavailable_reasons")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE_REASONS_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[TraceInvestigationThreadMessagePreviewV1]
    truncated: bool
    unavailable_reasons: _containers.RepeatedCompositeFieldContainer[TraceInvestigationUnavailableReasonV1]
    def __init__(self, messages: _Optional[_Iterable[_Union[TraceInvestigationThreadMessagePreviewV1, _Mapping]]] = ..., truncated: _Optional[bool] = ..., unavailable_reasons: _Optional[_Iterable[_Union[TraceInvestigationUnavailableReasonV1, _Mapping]]] = ...) -> None: ...

class TraceInvestigationSpanPreviewV1(_message.Message):
    __slots__ = ("span_id", "parent_span_id", "name", "kind", "service_name", "duration_ms", "status", "error_type", "error_message", "unavailable_reasons")
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE_REASONS_FIELD_NUMBER: _ClassVar[int]
    span_id: str
    parent_span_id: str
    name: str
    kind: str
    service_name: str
    duration_ms: float
    status: str
    error_type: str
    error_message: str
    unavailable_reasons: _containers.RepeatedCompositeFieldContainer[TraceInvestigationUnavailableReasonV1]
    def __init__(self, span_id: _Optional[str] = ..., parent_span_id: _Optional[str] = ..., name: _Optional[str] = ..., kind: _Optional[str] = ..., service_name: _Optional[str] = ..., duration_ms: _Optional[float] = ..., status: _Optional[str] = ..., error_type: _Optional[str] = ..., error_message: _Optional[str] = ..., unavailable_reasons: _Optional[_Iterable[_Union[TraceInvestigationUnavailableReasonV1, _Mapping]]] = ...) -> None: ...

class TraceInvestigationScorePreviewV1(_message.Message):
    __slots__ = ("score_id", "metric_name", "score_value", "score_label", "explanation", "evaluator_name", "evaluator_kind", "occurred_at")
    SCORE_ID_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    SCORE_VALUE_FIELD_NUMBER: _ClassVar[int]
    SCORE_LABEL_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_KIND_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    score_id: str
    metric_name: str
    score_value: float
    score_label: str
    explanation: str
    evaluator_name: str
    evaluator_kind: str
    occurred_at: _timestamp_pb2.Timestamp
    def __init__(self, score_id: _Optional[str] = ..., metric_name: _Optional[str] = ..., score_value: _Optional[float] = ..., score_label: _Optional[str] = ..., explanation: _Optional[str] = ..., evaluator_name: _Optional[str] = ..., evaluator_kind: _Optional[str] = ..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class TraceInvestigationFeedbackPreviewV1(_message.Message):
    __slots__ = ("feedback_event_id", "feedback_key", "rating_value", "rating_label", "comment_preview", "approval_status", "occurred_at")
    FEEDBACK_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_KEY_FIELD_NUMBER: _ClassVar[int]
    RATING_VALUE_FIELD_NUMBER: _ClassVar[int]
    RATING_LABEL_FIELD_NUMBER: _ClassVar[int]
    COMMENT_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    feedback_event_id: str
    feedback_key: str
    rating_value: float
    rating_label: str
    comment_preview: str
    approval_status: str
    occurred_at: _timestamp_pb2.Timestamp
    def __init__(self, feedback_event_id: _Optional[str] = ..., feedback_key: _Optional[str] = ..., rating_value: _Optional[float] = ..., rating_label: _Optional[str] = ..., comment_preview: _Optional[str] = ..., approval_status: _Optional[str] = ..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class TraceInvestigationOutcomePreviewV1(_message.Message):
    __slots__ = ("outcome_event_id", "outcome_type", "status", "numeric_value", "payload_preview", "truncated", "occurred_at")
    OUTCOME_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_VALUE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    outcome_event_id: str
    outcome_type: str
    status: str
    numeric_value: float
    payload_preview: str
    truncated: bool
    occurred_at: _timestamp_pb2.Timestamp
    def __init__(self, outcome_event_id: _Optional[str] = ..., outcome_type: _Optional[str] = ..., status: _Optional[str] = ..., numeric_value: _Optional[float] = ..., payload_preview: _Optional[str] = ..., truncated: _Optional[bool] = ..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class TraceInvestigationRawPayloadPreviewV1(_message.Message):
    __slots__ = ("content_manifest_id", "content_class", "storage_backend", "storage_uri", "sensitivity", "redaction_status", "size_bytes", "payload_preview", "truncated", "occurred_at")
    CONTENT_MANIFEST_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_CLASS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_BACKEND_FIELD_NUMBER: _ClassVar[int]
    STORAGE_URI_FIELD_NUMBER: _ClassVar[int]
    SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    REDACTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    content_manifest_id: str
    content_class: str
    storage_backend: str
    storage_uri: str
    sensitivity: str
    redaction_status: str
    size_bytes: int
    payload_preview: str
    truncated: bool
    occurred_at: _timestamp_pb2.Timestamp
    def __init__(self, content_manifest_id: _Optional[str] = ..., content_class: _Optional[str] = ..., storage_backend: _Optional[str] = ..., storage_uri: _Optional[str] = ..., sensitivity: _Optional[str] = ..., redaction_status: _Optional[str] = ..., size_bytes: _Optional[int] = ..., payload_preview: _Optional[str] = ..., truncated: _Optional[bool] = ..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AgenticEvidenceGraphNodeV1(_message.Message):
    __slots__ = ("node_id", "node_type", "label", "status", "metadata", "evidence_links")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_LINKS_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    node_type: str
    label: str
    status: str
    metadata: _struct_pb2.Struct
    evidence_links: _containers.RepeatedCompositeFieldContainer[TraceInvestigationEvidenceLinkV1]
    def __init__(self, node_id: _Optional[str] = ..., node_type: _Optional[str] = ..., label: _Optional[str] = ..., status: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., evidence_links: _Optional[_Iterable[_Union[TraceInvestigationEvidenceLinkV1, _Mapping]]] = ...) -> None: ...

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

class TraceInvestigationAgentGraphNodeV1(_message.Message):
    __slots__ = ("node_id", "node_type", "label", "status", "evidence_links")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_LINKS_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    node_type: str
    label: str
    status: str
    evidence_links: _containers.RepeatedCompositeFieldContainer[TraceInvestigationEvidenceLinkV1]
    def __init__(self, node_id: _Optional[str] = ..., node_type: _Optional[str] = ..., label: _Optional[str] = ..., status: _Optional[str] = ..., evidence_links: _Optional[_Iterable[_Union[TraceInvestigationEvidenceLinkV1, _Mapping]]] = ...) -> None: ...

class TraceInvestigationAgentGraphEdgeV1(_message.Message):
    __slots__ = ("source_node_id", "target_node_id", "relationship")
    SOURCE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    source_node_id: str
    target_node_id: str
    relationship: str
    def __init__(self, source_node_id: _Optional[str] = ..., target_node_id: _Optional[str] = ..., relationship: _Optional[str] = ...) -> None: ...

class TraceInvestigationAgentGraphPreviewV1(_message.Message):
    __slots__ = ("nodes", "edges", "truncated", "unavailable_reasons")
    NODES_FIELD_NUMBER: _ClassVar[int]
    EDGES_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE_REASONS_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[TraceInvestigationAgentGraphNodeV1]
    edges: _containers.RepeatedCompositeFieldContainer[TraceInvestigationAgentGraphEdgeV1]
    truncated: bool
    unavailable_reasons: _containers.RepeatedCompositeFieldContainer[TraceInvestigationUnavailableReasonV1]
    def __init__(self, nodes: _Optional[_Iterable[_Union[TraceInvestigationAgentGraphNodeV1, _Mapping]]] = ..., edges: _Optional[_Iterable[_Union[TraceInvestigationAgentGraphEdgeV1, _Mapping]]] = ..., truncated: _Optional[bool] = ..., unavailable_reasons: _Optional[_Iterable[_Union[TraceInvestigationUnavailableReasonV1, _Mapping]]] = ...) -> None: ...

class TraceInvestigationRelatedTraceRefV1(_message.Message):
    __slots__ = ("trace_id", "trace_name", "started_at", "relationship", "evidence_links")
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_NAME_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_LINKS_FIELD_NUMBER: _ClassVar[int]
    trace_id: str
    trace_name: str
    started_at: _timestamp_pb2.Timestamp
    relationship: str
    evidence_links: _containers.RepeatedCompositeFieldContainer[TraceInvestigationEvidenceLinkV1]
    def __init__(self, trace_id: _Optional[str] = ..., trace_name: _Optional[str] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., relationship: _Optional[str] = ..., evidence_links: _Optional[_Iterable[_Union[TraceInvestigationEvidenceLinkV1, _Mapping]]] = ...) -> None: ...

class TraceInvestigationDetailPreviewV1(_message.Message):
    __slots__ = ("timeline", "thread", "spans", "scores", "feedback", "outcomes", "raw_payloads", "agent_graph", "related_traces", "unavailable_reasons", "truncated")
    TIMELINE_FIELD_NUMBER: _ClassVar[int]
    THREAD_FIELD_NUMBER: _ClassVar[int]
    SPANS_FIELD_NUMBER: _ClassVar[int]
    SCORES_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    OUTCOMES_FIELD_NUMBER: _ClassVar[int]
    RAW_PAYLOADS_FIELD_NUMBER: _ClassVar[int]
    AGENT_GRAPH_FIELD_NUMBER: _ClassVar[int]
    RELATED_TRACES_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE_REASONS_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    timeline: _containers.RepeatedCompositeFieldContainer[TraceInvestigationTimelineEventV1]
    thread: TraceInvestigationThreadPreviewV1
    spans: _containers.RepeatedCompositeFieldContainer[TraceInvestigationSpanPreviewV1]
    scores: _containers.RepeatedCompositeFieldContainer[TraceInvestigationScorePreviewV1]
    feedback: _containers.RepeatedCompositeFieldContainer[TraceInvestigationFeedbackPreviewV1]
    outcomes: _containers.RepeatedCompositeFieldContainer[TraceInvestigationOutcomePreviewV1]
    raw_payloads: _containers.RepeatedCompositeFieldContainer[TraceInvestigationRawPayloadPreviewV1]
    agent_graph: TraceInvestigationAgentGraphPreviewV1
    related_traces: _containers.RepeatedCompositeFieldContainer[TraceInvestigationRelatedTraceRefV1]
    unavailable_reasons: _containers.RepeatedCompositeFieldContainer[TraceInvestigationUnavailableReasonV1]
    truncated: bool
    def __init__(self, timeline: _Optional[_Iterable[_Union[TraceInvestigationTimelineEventV1, _Mapping]]] = ..., thread: _Optional[_Union[TraceInvestigationThreadPreviewV1, _Mapping]] = ..., spans: _Optional[_Iterable[_Union[TraceInvestigationSpanPreviewV1, _Mapping]]] = ..., scores: _Optional[_Iterable[_Union[TraceInvestigationScorePreviewV1, _Mapping]]] = ..., feedback: _Optional[_Iterable[_Union[TraceInvestigationFeedbackPreviewV1, _Mapping]]] = ..., outcomes: _Optional[_Iterable[_Union[TraceInvestigationOutcomePreviewV1, _Mapping]]] = ..., raw_payloads: _Optional[_Iterable[_Union[TraceInvestigationRawPayloadPreviewV1, _Mapping]]] = ..., agent_graph: _Optional[_Union[TraceInvestigationAgentGraphPreviewV1, _Mapping]] = ..., related_traces: _Optional[_Iterable[_Union[TraceInvestigationRelatedTraceRefV1, _Mapping]]] = ..., unavailable_reasons: _Optional[_Iterable[_Union[TraceInvestigationUnavailableReasonV1, _Mapping]]] = ..., truncated: _Optional[bool] = ...) -> None: ...

class SessionSummaryV1(_message.Message):
    __slots__ = ("trace_count", "score_count", "feedback_count", "outcome_count", "content_manifest_count", "dataset_item_count", "annotation_task_count", "avg_score_value", "negative_feedback_count", "negative_outcome_count")
    TRACE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SCORE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_COUNT_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_MANIFEST_COUNT_FIELD_NUMBER: _ClassVar[int]
    DATASET_ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_TASK_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVG_SCORE_VALUE_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_FEEDBACK_COUNT_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_OUTCOME_COUNT_FIELD_NUMBER: _ClassVar[int]
    trace_count: int
    score_count: int
    feedback_count: int
    outcome_count: int
    content_manifest_count: int
    dataset_item_count: int
    annotation_task_count: int
    avg_score_value: float
    negative_feedback_count: int
    negative_outcome_count: int
    def __init__(self, trace_count: _Optional[int] = ..., score_count: _Optional[int] = ..., feedback_count: _Optional[int] = ..., outcome_count: _Optional[int] = ..., content_manifest_count: _Optional[int] = ..., dataset_item_count: _Optional[int] = ..., annotation_task_count: _Optional[int] = ..., avg_score_value: _Optional[float] = ..., negative_feedback_count: _Optional[int] = ..., negative_outcome_count: _Optional[int] = ...) -> None: ...

class SessionV1(_message.Message):
    __slots__ = ("session_id", "customer_id", "deployment_id", "prompt_version", "model_version", "tool_version", "started_at", "last_seen_at", "summary", "trace_ids", "dataset_item_ids", "annotation_task_ids")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
    TOOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    TRACE_IDS_FIELD_NUMBER: _ClassVar[int]
    DATASET_ITEM_IDS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_TASK_IDS_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    customer_id: str
    deployment_id: str
    prompt_version: str
    model_version: str
    tool_version: str
    started_at: _timestamp_pb2.Timestamp
    last_seen_at: _timestamp_pb2.Timestamp
    summary: SessionSummaryV1
    trace_ids: _containers.RepeatedScalarFieldContainer[str]
    dataset_item_ids: _containers.RepeatedScalarFieldContainer[str]
    annotation_task_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, session_id: _Optional[str] = ..., customer_id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., prompt_version: _Optional[str] = ..., model_version: _Optional[str] = ..., tool_version: _Optional[str] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., summary: _Optional[_Union[SessionSummaryV1, _Mapping]] = ..., trace_ids: _Optional[_Iterable[str]] = ..., dataset_item_ids: _Optional[_Iterable[str]] = ..., annotation_task_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class TraceInvestigationActionRouteV1(_message.Message):
    __slots__ = ("label", "path", "metadata")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    label: str
    path: str
    metadata: _struct_pb2.Struct
    def __init__(self, label: _Optional[str] = ..., path: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class TraceInvestigationActionResourceV1(_message.Message):
    __slots__ = ("resource_kind", "resource_id", "route_path", "metadata")
    RESOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTE_PATH_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    resource_kind: TraceInvestigationActionResourceKindV1
    resource_id: str
    route_path: str
    metadata: _struct_pb2.Struct
    def __init__(self, resource_kind: _Optional[_Union[TraceInvestigationActionResourceKindV1, str]] = ..., resource_id: _Optional[str] = ..., route_path: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class TraceInvestigationActionResultV1(_message.Message):
    __slots__ = ("action_id", "action_kind", "status", "trace_ids", "resources", "route", "metadata", "created_at", "updated_at")
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_KIND_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TRACE_IDS_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    action_id: str
    action_kind: TraceInvestigationActionKindV1
    status: TraceInvestigationActionStatusV1
    trace_ids: _containers.RepeatedScalarFieldContainer[str]
    resources: _containers.RepeatedCompositeFieldContainer[TraceInvestigationActionResourceV1]
    route: TraceInvestigationActionRouteV1
    metadata: _struct_pb2.Struct
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, action_id: _Optional[str] = ..., action_kind: _Optional[_Union[TraceInvestigationActionKindV1, str]] = ..., status: _Optional[_Union[TraceInvestigationActionStatusV1, str]] = ..., trace_ids: _Optional[_Iterable[str]] = ..., resources: _Optional[_Iterable[_Union[TraceInvestigationActionResourceV1, _Mapping]]] = ..., route: _Optional[_Union[TraceInvestigationActionRouteV1, _Mapping]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateTraceInvestigationActionRequest(_message.Message):
    __slots__ = ("action_kind", "trace_ids", "idempotency_key", "title", "summary", "evidence_links", "selected_evidence_keys", "queue_id", "queue_key", "rubric_id", "dataset_collection_id", "dataset_version_id", "dataset_version_label", "dataset_includes", "rationale", "score_config_id", "evaluator_template_id", "candidate_label", "baseline_label", "release_gate_id", "failed_gate_count", "release_impact_score", "suggested_action", "investigation_filter", "destination", "metadata")
    ACTION_KIND_FIELD_NUMBER: _ClassVar[int]
    TRACE_IDS_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_LINKS_FIELD_NUMBER: _ClassVar[int]
    SELECTED_EVIDENCE_KEYS_FIELD_NUMBER: _ClassVar[int]
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    QUEUE_KEY_FIELD_NUMBER: _ClassVar[int]
    RUBRIC_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_VERSION_LABEL_FIELD_NUMBER: _ClassVar[int]
    DATASET_INCLUDES_FIELD_NUMBER: _ClassVar[int]
    RATIONALE_FIELD_NUMBER: _ClassVar[int]
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_LABEL_FIELD_NUMBER: _ClassVar[int]
    BASELINE_LABEL_FIELD_NUMBER: _ClassVar[int]
    RELEASE_GATE_ID_FIELD_NUMBER: _ClassVar[int]
    FAILED_GATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    RELEASE_IMPACT_SCORE_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_ACTION_FIELD_NUMBER: _ClassVar[int]
    INVESTIGATION_FILTER_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    action_kind: TraceInvestigationActionKindV1
    trace_ids: _containers.RepeatedScalarFieldContainer[str]
    idempotency_key: str
    title: str
    summary: str
    evidence_links: _containers.RepeatedCompositeFieldContainer[TraceInvestigationEvidenceLinkV1]
    selected_evidence_keys: _containers.RepeatedScalarFieldContainer[str]
    queue_id: str
    queue_key: str
    rubric_id: str
    dataset_collection_id: str
    dataset_version_id: str
    dataset_version_label: str
    dataset_includes: _containers.RepeatedScalarFieldContainer[TraceInvestigationDatasetIncludeV1]
    rationale: str
    score_config_id: str
    evaluator_template_id: str
    candidate_label: str
    baseline_label: str
    release_gate_id: str
    failed_gate_count: int
    release_impact_score: float
    suggested_action: str
    investigation_filter: ListTraceInvestigationsRequest
    destination: TraceInvestigationActionDestinationV1
    metadata: _struct_pb2.Struct
    def __init__(self, action_kind: _Optional[_Union[TraceInvestigationActionKindV1, str]] = ..., trace_ids: _Optional[_Iterable[str]] = ..., idempotency_key: _Optional[str] = ..., title: _Optional[str] = ..., summary: _Optional[str] = ..., evidence_links: _Optional[_Iterable[_Union[TraceInvestigationEvidenceLinkV1, _Mapping]]] = ..., selected_evidence_keys: _Optional[_Iterable[str]] = ..., queue_id: _Optional[str] = ..., queue_key: _Optional[str] = ..., rubric_id: _Optional[str] = ..., dataset_collection_id: _Optional[str] = ..., dataset_version_id: _Optional[str] = ..., dataset_version_label: _Optional[str] = ..., dataset_includes: _Optional[_Iterable[_Union[TraceInvestigationDatasetIncludeV1, str]]] = ..., rationale: _Optional[str] = ..., score_config_id: _Optional[str] = ..., evaluator_template_id: _Optional[str] = ..., candidate_label: _Optional[str] = ..., baseline_label: _Optional[str] = ..., release_gate_id: _Optional[str] = ..., failed_gate_count: _Optional[int] = ..., release_impact_score: _Optional[float] = ..., suggested_action: _Optional[str] = ..., investigation_filter: _Optional[_Union[ListTraceInvestigationsRequest, _Mapping]] = ..., destination: _Optional[_Union[TraceInvestigationActionDestinationV1, str]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class CreateTraceInvestigationActionResponse(_message.Message):
    __slots__ = ("action",)
    ACTION_FIELD_NUMBER: _ClassVar[int]
    action: TraceInvestigationActionResultV1
    def __init__(self, action: _Optional[_Union[TraceInvestigationActionResultV1, _Mapping]] = ...) -> None: ...

class GetTraceInvestigationActionRequest(_message.Message):
    __slots__ = ("action_id",)
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    action_id: str
    def __init__(self, action_id: _Optional[str] = ...) -> None: ...

class GetTraceInvestigationActionResponse(_message.Message):
    __slots__ = ("action",)
    ACTION_FIELD_NUMBER: _ClassVar[int]
    action: TraceInvestigationActionResultV1
    def __init__(self, action: _Optional[_Union[TraceInvestigationActionResultV1, _Mapping]] = ...) -> None: ...

class ListTraceInvestigationActionsRequest(_message.Message):
    __slots__ = ("action_kind", "trace_id", "limit", "page_token", "page")
    ACTION_KIND_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    action_kind: TraceInvestigationActionKindV1
    trace_id: str
    limit: int
    page_token: str
    page: _common_pb2.PageRequestV1
    def __init__(self, action_kind: _Optional[_Union[TraceInvestigationActionKindV1, str]] = ..., trace_id: _Optional[str] = ..., limit: _Optional[int] = ..., page_token: _Optional[str] = ..., page: _Optional[_Union[_common_pb2.PageRequestV1, _Mapping]] = ...) -> None: ...

class ListTraceInvestigationActionsResponse(_message.Message):
    __slots__ = ("items", "next_page_token", "has_more", "total_count", "page")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[TraceInvestigationActionResultV1]
    next_page_token: str
    has_more: bool
    total_count: int
    page: _common_pb2.PageResponseV1
    def __init__(self, items: _Optional[_Iterable[_Union[TraceInvestigationActionResultV1, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., has_more: _Optional[bool] = ..., total_count: _Optional[int] = ..., page: _Optional[_Union[_common_pb2.PageResponseV1, _Mapping]] = ...) -> None: ...

class TraceInvestigationReleaseEvidenceV1(_message.Message):
    __slots__ = ("evidence_id", "action_id", "release_gate_id", "trace_ids", "evidence_links", "failed_gate_count", "release_impact_score", "suggested_action", "metadata", "created_by_user_id", "created_at", "updated_at")
    EVIDENCE_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_GATE_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_IDS_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_LINKS_FIELD_NUMBER: _ClassVar[int]
    FAILED_GATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    RELEASE_IMPACT_SCORE_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_ACTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    evidence_id: str
    action_id: str
    release_gate_id: str
    trace_ids: _containers.RepeatedScalarFieldContainer[str]
    evidence_links: _containers.RepeatedCompositeFieldContainer[TraceInvestigationEvidenceLinkV1]
    failed_gate_count: int
    release_impact_score: float
    suggested_action: str
    metadata: _struct_pb2.Struct
    created_by_user_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, evidence_id: _Optional[str] = ..., action_id: _Optional[str] = ..., release_gate_id: _Optional[str] = ..., trace_ids: _Optional[_Iterable[str]] = ..., evidence_links: _Optional[_Iterable[_Union[TraceInvestigationEvidenceLinkV1, _Mapping]]] = ..., failed_gate_count: _Optional[int] = ..., release_impact_score: _Optional[float] = ..., suggested_action: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., created_by_user_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetTraceInvestigationReleaseEvidenceRequest(_message.Message):
    __slots__ = ("evidence_id",)
    EVIDENCE_ID_FIELD_NUMBER: _ClassVar[int]
    evidence_id: str
    def __init__(self, evidence_id: _Optional[str] = ...) -> None: ...

class GetTraceInvestigationReleaseEvidenceResponse(_message.Message):
    __slots__ = ("evidence",)
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    evidence: TraceInvestigationReleaseEvidenceV1
    def __init__(self, evidence: _Optional[_Union[TraceInvestigationReleaseEvidenceV1, _Mapping]] = ...) -> None: ...

class ListTraceInvestigationReleaseEvidenceRequest(_message.Message):
    __slots__ = ("release_gate_id", "trace_id", "limit", "page_token", "page")
    RELEASE_GATE_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    release_gate_id: str
    trace_id: str
    limit: int
    page_token: str
    page: _common_pb2.PageRequestV1
    def __init__(self, release_gate_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., limit: _Optional[int] = ..., page_token: _Optional[str] = ..., page: _Optional[_Union[_common_pb2.PageRequestV1, _Mapping]] = ...) -> None: ...

class ListTraceInvestigationReleaseEvidenceResponse(_message.Message):
    __slots__ = ("items", "next_page_token", "has_more", "total_count", "page")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[TraceInvestigationReleaseEvidenceV1]
    next_page_token: str
    has_more: bool
    total_count: int
    page: _common_pb2.PageResponseV1
    def __init__(self, items: _Optional[_Iterable[_Union[TraceInvestigationReleaseEvidenceV1, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., has_more: _Optional[bool] = ..., total_count: _Optional[int] = ..., page: _Optional[_Union[_common_pb2.PageResponseV1, _Mapping]] = ...) -> None: ...

class TraceInvestigationAlertV1(_message.Message):
    __slots__ = ("alert_id", "action_id", "state", "destination", "trace_ids", "investigation_filter", "destination_metadata", "metadata", "created_by_user_id", "created_at", "updated_at")
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    TRACE_IDS_FIELD_NUMBER: _ClassVar[int]
    INVESTIGATION_FILTER_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    alert_id: str
    action_id: str
    state: TraceInvestigationAlertStateV1
    destination: TraceInvestigationActionDestinationV1
    trace_ids: _containers.RepeatedScalarFieldContainer[str]
    investigation_filter: ListTraceInvestigationsRequest
    destination_metadata: _struct_pb2.Struct
    metadata: _struct_pb2.Struct
    created_by_user_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, alert_id: _Optional[str] = ..., action_id: _Optional[str] = ..., state: _Optional[_Union[TraceInvestigationAlertStateV1, str]] = ..., destination: _Optional[_Union[TraceInvestigationActionDestinationV1, str]] = ..., trace_ids: _Optional[_Iterable[str]] = ..., investigation_filter: _Optional[_Union[ListTraceInvestigationsRequest, _Mapping]] = ..., destination_metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., created_by_user_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetTraceInvestigationAlertRequest(_message.Message):
    __slots__ = ("alert_id",)
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    alert_id: str
    def __init__(self, alert_id: _Optional[str] = ...) -> None: ...

class GetTraceInvestigationAlertResponse(_message.Message):
    __slots__ = ("alert",)
    ALERT_FIELD_NUMBER: _ClassVar[int]
    alert: TraceInvestigationAlertV1
    def __init__(self, alert: _Optional[_Union[TraceInvestigationAlertV1, _Mapping]] = ...) -> None: ...

class ListTraceInvestigationAlertsRequest(_message.Message):
    __slots__ = ("state", "trace_id", "limit", "page_token", "page")
    STATE_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    state: TraceInvestigationAlertStateV1
    trace_id: str
    limit: int
    page_token: str
    page: _common_pb2.PageRequestV1
    def __init__(self, state: _Optional[_Union[TraceInvestigationAlertStateV1, str]] = ..., trace_id: _Optional[str] = ..., limit: _Optional[int] = ..., page_token: _Optional[str] = ..., page: _Optional[_Union[_common_pb2.PageRequestV1, _Mapping]] = ...) -> None: ...

class ListTraceInvestigationAlertsResponse(_message.Message):
    __slots__ = ("items", "next_page_token", "has_more", "total_count", "page")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[TraceInvestigationAlertV1]
    next_page_token: str
    has_more: bool
    total_count: int
    page: _common_pb2.PageResponseV1
    def __init__(self, items: _Optional[_Iterable[_Union[TraceInvestigationAlertV1, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., has_more: _Optional[bool] = ..., total_count: _Optional[int] = ..., page: _Optional[_Union[_common_pb2.PageResponseV1, _Mapping]] = ...) -> None: ...

class TraceInvestigationRowV1(_message.Message):
    __slots__ = ("trace_id", "trace_name", "scenario_name", "scenario_summary", "started_at", "duration_ms", "span_count", "service_name", "customer_id", "deployment_id", "prompt_version", "tool_version", "model_version", "provider_name", "mcp_method_name", "score_count", "low_score_count", "avg_score_value", "feedback_count", "negative_feedback_count", "outcome_count", "negative_outcome_count", "content_manifest_count", "dataset_lineage_count", "related_review_task_count", "failed_gate_count", "fix_queue_impact_score", "fix_queue_total_cost_usd", "error_span_count", "has_tool_or_mcp_error", "urgency_label", "detail_preview", "reasons", "root_cause_candidates", "regression_comparisons", "session_id")
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_NAME_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_NAME_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    SPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_FIELD_NUMBER: _ClassVar[int]
    TOOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
    MCP_METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    SCORE_COUNT_FIELD_NUMBER: _ClassVar[int]
    LOW_SCORE_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVG_SCORE_VALUE_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_COUNT_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_FEEDBACK_COUNT_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_COUNT_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_OUTCOME_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_MANIFEST_COUNT_FIELD_NUMBER: _ClassVar[int]
    DATASET_LINEAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    RELATED_REVIEW_TASK_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_GATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FIX_QUEUE_IMPACT_SCORE_FIELD_NUMBER: _ClassVar[int]
    FIX_QUEUE_TOTAL_COST_USD_FIELD_NUMBER: _ClassVar[int]
    ERROR_SPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    HAS_TOOL_OR_MCP_ERROR_FIELD_NUMBER: _ClassVar[int]
    URGENCY_LABEL_FIELD_NUMBER: _ClassVar[int]
    DETAIL_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    REASONS_FIELD_NUMBER: _ClassVar[int]
    ROOT_CAUSE_CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    REGRESSION_COMPARISONS_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    trace_id: str
    trace_name: str
    scenario_name: str
    scenario_summary: str
    started_at: _timestamp_pb2.Timestamp
    duration_ms: float
    span_count: int
    service_name: str
    customer_id: str
    deployment_id: str
    prompt_version: str
    tool_version: str
    model_version: str
    provider_name: str
    mcp_method_name: str
    score_count: int
    low_score_count: int
    avg_score_value: float
    feedback_count: int
    negative_feedback_count: int
    outcome_count: int
    negative_outcome_count: int
    content_manifest_count: int
    dataset_lineage_count: int
    related_review_task_count: int
    failed_gate_count: int
    fix_queue_impact_score: float
    fix_queue_total_cost_usd: float
    error_span_count: int
    has_tool_or_mcp_error: bool
    urgency_label: str
    detail_preview: TraceInvestigationDetailPreviewV1
    reasons: _containers.RepeatedCompositeFieldContainer[TraceInvestigationReasonV1]
    root_cause_candidates: _containers.RepeatedCompositeFieldContainer[TraceInvestigationRootCauseCandidateV1]
    regression_comparisons: _containers.RepeatedCompositeFieldContainer[TraceInvestigationRegressionComparisonV1]
    session_id: str
    def __init__(self, trace_id: _Optional[str] = ..., trace_name: _Optional[str] = ..., scenario_name: _Optional[str] = ..., scenario_summary: _Optional[str] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., duration_ms: _Optional[float] = ..., span_count: _Optional[int] = ..., service_name: _Optional[str] = ..., customer_id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., prompt_version: _Optional[str] = ..., tool_version: _Optional[str] = ..., model_version: _Optional[str] = ..., provider_name: _Optional[str] = ..., mcp_method_name: _Optional[str] = ..., score_count: _Optional[int] = ..., low_score_count: _Optional[int] = ..., avg_score_value: _Optional[float] = ..., feedback_count: _Optional[int] = ..., negative_feedback_count: _Optional[int] = ..., outcome_count: _Optional[int] = ..., negative_outcome_count: _Optional[int] = ..., content_manifest_count: _Optional[int] = ..., dataset_lineage_count: _Optional[int] = ..., related_review_task_count: _Optional[int] = ..., failed_gate_count: _Optional[int] = ..., fix_queue_impact_score: _Optional[float] = ..., fix_queue_total_cost_usd: _Optional[float] = ..., error_span_count: _Optional[int] = ..., has_tool_or_mcp_error: _Optional[bool] = ..., urgency_label: _Optional[str] = ..., detail_preview: _Optional[_Union[TraceInvestigationDetailPreviewV1, _Mapping]] = ..., reasons: _Optional[_Iterable[_Union[TraceInvestigationReasonV1, _Mapping]]] = ..., root_cause_candidates: _Optional[_Iterable[_Union[TraceInvestigationRootCauseCandidateV1, _Mapping]]] = ..., regression_comparisons: _Optional[_Iterable[_Union[TraceInvestigationRegressionComparisonV1, _Mapping]]] = ..., session_id: _Optional[str] = ...) -> None: ...

class TraceInvestigationSummaryV1(_message.Message):
    __slots__ = ("total_traces", "unique_customers", "unique_deployments", "feedback_hotspots", "dataset_candidates")
    TOTAL_TRACES_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_CUSTOMERS_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_HOTSPOTS_FIELD_NUMBER: _ClassVar[int]
    DATASET_CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    total_traces: int
    unique_customers: int
    unique_deployments: int
    feedback_hotspots: int
    dataset_candidates: int
    def __init__(self, total_traces: _Optional[int] = ..., unique_customers: _Optional[int] = ..., unique_deployments: _Optional[int] = ..., feedback_hotspots: _Optional[int] = ..., dataset_candidates: _Optional[int] = ...) -> None: ...

class TraceInvestigationCohortV1(_message.Message):
    __slots__ = ("label", "value", "count")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    label: str
    value: str
    count: int
    def __init__(self, label: _Optional[str] = ..., value: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class TraceInvestigationFacetRequestV1(_message.Message):
    __slots__ = ("dimension", "limit")
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    dimension: TraceInvestigationFacetDimensionV1
    limit: int
    def __init__(self, dimension: _Optional[_Union[TraceInvestigationFacetDimensionV1, str]] = ..., limit: _Optional[int] = ...) -> None: ...

class TraceInvestigationFacetValueV1(_message.Message):
    __slots__ = ("label", "value", "count", "selected")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    SELECTED_FIELD_NUMBER: _ClassVar[int]
    label: str
    value: str
    count: int
    selected: bool
    def __init__(self, label: _Optional[str] = ..., value: _Optional[str] = ..., count: _Optional[int] = ..., selected: _Optional[bool] = ...) -> None: ...

class TraceInvestigationFacetV1(_message.Message):
    __slots__ = ("dimension", "values", "other_count")
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    OTHER_COUNT_FIELD_NUMBER: _ClassVar[int]
    dimension: TraceInvestigationFacetDimensionV1
    values: _containers.RepeatedCompositeFieldContainer[TraceInvestigationFacetValueV1]
    other_count: int
    def __init__(self, dimension: _Optional[_Union[TraceInvestigationFacetDimensionV1, str]] = ..., values: _Optional[_Iterable[_Union[TraceInvestigationFacetValueV1, _Mapping]]] = ..., other_count: _Optional[int] = ...) -> None: ...

class TraceInvestigationContextV1(_message.Message):
    __slots__ = ("service", "environment", "time_range", "start", "end", "namespace")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    service: str
    environment: str
    time_range: TraceInvestigationTimeRangeV1
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    namespace: str
    def __init__(self, service: _Optional[str] = ..., environment: _Optional[str] = ..., time_range: _Optional[_Union[TraceInvestigationTimeRangeV1, _Mapping]] = ..., start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., namespace: _Optional[str] = ...) -> None: ...

class TraceInvestigationTimeRangeV1(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    def __init__(self, start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class TraceInvestigationDetailPreviewOptionsV1(_message.Message):
    __slots__ = ("row_limit_per_trace", "text_limit", "related_trace_limit", "graph_node_limit", "hydrate_content_bodies")
    ROW_LIMIT_PER_TRACE_FIELD_NUMBER: _ClassVar[int]
    TEXT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    RELATED_TRACE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    GRAPH_NODE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    HYDRATE_CONTENT_BODIES_FIELD_NUMBER: _ClassVar[int]
    row_limit_per_trace: int
    text_limit: int
    related_trace_limit: int
    graph_node_limit: int
    hydrate_content_bodies: bool
    def __init__(self, row_limit_per_trace: _Optional[int] = ..., text_limit: _Optional[int] = ..., related_trace_limit: _Optional[int] = ..., graph_node_limit: _Optional[int] = ..., hydrate_content_bodies: _Optional[bool] = ...) -> None: ...

class TraceInvestigationTraceFilterV1(_message.Message):
    __slots__ = ("key", "operator", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    operator: TraceInvestigationFilterOpV1
    value: _struct_pb2.Value
    def __init__(self, key: _Optional[str] = ..., operator: _Optional[_Union[TraceInvestigationFilterOpV1, str]] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...

class ListTraceInvestigationsRequest(_message.Message):
    __slots__ = ("context", "trace_id", "customer_id", "deployment_id", "prompt_version", "tool_version", "model_version", "mcp_method_name", "metric_name", "mode", "limit", "page_token", "include_cohort_summaries", "page", "sort_key", "sort_direction", "facets", "detail_preview_level", "session_id", "detail_preview_options", "trace_filters")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_FIELD_NUMBER: _ClassVar[int]
    TOOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
    MCP_METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_COHORT_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    SORT_KEY_FIELD_NUMBER: _ClassVar[int]
    SORT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    FACETS_FIELD_NUMBER: _ClassVar[int]
    DETAIL_PREVIEW_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    DETAIL_PREVIEW_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    TRACE_FILTERS_FIELD_NUMBER: _ClassVar[int]
    context: TraceInvestigationContextV1
    trace_id: str
    customer_id: str
    deployment_id: str
    prompt_version: str
    tool_version: str
    model_version: str
    mcp_method_name: str
    metric_name: str
    mode: InvestigationModeV1
    limit: int
    page_token: str
    include_cohort_summaries: bool
    page: _common_pb2.PageRequestV1
    sort_key: TraceInvestigationSortKeyV1
    sort_direction: _common_pb2.SortDirectionV1
    facets: _containers.RepeatedCompositeFieldContainer[TraceInvestigationFacetRequestV1]
    detail_preview_level: TraceInvestigationDetailPreviewLevelV1
    session_id: str
    detail_preview_options: TraceInvestigationDetailPreviewOptionsV1
    trace_filters: _containers.RepeatedCompositeFieldContainer[TraceInvestigationTraceFilterV1]
    def __init__(self, context: _Optional[_Union[TraceInvestigationContextV1, _Mapping]] = ..., trace_id: _Optional[str] = ..., customer_id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., prompt_version: _Optional[str] = ..., tool_version: _Optional[str] = ..., model_version: _Optional[str] = ..., mcp_method_name: _Optional[str] = ..., metric_name: _Optional[str] = ..., mode: _Optional[_Union[InvestigationModeV1, str]] = ..., limit: _Optional[int] = ..., page_token: _Optional[str] = ..., include_cohort_summaries: _Optional[bool] = ..., page: _Optional[_Union[_common_pb2.PageRequestV1, _Mapping]] = ..., sort_key: _Optional[_Union[TraceInvestigationSortKeyV1, str]] = ..., sort_direction: _Optional[_Union[_common_pb2.SortDirectionV1, str]] = ..., facets: _Optional[_Iterable[_Union[TraceInvestigationFacetRequestV1, _Mapping]]] = ..., detail_preview_level: _Optional[_Union[TraceInvestigationDetailPreviewLevelV1, str]] = ..., session_id: _Optional[str] = ..., detail_preview_options: _Optional[_Union[TraceInvestigationDetailPreviewOptionsV1, _Mapping]] = ..., trace_filters: _Optional[_Iterable[_Union[TraceInvestigationTraceFilterV1, _Mapping]]] = ...) -> None: ...

class ListTraceInvestigationsResponse(_message.Message):
    __slots__ = ("items", "summary", "top_customers", "top_deployments", "top_prompts", "next_page_token", "has_more", "total_count", "facets", "page")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    TOP_CUSTOMERS_FIELD_NUMBER: _ClassVar[int]
    TOP_DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    TOP_PROMPTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    FACETS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[TraceInvestigationRowV1]
    summary: TraceInvestigationSummaryV1
    top_customers: _containers.RepeatedCompositeFieldContainer[TraceInvestigationCohortV1]
    top_deployments: _containers.RepeatedCompositeFieldContainer[TraceInvestigationCohortV1]
    top_prompts: _containers.RepeatedCompositeFieldContainer[TraceInvestigationCohortV1]
    next_page_token: str
    has_more: bool
    total_count: int
    facets: _containers.RepeatedCompositeFieldContainer[TraceInvestigationFacetV1]
    page: _common_pb2.PageResponseV1
    def __init__(self, items: _Optional[_Iterable[_Union[TraceInvestigationRowV1, _Mapping]]] = ..., summary: _Optional[_Union[TraceInvestigationSummaryV1, _Mapping]] = ..., top_customers: _Optional[_Iterable[_Union[TraceInvestigationCohortV1, _Mapping]]] = ..., top_deployments: _Optional[_Iterable[_Union[TraceInvestigationCohortV1, _Mapping]]] = ..., top_prompts: _Optional[_Iterable[_Union[TraceInvestigationCohortV1, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., has_more: _Optional[bool] = ..., total_count: _Optional[int] = ..., facets: _Optional[_Iterable[_Union[TraceInvestigationFacetV1, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponseV1, _Mapping]] = ...) -> None: ...

class ReleaseDestinationV1(_message.Message):
    __slots__ = ("release_destination_id", "destination_key", "name", "channel_kind", "enabled", "is_default", "email_recipients", "webhook_url", "webhook_secret_ref", "headers_json", "created_by_user_id", "created_at", "updated_at")
    RELEASE_DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_KIND_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_URL_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_SECRET_REF_FIELD_NUMBER: _ClassVar[int]
    HEADERS_JSON_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    release_destination_id: str
    destination_key: str
    name: str
    channel_kind: ReleaseDestinationChannelKindV1
    enabled: bool
    is_default: bool
    email_recipients: _containers.RepeatedScalarFieldContainer[str]
    webhook_url: str
    webhook_secret_ref: str
    headers_json: _struct_pb2.Struct
    created_by_user_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, release_destination_id: _Optional[str] = ..., destination_key: _Optional[str] = ..., name: _Optional[str] = ..., channel_kind: _Optional[_Union[ReleaseDestinationChannelKindV1, str]] = ..., enabled: _Optional[bool] = ..., is_default: _Optional[bool] = ..., email_recipients: _Optional[_Iterable[str]] = ..., webhook_url: _Optional[str] = ..., webhook_secret_ref: _Optional[str] = ..., headers_json: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., created_by_user_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ReleaseAlertDeliveryV1(_message.Message):
    __slots__ = ("release_alert_delivery_id", "release_gate_id", "release_gate_evaluation_id", "release_destination_id", "channel_kind", "state", "attempts", "last_error", "last_delivered_at", "acknowledged_by_user_id", "acknowledged_at", "escalated_at", "metadata", "created_at", "updated_at")
    RELEASE_ALERT_DELIVERY_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_GATE_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_GATE_EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_KIND_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_FIELD_NUMBER: _ClassVar[int]
    LAST_DELIVERED_AT_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGED_AT_FIELD_NUMBER: _ClassVar[int]
    ESCALATED_AT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    release_alert_delivery_id: str
    release_gate_id: str
    release_gate_evaluation_id: str
    release_destination_id: str
    channel_kind: ReleaseDestinationChannelKindV1
    state: ReleaseAlertDeliveryStateV1
    attempts: int
    last_error: str
    last_delivered_at: str
    acknowledged_by_user_id: str
    acknowledged_at: str
    escalated_at: str
    metadata: _struct_pb2.Struct
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, release_alert_delivery_id: _Optional[str] = ..., release_gate_id: _Optional[str] = ..., release_gate_evaluation_id: _Optional[str] = ..., release_destination_id: _Optional[str] = ..., channel_kind: _Optional[_Union[ReleaseDestinationChannelKindV1, str]] = ..., state: _Optional[_Union[ReleaseAlertDeliveryStateV1, str]] = ..., attempts: _Optional[int] = ..., last_error: _Optional[str] = ..., last_delivered_at: _Optional[str] = ..., acknowledged_by_user_id: _Optional[str] = ..., acknowledged_at: _Optional[str] = ..., escalated_at: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class FixQueueRankingExplanationV1(_message.Message):
    __slots__ = ("recurrence_factor", "cost_factor", "blast_radius_factor", "customer_priority_factor", "failed_gate_factor", "deployment_signal_factor", "normalized_failure_rate")
    RECURRENCE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    COST_FACTOR_FIELD_NUMBER: _ClassVar[int]
    BLAST_RADIUS_FACTOR_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_PRIORITY_FACTOR_FIELD_NUMBER: _ClassVar[int]
    FAILED_GATE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_SIGNAL_FACTOR_FIELD_NUMBER: _ClassVar[int]
    NORMALIZED_FAILURE_RATE_FIELD_NUMBER: _ClassVar[int]
    recurrence_factor: float
    cost_factor: float
    blast_radius_factor: float
    customer_priority_factor: float
    failed_gate_factor: float
    deployment_signal_factor: float
    normalized_failure_rate: float
    def __init__(self, recurrence_factor: _Optional[float] = ..., cost_factor: _Optional[float] = ..., blast_radius_factor: _Optional[float] = ..., customer_priority_factor: _Optional[float] = ..., failed_gate_factor: _Optional[float] = ..., deployment_signal_factor: _Optional[float] = ..., normalized_failure_rate: _Optional[float] = ...) -> None: ...

class FixQueueItemV1(_message.Message):
    __slots__ = ("group_key", "deployment_id", "prompt_version", "model_version", "tool_version", "feature_id", "metric_name", "total_scores", "failed_scores", "failure_rate", "recurrence_count", "affected_customers", "affected_users", "total_cost_usd", "avg_confidence", "strategic_customer_hits", "failed_gate_count", "impact_score", "latest_trace_id", "ranking_explanation")
    GROUP_KEY_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
    TOOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    FEATURE_ID_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SCORES_FIELD_NUMBER: _ClassVar[int]
    FAILED_SCORES_FIELD_NUMBER: _ClassVar[int]
    FAILURE_RATE_FIELD_NUMBER: _ClassVar[int]
    RECURRENCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_CUSTOMERS_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_USERS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COST_USD_FIELD_NUMBER: _ClassVar[int]
    AVG_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    STRATEGIC_CUSTOMER_HITS_FIELD_NUMBER: _ClassVar[int]
    FAILED_GATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    IMPACT_SCORE_FIELD_NUMBER: _ClassVar[int]
    LATEST_TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    RANKING_EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    group_key: str
    deployment_id: str
    prompt_version: str
    model_version: str
    tool_version: str
    feature_id: str
    metric_name: str
    total_scores: int
    failed_scores: int
    failure_rate: float
    recurrence_count: int
    affected_customers: int
    affected_users: int
    total_cost_usd: float
    avg_confidence: float
    strategic_customer_hits: int
    failed_gate_count: int
    impact_score: float
    latest_trace_id: str
    ranking_explanation: FixQueueRankingExplanationV1
    def __init__(self, group_key: _Optional[str] = ..., deployment_id: _Optional[str] = ..., prompt_version: _Optional[str] = ..., model_version: _Optional[str] = ..., tool_version: _Optional[str] = ..., feature_id: _Optional[str] = ..., metric_name: _Optional[str] = ..., total_scores: _Optional[int] = ..., failed_scores: _Optional[int] = ..., failure_rate: _Optional[float] = ..., recurrence_count: _Optional[int] = ..., affected_customers: _Optional[int] = ..., affected_users: _Optional[int] = ..., total_cost_usd: _Optional[float] = ..., avg_confidence: _Optional[float] = ..., strategic_customer_hits: _Optional[int] = ..., failed_gate_count: _Optional[int] = ..., impact_score: _Optional[float] = ..., latest_trace_id: _Optional[str] = ..., ranking_explanation: _Optional[_Union[FixQueueRankingExplanationV1, _Mapping]] = ...) -> None: ...

class SubmitScoreRequest(_message.Message):
    __slots__ = ("metric_name", "score_value", "score_label", "explanation", "source", "evaluator_name", "evaluator_version", "evaluator_kind", "execution_trace_id", "correlation", "metadata", "occurred_at")
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    SCORE_VALUE_FIELD_NUMBER: _ClassVar[int]
    SCORE_LABEL_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_KIND_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    metric_name: str
    score_value: float
    score_label: str
    explanation: str
    source: ScoreSourceV1
    evaluator_name: str
    evaluator_version: str
    evaluator_kind: str
    execution_trace_id: str
    correlation: CorrelationContextV1
    metadata: _struct_pb2.Struct
    occurred_at: _timestamp_pb2.Timestamp
    def __init__(self, metric_name: _Optional[str] = ..., score_value: _Optional[float] = ..., score_label: _Optional[str] = ..., explanation: _Optional[str] = ..., source: _Optional[_Union[ScoreSourceV1, str]] = ..., evaluator_name: _Optional[str] = ..., evaluator_version: _Optional[str] = ..., evaluator_kind: _Optional[str] = ..., execution_trace_id: _Optional[str] = ..., correlation: _Optional[_Union[CorrelationContextV1, _Mapping]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SubmitScoreResponse(_message.Message):
    __slots__ = ("score_id", "recorded_at")
    SCORE_ID_FIELD_NUMBER: _ClassVar[int]
    RECORDED_AT_FIELD_NUMBER: _ClassVar[int]
    score_id: str
    recorded_at: _timestamp_pb2.Timestamp
    def __init__(self, score_id: _Optional[str] = ..., recorded_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SubmitFeedbackRequest(_message.Message):
    __slots__ = ("feedback_key", "rating_value", "rating_label", "comment", "correction_payload", "source_type", "reviewer_identity", "approval_status", "linked_score_id", "correlation", "metadata", "occurred_at")
    FEEDBACK_KEY_FIELD_NUMBER: _ClassVar[int]
    RATING_VALUE_FIELD_NUMBER: _ClassVar[int]
    RATING_LABEL_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    CORRECTION_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    REVIEWER_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    LINKED_SCORE_ID_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    feedback_key: str
    rating_value: float
    rating_label: str
    comment: str
    correction_payload: _struct_pb2.Struct
    source_type: FeedbackSourceTypeV1
    reviewer_identity: str
    approval_status: FeedbackApprovalStatusV1
    linked_score_id: str
    correlation: CorrelationContextV1
    metadata: _struct_pb2.Struct
    occurred_at: _timestamp_pb2.Timestamp
    def __init__(self, feedback_key: _Optional[str] = ..., rating_value: _Optional[float] = ..., rating_label: _Optional[str] = ..., comment: _Optional[str] = ..., correction_payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., source_type: _Optional[_Union[FeedbackSourceTypeV1, str]] = ..., reviewer_identity: _Optional[str] = ..., approval_status: _Optional[_Union[FeedbackApprovalStatusV1, str]] = ..., linked_score_id: _Optional[str] = ..., correlation: _Optional[_Union[CorrelationContextV1, _Mapping]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SubmitFeedbackResponse(_message.Message):
    __slots__ = ("feedback_event_id", "recorded_at")
    FEEDBACK_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    RECORDED_AT_FIELD_NUMBER: _ClassVar[int]
    feedback_event_id: str
    recorded_at: _timestamp_pb2.Timestamp
    def __init__(self, feedback_event_id: _Optional[str] = ..., recorded_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SubmitOutcomeRequest(_message.Message):
    __slots__ = ("outcome_type", "status", "numeric_value", "payload", "correlation", "occurred_at")
    OUTCOME_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_VALUE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    outcome_type: str
    status: str
    numeric_value: float
    payload: _struct_pb2.Struct
    correlation: CorrelationContextV1
    occurred_at: _timestamp_pb2.Timestamp
    def __init__(self, outcome_type: _Optional[str] = ..., status: _Optional[str] = ..., numeric_value: _Optional[float] = ..., payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., correlation: _Optional[_Union[CorrelationContextV1, _Mapping]] = ..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SubmitOutcomeResponse(_message.Message):
    __slots__ = ("outcome_event_id", "recorded_at")
    OUTCOME_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    RECORDED_AT_FIELD_NUMBER: _ClassVar[int]
    outcome_event_id: str
    recorded_at: _timestamp_pb2.Timestamp
    def __init__(self, outcome_event_id: _Optional[str] = ..., recorded_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateContentManifestRequest(_message.Message):
    __slots__ = ("content_class", "storage_uri", "storage_backend", "checksum_sha256", "size_bytes", "encryption_key_ref", "sensitivity", "retention_class", "redaction_status", "metadata", "correlation", "occurred_at")
    CONTENT_CLASS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_URI_FIELD_NUMBER: _ClassVar[int]
    STORAGE_BACKEND_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_SHA256_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_REF_FIELD_NUMBER: _ClassVar[int]
    SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    RETENTION_CLASS_FIELD_NUMBER: _ClassVar[int]
    REDACTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    content_class: str
    storage_uri: str
    storage_backend: str
    checksum_sha256: str
    size_bytes: int
    encryption_key_ref: str
    sensitivity: str
    retention_class: str
    redaction_status: str
    metadata: _struct_pb2.Struct
    correlation: CorrelationContextV1
    occurred_at: _timestamp_pb2.Timestamp
    def __init__(self, content_class: _Optional[str] = ..., storage_uri: _Optional[str] = ..., storage_backend: _Optional[str] = ..., checksum_sha256: _Optional[str] = ..., size_bytes: _Optional[int] = ..., encryption_key_ref: _Optional[str] = ..., sensitivity: _Optional[str] = ..., retention_class: _Optional[str] = ..., redaction_status: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., correlation: _Optional[_Union[CorrelationContextV1, _Mapping]] = ..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateContentManifestResponse(_message.Message):
    __slots__ = ("content_manifest_id", "recorded_at")
    CONTENT_MANIFEST_ID_FIELD_NUMBER: _ClassVar[int]
    RECORDED_AT_FIELD_NUMBER: _ClassVar[int]
    content_manifest_id: str
    recorded_at: _timestamp_pb2.Timestamp
    def __init__(self, content_manifest_id: _Optional[str] = ..., recorded_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetExecutionArtifactRefRequest(_message.Message):
    __slots__ = ("artifact_ref_id",)
    ARTIFACT_REF_ID_FIELD_NUMBER: _ClassVar[int]
    artifact_ref_id: str
    def __init__(self, artifact_ref_id: _Optional[str] = ...) -> None: ...

class GetExecutionArtifactRefResponse(_message.Message):
    __slots__ = ("artifact_ref",)
    ARTIFACT_REF_FIELD_NUMBER: _ClassVar[int]
    artifact_ref: ExecutionArtifactRefV1
    def __init__(self, artifact_ref: _Optional[_Union[ExecutionArtifactRefV1, _Mapping]] = ...) -> None: ...

class ListExecutionArtifactRefsRequest(_message.Message):
    __slots__ = ("eval_job_id", "experiment_run_id", "experiment_run_item_id", "score_id", "artifact_role", "limit", "offset")
    EVAL_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_RUN_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_ID_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_ROLE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    eval_job_id: str
    experiment_run_id: str
    experiment_run_item_id: str
    score_id: str
    artifact_role: str
    limit: int
    offset: int
    def __init__(self, eval_job_id: _Optional[str] = ..., experiment_run_id: _Optional[str] = ..., experiment_run_item_id: _Optional[str] = ..., score_id: _Optional[str] = ..., artifact_role: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListExecutionArtifactRefsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ExecutionArtifactRefV1]
    def __init__(self, items: _Optional[_Iterable[_Union[ExecutionArtifactRefV1, _Mapping]]] = ...) -> None: ...

class GetExecutionArtifactContentRequest(_message.Message):
    __slots__ = ("artifact_ref_id", "max_bytes")
    ARTIFACT_REF_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_BYTES_FIELD_NUMBER: _ClassVar[int]
    artifact_ref_id: str
    max_bytes: int
    def __init__(self, artifact_ref_id: _Optional[str] = ..., max_bytes: _Optional[int] = ...) -> None: ...

class GetExecutionArtifactContentResponse(_message.Message):
    __slots__ = ("artifact_ref", "content_text", "resolved_url", "content_bytes", "truncated")
    ARTIFACT_REF_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TEXT_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_URL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_BYTES_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    artifact_ref: ExecutionArtifactRefV1
    content_text: str
    resolved_url: str
    content_bytes: int
    truncated: bool
    def __init__(self, artifact_ref: _Optional[_Union[ExecutionArtifactRefV1, _Mapping]] = ..., content_text: _Optional[str] = ..., resolved_url: _Optional[str] = ..., content_bytes: _Optional[int] = ..., truncated: _Optional[bool] = ...) -> None: ...

class ResolveExecutionArtifactUrlRequest(_message.Message):
    __slots__ = ("artifact_ref_id",)
    ARTIFACT_REF_ID_FIELD_NUMBER: _ClassVar[int]
    artifact_ref_id: str
    def __init__(self, artifact_ref_id: _Optional[str] = ...) -> None: ...

class ResolveExecutionArtifactUrlResponse(_message.Message):
    __slots__ = ("artifact_ref", "resolved_url")
    ARTIFACT_REF_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_URL_FIELD_NUMBER: _ClassVar[int]
    artifact_ref: ExecutionArtifactRefV1
    resolved_url: str
    def __init__(self, artifact_ref: _Optional[_Union[ExecutionArtifactRefV1, _Mapping]] = ..., resolved_url: _Optional[str] = ...) -> None: ...

class CompareExecutionArtifactsRequest(_message.Message):
    __slots__ = ("baseline_scope", "comparison_scope")
    BASELINE_SCOPE_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_SCOPE_FIELD_NUMBER: _ClassVar[int]
    baseline_scope: ExecutionArtifactScopeV1
    comparison_scope: ExecutionArtifactScopeV1
    def __init__(self, baseline_scope: _Optional[_Union[ExecutionArtifactScopeV1, _Mapping]] = ..., comparison_scope: _Optional[_Union[ExecutionArtifactScopeV1, _Mapping]] = ...) -> None: ...

class CompareExecutionArtifactsResponse(_message.Message):
    __slots__ = ("comparison",)
    COMPARISON_FIELD_NUMBER: _ClassVar[int]
    comparison: ExecutionArtifactComparisonV1
    def __init__(self, comparison: _Optional[_Union[ExecutionArtifactComparisonV1, _Mapping]] = ...) -> None: ...

class PromoteDatasetItemRequest(_message.Message):
    __slots__ = ("collection_name", "collection_description", "target_version_id", "version_label", "source_kind", "correlation", "input_payload", "expected_output", "correction_payload", "evaluator_snapshot", "original_context", "tags", "rationale", "split")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TARGET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_LABEL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_FIELD_NUMBER: _ClassVar[int]
    INPUT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    CORRECTION_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    RATIONALE_FIELD_NUMBER: _ClassVar[int]
    SPLIT_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    collection_description: str
    target_version_id: str
    version_label: str
    source_kind: DatasetItemSourceKindV1
    correlation: CorrelationContextV1
    input_payload: _struct_pb2.Struct
    expected_output: _struct_pb2.Struct
    correction_payload: _struct_pb2.Struct
    evaluator_snapshot: _struct_pb2.Struct
    original_context: _struct_pb2.Struct
    tags: _containers.RepeatedScalarFieldContainer[str]
    rationale: str
    split: DatasetItemSplitV1
    def __init__(self, collection_name: _Optional[str] = ..., collection_description: _Optional[str] = ..., target_version_id: _Optional[str] = ..., version_label: _Optional[str] = ..., source_kind: _Optional[_Union[DatasetItemSourceKindV1, str]] = ..., correlation: _Optional[_Union[CorrelationContextV1, _Mapping]] = ..., input_payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., expected_output: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., correction_payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., evaluator_snapshot: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., original_context: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., tags: _Optional[_Iterable[str]] = ..., rationale: _Optional[str] = ..., split: _Optional[_Union[DatasetItemSplitV1, str]] = ...) -> None: ...

class PromoteDatasetItemResponse(_message.Message):
    __slots__ = ("collection_id", "version_id", "version_number", "item_id", "recorded_at")
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    RECORDED_AT_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    version_id: str
    version_number: int
    item_id: str
    recorded_at: _timestamp_pb2.Timestamp
    def __init__(self, collection_id: _Optional[str] = ..., version_id: _Optional[str] = ..., version_number: _Optional[int] = ..., item_id: _Optional[str] = ..., recorded_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DatasetCollectionV1(_message.Message):
    __slots__ = ("collection_id", "name", "description", "labels", "created_by_user_id", "created_at", "updated_at", "total_versions", "total_items", "latest_version_id", "latest_version_number", "latest_version_label", "is_archived", "archived_at", "archived_by_user_id", "usage_summary")
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ITEMS_FIELD_NUMBER: _ClassVar[int]
    LATEST_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    LATEST_VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LATEST_VERSION_LABEL_FIELD_NUMBER: _ClassVar[int]
    IS_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_AT_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    USAGE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    name: str
    description: str
    labels: _struct_pb2.Struct
    created_by_user_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    total_versions: int
    total_items: int
    latest_version_id: str
    latest_version_number: int
    latest_version_label: str
    is_archived: bool
    archived_at: _timestamp_pb2.Timestamp
    archived_by_user_id: str
    usage_summary: DatasetUsageSummaryV1
    def __init__(self, collection_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., labels: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., created_by_user_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., total_versions: _Optional[int] = ..., total_items: _Optional[int] = ..., latest_version_id: _Optional[str] = ..., latest_version_number: _Optional[int] = ..., latest_version_label: _Optional[str] = ..., is_archived: _Optional[bool] = ..., archived_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., archived_by_user_id: _Optional[str] = ..., usage_summary: _Optional[_Union[DatasetUsageSummaryV1, _Mapping]] = ...) -> None: ...

class DatasetVersionV1(_message.Message):
    __slots__ = ("version_id", "collection_id", "version_number", "label", "is_pinned", "pinned_reason", "pinned_by_user_id", "pinned_at", "created_at", "item_count", "base_version_id", "usage_summary")
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    IS_PINNED_FIELD_NUMBER: _ClassVar[int]
    PINNED_REASON_FIELD_NUMBER: _ClassVar[int]
    PINNED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    PINNED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    BASE_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    USAGE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    version_id: str
    collection_id: str
    version_number: int
    label: str
    is_pinned: bool
    pinned_reason: str
    pinned_by_user_id: str
    pinned_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    item_count: int
    base_version_id: str
    usage_summary: DatasetUsageSummaryV1
    def __init__(self, version_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., version_number: _Optional[int] = ..., label: _Optional[str] = ..., is_pinned: _Optional[bool] = ..., pinned_reason: _Optional[str] = ..., pinned_by_user_id: _Optional[str] = ..., pinned_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., item_count: _Optional[int] = ..., base_version_id: _Optional[str] = ..., usage_summary: _Optional[_Union[DatasetUsageSummaryV1, _Mapping]] = ...) -> None: ...

class DatasetUsageSummaryV1(_message.Message):
    __slots__ = ("experiment_input_count", "experiment_run_count", "release_gate_count", "regressions_since_version_count", "latest_experiment_input_id", "latest_experiment_run_id")
    EXPERIMENT_INPUT_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    RELEASE_GATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    REGRESSIONS_SINCE_VERSION_COUNT_FIELD_NUMBER: _ClassVar[int]
    LATEST_EXPERIMENT_INPUT_ID_FIELD_NUMBER: _ClassVar[int]
    LATEST_EXPERIMENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    experiment_input_count: int
    experiment_run_count: int
    release_gate_count: int
    regressions_since_version_count: int
    latest_experiment_input_id: str
    latest_experiment_run_id: str
    def __init__(self, experiment_input_count: _Optional[int] = ..., experiment_run_count: _Optional[int] = ..., release_gate_count: _Optional[int] = ..., regressions_since_version_count: _Optional[int] = ..., latest_experiment_input_id: _Optional[str] = ..., latest_experiment_run_id: _Optional[str] = ...) -> None: ...

class DatasetItemV1(_message.Message):
    __slots__ = ("item_id", "version_id", "collection_id", "source_kind", "source_feedback_event_id", "source_outcome_event_id", "source_score_id", "source_annotation_task_id", "correlation", "input_payload", "expected_output", "correction_payload", "evaluator_snapshot", "original_context", "reviewer_user_id", "reviewer_identity", "reviewed_at", "tags", "rationale", "promoted_by_user_id", "created_at", "derived_from_item_id", "split", "source_session_id")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FEEDBACK_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_OUTCOME_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SCORE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ANNOTATION_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_FIELD_NUMBER: _ClassVar[int]
    INPUT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    CORRECTION_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REVIEWER_USER_ID_FIELD_NUMBER: _ClassVar[int]
    REVIEWER_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    REVIEWED_AT_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    RATIONALE_FIELD_NUMBER: _ClassVar[int]
    PROMOTED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DERIVED_FROM_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    SPLIT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    item_id: str
    version_id: str
    collection_id: str
    source_kind: DatasetItemSourceKindV1
    source_feedback_event_id: str
    source_outcome_event_id: str
    source_score_id: str
    source_annotation_task_id: str
    correlation: CorrelationContextV1
    input_payload: _struct_pb2.Struct
    expected_output: _struct_pb2.Struct
    correction_payload: _struct_pb2.Struct
    evaluator_snapshot: _struct_pb2.Struct
    original_context: _struct_pb2.Struct
    reviewer_user_id: str
    reviewer_identity: str
    reviewed_at: _timestamp_pb2.Timestamp
    tags: _containers.RepeatedScalarFieldContainer[str]
    rationale: str
    promoted_by_user_id: str
    created_at: _timestamp_pb2.Timestamp
    derived_from_item_id: str
    split: DatasetItemSplitV1
    source_session_id: str
    def __init__(self, item_id: _Optional[str] = ..., version_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., source_kind: _Optional[_Union[DatasetItemSourceKindV1, str]] = ..., source_feedback_event_id: _Optional[str] = ..., source_outcome_event_id: _Optional[str] = ..., source_score_id: _Optional[str] = ..., source_annotation_task_id: _Optional[str] = ..., correlation: _Optional[_Union[CorrelationContextV1, _Mapping]] = ..., input_payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., expected_output: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., correction_payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., evaluator_snapshot: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., original_context: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., reviewer_user_id: _Optional[str] = ..., reviewer_identity: _Optional[str] = ..., reviewed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tags: _Optional[_Iterable[str]] = ..., rationale: _Optional[str] = ..., promoted_by_user_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., derived_from_item_id: _Optional[str] = ..., split: _Optional[_Union[DatasetItemSplitV1, str]] = ..., source_session_id: _Optional[str] = ...) -> None: ...

class ListDatasetCollectionsRequest(_message.Message):
    __slots__ = ("limit", "offset", "include_archived")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    include_archived: bool
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., include_archived: _Optional[bool] = ...) -> None: ...

class ListDatasetCollectionsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[DatasetCollectionV1]
    def __init__(self, items: _Optional[_Iterable[_Union[DatasetCollectionV1, _Mapping]]] = ...) -> None: ...

class GetDatasetCollectionRequest(_message.Message):
    __slots__ = ("collection_id",)
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    def __init__(self, collection_id: _Optional[str] = ...) -> None: ...

class GetDatasetCollectionResponse(_message.Message):
    __slots__ = ("collection", "versions")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    collection: DatasetCollectionV1
    versions: _containers.RepeatedCompositeFieldContainer[DatasetVersionV1]
    def __init__(self, collection: _Optional[_Union[DatasetCollectionV1, _Mapping]] = ..., versions: _Optional[_Iterable[_Union[DatasetVersionV1, _Mapping]]] = ...) -> None: ...

class ListDatasetVersionsRequest(_message.Message):
    __slots__ = ("collection_id", "collection_name", "limit", "offset")
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    collection_name: str
    limit: int
    offset: int
    def __init__(self, collection_id: _Optional[str] = ..., collection_name: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListDatasetVersionsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[DatasetVersionV1]
    def __init__(self, items: _Optional[_Iterable[_Union[DatasetVersionV1, _Mapping]]] = ...) -> None: ...

class GetDatasetVersionRequest(_message.Message):
    __slots__ = ("version_id",)
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    version_id: str
    def __init__(self, version_id: _Optional[str] = ...) -> None: ...

class GetDatasetVersionResponse(_message.Message):
    __slots__ = ("collection", "version")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    collection: DatasetCollectionV1
    version: DatasetVersionV1
    def __init__(self, collection: _Optional[_Union[DatasetCollectionV1, _Mapping]] = ..., version: _Optional[_Union[DatasetVersionV1, _Mapping]] = ...) -> None: ...

class ListDatasetItemsRequest(_message.Message):
    __slots__ = ("collection_id", "version_id", "source_kind", "limit", "offset", "split")
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SPLIT_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    version_id: str
    source_kind: DatasetItemSourceKindV1
    limit: int
    offset: int
    split: DatasetItemSplitV1
    def __init__(self, collection_id: _Optional[str] = ..., version_id: _Optional[str] = ..., source_kind: _Optional[_Union[DatasetItemSourceKindV1, str]] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ..., split: _Optional[_Union[DatasetItemSplitV1, str]] = ...) -> None: ...

class ListDatasetItemsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[DatasetItemV1]
    def __init__(self, items: _Optional[_Iterable[_Union[DatasetItemV1, _Mapping]]] = ...) -> None: ...

class GetDatasetItemRequest(_message.Message):
    __slots__ = ("item_id",)
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    item_id: str
    def __init__(self, item_id: _Optional[str] = ...) -> None: ...

class GetDatasetItemResponse(_message.Message):
    __slots__ = ("collection", "version", "item")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    collection: DatasetCollectionV1
    version: DatasetVersionV1
    item: DatasetItemV1
    def __init__(self, collection: _Optional[_Union[DatasetCollectionV1, _Mapping]] = ..., version: _Optional[_Union[DatasetVersionV1, _Mapping]] = ..., item: _Optional[_Union[DatasetItemV1, _Mapping]] = ...) -> None: ...

class StringFieldPatchV1(_message.Message):
    __slots__ = ("value", "clear")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CLEAR_FIELD_NUMBER: _ClassVar[int]
    value: str
    clear: bool
    def __init__(self, value: _Optional[str] = ..., clear: _Optional[bool] = ...) -> None: ...

class StructFieldPatchV1(_message.Message):
    __slots__ = ("value", "clear")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CLEAR_FIELD_NUMBER: _ClassVar[int]
    value: _struct_pb2.Struct
    clear: bool
    def __init__(self, value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., clear: _Optional[bool] = ...) -> None: ...

class UpdateDatasetCollectionRequest(_message.Message):
    __slots__ = ("collection_id", "name", "description", "labels")
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    name: StringFieldPatchV1
    description: StringFieldPatchV1
    labels: StructFieldPatchV1
    def __init__(self, collection_id: _Optional[str] = ..., name: _Optional[_Union[StringFieldPatchV1, _Mapping]] = ..., description: _Optional[_Union[StringFieldPatchV1, _Mapping]] = ..., labels: _Optional[_Union[StructFieldPatchV1, _Mapping]] = ...) -> None: ...

class UpdateDatasetCollectionResponse(_message.Message):
    __slots__ = ("collection",)
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: DatasetCollectionV1
    def __init__(self, collection: _Optional[_Union[DatasetCollectionV1, _Mapping]] = ...) -> None: ...

class CreateDatasetVersionRequest(_message.Message):
    __slots__ = ("collection_id", "label", "base_version_id")
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    BASE_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    label: str
    base_version_id: str
    def __init__(self, collection_id: _Optional[str] = ..., label: _Optional[str] = ..., base_version_id: _Optional[str] = ...) -> None: ...

class CreateDatasetVersionResponse(_message.Message):
    __slots__ = ("collection", "version", "copied_item_count")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    COPIED_ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    collection: DatasetCollectionV1
    version: DatasetVersionV1
    copied_item_count: int
    def __init__(self, collection: _Optional[_Union[DatasetCollectionV1, _Mapping]] = ..., version: _Optional[_Union[DatasetVersionV1, _Mapping]] = ..., copied_item_count: _Optional[int] = ...) -> None: ...

class CreateDatasetItemRequest(_message.Message):
    __slots__ = ("collection_id", "collection_name", "collection_description", "target_version_id", "version_label", "source_kind", "correlation", "input_payload", "expected_output", "correction_payload", "evaluator_snapshot", "original_context", "tags", "rationale", "split")
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TARGET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_LABEL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_FIELD_NUMBER: _ClassVar[int]
    INPUT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    CORRECTION_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    RATIONALE_FIELD_NUMBER: _ClassVar[int]
    SPLIT_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    collection_name: str
    collection_description: str
    target_version_id: str
    version_label: str
    source_kind: DatasetItemSourceKindV1
    correlation: CorrelationContextV1
    input_payload: _struct_pb2.Struct
    expected_output: _struct_pb2.Struct
    correction_payload: _struct_pb2.Struct
    evaluator_snapshot: _struct_pb2.Struct
    original_context: _struct_pb2.Struct
    tags: _containers.RepeatedScalarFieldContainer[str]
    rationale: str
    split: DatasetItemSplitV1
    def __init__(self, collection_id: _Optional[str] = ..., collection_name: _Optional[str] = ..., collection_description: _Optional[str] = ..., target_version_id: _Optional[str] = ..., version_label: _Optional[str] = ..., source_kind: _Optional[_Union[DatasetItemSourceKindV1, str]] = ..., correlation: _Optional[_Union[CorrelationContextV1, _Mapping]] = ..., input_payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., expected_output: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., correction_payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., evaluator_snapshot: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., original_context: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., tags: _Optional[_Iterable[str]] = ..., rationale: _Optional[str] = ..., split: _Optional[_Union[DatasetItemSplitV1, str]] = ...) -> None: ...

class CreateDatasetItemResponse(_message.Message):
    __slots__ = ("collection", "version", "item")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    collection: DatasetCollectionV1
    version: DatasetVersionV1
    item: DatasetItemV1
    def __init__(self, collection: _Optional[_Union[DatasetCollectionV1, _Mapping]] = ..., version: _Optional[_Union[DatasetVersionV1, _Mapping]] = ..., item: _Optional[_Union[DatasetItemV1, _Mapping]] = ...) -> None: ...

class UpdateDatasetItemRequest(_message.Message):
    __slots__ = ("item_id", "version_label", "input_payload", "expected_output", "correction_payload", "evaluator_snapshot", "original_context", "tags", "replace_tags", "rationale", "split")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_LABEL_FIELD_NUMBER: _ClassVar[int]
    INPUT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    CORRECTION_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    REPLACE_TAGS_FIELD_NUMBER: _ClassVar[int]
    RATIONALE_FIELD_NUMBER: _ClassVar[int]
    SPLIT_FIELD_NUMBER: _ClassVar[int]
    item_id: str
    version_label: str
    input_payload: StructFieldPatchV1
    expected_output: StructFieldPatchV1
    correction_payload: StructFieldPatchV1
    evaluator_snapshot: StructFieldPatchV1
    original_context: StructFieldPatchV1
    tags: _containers.RepeatedScalarFieldContainer[str]
    replace_tags: bool
    rationale: StringFieldPatchV1
    split: DatasetItemSplitV1
    def __init__(self, item_id: _Optional[str] = ..., version_label: _Optional[str] = ..., input_payload: _Optional[_Union[StructFieldPatchV1, _Mapping]] = ..., expected_output: _Optional[_Union[StructFieldPatchV1, _Mapping]] = ..., correction_payload: _Optional[_Union[StructFieldPatchV1, _Mapping]] = ..., evaluator_snapshot: _Optional[_Union[StructFieldPatchV1, _Mapping]] = ..., original_context: _Optional[_Union[StructFieldPatchV1, _Mapping]] = ..., tags: _Optional[_Iterable[str]] = ..., replace_tags: _Optional[bool] = ..., rationale: _Optional[_Union[StringFieldPatchV1, _Mapping]] = ..., split: _Optional[_Union[DatasetItemSplitV1, str]] = ...) -> None: ...

class UpdateDatasetItemResponse(_message.Message):
    __slots__ = ("collection", "version", "previous_item", "item")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_ITEM_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    collection: DatasetCollectionV1
    version: DatasetVersionV1
    previous_item: DatasetItemV1
    item: DatasetItemV1
    def __init__(self, collection: _Optional[_Union[DatasetCollectionV1, _Mapping]] = ..., version: _Optional[_Union[DatasetVersionV1, _Mapping]] = ..., previous_item: _Optional[_Union[DatasetItemV1, _Mapping]] = ..., item: _Optional[_Union[DatasetItemV1, _Mapping]] = ...) -> None: ...

class DeleteDatasetItemRequest(_message.Message):
    __slots__ = ("item_id", "version_label")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_LABEL_FIELD_NUMBER: _ClassVar[int]
    item_id: str
    version_label: str
    def __init__(self, item_id: _Optional[str] = ..., version_label: _Optional[str] = ...) -> None: ...

class DeleteDatasetItemResponse(_message.Message):
    __slots__ = ("collection", "version", "deleted_item_id")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DELETED_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    collection: DatasetCollectionV1
    version: DatasetVersionV1
    deleted_item_id: str
    def __init__(self, collection: _Optional[_Union[DatasetCollectionV1, _Mapping]] = ..., version: _Optional[_Union[DatasetVersionV1, _Mapping]] = ..., deleted_item_id: _Optional[str] = ...) -> None: ...

class MoveDatasetItemRequest(_message.Message):
    __slots__ = ("item_id", "target_version_id")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    item_id: str
    target_version_id: str
    def __init__(self, item_id: _Optional[str] = ..., target_version_id: _Optional[str] = ...) -> None: ...

class MoveDatasetItemResponse(_message.Message):
    __slots__ = ("source_collection", "source_version", "target_collection", "target_version", "item")
    SOURCE_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    TARGET_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    TARGET_VERSION_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    source_collection: DatasetCollectionV1
    source_version: DatasetVersionV1
    target_collection: DatasetCollectionV1
    target_version: DatasetVersionV1
    item: DatasetItemV1
    def __init__(self, source_collection: _Optional[_Union[DatasetCollectionV1, _Mapping]] = ..., source_version: _Optional[_Union[DatasetVersionV1, _Mapping]] = ..., target_collection: _Optional[_Union[DatasetCollectionV1, _Mapping]] = ..., target_version: _Optional[_Union[DatasetVersionV1, _Mapping]] = ..., item: _Optional[_Union[DatasetItemV1, _Mapping]] = ...) -> None: ...

class ArchiveDatasetCollectionRequest(_message.Message):
    __slots__ = ("collection_id",)
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    def __init__(self, collection_id: _Optional[str] = ...) -> None: ...

class ArchiveDatasetCollectionResponse(_message.Message):
    __slots__ = ("collection",)
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: DatasetCollectionV1
    def __init__(self, collection: _Optional[_Union[DatasetCollectionV1, _Mapping]] = ...) -> None: ...

class UnarchiveDatasetCollectionRequest(_message.Message):
    __slots__ = ("collection_id",)
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    def __init__(self, collection_id: _Optional[str] = ...) -> None: ...

class UnarchiveDatasetCollectionResponse(_message.Message):
    __slots__ = ("collection",)
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: DatasetCollectionV1
    def __init__(self, collection: _Optional[_Union[DatasetCollectionV1, _Mapping]] = ...) -> None: ...

class DatasetImportRowFailureV1(_message.Message):
    __slots__ = ("row_number", "fields", "message")
    ROW_NUMBER_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    row_number: int
    fields: _containers.RepeatedScalarFieldContainer[str]
    message: str
    def __init__(self, row_number: _Optional[int] = ..., fields: _Optional[_Iterable[str]] = ..., message: _Optional[str] = ...) -> None: ...

class ImportDatasetFileRequest(_message.Message):
    __slots__ = ("collection_id", "collection_name", "collection_description", "target_version_id", "version_label", "format", "file_name", "file_bytes", "field_mappings", "default_source_kind", "content_type", "default_split")
    class FieldMappingsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TARGET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_LABEL_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_BYTES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SPLIT_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    collection_name: str
    collection_description: str
    target_version_id: str
    version_label: str
    format: DatasetImportFormatV1
    file_name: str
    file_bytes: bytes
    field_mappings: _containers.ScalarMap[str, str]
    default_source_kind: DatasetItemSourceKindV1
    content_type: str
    default_split: DatasetItemSplitV1
    def __init__(self, collection_id: _Optional[str] = ..., collection_name: _Optional[str] = ..., collection_description: _Optional[str] = ..., target_version_id: _Optional[str] = ..., version_label: _Optional[str] = ..., format: _Optional[_Union[DatasetImportFormatV1, str]] = ..., file_name: _Optional[str] = ..., file_bytes: _Optional[bytes] = ..., field_mappings: _Optional[_Mapping[str, str]] = ..., default_source_kind: _Optional[_Union[DatasetItemSourceKindV1, str]] = ..., content_type: _Optional[str] = ..., default_split: _Optional[_Union[DatasetItemSplitV1, str]] = ...) -> None: ...

class ExportDatasetVersionRequest(_message.Message):
    __slots__ = ("version_id", "format")
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    version_id: str
    format: DatasetExportFormatV1
    def __init__(self, version_id: _Optional[str] = ..., format: _Optional[_Union[DatasetExportFormatV1, str]] = ...) -> None: ...

class ExportDatasetVersionResponse(_message.Message):
    __slots__ = ("collection", "version", "file_name", "content_type", "file_bytes", "item_count")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_BYTES_FIELD_NUMBER: _ClassVar[int]
    ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    collection: DatasetCollectionV1
    version: DatasetVersionV1
    file_name: str
    content_type: str
    file_bytes: bytes
    item_count: int
    def __init__(self, collection: _Optional[_Union[DatasetCollectionV1, _Mapping]] = ..., version: _Optional[_Union[DatasetVersionV1, _Mapping]] = ..., file_name: _Optional[str] = ..., content_type: _Optional[str] = ..., file_bytes: _Optional[bytes] = ..., item_count: _Optional[int] = ...) -> None: ...

class ImportDatasetFileResponse(_message.Message):
    __slots__ = ("collection", "version", "total_rows", "imported_rows", "applied", "row_failures")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ROWS_FIELD_NUMBER: _ClassVar[int]
    IMPORTED_ROWS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    ROW_FAILURES_FIELD_NUMBER: _ClassVar[int]
    collection: DatasetCollectionV1
    version: DatasetVersionV1
    total_rows: int
    imported_rows: int
    applied: bool
    row_failures: _containers.RepeatedCompositeFieldContainer[DatasetImportRowFailureV1]
    def __init__(self, collection: _Optional[_Union[DatasetCollectionV1, _Mapping]] = ..., version: _Optional[_Union[DatasetVersionV1, _Mapping]] = ..., total_rows: _Optional[int] = ..., imported_rows: _Optional[int] = ..., applied: _Optional[bool] = ..., row_failures: _Optional[_Iterable[_Union[DatasetImportRowFailureV1, _Mapping]]] = ...) -> None: ...

class PromoteApprovedAnnotationTaskRequest(_message.Message):
    __slots__ = ("task_id", "collection_name", "collection_description", "target_version_id", "version_label", "source_kind", "input_payload", "expected_output", "evaluator_snapshot", "original_context", "tags", "rationale", "split")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TARGET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_LABEL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
    INPUT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    RATIONALE_FIELD_NUMBER: _ClassVar[int]
    SPLIT_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    collection_name: str
    collection_description: str
    target_version_id: str
    version_label: str
    source_kind: DatasetItemSourceKindV1
    input_payload: _struct_pb2.Struct
    expected_output: _struct_pb2.Struct
    evaluator_snapshot: _struct_pb2.Struct
    original_context: _struct_pb2.Struct
    tags: _containers.RepeatedScalarFieldContainer[str]
    rationale: str
    split: DatasetItemSplitV1
    def __init__(self, task_id: _Optional[str] = ..., collection_name: _Optional[str] = ..., collection_description: _Optional[str] = ..., target_version_id: _Optional[str] = ..., version_label: _Optional[str] = ..., source_kind: _Optional[_Union[DatasetItemSourceKindV1, str]] = ..., input_payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., expected_output: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., evaluator_snapshot: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., original_context: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., tags: _Optional[_Iterable[str]] = ..., rationale: _Optional[str] = ..., split: _Optional[_Union[DatasetItemSplitV1, str]] = ...) -> None: ...

class ExperimentInputV1(_message.Message):
    __slots__ = ("input_id", "input_key", "name", "description", "dataset_collection_id", "dataset_version_id", "metadata", "created_by_user_id", "created_at")
    INPUT_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    input_id: str
    input_key: str
    name: str
    description: str
    dataset_collection_id: str
    dataset_version_id: str
    metadata: _struct_pb2.Struct
    created_by_user_id: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, input_id: _Optional[str] = ..., input_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., dataset_collection_id: _Optional[str] = ..., dataset_version_id: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., created_by_user_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreatePromptTemplateRequest(_message.Message):
    __slots__ = ("template_key", "name", "description", "labels")
    TEMPLATE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    template_key: str
    name: str
    description: str
    labels: _struct_pb2.Struct
    def __init__(self, template_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., labels: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class CreatePromptTemplateResponse(_message.Message):
    __slots__ = ("prompt_template",)
    PROMPT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    prompt_template: PromptTemplateV1
    def __init__(self, prompt_template: _Optional[_Union[PromptTemplateV1, _Mapping]] = ...) -> None: ...

class GetPromptTemplateRequest(_message.Message):
    __slots__ = ("prompt_template_id",)
    PROMPT_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    prompt_template_id: str
    def __init__(self, prompt_template_id: _Optional[str] = ...) -> None: ...

class GetPromptTemplateResponse(_message.Message):
    __slots__ = ("prompt_template",)
    PROMPT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    prompt_template: PromptTemplateV1
    def __init__(self, prompt_template: _Optional[_Union[PromptTemplateV1, _Mapping]] = ...) -> None: ...

class ListPromptTemplatesRequest(_message.Message):
    __slots__ = ("include_archived", "limit", "offset")
    INCLUDE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    include_archived: bool
    limit: int
    offset: int
    def __init__(self, include_archived: _Optional[bool] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListPromptTemplatesResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PromptTemplateV1]
    def __init__(self, items: _Optional[_Iterable[_Union[PromptTemplateV1, _Mapping]]] = ...) -> None: ...

class UpdatePromptTemplateRequest(_message.Message):
    __slots__ = ("prompt_template_id", "template_key", "name", "description", "labels")
    PROMPT_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    prompt_template_id: str
    template_key: str
    name: str
    description: str
    labels: _struct_pb2.Struct
    def __init__(self, prompt_template_id: _Optional[str] = ..., template_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., labels: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class UpdatePromptTemplateResponse(_message.Message):
    __slots__ = ("prompt_template",)
    PROMPT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    prompt_template: PromptTemplateV1
    def __init__(self, prompt_template: _Optional[_Union[PromptTemplateV1, _Mapping]] = ...) -> None: ...

class DeletePromptTemplateRequest(_message.Message):
    __slots__ = ("prompt_template_id",)
    PROMPT_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    prompt_template_id: str
    def __init__(self, prompt_template_id: _Optional[str] = ...) -> None: ...

class DeletePromptTemplateResponse(_message.Message):
    __slots__ = ("prompt_template_id",)
    PROMPT_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    prompt_template_id: str
    def __init__(self, prompt_template_id: _Optional[str] = ...) -> None: ...

class CreatePromptVersionRequest(_message.Message):
    __slots__ = ("prompt_template_id", "version_label", "environments", "prompt_text", "system_prompt", "metadata")
    PROMPT_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_LABEL_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TEXT_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_PROMPT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    prompt_template_id: str
    version_label: str
    environments: _containers.RepeatedScalarFieldContainer[PromptEnvironmentV1]
    prompt_text: str
    system_prompt: str
    metadata: _struct_pb2.Struct
    def __init__(self, prompt_template_id: _Optional[str] = ..., version_label: _Optional[str] = ..., environments: _Optional[_Iterable[_Union[PromptEnvironmentV1, str]]] = ..., prompt_text: _Optional[str] = ..., system_prompt: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class CreatePromptVersionResponse(_message.Message):
    __slots__ = ("prompt_version",)
    PROMPT_VERSION_FIELD_NUMBER: _ClassVar[int]
    prompt_version: PromptVersionV1
    def __init__(self, prompt_version: _Optional[_Union[PromptVersionV1, _Mapping]] = ...) -> None: ...

class GetPromptVersionRequest(_message.Message):
    __slots__ = ("prompt_version_id",)
    PROMPT_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    prompt_version_id: str
    def __init__(self, prompt_version_id: _Optional[str] = ...) -> None: ...

class GetPromptVersionResponse(_message.Message):
    __slots__ = ("prompt_version",)
    PROMPT_VERSION_FIELD_NUMBER: _ClassVar[int]
    prompt_version: PromptVersionV1
    def __init__(self, prompt_version: _Optional[_Union[PromptVersionV1, _Mapping]] = ...) -> None: ...

class ListPromptVersionsRequest(_message.Message):
    __slots__ = ("prompt_template_id", "include_archived", "limit", "offset")
    PROMPT_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    prompt_template_id: str
    include_archived: bool
    limit: int
    offset: int
    def __init__(self, prompt_template_id: _Optional[str] = ..., include_archived: _Optional[bool] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListPromptVersionsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PromptVersionV1]
    def __init__(self, items: _Optional[_Iterable[_Union[PromptVersionV1, _Mapping]]] = ...) -> None: ...

class UpdatePromptVersionRequest(_message.Message):
    __slots__ = ("prompt_version_id", "version_label", "environments", "prompt_text", "system_prompt", "metadata")
    PROMPT_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_LABEL_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TEXT_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_PROMPT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    prompt_version_id: str
    version_label: str
    environments: _containers.RepeatedScalarFieldContainer[PromptEnvironmentV1]
    prompt_text: str
    system_prompt: str
    metadata: _struct_pb2.Struct
    def __init__(self, prompt_version_id: _Optional[str] = ..., version_label: _Optional[str] = ..., environments: _Optional[_Iterable[_Union[PromptEnvironmentV1, str]]] = ..., prompt_text: _Optional[str] = ..., system_prompt: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class UpdatePromptVersionResponse(_message.Message):
    __slots__ = ("prompt_version",)
    PROMPT_VERSION_FIELD_NUMBER: _ClassVar[int]
    prompt_version: PromptVersionV1
    def __init__(self, prompt_version: _Optional[_Union[PromptVersionV1, _Mapping]] = ...) -> None: ...

class DeletePromptVersionRequest(_message.Message):
    __slots__ = ("prompt_version_id",)
    PROMPT_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    prompt_version_id: str
    def __init__(self, prompt_version_id: _Optional[str] = ...) -> None: ...

class DeletePromptVersionResponse(_message.Message):
    __slots__ = ("prompt_version_id",)
    PROMPT_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    prompt_version_id: str
    def __init__(self, prompt_version_id: _Optional[str] = ...) -> None: ...

class ExperimentTargetV1(_message.Message):
    __slots__ = ("target_id", "target_key", "name", "target_mode", "config", "provider_execution", "prompt_template", "prompt_version", "prompt_label", "created_by_user_id", "created_at", "updated_at", "prompt_template_id", "prompt_version_id", "is_archived", "archived_at", "archived_by_user_id")
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_MODE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROMPT_LABEL_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_AT_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    target_id: str
    target_key: str
    name: str
    target_mode: ExperimentTargetModeV1
    config: _struct_pb2.Struct
    provider_execution: ProviderExecutionConfigV1
    prompt_template: str
    prompt_version: str
    prompt_label: str
    created_by_user_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    prompt_template_id: str
    prompt_version_id: str
    is_archived: bool
    archived_at: _timestamp_pb2.Timestamp
    archived_by_user_id: str
    def __init__(self, target_id: _Optional[str] = ..., target_key: _Optional[str] = ..., name: _Optional[str] = ..., target_mode: _Optional[_Union[ExperimentTargetModeV1, str]] = ..., config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., provider_execution: _Optional[_Union[ProviderExecutionConfigV1, _Mapping]] = ..., prompt_template: _Optional[str] = ..., prompt_version: _Optional[str] = ..., prompt_label: _Optional[str] = ..., created_by_user_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., prompt_template_id: _Optional[str] = ..., prompt_version_id: _Optional[str] = ..., is_archived: _Optional[bool] = ..., archived_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., archived_by_user_id: _Optional[str] = ...) -> None: ...

class ExperimentExecutionTargetSnapshotV1(_message.Message):
    __slots__ = ("target_id", "target_key", "name", "target_mode", "config", "provider_execution", "prompt_template", "prompt_version", "prompt_label", "prompt_template_id", "prompt_version_id")
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_MODE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROMPT_LABEL_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    target_id: str
    target_key: str
    name: str
    target_mode: ExperimentTargetModeV1
    config: _struct_pb2.Struct
    provider_execution: ProviderExecutionConfigV1
    prompt_template: str
    prompt_version: str
    prompt_label: str
    prompt_template_id: str
    prompt_version_id: str
    def __init__(self, target_id: _Optional[str] = ..., target_key: _Optional[str] = ..., name: _Optional[str] = ..., target_mode: _Optional[_Union[ExperimentTargetModeV1, str]] = ..., config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., provider_execution: _Optional[_Union[ProviderExecutionConfigV1, _Mapping]] = ..., prompt_template: _Optional[str] = ..., prompt_version: _Optional[str] = ..., prompt_label: _Optional[str] = ..., prompt_template_id: _Optional[str] = ..., prompt_version_id: _Optional[str] = ...) -> None: ...

class CreateExperimentInputRequest(_message.Message):
    __slots__ = ("input_key", "name", "description", "dataset_version_id", "metadata")
    INPUT_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    input_key: str
    name: str
    description: str
    dataset_version_id: str
    metadata: _struct_pb2.Struct
    def __init__(self, input_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., dataset_version_id: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class CreateExperimentInputResponse(_message.Message):
    __slots__ = ("input", "dataset_version")
    INPUT_FIELD_NUMBER: _ClassVar[int]
    DATASET_VERSION_FIELD_NUMBER: _ClassVar[int]
    input: ExperimentInputV1
    dataset_version: DatasetVersionV1
    def __init__(self, input: _Optional[_Union[ExperimentInputV1, _Mapping]] = ..., dataset_version: _Optional[_Union[DatasetVersionV1, _Mapping]] = ...) -> None: ...

class ListExperimentInputsRequest(_message.Message):
    __slots__ = ("dataset_collection_id", "dataset_version_id", "limit", "offset")
    DATASET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    dataset_collection_id: str
    dataset_version_id: str
    limit: int
    offset: int
    def __init__(self, dataset_collection_id: _Optional[str] = ..., dataset_version_id: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListExperimentInputsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ExperimentInputV1]
    def __init__(self, items: _Optional[_Iterable[_Union[ExperimentInputV1, _Mapping]]] = ...) -> None: ...

class GetExperimentInputRequest(_message.Message):
    __slots__ = ("experiment_input_id",)
    EXPERIMENT_INPUT_ID_FIELD_NUMBER: _ClassVar[int]
    experiment_input_id: str
    def __init__(self, experiment_input_id: _Optional[str] = ...) -> None: ...

class GetExperimentInputResponse(_message.Message):
    __slots__ = ("input", "collection", "dataset_version")
    INPUT_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    DATASET_VERSION_FIELD_NUMBER: _ClassVar[int]
    input: ExperimentInputV1
    collection: DatasetCollectionV1
    dataset_version: DatasetVersionV1
    def __init__(self, input: _Optional[_Union[ExperimentInputV1, _Mapping]] = ..., collection: _Optional[_Union[DatasetCollectionV1, _Mapping]] = ..., dataset_version: _Optional[_Union[DatasetVersionV1, _Mapping]] = ...) -> None: ...

class CreateExperimentTargetRequest(_message.Message):
    __slots__ = ("target_key", "name", "target_mode", "config", "provider_execution", "prompt_template", "prompt_version", "prompt_label", "prompt_template_id", "prompt_version_id")
    TARGET_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_MODE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROMPT_LABEL_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    target_key: str
    name: str
    target_mode: ExperimentTargetModeV1
    config: _struct_pb2.Struct
    provider_execution: ProviderExecutionConfigV1
    prompt_template: str
    prompt_version: str
    prompt_label: str
    prompt_template_id: str
    prompt_version_id: str
    def __init__(self, target_key: _Optional[str] = ..., name: _Optional[str] = ..., target_mode: _Optional[_Union[ExperimentTargetModeV1, str]] = ..., config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., provider_execution: _Optional[_Union[ProviderExecutionConfigV1, _Mapping]] = ..., prompt_template: _Optional[str] = ..., prompt_version: _Optional[str] = ..., prompt_label: _Optional[str] = ..., prompt_template_id: _Optional[str] = ..., prompt_version_id: _Optional[str] = ...) -> None: ...

class CreateExperimentTargetResponse(_message.Message):
    __slots__ = ("target",)
    TARGET_FIELD_NUMBER: _ClassVar[int]
    target: ExperimentTargetV1
    def __init__(self, target: _Optional[_Union[ExperimentTargetV1, _Mapping]] = ...) -> None: ...

class GetExperimentTargetRequest(_message.Message):
    __slots__ = ("experiment_target_id",)
    EXPERIMENT_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    experiment_target_id: str
    def __init__(self, experiment_target_id: _Optional[str] = ...) -> None: ...

class GetExperimentTargetResponse(_message.Message):
    __slots__ = ("target",)
    TARGET_FIELD_NUMBER: _ClassVar[int]
    target: ExperimentTargetV1
    def __init__(self, target: _Optional[_Union[ExperimentTargetV1, _Mapping]] = ...) -> None: ...

class ListExperimentTargetsRequest(_message.Message):
    __slots__ = ("target_mode", "limit", "offset", "include_archived")
    TARGET_MODE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    target_mode: ExperimentTargetModeV1
    limit: int
    offset: int
    include_archived: bool
    def __init__(self, target_mode: _Optional[_Union[ExperimentTargetModeV1, str]] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ..., include_archived: _Optional[bool] = ...) -> None: ...

class ListExperimentTargetsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ExperimentTargetV1]
    def __init__(self, items: _Optional[_Iterable[_Union[ExperimentTargetV1, _Mapping]]] = ...) -> None: ...

class UpdateExperimentTargetRequest(_message.Message):
    __slots__ = ("experiment_target_id", "target_key", "name", "target_mode", "config", "provider_execution", "prompt_template", "prompt_version", "prompt_label", "prompt_template_id", "prompt_version_id")
    EXPERIMENT_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_MODE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROMPT_LABEL_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    experiment_target_id: str
    target_key: str
    name: str
    target_mode: ExperimentTargetModeV1
    config: _struct_pb2.Struct
    provider_execution: ProviderExecutionConfigV1
    prompt_template: str
    prompt_version: str
    prompt_label: str
    prompt_template_id: str
    prompt_version_id: str
    def __init__(self, experiment_target_id: _Optional[str] = ..., target_key: _Optional[str] = ..., name: _Optional[str] = ..., target_mode: _Optional[_Union[ExperimentTargetModeV1, str]] = ..., config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., provider_execution: _Optional[_Union[ProviderExecutionConfigV1, _Mapping]] = ..., prompt_template: _Optional[str] = ..., prompt_version: _Optional[str] = ..., prompt_label: _Optional[str] = ..., prompt_template_id: _Optional[str] = ..., prompt_version_id: _Optional[str] = ...) -> None: ...

class UpdateExperimentTargetResponse(_message.Message):
    __slots__ = ("target",)
    TARGET_FIELD_NUMBER: _ClassVar[int]
    target: ExperimentTargetV1
    def __init__(self, target: _Optional[_Union[ExperimentTargetV1, _Mapping]] = ...) -> None: ...

class ArchiveExperimentTargetRequest(_message.Message):
    __slots__ = ("experiment_target_id",)
    EXPERIMENT_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    experiment_target_id: str
    def __init__(self, experiment_target_id: _Optional[str] = ...) -> None: ...

class ArchiveExperimentTargetResponse(_message.Message):
    __slots__ = ("target",)
    TARGET_FIELD_NUMBER: _ClassVar[int]
    target: ExperimentTargetV1
    def __init__(self, target: _Optional[_Union[ExperimentTargetV1, _Mapping]] = ...) -> None: ...

class DeleteExperimentTargetRequest(_message.Message):
    __slots__ = ("experiment_target_id",)
    EXPERIMENT_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    experiment_target_id: str
    def __init__(self, experiment_target_id: _Optional[str] = ...) -> None: ...

class DeleteExperimentTargetResponse(_message.Message):
    __slots__ = ("experiment_target_id",)
    EXPERIMENT_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    experiment_target_id: str
    def __init__(self, experiment_target_id: _Optional[str] = ...) -> None: ...

class CreateEvaluatorTemplateRequest(_message.Message):
    __slots__ = ("template_key", "name", "evaluator_kind", "execution_mode", "config", "provider_execution", "settings", "prompt_template_id", "prompt_version_id", "description", "metadata")
    TEMPLATE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_KIND_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_MODE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    template_key: str
    name: str
    evaluator_kind: str
    execution_mode: EvaluatorExecutionModeV1
    config: _struct_pb2.Struct
    provider_execution: ProviderExecutionConfigV1
    settings: EvaluatorTemplateSettingsV1
    prompt_template_id: str
    prompt_version_id: str
    description: str
    metadata: _struct_pb2.Struct
    def __init__(self, template_key: _Optional[str] = ..., name: _Optional[str] = ..., evaluator_kind: _Optional[str] = ..., execution_mode: _Optional[_Union[EvaluatorExecutionModeV1, str]] = ..., config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., provider_execution: _Optional[_Union[ProviderExecutionConfigV1, _Mapping]] = ..., settings: _Optional[_Union[EvaluatorTemplateSettingsV1, _Mapping]] = ..., prompt_template_id: _Optional[str] = ..., prompt_version_id: _Optional[str] = ..., description: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class CreateEvaluatorTemplateResponse(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: EvaluatorTemplateV1
    def __init__(self, template: _Optional[_Union[EvaluatorTemplateV1, _Mapping]] = ...) -> None: ...

class ListEvaluatorTemplatesRequest(_message.Message):
    __slots__ = ("limit", "offset", "include_archived")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    include_archived: bool
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., include_archived: _Optional[bool] = ...) -> None: ...

class ListEvaluatorTemplatesResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[EvaluatorTemplateV1]
    def __init__(self, items: _Optional[_Iterable[_Union[EvaluatorTemplateV1, _Mapping]]] = ...) -> None: ...

class GetEvaluatorTemplateRequest(_message.Message):
    __slots__ = ("template_id",)
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    def __init__(self, template_id: _Optional[str] = ...) -> None: ...

class GetEvaluatorTemplateResponse(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: EvaluatorTemplateV1
    def __init__(self, template: _Optional[_Union[EvaluatorTemplateV1, _Mapping]] = ...) -> None: ...

class UpdateEvaluatorTemplateRequest(_message.Message):
    __slots__ = ("template_id", "template_key", "name", "evaluator_kind", "execution_mode", "config", "provider_execution", "settings", "prompt_template_id", "prompt_version_id", "description", "metadata")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_KIND_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_MODE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    template_key: str
    name: str
    evaluator_kind: str
    execution_mode: EvaluatorExecutionModeV1
    config: _struct_pb2.Struct
    provider_execution: ProviderExecutionConfigV1
    settings: EvaluatorTemplateSettingsV1
    prompt_template_id: str
    prompt_version_id: str
    description: str
    metadata: _struct_pb2.Struct
    def __init__(self, template_id: _Optional[str] = ..., template_key: _Optional[str] = ..., name: _Optional[str] = ..., evaluator_kind: _Optional[str] = ..., execution_mode: _Optional[_Union[EvaluatorExecutionModeV1, str]] = ..., config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., provider_execution: _Optional[_Union[ProviderExecutionConfigV1, _Mapping]] = ..., settings: _Optional[_Union[EvaluatorTemplateSettingsV1, _Mapping]] = ..., prompt_template_id: _Optional[str] = ..., prompt_version_id: _Optional[str] = ..., description: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class UpdateEvaluatorTemplateResponse(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: EvaluatorTemplateV1
    def __init__(self, template: _Optional[_Union[EvaluatorTemplateV1, _Mapping]] = ...) -> None: ...

class ArchiveEvaluatorTemplateRequest(_message.Message):
    __slots__ = ("template_id",)
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    def __init__(self, template_id: _Optional[str] = ...) -> None: ...

class ArchiveEvaluatorTemplateResponse(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: EvaluatorTemplateV1
    def __init__(self, template: _Optional[_Union[EvaluatorTemplateV1, _Mapping]] = ...) -> None: ...

class DeleteEvaluatorTemplateRequest(_message.Message):
    __slots__ = ("template_id",)
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    def __init__(self, template_id: _Optional[str] = ...) -> None: ...

class DeleteEvaluatorTemplateResponse(_message.Message):
    __slots__ = ("template_id",)
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    def __init__(self, template_id: _Optional[str] = ...) -> None: ...

class CreateScoreConfigRequest(_message.Message):
    __slots__ = ("config_key", "name", "metric_name", "score_source", "evaluator_template_id", "pass_label", "fail_label", "pass_threshold", "max_attempts", "retry_backoff_seconds", "config", "provider_execution", "settings", "description", "metadata")
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    SCORE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PASS_LABEL_FIELD_NUMBER: _ClassVar[int]
    FAIL_LABEL_FIELD_NUMBER: _ClassVar[int]
    PASS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    RETRY_BACKOFF_SECONDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    config_key: str
    name: str
    metric_name: str
    score_source: ScoreSourceV1
    evaluator_template_id: str
    pass_label: str
    fail_label: str
    pass_threshold: float
    max_attempts: int
    retry_backoff_seconds: int
    config: _struct_pb2.Struct
    provider_execution: ProviderExecutionConfigV1
    settings: ScoreConfigSettingsV1
    description: str
    metadata: _struct_pb2.Struct
    def __init__(self, config_key: _Optional[str] = ..., name: _Optional[str] = ..., metric_name: _Optional[str] = ..., score_source: _Optional[_Union[ScoreSourceV1, str]] = ..., evaluator_template_id: _Optional[str] = ..., pass_label: _Optional[str] = ..., fail_label: _Optional[str] = ..., pass_threshold: _Optional[float] = ..., max_attempts: _Optional[int] = ..., retry_backoff_seconds: _Optional[int] = ..., config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., provider_execution: _Optional[_Union[ProviderExecutionConfigV1, _Mapping]] = ..., settings: _Optional[_Union[ScoreConfigSettingsV1, _Mapping]] = ..., description: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class CreateProviderCredentialRequest(_message.Message):
    __slots__ = ("provider_name", "credential_key", "auth_ref", "key_ref", "is_default")
    PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_KEY_FIELD_NUMBER: _ClassVar[int]
    AUTH_REF_FIELD_NUMBER: _ClassVar[int]
    KEY_REF_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    provider_name: ProviderNameV1
    credential_key: str
    auth_ref: str
    key_ref: str
    is_default: bool
    def __init__(self, provider_name: _Optional[_Union[ProviderNameV1, str]] = ..., credential_key: _Optional[str] = ..., auth_ref: _Optional[str] = ..., key_ref: _Optional[str] = ..., is_default: _Optional[bool] = ...) -> None: ...

class CreateProviderCredentialResponse(_message.Message):
    __slots__ = ("provider_credential",)
    PROVIDER_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    provider_credential: ProviderCredentialV1
    def __init__(self, provider_credential: _Optional[_Union[ProviderCredentialV1, _Mapping]] = ...) -> None: ...

class GetProviderCredentialRequest(_message.Message):
    __slots__ = ("provider_credential_id",)
    PROVIDER_CREDENTIAL_ID_FIELD_NUMBER: _ClassVar[int]
    provider_credential_id: str
    def __init__(self, provider_credential_id: _Optional[str] = ...) -> None: ...

class GetProviderCredentialResponse(_message.Message):
    __slots__ = ("provider_credential",)
    PROVIDER_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    provider_credential: ProviderCredentialV1
    def __init__(self, provider_credential: _Optional[_Union[ProviderCredentialV1, _Mapping]] = ...) -> None: ...

class ListProviderCredentialsRequest(_message.Message):
    __slots__ = ("limit", "offset")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListProviderCredentialsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ProviderCredentialV1]
    def __init__(self, items: _Optional[_Iterable[_Union[ProviderCredentialV1, _Mapping]]] = ...) -> None: ...

class UpdateProviderCredentialRequest(_message.Message):
    __slots__ = ("provider_credential_id", "provider_name", "credential_key", "auth_ref", "key_ref", "is_default")
    PROVIDER_CREDENTIAL_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_KEY_FIELD_NUMBER: _ClassVar[int]
    AUTH_REF_FIELD_NUMBER: _ClassVar[int]
    KEY_REF_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    provider_credential_id: str
    provider_name: ProviderNameV1
    credential_key: str
    auth_ref: str
    key_ref: str
    is_default: bool
    def __init__(self, provider_credential_id: _Optional[str] = ..., provider_name: _Optional[_Union[ProviderNameV1, str]] = ..., credential_key: _Optional[str] = ..., auth_ref: _Optional[str] = ..., key_ref: _Optional[str] = ..., is_default: _Optional[bool] = ...) -> None: ...

class UpdateProviderCredentialResponse(_message.Message):
    __slots__ = ("provider_credential",)
    PROVIDER_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    provider_credential: ProviderCredentialV1
    def __init__(self, provider_credential: _Optional[_Union[ProviderCredentialV1, _Mapping]] = ...) -> None: ...

class SetProviderCredentialSecretRequest(_message.Message):
    __slots__ = ("provider_credential_id", "secret_value", "note")
    PROVIDER_CREDENTIAL_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_VALUE_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    provider_credential_id: str
    secret_value: str
    note: str
    def __init__(self, provider_credential_id: _Optional[str] = ..., secret_value: _Optional[str] = ..., note: _Optional[str] = ...) -> None: ...

class SetProviderCredentialSecretResponse(_message.Message):
    __slots__ = ("provider_credential", "provider_credential_secret")
    PROVIDER_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_CREDENTIAL_SECRET_FIELD_NUMBER: _ClassVar[int]
    provider_credential: ProviderCredentialV1
    provider_credential_secret: ProviderCredentialSecretV1
    def __init__(self, provider_credential: _Optional[_Union[ProviderCredentialV1, _Mapping]] = ..., provider_credential_secret: _Optional[_Union[ProviderCredentialSecretV1, _Mapping]] = ...) -> None: ...

class ListProviderCredentialSecretsRequest(_message.Message):
    __slots__ = ("provider_credential_id", "limit", "offset")
    PROVIDER_CREDENTIAL_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    provider_credential_id: str
    limit: int
    offset: int
    def __init__(self, provider_credential_id: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListProviderCredentialSecretsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ProviderCredentialSecretV1]
    def __init__(self, items: _Optional[_Iterable[_Union[ProviderCredentialSecretV1, _Mapping]]] = ...) -> None: ...

class RevokeProviderCredentialSecretRequest(_message.Message):
    __slots__ = ("provider_credential_id", "note")
    PROVIDER_CREDENTIAL_ID_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    provider_credential_id: str
    note: str
    def __init__(self, provider_credential_id: _Optional[str] = ..., note: _Optional[str] = ...) -> None: ...

class RevokeProviderCredentialSecretResponse(_message.Message):
    __slots__ = ("provider_credential", "provider_credential_secret")
    PROVIDER_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_CREDENTIAL_SECRET_FIELD_NUMBER: _ClassVar[int]
    provider_credential: ProviderCredentialV1
    provider_credential_secret: ProviderCredentialSecretV1
    def __init__(self, provider_credential: _Optional[_Union[ProviderCredentialV1, _Mapping]] = ..., provider_credential_secret: _Optional[_Union[ProviderCredentialSecretV1, _Mapping]] = ...) -> None: ...

class CreateScoreConfigResponse(_message.Message):
    __slots__ = ("score_config",)
    SCORE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    score_config: ScoreConfigV1
    def __init__(self, score_config: _Optional[_Union[ScoreConfigV1, _Mapping]] = ...) -> None: ...

class ListScoreConfigsRequest(_message.Message):
    __slots__ = ("limit", "offset", "include_archived")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    include_archived: bool
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., include_archived: _Optional[bool] = ...) -> None: ...

class ListScoreConfigsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ScoreConfigV1]
    def __init__(self, items: _Optional[_Iterable[_Union[ScoreConfigV1, _Mapping]]] = ...) -> None: ...

class GetScoreConfigRequest(_message.Message):
    __slots__ = ("score_config_id",)
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    def __init__(self, score_config_id: _Optional[str] = ...) -> None: ...

class GetScoreConfigResponse(_message.Message):
    __slots__ = ("score_config",)
    SCORE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    score_config: ScoreConfigV1
    def __init__(self, score_config: _Optional[_Union[ScoreConfigV1, _Mapping]] = ...) -> None: ...

class UpdateScoreConfigRequest(_message.Message):
    __slots__ = ("score_config_id", "config_key", "name", "metric_name", "score_source", "evaluator_template_id", "pass_label", "fail_label", "pass_threshold", "max_attempts", "retry_backoff_seconds", "config", "provider_execution", "settings", "description", "metadata")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    SCORE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PASS_LABEL_FIELD_NUMBER: _ClassVar[int]
    FAIL_LABEL_FIELD_NUMBER: _ClassVar[int]
    PASS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    RETRY_BACKOFF_SECONDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    config_key: str
    name: str
    metric_name: str
    score_source: ScoreSourceV1
    evaluator_template_id: str
    pass_label: str
    fail_label: str
    pass_threshold: float
    max_attempts: int
    retry_backoff_seconds: int
    config: _struct_pb2.Struct
    provider_execution: ProviderExecutionConfigV1
    settings: ScoreConfigSettingsV1
    description: str
    metadata: _struct_pb2.Struct
    def __init__(self, score_config_id: _Optional[str] = ..., config_key: _Optional[str] = ..., name: _Optional[str] = ..., metric_name: _Optional[str] = ..., score_source: _Optional[_Union[ScoreSourceV1, str]] = ..., evaluator_template_id: _Optional[str] = ..., pass_label: _Optional[str] = ..., fail_label: _Optional[str] = ..., pass_threshold: _Optional[float] = ..., max_attempts: _Optional[int] = ..., retry_backoff_seconds: _Optional[int] = ..., config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., provider_execution: _Optional[_Union[ProviderExecutionConfigV1, _Mapping]] = ..., settings: _Optional[_Union[ScoreConfigSettingsV1, _Mapping]] = ..., description: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class UpdateScoreConfigResponse(_message.Message):
    __slots__ = ("score_config",)
    SCORE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    score_config: ScoreConfigV1
    def __init__(self, score_config: _Optional[_Union[ScoreConfigV1, _Mapping]] = ...) -> None: ...

class ScorerStarterSystemV1(_message.Message):
    __slots__ = ("starter_key", "name", "description", "kind", "tags", "default_prompt_template_draft", "default_prompt_version_draft", "default_evaluator_template_draft", "default_score_config_draft", "recommended_input_mapping", "recommended_output_type")
    STARTER_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PROMPT_TEMPLATE_DRAFT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PROMPT_VERSION_DRAFT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_EVALUATOR_TEMPLATE_DRAFT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SCORE_CONFIG_DRAFT_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_INPUT_MAPPING_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_OUTPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    starter_key: str
    name: str
    description: str
    kind: ScorerStarterKindV1
    tags: _containers.RepeatedScalarFieldContainer[str]
    default_prompt_template_draft: CreatePromptTemplateRequest
    default_prompt_version_draft: CreatePromptVersionRequest
    default_evaluator_template_draft: CreateEvaluatorTemplateRequest
    default_score_config_draft: CreateScoreConfigRequest
    recommended_input_mapping: _struct_pb2.Struct
    recommended_output_type: str
    def __init__(self, starter_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., kind: _Optional[_Union[ScorerStarterKindV1, str]] = ..., tags: _Optional[_Iterable[str]] = ..., default_prompt_template_draft: _Optional[_Union[CreatePromptTemplateRequest, _Mapping]] = ..., default_prompt_version_draft: _Optional[_Union[CreatePromptVersionRequest, _Mapping]] = ..., default_evaluator_template_draft: _Optional[_Union[CreateEvaluatorTemplateRequest, _Mapping]] = ..., default_score_config_draft: _Optional[_Union[CreateScoreConfigRequest, _Mapping]] = ..., recommended_input_mapping: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., recommended_output_type: _Optional[str] = ...) -> None: ...

class ListScorerStartersRequest(_message.Message):
    __slots__ = ("kind", "tags")
    KIND_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    kind: ScorerStarterKindV1
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, kind: _Optional[_Union[ScorerStarterKindV1, str]] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class ListScorerStartersResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ScorerStarterSystemV1]
    def __init__(self, items: _Optional[_Iterable[_Union[ScorerStarterSystemV1, _Mapping]]] = ...) -> None: ...

class ScorerBundleUsageSummaryV1(_message.Message):
    __slots__ = ("experiment_run_count", "release_gate_count", "online_scoring_rule_count", "latest_experiment_run_id", "latest_release_gate_id", "automation_rule_count", "latest_online_scoring_rule_id", "latest_automation_rule_id", "has_online_scoring_rule", "has_automation_rule")
    EXPERIMENT_RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    RELEASE_GATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    ONLINE_SCORING_RULE_COUNT_FIELD_NUMBER: _ClassVar[int]
    LATEST_EXPERIMENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    LATEST_RELEASE_GATE_ID_FIELD_NUMBER: _ClassVar[int]
    AUTOMATION_RULE_COUNT_FIELD_NUMBER: _ClassVar[int]
    LATEST_ONLINE_SCORING_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    LATEST_AUTOMATION_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    HAS_ONLINE_SCORING_RULE_FIELD_NUMBER: _ClassVar[int]
    HAS_AUTOMATION_RULE_FIELD_NUMBER: _ClassVar[int]
    experiment_run_count: int
    release_gate_count: int
    online_scoring_rule_count: int
    latest_experiment_run_id: str
    latest_release_gate_id: str
    automation_rule_count: int
    latest_online_scoring_rule_id: str
    latest_automation_rule_id: str
    has_online_scoring_rule: bool
    has_automation_rule: bool
    def __init__(self, experiment_run_count: _Optional[int] = ..., release_gate_count: _Optional[int] = ..., online_scoring_rule_count: _Optional[int] = ..., latest_experiment_run_id: _Optional[str] = ..., latest_release_gate_id: _Optional[str] = ..., automation_rule_count: _Optional[int] = ..., latest_online_scoring_rule_id: _Optional[str] = ..., latest_automation_rule_id: _Optional[str] = ..., has_online_scoring_rule: _Optional[bool] = ..., has_automation_rule: _Optional[bool] = ...) -> None: ...

class ScorerBundleCompletenessV1(_message.Message):
    __slots__ = ("has_score_config", "has_evaluator_template", "has_prompt_template", "has_prompt_version", "is_runnable", "missing_fields", "warnings")
    HAS_SCORE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    HAS_EVALUATOR_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    HAS_PROMPT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    HAS_PROMPT_VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_RUNNABLE_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELDS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    has_score_config: bool
    has_evaluator_template: bool
    has_prompt_template: bool
    has_prompt_version: bool
    is_runnable: bool
    missing_fields: _containers.RepeatedScalarFieldContainer[str]
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, has_score_config: _Optional[bool] = ..., has_evaluator_template: _Optional[bool] = ..., has_prompt_template: _Optional[bool] = ..., has_prompt_version: _Optional[bool] = ..., is_runnable: _Optional[bool] = ..., missing_fields: _Optional[_Iterable[str]] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...

class ScorerBundlePromptResolutionV1(_message.Message):
    __slots__ = ("prompt_template_id", "prompt_version_id", "template_key", "template_name", "version_number", "version_label", "version_ref", "environments", "source", "prompt_version_matches_template", "warnings")
    PROMPT_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_KEY_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    VERSION_LABEL_FIELD_NUMBER: _ClassVar[int]
    VERSION_REF_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_MATCHES_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    prompt_template_id: str
    prompt_version_id: str
    template_key: str
    template_name: str
    version_number: int
    version_label: str
    version_ref: str
    environments: _containers.RepeatedScalarFieldContainer[PromptEnvironmentV1]
    source: str
    prompt_version_matches_template: bool
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, prompt_template_id: _Optional[str] = ..., prompt_version_id: _Optional[str] = ..., template_key: _Optional[str] = ..., template_name: _Optional[str] = ..., version_number: _Optional[int] = ..., version_label: _Optional[str] = ..., version_ref: _Optional[str] = ..., environments: _Optional[_Iterable[_Union[PromptEnvironmentV1, str]]] = ..., source: _Optional[str] = ..., prompt_version_matches_template: _Optional[bool] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...

class ScorerBundleAutomationHandoffV1(_message.Message):
    __slots__ = ("can_create_automation_rule", "supported_automation_scopes", "supported_runtime_scopes", "recommended_default_scope", "recommended_runtime_scope", "cta_label", "cta_hint", "handoff_status", "default_rule_config", "warnings")
    CAN_CREATE_AUTOMATION_RULE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_AUTOMATION_SCOPES_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_RUNTIME_SCOPES_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_DEFAULT_SCOPE_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_RUNTIME_SCOPE_FIELD_NUMBER: _ClassVar[int]
    CTA_LABEL_FIELD_NUMBER: _ClassVar[int]
    CTA_HINT_FIELD_NUMBER: _ClassVar[int]
    HANDOFF_STATUS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_RULE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    can_create_automation_rule: bool
    supported_automation_scopes: _containers.RepeatedScalarFieldContainer[str]
    supported_runtime_scopes: _containers.RepeatedScalarFieldContainer[str]
    recommended_default_scope: str
    recommended_runtime_scope: str
    cta_label: str
    cta_hint: str
    handoff_status: str
    default_rule_config: _struct_pb2.Struct
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, can_create_automation_rule: _Optional[bool] = ..., supported_automation_scopes: _Optional[_Iterable[str]] = ..., supported_runtime_scopes: _Optional[_Iterable[str]] = ..., recommended_default_scope: _Optional[str] = ..., recommended_runtime_scope: _Optional[str] = ..., cta_label: _Optional[str] = ..., cta_hint: _Optional[str] = ..., handoff_status: _Optional[str] = ..., default_rule_config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...

class ScorerBundleV1(_message.Message):
    __slots__ = ("bundle_id", "score_config", "evaluator_template", "prompt_template", "prompt_version", "usage_summary", "completeness", "prompt_resolution", "automation_handoff")
    BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_FIELD_NUMBER: _ClassVar[int]
    USAGE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    COMPLETENESS_FIELD_NUMBER: _ClassVar[int]
    PROMPT_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    AUTOMATION_HANDOFF_FIELD_NUMBER: _ClassVar[int]
    bundle_id: str
    score_config: ScoreConfigV1
    evaluator_template: EvaluatorTemplateV1
    prompt_template: PromptTemplateV1
    prompt_version: PromptVersionV1
    usage_summary: ScorerBundleUsageSummaryV1
    completeness: ScorerBundleCompletenessV1
    prompt_resolution: ScorerBundlePromptResolutionV1
    automation_handoff: ScorerBundleAutomationHandoffV1
    def __init__(self, bundle_id: _Optional[str] = ..., score_config: _Optional[_Union[ScoreConfigV1, _Mapping]] = ..., evaluator_template: _Optional[_Union[EvaluatorTemplateV1, _Mapping]] = ..., prompt_template: _Optional[_Union[PromptTemplateV1, _Mapping]] = ..., prompt_version: _Optional[_Union[PromptVersionV1, _Mapping]] = ..., usage_summary: _Optional[_Union[ScorerBundleUsageSummaryV1, _Mapping]] = ..., completeness: _Optional[_Union[ScorerBundleCompletenessV1, _Mapping]] = ..., prompt_resolution: _Optional[_Union[ScorerBundlePromptResolutionV1, _Mapping]] = ..., automation_handoff: _Optional[_Union[ScorerBundleAutomationHandoffV1, _Mapping]] = ...) -> None: ...

class ListScorerBundlesRequest(_message.Message):
    __slots__ = ("limit", "offset", "include_archived")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    include_archived: bool
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., include_archived: _Optional[bool] = ...) -> None: ...

class ListScorerBundlesResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ScorerBundleV1]
    def __init__(self, items: _Optional[_Iterable[_Union[ScorerBundleV1, _Mapping]]] = ...) -> None: ...

class GetScorerBundleRequest(_message.Message):
    __slots__ = ("bundle_id",)
    BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
    bundle_id: str
    def __init__(self, bundle_id: _Optional[str] = ...) -> None: ...

class GetScorerBundleResponse(_message.Message):
    __slots__ = ("bundle",)
    BUNDLE_FIELD_NUMBER: _ClassVar[int]
    bundle: ScorerBundleV1
    def __init__(self, bundle: _Optional[_Union[ScorerBundleV1, _Mapping]] = ...) -> None: ...

class ScorerPromptRefV1(_message.Message):
    __slots__ = ("prompt_template_id", "prompt_version_id")
    PROMPT_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    prompt_template_id: str
    prompt_version_id: str
    def __init__(self, prompt_template_id: _Optional[str] = ..., prompt_version_id: _Optional[str] = ...) -> None: ...

class ScorerPromptDraftV1(_message.Message):
    __slots__ = ("prompt_text", "system_prompt", "metadata")
    PROMPT_TEXT_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_PROMPT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    prompt_text: str
    system_prompt: str
    metadata: _struct_pb2.Struct
    def __init__(self, prompt_text: _Optional[str] = ..., system_prompt: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ScorerInlinePreviewPayloadV1(_message.Message):
    __slots__ = ("input_payload", "subject_output", "expected_output", "correlation")
    INPUT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_FIELD_NUMBER: _ClassVar[int]
    input_payload: _struct_pb2.Struct
    subject_output: _struct_pb2.Struct
    expected_output: _struct_pb2.Struct
    correlation: CorrelationContextV1
    def __init__(self, input_payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., subject_output: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., expected_output: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., correlation: _Optional[_Union[CorrelationContextV1, _Mapping]] = ...) -> None: ...

class ScorerPreviewTargetV1(_message.Message):
    __slots__ = ("trace_id", "session_id", "dataset_item_id", "experiment_run_item_id", "inline_payload")
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_RUN_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    INLINE_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    trace_id: str
    session_id: str
    dataset_item_id: str
    experiment_run_item_id: str
    inline_payload: ScorerInlinePreviewPayloadV1
    def __init__(self, trace_id: _Optional[str] = ..., session_id: _Optional[str] = ..., dataset_item_id: _Optional[str] = ..., experiment_run_item_id: _Optional[str] = ..., inline_payload: _Optional[_Union[ScorerInlinePreviewPayloadV1, _Mapping]] = ...) -> None: ...

class ScorerPreviewOptionsV1(_message.Message):
    __slots__ = ("execute", "include_artifact_previews")
    EXECUTE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ARTIFACT_PREVIEWS_FIELD_NUMBER: _ClassVar[int]
    execute: bool
    include_artifact_previews: bool
    def __init__(self, execute: _Optional[bool] = ..., include_artifact_previews: _Optional[bool] = ...) -> None: ...

class PreviewScorerDraftRequest(_message.Message):
    __slots__ = ("prompt_ref", "prompt_draft", "evaluator_template_draft", "score_config_draft", "preview_target", "preview_options", "target_selector")
    PROMPT_REF_FIELD_NUMBER: _ClassVar[int]
    PROMPT_DRAFT_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_TEMPLATE_DRAFT_FIELD_NUMBER: _ClassVar[int]
    SCORE_CONFIG_DRAFT_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_TARGET_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    TARGET_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    prompt_ref: ScorerPromptRefV1
    prompt_draft: ScorerPromptDraftV1
    evaluator_template_draft: CreateEvaluatorTemplateRequest
    score_config_draft: CreateScoreConfigRequest
    preview_target: ScorerPreviewTargetV1
    preview_options: ScorerPreviewOptionsV1
    target_selector: ScorerTargetSelectorV1
    def __init__(self, prompt_ref: _Optional[_Union[ScorerPromptRefV1, _Mapping]] = ..., prompt_draft: _Optional[_Union[ScorerPromptDraftV1, _Mapping]] = ..., evaluator_template_draft: _Optional[_Union[CreateEvaluatorTemplateRequest, _Mapping]] = ..., score_config_draft: _Optional[_Union[CreateScoreConfigRequest, _Mapping]] = ..., preview_target: _Optional[_Union[ScorerPreviewTargetV1, _Mapping]] = ..., preview_options: _Optional[_Union[ScorerPreviewOptionsV1, _Mapping]] = ..., target_selector: _Optional[_Union[ScorerTargetSelectorV1, _Mapping]] = ...) -> None: ...

class PreviewScorerDraftResponse(_message.Message):
    __slots__ = ("rendered_prompt", "resolved_mapping", "provider_request_preview", "verdict_preview", "mapped_score", "passes_threshold", "artifact_previews", "execution_metadata", "resolved_target", "warnings")
    RENDERED_PROMPT_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_MAPPING_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_REQUEST_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    VERDICT_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    MAPPED_SCORE_FIELD_NUMBER: _ClassVar[int]
    PASSES_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_PREVIEWS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_METADATA_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_TARGET_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    rendered_prompt: str
    resolved_mapping: _struct_pb2.Struct
    provider_request_preview: _struct_pb2.Struct
    verdict_preview: _struct_pb2.Struct
    mapped_score: float
    passes_threshold: bool
    artifact_previews: _containers.RepeatedCompositeFieldContainer[ExecutionArtifactPreviewV1]
    execution_metadata: _struct_pb2.Struct
    resolved_target: ResolvedScorerTargetV1
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, rendered_prompt: _Optional[str] = ..., resolved_mapping: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., provider_request_preview: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., verdict_preview: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., mapped_score: _Optional[float] = ..., passes_threshold: _Optional[bool] = ..., artifact_previews: _Optional[_Iterable[_Union[ExecutionArtifactPreviewV1, _Mapping]]] = ..., execution_metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., resolved_target: _Optional[_Union[ResolvedScorerTargetV1, _Mapping]] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...

class ResolveScorerTargetRequest(_message.Message):
    __slots__ = ("preview_target", "target_selector", "include_turns", "max_turns")
    PREVIEW_TARGET_FIELD_NUMBER: _ClassVar[int]
    TARGET_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TURNS_FIELD_NUMBER: _ClassVar[int]
    MAX_TURNS_FIELD_NUMBER: _ClassVar[int]
    preview_target: ScorerPreviewTargetV1
    target_selector: ScorerTargetSelectorV1
    include_turns: bool
    max_turns: int
    def __init__(self, preview_target: _Optional[_Union[ScorerPreviewTargetV1, _Mapping]] = ..., target_selector: _Optional[_Union[ScorerTargetSelectorV1, _Mapping]] = ..., include_turns: _Optional[bool] = ..., max_turns: _Optional[int] = ...) -> None: ...

class ResolveScorerTargetResponse(_message.Message):
    __slots__ = ("target", "turns", "warnings")
    TARGET_FIELD_NUMBER: _ClassVar[int]
    TURNS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    target: ResolvedScorerTargetV1
    turns: _containers.RepeatedCompositeFieldContainer[AgenticMessageTurnV1]
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, target: _Optional[_Union[ResolvedScorerTargetV1, _Mapping]] = ..., turns: _Optional[_Iterable[_Union[AgenticMessageTurnV1, _Mapping]]] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...

class PreviewScorerAutomationRuleOptionsV1(_message.Message):
    __slots__ = ("execute_sample", "max_candidates", "max_execute_candidates", "max_execute_scorers", "include_candidate_turns")
    EXECUTE_SAMPLE_FIELD_NUMBER: _ClassVar[int]
    MAX_CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    MAX_EXECUTE_CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    MAX_EXECUTE_SCORERS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CANDIDATE_TURNS_FIELD_NUMBER: _ClassVar[int]
    execute_sample: bool
    max_candidates: int
    max_execute_candidates: int
    max_execute_scorers: int
    include_candidate_turns: bool
    def __init__(self, execute_sample: _Optional[bool] = ..., max_candidates: _Optional[int] = ..., max_execute_candidates: _Optional[int] = ..., max_execute_scorers: _Optional[int] = ..., include_candidate_turns: _Optional[bool] = ...) -> None: ...

class ScorerAutomationPreviewScorerResultV1(_message.Message):
    __slots__ = ("score_config_id", "scorer_suite_item_id", "metric_name", "display_name", "selected_by_execution_bounds", "resolved_target", "turns", "rendered_prompt", "verdict_preview", "mapped_score", "passes_threshold", "artifact_previews", "execution_metadata", "warnings")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    SCORER_SUITE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SELECTED_BY_EXECUTION_BOUNDS_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_TARGET_FIELD_NUMBER: _ClassVar[int]
    TURNS_FIELD_NUMBER: _ClassVar[int]
    RENDERED_PROMPT_FIELD_NUMBER: _ClassVar[int]
    VERDICT_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    MAPPED_SCORE_FIELD_NUMBER: _ClassVar[int]
    PASSES_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_PREVIEWS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_METADATA_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    scorer_suite_item_id: str
    metric_name: str
    display_name: str
    selected_by_execution_bounds: bool
    resolved_target: ResolvedScorerTargetV1
    turns: _containers.RepeatedCompositeFieldContainer[AgenticMessageTurnV1]
    rendered_prompt: str
    verdict_preview: _struct_pb2.Struct
    mapped_score: float
    passes_threshold: bool
    artifact_previews: _containers.RepeatedCompositeFieldContainer[ExecutionArtifactPreviewV1]
    execution_metadata: _struct_pb2.Struct
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, score_config_id: _Optional[str] = ..., scorer_suite_item_id: _Optional[str] = ..., metric_name: _Optional[str] = ..., display_name: _Optional[str] = ..., selected_by_execution_bounds: _Optional[bool] = ..., resolved_target: _Optional[_Union[ResolvedScorerTargetV1, _Mapping]] = ..., turns: _Optional[_Iterable[_Union[AgenticMessageTurnV1, _Mapping]]] = ..., rendered_prompt: _Optional[str] = ..., verdict_preview: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., mapped_score: _Optional[float] = ..., passes_threshold: _Optional[bool] = ..., artifact_previews: _Optional[_Iterable[_Union[ExecutionArtifactPreviewV1, _Mapping]]] = ..., execution_metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...

class ScorerAutomationPreviewCandidateV1(_message.Message):
    __slots__ = ("trace", "trace_id", "session_id", "matched_filter", "idle_eligible", "eligible_after", "selected_by_sampling", "sampling_key", "sampling_hash", "sampling_value_percent", "resolved_target", "turns", "warnings", "scorer_results")
    TRACE_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    MATCHED_FILTER_FIELD_NUMBER: _ClassVar[int]
    IDLE_ELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    ELIGIBLE_AFTER_FIELD_NUMBER: _ClassVar[int]
    SELECTED_BY_SAMPLING_FIELD_NUMBER: _ClassVar[int]
    SAMPLING_KEY_FIELD_NUMBER: _ClassVar[int]
    SAMPLING_HASH_FIELD_NUMBER: _ClassVar[int]
    SAMPLING_VALUE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_TARGET_FIELD_NUMBER: _ClassVar[int]
    TURNS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    SCORER_RESULTS_FIELD_NUMBER: _ClassVar[int]
    trace: TraceInvestigationRowV1
    trace_id: str
    session_id: str
    matched_filter: bool
    idle_eligible: bool
    eligible_after: _timestamp_pb2.Timestamp
    selected_by_sampling: bool
    sampling_key: str
    sampling_hash: int
    sampling_value_percent: float
    resolved_target: ResolvedScorerTargetV1
    turns: _containers.RepeatedCompositeFieldContainer[AgenticMessageTurnV1]
    warnings: _containers.RepeatedScalarFieldContainer[str]
    scorer_results: _containers.RepeatedCompositeFieldContainer[ScorerAutomationPreviewScorerResultV1]
    def __init__(self, trace: _Optional[_Union[TraceInvestigationRowV1, _Mapping]] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ..., matched_filter: _Optional[bool] = ..., idle_eligible: _Optional[bool] = ..., eligible_after: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., selected_by_sampling: _Optional[bool] = ..., sampling_key: _Optional[str] = ..., sampling_hash: _Optional[int] = ..., sampling_value_percent: _Optional[float] = ..., resolved_target: _Optional[_Union[ResolvedScorerTargetV1, _Mapping]] = ..., turns: _Optional[_Iterable[_Union[AgenticMessageTurnV1, _Mapping]]] = ..., warnings: _Optional[_Iterable[str]] = ..., scorer_results: _Optional[_Iterable[_Union[ScorerAutomationPreviewScorerResultV1, _Mapping]]] = ...) -> None: ...

class PreviewScorerAutomationRuleRequest(_message.Message):
    __slots__ = ("rule_draft", "options")
    RULE_DRAFT_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    rule_draft: CreateScorerAutomationRuleRequest
    options: PreviewScorerAutomationRuleOptionsV1
    def __init__(self, rule_draft: _Optional[_Union[CreateScorerAutomationRuleRequest, _Mapping]] = ..., options: _Optional[_Union[PreviewScorerAutomationRuleOptionsV1, _Mapping]] = ...) -> None: ...

class PreviewScorerAutomationRuleResponse(_message.Message):
    __slots__ = ("matched_candidate_count", "idle_eligible_candidate_count", "sampled_candidate_count", "estimated_job_count", "executed_job_count", "estimated_execution_cost_usd", "candidates", "warnings", "execution_metadata")
    MATCHED_CANDIDATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    IDLE_ELIGIBLE_CANDIDATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SAMPLED_CANDIDATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_JOB_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_JOB_COUNT_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_EXECUTION_COST_USD_FIELD_NUMBER: _ClassVar[int]
    CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_METADATA_FIELD_NUMBER: _ClassVar[int]
    matched_candidate_count: int
    idle_eligible_candidate_count: int
    sampled_candidate_count: int
    estimated_job_count: int
    executed_job_count: int
    estimated_execution_cost_usd: float
    candidates: _containers.RepeatedCompositeFieldContainer[ScorerAutomationPreviewCandidateV1]
    warnings: _containers.RepeatedScalarFieldContainer[str]
    execution_metadata: _struct_pb2.Struct
    def __init__(self, matched_candidate_count: _Optional[int] = ..., idle_eligible_candidate_count: _Optional[int] = ..., sampled_candidate_count: _Optional[int] = ..., estimated_job_count: _Optional[int] = ..., executed_job_count: _Optional[int] = ..., estimated_execution_cost_usd: _Optional[float] = ..., candidates: _Optional[_Iterable[_Union[ScorerAutomationPreviewCandidateV1, _Mapping]]] = ..., warnings: _Optional[_Iterable[str]] = ..., execution_metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class CreateScorerSuiteRequest(_message.Message):
    __slots__ = ("suite_key", "name", "description", "aggregation_mode", "pass_threshold", "items", "metadata", "default_reasoning_mode")
    SUITE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_MODE_FIELD_NUMBER: _ClassVar[int]
    PASS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_REASONING_MODE_FIELD_NUMBER: _ClassVar[int]
    suite_key: str
    name: str
    description: str
    aggregation_mode: ScorerAggregationModeV1
    pass_threshold: float
    items: _containers.RepeatedCompositeFieldContainer[ScorerSuiteItemDraftV1]
    metadata: _struct_pb2.Struct
    default_reasoning_mode: ScorerReasoningModeV1
    def __init__(self, suite_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., aggregation_mode: _Optional[_Union[ScorerAggregationModeV1, str]] = ..., pass_threshold: _Optional[float] = ..., items: _Optional[_Iterable[_Union[ScorerSuiteItemDraftV1, _Mapping]]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., default_reasoning_mode: _Optional[_Union[ScorerReasoningModeV1, str]] = ...) -> None: ...

class CreateScorerSuiteResponse(_message.Message):
    __slots__ = ("suite",)
    SUITE_FIELD_NUMBER: _ClassVar[int]
    suite: ScorerSuiteV1
    def __init__(self, suite: _Optional[_Union[ScorerSuiteV1, _Mapping]] = ...) -> None: ...

class GetScorerSuiteRequest(_message.Message):
    __slots__ = ("scorer_suite_id",)
    SCORER_SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    scorer_suite_id: str
    def __init__(self, scorer_suite_id: _Optional[str] = ...) -> None: ...

class GetScorerSuiteResponse(_message.Message):
    __slots__ = ("suite",)
    SUITE_FIELD_NUMBER: _ClassVar[int]
    suite: ScorerSuiteV1
    def __init__(self, suite: _Optional[_Union[ScorerSuiteV1, _Mapping]] = ...) -> None: ...

class ListScorerSuitesRequest(_message.Message):
    __slots__ = ("limit", "offset", "include_archived")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    include_archived: bool
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., include_archived: _Optional[bool] = ...) -> None: ...

class ListScorerSuitesResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ScorerSuiteV1]
    def __init__(self, items: _Optional[_Iterable[_Union[ScorerSuiteV1, _Mapping]]] = ...) -> None: ...

class UpdateScorerSuiteRequest(_message.Message):
    __slots__ = ("scorer_suite_id", "suite_key", "name", "description", "aggregation_mode", "pass_threshold", "items", "metadata", "default_reasoning_mode")
    SCORER_SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    SUITE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_MODE_FIELD_NUMBER: _ClassVar[int]
    PASS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_REASONING_MODE_FIELD_NUMBER: _ClassVar[int]
    scorer_suite_id: str
    suite_key: str
    name: str
    description: str
    aggregation_mode: ScorerAggregationModeV1
    pass_threshold: float
    items: _containers.RepeatedCompositeFieldContainer[ScorerSuiteItemDraftV1]
    metadata: _struct_pb2.Struct
    default_reasoning_mode: ScorerReasoningModeV1
    def __init__(self, scorer_suite_id: _Optional[str] = ..., suite_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., aggregation_mode: _Optional[_Union[ScorerAggregationModeV1, str]] = ..., pass_threshold: _Optional[float] = ..., items: _Optional[_Iterable[_Union[ScorerSuiteItemDraftV1, _Mapping]]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., default_reasoning_mode: _Optional[_Union[ScorerReasoningModeV1, str]] = ...) -> None: ...

class UpdateScorerSuiteResponse(_message.Message):
    __slots__ = ("suite",)
    SUITE_FIELD_NUMBER: _ClassVar[int]
    suite: ScorerSuiteV1
    def __init__(self, suite: _Optional[_Union[ScorerSuiteV1, _Mapping]] = ...) -> None: ...

class ArchiveScorerSuiteRequest(_message.Message):
    __slots__ = ("scorer_suite_id",)
    SCORER_SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    scorer_suite_id: str
    def __init__(self, scorer_suite_id: _Optional[str] = ...) -> None: ...

class ArchiveScorerSuiteResponse(_message.Message):
    __slots__ = ("suite",)
    SUITE_FIELD_NUMBER: _ClassVar[int]
    suite: ScorerSuiteV1
    def __init__(self, suite: _Optional[_Union[ScorerSuiteV1, _Mapping]] = ...) -> None: ...

class DeleteScorerSuiteRequest(_message.Message):
    __slots__ = ("scorer_suite_id",)
    SCORER_SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    scorer_suite_id: str
    def __init__(self, scorer_suite_id: _Optional[str] = ...) -> None: ...

class DeleteScorerSuiteResponse(_message.Message):
    __slots__ = ("scorer_suite_id",)
    SCORER_SUITE_ID_FIELD_NUMBER: _ClassVar[int]
    scorer_suite_id: str
    def __init__(self, scorer_suite_id: _Optional[str] = ...) -> None: ...

class ScorerAutomationRuleV1(_message.Message):
    __slots__ = ("automation_rule_id", "rule_key", "name", "description", "enabled", "runtime_scope", "scorer_target", "idle_timeout_seconds", "sampling_rate_percent", "trace_filter", "target_selector", "metadata", "created_at", "updated_at", "reasoning_mode", "created_by_user_id")
    AUTOMATION_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_SCOPE_FIELD_NUMBER: _ClassVar[int]
    SCORER_TARGET_FIELD_NUMBER: _ClassVar[int]
    IDLE_TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SAMPLING_RATE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    TRACE_FILTER_FIELD_NUMBER: _ClassVar[int]
    TARGET_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    REASONING_MODE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    automation_rule_id: str
    rule_key: str
    name: str
    description: str
    enabled: bool
    runtime_scope: ScorerAutomationRuntimeScopeV1
    scorer_target: ExperimentRunScorerTargetV1
    idle_timeout_seconds: int
    sampling_rate_percent: float
    trace_filter: ListTraceInvestigationsRequest
    target_selector: ScorerTargetSelectorV1
    metadata: _struct_pb2.Struct
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    reasoning_mode: ScorerReasoningModeV1
    created_by_user_id: str
    def __init__(self, automation_rule_id: _Optional[str] = ..., rule_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., enabled: _Optional[bool] = ..., runtime_scope: _Optional[_Union[ScorerAutomationRuntimeScopeV1, str]] = ..., scorer_target: _Optional[_Union[ExperimentRunScorerTargetV1, _Mapping]] = ..., idle_timeout_seconds: _Optional[int] = ..., sampling_rate_percent: _Optional[float] = ..., trace_filter: _Optional[_Union[ListTraceInvestigationsRequest, _Mapping]] = ..., target_selector: _Optional[_Union[ScorerTargetSelectorV1, _Mapping]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., reasoning_mode: _Optional[_Union[ScorerReasoningModeV1, str]] = ..., created_by_user_id: _Optional[str] = ...) -> None: ...

class CreateScorerAutomationRuleRequest(_message.Message):
    __slots__ = ("rule_key", "name", "description", "enabled", "runtime_scope", "scorer_target", "idle_timeout_seconds", "sampling_rate_percent", "trace_filter", "target_selector", "metadata", "reasoning_mode")
    RULE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_SCOPE_FIELD_NUMBER: _ClassVar[int]
    SCORER_TARGET_FIELD_NUMBER: _ClassVar[int]
    IDLE_TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SAMPLING_RATE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    TRACE_FILTER_FIELD_NUMBER: _ClassVar[int]
    TARGET_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    REASONING_MODE_FIELD_NUMBER: _ClassVar[int]
    rule_key: str
    name: str
    description: str
    enabled: bool
    runtime_scope: ScorerAutomationRuntimeScopeV1
    scorer_target: ExperimentRunScorerTargetV1
    idle_timeout_seconds: int
    sampling_rate_percent: float
    trace_filter: ListTraceInvestigationsRequest
    target_selector: ScorerTargetSelectorV1
    metadata: _struct_pb2.Struct
    reasoning_mode: ScorerReasoningModeV1
    def __init__(self, rule_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., enabled: _Optional[bool] = ..., runtime_scope: _Optional[_Union[ScorerAutomationRuntimeScopeV1, str]] = ..., scorer_target: _Optional[_Union[ExperimentRunScorerTargetV1, _Mapping]] = ..., idle_timeout_seconds: _Optional[int] = ..., sampling_rate_percent: _Optional[float] = ..., trace_filter: _Optional[_Union[ListTraceInvestigationsRequest, _Mapping]] = ..., target_selector: _Optional[_Union[ScorerTargetSelectorV1, _Mapping]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., reasoning_mode: _Optional[_Union[ScorerReasoningModeV1, str]] = ...) -> None: ...

class CreateScorerAutomationRuleResponse(_message.Message):
    __slots__ = ("automation_rule",)
    AUTOMATION_RULE_FIELD_NUMBER: _ClassVar[int]
    automation_rule: ScorerAutomationRuleV1
    def __init__(self, automation_rule: _Optional[_Union[ScorerAutomationRuleV1, _Mapping]] = ...) -> None: ...

class GetScorerAutomationRuleRequest(_message.Message):
    __slots__ = ("automation_rule_id",)
    AUTOMATION_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    automation_rule_id: str
    def __init__(self, automation_rule_id: _Optional[str] = ...) -> None: ...

class GetScorerAutomationRuleResponse(_message.Message):
    __slots__ = ("automation_rule",)
    AUTOMATION_RULE_FIELD_NUMBER: _ClassVar[int]
    automation_rule: ScorerAutomationRuleV1
    def __init__(self, automation_rule: _Optional[_Union[ScorerAutomationRuleV1, _Mapping]] = ...) -> None: ...

class ListScorerAutomationRulesRequest(_message.Message):
    __slots__ = ("limit", "offset", "enabled")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    enabled: bool
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., enabled: _Optional[bool] = ...) -> None: ...

class ListScorerAutomationRulesResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ScorerAutomationRuleV1]
    def __init__(self, items: _Optional[_Iterable[_Union[ScorerAutomationRuleV1, _Mapping]]] = ...) -> None: ...

class UpdateScorerAutomationRuleRequest(_message.Message):
    __slots__ = ("automation_rule_id", "rule_key", "name", "description", "enabled", "runtime_scope", "scorer_target", "idle_timeout_seconds", "sampling_rate_percent", "trace_filter", "target_selector", "metadata", "reasoning_mode")
    AUTOMATION_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_SCOPE_FIELD_NUMBER: _ClassVar[int]
    SCORER_TARGET_FIELD_NUMBER: _ClassVar[int]
    IDLE_TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SAMPLING_RATE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    TRACE_FILTER_FIELD_NUMBER: _ClassVar[int]
    TARGET_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    REASONING_MODE_FIELD_NUMBER: _ClassVar[int]
    automation_rule_id: str
    rule_key: str
    name: str
    description: str
    enabled: bool
    runtime_scope: ScorerAutomationRuntimeScopeV1
    scorer_target: ExperimentRunScorerTargetV1
    idle_timeout_seconds: int
    sampling_rate_percent: float
    trace_filter: ListTraceInvestigationsRequest
    target_selector: ScorerTargetSelectorV1
    metadata: _struct_pb2.Struct
    reasoning_mode: ScorerReasoningModeV1
    def __init__(self, automation_rule_id: _Optional[str] = ..., rule_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., enabled: _Optional[bool] = ..., runtime_scope: _Optional[_Union[ScorerAutomationRuntimeScopeV1, str]] = ..., scorer_target: _Optional[_Union[ExperimentRunScorerTargetV1, _Mapping]] = ..., idle_timeout_seconds: _Optional[int] = ..., sampling_rate_percent: _Optional[float] = ..., trace_filter: _Optional[_Union[ListTraceInvestigationsRequest, _Mapping]] = ..., target_selector: _Optional[_Union[ScorerTargetSelectorV1, _Mapping]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., reasoning_mode: _Optional[_Union[ScorerReasoningModeV1, str]] = ...) -> None: ...

class UpdateScorerAutomationRuleResponse(_message.Message):
    __slots__ = ("automation_rule",)
    AUTOMATION_RULE_FIELD_NUMBER: _ClassVar[int]
    automation_rule: ScorerAutomationRuleV1
    def __init__(self, automation_rule: _Optional[_Union[ScorerAutomationRuleV1, _Mapping]] = ...) -> None: ...

class DeleteScorerAutomationRuleRequest(_message.Message):
    __slots__ = ("automation_rule_id",)
    AUTOMATION_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    automation_rule_id: str
    def __init__(self, automation_rule_id: _Optional[str] = ...) -> None: ...

class DeleteScorerAutomationRuleResponse(_message.Message):
    __slots__ = ("automation_rule_id",)
    AUTOMATION_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    automation_rule_id: str
    def __init__(self, automation_rule_id: _Optional[str] = ...) -> None: ...

class ScorerAutomationExecutionV1(_message.Message):
    __slots__ = ("automation_execution_id", "automation_rule_id", "runtime_scope", "trace_id", "session_id", "state", "eval_job_count", "score_count", "warning_count", "error", "sampling_key", "sampling_hash", "sampling_value_percent", "selected_by_sampling", "idle_eligible", "eligible_after", "resolved_target", "execution_summary", "metadata", "created_by_user_id", "finished_at", "created_at", "updated_at")
    AUTOMATION_EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    AUTOMATION_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_SCOPE_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    EVAL_JOB_COUNT_FIELD_NUMBER: _ClassVar[int]
    SCORE_COUNT_FIELD_NUMBER: _ClassVar[int]
    WARNING_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SAMPLING_KEY_FIELD_NUMBER: _ClassVar[int]
    SAMPLING_HASH_FIELD_NUMBER: _ClassVar[int]
    SAMPLING_VALUE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    SELECTED_BY_SAMPLING_FIELD_NUMBER: _ClassVar[int]
    IDLE_ELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    ELIGIBLE_AFTER_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_TARGET_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    automation_execution_id: str
    automation_rule_id: str
    runtime_scope: str
    trace_id: str
    session_id: str
    state: ScorerAutomationExecutionStateV1
    eval_job_count: int
    score_count: int
    warning_count: int
    error: str
    sampling_key: str
    sampling_hash: str
    sampling_value_percent: float
    selected_by_sampling: bool
    idle_eligible: bool
    eligible_after: _timestamp_pb2.Timestamp
    resolved_target: ResolvedScorerTargetV1
    execution_summary: _struct_pb2.Struct
    metadata: _struct_pb2.Struct
    created_by_user_id: str
    finished_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, automation_execution_id: _Optional[str] = ..., automation_rule_id: _Optional[str] = ..., runtime_scope: _Optional[str] = ..., trace_id: _Optional[str] = ..., session_id: _Optional[str] = ..., state: _Optional[_Union[ScorerAutomationExecutionStateV1, str]] = ..., eval_job_count: _Optional[int] = ..., score_count: _Optional[int] = ..., warning_count: _Optional[int] = ..., error: _Optional[str] = ..., sampling_key: _Optional[str] = ..., sampling_hash: _Optional[str] = ..., sampling_value_percent: _Optional[float] = ..., selected_by_sampling: _Optional[bool] = ..., idle_eligible: _Optional[bool] = ..., eligible_after: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., resolved_target: _Optional[_Union[ResolvedScorerTargetV1, _Mapping]] = ..., execution_summary: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., created_by_user_id: _Optional[str] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListScorerAutomationExecutionsRequest(_message.Message):
    __slots__ = ("automation_rule_id", "states", "limit", "offset")
    AUTOMATION_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    automation_rule_id: str
    states: _containers.RepeatedScalarFieldContainer[ScorerAutomationExecutionStateV1]
    limit: int
    offset: int
    def __init__(self, automation_rule_id: _Optional[str] = ..., states: _Optional[_Iterable[_Union[ScorerAutomationExecutionStateV1, str]]] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListScorerAutomationExecutionsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ScorerAutomationExecutionV1]
    def __init__(self, items: _Optional[_Iterable[_Union[ScorerAutomationExecutionV1, _Mapping]]] = ...) -> None: ...

class GetScorerAutomationExecutionRequest(_message.Message):
    __slots__ = ("automation_execution_id",)
    AUTOMATION_EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    automation_execution_id: str
    def __init__(self, automation_execution_id: _Optional[str] = ...) -> None: ...

class GetScorerAutomationExecutionResponse(_message.Message):
    __slots__ = ("automation_execution",)
    AUTOMATION_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    automation_execution: ScorerAutomationExecutionV1
    def __init__(self, automation_execution: _Optional[_Union[ScorerAutomationExecutionV1, _Mapping]] = ...) -> None: ...

class RunScorerAutomationWorkerOnceRequest(_message.Message):
    __slots__ = ("rule_limit", "trace_limit_per_rule")
    RULE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TRACE_LIMIT_PER_RULE_FIELD_NUMBER: _ClassVar[int]
    rule_limit: int
    trace_limit_per_rule: int
    def __init__(self, rule_limit: _Optional[int] = ..., trace_limit_per_rule: _Optional[int] = ...) -> None: ...

class RunScorerAutomationWorkerOnceResponse(_message.Message):
    __slots__ = ("loaded_rule_count", "matched_trace_count", "idle_eligible_trace_count", "sampled_trace_count", "claimed_trace_count", "skipped_by_idle_count", "skipped_by_sampling_count", "skipped_by_dedupe_count", "created_execution_count", "created_eval_job_count", "dispatched_eval_job_count", "failed_execution_count", "warnings", "reclaimed_execution_count", "abandoned_execution_count", "lost_lease_count")
    LOADED_RULE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MATCHED_TRACE_COUNT_FIELD_NUMBER: _ClassVar[int]
    IDLE_ELIGIBLE_TRACE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SAMPLED_TRACE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CLAIMED_TRACE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_BY_IDLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_BY_SAMPLING_COUNT_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_BY_DEDUPE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATED_EXECUTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATED_EVAL_JOB_COUNT_FIELD_NUMBER: _ClassVar[int]
    DISPATCHED_EVAL_JOB_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_EXECUTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    RECLAIMED_EXECUTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    ABANDONED_EXECUTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    LOST_LEASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    loaded_rule_count: int
    matched_trace_count: int
    idle_eligible_trace_count: int
    sampled_trace_count: int
    claimed_trace_count: int
    skipped_by_idle_count: int
    skipped_by_sampling_count: int
    skipped_by_dedupe_count: int
    created_execution_count: int
    created_eval_job_count: int
    dispatched_eval_job_count: int
    failed_execution_count: int
    warnings: _containers.RepeatedScalarFieldContainer[str]
    reclaimed_execution_count: int
    abandoned_execution_count: int
    lost_lease_count: int
    def __init__(self, loaded_rule_count: _Optional[int] = ..., matched_trace_count: _Optional[int] = ..., idle_eligible_trace_count: _Optional[int] = ..., sampled_trace_count: _Optional[int] = ..., claimed_trace_count: _Optional[int] = ..., skipped_by_idle_count: _Optional[int] = ..., skipped_by_sampling_count: _Optional[int] = ..., skipped_by_dedupe_count: _Optional[int] = ..., created_execution_count: _Optional[int] = ..., created_eval_job_count: _Optional[int] = ..., dispatched_eval_job_count: _Optional[int] = ..., failed_execution_count: _Optional[int] = ..., warnings: _Optional[_Iterable[str]] = ..., reclaimed_execution_count: _Optional[int] = ..., abandoned_execution_count: _Optional[int] = ..., lost_lease_count: _Optional[int] = ...) -> None: ...

class ArchiveScoreConfigRequest(_message.Message):
    __slots__ = ("score_config_id",)
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    def __init__(self, score_config_id: _Optional[str] = ...) -> None: ...

class ArchiveScoreConfigResponse(_message.Message):
    __slots__ = ("score_config",)
    SCORE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    score_config: ScoreConfigV1
    def __init__(self, score_config: _Optional[_Union[ScoreConfigV1, _Mapping]] = ...) -> None: ...

class DeleteScoreConfigRequest(_message.Message):
    __slots__ = ("score_config_id",)
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    def __init__(self, score_config_id: _Optional[str] = ...) -> None: ...

class DeleteScoreConfigResponse(_message.Message):
    __slots__ = ("score_config_id",)
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    def __init__(self, score_config_id: _Optional[str] = ...) -> None: ...

class CreateEvalJobRequest(_message.Message):
    __slots__ = ("score_config_id", "correlation", "input_payload", "subject_output", "expected_output", "metadata")
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_FIELD_NUMBER: _ClassVar[int]
    INPUT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    score_config_id: str
    correlation: CorrelationContextV1
    input_payload: _struct_pb2.Struct
    subject_output: _struct_pb2.Struct
    expected_output: _struct_pb2.Struct
    metadata: _struct_pb2.Struct
    def __init__(self, score_config_id: _Optional[str] = ..., correlation: _Optional[_Union[CorrelationContextV1, _Mapping]] = ..., input_payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., subject_output: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., expected_output: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class CreateEvalJobResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: EvalJobV1
    def __init__(self, job: _Optional[_Union[EvalJobV1, _Mapping]] = ...) -> None: ...

class ListEvalJobsRequest(_message.Message):
    __slots__ = ("states", "limit", "offset")
    STATES_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    states: _containers.RepeatedScalarFieldContainer[EvalJobStateV1]
    limit: int
    offset: int
    def __init__(self, states: _Optional[_Iterable[_Union[EvalJobStateV1, str]]] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListEvalJobsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[EvalJobV1]
    def __init__(self, items: _Optional[_Iterable[_Union[EvalJobV1, _Mapping]]] = ...) -> None: ...

class GetEvalJobRequest(_message.Message):
    __slots__ = ("eval_job_id",)
    EVAL_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    eval_job_id: str
    def __init__(self, eval_job_id: _Optional[str] = ...) -> None: ...

class GetEvalJobResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: EvalJobV1
    def __init__(self, job: _Optional[_Union[EvalJobV1, _Mapping]] = ...) -> None: ...

class RetryEvalJobRequest(_message.Message):
    __slots__ = ("eval_job_id",)
    EVAL_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    eval_job_id: str
    def __init__(self, eval_job_id: _Optional[str] = ...) -> None: ...

class RetryEvalJobResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: EvalJobV1
    def __init__(self, job: _Optional[_Union[EvalJobV1, _Mapping]] = ...) -> None: ...

class ReplayEvalJobRequest(_message.Message):
    __slots__ = ("eval_job_id",)
    EVAL_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    eval_job_id: str
    def __init__(self, eval_job_id: _Optional[str] = ...) -> None: ...

class ReplayEvalJobResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: EvalJobV1
    def __init__(self, job: _Optional[_Union[EvalJobV1, _Mapping]] = ...) -> None: ...

class CancelEvalJobRequest(_message.Message):
    __slots__ = ("eval_job_id", "reason")
    EVAL_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    eval_job_id: str
    reason: str
    def __init__(self, eval_job_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class CancelEvalJobResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: EvalJobV1
    def __init__(self, job: _Optional[_Union[EvalJobV1, _Mapping]] = ...) -> None: ...

class RunEvalSchedulerOnceRequest(_message.Message):
    __slots__ = ("limit",)
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    limit: int
    def __init__(self, limit: _Optional[int] = ...) -> None: ...

class RunEvalSchedulerOnceResponse(_message.Message):
    __slots__ = ("leased_jobs", "succeeded_jobs", "retried_jobs", "failed_jobs", "dead_letter_jobs", "async_jobs_spawned", "leased_expansions", "succeeded_expansions", "failed_expansions")
    LEASED_JOBS_FIELD_NUMBER: _ClassVar[int]
    SUCCEEDED_JOBS_FIELD_NUMBER: _ClassVar[int]
    RETRIED_JOBS_FIELD_NUMBER: _ClassVar[int]
    FAILED_JOBS_FIELD_NUMBER: _ClassVar[int]
    DEAD_LETTER_JOBS_FIELD_NUMBER: _ClassVar[int]
    ASYNC_JOBS_SPAWNED_FIELD_NUMBER: _ClassVar[int]
    LEASED_EXPANSIONS_FIELD_NUMBER: _ClassVar[int]
    SUCCEEDED_EXPANSIONS_FIELD_NUMBER: _ClassVar[int]
    FAILED_EXPANSIONS_FIELD_NUMBER: _ClassVar[int]
    leased_jobs: int
    succeeded_jobs: int
    retried_jobs: int
    failed_jobs: int
    dead_letter_jobs: int
    async_jobs_spawned: int
    leased_expansions: int
    succeeded_expansions: int
    failed_expansions: int
    def __init__(self, leased_jobs: _Optional[int] = ..., succeeded_jobs: _Optional[int] = ..., retried_jobs: _Optional[int] = ..., failed_jobs: _Optional[int] = ..., dead_letter_jobs: _Optional[int] = ..., async_jobs_spawned: _Optional[int] = ..., leased_expansions: _Optional[int] = ..., succeeded_expansions: _Optional[int] = ..., failed_expansions: _Optional[int] = ...) -> None: ...

class CreateExperimentRunRequest(_message.Message):
    __slots__ = ("run_key", "name", "experiment_input_id", "score_config_id", "summary", "experiment_target_id", "comparison_role", "baseline_experiment_run_id", "candidate_experiment_run_id", "scorer_target")
    RUN_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_INPUT_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_ROLE_FIELD_NUMBER: _ClassVar[int]
    BASELINE_EXPERIMENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_EXPERIMENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    SCORER_TARGET_FIELD_NUMBER: _ClassVar[int]
    run_key: str
    name: str
    experiment_input_id: str
    score_config_id: str
    summary: _struct_pb2.Struct
    experiment_target_id: str
    comparison_role: ExperimentRunRoleV1
    baseline_experiment_run_id: str
    candidate_experiment_run_id: str
    scorer_target: ExperimentRunScorerTargetV1
    def __init__(self, run_key: _Optional[str] = ..., name: _Optional[str] = ..., experiment_input_id: _Optional[str] = ..., score_config_id: _Optional[str] = ..., summary: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., experiment_target_id: _Optional[str] = ..., comparison_role: _Optional[_Union[ExperimentRunRoleV1, str]] = ..., baseline_experiment_run_id: _Optional[str] = ..., candidate_experiment_run_id: _Optional[str] = ..., scorer_target: _Optional[_Union[ExperimentRunScorerTargetV1, _Mapping]] = ...) -> None: ...

class CreateExperimentRunResponse(_message.Message):
    __slots__ = ("experiment_run",)
    EXPERIMENT_RUN_FIELD_NUMBER: _ClassVar[int]
    experiment_run: ExperimentRunV1
    def __init__(self, experiment_run: _Optional[_Union[ExperimentRunV1, _Mapping]] = ...) -> None: ...

class ListExperimentRunsRequest(_message.Message):
    __slots__ = ("states", "limit", "offset")
    STATES_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    states: _containers.RepeatedScalarFieldContainer[ExperimentRunStateV1]
    limit: int
    offset: int
    def __init__(self, states: _Optional[_Iterable[_Union[ExperimentRunStateV1, str]]] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListExperimentRunsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ExperimentRunV1]
    def __init__(self, items: _Optional[_Iterable[_Union[ExperimentRunV1, _Mapping]]] = ...) -> None: ...

class CompareExperimentRunsRequest(_message.Message):
    __slots__ = ("baseline_experiment_run_id", "comparison_experiment_run_id", "item_limit")
    BASELINE_EXPERIMENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_EXPERIMENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_LIMIT_FIELD_NUMBER: _ClassVar[int]
    baseline_experiment_run_id: str
    comparison_experiment_run_id: str
    item_limit: int
    def __init__(self, baseline_experiment_run_id: _Optional[str] = ..., comparison_experiment_run_id: _Optional[str] = ..., item_limit: _Optional[int] = ...) -> None: ...

class CompareExperimentRunsResponse(_message.Message):
    __slots__ = ("comparison", "item_comparisons")
    COMPARISON_FIELD_NUMBER: _ClassVar[int]
    ITEM_COMPARISONS_FIELD_NUMBER: _ClassVar[int]
    comparison: ExperimentRunComparisonV1
    item_comparisons: _containers.RepeatedCompositeFieldContainer[ExperimentRunItemComparisonV1]
    def __init__(self, comparison: _Optional[_Union[ExperimentRunComparisonV1, _Mapping]] = ..., item_comparisons: _Optional[_Iterable[_Union[ExperimentRunItemComparisonV1, _Mapping]]] = ...) -> None: ...

class CompareTraceAgenticContextsRequest(_message.Message):
    __slots__ = ("baseline_trace_id", "comparison_trace_id", "limit")
    BASELINE_TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    baseline_trace_id: str
    comparison_trace_id: str
    limit: int
    def __init__(self, baseline_trace_id: _Optional[str] = ..., comparison_trace_id: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class CompareTraceAgenticContextsResponse(_message.Message):
    __slots__ = ("comparison",)
    COMPARISON_FIELD_NUMBER: _ClassVar[int]
    comparison: TraceAgenticComparisonV1
    def __init__(self, comparison: _Optional[_Union[TraceAgenticComparisonV1, _Mapping]] = ...) -> None: ...

class GetExperimentRunRequest(_message.Message):
    __slots__ = ("experiment_run_id", "states", "limit", "offset", "filter", "sort")
    EXPERIMENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    experiment_run_id: str
    states: _containers.RepeatedScalarFieldContainer[EvalJobStateV1]
    limit: int
    offset: int
    filter: ExperimentRunItemFilterV1
    sort: ExperimentRunItemSortV1
    def __init__(self, experiment_run_id: _Optional[str] = ..., states: _Optional[_Iterable[_Union[EvalJobStateV1, str]]] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ..., filter: _Optional[_Union[ExperimentRunItemFilterV1, _Mapping]] = ..., sort: _Optional[_Union[ExperimentRunItemSortV1, _Mapping]] = ...) -> None: ...

class GetExperimentRunResponse(_message.Message):
    __slots__ = ("experiment_run", "input", "items", "score_config", "evaluator_template", "execution_target", "run_summary", "item_details", "artifact_summary", "rich_summary")
    EXPERIMENT_RUN_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    SCORE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TARGET_FIELD_NUMBER: _ClassVar[int]
    RUN_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    ITEM_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    RICH_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    experiment_run: ExperimentRunV1
    input: ExperimentInputV1
    items: _containers.RepeatedCompositeFieldContainer[ExperimentRunItemV1]
    score_config: ScoreConfigV1
    evaluator_template: EvaluatorTemplateV1
    execution_target: ExperimentExecutionTargetSnapshotV1
    run_summary: ExperimentRunSummaryV1
    item_details: _containers.RepeatedCompositeFieldContainer[ExperimentRunItemDetailV1]
    artifact_summary: ExperimentRunArtifactSummaryV1
    rich_summary: ExperimentRunRichSummaryV1
    def __init__(self, experiment_run: _Optional[_Union[ExperimentRunV1, _Mapping]] = ..., input: _Optional[_Union[ExperimentInputV1, _Mapping]] = ..., items: _Optional[_Iterable[_Union[ExperimentRunItemV1, _Mapping]]] = ..., score_config: _Optional[_Union[ScoreConfigV1, _Mapping]] = ..., evaluator_template: _Optional[_Union[EvaluatorTemplateV1, _Mapping]] = ..., execution_target: _Optional[_Union[ExperimentExecutionTargetSnapshotV1, _Mapping]] = ..., run_summary: _Optional[_Union[ExperimentRunSummaryV1, _Mapping]] = ..., item_details: _Optional[_Iterable[_Union[ExperimentRunItemDetailV1, _Mapping]]] = ..., artifact_summary: _Optional[_Union[ExperimentRunArtifactSummaryV1, _Mapping]] = ..., rich_summary: _Optional[_Union[ExperimentRunRichSummaryV1, _Mapping]] = ...) -> None: ...

class GetExperimentRunItemRequest(_message.Message):
    __slots__ = ("experiment_run_item_id",)
    EXPERIMENT_RUN_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    experiment_run_item_id: str
    def __init__(self, experiment_run_item_id: _Optional[str] = ...) -> None: ...

class GetExperimentRunItemResponse(_message.Message):
    __slots__ = ("experiment_run_item", "detail")
    EXPERIMENT_RUN_ITEM_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    experiment_run_item: ExperimentRunItemV1
    detail: ExperimentRunItemDetailV1
    def __init__(self, experiment_run_item: _Optional[_Union[ExperimentRunItemV1, _Mapping]] = ..., detail: _Optional[_Union[ExperimentRunItemDetailV1, _Mapping]] = ...) -> None: ...

class ListExperimentRunItemsRequest(_message.Message):
    __slots__ = ("experiment_run_id", "states", "limit", "offset", "filter", "sort")
    EXPERIMENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    experiment_run_id: str
    states: _containers.RepeatedScalarFieldContainer[EvalJobStateV1]
    limit: int
    offset: int
    filter: ExperimentRunItemFilterV1
    sort: ExperimentRunItemSortV1
    def __init__(self, experiment_run_id: _Optional[str] = ..., states: _Optional[_Iterable[_Union[EvalJobStateV1, str]]] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ..., filter: _Optional[_Union[ExperimentRunItemFilterV1, _Mapping]] = ..., sort: _Optional[_Union[ExperimentRunItemSortV1, _Mapping]] = ...) -> None: ...

class ListExperimentRunItemsResponse(_message.Message):
    __slots__ = ("items", "item_details")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    ITEM_DETAILS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ExperimentRunItemV1]
    item_details: _containers.RepeatedCompositeFieldContainer[ExperimentRunItemDetailV1]
    def __init__(self, items: _Optional[_Iterable[_Union[ExperimentRunItemV1, _Mapping]]] = ..., item_details: _Optional[_Iterable[_Union[ExperimentRunItemDetailV1, _Mapping]]] = ...) -> None: ...

class CreateReleaseGateRequest(_message.Message):
    __slots__ = ("gate_key", "name", "metric_name", "deployment_id", "baseline_deployment_id", "evaluation_window_hours", "min_samples", "max_score_regression", "max_avg_cost_usd", "max_bad_outcomes", "config", "destination_ids", "customer_priority_policy_id", "service_name", "namespace", "environment", "policy")
    GATE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    BASELINE_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_WINDOW_HOURS_FIELD_NUMBER: _ClassVar[int]
    MIN_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    MAX_SCORE_REGRESSION_FIELD_NUMBER: _ClassVar[int]
    MAX_AVG_COST_USD_FIELD_NUMBER: _ClassVar[int]
    MAX_BAD_OUTCOMES_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_IDS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_PRIORITY_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    gate_key: str
    name: str
    metric_name: str
    deployment_id: str
    baseline_deployment_id: str
    evaluation_window_hours: int
    min_samples: int
    max_score_regression: float
    max_avg_cost_usd: float
    max_bad_outcomes: int
    config: _struct_pb2.Struct
    destination_ids: _containers.RepeatedScalarFieldContainer[str]
    customer_priority_policy_id: str
    service_name: str
    namespace: str
    environment: str
    policy: ReleaseGatePolicyV1
    def __init__(self, gate_key: _Optional[str] = ..., name: _Optional[str] = ..., metric_name: _Optional[str] = ..., deployment_id: _Optional[str] = ..., baseline_deployment_id: _Optional[str] = ..., evaluation_window_hours: _Optional[int] = ..., min_samples: _Optional[int] = ..., max_score_regression: _Optional[float] = ..., max_avg_cost_usd: _Optional[float] = ..., max_bad_outcomes: _Optional[int] = ..., config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., destination_ids: _Optional[_Iterable[str]] = ..., customer_priority_policy_id: _Optional[str] = ..., service_name: _Optional[str] = ..., namespace: _Optional[str] = ..., environment: _Optional[str] = ..., policy: _Optional[_Union[ReleaseGatePolicyV1, _Mapping]] = ...) -> None: ...

class CreateReleaseGateResponse(_message.Message):
    __slots__ = ("gate",)
    GATE_FIELD_NUMBER: _ClassVar[int]
    gate: ReleaseGateV1
    def __init__(self, gate: _Optional[_Union[ReleaseGateV1, _Mapping]] = ...) -> None: ...

class GetReleaseGateRequest(_message.Message):
    __slots__ = ("gate_id",)
    GATE_ID_FIELD_NUMBER: _ClassVar[int]
    gate_id: str
    def __init__(self, gate_id: _Optional[str] = ...) -> None: ...

class GetReleaseGateResponse(_message.Message):
    __slots__ = ("gate", "latest_evaluation", "last_successful_baseline_evaluation", "delivery_summary", "fix_queue_group_keys")
    GATE_FIELD_NUMBER: _ClassVar[int]
    LATEST_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    LAST_SUCCESSFUL_BASELINE_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    FIX_QUEUE_GROUP_KEYS_FIELD_NUMBER: _ClassVar[int]
    gate: ReleaseGateV1
    latest_evaluation: ReleaseGateEvaluationV1
    last_successful_baseline_evaluation: ReleaseGateEvaluationV1
    delivery_summary: ReleaseGateDeliverySummaryV1
    fix_queue_group_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, gate: _Optional[_Union[ReleaseGateV1, _Mapping]] = ..., latest_evaluation: _Optional[_Union[ReleaseGateEvaluationV1, _Mapping]] = ..., last_successful_baseline_evaluation: _Optional[_Union[ReleaseGateEvaluationV1, _Mapping]] = ..., delivery_summary: _Optional[_Union[ReleaseGateDeliverySummaryV1, _Mapping]] = ..., fix_queue_group_keys: _Optional[_Iterable[str]] = ...) -> None: ...

class ListReleaseGatesRequest(_message.Message):
    __slots__ = ("limit", "offset")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ReleaseGateListItemV1(_message.Message):
    __slots__ = ("gate", "latest_evaluation", "last_successful_baseline_evaluation", "delivery_summary", "fix_queue_group_keys")
    GATE_FIELD_NUMBER: _ClassVar[int]
    LATEST_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    LAST_SUCCESSFUL_BASELINE_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    FIX_QUEUE_GROUP_KEYS_FIELD_NUMBER: _ClassVar[int]
    gate: ReleaseGateV1
    latest_evaluation: ReleaseGateEvaluationV1
    last_successful_baseline_evaluation: ReleaseGateEvaluationV1
    delivery_summary: ReleaseGateDeliverySummaryV1
    fix_queue_group_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, gate: _Optional[_Union[ReleaseGateV1, _Mapping]] = ..., latest_evaluation: _Optional[_Union[ReleaseGateEvaluationV1, _Mapping]] = ..., last_successful_baseline_evaluation: _Optional[_Union[ReleaseGateEvaluationV1, _Mapping]] = ..., delivery_summary: _Optional[_Union[ReleaseGateDeliverySummaryV1, _Mapping]] = ..., fix_queue_group_keys: _Optional[_Iterable[str]] = ...) -> None: ...

class ListReleaseGatesResponse(_message.Message):
    __slots__ = ("items", "summaries")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ReleaseGateV1]
    summaries: _containers.RepeatedCompositeFieldContainer[ReleaseGateListItemV1]
    def __init__(self, items: _Optional[_Iterable[_Union[ReleaseGateV1, _Mapping]]] = ..., summaries: _Optional[_Iterable[_Union[ReleaseGateListItemV1, _Mapping]]] = ...) -> None: ...

class UpdateReleaseGateRequest(_message.Message):
    __slots__ = ("gate_id", "gate_key", "name", "metric_name", "deployment_id", "baseline_deployment_id", "evaluation_window_hours", "min_samples", "max_score_regression", "max_avg_cost_usd", "max_bad_outcomes", "config", "destination_ids", "customer_priority_policy_id", "service_name", "namespace", "environment", "policy")
    GATE_ID_FIELD_NUMBER: _ClassVar[int]
    GATE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    BASELINE_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_WINDOW_HOURS_FIELD_NUMBER: _ClassVar[int]
    MIN_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    MAX_SCORE_REGRESSION_FIELD_NUMBER: _ClassVar[int]
    MAX_AVG_COST_USD_FIELD_NUMBER: _ClassVar[int]
    MAX_BAD_OUTCOMES_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_IDS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_PRIORITY_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    gate_id: str
    gate_key: str
    name: str
    metric_name: str
    deployment_id: str
    baseline_deployment_id: str
    evaluation_window_hours: int
    min_samples: int
    max_score_regression: float
    max_avg_cost_usd: float
    max_bad_outcomes: int
    config: _struct_pb2.Struct
    destination_ids: _containers.RepeatedScalarFieldContainer[str]
    customer_priority_policy_id: str
    service_name: str
    namespace: str
    environment: str
    policy: ReleaseGatePolicyV1
    def __init__(self, gate_id: _Optional[str] = ..., gate_key: _Optional[str] = ..., name: _Optional[str] = ..., metric_name: _Optional[str] = ..., deployment_id: _Optional[str] = ..., baseline_deployment_id: _Optional[str] = ..., evaluation_window_hours: _Optional[int] = ..., min_samples: _Optional[int] = ..., max_score_regression: _Optional[float] = ..., max_avg_cost_usd: _Optional[float] = ..., max_bad_outcomes: _Optional[int] = ..., config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., destination_ids: _Optional[_Iterable[str]] = ..., customer_priority_policy_id: _Optional[str] = ..., service_name: _Optional[str] = ..., namespace: _Optional[str] = ..., environment: _Optional[str] = ..., policy: _Optional[_Union[ReleaseGatePolicyV1, _Mapping]] = ...) -> None: ...

class UpdateReleaseGateResponse(_message.Message):
    __slots__ = ("gate",)
    GATE_FIELD_NUMBER: _ClassVar[int]
    gate: ReleaseGateV1
    def __init__(self, gate: _Optional[_Union[ReleaseGateV1, _Mapping]] = ...) -> None: ...

class DeleteReleaseGateRequest(_message.Message):
    __slots__ = ("gate_id",)
    GATE_ID_FIELD_NUMBER: _ClassVar[int]
    gate_id: str
    def __init__(self, gate_id: _Optional[str] = ...) -> None: ...

class DeleteReleaseGateResponse(_message.Message):
    __slots__ = ("gate_id",)
    GATE_ID_FIELD_NUMBER: _ClassVar[int]
    gate_id: str
    def __init__(self, gate_id: _Optional[str] = ...) -> None: ...

class GetReleaseGateEvaluationRequest(_message.Message):
    __slots__ = ("evaluation_id",)
    EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    evaluation_id: str
    def __init__(self, evaluation_id: _Optional[str] = ...) -> None: ...

class GetReleaseGateEvaluationResponse(_message.Message):
    __slots__ = ("gate", "evaluation")
    GATE_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    gate: ReleaseGateV1
    evaluation: ReleaseGateEvaluationV1
    def __init__(self, gate: _Optional[_Union[ReleaseGateV1, _Mapping]] = ..., evaluation: _Optional[_Union[ReleaseGateEvaluationV1, _Mapping]] = ...) -> None: ...

class ListReleaseGateEvaluationsRequest(_message.Message):
    __slots__ = ("gate_id", "limit", "offset")
    GATE_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    gate_id: str
    limit: int
    offset: int
    def __init__(self, gate_id: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListReleaseGateEvaluationsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ReleaseGateEvaluationV1]
    def __init__(self, items: _Optional[_Iterable[_Union[ReleaseGateEvaluationV1, _Mapping]]] = ...) -> None: ...

class CompareReleaseGateEvaluationsRequest(_message.Message):
    __slots__ = ("baseline_evaluation_id", "comparison_evaluation_id")
    BASELINE_EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    baseline_evaluation_id: str
    comparison_evaluation_id: str
    def __init__(self, baseline_evaluation_id: _Optional[str] = ..., comparison_evaluation_id: _Optional[str] = ...) -> None: ...

class CompareReleaseGateEvaluationsResponse(_message.Message):
    __slots__ = ("comparison",)
    COMPARISON_FIELD_NUMBER: _ClassVar[int]
    comparison: ReleaseGateEvaluationComparisonV1
    def __init__(self, comparison: _Optional[_Union[ReleaseGateEvaluationComparisonV1, _Mapping]] = ...) -> None: ...

class EvaluateReleaseGateRequest(_message.Message):
    __slots__ = ("gate_id",)
    GATE_ID_FIELD_NUMBER: _ClassVar[int]
    gate_id: str
    def __init__(self, gate_id: _Optional[str] = ...) -> None: ...

class EvaluateReleaseGateResponse(_message.Message):
    __slots__ = ("gate", "evaluation")
    GATE_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    gate: ReleaseGateV1
    evaluation: ReleaseGateEvaluationV1
    def __init__(self, gate: _Optional[_Union[ReleaseGateV1, _Mapping]] = ..., evaluation: _Optional[_Union[ReleaseGateEvaluationV1, _Mapping]] = ...) -> None: ...

class SimulateReleaseGateRequest(_message.Message):
    __slots__ = ("gate_id", "deployment_id", "baseline_deployment_id", "evaluation_window_hours", "start", "end")
    GATE_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    BASELINE_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_WINDOW_HOURS_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    gate_id: str
    deployment_id: str
    baseline_deployment_id: str
    evaluation_window_hours: int
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    def __init__(self, gate_id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., baseline_deployment_id: _Optional[str] = ..., evaluation_window_hours: _Optional[int] = ..., start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SimulateReleaseGateResponse(_message.Message):
    __slots__ = ("gate", "evaluation")
    GATE_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    gate: ReleaseGateV1
    evaluation: ReleaseGateEvaluationV1
    def __init__(self, gate: _Optional[_Union[ReleaseGateV1, _Mapping]] = ..., evaluation: _Optional[_Union[ReleaseGateEvaluationV1, _Mapping]] = ...) -> None: ...

class CreateReleaseDestinationRequest(_message.Message):
    __slots__ = ("destination_key", "name", "channel_kind", "enabled", "is_default", "email_recipients", "webhook_url", "webhook_secret_ref", "headers_json")
    DESTINATION_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_KIND_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_URL_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_SECRET_REF_FIELD_NUMBER: _ClassVar[int]
    HEADERS_JSON_FIELD_NUMBER: _ClassVar[int]
    destination_key: str
    name: str
    channel_kind: ReleaseDestinationChannelKindV1
    enabled: bool
    is_default: bool
    email_recipients: _containers.RepeatedScalarFieldContainer[str]
    webhook_url: str
    webhook_secret_ref: str
    headers_json: _struct_pb2.Struct
    def __init__(self, destination_key: _Optional[str] = ..., name: _Optional[str] = ..., channel_kind: _Optional[_Union[ReleaseDestinationChannelKindV1, str]] = ..., enabled: _Optional[bool] = ..., is_default: _Optional[bool] = ..., email_recipients: _Optional[_Iterable[str]] = ..., webhook_url: _Optional[str] = ..., webhook_secret_ref: _Optional[str] = ..., headers_json: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class CreateReleaseDestinationResponse(_message.Message):
    __slots__ = ("release_destination",)
    RELEASE_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    release_destination: ReleaseDestinationV1
    def __init__(self, release_destination: _Optional[_Union[ReleaseDestinationV1, _Mapping]] = ...) -> None: ...

class GetReleaseDestinationRequest(_message.Message):
    __slots__ = ("release_destination_id",)
    RELEASE_DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    release_destination_id: str
    def __init__(self, release_destination_id: _Optional[str] = ...) -> None: ...

class GetReleaseDestinationResponse(_message.Message):
    __slots__ = ("release_destination",)
    RELEASE_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    release_destination: ReleaseDestinationV1
    def __init__(self, release_destination: _Optional[_Union[ReleaseDestinationV1, _Mapping]] = ...) -> None: ...

class ListReleaseDestinationsRequest(_message.Message):
    __slots__ = ("limit", "offset")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListReleaseDestinationsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ReleaseDestinationV1]
    def __init__(self, items: _Optional[_Iterable[_Union[ReleaseDestinationV1, _Mapping]]] = ...) -> None: ...

class UpdateReleaseDestinationRequest(_message.Message):
    __slots__ = ("release_destination_id", "destination_key", "name", "channel_kind", "enabled", "is_default", "email_recipients", "webhook_url", "webhook_secret_ref", "headers_json")
    RELEASE_DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_KIND_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_URL_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_SECRET_REF_FIELD_NUMBER: _ClassVar[int]
    HEADERS_JSON_FIELD_NUMBER: _ClassVar[int]
    release_destination_id: str
    destination_key: str
    name: str
    channel_kind: ReleaseDestinationChannelKindV1
    enabled: bool
    is_default: bool
    email_recipients: _containers.RepeatedScalarFieldContainer[str]
    webhook_url: str
    webhook_secret_ref: str
    headers_json: _struct_pb2.Struct
    def __init__(self, release_destination_id: _Optional[str] = ..., destination_key: _Optional[str] = ..., name: _Optional[str] = ..., channel_kind: _Optional[_Union[ReleaseDestinationChannelKindV1, str]] = ..., enabled: _Optional[bool] = ..., is_default: _Optional[bool] = ..., email_recipients: _Optional[_Iterable[str]] = ..., webhook_url: _Optional[str] = ..., webhook_secret_ref: _Optional[str] = ..., headers_json: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class UpdateReleaseDestinationResponse(_message.Message):
    __slots__ = ("release_destination",)
    RELEASE_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    release_destination: ReleaseDestinationV1
    def __init__(self, release_destination: _Optional[_Union[ReleaseDestinationV1, _Mapping]] = ...) -> None: ...

class DeleteReleaseDestinationRequest(_message.Message):
    __slots__ = ("release_destination_id",)
    RELEASE_DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    release_destination_id: str
    def __init__(self, release_destination_id: _Optional[str] = ...) -> None: ...

class DeleteReleaseDestinationResponse(_message.Message):
    __slots__ = ("release_destination_id",)
    RELEASE_DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    release_destination_id: str
    def __init__(self, release_destination_id: _Optional[str] = ...) -> None: ...

class ListReleaseAlertDeliveriesRequest(_message.Message):
    __slots__ = ("release_gate_id", "release_gate_evaluation_id", "release_destination_id", "state", "limit", "offset")
    RELEASE_GATE_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_GATE_EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    release_gate_id: str
    release_gate_evaluation_id: str
    release_destination_id: str
    state: ReleaseAlertDeliveryStateV1
    limit: int
    offset: int
    def __init__(self, release_gate_id: _Optional[str] = ..., release_gate_evaluation_id: _Optional[str] = ..., release_destination_id: _Optional[str] = ..., state: _Optional[_Union[ReleaseAlertDeliveryStateV1, str]] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListReleaseAlertDeliveriesResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ReleaseAlertDeliveryV1]
    def __init__(self, items: _Optional[_Iterable[_Union[ReleaseAlertDeliveryV1, _Mapping]]] = ...) -> None: ...

class GetReleaseAlertDeliveryRequest(_message.Message):
    __slots__ = ("release_alert_delivery_id",)
    RELEASE_ALERT_DELIVERY_ID_FIELD_NUMBER: _ClassVar[int]
    release_alert_delivery_id: str
    def __init__(self, release_alert_delivery_id: _Optional[str] = ...) -> None: ...

class GetReleaseAlertDeliveryResponse(_message.Message):
    __slots__ = ("release_alert_delivery",)
    RELEASE_ALERT_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    release_alert_delivery: ReleaseAlertDeliveryV1
    def __init__(self, release_alert_delivery: _Optional[_Union[ReleaseAlertDeliveryV1, _Mapping]] = ...) -> None: ...

class AcknowledgeReleaseAlertRequest(_message.Message):
    __slots__ = ("release_alert_delivery_id",)
    RELEASE_ALERT_DELIVERY_ID_FIELD_NUMBER: _ClassVar[int]
    release_alert_delivery_id: str
    def __init__(self, release_alert_delivery_id: _Optional[str] = ...) -> None: ...

class AcknowledgeReleaseAlertResponse(_message.Message):
    __slots__ = ("release_alert_delivery",)
    RELEASE_ALERT_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    release_alert_delivery: ReleaseAlertDeliveryV1
    def __init__(self, release_alert_delivery: _Optional[_Union[ReleaseAlertDeliveryV1, _Mapping]] = ...) -> None: ...

class SuppressReleaseAlertRequest(_message.Message):
    __slots__ = ("release_alert_delivery_id", "note")
    RELEASE_ALERT_DELIVERY_ID_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    release_alert_delivery_id: str
    note: str
    def __init__(self, release_alert_delivery_id: _Optional[str] = ..., note: _Optional[str] = ...) -> None: ...

class SuppressReleaseAlertResponse(_message.Message):
    __slots__ = ("release_alert_delivery",)
    RELEASE_ALERT_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    release_alert_delivery: ReleaseAlertDeliveryV1
    def __init__(self, release_alert_delivery: _Optional[_Union[ReleaseAlertDeliveryV1, _Mapping]] = ...) -> None: ...

class EscalateReleaseAlertRequest(_message.Message):
    __slots__ = ("release_alert_delivery_id", "note")
    RELEASE_ALERT_DELIVERY_ID_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    release_alert_delivery_id: str
    note: str
    def __init__(self, release_alert_delivery_id: _Optional[str] = ..., note: _Optional[str] = ...) -> None: ...

class EscalateReleaseAlertResponse(_message.Message):
    __slots__ = ("release_alert_delivery",)
    RELEASE_ALERT_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    release_alert_delivery: ReleaseAlertDeliveryV1
    def __init__(self, release_alert_delivery: _Optional[_Union[ReleaseAlertDeliveryV1, _Mapping]] = ...) -> None: ...

class ListFixQueueRequest(_message.Message):
    __slots__ = ("lookback_hours", "limit", "failure_threshold", "strategic_customer_ids")
    LOOKBACK_HOURS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    STRATEGIC_CUSTOMER_IDS_FIELD_NUMBER: _ClassVar[int]
    lookback_hours: int
    limit: int
    failure_threshold: float
    strategic_customer_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, lookback_hours: _Optional[int] = ..., limit: _Optional[int] = ..., failure_threshold: _Optional[float] = ..., strategic_customer_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ListFixQueueResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[FixQueueItemV1]
    def __init__(self, items: _Optional[_Iterable[_Union[FixQueueItemV1, _Mapping]]] = ...) -> None: ...

class ListSessionsRequest(_message.Message):
    __slots__ = ("customer_id", "deployment_id", "prompt_version", "limit", "offset", "start", "end")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    deployment_id: str
    prompt_version: str
    limit: int
    offset: int
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    def __init__(self, customer_id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., prompt_version: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ..., start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListSessionsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[SessionV1]
    def __init__(self, items: _Optional[_Iterable[_Union[SessionV1, _Mapping]]] = ...) -> None: ...

class GetSessionRequest(_message.Message):
    __slots__ = ("session_id", "detail_preview_level", "detail_preview_options")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    DETAIL_PREVIEW_LEVEL_FIELD_NUMBER: _ClassVar[int]
    DETAIL_PREVIEW_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    detail_preview_level: TraceInvestigationDetailPreviewLevelV1
    detail_preview_options: TraceInvestigationDetailPreviewOptionsV1
    def __init__(self, session_id: _Optional[str] = ..., detail_preview_level: _Optional[_Union[TraceInvestigationDetailPreviewLevelV1, str]] = ..., detail_preview_options: _Optional[_Union[TraceInvestigationDetailPreviewOptionsV1, _Mapping]] = ...) -> None: ...

class GetSessionResponse(_message.Message):
    __slots__ = ("session", "related_traces", "evidence_graph")
    SESSION_FIELD_NUMBER: _ClassVar[int]
    RELATED_TRACES_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_GRAPH_FIELD_NUMBER: _ClassVar[int]
    session: SessionV1
    related_traces: _containers.RepeatedCompositeFieldContainer[TraceInvestigationRowV1]
    evidence_graph: AgenticEvidenceGraphV1
    def __init__(self, session: _Optional[_Union[SessionV1, _Mapping]] = ..., related_traces: _Optional[_Iterable[_Union[TraceInvestigationRowV1, _Mapping]]] = ..., evidence_graph: _Optional[_Union[AgenticEvidenceGraphV1, _Mapping]] = ...) -> None: ...

class GetAgenticEvidenceGraphRequest(_message.Message):
    __slots__ = ("trace_id", "session_id", "dataset_item_id", "eval_job_id", "experiment_run_item_id", "release_gate_evaluation_id", "annotation_task_id", "agent_run_id", "node_limit")
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    EVAL_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_RUN_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_GATE_EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    trace_id: str
    session_id: str
    dataset_item_id: str
    eval_job_id: str
    experiment_run_item_id: str
    release_gate_evaluation_id: str
    annotation_task_id: str
    agent_run_id: str
    node_limit: int
    def __init__(self, trace_id: _Optional[str] = ..., session_id: _Optional[str] = ..., dataset_item_id: _Optional[str] = ..., eval_job_id: _Optional[str] = ..., experiment_run_item_id: _Optional[str] = ..., release_gate_evaluation_id: _Optional[str] = ..., annotation_task_id: _Optional[str] = ..., agent_run_id: _Optional[str] = ..., node_limit: _Optional[int] = ...) -> None: ...

class GetAgenticEvidenceGraphResponse(_message.Message):
    __slots__ = ("graph",)
    GRAPH_FIELD_NUMBER: _ClassVar[int]
    graph: AgenticEvidenceGraphV1
    def __init__(self, graph: _Optional[_Union[AgenticEvidenceGraphV1, _Mapping]] = ...) -> None: ...

class CreateRoutingPolicyRequest(_message.Message):
    __slots__ = ("policy_key", "name", "description", "is_default", "enabled", "version", "rules_json")
    POLICY_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    RULES_JSON_FIELD_NUMBER: _ClassVar[int]
    policy_key: str
    name: str
    description: str
    is_default: bool
    enabled: bool
    version: int
    rules_json: _struct_pb2.Struct
    def __init__(self, policy_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_default: _Optional[bool] = ..., enabled: _Optional[bool] = ..., version: _Optional[int] = ..., rules_json: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class CreateRoutingPolicyResponse(_message.Message):
    __slots__ = ("routing_policy",)
    ROUTING_POLICY_FIELD_NUMBER: _ClassVar[int]
    routing_policy: RoutingPolicyV1
    def __init__(self, routing_policy: _Optional[_Union[RoutingPolicyV1, _Mapping]] = ...) -> None: ...

class GetRoutingPolicyRequest(_message.Message):
    __slots__ = ("routing_policy_id",)
    ROUTING_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    routing_policy_id: str
    def __init__(self, routing_policy_id: _Optional[str] = ...) -> None: ...

class GetRoutingPolicyResponse(_message.Message):
    __slots__ = ("routing_policy",)
    ROUTING_POLICY_FIELD_NUMBER: _ClassVar[int]
    routing_policy: RoutingPolicyV1
    def __init__(self, routing_policy: _Optional[_Union[RoutingPolicyV1, _Mapping]] = ...) -> None: ...

class ListRoutingPoliciesRequest(_message.Message):
    __slots__ = ("limit", "offset")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListRoutingPoliciesResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[RoutingPolicyV1]
    def __init__(self, items: _Optional[_Iterable[_Union[RoutingPolicyV1, _Mapping]]] = ...) -> None: ...

class UpdateRoutingPolicyRequest(_message.Message):
    __slots__ = ("routing_policy_id", "policy_key", "name", "description", "is_default", "enabled", "version", "rules_json")
    ROUTING_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    RULES_JSON_FIELD_NUMBER: _ClassVar[int]
    routing_policy_id: str
    policy_key: str
    name: str
    description: str
    is_default: bool
    enabled: bool
    version: int
    rules_json: _struct_pb2.Struct
    def __init__(self, routing_policy_id: _Optional[str] = ..., policy_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_default: _Optional[bool] = ..., enabled: _Optional[bool] = ..., version: _Optional[int] = ..., rules_json: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class UpdateRoutingPolicyResponse(_message.Message):
    __slots__ = ("routing_policy",)
    ROUTING_POLICY_FIELD_NUMBER: _ClassVar[int]
    routing_policy: RoutingPolicyV1
    def __init__(self, routing_policy: _Optional[_Union[RoutingPolicyV1, _Mapping]] = ...) -> None: ...

class CompareRoutingPoliciesRequest(_message.Message):
    __slots__ = ("baseline_routing_policy_id", "comparison_routing_policy_id")
    BASELINE_ROUTING_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_ROUTING_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    baseline_routing_policy_id: str
    comparison_routing_policy_id: str
    def __init__(self, baseline_routing_policy_id: _Optional[str] = ..., comparison_routing_policy_id: _Optional[str] = ...) -> None: ...

class CompareRoutingPoliciesResponse(_message.Message):
    __slots__ = ("comparison",)
    COMPARISON_FIELD_NUMBER: _ClassVar[int]
    comparison: RoutingPolicyComparisonV1
    def __init__(self, comparison: _Optional[_Union[RoutingPolicyComparisonV1, _Mapping]] = ...) -> None: ...

class CreateCustomerPriorityPolicyRequest(_message.Message):
    __slots__ = ("policy_key", "name", "description", "is_default", "enabled", "version", "cohorts_json")
    POLICY_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    COHORTS_JSON_FIELD_NUMBER: _ClassVar[int]
    policy_key: str
    name: str
    description: str
    is_default: bool
    enabled: bool
    version: int
    cohorts_json: _struct_pb2.Struct
    def __init__(self, policy_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_default: _Optional[bool] = ..., enabled: _Optional[bool] = ..., version: _Optional[int] = ..., cohorts_json: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class CreateCustomerPriorityPolicyResponse(_message.Message):
    __slots__ = ("customer_priority_policy",)
    CUSTOMER_PRIORITY_POLICY_FIELD_NUMBER: _ClassVar[int]
    customer_priority_policy: CustomerPriorityPolicyV1
    def __init__(self, customer_priority_policy: _Optional[_Union[CustomerPriorityPolicyV1, _Mapping]] = ...) -> None: ...

class GetCustomerPriorityPolicyRequest(_message.Message):
    __slots__ = ("customer_priority_policy_id",)
    CUSTOMER_PRIORITY_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    customer_priority_policy_id: str
    def __init__(self, customer_priority_policy_id: _Optional[str] = ...) -> None: ...

class GetCustomerPriorityPolicyResponse(_message.Message):
    __slots__ = ("customer_priority_policy",)
    CUSTOMER_PRIORITY_POLICY_FIELD_NUMBER: _ClassVar[int]
    customer_priority_policy: CustomerPriorityPolicyV1
    def __init__(self, customer_priority_policy: _Optional[_Union[CustomerPriorityPolicyV1, _Mapping]] = ...) -> None: ...

class ListCustomerPriorityPoliciesRequest(_message.Message):
    __slots__ = ("limit", "offset")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListCustomerPriorityPoliciesResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CustomerPriorityPolicyV1]
    def __init__(self, items: _Optional[_Iterable[_Union[CustomerPriorityPolicyV1, _Mapping]]] = ...) -> None: ...

class UpdateCustomerPriorityPolicyRequest(_message.Message):
    __slots__ = ("customer_priority_policy_id", "policy_key", "name", "description", "is_default", "enabled", "version", "cohorts_json")
    CUSTOMER_PRIORITY_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    COHORTS_JSON_FIELD_NUMBER: _ClassVar[int]
    customer_priority_policy_id: str
    policy_key: str
    name: str
    description: str
    is_default: bool
    enabled: bool
    version: int
    cohorts_json: _struct_pb2.Struct
    def __init__(self, customer_priority_policy_id: _Optional[str] = ..., policy_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_default: _Optional[bool] = ..., enabled: _Optional[bool] = ..., version: _Optional[int] = ..., cohorts_json: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class UpdateCustomerPriorityPolicyResponse(_message.Message):
    __slots__ = ("customer_priority_policy",)
    CUSTOMER_PRIORITY_POLICY_FIELD_NUMBER: _ClassVar[int]
    customer_priority_policy: CustomerPriorityPolicyV1
    def __init__(self, customer_priority_policy: _Optional[_Union[CustomerPriorityPolicyV1, _Mapping]] = ...) -> None: ...

class CompareCustomerPriorityPoliciesRequest(_message.Message):
    __slots__ = ("baseline_customer_priority_policy_id", "comparison_customer_priority_policy_id")
    BASELINE_CUSTOMER_PRIORITY_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_CUSTOMER_PRIORITY_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    baseline_customer_priority_policy_id: str
    comparison_customer_priority_policy_id: str
    def __init__(self, baseline_customer_priority_policy_id: _Optional[str] = ..., comparison_customer_priority_policy_id: _Optional[str] = ...) -> None: ...

class CompareCustomerPriorityPoliciesResponse(_message.Message):
    __slots__ = ("comparison",)
    COMPARISON_FIELD_NUMBER: _ClassVar[int]
    comparison: CustomerPriorityPolicyComparisonV1
    def __init__(self, comparison: _Optional[_Union[CustomerPriorityPolicyComparisonV1, _Mapping]] = ...) -> None: ...

class GetRoutingSignalRequest(_message.Message):
    __slots__ = ("routing_signal_id",)
    ROUTING_SIGNAL_ID_FIELD_NUMBER: _ClassVar[int]
    routing_signal_id: str
    def __init__(self, routing_signal_id: _Optional[str] = ...) -> None: ...

class GetRoutingSignalResponse(_message.Message):
    __slots__ = ("routing_signal",)
    ROUTING_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    routing_signal: RoutingSignalV1
    def __init__(self, routing_signal: _Optional[_Union[RoutingSignalV1, _Mapping]] = ...) -> None: ...

class ListRoutingSignalsRequest(_message.Message):
    __slots__ = ("states", "limit", "offset")
    STATES_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    states: _containers.RepeatedScalarFieldContainer[RoutingSignalStateV1]
    limit: int
    offset: int
    def __init__(self, states: _Optional[_Iterable[_Union[RoutingSignalStateV1, str]]] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListRoutingSignalsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[RoutingSignalV1]
    def __init__(self, items: _Optional[_Iterable[_Union[RoutingSignalV1, _Mapping]]] = ...) -> None: ...

class ReplayRoutingSignalRequest(_message.Message):
    __slots__ = ("routing_signal_id",)
    ROUTING_SIGNAL_ID_FIELD_NUMBER: _ClassVar[int]
    routing_signal_id: str
    def __init__(self, routing_signal_id: _Optional[str] = ...) -> None: ...

class ReplayRoutingSignalResponse(_message.Message):
    __slots__ = ("routing_signal",)
    ROUTING_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    routing_signal: RoutingSignalV1
    def __init__(self, routing_signal: _Optional[_Union[RoutingSignalV1, _Mapping]] = ...) -> None: ...

class ListRoutingAuditsRequest(_message.Message):
    __slots__ = ("routing_signal_id", "limit", "offset")
    ROUTING_SIGNAL_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    routing_signal_id: str
    limit: int
    offset: int
    def __init__(self, routing_signal_id: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListRoutingAuditsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[RoutingAuditV1]
    def __init__(self, items: _Optional[_Iterable[_Union[RoutingAuditV1, _Mapping]]] = ...) -> None: ...

class RunRoutingWorkerOnceRequest(_message.Message):
    __slots__ = ("limit", "per_tenant_limit")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PER_TENANT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    limit: int
    per_tenant_limit: int
    def __init__(self, limit: _Optional[int] = ..., per_tenant_limit: _Optional[int] = ...) -> None: ...

class RunRoutingWorkerOnceResponse(_message.Message):
    __slots__ = ("leased_signals", "materialized_signals", "skipped_signals", "retried_signals", "dead_letter_signals", "created_tasks")
    LEASED_SIGNALS_FIELD_NUMBER: _ClassVar[int]
    MATERIALIZED_SIGNALS_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_SIGNALS_FIELD_NUMBER: _ClassVar[int]
    RETRIED_SIGNALS_FIELD_NUMBER: _ClassVar[int]
    DEAD_LETTER_SIGNALS_FIELD_NUMBER: _ClassVar[int]
    CREATED_TASKS_FIELD_NUMBER: _ClassVar[int]
    leased_signals: int
    materialized_signals: int
    skipped_signals: int
    retried_signals: int
    dead_letter_signals: int
    created_tasks: int
    def __init__(self, leased_signals: _Optional[int] = ..., materialized_signals: _Optional[int] = ..., skipped_signals: _Optional[int] = ..., retried_signals: _Optional[int] = ..., dead_letter_signals: _Optional[int] = ..., created_tasks: _Optional[int] = ...) -> None: ...

class GetAgenticDispatchOutboxEntryRequest(_message.Message):
    __slots__ = ("dispatch_entry_id",)
    DISPATCH_ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    dispatch_entry_id: str
    def __init__(self, dispatch_entry_id: _Optional[str] = ...) -> None: ...

class GetAgenticDispatchOutboxEntryResponse(_message.Message):
    __slots__ = ("entry",)
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    entry: AgenticDispatchOutboxEntryV1
    def __init__(self, entry: _Optional[_Union[AgenticDispatchOutboxEntryV1, _Mapping]] = ...) -> None: ...

class ListAgenticDispatchOutboxEntriesRequest(_message.Message):
    __slots__ = ("states", "kinds", "limit", "offset")
    STATES_FIELD_NUMBER: _ClassVar[int]
    KINDS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    states: _containers.RepeatedScalarFieldContainer[AgenticDispatchStateV1]
    kinds: _containers.RepeatedScalarFieldContainer[AgenticDispatchKindV1]
    limit: int
    offset: int
    def __init__(self, states: _Optional[_Iterable[_Union[AgenticDispatchStateV1, str]]] = ..., kinds: _Optional[_Iterable[_Union[AgenticDispatchKindV1, str]]] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListAgenticDispatchOutboxEntriesResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AgenticDispatchOutboxEntryV1]
    def __init__(self, items: _Optional[_Iterable[_Union[AgenticDispatchOutboxEntryV1, _Mapping]]] = ...) -> None: ...

class RetryAgenticDispatchOutboxEntryRequest(_message.Message):
    __slots__ = ("dispatch_entry_id",)
    DISPATCH_ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    dispatch_entry_id: str
    def __init__(self, dispatch_entry_id: _Optional[str] = ...) -> None: ...

class RetryAgenticDispatchOutboxEntryResponse(_message.Message):
    __slots__ = ("entry",)
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    entry: AgenticDispatchOutboxEntryV1
    def __init__(self, entry: _Optional[_Union[AgenticDispatchOutboxEntryV1, _Mapping]] = ...) -> None: ...

class CreateAnnotationQueueRequest(_message.Message):
    __slots__ = ("queue_key", "name", "description", "routing_reason", "routing_config")
    QUEUE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ROUTING_REASON_FIELD_NUMBER: _ClassVar[int]
    ROUTING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    queue_key: str
    name: str
    description: str
    routing_reason: AnnotationRoutingReasonV1
    routing_config: _struct_pb2.Struct
    def __init__(self, queue_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., routing_reason: _Optional[_Union[AnnotationRoutingReasonV1, str]] = ..., routing_config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class CreateAnnotationQueueResponse(_message.Message):
    __slots__ = ("queue",)
    QUEUE_FIELD_NUMBER: _ClassVar[int]
    queue: AnnotationQueueV1
    def __init__(self, queue: _Optional[_Union[AnnotationQueueV1, _Mapping]] = ...) -> None: ...

class ListAnnotationQueuesRequest(_message.Message):
    __slots__ = ("limit", "offset")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListAnnotationQueuesResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AnnotationQueueV1]
    def __init__(self, items: _Optional[_Iterable[_Union[AnnotationQueueV1, _Mapping]]] = ...) -> None: ...

class GetAnnotationQueueRequest(_message.Message):
    __slots__ = ("queue_id",)
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    queue_id: str
    def __init__(self, queue_id: _Optional[str] = ...) -> None: ...

class GetAnnotationQueueResponse(_message.Message):
    __slots__ = ("queue",)
    QUEUE_FIELD_NUMBER: _ClassVar[int]
    queue: AnnotationQueueV1
    def __init__(self, queue: _Optional[_Union[AnnotationQueueV1, _Mapping]] = ...) -> None: ...

class UpdateAnnotationQueueRequest(_message.Message):
    __slots__ = ("queue_id", "queue_key", "name", "description", "routing_reason", "routing_config")
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    QUEUE_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ROUTING_REASON_FIELD_NUMBER: _ClassVar[int]
    ROUTING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    queue_id: str
    queue_key: str
    name: str
    description: str
    routing_reason: AnnotationRoutingReasonV1
    routing_config: _struct_pb2.Struct
    def __init__(self, queue_id: _Optional[str] = ..., queue_key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., routing_reason: _Optional[_Union[AnnotationRoutingReasonV1, str]] = ..., routing_config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class UpdateAnnotationQueueResponse(_message.Message):
    __slots__ = ("queue",)
    QUEUE_FIELD_NUMBER: _ClassVar[int]
    queue: AnnotationQueueV1
    def __init__(self, queue: _Optional[_Union[AnnotationQueueV1, _Mapping]] = ...) -> None: ...

class ListAnnotationTasksRequest(_message.Message):
    __slots__ = ("queue_id", "states", "limit", "offset", "experiment_run_id", "task_mode", "assigned_user_id", "claimed_by_user_id", "current_user_only")
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_MODE_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CLAIMED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_USER_ONLY_FIELD_NUMBER: _ClassVar[int]
    queue_id: str
    states: _containers.RepeatedScalarFieldContainer[AnnotationTaskStateV1]
    limit: int
    offset: int
    experiment_run_id: str
    task_mode: AnnotationTaskModeV1
    assigned_user_id: str
    claimed_by_user_id: str
    current_user_only: bool
    def __init__(self, queue_id: _Optional[str] = ..., states: _Optional[_Iterable[_Union[AnnotationTaskStateV1, str]]] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ..., experiment_run_id: _Optional[str] = ..., task_mode: _Optional[_Union[AnnotationTaskModeV1, str]] = ..., assigned_user_id: _Optional[str] = ..., claimed_by_user_id: _Optional[str] = ..., current_user_only: _Optional[bool] = ...) -> None: ...

class ListAnnotationTasksResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AnnotationTaskV1]
    def __init__(self, items: _Optional[_Iterable[_Union[AnnotationTaskV1, _Mapping]]] = ...) -> None: ...

class GetAnnotationTaskRequest(_message.Message):
    __slots__ = ("task_id",)
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    def __init__(self, task_id: _Optional[str] = ...) -> None: ...

class GetAnnotationTaskResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: AnnotationTaskV1
    def __init__(self, task: _Optional[_Union[AnnotationTaskV1, _Mapping]] = ...) -> None: ...

class CreatePairwiseAnnotationTaskRequest(_message.Message):
    __slots__ = ("queue_id", "task_key", "title", "summary", "correlation", "evidence", "correction_payload", "resolution_notes", "priority_tier", "assigned_user_id", "due_at", "experiment_run_id", "experiment_run_item_id", "pairwise_refs")
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_KEY_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    CORRECTION_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_NOTES_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_TIER_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_USER_ID_FIELD_NUMBER: _ClassVar[int]
    DUE_AT_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_RUN_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_REFS_FIELD_NUMBER: _ClassVar[int]
    queue_id: str
    task_key: str
    title: str
    summary: str
    correlation: CorrelationContextV1
    evidence: _struct_pb2.Struct
    correction_payload: _struct_pb2.Struct
    resolution_notes: str
    priority_tier: RoutingPriorityTierV1
    assigned_user_id: str
    due_at: _timestamp_pb2.Timestamp
    experiment_run_id: str
    experiment_run_item_id: str
    pairwise_refs: AnnotationPairwiseRefsV1
    def __init__(self, queue_id: _Optional[str] = ..., task_key: _Optional[str] = ..., title: _Optional[str] = ..., summary: _Optional[str] = ..., correlation: _Optional[_Union[CorrelationContextV1, _Mapping]] = ..., evidence: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., correction_payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., resolution_notes: _Optional[str] = ..., priority_tier: _Optional[_Union[RoutingPriorityTierV1, str]] = ..., assigned_user_id: _Optional[str] = ..., due_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., experiment_run_id: _Optional[str] = ..., experiment_run_item_id: _Optional[str] = ..., pairwise_refs: _Optional[_Union[AnnotationPairwiseRefsV1, _Mapping]] = ...) -> None: ...

class CreatePairwiseAnnotationTaskResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: AnnotationTaskV1
    def __init__(self, task: _Optional[_Union[AnnotationTaskV1, _Mapping]] = ...) -> None: ...

class ClaimAnnotationTaskRequest(_message.Message):
    __slots__ = ("task_id", "note")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    note: str
    def __init__(self, task_id: _Optional[str] = ..., note: _Optional[str] = ...) -> None: ...

class ClaimAnnotationTaskResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: AnnotationTaskV1
    def __init__(self, task: _Optional[_Union[AnnotationTaskV1, _Mapping]] = ...) -> None: ...

class SaveAnnotationTaskReviewRequest(_message.Message):
    __slots__ = ("task_id", "correction_payload", "resolution_notes", "pairwise_winner", "clear_correction_payload", "clear_pairwise_winner")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CORRECTION_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_NOTES_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_WINNER_FIELD_NUMBER: _ClassVar[int]
    CLEAR_CORRECTION_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CLEAR_PAIRWISE_WINNER_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    correction_payload: _struct_pb2.Struct
    resolution_notes: str
    pairwise_winner: AnnotationPairwiseWinnerV1
    clear_correction_payload: bool
    clear_pairwise_winner: bool
    def __init__(self, task_id: _Optional[str] = ..., correction_payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., resolution_notes: _Optional[str] = ..., pairwise_winner: _Optional[_Union[AnnotationPairwiseWinnerV1, str]] = ..., clear_correction_payload: _Optional[bool] = ..., clear_pairwise_winner: _Optional[bool] = ...) -> None: ...

class SaveAnnotationTaskReviewResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: AnnotationTaskV1
    def __init__(self, task: _Optional[_Union[AnnotationTaskV1, _Mapping]] = ...) -> None: ...

class ReleaseAnnotationTaskClaimRequest(_message.Message):
    __slots__ = ("task_id", "note")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    note: str
    def __init__(self, task_id: _Optional[str] = ..., note: _Optional[str] = ...) -> None: ...

class ReleaseAnnotationTaskClaimResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: AnnotationTaskV1
    def __init__(self, task: _Optional[_Union[AnnotationTaskV1, _Mapping]] = ...) -> None: ...

class TransferAnnotationTaskClaimRequest(_message.Message):
    __slots__ = ("task_id", "target_user_id", "note")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_USER_ID_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    target_user_id: str
    note: str
    def __init__(self, task_id: _Optional[str] = ..., target_user_id: _Optional[str] = ..., note: _Optional[str] = ...) -> None: ...

class TransferAnnotationTaskClaimResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: AnnotationTaskV1
    def __init__(self, task: _Optional[_Union[AnnotationTaskV1, _Mapping]] = ...) -> None: ...

class CompleteAnnotationTaskRequest(_message.Message):
    __slots__ = ("task_id", "correction_payload", "resolution_notes", "pairwise_winner")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CORRECTION_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_NOTES_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_WINNER_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    correction_payload: _struct_pb2.Struct
    resolution_notes: str
    pairwise_winner: AnnotationPairwiseWinnerV1
    def __init__(self, task_id: _Optional[str] = ..., correction_payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., resolution_notes: _Optional[str] = ..., pairwise_winner: _Optional[_Union[AnnotationPairwiseWinnerV1, str]] = ...) -> None: ...

class CompleteAnnotationTaskResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: AnnotationTaskV1
    def __init__(self, task: _Optional[_Union[AnnotationTaskV1, _Mapping]] = ...) -> None: ...

class ApproveAnnotationTaskRequest(_message.Message):
    __slots__ = ("task_id", "note")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    note: str
    def __init__(self, task_id: _Optional[str] = ..., note: _Optional[str] = ...) -> None: ...

class ApproveAnnotationTaskResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: AnnotationTaskV1
    def __init__(self, task: _Optional[_Union[AnnotationTaskV1, _Mapping]] = ...) -> None: ...

class RejectAnnotationTaskRequest(_message.Message):
    __slots__ = ("task_id", "note")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    note: str
    def __init__(self, task_id: _Optional[str] = ..., note: _Optional[str] = ...) -> None: ...

class RejectAnnotationTaskResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: AnnotationTaskV1
    def __init__(self, task: _Optional[_Union[AnnotationTaskV1, _Mapping]] = ...) -> None: ...

class RequeueAnnotationTaskRequest(_message.Message):
    __slots__ = ("task_id", "note")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    note: str
    def __init__(self, task_id: _Optional[str] = ..., note: _Optional[str] = ...) -> None: ...

class RequeueAnnotationTaskResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: AnnotationTaskV1
    def __init__(self, task: _Optional[_Union[AnnotationTaskV1, _Mapping]] = ...) -> None: ...
