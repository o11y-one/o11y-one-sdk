"""Tests for the code scorer helpers and the ``score()`` types.

Needs ``gen-py-agentic`` regenerated at PROTO_PIN: the request and result
messages these build and read are new there. Same fakes as ``test_agentic.py``:
no transport, so nothing here can reach the network.
"""

from __future__ import annotations

import asyncio
import json
import time

import pytest
from connectrpc.code import Code
from connectrpc.errors import ConnectError
from o11y_one.agentic.v1.evaluation_pb2 import (
    AgenticEvaluationCapabilitiesV1,
    CreateEvaluationScorerConfigResponse,
    EvaluationCodeScorerJobStateV1,
    EvaluationCodeScorerResultV1,
    EvaluationDeterminismClassV1,
    EvaluationScorerCodeConfigV1,
    EvaluationScorerCodeLanguageV1,
    EvaluationScorerConfigRejectionKindV1,
    EvaluationScorerConfigRejectionV1,
    EvaluationScorerConfigV1,
    EvaluationScorerInputFieldV1,
    EvaluationScorerKindV1,
    EvaluationScorerLimitProfileV1,
    EvaluationScorerRuntimeProfileRefV1,
    EvaluationScorerRuntimeV1,
    EvaluationVerdictV1,
    GetEvaluationScorerPreviewResponse,
    PublishEvaluationScorerConfigResponse,
    StartEvaluationScorerPreviewResponse,
)
from o11y_one.sdk.code_scorer import CodeScorerClient, CodeScorerClientSync
from o11y_one.sdk.results import Refusal
from o11y_one.sdk.scorer import ScorerContext, ScorerInput, ScorerOutput
from o11y_one.sdk.validation import ValidationError
from test_agentic import FakeAsyncClient, FakeSyncClient

SOURCE = "def score(input, context):\n    return {'score': 0.75, 'verdict': 'pass'}\n"
TS_SOURCE = 'export function score() {\n  return { score: 0.75, verdict: "pass" };\n}\n'
QUEUED = EvaluationCodeScorerJobStateV1.EVALUATION_CODE_SCORER_JOB_STATE_V1_QUEUED
RUNNING = EvaluationCodeScorerJobStateV1.EVALUATION_CODE_SCORER_JOB_STATE_V1_RUNNING
FINISHED = EvaluationCodeScorerJobStateV1.EVALUATION_CODE_SCORER_JOB_STATE_V1_FINISHED


def _preview_reads(*states: int):
    """A ``get_evaluation_scorer_preview`` handler: ``states`` in turn, then the last forever."""
    answers = list(states)

    def read(request):
        state = answers.pop(0) if len(answers) > 1 else answers[0]
        result = EvaluationCodeScorerResultV1(job_id="job-1", state=state)
        if state == FINISHED:
            result.verdict = EvaluationVerdictV1.EVALUATION_VERDICT_V1_PASS
            result.score = 0.75
        return GetEvaluationScorerPreviewResponse(preview_id=request.preview_id, result=result)

    return read


def _rejected(kind: str, reason_code: str) -> ConnectError:
    rejection = EvaluationScorerConfigRejectionV1(
        kind=EvaluationScorerConfigRejectionKindV1.Value(
            f"EVALUATION_SCORER_CONFIG_REJECTION_KIND_V1_{kind}"
        ),
        reason_code=reason_code,
        detail="code scorers are not available right now",
    )
    return ConnectError(Code.FAILED_PRECONDITION, "refused", details=[rejection])


def test_create_sends_a_python_code_draft_with_its_sorted_bundle_profiles_and_fields() -> None:
    config = EvaluationScorerConfigV1(score_config_id="sc-1")
    fake = FakeSyncClient(
        create_evaluation_scorer_config=CreateEvaluationScorerConfigResponse(scorer_config=config)
    )
    created = CodeScorerClientSync(fake).create_code_scorer(
        config_key="exact",
        name="Exact match",
        metric_name="quality.exact",
        files={"score.py": SOURCE, "lib/util.py": b"X = 1\n"},
        limit_profile="small",
        determinism="nondeterministic",
        input_fields=["candidate_output", "correction"],
        idempotency_key="create-1",
    )

    assert created == config
    ((name, sent),) = fake.calls
    assert name == "create_evaluation_scorer_config"
    assert sent.kind == EvaluationScorerKindV1.EVALUATION_SCORER_KIND_V1_CODE
    assert (sent.config_key, sent.metric_name, sent.idempotency_key) == (
        "exact",
        "quality.exact",
        "create-1",
    )
    code = sent.code
    assert code.language == EvaluationScorerCodeLanguageV1.EVALUATION_SCORER_CODE_LANGUAGE_V1_PYTHON
    assert [(f.path, f.content) for f in code.files] == [
        ("lib/util.py", b"X = 1\n"),
        ("score.py", SOURCE.encode()),
    ]
    assert code.entrypoint_path == "score.py"
    assert (code.runtime_profile.id, code.runtime_profile.version) == ("python-3.14", 1)
    assert (code.limit_profile.id, code.limit_profile.version) == (
        EvaluationScorerLimitProfileV1.EVALUATION_SCORER_LIMIT_PROFILE_V1_SMALL,
        1,
    )
    assert code.determinism_class == (
        EvaluationDeterminismClassV1.EVALUATION_DETERMINISM_CLASS_V1_NONDETERMINISTIC
    )
    assert list(code.input_fields) == [
        EvaluationScorerInputFieldV1.EVALUATION_SCORER_INPUT_FIELD_V1_CANDIDATE_OUTPUT,
        EvaluationScorerInputFieldV1.EVALUATION_SCORER_INPUT_FIELD_V1_CORRECTION,
    ]


