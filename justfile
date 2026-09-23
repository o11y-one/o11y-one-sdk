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
#   just surface-check  fail if a published artifact carries a non-agentic domain
#   just pack-check     inspect the npm tarballs a release would publish
#   just clean      remove build artifacts
#   just publish-dry rehearse the publish without publishing

set shell := ["bash", "-euo", "pipefail", "-c"]

# The agentic import closure as domain names ("agentic common"), read from
# AGENTIC_CLOSURE_PATHS in tools/generate.sh so there is exactly one list.
agentic_closure := `sed -n '/^AGENTIC_CLOSURE_PATHS=(/,/^)/s|.*proto/o11y_one/\([a-z_]*\).*|\1|p' tools/generate.sh | xargs`

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
    # status, not diff: a newly generated file nobody committed is drift too.
    drift="$(git status --porcelain -- gen internal/gen packages/gen-ts/src packages/gen-ts-agentic/src packages/gen-py/src packages/gen-py-agentic/src)"
    if [[ -n "$drift" ]]; then
        echo "generated code is out of date with buf.gen.yaml / the proto snapshot." >&2
        echo "run 'just gen' and commit the result." >&2
        echo "$drift" >&2
        exit 1
    fi
    echo "generated code is up to date"

# The published surface is the agentic closure and nothing else. Fails if a
# publishable artifact's generated tree carries a proto domain outside
# AGENTIC_CLOSURE_PATHS (tools/generate.sh), or if a whole-tree package loses
# the marker that keeps it off its registry. See docs/proto-subsetting.md.
surface-check:
    #!/usr/bin/env bash
    set -euo pipefail
    closure="{{agentic_closure}}"
    fail=0
    for root in gen/go packages/gen-ts-agentic/src packages/gen-py-agentic/src; do
        for dir in "$root"/o11y_one/*/; do
            domain="$(basename "$dir")"
            if [[ " $closure " != *" $domain "* ]]; then
                echo "$root carries o11y_one/$domain, outside AGENTIC_CLOSURE_PATHS" >&2
                fail=1
            fi
        done
        echo "$root/o11y_one: $(cd "$root/o11y_one" && echo */)"
    done
    if [[ "$(node -p 'require("./packages/gen-ts/package.json").private')" != true ]]; then
        echo 'packages/gen-ts/package.json must stay "private": true (the whole tree is not published)' >&2
        fail=1
    fi
    if ! grep -q '"Private :: Do Not Upload"' packages/gen-py/pyproject.toml; then
        echo "packages/gen-py/pyproject.toml must keep its 'Private :: Do Not Upload' classifier" >&2
        fail=1
    fi
    [[ "$fail" -eq 0 ]] || exit 1
    echo "published surface = agentic closure ($closure); gen-ts and gen-py are unpublishable"

# Pack the npm tarballs exactly as the publish job does and fail on anything
# that must not ship: source maps, .ts that is not .d.ts, tests, test data,
# .env files. The packed @o11y-one/sdk must name a real version of
# @o11y-one/api-agentic, never the workspace protocol.
pack-check:
    #!/usr/bin/env bash
    set -euo pipefail
    out="$(mktemp -d "${TMPDIR:-/tmp}/o11y-pack.XXXXXX")"
    trap 'rm -rf "$out"' EXIT
    # Clean first: tsc never deletes a stale output, and the publish job packs
    # a fresh build.
    pnpm --filter @o11y-one/api-agentic --filter @o11y-one/sdk run clean >/dev/null
    pnpm --filter @o11y-one/api-agentic --filter @o11y-one/sdk run build >/dev/null
    for pkg in gen-ts-agentic sdk-ts; do
        (cd "packages/$pkg" && pnpm pack --pack-destination "$out" >/dev/null)
    done
    fail=0
    for artifact in "$out"/*; do
        listing="$(tar -tzf "$artifact")"
        echo "==> ${artifact##*/}"
        sed 's/^/    /' <<<"$listing"
        bad="$(grep -E '\.map$|\.ts$|(^|/)(tests?|testdata)/|(^|/)\.env' <<<"$listing" | grep -v '\.d\.ts$' || true)"
        if [[ -n "$bad" ]]; then
            echo "${artifact##*/} must not ship:" >&2
            sed 's/^/    /' <<<"$bad" >&2
            fail=1
        fi
    done
    dep="$(tar -xzOf "$out"/o11y-one-sdk-*.tgz package/package.json \
        | node -p 'JSON.parse(require("fs").readFileSync(0, "utf8")).dependencies["@o11y-one/api-agentic"]')"
    echo "packed @o11y-one/sdk depends on @o11y-one/api-agentic@$dep"
    if [[ ! "$dep" =~ ^[0-9]+\.[0-9]+\.[0-9]+(-[0-9A-Za-z.-]+)?$ ]]; then
        echo "that is not a published version; the tarball would not install" >&2
        fail=1
    fi
    exit "$fail"

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

# The published Python distributions, sdist + wheel, into dist/, which is
# exactly what `uv publish dist/*` uploads. o11y-one-api (the whole tree) is
# deliberately absent: it is workspace-only. See docs/proto-subsetting.md.
build-py:
    uv build --package o11y-one-api-agentic --out-dir dist
    uv build --package o11y-one --out-dir dist

build-go:
    cd gen/go && go build ./...
    cd internal/gen/go && go build ./...

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
    cd internal/gen/go && go build ./...
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
    (cd internal/gen/go && go vet ./...)
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
