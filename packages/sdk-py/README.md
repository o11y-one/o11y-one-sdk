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