def _runtime(runtime_id: str, version: int, language: str, *, default: bool = True):
    return EvaluationScorerRuntimeV1(
        profile=EvaluationScorerRuntimeProfileRefV1(id=runtime_id, version=version),
        language=EvaluationScorerCodeLanguageV1.Value(
            f"EVALUATION_SCORER_CODE_LANGUAGE_V1_{language.upper()}"
        ),
        is_default=default,
    )


def _create_typescript(client: str, **kwargs):
    """Creates a TypeScript draft through the sync or the async client; answers (result, fake)."""
    handlers = {
        "create_evaluation_scorer_config": CreateEvaluationScorerConfigResponse(
            scorer_config=EvaluationScorerConfigV1(score_config_id="sc-ts")
        )
    }
    args = {
        "config_key": "ts-exact",
        "name": "Exact match",
        "metric_name": "quality.exact",
        "files": {"score.ts": TS_SOURCE, "lib/o11y_prng.ts": "export {};\n"},
        "idempotency_key": "create-ts",
        "language": "typescript",
        **kwargs,
    }
    if client == "sync":
        fake = FakeSyncClient(**handlers)
        return CodeScorerClientSync(fake).create_code_scorer(**args), fake
    fake = FakeAsyncClient(**handlers)
    return asyncio.run(CodeScorerClient(fake).create_code_scorer(**args)), fake


@pytest.mark.parametrize("client", ["sync", "async"])
def test_create_sends_a_typescript_draft_with_score_ts_on_its_default_runtime(client) -> None:
    created, fake = _create_typescript(client)

    assert created.score_config_id == "sc-ts"
    ((_, sent),) = fake.calls
    code = sent.code
    assert code.language == (
        EvaluationScorerCodeLanguageV1.EVALUATION_SCORER_CODE_LANGUAGE_V1_TYPESCRIPT
    )
    assert code.entrypoint_path == "score.ts"
    assert [f.path for f in code.files] == ["lib/o11y_prng.ts", "score.ts"]
    assert (code.runtime_profile.id, code.runtime_profile.version) == ("typescript-base", 1)


@pytest.mark.parametrize("client", ["sync", "async"])
def test_the_runtime_profile_is_the_served_default_for_the_language(client) -> None:
    capabilities = AgenticEvaluationCapabilitiesV1(
        scorer_runtimes=[
            _runtime("python-3.14", 1, "python"),
            _runtime("typescript-base", 1, "typescript", default=False),
            _runtime("typescript-base", 2, "typescript"),
        ]
    )
    _, fake = _create_typescript(client, capabilities=capabilities)

    ((_, sent),) = fake.calls
    profile = sent.code.runtime_profile
    assert (profile.id, profile.version) == ("typescript-base", 2)


def test_a_language_the_deployment_serves_no_runtime_for_is_refused_locally() -> None:
    capabilities = AgenticEvaluationCapabilitiesV1(
        scorer_runtimes=[_runtime("python-3.14", 1, "python")]
    )
    with pytest.raises(ValidationError, match="code_language_unsupported"):
        _create_typescript("sync", capabilities=capabilities)


def test_a_runtime_profile_the_author_names_wins_over_the_served_default() -> None:
    capabilities = AgenticEvaluationCapabilitiesV1(
        scorer_runtimes=[_runtime("typescript-base", 2, "typescript")]
    )
    _, fake = _create_typescript(
        "sync", capabilities=capabilities, runtime_profile=("typescript-base", 1)
    )

    ((_, sent),) = fake.calls
    profile = sent.code.runtime_profile
    assert (profile.id, profile.version) == ("typescript-base", 1)


TS = {"language": "typescript"}


