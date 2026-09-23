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
    base_url="https://api.o11y.one",
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
