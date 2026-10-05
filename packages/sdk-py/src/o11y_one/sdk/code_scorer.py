"""Code scorers (o11y-api #611): a member authors a Python scorer as a draft,
previews it on one input, and an admin publishes it; only a published version
runs across a dataset.

Three calls, on the same ``AgenticEvaluationServiceClient`` /
``...ClientSync`` the rest of :mod:`o11y_one.sdk.agentic` wraps:

* :meth:`CodeScorerClient.create_code_scorer` uploads the bundle as a draft;
* :meth:`CodeScorerClient.preview_code_scorer` runs the draft once in the
  sandbox and waits, at most ``wait_seconds``, for its result (nothing is
  scored, and it bills);
* :meth:`CodeScorerClient.publish_code_scorer` starts the publication: each
  smoke input runs once, a seeded scorer twice more, and
  ``GetEvaluationScorerConfig`` reads its ``publication_state``.

Inputs are the dicts ``score()`` receives (:class:`o11y_one.sdk.scorer.ScorerInput`);
each field goes over the wire as its JSON text. A typed refusal (the sandbox
unavailable, a bundle or input the sandbox would refuse, a published version)
comes back as a :class:`~o11y_one.sdk.results.Refusal` whose ``reason_code`` is
the rejection kind and whose ``message`` starts with the server's stable code.
"""

from __future__ import annotations

import asyncio
import json
import time
from collections.abc import Mapping, Sequence
from typing import Literal

from connectrpc.errors import ConnectError
from connectrpc.request import Headers
from google.protobuf.internal.enum_type_wrapper import EnumTypeWrapper
from o11y_one.agentic.v1.evaluation_connect import (
    AgenticEvaluationServiceClient,
    AgenticEvaluationServiceClientSync,
)
from o11y_one.agentic.v1.evaluation_pb2 import (
    CreateEvaluationScorerConfigRequest,
    EvaluationCodeScorerJobStateV1,
    EvaluationCodeScorerResultV1,
    EvaluationDeterminismClassV1,
    EvaluationScorerCodeConfigV1,
    EvaluationScorerCodeInputV1,
    EvaluationScorerCodeLanguageV1,
    EvaluationScorerCodeSpecV1,
    EvaluationScorerConfigRejectionKindV1,
    EvaluationScorerConfigRejectionV1,
    EvaluationScorerConfigV1,
    EvaluationScorerInputFieldV1,
    EvaluationScorerKindV1,
    EvaluationScorerLimitProfileRefV1,
    EvaluationScorerLimitProfileV1,
    EvaluationScorerRuntimeProfileRefV1,
    EvaluationScorerSourceFileV1,
    GetEvaluationScorerPreviewRequest,
    PublishEvaluationScorerConfigRequest,
    StartEvaluationScorerPreviewRequest,
)

from .recovery import bare_enum_name, find_error_detail
from .results import Refusal
from .scorer import ScorerInput
from .validation import ValidationError, require_non_empty, require_non_empty_sequence

__all__ = ["CodeScorerClient", "CodeScorerClientSync"]

LimitProfile = Literal["small", "standard", "large"]
Determinism = Literal["seeded_best_effort", "nondeterministic"]


def _named(enum_type: EnumTypeWrapper, prefix: str, *names: str) -> dict[str, int]:
    return {name: enum_type.Value(f"{prefix}_{name.upper()}") for name in names}


_LIMIT_PROFILES = _named(
    EvaluationScorerLimitProfileV1,
    "EVALUATION_SCORER_LIMIT_PROFILE_V1",
    "small",
    "standard",
    "large",
)
_DETERMINISM = _named(
    EvaluationDeterminismClassV1,
    "EVALUATION_DETERMINISM_CLASS_V1",
    "seeded_best_effort",
    "nondeterministic",
)
_INPUT_FIELDS = _named(
    EvaluationScorerInputFieldV1,
    "EVALUATION_SCORER_INPUT_FIELD_V1",
    *ScorerInput.__optional_keys__,
)
_FINISHED = EvaluationCodeScorerJobStateV1.EVALUATION_CODE_SCORER_JOB_STATE_V1_FINISHED


