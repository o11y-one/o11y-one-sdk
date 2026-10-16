"""The verl adapter against a fake Loop: verl's own agent-loop config loads LoopAgentLoop, its
tool turns become Loop steps, and each trajectory's close is its reward.

Needs the ``verl`` extra; skipped without it. The model is a fake server manager answering
TokenOutput, as verl's own CPU agent-loop tests do; the tokenizer is TRL's tiny Qwen3's.
"""

from __future__ import annotations

import asyncio
import json
import uuid

import pytest

pytest.importorskip("verl")

import hydra  # noqa: E402
import loop_exports  # noqa: E402
from fake_loop import CONNECTS, CREDENTIAL, tiny_qwen3  # noqa: E402
from o11y_one.agentic.v1.rollout_pb2 import LoopFailureClassV1  # noqa: E402
from o11y_one.sdk.loop import RolloutRefused, _core  # noqa: E402
from o11y_one.sdk.loop import verl as adapter  # noqa: E402
from omegaconf import OmegaConf  # noqa: E402
from transformers import AutoTokenizer  # noqa: E402
from verl.experimental.agent_loop.agent_loop import DictConfigWrap, ToolListWrap  # noqa: E402
from verl.utils.dataset.rl_dataset import RLHFDataset  # noqa: E402
from verl.workers.rollout.replica import TokenOutput  # noqa: E402

INFRASTRUCTURE = LoopFailureClassV1.LOOP_FAILURE_CLASS_V1_INFRASTRUCTURE
TOKENIZER = tiny_qwen3()
TOOL_CALL = '<tool_call>\n{"name": "shell", "arguments": {"command": "pytest -q"}}\n</tool_call>'
N = 4


class Model:
    """verl's server manager: each trajectory calls shell once, then stops."""

    def __init__(self, tokenizer, fail: bool = False) -> None:
        self.tokenizer, self.fail, self.turns = tokenizer, fail, {}

    async def generate(self, request_id: str, *, prompt_ids: list[int], **_) -> TokenOutput:
        if self.fail:
            raise RuntimeError("the inference server went away")
        turn = self.turns[request_id] = self.turns.get(request_id, 0) + 1
        text = TOOL_CALL if turn == 1 else "Done."
        return TokenOutput(token_ids=self.tokenizer.encode(text + "<|im_end|>"))


@pytest.fixture(scope="module")
def tokenizer():
    return AutoTokenizer.from_pretrained(TOKENIZER)


def config():
    rollout = {
        "n": N,
        "prompt_length": 1024,
        "response_length": 1024,
        "full_determinism": False,
        "multi_turn": {
            "max_user_turns": 4,
            "max_assistant_turns": 4,
            "max_parallel_calls": 1,
            "max_tool_response_length": 4096,
            "tool_response_truncate_side": "middle",
            "format": "hermes",
        },
    }
    return OmegaConf.create(
        {
            "actor_rollout_ref": {"rollout": rollout},
            "trainer": {"experiment_name": "pyfix-verl"},
            "data": {},
        }
    )


def agent_loop(loop, tokenizer, model):
    """A LoopAgentLoop as verl's AgentLoopWorker makes one from agent_loop_config_path."""
    (entry,) = [e for e in OmegaConf.load(adapter.CONFIG) if e.name == "loop"]
    trainer = config()
    return hydra.utils.instantiate(
        config=entry,
        trainer_config=DictConfigWrap(config=trainer),
        server_manager=model,
        tokenizer=tokenizer,
        processor=None,
        dataset_cls=RLHFDataset,
        data_config=DictConfigWrap(trainer.data),
        tools=ToolListWrap([]),
        base_url=loop.url,
    )


def row(uid: str, case: str = "case-a") -> dict:
    return {
        "raw_prompt": [{"role": "user", "content": "Fix the module."}],
        "uid": uid,
        "extra_info": {"loop": {"case_revision_id": case}},
    }


async def trajectories(loop, tokenizer, rows, model=None):
    model = model or Model(tokenizer)
    return await asyncio.gather(
        *(agent_loop(loop, tokenizer, model).run({}, **kwargs) for kwargs in rows)
    )


