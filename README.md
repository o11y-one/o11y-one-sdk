# o11y-one-sdk

Client SDKs and the CI runner for the [O11y One](https://o11y.one) API, in one
repository: TypeScript, Python, Go, and the `o11y-eval` binary that CI pipelines
invoke.

Everything here is downstream of one input — the `.proto` files that o11y-api
owns. This repo vendors a snapshot of them, generates code from it, commits the
result, and publishes it.

```
o11y-one-sdk/
├── PROTO_PIN              the o11y-api commit this snapshot came from
├── proto/o11y_one/        vendored .proto snapshot          (read-only here)
├── buf.yaml               module layout
├── buf.gen.yaml           whole tree, three languages, plugins pinned by exact version
├── buf.gen.agentic.yaml   the agentic closure: the only generated code published
├── gen/go/                Go module, agentic closure        (committed)
├── internal/gen/go/       Go module, whole tree             (committed, unimportable)
├── packages/
│   ├── gen-ts/            @o11y-one/api          TS, whole tree          (private)
│   ├── gen-ts-agentic/    @o11y-one/api-agentic  TS, agentic closure
│   ├── gen-py/            o11y-one-api           Python, whole tree      (private)
│   ├── gen-py-agentic/    o11y-one-api-agentic   Python, agentic closure
│   ├── sdk-ts/            @o11y-one/sdk          hand-written
│   └── sdk-py/            o11y-one               hand-written
├── tools/
│   ├── sync-proto.sh      re-vendor from o11y-api, then regenerate
│   ├── generate.sh        regenerate without re-vendoring
│   └── ci-runner/         o11y-eval, a static Go binary
├── mise.toml              the toolchain, exact versions
└── justfile               the tasks
```

## Getting set up

```sh
mise install          # node, pnpm, python, uv, go, buf, just — exact versions
just install          # pnpm install --frozen-lockfile + uv sync --locked
just build
just test
```

`mise.toml` is the single source of truth for tool versions; CI installs from the
same file, so a green laptop and a green runner mean the same thing. There is no
Turborepo, Nx, or moon here on purpose: each package is built by its own
ecosystem's tool and `just` sequences them. A fourth system modelling three
dependency graphs would earn its keep only at a scale this repo is nowhere near.

## The regen ritual

The `.proto` files are **not** editable here. o11y-api owns them; this repo holds
a snapshot, and `PROTO_PIN` records which commit it came from. Regeneration is
deliberately manual — there is no bot, no submodule, no scheduled sync. Moving
the snapshot is a decision someone makes and reviews.

```sh
# 1. check out o11y-api at the commit you want
git -C ../o11y-api checkout <sha>

# 2. update PROTO_PIN to that sha, then re-vendor and regenerate
just sync-proto ../o11y-api

# 3. review the diff — BOTH halves of it
git diff proto/            # what actually changed upstream
git diff gen/ packages/    # what that did to the generated surface

# 4. commit the snapshot, the pin and the generated code TOGETHER
```

`sync-proto.sh` refuses to run if the checkout is not at `PROTO_PIN`
(`--allow-dirty-pin` overrides, and tells you to update the pin in the same
commit). It then audits every import, builds the module, and regenerates.

It extracts the snapshot with `git archive` **from the commit**, never by copying
the working tree — and says so when the checkout is dirty. o11y-api is worked on
continuously and its tree is routinely mid-edit; copying it would vendor
somebody's half-finished change under a `PROTO_PIN` claiming a specific commit,
producing a snapshot nobody could ever reproduce.

### The one edit made to vendored bytes

`sync-proto.sh` rewrites intra-tree imports to carry an `o11y_one/` prefix:

```diff
- import "common/v1/common.proto";
+ import "o11y_one/common/v1/common.proto";
```

o11y-api roots its buf module at `proto/o11y_one`, so its file paths have no
prefix — which would make the generated Python top-level packages `common`,
`billing`, `auth`. A published PyPI distribution cannot squat those names on
`sys.path`. Re-rooting at `proto/` fixes Python, gives Go and TS a tidier prefix,
and makes `buf lint`'s `PACKAGE_DIRECTORY_MATCH` pass for the first time.

The transform is deterministic, so re-running at the same pin produces a
byte-identical tree — which is what CI's `gen-check` asserts. **Nothing on the
wire changes**: RPC and message full names come from the proto `package`
statement, which is untouched. Only descriptor file names move.

### Generated code is committed

All of it. `gen/go/o11y_one/**`, `internal/gen/go/o11y_one/**`,
`packages/*/src/o11y_one/**`. Three reasons:

1. **The diff is the review.** A proto change that alters the generated surface
   shows up as a reviewable diff instead of appearing at publish time.
2. **Consumers build without buf.** `go get`, `pnpm add`, `pip install` — none
   of them run a code generator.
3. **CI can prove it.** `just gen-check` regenerates and fails if the result
   differs from what is committed, so "generated" and "committed" cannot drift.

Codegen uses BSR remote plugins pinned to exact versions in `buf.gen.yaml`
(`bufbuild/es`, `protocolbuffers/go`, `connectrpc/go`, `protocolbuffers/python`,
`protocolbuffers/pyi`, `connectrpc/python`). Remote rather than local plugin
binaries: local ones would add five more publishers to this repo's dependency
graph and five more lockfile entries for consumers to reason about. Generation
happens rarely and its output is committed, so a network dependency there costs
nothing downstream. Anonymous BSR use is rate-limited; a full `just gen` is
twelve requests (six plugins, two passes), comfortably inside it, which is why
there is no `BUF_TOKEN` here.

### If `just gen` fails with a Buf auth error

```
Failure: the BUF_TOKEN environment variable is not valid for buf.build
Failure: your Buf API token for buf.build is invalid
```

Generation is anonymous and needs no credential at all, but buf will still try a
stale one if it finds it. Clear both places it looks:

```sh
unset BUF_TOKEN            # the environment
grep -n buf.build ~/.netrc # and remove the stale machine entry, if any
```

`resource_exhausted: too many requests` means the anonymous BSR rate limit; wait
a minute and re-run. A single `just gen` is twelve requests, so this only shows
up if something is looping.

## The packages

| package | published as | contents |
|---|---|---|
| `packages/gen-ts-agentic` | `@o11y-one/api-agentic` (npm) | generated types + service descriptors, agentic closure |
| `packages/sdk-ts` | `@o11y-one/sdk` (npm) | transport, credentials, error taxonomy |
| `packages/gen-py-agentic` | `o11y-one-api-agentic` (PyPI) | generated messages + Connect clients, agentic closure |
| `packages/sdk-py` | `o11y-one` (PyPI) | transport, credentials, error taxonomy |
| `gen/go` | `github.com/o11y-one/o11y-one-sdk/gen/go` | generated messages + connect-go clients, agentic closure |
| `tools/ci-runner` | GitHub release binaries | `o11y-eval`, static, signed |
| `packages/gen-ts`, `packages/gen-py`, `internal/gen/go` | **not published** | the whole tree, every domain, for local use |

The agentic closure is `o11y_one/agentic` + `o11y_one/common`. Why, and how the
whole tree is kept unpublishable, is in
[`docs/proto-subsetting.md`](docs/proto-subsetting.md); `just surface-check`
enforces it.

The hand-written SDKs are deliberately thin: transport construction, credential
injection, and the failure taxonomy. They do **not** wrap RPCs. The generated
packages already expose every service; a facade over 29 of them would be a second
API surface to keep in sync with the proto, and it would rot on the first field
addition upstream.

### The Go module path is a placeholder

`github.com/o11y-one/o11y-one-sdk` is not claimed yet. Go bakes module paths into
every generated import, so it had to be a concrete string before the org name is
settled. `gen/go/README.md` has the one-command rename for when it is.

### `o11y_one` is a shared Python namespace

`o11y-one-api-agentic` and `o11y-one` both contribute to the `o11y_one` package,
which is a [PEP 420](https://peps.python.org/pep-0420/) implicit namespace: the
generated distribution owns `o11y_one.agentic` and `o11y_one.common`, and the SDK
owns `o11y_one.sdk`. Neither may ship an `o11y_one/__init__.py`; `tools/generate.sh`
asserts this, and `packages/sdk-py/tests` proves the two import side by side.

## Publishing

Nothing publishes from a laptop. `just publish-dry` rehearses everything without
uploading; the real thing happens only in `.github/workflows/publish.yml`, on a
`v*` tag, in a protected `release` environment.

One tag publishes all four packages at the same version, plus signed `o11y-eval`
binaries. They move together because they come from one proto snapshot; letting
them drift would create a compatibility matrix nobody wants to maintain. The
`verify` job fails the release if a manifest version and the tag disagree.

## Supply-chain posture

The rule this repo follows: **no long-lived publishing credentials, and no
install-time code execution.**

| measure | where |
|---|---|
| No `NPM_TOKEN`, no `PYPI_TOKEN` — publishing is OIDC only | `publish.yml` (npm trusted publishing, PyPI Trusted Publishers) |
| npm provenance attestations (`npm publish --provenance`) | `publish.yml`; verify with `npm audit signatures` |
| `permissions: {}` at workflow level, minimum granted per job | `ci.yml`, `publish.yml` |
| `id-token: write` on publish jobs **only**, never in CI | `publish.yml` |
| Publish gated on a protected environment | `publish.yml` (`environment: release`) |
| Every action pinned to a full commit SHA, never a tag | `ci.yml`, `publish.yml` |
| `persist-credentials: false` on every checkout | `ci.yml`, `publish.yml` |
| Third-party actions kept to two (`mise-action`, `cosign-installer`); releases cut with the preinstalled `gh` | `publish.yml` |
| npm install scripts blocked, with an explicit (currently empty) allowlist | `pnpm-workspace.yaml` (`allowBuilds`) |
| No npm package younger than 7 days | `pnpm-workspace.yaml` (`minimumReleaseAge: 10080`) |
| No silent dependency downgrades | `pnpm-workspace.yaml` (`trustPolicy: no-downgrade`) |
| Lockfiles committed; CI never re-resolves | `pnpm install --frozen-lockfile`, `uv sync --locked` |
| Codegen plugins pinned to exact versions | `buf.gen.yaml` |
| Toolchain pinned to exact versions | `mise.toml` |
| `o11y-eval` binaries checksummed and keyless-signed | `publish.yml` (cosign + Sigstore) |
| Reproducible Go builds (`-trimpath`, `CGO_ENABLED=0`) | `justfile`, `publish.yml` |

Known gap, stated rather than hidden: uv has no age-based equivalent of pnpm's
`minimumReleaseAge`, so a new Python dependency is not held back for a week. The
committed `uv.lock` plus `uv sync --locked` means nothing enters the graph
without a reviewed lockfile diff — reviewers should check release dates on
anything new.

### Verifying an `o11y-eval` binary

```sh
cosign verify-blob o11y-eval-linux-amd64 \
  --bundle o11y-eval-linux-amd64.cosign.bundle \
  --certificate-identity-regexp '^https://github.com/o11y-one/o11y-one-sdk/\.github/workflows/publish\.yml@' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
```

## `o11y-eval` exit codes

The verdict **is** the exit code, because a CI system sees nothing else:

| code | meaning |
|---|---|
| `0` | improvement — gate passes |
| `1` | regression — a comparison completed and the result is worse than baseline |
| `2` | indeterminate — no verdict reachable (too few cases, no baseline) |
| `3` | infra-failure — the runner or platform broke; says nothing about the change |
| `64` | usage-error — bad invocation |

`2` and `3` exist so that a flaky network never gets reported as a regression,
and so that a stub never gets reported as a pass. **Today every subcommand
returns `3`**: the runner is a scaffold whose RPCs do not exist in the snapshot
at `PROTO_PIN` yet. It says so when you run it.

## License

Apache-2.0.
