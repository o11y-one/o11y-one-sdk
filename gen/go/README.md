# `gen/go` — generated Go bindings for the agentic API

Generated from the agentic import closure — `proto/o11y_one/agentic/**` and
`proto/o11y_one/common/**` — at the commit in `PROTO_PIN`. **Do not edit.** Run
`just gen` from the repo root instead.

This is the public Go module, and it carries exactly what the npm and PyPI
packages carry: the closure named by `AGENTIC_CLOSURE_PATHS` in
`tools/generate.sh`. `just surface-check` fails if another domain appears here.

## The whole tree is `internal/`

Every other domain is generated into `internal/gen/go`
(`github.com/o11y-one/o11y-one-sdk/internal/gen/go`). Go refuses to compile an
import of an `internal/` path from any module outside
`github.com/o11y-one/o11y-one-sdk/...`, so that code can never become public
surface, even with the repository public. Code in this repository may import it.

## Module path is a placeholder

```
module github.com/o11y-one/o11y-one-sdk/gen/go
```

Nothing has claimed `github.com/o11y-one` yet. Go module paths are baked into
every generated file's import statements, so this had to be *some* concrete
string before the org name is settled — and picking a fake-looking placeholder
(`example.com/...`) would only mean a second rename later.

**When the operator names the real org / repo, one change fixes everything:**

```sh
# 1. new path in the module declaration
sed -i '' 's|github.com/o11y-one/o11y-one-sdk|<REAL>|' gen/go/go.mod tools/ci-runner/go.mod
# 2. new path in managed mode, then regenerate — imports follow automatically
sed -i '' 's|github.com/o11y-one/o11y-one-sdk|<REAL>|' buf.gen.yaml
just gen
```

The same placeholder appears in `packages/*/package.json` and `pyproject.toml`
`repository` / `Source` URLs, where it is only metadata.

## Separate modules, on purpose

`gen/go`, `internal/gen/go` and `tools/ci-runner` are separate Go modules. A
single root module would be simpler to build, but it would put the CI runner's
dependency graph into the `go.mod` that every SDK consumer inherits. The
generated bindings depend on exactly two things — `google.golang.org/protobuf`
and `connectrpc.com/connect` — and that is the whole point.

## Layout

```
gen/go/o11y_one/agentic/v1/<file>.pb.go             messages  (protoc-gen-go)
gen/go/o11y_one/agentic/v1/agenticv1connect/*.go    clients   (protoc-gen-connect-go)
gen/go/o11y_one/common/v1/common.pb.go              messages
```

`package` names come from managed mode: `agenticv1`, `agenticv1connect`,
`commonv1`.
