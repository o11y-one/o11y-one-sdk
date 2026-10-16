# Tinker on Loop

`o11y_one.sdk.loop.tinker` plugs Loop into tinker-cookbook's own RL loop.
`LoopRLDataset` yields `LoopEnvGroupBuilder` groups. Each env is the cookbook's own tool env,
whose tools run in a Loop rollout, and each trajectory's reward is that rollout's verifier
reward. Sampling and training stay Tinker's.

## Install

```sh
pip install 'o11y-one[tinker]'   # tinker-cookbook 0.5.x (0.5.7 tested), tinker 0.33; Python 3.11+
```

## Auth: two keys, kept apart

- **Loop.** A person creates the run in the web (**Connect a trainer**). That gives you
  `O11Y_RUN` (not a secret) and `O11Y_API_KEY` (a machine key with the `rollout:drive` scope).
  The builder reads the key from the environment only when it makes the envs. Groups pickle
  without it.
- **Tinker.** `TINKER_API_KEY` is read by the `tinker` SDK in your process, and by nothing
  else. This adapter never imports `tinker` or reads its key, and no Loop request carries it.
- Put both keys in your secret manager or an env file, never on a command line.
- `O11Y_BASE_URL` names another Loop endpoint, such as your region's.

## Wire-up

```python
import json

import chz
from tinker_cookbook.rl import train
from tinker_cookbook.rl.types import RLDatasetBuilder

from o11y_one.sdk.loop.tinker import LoopRLDataset


@chz.chz
class PyfixDataset(RLDatasetBuilder):
    path: str

    async def __call__(self):
        rows = [json.loads(line) for line in open(self.path)]  # Loop's Tinker dataset export
        return LoopRLDataset(
            rows,
            batch_size=8,
            group_size=8,
            model_name="Qwen/Qwen3-4B-Instruct-2507",
            renderer_name="qwen3_instruct",
        ), None


config = train.Config(
    model_name="Qwen/Qwen3-4B-Instruct-2507",
    recipe_name="loop_pyfix",
    dataset_builder=PyfixDataset(path="pyfix.tinker.jsonl"),
    learning_rate=4e-5,
    max_tokens=2048,
    log_path="~/runs/pyfix-tinker",
    rollout_error_tolerance=True,  # a group Loop failed is skipped, never trained on
)
```

Then run it with `asyncio.run(train.main(config))`.

## Dataset

- Rows are `{"messages": [...], "loop": {"case_revision_id": ...}}`.
- Each row is one group of `group_size` envs: one Loop group, with indices 0 to n−1.
- Step `i` is batch `i`, and its resets carry `trainer_step=i`.
- **An env starts its rollout at its first use.** That is its first tool call, or its grading
  when it never called one. So the spare envs a retry's `make_envs` makes are never started,
  and never billed.

## Concurrency

- **Rollouts open at once** = `groups_per_batch × group_size`, in sync or async training.
  - Set the run's environment limit to at least that.
  - Keep it within your plan's limit, minus what other runs keep open.
- **`run_concurrency_reached` and `plan_concurrency_reached`:** Loop waits up to 60 seconds
  for room, then refuses. The refusal fails the rollout. With `rollout_error_tolerance=True`,
  the cookbook retries it up to three times (each after Loop's own wait), then drops the
  group.
- **`run_paused`:** each reset waits up to 30 minutes for the run to resume.
- **Tool calls** in one turn run in parallel in the cookbook, and reach Loop one at a time.
  Each one's step carries the assistant message it came from, as the renderer's
  `to_openai_message` writes it.

## Rewards

- Rewards come in the environment's declared order, primary first (rollout.proto).
- The verifier's primary reward is each trajectory's whole reward. `compute_group_rewards`
  closes the group's rollouts at once and adds it, however each episode ended.
- The env's own grader scores 0, and so does a malformed tool call
  (`failed_parse_reward=0.0`), so nothing else is mixed in.
- A rollout that failed on its task or its verifier keeps its value: train on it.
- Our failure (`INFRASTRUCTURE`, never billed) raises `LoopInfrastructureFailure`. The group is
  then never scored: `rollout_error_tolerance=True` skips it, and the default strategy stops
  the run.

## Cost

- **Loop** bills sandbox time in unit-seconds (1 vCPU and 2 GiB for one second) at your plan's
  rate.
  - The run's boards show `billed_unit_seconds` and `spend_cents`.
  - Divide by training steps for sandbox-hours per step.
  - Our failures are never billed. The run's spend cap refuses resets once it's reached.
- **Tinker** bills its own sampling and training tokens, under your Tinker account. Loop never
  sees that bill.

## Reference run

The reference run trains `Qwen/Qwen3-4B-Instruct-2507` with LoRA (renderer `qwen3_instruct`)
on Tinker, with your own Tinker key and a spend cap you set, on `loop-ref-pyfix`
(`examples/loop/pyfix/`): `groups_per_batch=8` and `group_size=8`, so 64 rollouts a step, for
30 steps. Give its run an environment limit of 64.

It is measured by the per-step mean reward on the run's Train live board; failures by
class and by code; rollouts per minute; and sandbox-hours per step
(`billed_unit_seconds ÷ 3600 ÷ steps`), beside Tinker's own tokens and spend.
