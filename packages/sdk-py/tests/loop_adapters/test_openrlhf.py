"""The OpenRLHF adapter against a fake Loop, loaded by path as OpenRLHF's vLLM engine loads
``--train.agent_func_path``, with a fake engine answering as vLLM does.

Needs OpenRLHF's agent module (``pip install --no-deps openrlhf==0.11.2`` with aiohttp, sympy,
pylatexenc and transformers 5.15); skipped without it. The tokenizer is TRL's tiny Qwen3's.
"""

from __future__ import annotations

import asyncio
import importlib.util
import json
import sys
from types import SimpleNamespace

import pytest

pytest.importorskip("openrlhf")

import o11y_one.sdk.loop.openrlhf as adapter  # noqa: E402
from fake_loop import CONNECTS, CREDENTIAL, refusal  # noqa: E402
from o11y_one.agentic.v1.rollout_pb2 import LoopFailureClassV1  # noqa: E402
from o11y_one.sdk.loop import RolloutRefused, _core  # noqa: E402
from openrlhf.utils.agent import AgentExecutorBase  # noqa: E402
from transformers import AutoTokenizer  # noqa: E402

TOKENIZER = "trl-internal-testing/tiny-Qwen3MoeForCausalLM"
SHELL = '<tool_call>\n{"name": "shell", "arguments": {"command": "pytest -q"}}\n</tool_call>'
READ = '<tool_call>\n{"name": "read_file", "arguments": {"path": "/work/mod.py"}}\n</tool_call>'
LABEL = json.dumps({"case_revision_id": "case-a", "environment_version_id": "v-1"})


@pytest.fixture(scope="module")
def tokenizer():
    return AutoTokenizer.from_pretrained(TOKENIZER)


def load_executor() -> AgentExecutorBase:
    """openrlhf/trainer/ray/vllm_engine.py's _load_agent_executor, line for line."""
    spec = importlib.util.spec_from_file_location("agent_module", adapter.__file__)
    agent_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(agent_module)
    assert issubclass(agent_module.AgentExecutor, AgentExecutorBase)
    return agent_module.AgentExecutor()


class Engine:
    """vLLM's answer shape: each trajectory acts ``action``, then stops once it sees a tool turn."""

    def __init__(self, tokenizer, action: str = SHELL, fail: bool = False) -> None:
        self.tokenizer, self.action, self.fail, self.prompts = tokenizer, action, fail, []

    async def generate(self, prompt_token_ids, sampling_params, multi_modal_data=None):
        if self.fail:
            raise RuntimeError("the vLLM engine went away")
        seen = self.tokenizer.decode(prompt_token_ids)
        self.prompts.append(seen)
        text = "Done." if "<tool_response>" in seen else self.action
        ids = self.tokenizer.encode(text + "<|im_end|>")
        return SimpleNamespace(
            outputs=[SimpleNamespace(token_ids=ids, text=text, finish_reason="stop")]
        )


def execute(loop, tokenizer, engine=None, label=LABEL, samples: int = 1):
    """OpenRLHF's generate_responses: one executor per engine, its samples gathered."""
    executor, engine = load_executor(), engine or Engine(tokenizer)
    prompt = tokenizer.apply_chat_template(
        [{"role": "user", "content": "Fix the module."}], tokenize=False, add_generation_prompt=True
    )

    async def run():
        return await asyncio.gather(
            *(
                executor.execute(
                    prompt=prompt,
                    label=label,
                    sampling_params=SimpleNamespace(max_tokens=None, logprobs=None),
                    max_length=4096,
                    hf_tokenizer=tokenizer,
                    llm_engine=engine,
                )
                for _ in range(samples)
            )
        )

    return asyncio.run(run())


def test_each_sample_is_a_rollout_of_the_labels_case_rewarded_at_its_close(loop, tokenizer) -> None:
    CONNECTS.clear()
    responses = execute(loop, tokenizer, samples=4)
    assert set(CONNECTS) <= {("127.0.0.1", int(loop.url.rsplit(":", 1)[1]))}  # no Python egress
    assert {reset.case_revision_id for reset in loop.sent("reset")} == {"case-a"}
    assert {reset.client.adapter for reset in loop.sent("reset")} == {"o11y_one.sdk.loop.openrlhf"}
    closed = sorted(close.rollout_id for close in loop.sent("close"))
    assert closed == ["r-1", "r-2", "r-3", "r-4"]
    assert sorted(response["reward"] for response in responses) == [0.1, 0.2, 0.3, 0.4]
    assert all(response["scores"] == response["reward"] for response in responses)
    assert loop.keys == {CREDENTIAL}


