# Proto subsetting: the agentic SDK carries only its import closure

## Problem

This repo vendors the whole o11y-api proto tree — 11 domains (`agentic`,
`alerts`, `auth`, `billing`, `common`, `dashboards`, `mcp`, `objectives`,
`organizations`, `query_engine`, `service_discovery`) — and generates all of it
into `gen/go`, `packages/gen-ts`, and `packages/gen-py`.

The published agentic SDKs (`@o11y-one/sdk`, `o11y_one`) are thin wrappers over
the generated code. Before this change they depended on the **whole** generated
package (`@o11y-one/api`, `o11y-one-api`), so anyone installing the agentic SDK
transitively pulled all 11 domains — `billing`, `auth`, `dashboards`, and the
rest — even though the agentic surface never touches them.

We want the agentic SDK's published footprint to be **only the agentic import
closure**, while keeping the whole generated code available for o11y-web, which
reuses these same stubs and may need any domain.

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
faithfully mirrors o11y-api and o11y-web consumes other domains from the whole
generated packages. Instead:

- The whole tree is still generated into `gen/go`, `packages/gen-ts`
  (`@o11y-one/api`), and `packages/gen-py` (`o11y-one-api`) — unchanged, for
  o11y-web.
- A **second, `--path`-scoped generation pass** emits the agentic closure alone
  into two new dedicated distributions:
  - **TS**: `@o11y-one/api-agentic` (`packages/gen-ts-agentic`)
  - **Python**: `o11y-one-api-agentic` (`packages/gen-py-agentic`)
- The agentic SDKs depend on the scoped distributions instead of the whole ones:
  - `@o11y-one/sdk` → `@o11y-one/api-agentic`
  - `o11y_one` → `o11y-one-api-agentic`

### Why a separate distribution rather than a subpath export

A subpath export (`@o11y-one/api/agentic`) of the whole package would NOT shrink
the footprint: npm/PyPI install the whole package regardless of which subpaths a
consumer imports, and a Python wheel ships every module under its `packages`
root. The dependency closure is what a subsetting change has to move, and that
means a distribution boundary. So the mechanism is a dedicated package per
language whose published artifact contains only agentic + common.

### Why this is not code duplication we have to maintain

The scoped package's `src/` is generated, never hand-written, and the subset is
**byte-identical** to the corresponding `agentic/` + `common/` subtrees of the
whole package (verified: `diff -rq` is clean for both TS and Python). Both come
from the same protos via the same pinned buf plugins; only the `--path`
allowlist and the `out` root differ. `just gen-check` regenerates both and
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

**No change needed.** The Go module `gen/go` is a single module with a package
per proto-package, and Go links only what is imported. `go list -deps` on
`tools/ci-runner` resolves exactly:

```
gen/go/o11y_one/agentic/v1
gen/go/o11y_one/agentic/v1/agenticv1connect
gen/go/o11y_one/common/v1
```

`tools/pr-diff` links no generated code at all. The Go binaries already carry
the agentic closure and nothing else, so there is nothing to subset — the
per-package layout gives Go the property the TS/Python packages had to be
restructured to get.

## Footprint: before → after

| SDK | before | after |
|---|---|---|
| `@o11y-one/sdk` (npm) | dep `@o11y-one/api` → 11 domains | dep `@o11y-one/api-agentic` → agentic + common |
| `o11y_one` (PyPI)     | dep `o11y-one-api` → 11 domains | dep `o11y-one-api-agentic` → agentic + common |
| `o11y-eval` (Go)      | links agentic + common (already) | unchanged |

The whole `@o11y-one/api` / `o11y-one-api` / `gen/go` remain published (versions
stay `0.0.0`) so o11y-web keeps consuming any domain it needs.

## Left for o11y-web to adopt

Nothing is forced. o11y-web keeps depending on the whole `@o11y-one/api` /
`o11y-one-api`. If any o11y-web surface turns out to be agentic-only, it can
optionally switch that surface to `@o11y-one/api-agentic` /
`o11y-one-api-agentic` to shrink its own install closure — but that is its call,
not a requirement of this change.
