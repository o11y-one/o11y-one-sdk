# o11y-one-sdk task runner.
#
# mise pins the toolchain; just sequences the work. There is no meta-build-system
# here on purpose — each recipe delegates to the ecosystem's own tool (pnpm, uv,
# go) rather than teaching a third system to model three dependency graphs.
#
#   just            list recipes
#   just gen        regenerate from the vendored proto snapshot
#   just build      build every package
#   just test       test every package
#   just lint       fmt/vet/typecheck every package
#   just clean      remove build artifacts
#   just publish-dry rehearse the publish without publishing

set shell := ["bash", "-euo", "pipefail", "-c"]

default:
    @just --list

# --- generation -------------------------------------------------------------

# Regenerate from the vendored proto snapshot. Does NOT re-vendor.
gen:
    ./tools/generate.sh

# Re-vendor the proto snapshot from an o11y-api checkout, then regenerate.
# The checkout must be at the commit in PROTO_PIN.
sync-proto checkout="../o11y-api":
    ./tools/sync-proto.sh {{checkout}}

# Fail if the working tree is not byte-identical after a regeneration.
# This is the invariant CI enforces: committed generated code == `just gen`.
gen-check:
    #!/usr/bin/env bash
    set -euo pipefail
    ./tools/generate.sh
    if ! git diff --quiet --exit-code -- gen packages/gen-ts/src packages/gen-ts-agentic/src packages/gen-py/src packages/gen-py-agentic/src; then
        echo "generated code is out of date with buf.gen.yaml / the proto snapshot." >&2
        echo "run 'just gen' and commit the result." >&2
        git --no-pager diff --stat -- gen packages/gen-ts/src packages/gen-ts-agentic/src packages/gen-py/src packages/gen-py-agentic/src >&2
        exit 1
    fi
    echo "generated code is up to date"

# --- install ----------------------------------------------------------------

install: install-ts install-py

install-ts:
    pnpm install --frozen-lockfile

install-py:
    uv sync --all-packages --locked

# --- build ------------------------------------------------------------------

build: build-ts build-py build-go build-ci-runner build-pr-diff

build-ts:
    pnpm -r --filter "./packages/**" run build

# All Python distributions, sdist + wheel, into dist/. o11y-one-api is the whole
# tree (for o11y-web); o11y-one-api-agentic is the agentic + common subset that
# o11y-one depends on. See docs/proto-subsetting.md.
build-py:
    uv build --package o11y-one-api --out-dir dist
    uv build --package o11y-one-api-agentic --out-dir dist
    uv build --package o11y-one --out-dir dist

build-go:
    cd gen/go && go build ./...

# Static binary: CGO_ENABLED=0 so a pipeline can curl it and run it on any
# glibc/musl image without a toolchain.
build-ci-runner version="dev":
    cd tools/ci-runner && CGO_ENABLED=0 go build -trimpath \
        -ldflags "-s -w -X main.version={{version}}" \
        -o bin/o11y-eval .

# The PR eval-diff renderer: consumes the ci-runner's diff document and
# renders a GitHub PR comment. Same static-binary posture as the runner.
build-pr-diff version="dev":
    cd tools/pr-diff && CGO_ENABLED=0 go build -trimpath \
        -ldflags "-s -w -X main.version={{version}}" \
        -o bin/pr-diff .

# --- test -------------------------------------------------------------------

test: test-ts test-py test-go

test-ts:
    pnpm -r --filter "./packages/**" run test

test-py:
    uv run --package o11y-one pytest packages/sdk-py/tests

test-go:
    cd gen/go && go build ./...
    cd tools/ci-runner && go test ./...
    cd tools/pr-diff && go test ./...

# --- lint -------------------------------------------------------------------

lint: lint-proto lint-ts lint-py lint-go

# `buf build`, not `buf lint`: proto style is enforced upstream in o11y-api,
# where a finding can actually be fixed. See buf.yaml.
lint-proto:
    buf build -o /dev/null

lint-ts:
    pnpm -r --filter "./packages/**" run typecheck

lint-py:
    uv run ruff check .
    uv run ruff format --check .

lint-go:
    #!/usr/bin/env bash
    set -euo pipefail
    (cd gen/go && go vet ./...)
    cd tools/ci-runner
    unformatted="$(gofmt -l .)"
    if [[ -n "$unformatted" ]]; then
        echo "gofmt would change these files:" >&2
        echo "$unformatted" >&2
        exit 1
    fi
    go vet ./...

# --- clean ------------------------------------------------------------------

clean:
    rm -rf dist
    rm -rf packages/*/dist packages/*/*.tsbuildinfo
    rm -rf tools/ci-runner/bin
    find . -name __pycache__ -type d -prune -exec rm -rf {} +
    find . -name '*.egg-info' -type d -prune -exec rm -rf {} +

clean-all: clean
    rm -rf node_modules packages/*/node_modules .venv

# --- publish ----------------------------------------------------------------

# Rehearse a publish without publishing anything.
#
# Nothing here can reach a registry: `pnpm publish --dry-run` and
# `uv publish --dry-run` stop before the upload, and there is no token in the
# environment to upload with anyway. Real publishing happens ONLY in
# .github/workflows/publish.yml, over OIDC, from a tag.
#
# Off CI, uv prints "No OIDC token discovered: are you in a supported trusted
# publishing environment?" before it checks the files. That is the expected
# output on a laptop — there is no OIDC token outside a GitHub Actions job, which
# is precisely the property that makes trusted publishing worth having. The
# artifact checks still run and the recipe still exits 0.
publish-dry: build
    @echo "==> npm (dry run)"
    pnpm -r --filter "./packages/**" publish --dry-run --no-git-checks
    @echo "==> PyPI (dry run)"
    uv publish --dry-run dist/*
    @echo "==> ci-runner binaries"
    @just release-matrix
    @echo
    @echo "Nothing was published. Tag a release to publish; see README."

# Print the platform matrix the release workflow cross-compiles.
release-matrix:
    @echo "  linux/amd64 linux/arm64 darwin/amd64 darwin/arm64 windows/amd64"
