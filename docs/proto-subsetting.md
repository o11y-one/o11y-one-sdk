# Proto subsetting: only the agentic import closure is vendored and published

## Problem

o11y-api's proto tree has 11 domains (`agentic`, `alerts`, `auth`, `billing`,
`common`, `dashboards`, `mcp`, `objectives`, `organizations`, `query_engine`,
`service_discovery`). The published SDKs (`@o11y-one/sdk`, `o11y_one`,
`gen/go`, `o11y-eval`) touch exactly two of them. Anything else that lives in
this repository becomes public the day the repository does, whether or not a
registry ever sees it: a `.proto` file is the API contract in plain text, and a
Go module is published by the repository being public.

## Decision

**Vendor the agentic import closure and nothing else.** `proto/o11y_one`
holds `agentic/` and `common/` from o11y-api at `PROTO_PIN`, byte for byte bar
the import re-rooting, and that is the whole snapshot. Generation and packaging
follow from it:

- `tools/sync-proto.sh` archives only `proto/o11y_one/agentic` and
  `proto/o11y_one/common` from the o11y-api checkout. Its import audit then
  fails if an agentic proto imports a domain that was not vendored, which is
  how a growth of the closure is noticed rather than silently copied in.
- `tools/generate.sh` runs one `buf generate` pass with
  `buf.gen.agentic.yaml` and the `--path` allowlist `AGENTIC_CLOSURE_PATHS`,
  into the three published artifacts:
  - **TS**: `@o11y-one/api-agentic` (`packages/gen-ts-agentic`)
  - **Python**: `o11y-one-api-agentic` (`packages/gen-py-agentic`)
  - **Go**: `github.com/o11y-one/o11y-one-sdk/gen/go` (`gen/go`)
- The hand-written SDKs depend on those: `@o11y-one/sdk` on
  `@o11y-one/api-agentic`, `o11y_one` on `o11y-one-api-agentic`,
  `tools/ci-runner` on `gen/go` (its `go list -deps` resolves exactly
  `agentic/v1`, `agentic/v1/agenticv1connect` and `common/v1`).
- `just surface-check` (CI and the release `verify` job) fails if
  `proto/o11y_one` or any of the three generated trees carries an
  `o11y_one/<domain>` outside `AGENTIC_CLOSURE_PATHS`. `just pack-check` then
  inspects the built tarballs, wheels and sdists themselves.
- `just gen-check` regenerates and asserts the working tree is unchanged, so
  "generated" and "committed" cannot drift.

## What the closure is (computed, not guessed)

`agentic/v1/*.proto` imports only itself, `o11y_one/common/v1/common.proto`
and Google well-known types; `common.proto` imports nothing. That is the
transitive closure, and it is what `AGENTIC_CLOSURE_PATHS` names. A future
agentic import of another domain is a product decision to widen the published
surface, taken in the same change that adds the path.

## History

Until 2026-09-24 this repository vendored all 11 domains and generated them
into unpublished whole-tree packages (`@o11y-one/api`, `o11y-one-api`,
`internal/gen/go`) "for local use". Nothing consumed them, and going public
would have exposed the entire control-plane contract, so they were removed and
the history rewritten before the repository was made public. A consumer that
needs a domain outside the closure gets a new scoped package, not the whole
tree.
