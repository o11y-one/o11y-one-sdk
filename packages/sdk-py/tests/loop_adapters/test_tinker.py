"""The Tinker adapter against a fake Loop, through tinker-cookbook's own do_group_rollout, with a
fake TokenCompleter in Tinker's place: no Tinker client is ever made, and no Tinker key is real.

Needs the ``tinker`` extra; skipped without it. The tokenizer is TRL's tiny Qwen3's.
"""

from __future__ import annotations

import asyncio
import pickle

import pytest

pytest.importorskip("tinker_cookbook")

from fake_loop import CONNECTS, CREDENTIAL, refusal  # noqa: E402
from o11y_one.agentic.v1.rollout_pb2 import LoopFailureClassV1  # noqa: E402
from o11y_one.sdk.loop import RolloutRefused, _core  # noqa: E402
from o11y_one.sdk.loop import tinker as adapter  # noqa: E402
from tinker_cookbook.completers import TokenCompleter, TokensWithLogprobs  # noqa: E402
from tinker_cookbook.rl.rollouts import do_group_rollout  # noqa: E402
from transformers import AutoTokenizer  # noqa: E402

MODEL = "trl-internal-testing/tiny-Qwen3MoeForCausalLM"
SHELL = '<tool_call>\n{"name": "shell", "arguments": {"command": "pytest -q"}}\n</tool_call>'
TINKER_CANARY = "tinker-canary-not-a-key"
N = 4


class Policy(TokenCompleter):
    """Tinker's sampler, faked: each rollout acts ``action``, then stops at a tool turn.
    Its own tokenizer: the renderer's encodes in worker threads."""

    def __init__(self, action: str = SHELL) -> None:
        self.tokenizer, self.action = AutoTokenizer.from_pretrained(MODEL), action

    async def __call__(self, model_input, stop, *, max_tokens=None) -> TokensWithLogprobs:
        seen = self.tokenizer.decode(model_input.to_ints())
        text = "Done." if "<tool_response>" in seen else self.action
        tokens = self.tokenizer.encode(text + "<|im_end|>", add_special_tokens=False)
        return TokensWithLogprobs(tokens=tokens, maybe_logprobs=[0.0] * len(tokens))


def builder(loop, step: int = 3) -> adapter.LoopEnvGroupBuilder:
    return adapter.LoopEnvGroupBuilder(
        messages=[{"role": "user", "content": "Fix the module."}],
        group_size=N,
        trainer_step=step,
        model_name=MODEL,
        renderer_name="qwen3_instruct",
        case_revision_id="case-a",
        base_url=loop.url,
    )


def rollout(group, policy=None):
    return asyncio.run(do_group_rollout(group, policy or Policy()))


def test_a_group_is_n_rollouts_of_one_case_and_the_verifier_is_each_ones_whole_reward(
    loop, monkeypatch
) -> None:
    monkeypatch.setenv("TINKER_API_KEY", TINKER_CANARY)
    CONNECTS.clear()
    trajectories = rollout(builder(loop))
    assert set(CONNECTS) <= {("127.0.0.1", int(loop.url.rsplit(":", 1)[1]))}  # no Python egress
    resets = loop.sent("reset")
    assert len({reset.group_id for reset in resets}) == 1
    assert sorted(reset.group_index for reset in resets) == list(range(N))
    assert {(r.group_size, r.trainer_step, r.case_revision_id) for r in resets} == {
        (N, 3, "case-a")
    }
    assert {r.client.adapter for r in resets} == {"o11y_one.sdk.loop.tinker"}
    assert sorted(trajectories.get_total_rewards()) == [0.1, 0.2, 0.3, 0.4]
    assert {call.WhichOneof("call") for step in loop.sent("step") for call in step.calls} == {
        "shell"
    }
    assert loop.keys == {CREDENTIAL}
    assert not [
        request
        for _, request in loop.requests
        if TINKER_CANARY.encode() in request.SerializeToString()
    ]


def test_making_the_envs_starts_no_rollout(loop) -> None:
    group = builder(loop)
    assert len(asyncio.run(group.make_envs())) == N
    assert loop.sent("reset") == []
    asyncio.run(group.cleanup())
    assert loop.sent("close") == []


def test_a_malformed_tool_call_scores_the_verifier_not_a_parse_penalty(loop) -> None:
    broken = '<tool_call>\n{"name": "shell", "arguments": \n</tool_call>'
    trajectories = rollout(builder(loop), Policy(action=broken))
    assert sorted(trajectories.get_total_rewards()) == [0.1, 0.2, 0.3, 0.4]


def test_a_task_failure_keeps_its_value_and_ours_fails_the_group(loop) -> None:
    loop.closes["r-1"] = (LoopFailureClassV1.LOOP_FAILURE_CLASS_V1_TASK, [("tests_passed", -1.0)])
    assert -1.0 in rollout(builder(loop)).get_total_rewards()
    loop.closes["r-5"] = (LoopFailureClassV1.LOOP_FAILURE_CLASS_V1_INFRASTRUCTURE, [])
    with pytest.raises(_core.LoopInfrastructureFailure, match="r-5"):
        rollout(builder(loop))
    assert len(loop.sent("close")) == 8  # the group's other rollouts still closed


def test_cleanup_closes_what_is_open_once_and_never_raises(loop) -> None:
    group = builder(loop)

    async def opened():
        envs = await group.make_envs()
        await asyncio.gather(*(group._rollouts[id(env)].open() for env in envs[:2]))

    asyncio.run(opened())
    loop.refusals["close"] = [refusal("rate_limited")]
    asyncio.run(group.cleanup())
    asyncio.run(group.cleanup())
    assert len(loop.sent("close")) == 2


def test_a_refused_reset_fails_the_rollout_with_its_code(loop) -> None:
    loop.refusals["reset"] = [refusal("run_concurrency_reached")]
    with pytest.raises(RolloutRefused) as refused:
        rollout(builder(loop))
    assert refused.value.code == "run_concurrency_reached"


def test_a_builder_pickles_without_any_credential(loop, monkeypatch) -> None:
    monkeypatch.setenv("TINKER_API_KEY", TINKER_CANARY)
    pickled = pickle.dumps(builder(loop))
    assert CREDENTIAL.encode() not in pickled and TINKER_CANARY.encode() not in pickled
    assert pickle.loads(pickled).case_revision_id == "case-a"


def test_the_tools_are_the_core_three() -> None:
    specs = [tool.to_spec() for tool in adapter._tools(None)]
    assert [{"type": "function", "function": spec} for spec in specs] == _core.TOOLS


def test_the_dataset_gives_each_step_its_groups(loop) -> None:
    rows = [
        {
            "messages": [{"role": "user", "content": f"case {i}"}],
            "loop": {"case_revision_id": f"c{i}"},
        }
        for i in range(4)
    ]
    dataset = adapter.LoopRLDataset(
        rows, batch_size=2, group_size=N, model_name=MODEL, renderer_name="qwen3_instruct"
    )
    assert len(dataset) == 2
    second = dataset.get_batch(1)
    assert [(b.case_revision_id, b.trainer_step, b.trainer_total_steps) for b in second] == [
        ("c2", 1, 2),
        ("c3", 1, 2),
    ]
