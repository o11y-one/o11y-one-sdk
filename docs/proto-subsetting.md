# Proto subsetting: only the agentic import closure is published

## Problem

This repo vendors the whole o11y-api proto tree — 11 domains (`agentic`,
`alerts`, `auth`, `billing`, `common`, `dashboards`, `mcp`, `objectives`,
`organizations`, `query_engine`, `service_discovery`) — and generates all of it
into `internal/gen/go`, `packages/gen-ts`, and `packages/gen-py`.

The published agentic SDKs (`@o11y-one/sdk`, `o11y_one`) are thin wrappers over
the generated code. Before this change they depended on the **whole** generated
package (`@o11y-one/api`, `o11y-one-api`), so anyone installing the agentic SDK
transitively pulled all 11 domains — `billing`, `auth`, `dashboards`, and the
rest — even though the agentic surface never touches them.

We want everything this repo publishes to be **only the agentic import
closure**, while keeping the whole generated code available locally.

## The agentic import closure (computed, not guessed)

Chased from the `import` lines in the agentic protos
(`proto/o11y_one/agentic/v1/*.proto`):

| proto | imports |
|---|---|
| `agentic.proto`    | `google/protobuf/{struct,timestamp}`, `o11y_one/common/v1/common.proto` |
| `evaluation.proto` | `google/protobuf/timestamp`, `o11y_one/common/v1/common.proto`, `o11y_one/agentic/v1/agentic.proto` |
| `agent_run.proto`  | `google/protobuf/timestamp`, `o11y_one/agentic/v1/{evaluation,artifact}.proto` |
| `artifact.proto`   | `google/protobuf/timestamp`, `o11y_one/agentic/v1/evaluation.proto` |
| `trace_view.proto` | `google/protobuf/timestamp`, `o11y_one/agentic/v1/{evaluation,agent_run,artifact}.proto` |

`common.proto` imports **nothing** (no protos, no well-known types).

**Closure = `o11y_one/agentic/v1/*` + `o11y_one/common/v1/*`**, plus the
`google/protobuf` well-known types buf carries itself. The only cross-domain
edge out of `agentic` is into `common`, and `common` is a leaf. No surprises:
no `billing`, `auth`, `query_engine`, or anything else is reachable.

If the agentic protos ever grow an import into a new domain, `sync-proto.sh`'s
import audit still passes (the domain is in the whole vendored tree), but the
subset generation would emit code referencing an ungenerated module — so a new
domain in the closure must be added to `AGENTIC_CLOSURE_PATHS` in
`tools/generate.sh` (and this table) in the same change.

## Decision

**Keep the vendored proto mirror whole; make GENERATION + PACKAGING per-domain.**

We do NOT delete the non-agentic protos from the source-of-truth mirror — it
is `proto/o11y_one` at `PROTO_PIN`, byte for byte bar the import re-rooting,
which is what makes the snapshot reproducible. Instead:

- The whole tree is still generated, into `internal/gen/go`,
  `packages/gen-ts` (`@o11y-one/api`) and `packages/gen-py` (`o11y-one-api`),
  for local use. **None of it is publishable**: `packages/gen-ts` is
  `"private": true`, `packages/gen-py` carries the `Private :: Do Not Upload`
  classifier PyPI rejects and is not built by `just build-py`, and Go refuses
  to let any module outside this repository import an `internal/` path.
- A **second, `--path`-scoped generation pass** emits the agentic closure alone
  into the three artifacts that are published:
  - **TS**: `@o11y-one/api-agentic` (`packages/gen-ts-agentic`)
  - **Python**: `o11y-one-api-agentic` (`packages/gen-py-agentic`)
  - **Go**: `github.com/o11y-one/o11y-one-sdk/gen/go` (`gen/go`)
- The agentic SDKs depend on the scoped distributions instead of the whole ones:
  - `@o11y-one/sdk` → `@o11y-one/api-agentic`
  - `o11y_one` → `o11y-one-api-agentic`
- `just surface-check` (CI and the release `verify` job) fails if any of the
  three carries an `o11y_one/<domain>` outside `AGENTIC_CLOSURE_PATHS`, or if
  either whole-tree package loses its unpublishable marker.