def test_a_group_is_verls_uid_with_its_n_indices_and_the_rows_case(loop, tokenizer) -> None:
    uids = [str(uuid.uuid4()) for _ in range(2)]
    rows = [
        row(uid, case)
        for uid, case in zip(uids, ["case-a", "case-b"], strict=True)
        for _ in range(N)
    ]
    CONNECTS.clear()
    asyncio.run(trajectories(loop, tokenizer, rows))
    assert set(CONNECTS) <= {("127.0.0.1", int(loop.url.rsplit(":", 1)[1]))}  # no Python egress
    resets = loop.sent("reset")
    for uid, case in zip(uids, ["case-a", "case-b"], strict=True):
        group = [reset for reset in resets if reset.group_id == uid]
        assert sorted(reset.group_index for reset in group) == list(range(N))
        assert {(reset.group_size, reset.case_revision_id) for reset in group} == {(N, case)}
    assert {reset.experiment_name for reset in resets} == {"pyfix-verl"}
    assert [json.loads(reset.tools_json) for reset in resets] == [_core.TOOLS] * len(rows)
    clients = {(reset.client.adapter, reset.client.framework_version) for reset in resets}
    assert clients == {("o11y_one.sdk.loop.verl", adapter.verl.__version__)}


def test_a_uid_seen_again_wraps_inside_its_group(loop, tokenizer) -> None:
    uid = str(uuid.uuid4())
    asyncio.run(trajectories(loop, tokenizer, [row(uid) for _ in range(N + 1)]))
    indices = sorted(reset.group_index for reset in loop.sent("reset"))
    assert indices == [0, 0, *range(1, N)]


def test_each_tool_turn_is_a_step_with_the_assistant_message(loop, tokenizer) -> None:
    (output,) = asyncio.run(trajectories(loop, tokenizer, [row(str(uuid.uuid4()))]))
    (step,) = loop.sent("step")
    (call,) = step.calls
    assert call.shell.script == "pytest -q"
    message = json.loads(step.model_message_json)
    assert message["role"] == "assistant"
    assert message["tool_calls"][0]["function"]["name"] == "shell"
    assert output.num_turns == 4  # user, assistant, tool, assistant


def test_the_reward_is_the_close_and_a_task_failure_keeps_its_value(loop, tokenizer) -> None:
    loop.closes["r-2"] = (LoopFailureClassV1.LOOP_FAILURE_CLASS_V1_TASK, [("tests_passed", -1.0)])
    uid = str(uuid.uuid4())
    first = asyncio.run(trajectories(loop, tokenizer, [row(uid)]))
    second = asyncio.run(trajectories(loop, tokenizer, [row(uid)]))
    assert [first[0].reward_score, second[0].reward_score] == [0.1, -1.0]


def test_a_trajectory_that_fails_still_closes_its_rollout(loop, tokenizer) -> None:
    with pytest.raises(RuntimeError, match="went away"):
        asyncio.run(trajectories(loop, tokenizer, [row(str(uuid.uuid4()))], Model(tokenizer, True)))
    assert [close.rollout_id for close in loop.sent("close")] == ["r-1"]


def test_our_failure_reruns_the_trajectory_once_then_raises(loop, tokenizer) -> None:
    loop.closes["r-1"] = (INFRASTRUCTURE, [])
    (output,) = asyncio.run(trajectories(loop, tokenizer, [row(str(uuid.uuid4()))]))
    assert output.reward_score == 0.2
    assert len(loop.sent("reset")) == 2
    resets = loop.sent("reset")
    assert resets[0].group_index == resets[1].group_index
    loop.closes["r-3"] = loop.closes["r-4"] = (INFRASTRUCTURE, [])
    with pytest.raises(adapter.LoopInfrastructureFailure, match="r-4"):
        asyncio.run(trajectories(loop, tokenizer, [row(str(uuid.uuid4()))]))
    assert len(loop.sent("reset")) == 4


def test_a_refused_reset_fails_the_trajectory_with_its_code(loop, tokenizer) -> None:
    from fake_loop import refusal

    loop.refusals["reset"] = [refusal("run_concurrency_reached")]
    with pytest.raises(RolloutRefused) as refused:
        asyncio.run(trajectories(loop, tokenizer, [row(str(uuid.uuid4()))]))
    assert refused.value.code == "run_concurrency_reached"