def test_a_turns_tool_calls_are_one_step_and_its_feedback_is_the_templates_tool_turn(
    loop, tokenizer
) -> None:
    engine = Engine(tokenizer, action=f"Checking.\n{SHELL}\n{READ}")
    (response,) = execute(loop, tokenizer, engine)
    (step,) = loop.sent("step")
    assert len(engine.prompts) == 2  # the turn without a tool call ends the sample
    assert [call.WhichOneof("call") for call in step.calls] == ["shell", "read_file"]
    assert json.loads(step.model_message_json) == {"role": "assistant", "content": engine.action}
    turn = (
        f"{READ}<|im_end|>\n<|im_start|>user\n<tool_response>\nexit code 0\nstdout:\nran shell\n"
        "</tool_response>\n<tool_response>\nexit code 0\nstdout:\nran read_file\n</tool_response>"
        "<|im_end|>\n<|im_start|>assistant\n"
    )
    assert turn in tokenizer.decode(response["observation_tokens"])


def test_a_tool_call_that_does_not_parse_is_answered_without_a_step(loop, tokenizer) -> None:
    engine = Engine(tokenizer, action='<tool_call>\n{"name": "shell", "arguments": \n</tool_call>')
    execute(loop, tokenizer, engine)
    assert loop.sent("step") == []
    assert "error: tool_call_invalid" in engine.prompts[-1]


def test_a_sample_whose_engine_fails_still_closes_its_rollout(loop, tokenizer) -> None:
    with pytest.raises(RuntimeError, match="went away"):
        execute(loop, tokenizer, Engine(tokenizer, fail=True))
    assert [close.rollout_id for close in loop.sent("close")] == ["r-1"]


def test_a_task_failure_keeps_its_value_and_ours_reruns_once_then_raises(loop, tokenizer) -> None:
    loop.closes["r-1"] = (LoopFailureClassV1.LOOP_FAILURE_CLASS_V1_TASK, [("tests_passed", -1.0)])
    assert execute(loop, tokenizer)[0]["reward"] == -1.0
    loop.closes["r-2"] = (LoopFailureClassV1.LOOP_FAILURE_CLASS_V1_INFRASTRUCTURE, [])
    assert execute(loop, tokenizer)[0]["reward"] == 0.3
    loop.closes["r-4"] = loop.closes["r-5"] = loop.closes["r-2"]
    with pytest.raises(_core.LoopInfrastructureFailure, match="r-5"):
        execute(loop, tokenizer)
    assert len(loop.sent("reset")) == 5


def test_a_refused_reset_fails_the_sample_with_its_code(loop, tokenizer) -> None:
    loop.refusals["reset"] = [refusal("plan_concurrency_reached")]
    with pytest.raises(RolloutRefused) as refused:
        execute(loop, tokenizer)
    assert refused.value.code == "plan_concurrency_reached"


def test_render_prompts_puts_the_core_tools_in_each_prompt(tmp_path, tokenizer) -> None:
    rows = tmp_path / "in.jsonl"
    rows.write_text(
        json.dumps({"prompt": [{"role": "user", "content": "Fix it."}], "label": LABEL})
    )
    adapter.render_prompts(rows, tmp_path / "out.jsonl", tokenizer)
    (row,) = [json.loads(line) for line in (tmp_path / "out.jsonl").read_text().splitlines()]
    assert row["label"] == LABEL
    assert row["prompt"].endswith("<|im_start|>assistant\n")
    assert all(json.dumps(tool["function"]["name"]) in row["prompt"] for tool in _core.TOOLS)


def test_an_openrlhf_outside_the_tested_range_is_refused_at_import(monkeypatch) -> None:
    import importlib.metadata

    monkeypatch.setattr(importlib.metadata, "version", lambda name: "0.10.4")
    monkeypatch.delitem(sys.modules, "o11y_one.sdk.loop.openrlhf")
    with pytest.raises(ImportError, match=r"0\.11\.2.*0\.12.*0\.10\.4"):
        importlib.import_module("o11y_one.sdk.loop.openrlhf")
