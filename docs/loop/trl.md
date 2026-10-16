# TRL on Loop

`o11y_one.sdk.loop.trl` runs TRL's `GRPOTrainer` on a Loop run. Every rollout's tool calls
run in a Loop environment, and every reward comes from that environment's verifier.

## Install

```sh
pip install 'o11y-one[trl]'   # TRL 1.15.x, transformers 5.2 or later; Python 3.11+
```

Training needs a GPU. TRL 1.15 computes the GRPO loss with a Triton kernel, and that kernel
has no CPU path.

## Auth

- A person creates the run in the web (**Connect a trainer**). That gives you two values:
  - `O11Y_RUN`, the run's id (`trn_…`). It is not a secret.
  - `O11Y_API_KEY`, a machine key with the `rollout:drive` scope.
- Put the key in your secret manager or an env file on every training node.
- Never put the key on a command line or in a notebook.
- Revoking the key stops the run's resets at their next call.

## Wire-up

```python
from trl import GRPOConfig, GRPOTrainer
from o11y_one.sdk.loop.trl import LoopCallback, LoopEnvironment, loop_reward

trainer = GRPOTrainer(
    model="Qwen/Qwen3-1.7B",
    args=GRPOConfig(num_generations=8, max_steps=30),
    train_dataset=dataset,
    environment_factory=LoopEnvironment,
    reward_funcs=[loop_reward],
    callbacks=[LoopCallback()],
)
trainer.train()
```

- Each rollout is a `LoopEnvironment`. Its tools are `shell`, `read_file` and `write_file`.
  Each reset names those tools, and a trajectory export of the run carries them.
- `loop_reward` closes the batch's rollouts all at once, and scores each with the verifier's
  primary reward.
- `LoopCallback` tells the environments the group size and the training step.
- To use another endpoint, pass `environment_factory=functools.partial(LoopEnvironment,
  base_url=...)`.

## Dataset

- `prompt` holds the task, as GRPO expects.
- `loop_case_revision_id` names the case. Loop's TRL dataset export writes it. The adapter sends it
  on reset, and groups by it.
- A row without that column is grouped by its prompt.
- A group is one step's rollouts of one case. Its id is derived from the run, the step and
  the case, so every process names it the same way.

## Concurrency

- **Rollouts open at once** = `generation_batch_size` (`per_device_train_batch_size ×
  num_processes × steps_per_generation`).
  - Set the run's environment limit to at least that.
  - Keep it within your plan's limit, minus what other runs keep open.
- **TRL resets the batch serially.** `LoopEnvironment.reset` only starts the reset and
  answers at once. The first tool call waits for it.
- **TRL 1.15 runs a batch's tool calls one after another.** Each tool-calling round costs
  the sum of the batch's step times, and the GPU idles meanwhile.
- **`run_concurrency_reached` and `plan_concurrency_reached`:** Loop waits up to 60 seconds
  for room, then refuses. The refusal reaches the model as a tool error, and `loop_reward`
  then raises `RolloutRefused` with the code, which stops training. Raise the limit, or
  shrink the batch.
- **`run_paused`:** each reset waits up to 30 minutes for the run to resume, so training
  stalls rather than fails.

## Rewards

- The verifier's reward is the reward. Rewards come in the environment's declared order,
  primary first (rollout.proto), and `loop_reward` answers the primary.
- A rollout that failed on its task or its verifier keeps its value: train on it.
- Our failures (`INFRASTRUCTURE`) and a person's Stop score `None`, which TRL leaves out of
  the advantages.
- Don't add a reward function that reads the environment's own report. The verifier is the
  only score.
- TRL never hands a tool the assistant message, so Loop's trajectories carry no
  `model_message` for TRL runs.

## Region

- Run the trainer in the region of the run's Loop environments.
- Watch `step_overhead_p50` on the run's Train live board. One round trip per step is the
  budget against the 5% overhead target.

## Troubleshooting

Every refusal raises `RolloutRefused` with a stable `code`. The codes are listed in the
sdk-py README's Loop section.

## Reference run

The reference GRPO run trains Qwen3-1.7B with LoRA (r=16) on one 80 GB H100, on
`loop-ref-pyfix` (`examples/loop/pyfix/`): `num_generations=8`,
`per_device_train_batch_size=8` and `gradient_accumulation_steps=8`, so 64 rollouts a step, for
30 steps. Give its run a group size of 8 and an environment limit of 64.

It is measured by the per-step mean reward on the run's Train live board; failures by
class and by code; Loop's overhead (reset, step overhead and the client's round trip) as a
share of rollout wall time, which should stay at or below 5%; rollouts per minute; and GPU
utilisation while each step's rollouts run.
TRL's serial tool calls show up as GPU idle time between generations.