@pytest.mark.parametrize(
    ("overrides", "field"),
    [
        ({"entrypoint_path": "main.py"}, "entrypoint_path"),
        ({"limit_profile": "huge"}, "limit_profile"),
        ({"determinism": "deterministic"}, "determinism"),
        ({"input_fields": ["prompt"]}, "input_fields"),
        ({"idempotency_key": ""}, "idempotency_key"),
        ({"language": "ruby"}, "language"),
        ({"files": {"score.py": SOURCE, "notes.txt": "x"}}, "source_path_invalid"),
        ({**TS, "files": {"main.ts": TS_SOURCE}, "entrypoint_path": "main.ts"}, "score_ts"),
        ({**TS, "files": {"score.ts": TS_SOURCE, "util.js": "x"}}, "source_path_invalid"),
        ({**TS, "files": {"score.ts": TS_SOURCE, "lib-x/util.ts": "x"}}, "source_path_invalid"),
        ({**TS, "files": {"score.ts": TS_SOURCE, "../up.ts": "x"}}, "source_path_invalid"),
        ({**TS, "files": {"score.ts": TS_SOURCE, "/abs.ts": "x"}}, "source_path_invalid"),
        ({**TS, "files": {"score.ts": TS_SOURCE, "2nd.ts": "x"}}, "source_path_invalid"),
        ({**TS, "files": {"score.ts": TS_SOURCE, "café.ts": "x"}}, "source_path_invalid"),
        ({**TS, "files": {"score.ts": TS_SOURCE, "a/" * 127 + "b.ts": "x"}}, "source_path"),
    ],
)
def test_create_refuses_locally_what_the_server_would_refuse(overrides, field) -> None:
    fake = FakeSyncClient()
    kwargs = {
        "config_key": "exact",
        "name": "Exact match",
        "metric_name": "quality.exact",
        "files": {"score.py": SOURCE},
        "idempotency_key": "create-1",
        **overrides,
    }
    with pytest.raises(ValidationError, match=field):
        CodeScorerClientSync(fake).create_code_scorer(**kwargs)
    assert fake.calls == [], "nothing reached the wire"


def test_a_typed_rejection_comes_back_as_a_refusal_naming_its_stable_code() -> None:
    fake = FakeSyncClient(
        create_evaluation_scorer_config=_rejected("CODE_SPEC_INVALID", "source_path_invalid")
    )
    refused = CodeScorerClientSync(fake).create_code_scorer(
        config_key="exact",
        name="Exact match",
        metric_name="quality.exact",
        files={"score.py": SOURCE},
        idempotency_key="create-1",
    )
    assert isinstance(refused, Refusal)
    assert refused.reason_code == "CODE_SPEC_INVALID"
    assert refused.message.startswith("source_path_invalid: ")


def test_a_transport_error_without_a_typed_rejection_is_raised() -> None:
    fake = FakeSyncClient(publish_evaluation_scorer_config=ConnectError(Code.UNAVAILABLE, "down"))
    with pytest.raises(ConnectError, match="down"):
        CodeScorerClientSync(fake).publish_code_scorer(
            score_config_id="sc-1", smoke_inputs=[{"candidate_output": "x"}], idempotency_key="p-1"
        )


def test_a_preview_sends_each_field_as_json_text_and_polls_until_it_finished() -> None:
    fake = FakeSyncClient(
        start_evaluation_scorer_preview=StartEvaluationScorerPreviewResponse(preview_id="pv-1"),
        get_evaluation_scorer_preview=_preview_reads(QUEUED, RUNNING, FINISHED),
    )
    scorer_input: ScorerInput = {"candidate_output": {"answer": 42}, "reference_output": "42"}
    result = CodeScorerClientSync(fake).preview_code_scorer(
        score_config_id="sc-1",
        scorer_input=scorer_input,
        idempotency_key="pv-key",
        poll_interval_seconds=0.001,
    )

    assert result.state == FINISHED
    assert (result.verdict, result.score) == (EvaluationVerdictV1.EVALUATION_VERDICT_V1_PASS, 0.75)
    names = [name for name, _ in fake.calls]
    assert names == ["start_evaluation_scorer_preview"] + ["get_evaluation_scorer_preview"] * 3
    started = fake.calls[0][1]
    assert (started.score_config_id, started.idempotency_key) == ("sc-1", "pv-key")
    assert json.loads(started.input.candidate_output_json) == {"answer": 42}
    assert json.loads(started.input.reference_output_json) == "42"
    assert not started.input.HasField("case_input_json"), "an absent field stays absent"
    assert {request.preview_id for _, request in fake.calls[1:]} == {"pv-1"}