def test_the_tools_are_the_core_three(loop, tokenizer) -> None:
    from o11y_one.sdk.loop import _core

    tools = agent_loop(loop, tokenizer, Model(tokenizer)).tool_schemas
    assert tools == _core.TOOLS


def test_the_key_reaches_loop(loop, tokenizer) -> None:
    asyncio.run(trajectories(loop, tokenizer, [row(str(uuid.uuid4()))]))
    assert loop.keys == {CREDENTIAL}


def test_the_module_prints_only_the_config_path_for_the_shell_to_take() -> None:
    import subprocess
    import sys

    run = subprocess.run(
        [sys.executable, "-m", "o11y_one.sdk.loop.verl"], capture_output=True, text=True, check=True
    )
    assert run.stdout == f"{adapter.CONFIG}\n"
    assert adapter.CONFIG.is_file()


def test_a_worker_keeps_counters_for_its_recent_uids_only() -> None:
    adapter._counter.cache_clear()
    for number in range(adapter.UIDS_KEPT + 10):
        next(adapter._counter(f"uid-{number}"))
    assert adapter._counter.cache_info().currsize == adapter.UIDS_KEPT


def test_the_sft_dataset_parses_the_trajectory_exports_tools_and_arguments(
    tmp_path, tokenizer
) -> None:
    from o11y_one.sdk.loop import _core

    path = loop_exports.trajectory_set("verl", tmp_path / "verl.parquet")
    # Qwen3's template answers a message's parallel calls in one tool block, which verl's
    # per-turn check reports; its own setting accepts that.
    config = {"ignore_input_ids_mismatch": True}
    dataset = adapter.LoopSFTDataset(str(path), tokenizer, config)
    assert dataset.tools == [_core.TOOLS, _core.TOOLS]
    # verl's __getitem__ builds each row's messages from its frame, not from dataset.messages.
    built = dataset._build_messages(dataset.dataframe.iloc[1].to_dict())
    assert built == dataset.messages[1]
    arguments = [call["function"]["arguments"] for call in built[1]["tool_calls"]]
    assert arguments[0] == {"path": "/work/mod.py"}
    assert built[0] == loop_exports.PROMPTS[1][0]  # a field the message lacks is absent
    assert dataset[1]["loss_mask"].sum() > 0


def test_verls_rl_loader_takes_a_task_set_whose_batch_resets_on_its_case(
    loop, tmp_path, tokenizer
) -> None:
    from torch.utils.data import DataLoader
    from verl.utils.dataset.rl_dataset import collate_fn

    path = loop_exports.task_set("verl", tmp_path / "tasks.parquet")
    config = OmegaConf.create({"filter_overlong_prompts_workers": 1, "cache_dir": str(tmp_path)})
    batch = next(
        iter(DataLoader(RLHFDataset(str(path), tokenizer, config), 2, collate_fn=collate_fn))
    )
    assert list(batch["agent_name"]) == ["loop", "loop"]
    first = {
        "raw_prompt": batch["raw_prompt"][0],
        "uid": "u-1",
        "extra_info": batch["extra_info"][0],
    }
    asyncio.run(trajectories(loop, tokenizer, [first]))
    assert [reset.case_revision_id for reset in loop.sent("reset")] == loop_exports.CASES[:1]


def test_verls_sft_loader_takes_a_trajectory_set_through_loop_sft_dataset(
    tmp_path, tokenizer
) -> None:
    from torch.utils.data import DataLoader

    path = loop_exports.trajectory_set("verl", tmp_path / "trajectories.parquet")
    # Qwen3's template answers a message's parallel calls in one tool block, which verl's
    # per-turn check reports; its own setting accepts that.
    config = {"pad_mode": "right", "max_length": 1024, "ignore_input_ids_mismatch": True}
    dataset = adapter.LoopSFTDataset(str(path), tokenizer, config)
    batch = next(iter(DataLoader(dataset, batch_size=2)))
    assert batch["input_ids"].shape == (2, 1024)
    assert (batch["loss_mask"].sum(dim=1) > 0).all()  # each row trains on its assistant turns
    text = tokenizer.decode(batch["input_ids"][1][batch["attention_mask"][1].bool()])
    assert '{"name": "write_file", "arguments": {"path": "/work/mod.py"' in text
    assert '"name": "write_file", "description"' in text  # the tools the rollout reset with
