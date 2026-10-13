# `o11y-one`

The Python client for the O11y One API. A thin, hand-written layer over the
generated [`o11y-one-api-agentic`](../gen-py-agentic) package.

## Install

```sh
uv add o11y-one        # or: pip install o11y-one
```

## Use

```python
import os

from o11y_one.sdk import O11yClient, Disposition, classify
from o11y_one.agentic.v1.evaluation_pb2 import ListEvaluationDefinitionsRequest
from o11y_one.agentic.v1.evaluation_connect import AgenticEvaluationServiceClientSync

o11y = O11yClient(
    base_url="https://grpc.o11y.one",
    credential=os.environ["O11Y_API_KEY"],  # o11y_mach.<selector>.<secret>
    org_id=os.environ["O11Y_ORG_ID"],
)

evals = o11y.service_sync(AgenticEvaluationServiceClientSync)
try:
    defs = evals.list_evaluation_definitions(ListEvaluationDefinitionsRequest())
except Exception as err:  # noqa: BLE001 - classify sorts it out
    failure = classify(err)
    if failure.disposition is Disposition.INSUFFICIENT_SCOPE:
        raise SystemExit(f"credential is missing scope {failure.missing_scope}") from err
    raise
```

## What is here, and what deliberately is not

Three modules and nothing else:

| module | responsibility |
|---|---|
| `o11y_one.sdk.client` | transport construction, credential and scoping header injection |
| `o11y_one.sdk.auth`   | the credential wire format and local structural validation |
| `o11y_one.sdk.errors` | the failure taxonomy: reauthenticate / insufficient-scope / version-skew / retry / unclassified |

Service methods are **not** wrapped. `o11y-one-api-agentic` already ships a client class
per service; a hand-written facade over all of them would be a second API surface
to keep in sync with the proto, and it would rot the first time a field is added
upstream. Import the generated client class and hand it to
`O11yClient.service_sync()` / `O11yClient.service()`.

## Record and replay

An externally executed candidate's runtime routes each model and tool call
through a lease tape. Under record, `live` runs and the call is buffered, then
sent to `RecordEvaluationCaseSteps` within the bounds the server publishes on
`sdk_record_replay`. Under replay, `live` never runs: each call is answered from
the source recording through `LookupReplayStep`. The harness code is the same
in both modes.

```python
evals = AgenticClientSync(client.service_sync(AgenticEvaluationServiceClientSync))
tape = evals.record_lease(evaluation_run_id=run_id, lease=lease)  # or replay_lease
case = tape.case(leased_case)
reply = case.model(request_json, lambda: call_model(request_json))
hits = case.tool("search", args_json, lambda: search(args_json))
case.finish()
tape.flush()  # record, then submit
evals.submit_case_outputs(...)
```

`AgenticClient` returns the async twin, whose `live` is a coroutine function.
The sync tape is safe to share across the threads a harness fans its cases out on.

- `ReplayDivergedError` names the step, the divergence kind and both request
  digests. The server has already made it the case's verdict: stop the case and
  do not submit it.
- `LeaseRefusedError` carries a lease refusal (`CASE_ALREADY_SUBMITTED`,
  `LEASE_EXPIRED`, ...). `RecordingUnavailableError` means this deployment
  cannot record or replay, and is not retryable.
- A `ConnectError` with code `UNAVAILABLE` is transient; the buffered calls are
  kept and the next `flush()` resends them.
- Steps that never reached a flush are lost with the process, and the case
  replays as `RECORDING_INCOMPLETE`.
- Redaction is the server's, before anything is digested or stored. The SDK
  redacts nothing and logs no call.

The tape records and replays. `o11y-eval run --record|--replay --candidate <key>`
only asserts, before launching, that the candidate is the kind that mode needs;
the runner never executes a harness.

## Code scorers

A code scorer is a Python `score(input, context)` the server runs in its sandbox.
A member drafts and previews one; an admin publishes it, and only a published
version runs across a dataset. `o11y_one.sdk.scorer` types the contract.