def test_a_preview_that_never_finishes_raises_after_its_bounded_wait() -> None:
    fake = FakeSyncClient(
        start_evaluation_scorer_preview=StartEvaluationScorerPreviewResponse(preview_id="pv-1"),
        get_evaluation_scorer_preview=_preview_reads(QUEUED),
    )
    began = time.monotonic()
    with pytest.raises(TimeoutError, match="pv-1"):
        CodeScorerClientSync(fake).preview_code_scorer(
            score_config_id="sc-1",
            scorer_input={"candidate_output": "x"},
            idempotency_key="pv-key",
            wait_seconds=0.05,
            poll_interval_seconds=0.01,
        )
    waited = time.monotonic() - began
    reads = sum(name == "get_evaluation_scorer_preview" for name, _ in fake.calls)
    assert 0.05 <= waited < 1.0, waited
    assert 2 <= reads <= 7, reads


def test_a_preview_refused_at_start_is_a_refusal_and_is_never_polled() -> None:
    fake = FakeSyncClient(
        start_evaluation_scorer_preview=_rejected("SANDBOX_UNAVAILABLE", "sandbox_unavailable")
    )
    refused = CodeScorerClientSync(fake).preview_code_scorer(
        score_config_id="sc-1", scorer_input={"candidate_output": "x"}, idempotency_key="pv-key"
    )
    assert isinstance(refused, Refusal)
    assert refused.reason_code == "SANDBOX_UNAVAILABLE"
    assert [name for name, _ in fake.calls] == ["start_evaluation_scorer_preview"]


def test_an_input_field_the_scorer_cannot_read_is_refused_locally() -> None:
    with pytest.raises(ValidationError, match="unknown fields"):
        CodeScorerClientSync(FakeSyncClient()).preview_code_scorer(
            score_config_id="sc-1", scorer_input={"prompt": "x"}, idempotency_key="pv-key"
        )


def test_a_publication_sends_its_smoke_inputs_and_answers_the_code_block() -> None:
    publishing = EvaluationScorerCodeConfigV1(entrypoint_path="score.py")
    fake = FakeSyncClient(
        publish_evaluation_scorer_config=PublishEvaluationScorerConfigResponse(code=publishing)
    )
    smoke: list[ScorerInput] = [
        {"candidate_output": "a"},
        {"candidate_output": "b", "correction": 1},
    ]
    code = CodeScorerClientSync(fake).publish_code_scorer(
        score_config_id="sc-1", smoke_inputs=smoke, idempotency_key="pub-1"
    )

    assert code == publishing
    ((_, sent),) = fake.calls
    assert (sent.score_config_id, sent.idempotency_key) == ("sc-1", "pub-1")
    assert [json.loads(i.candidate_output_json) for i in sent.smoke_inputs] == ["a", "b"]
    assert json.loads(sent.smoke_inputs[1].correction_json) == 1
    with pytest.raises(ValidationError, match="smoke_inputs"):
        CodeScorerClientSync(fake).publish_code_scorer(
            score_config_id="sc-1", smoke_inputs=[], idempotency_key="pub-2"
        )


def test_the_async_client_polls_the_same_way() -> None:
    fake = FakeAsyncClient(
        start_evaluation_scorer_preview=StartEvaluationScorerPreviewResponse(preview_id="pv-1"),
        get_evaluation_scorer_preview=_preview_reads(RUNNING, FINISHED),
    )
    client = CodeScorerClient(fake)

    async def run() -> None:
        result = await client.preview_code_scorer(
            score_config_id="sc-1",
            scorer_input={"candidate_output": "x"},
            idempotency_key="pv-key",
            poll_interval_seconds=0.001,
        )
        assert result.state == FINISHED
        with pytest.raises(TimeoutError):
            await CodeScorerClient(
                FakeAsyncClient(
                    start_evaluation_scorer_preview=StartEvaluationScorerPreviewResponse(
                        preview_id="pv-2"
                    ),
                    get_evaluation_scorer_preview=_preview_reads(QUEUED),
                )
            ).preview_code_scorer(
                score_config_id="sc-1",
                scorer_input={},
                idempotency_key="pv-key-2",
                wait_seconds=0.02,
                poll_interval_seconds=0.005,
            )

    asyncio.run(run())


def test_the_score_types_name_exactly_what_the_harness_passes_and_accepts() -> None:
    # The sandbox's ScorerInputV1 fields and ScorerContextV1, and the harness's OUTPUT_FIELDS.
    assert ScorerInput.__optional_keys__ == {
        "case_input",
        "candidate_output",
        "reference_output",
        "correction",
        "original_context",
    }
    assert ScorerContext.__required_keys__ == {"seed", "frozen_evaluation_time_unix_nanos"}
    assert ScorerOutput.__required_keys__ == {"score", "verdict"}
    assert ScorerOutput.__optional_keys__ == {"label", "explanation", "metrics"}
