# `gen/go` — generated Go bindings

Generated from `proto/o11y_one/**` at the commit in `PROTO_PIN`. **Do not edit.**
Run `just gen` from the repo root instead.

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

## Two modules, on purpose

`gen/go` and `tools/ci-runner` are separate Go modules. A single root module
would be simpler to build, but it would put the CI runner's dependency graph
into the `go.mod` that every SDK consumer inherits. The generated bindings
depend on exactly two things — `google.golang.org/protobuf` and
`connectrpc.com/connect` — and that is the whole point.

## Layout

```
gen/go/o11y_one/<domain>/v1/<file>.pb.go              messages  (protoc-gen-go)
gen/go/o11y_one/<domain>/v1/<domain>v1connect/*.go    clients   (protoc-gen-connect-go)
```

`package` names come from managed mode: `billingv1`, `billingv1connect`, etc.
