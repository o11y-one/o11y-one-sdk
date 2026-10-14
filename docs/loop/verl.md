# verl on Loop

`o11y_one.sdk.loop.verl` is verl's own agent-loop extension. A `ToolAgentLoop` runs each
trajectory as one rollout of a Loop run. Its tool calls run in a Loop environment, and its
`reward_score` is that environment's verifier reward.

## Install

```sh
pip install 'o11y-one[verl]'   # verl 0.9.x (0.9.1 tested); Python 3.11 or 3.12
```

vLLM or SGLang is still yours to install, as verl's own docs describe.

## Auth

- A person creates the run in the web (**Connect a trainer**). That gives you two values:
  - `O11Y_RUN`, the run's id. It is not a secret.
  - `O11Y_API_KEY`, a machine key with the `rollout:drive` scope.
- Every Ray worker reads both from its own environment. Set them on every node, through your
  secret manager or an env file.
- Never put the key in a Hydra override or in `ray_init.runtime_env.env_vars`, because Ray
  shows those in its dashboard and job metadata.
- Revoking the key stops resets at the next call.

## Wire-up

```sh
python -m verl.trainer.main_ppo \
  actor_rollout_ref.rollout.agent.agent_loop_config_path=$(python -m o11y_one.sdk.loop.verl) \
  ...
```

This relies on verl 0.9's defaults: `data.return_raw_chat=True`, `rollout.mode=async` and
`multi_turn.format=hermes`.

- Each row of the dataset names `agent_name: loop`. Loop's verl dataset export writes it.
- The agent-loop config (`verl.yaml`, shipped in the package) maps `loop` to `LoopAgentLoop`.
- To use another endpoint, add `base_url: https://…` beside `_target_` in a copy of that file.
- The tools are `shell`, `read_file` and `write_file`. Each tool call is one Loop step, and it
  carries the assistant message that made it.

## Dataset

- `prompt` holds the chat messages.
- `extra_info.loop.case_revision_id` names the case, which the adapter sends on reset.
- verl's `uid` (one per prompt, shared by its `rollout.n` trajectories) is the Loop group.
  Each trajectory takes an index from 0 to n−1 within it.
- **Two rollouts of a group can share an index.** Each worker counts its own trajectories
  of a uid. verl's chunking can split a uid's samples across workers, and a re-run reuses
  its slot by design. Loop checks only that `0 ≤ index < size`, so the group is still
  scored as one.
- A worker keeps counters for its 65,536 most recent uids, far more than one step holds.

## Concurrency

- **Rollouts open at once** = `data.train_batch_size × actor_rollout_ref.rollout.n`. verl runs
  every trajectory of a step concurrently, spread over `agent.num_workers` workers.
  - Set the run's environment limit to at least that.
  - Keep it within your plan's limit, minus what other runs keep open.
- **`run_concurrency_reached` and `plan_concurrency_reached`:** Loop waits up to 60 seconds for
  room, then refuses. The refusal raises `RolloutRefused` out of the trajectory, and verl's
  step fails with the code.
- **`run_paused`:** each reset waits up to 30 minutes for the run to resume.
- **Several tool calls in one turn** (`multi_turn.max_parallel_calls` > 1) are sent to Loop
  one at a time, because the async client's steps take turns.

## Rewards

- Rewards come in the environment's declared order, primary first (rollout.proto).
- `reward_score` is the primary reward, so verl skips its own reward manager.
- A rollout that failed on its task or its verifier keeps its value: train on it.
- Our failure (`INFRASTRUCTURE`, never billed) re-runs the trajectory once, from a fresh reset
  in the same group slot. A second one in a row raises `LoopInfrastructureFailure`.
- **Not sent:** `trainer_step`. verl doesn't hand its step to an agent loop, so the run's
  boards show its series by time, not by step.

## Region

- Run the trainer in the region of the run's Loop environments.
- Watch `step_overhead_p50` on the run's Train live board. One round trip per step is the
  budget against the 5% overhead target.

## Reference run

The reference GRPO run trains Qwen3-1.7B (full FSDP, vLLM colocated) on one 80 GB H100, on
`loop-ref-pyfix` (`examples/loop/pyfix/`): `data.train_batch_size=8` and `rollout.n=8`, so 64
rollouts a step, for 30 steps, with `multi_turn.max_assistant_turns=8`. Give its run a group
size of 8 and an environment limit of 64.

It is measured by the per-step mean reward on the run's Train live board; failures by
class and by code; Loop's overhead (reset, step overhead and the client's round trip) as a
share of rollout wall time, which should stay at or below 5%; rollouts per minute; and GPU
utilisation while each step's rollouts run.