### Why a separate distribution rather than a subpath export

A subpath export (`@o11y-one/api/agentic`) of the whole package would NOT shrink
the footprint: npm/PyPI install the whole package regardless of which subpaths a
consumer imports, and a Python wheel ships every module under its `packages`
root. The dependency closure is what a subsetting change has to move, and that
means a distribution boundary. So the mechanism is a dedicated package per
language whose published artifact contains only agentic + common.

### Why this is not code duplication we have to maintain

The scoped package's `src/` is generated, never hand-written, and the subset
matches the corresponding `agentic/` + `common/` subtrees of the whole package
in everything but one descriptor option: each embedded file descriptor carries
`go_package`, which names the Go module that file's Go code lives in (`gen/go`
for the closure, `internal/gen/go` for the whole tree). Both come from the same
protos via the same pinned buf plugins; only the `--path` allowlist, the `out`
root and that Go prefix differ. `just gen-check` regenerates both and
asserts the working tree is unchanged, so drift is a CI failure, not a latent
bug.

## Mechanism per language

### TypeScript

`buf.gen.agentic.yaml` runs `protoc-gen-es` (same pinned version as
`buf.gen.yaml`) into `packages/gen-ts-agentic/src`, invoked with
`--path proto/o11y_one/agentic --path proto/o11y_one/common`. The package
mirrors `@o11y-one/api`'s `./*` subpath export map, so the SDK imports move from
`@o11y-one/api/o11y_one/agentic/v1/evaluation_pb` to
`@o11y-one/api-agentic/o11y_one/agentic/v1/evaluation_pb`. `@o11y-one/sdk`'s only
`@o11y-one/api*` dependency is now `@o11y-one/api-agentic`.

### Python

`buf.gen.agentic.yaml` runs the protobuf/pyi/connect Python plugins (same pinned
versions) into `packages/gen-py-agentic/src`. The new distribution
`o11y-one-api-agentic` ships the `o11y_one` PEP 420 namespace restricted to
`o11y_one.agentic` + `o11y_one.common`. `o11y_one` (the hand-written SDK)
depends on it instead of `o11y-one-api`, and still contributes `o11y_one.sdk` to
the same namespace. There is no `src/o11y_one/__init__.py` in either generated
distribution — `tools/generate.sh` asserts none appears in the new package too.

### Go

Go links only what is imported, so the binaries never needed subsetting. The
**module** did: a Go module is published by the repository being public, and
`gen/go` held all 11 domains. So `buf.gen.agentic.yaml` also runs the Go
plugins, into `gen/go` (the public module, managed `go_package_prefix`
`github.com/o11y-one/o11y-one-sdk/gen/go`), and `buf.gen.yaml` points the whole
tree at `internal/gen/go` (prefix `.../internal/gen/go`), a separate module Go
will not let any outside module import. `go list -deps` on `tools/ci-runner`
resolves exactly:

```
gen/go/o11y_one/agentic/v1
gen/go/o11y_one/agentic/v1/agenticv1connect
gen/go/o11y_one/common/v1
```

`tools/pr-diff` links no generated code at all. Neither tool imports
`internal/gen/go`; code in this repository may, if it ever needs another
domain.

## Footprint: before → after

| SDK | before | after |
|---|---|---|
| `@o11y-one/sdk` (npm) | dep `@o11y-one/api` → 11 domains | dep `@o11y-one/api-agentic` → agentic + common |
| `o11y_one` (PyPI)     | dep `o11y-one-api` → 11 domains | dep `o11y-one-api-agentic` → agentic + common |
| `gen/go` (Go module)  | 11 domains, public with the repo | agentic + common; the rest under `internal/gen/go` |
| `o11y-eval` (Go)      | links agentic + common (already) | unchanged |

The whole `@o11y-one/api` / `o11y-one-api` / `internal/gen/go` are not
published and have no external consumer: o11y-web talks to the API through
`@o11y-one/typed-fetch`, not these packages. A consumer that needs a domain
outside the closure gets a new scoped package, not the whole tree.
