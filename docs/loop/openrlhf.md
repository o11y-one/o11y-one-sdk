# OpenRLHF on Loop

`o11y_one.sdk.loop.openrlhf` is OpenRLHF's own `--train.agent_func_path` agent: a
`MultiTurnAgentExecutor` that runs each sample as one rollout of a Loop run. A turn's tool
calls run in a Loop environment, and the sample's reward is that environment's verifier
reward.

## Install

```sh
pip install o11y-one   # into your OpenRLHF 0.11.2 image; Python 3.11 or 3.12
```

- There is no extra. OpenRLHF's wheel pins CUDA builds (deepspeed, flash-attn) and ships
  for Linux x86_64 only, so it stays in your image as you install it.
- The adapter refuses to import outside OpenRLHF 0.11.2 to 0.12, and names the release it
  found.

## Auth

- A person creates the run in the web (**Connect a trainer**). That gives you two values:
  - `O11Y_RUN`, the run's id. It is not a secret.
  - `O11Y_API_KEY`, a machine key with the `rollout:drive` scope.
- Every Ray node reads both from its own environment: your secret manager, or an env file.
- Never put the key on the command line or in `runtime_env`.
- `O11Y_BASE_URL` names another endpoint, such as your region's.
- Revoking the key stops resets at the next call.

## Wire-up

```sh
python -c 'import sys, o11y_one.sdk.loop.openrlhf as m; from transformers import AutoTokenizer; \
  m.render_prompts(sys.argv[1], sys.argv[2], AutoTokenizer.from_pretrained(sys.argv[3]))' \
  pyfix.jsonl pyfix.rendered.jsonl Qwen/Qwen3-1.7B

python -m openrlhf.cli.train_ppo_ray \
  --train.agent_func_path $(python -c 'import o11y_one.sdk.loop.openrlhf as m; print(m.__file__)') \
  --data.input_key prompt --data.label_key label \
  ...   # without --data.apply_chat_template: the prompts are already rendered
```

- **`render_prompts`** renders each row's messages with the model's chat template and the
  tools `shell`, `read_file` and `write_file`. OpenRLHF itself never passes `tools=`.
- **The agent path** is the installed module's own file, never a copy. OpenRLHF executes
  whatever file the path names.
- **Tool calls** are parsed in the Hermes `<tool_call>{json}</tool_call>` form, which Qwen3
  emits. Each turn's calls (up to 16) go to Loop as one step, carrying the assistant message.
  The results come back as the chat template's own tool turn.
- **A turn with no tool call ends the sample.**

## Dataset

- Loop's OpenRLHF dataset export holds `prompt`, the messages, and `label`, a JSON string.
- The adapter sends the label's `case_revision_id` on reset.
- **Not sent:** `group_id` and `trainer_step`. OpenRLHF's executor gets neither, so each
  sample is its own group on the boards, and its series run by time, not by step.

## Concurrency

- **Rollouts open at once** = `rollout.vllm_generate_batch_size` (by default
  `rollout.batch_size`) × `rollout.n_samples_per_prompt`. More with `--train.async_enable`.
  - Set the run's environment limit to at least that.
  - Keep it within your plan's limit, minus what other runs keep open.
- **`run_concurrency_reached` and `plan_concurrency_reached`:** Loop waits up to 60 seconds
  for room, then refuses. The refusal raises `RolloutRefused`, which fails the sample's Ray
  task and then the step.
- **`run_paused`:** each reset waits up to 30 minutes for the run to resume.

## Rewards

- Rewards come in the environment's declared order, primary first (rollout.proto).
- The sample's `reward` and `scores` are the primary reward, set once its rollout closes,
  however the sample ended: a turn with no tool call, or the length budget. Every step before
  that rewards 0, so OpenRLHF's per-step sum is never added to it.
- A rollout that failed on its task or its verifier keeps its value: train on it.
- Our failure (`INFRASTRUCTURE`, never billed) re-runs the sample once. A second one in a row
  raises `LoopInfrastructureFailure`.

## Region

Run the trainer in the region of the run's Loop environments, set `O11Y_BASE_URL` to that
region's endpoint, and watch `step_overhead_p50` on the run's Train live board.

## Reference run

The reference run trains Qwen3-1.7B on two 80 GB H100s (Ray: the actor and vLLM), on
`loop-ref-pyfix` (`examples/loop/pyfix/`): `rollout.batch_size=8` and
`rollout.n_samples_per_prompt=8`, so 64 rollouts a step, for 30 steps. Give its run an
environment limit of 64.

It is measured by the per-step mean reward on the run's Train live board; failures by
class and by code; Loop's overhead (reset, step overhead and the client's round trip) as a
share of rollout wall time, which should stay at or below 5%; rollouts per minute; and GPU
utilisation while each step's rollouts run.