These verbs are a person's, never a machine credential's, so the client carries
no credential and each call carries the person's token:

```python
from connectrpc.request import Headers
from o11y_one.sdk.code_scorer import CodeScorerClientSync

o11y = O11yClient(base_url="https://grpc.o11y.one", org_id=os.environ["O11Y_ORG_ID"])
scorers = CodeScorerClientSync(o11y.service_sync(AgenticEvaluationServiceClientSync))
me = Headers({"authorization": f"Bearer {os.environ['O11Y_USER_TOKEN']}"})
draft = scorers.create_code_scorer(
    config_key="exact-answer",
    name="Exact answer",
    metric_name="quality.exact",
    files={"score.py": open("score.py").read()},
    idempotency_key="exact-answer-v1",
    headers=me,
)
result = scorers.preview_code_scorer(  # waits at most wait_seconds for the sandbox
    score_config_id=draft.score_config_id,
    scorer_input={"candidate_output": "42", "reference_output": "42"},
    idempotency_key="exact-answer-preview-1",
    headers=me,
)
publishing = scorers.publish_code_scorer(  # admin; GetEvaluationScorerConfig reads the outcome
    score_config_id=draft.score_config_id,
    smoke_inputs=[{"candidate_output": "42", "reference_output": "42"}],
    idempotency_key="exact-answer-publish-1",
    headers=me,
)
```

Each returns a `Refusal` for a typed rejection (`SANDBOX_UNAVAILABLE`,
`CODE_SPEC_INVALID`, `CODE_INPUT_INVALID`, `CODE_VERSION_IMMUTABLE`, ...), whose
`message` starts with the server's stable code.

A TypeScript scorer runs where the deployment serves the `typescript-base`
runtime. Its bundle is `.ts` files with the entry `score.ts`, and it imports
only its own files (relative, naming the `.ts`) and Node's built-ins: no npm
packages and no network. [`scorer-kit`](../sdk-ts/scorer-kit) holds its types,
a seeded PRNG to copy into the bundle and an example `score.ts`. There,
`context.seed` and `context.frozen_evaluation_time_unix_nanos` are `bigint`s.

```python
from pathlib import Path

from o11y_one.agentic.v1.evaluation_pb2 import GetAgenticEvaluationCapabilitiesRequest

service = o11y.service_sync(AgenticEvaluationServiceClientSync)
served = service.get_agentic_evaluation_capabilities(
    GetAgenticEvaluationCapabilitiesRequest(), headers=me
).capabilities
kit = Path("packages/sdk-ts/scorer-kit")
draft = scorers.create_code_scorer(
    config_key="sampled-lines",
    name="Sampled lines",
    metric_name="quality.sampled_lines",
    language="typescript",
    files={f: (kit / f).read_text() for f in ("score.ts", "o11y_scorer.ts", "o11y_prng.ts")},
    capabilities=served,  # its served TypeScript runtime; without it, typescript-base v1
    idempotency_key="sampled-lines-v1",
    headers=me,
)
```

A path that is not identifiers ending in the language's extension, or a
TypeScript entry other than `score.ts`, raises `ValidationError` before the
wire, and so does a language the capabilities serve no runtime for
(`code_language_unsupported`).

## Loop rollouts

A person mints a Loop run in the web and hands the trainer two values: the run's
id, `O11Y_RUN` (`trn_…`, not a secret), and an organization machine key with the
`rollout:drive` scope, `O11Y_API_KEY`. `LoopClient` reads both from the
environment when they aren't passed, and never logs or shows the key.

