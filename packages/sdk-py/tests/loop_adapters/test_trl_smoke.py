"""GRPOTrainer runs two training steps on CPU against the fake Loop: TRL's own tiny test
model, its ``generate`` patched to call ``shell`` once and then stop, as TRL's own
``test_train_with_environment_factory`` does. The loss is zero: TRL 1.15 computes
it with a Triton kernel (``add_fused_lm_head``), which runs on a GPU only, and the
adapter's part ends at the rewards.

Needs the ``trl`` extra and the model in the Hugging Face cache, with
``HF_HUB_OFFLINE=1``: the run opens no Python socket but to the fake Loop. The
SDK's own transport connects in Rust, beneath the audit hook, so the fake Loop's
request log is what shows its traffic.
"""

from __future__ import annotations

import functools
import logging
import socket
import statistics
from unittest.mock import patch

import pytest

pytest.importorskip("trl")

import torch  # noqa: E402
from datasets import Dataset  # noqa: E402
from fake_loop import CONNECTS, CREDENTIAL  # noqa: E402
from o11y_one.sdk.loop.trl import LoopCallback, LoopEnvironment, loop_reward  # noqa: E402
from trl import GRPOConfig, GRPOTrainer  # noqa: E402

MODEL = "trl-internal-testing/tiny-Qwen3MoeForCausalLM"


class CpuGRPOTrainer(GRPOTrainer):
    def compute_loss(self, model, inputs, *args, **kwargs):
        return sum(param.sum() for param in model.parameters()) * 0


TOOL_CALL = (
    '<tool_call>\n{"name": "shell", "arguments": {"command": "pytest -q"}}\n</tool_call><|im_end|>'
)


def test_grpo_trains_on_loop_rewards_with_tools_run_in_loop(
    loop, tmp_path, caplog: pytest.LogCaptureFixture
) -> None:
    caplog.set_level(logging.DEBUG)
    rows = [
        {"prompt": [{"role": "user", "content": "Fix the module."}], "loop_case_revision_id": "c"}
    ]
    args = GRPOConfig(
        output_dir=str(tmp_path),
        per_device_train_batch_size=4,
        num_generations=4,
        max_steps=2,
        learning_rate=0.1,
        logging_steps=1,
        report_to="none",
        use_cpu=True,
    )
    trainer = CpuGRPOTrainer(
        model=MODEL,
        args=args,
        train_dataset=Dataset.from_list(rows * 8),
        environment_factory=functools.partial(LoopEnvironment, base_url=loop.url),
        reward_funcs=[loop_reward],
        callbacks=[LoopCallback()],
    )
    tokenizer = trainer.processing_class
    turns = iter([TOOL_CALL, "Done!<|im_end|>"] * 2)

    def generate(input_ids, **_):
        completion = tokenizer(next(turns), return_tensors="pt").input_ids.to(input_ids.device)
        return torch.cat([input_ids, completion.repeat(input_ids.shape[0], 1)], dim=-1)

    fake = ("127.0.0.1", int(loop.url.rsplit(":", 1)[1]))
    socket.create_connection(fake).close()
    assert [fake] == CONNECTS  # the hook sees Python's sockets
    CONNECTS.clear()
    with patch.object(trainer.model, "generate", side_effect=generate):
        trainer.train()

    assert set(CONNECTS) <= {fake}
    assert {verb for verb, _ in loop.requests} == {"reset", "step", "close"}
    assert {call.shell.script for step in loop.sent("step") for call in step.calls} == {"pytest -q"}
    resets = loop.sent("reset")
    assert len(resets) == len(loop.sent("close")) == 8
    for step in (0, 1):
        group = [reset for reset in resets if reset.trainer_step == step]
        assert len({reset.group_id for reset in group}) == 1
        assert sorted(reset.group_index for reset in group) == [0, 1, 2, 3]
    # The fake rewards rollout r-n with n / 10: r-1 to r-4 at step 0, r-5 to r-8 at step 1.
    logged = [entry["rewards/loop_reward/mean"] for entry in trainer.state.log_history[:-1]]
    assert logged == pytest.approx([statistics.mean([0.1, 0.2, 0.3, 0.4]), 0.65])
    assert trainer.state.global_step == 2
    assert loop.keys == {CREDENTIAL}
    assert CREDENTIAL not in caplog.text