def _choice(table: Mapping[str, int], value: str, *, field: str) -> int:
    if value not in table:
        raise ValidationError(field, f"must be one of {sorted(table)}, got {value!r}")
    return table[value]


def _build_create(
    *,
    config_key: str,
    name: str,
    metric_name: str,
    files: Mapping[str, str | bytes],
    entrypoint_path: str,
    limit_profile: LimitProfile,
    determinism: Determinism,
    input_fields: Sequence[str],
    runtime_profile: tuple[str, int],
    success_dimension: str,
    description: str | None,
    idempotency_key: str,
) -> CreateEvaluationScorerConfigRequest:
    for value, field in ((config_key, "config_key"), (name, "name"), (metric_name, "metric_name")):
        require_non_empty(value, field=field)
    require_non_empty(idempotency_key, field="idempotency_key")
    if entrypoint_path not in files:
        raise ValidationError("entrypoint_path", f"{entrypoint_path!r} is not one of the files")
    # The bundle's paths ascend, as the sandbox requires; the content is the bytes the author wrote.
    sources = [
        EvaluationScorerSourceFileV1(
            path=path, content=content.encode() if isinstance(content, str) else content
        )
        for path, content in sorted(files.items())
    ]
    runtime_id, runtime_version = runtime_profile
    return CreateEvaluationScorerConfigRequest(
        config_key=config_key,
        name=name,
        description=description,
        metric_name=metric_name,
        success_dimension=success_dimension,
        kind=EvaluationScorerKindV1.EVALUATION_SCORER_KIND_V1_CODE,
        idempotency_key=idempotency_key,
        code=EvaluationScorerCodeSpecV1(
            language=EvaluationScorerCodeLanguageV1.EVALUATION_SCORER_CODE_LANGUAGE_V1_PYTHON,
            files=sources,
            entrypoint_path=entrypoint_path,
            runtime_profile=EvaluationScorerRuntimeProfileRefV1(
                id=runtime_id, version=runtime_version
            ),
            # Version 1 is the launch limit table the capability set publishes as `limits_version`.
            limit_profile=EvaluationScorerLimitProfileRefV1(
                id=_choice(_LIMIT_PROFILES, limit_profile, field="limit_profile"), version=1
            ),
            determinism_class=_choice(_DETERMINISM, determinism, field="determinism"),
            input_fields=[
                _choice(_INPUT_FIELDS, field, field="input_fields") for field in input_fields
            ],
        ),
    )


def _code_input(scorer_input: ScorerInput) -> EvaluationScorerCodeInputV1:
    unknown = sorted(set(scorer_input) - set(_INPUT_FIELDS))
    if unknown:
        raise ValidationError(
            "input", f"unknown fields {unknown}; a scorer reads {sorted(_INPUT_FIELDS)}"
        )
    return EvaluationScorerCodeInputV1(
        **{f"{field}_json": json.dumps(value) for field, value in scorer_input.items()}
    )


def _build_preview(
    *, score_config_id: str, scorer_input: ScorerInput, idempotency_key: str
) -> StartEvaluationScorerPreviewRequest:
    require_non_empty(score_config_id, field="score_config_id")
    require_non_empty(idempotency_key, field="idempotency_key")
    return StartEvaluationScorerPreviewRequest(
        score_config_id=score_config_id,
        input=_code_input(scorer_input),
        idempotency_key=idempotency_key,
    )


def _build_publish(
    *, score_config_id: str, smoke_inputs: Sequence[ScorerInput], idempotency_key: str
) -> PublishEvaluationScorerConfigRequest:
    require_non_empty(score_config_id, field="score_config_id")
    require_non_empty(idempotency_key, field="idempotency_key")
    require_non_empty_sequence(smoke_inputs, field="smoke_inputs")
    return PublishEvaluationScorerConfigRequest(
        score_config_id=score_config_id,
        smoke_inputs=[_code_input(smoke) for smoke in smoke_inputs],
        idempotency_key=idempotency_key,
    )