```python
from o11y_one.agentic.v1.rollout_pb2 import LoopToolCallV1, LoopToolExecV1
from o11y_one.sdk.loop import LoopClient, RolloutRefused

loop = LoopClient()  # run=O11Y_RUN, credential=O11Y_API_KEY
try:
    rollout = loop.reset(trainer_step=1, trainer_total_steps=300)
except RolloutRefused as refused:
    raise SystemExit(f"Loop refused the reset: {refused.code}") from refused
step = loop.step(
    [LoopToolCallV1(timeout_millis=60_000, exec=LoopToolExecV1(argv=["pytest", "-q"]))],
    model_message='{"role": "assistant", "content": "run the tests"}',
)
print(step.results[0].exit_code, step.results[0].stdout.decode())
closed = loop.close()  # waits for the verifier's rewards
rewards = {reward.name: reward.value for reward in closed.rewards}
```

- **One open rollout per client.** `reset()` closes the open one first, as an
  OpenEnv environment's reset abandons its episode, so a pooled trainer
  instance that never calls `close()` leaves nothing open. Run a GRPO group as
  one client per rollout, each reset with the same `group_id` (a UUID you pick),
  its own `group_index` and the `group_size`.
- **A trainer adapter names itself:** `LoopClient(adapter=, adapter_version=,
  framework_version=)`, which every reset reports and the run's boards show.
- **`fork(n)`** branches the open rollout into `n` copies of its current state
  and answers a client per copy, this one first.
- **Refusals** raise `RolloutRefused` with the server's stable `code` and, when
  it named one, `retry_after_ms`. `run_paused` is retried after each
  `retry_after_ms` for up to 30 minutes, then raised; every other code, such as
  `plan_concurrency_reached`, raises at once. A revoked or unknown key is the
  server's own `ConnectError`, which `classify()` reads as `REAUTHENTICATE`.
- **Keep error rows with their value.** A rollout that failed on its task or its
  verifier (`closed.failure.failure_class` `TASK` or `VERIFIER`) still has
  `rewards`: each reward's declared minimum, or the environment's failure
  reward. Train on those rows as they are. Dropping them makes a crash score
  better than an honest wrong answer. Only our failures (`INFRASTRUCTURE`)
  carry no reward and are never billed; reset again.

### OpenEnv

`LoopEnvClient` is OpenEnv v0.8.0's own `GenericEnvClient`, sending the key on
its WebSocket upgrade; a stock OpenEnv client sends none, so Loop refuses it.
It needs the `openenv` extra:

```sh
uv add 'o11y-one[openenv]'   # or: pip install 'o11y-one[openenv]'
```

```python
from o11y_one.sdk.loop import LoopEnvClient

with LoopEnvClient("https://api.o11y.one/loop/v1/openenv").sync() as env:
    env.reset()
    env.step({"type": "call_tool", "tool_name": "exec", "arguments": {"argv": ["pytest", "-q"]}})
    result = env.step({"submit": {}})  # done, with the primary reward
print(result.reward, result.metadata["rewards"])
```

## The distinction this package exists to preserve

`UNAUTHENTICATED` and `PERMISSION_DENIED` are different problems:

* **`UNAUTHENTICATED`** — the credential is absent, malformed, unknown, expired,
  or revoked. Re-auth. Retrying cannot change the answer.
* **`PERMISSION_DENIED`** — the credential is fine; it lacks a scope (the server
  names which one) or it was presented to a non-machine surface.

`classify()` keeps them apart, along with `UNAVAILABLE` (auth backend down —
retry with backoff) and `INVALID_ARGUMENT` (SDK/server version skew). Collapsing
these into a single "auth error" is the failure mode this module exists to
prevent.

## Credentials

A machine credential is `o11y_mach.<selector>.<secret>`, presented in the
`x-o11y-key` header. It is:

* **returned exactly once**, by `CreateMachineCredential`. There is no read-back
  RPC and no recovery path — lose it and you rotate.
* **rotated create-then-revoke**, not atomically. A principal may hold several
  active credentials at once, which is what makes zero-downtime rotation work:
  create the new one, deploy it, then revoke the old.
* **revoked effective on the next request**, not on a TTL boundary.
* **expiring** at +365 days by default, capped at three years.

Never send it as `authorization: Bearer` — that path carries the browser session
JWT and a machine credential presented there is rejected.
