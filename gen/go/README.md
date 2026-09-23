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

## Module path

```
module github.com/o11y-one/o11y-one-sdk/gen/go
```

This is the repository's own path, so the module resolves with `go get` once
the repository is public. Managed mode bakes it into every generated import
(`go_package_prefix` in `buf.gen.agentic.yaml`); `tools/ci-runner` reaches it
through a `replace` directive.

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