def _refusal(err: ConnectError) -> Refusal:
    detail = find_error_detail(err, EvaluationScorerConfigRejectionV1)
    if detail is None:
        raise err
    return Refusal(
        reason_code=bare_enum_name(EvaluationScorerConfigRejectionKindV1, detail.kind),
        message=f"{detail.reason_code}: {detail.detail}" if detail.detail else detail.reason_code,
    )


def _check_wait(wait_seconds: float, poll_interval_seconds: float) -> None:
    if wait_seconds < 0 or poll_interval_seconds <= 0:
        raise ValidationError("wait_seconds", "waits at least 0 s, polling at a positive interval")


def _timed_out(preview_id: str, wait_seconds: float) -> TimeoutError:
    return TimeoutError(
        f"preview {preview_id} has not finished after {wait_seconds} s; "
        "read it again with GetEvaluationScorerPreview"
    )


class CodeScorerClient:
    """Code scorer authoring over ``AgenticEvaluationServiceClient``."""

    def __init__(self, client: AgenticEvaluationServiceClient) -> None:
        self._client = client

    async def create_code_scorer(
        self,
        *,
        config_key: str,
        name: str,
        metric_name: str,
        files: Mapping[str, str | bytes],
        idempotency_key: str,
        entrypoint_path: str = "score.py",
        limit_profile: LimitProfile = "standard",
        determinism: Determinism = "seeded_best_effort",
        input_fields: Sequence[str] = (),
        runtime_profile: tuple[str, int] = ("python-3.14", 1),
        success_dimension: str = "quality",
        description: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> EvaluationScorerConfigV1 | Refusal:
        """Upload ``files`` (bundle path to source) as a member draft. An empty
        ``input_fields`` reads the case input, the candidate output and the
        reference output."""
        req = _build_create(
            config_key=config_key,
            name=name,
            metric_name=metric_name,
            files=files,
            entrypoint_path=entrypoint_path,
            limit_profile=limit_profile,
            determinism=determinism,
            input_fields=input_fields,
            runtime_profile=runtime_profile,
            success_dimension=success_dimension,
            description=description,
            idempotency_key=idempotency_key,
        )
        try:
            resp = await self._client.create_evaluation_scorer_config(
                req, headers=headers, timeout_ms=timeout_ms
            )
        except ConnectError as err:
            return _refusal(err)
        return resp.scorer_config

    async def preview_code_scorer(
        self,
        *,
        score_config_id: str,
        scorer_input: ScorerInput,
        idempotency_key: str,
        wait_seconds: float = 120.0,
        poll_interval_seconds: float = 1.0,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> EvaluationCodeScorerResultV1 | Refusal:
        """Run the scorer once on ``scorer_input`` and return its finished result.

        Raises :class:`TimeoutError` once ``wait_seconds`` pass without one; the
        preview keeps running, and replaying ``idempotency_key`` resumes the wait.
        """
        _check_wait(wait_seconds, poll_interval_seconds)
        req = _build_preview(
            score_config_id=score_config_id,
            scorer_input=scorer_input,
            idempotency_key=idempotency_key,
        )
        try:
            started = await self._client.start_evaluation_scorer_preview(
                req, headers=headers, timeout_ms=timeout_ms
            )
        except ConnectError as err:
            return _refusal(err)
        deadline = time.monotonic() + wait_seconds
        read = GetEvaluationScorerPreviewRequest(preview_id=started.preview_id)
        while True:
            got = await self._client.get_evaluation_scorer_preview(
                read, headers=headers, timeout_ms=timeout_ms
            )
            if got.result.state == _FINISHED:
                return got.result
            if time.monotonic() >= deadline:
                raise _timed_out(started.preview_id, wait_seconds)
            await asyncio.sleep(poll_interval_seconds)

    async def publish_code_scorer(
        self,
        *,
        score_config_id: str,
        smoke_inputs: Sequence[ScorerInput],
        idempotency_key: str,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> EvaluationScorerCodeConfigV1 | Refusal:
        """Start publishing the draft (admin): 1 to 3 smoke inputs. The answer
        reads ``PUBLISHING``; ``GetEvaluationScorerConfig`` reads how it ended."""
        req = _build_publish(
            score_config_id=score_config_id,
            smoke_inputs=smoke_inputs,
            idempotency_key=idempotency_key,
        )
        try:
            resp = await self._client.publish_evaluation_scorer_config(
                req, headers=headers, timeout_ms=timeout_ms
            )
        except ConnectError as err:
            return _refusal(err)
        return resp.code


class CodeScorerClientSync:
    """:class:`CodeScorerClient` over ``AgenticEvaluationServiceClientSync``."""

    def __init__(self, client: AgenticEvaluationServiceClientSync) -> None:
        self._client = client

    def create_code_scorer(
        self,
        *,
        config_key: str,
        name: str,
        metric_name: str,
        files: Mapping[str, str | bytes],
        idempotency_key: str,
        entrypoint_path: str = "score.py",
        limit_profile: LimitProfile = "standard",
        determinism: Determinism = "seeded_best_effort",
        input_fields: Sequence[str] = (),
        runtime_profile: tuple[str, int] = ("python-3.14", 1),
        success_dimension: str = "quality",
        description: str | None = None,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> EvaluationScorerConfigV1 | Refusal:
        req = _build_create(
            config_key=config_key,
            name=name,
            metric_name=metric_name,
            files=files,
            entrypoint_path=entrypoint_path,
            limit_profile=limit_profile,
            determinism=determinism,
            input_fields=input_fields,
            runtime_profile=runtime_profile,
            success_dimension=success_dimension,
            description=description,
            idempotency_key=idempotency_key,
        )
        try:
            resp = self._client.create_evaluation_scorer_config(
                req, headers=headers, timeout_ms=timeout_ms
            )
        except ConnectError as err:
            return _refusal(err)
        return resp.scorer_config

    def preview_code_scorer(
        self,
        *,
        score_config_id: str,
        scorer_input: ScorerInput,
        idempotency_key: str,
        wait_seconds: float = 120.0,
        poll_interval_seconds: float = 1.0,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> EvaluationCodeScorerResultV1 | Refusal:
        _check_wait(wait_seconds, poll_interval_seconds)
        req = _build_preview(
            score_config_id=score_config_id,
            scorer_input=scorer_input,
            idempotency_key=idempotency_key,
        )
        try:
            started = self._client.start_evaluation_scorer_preview(
                req, headers=headers, timeout_ms=timeout_ms
            )
        except ConnectError as err:
            return _refusal(err)
        deadline = time.monotonic() + wait_seconds
        read = GetEvaluationScorerPreviewRequest(preview_id=started.preview_id)
        while True:
            got = self._client.get_evaluation_scorer_preview(
                read, headers=headers, timeout_ms=timeout_ms
            )
            if got.result.state == _FINISHED:
                return got.result
            if time.monotonic() >= deadline:
                raise _timed_out(started.preview_id, wait_seconds)
            time.sleep(poll_interval_seconds)

    def publish_code_scorer(
        self,
        *,
        score_config_id: str,
        smoke_inputs: Sequence[ScorerInput],
        idempotency_key: str,
        headers: Headers | None = None,
        timeout_ms: int | None = None,
    ) -> EvaluationScorerCodeConfigV1 | Refusal:
        req = _build_publish(
            score_config_id=score_config_id,
            smoke_inputs=smoke_inputs,
            idempotency_key=idempotency_key,
        )
        try:
            resp = self._client.publish_evaluation_scorer_config(
                req, headers=headers, timeout_ms=timeout_ms
            )
        except ConnectError as err:
            return _refusal(err)
        return resp.code
