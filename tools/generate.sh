#!/usr/bin/env bash
#
# generate.sh — run buf generate for all three languages.
#
# Split out of sync-proto.sh so `just gen` can regenerate without re-vendoring
# (useful when only buf.gen.agentic.yaml changed). Generated code is COMMITTED; this
# script must be deterministic, and CI's gen-check job runs it and asserts the
# working tree is unchanged.
#
# Two properties this script is careful about:
#
#   1. It is ALL-OR-NOTHING. The previous output has to be cleared before
#      generating (a file deleted upstream must disappear here), but a failed
#      generate must not leave the repo gutted. So the trees are moved aside,
#      not deleted, and restored if anything goes wrong.
#
#   2. It RETRIES on BSR rate limiting. Codegen uses anonymous remote plugins;
#      a full run is twelve requests, which is normally fine, but a busy shared
#      egress IP can still trip resource_exhausted. Retrying a handful of times
#      is the difference between a flaky CI job and a real signal.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

# The generated subtrees. Their parents hold hand-written files that must
# survive (the go.mod files, the package manifests), which is why
# buf.gen.agentic.yaml sets `clean: false` and the wiping happens here, scoped
# to these paths. Only the agentic closure (agentic + common) is vendored and
# generated; see docs/proto-subsetting.md.
OUTPUTS=(
  gen/go/o11y_one
  packages/gen-ts-agentic/src/o11y_one
  packages/gen-py-agentic/src/o11y_one
)

# The agentic import CLOSURE, as buf --path arguments: the proto trees the
# agentic protos transitively import (agentic itself + common; common imports
# nothing). Chased from the `import` lines, not guessed — see
# docs/proto-subsetting.md. A new domain entering the closure must be added here.
# `just surface-check` reads this list: it is the allowlist for every
# published artifact.
AGENTIC_CLOSURE_PATHS=(
  --path proto/o11y_one/agentic
  --path proto/o11y_one/common
)

backup="$(mktemp -d "${TMPDIR:-/tmp}/o11y-gen.XXXXXX")"
restored=0

restore() {
  [[ "$restored" -eq 1 ]] && return
  restored=1
  echo "==> generation failed; restoring the previous output" >&2
  for i in "${!OUTPUTS[@]}"; do
    out="${OUTPUTS[$i]}"
    rm -rf "$out"
    if [[ -d "$backup/$i" ]]; then
      mkdir -p "$(dirname "$out")"
      mv "$backup/$i" "$out"
    fi
  done
  rm -rf "$backup"
}

cleanup() {
  local status=$?
  if [[ "$status" -ne 0 ]]; then
    restore
  else
    rm -rf "$backup"
  fi
}
trap cleanup EXIT

echo "==> setting aside previous output"
for i in "${!OUTPUTS[@]}"; do
  out="${OUTPUTS[$i]}"
  if [[ -d "$out" ]]; then
    mv "$out" "$backup/$i"
  fi
done

# Run `buf generate <args...>` with a handful of retries on BSR rate limiting.
# Codegen uses anonymous remote plugins; a busy shared egress IP can trip
# resource_exhausted, and retrying is the difference between a flaky CI job and
# a real signal.
run_buf() {
  local attempts=4 attempt err
  for attempt in $(seq 1 "$attempts"); do
    if err="$(buf generate "$@" 2>&1)"; then
      return 0
    fi
    if [[ "$attempt" -eq "$attempts" ]] || ! grep -qE 'resource_exhausted|unavailable' <<<"$err"; then
      printf '%s\n' "$err" >&2
      return 1
    fi
    echo "    BSR is rate limiting or briefly unavailable; retry $attempt/$((attempts - 1)) in 45s" >&2
    sleep 45
  done
}

echo "==> buf generate (agentic closure: agentic + common -> gen/go, gen-ts-agentic, gen-py-agentic)"
run_buf --template buf.gen.agentic.yaml "${AGENTIC_CLOSURE_PATHS[@]}" || exit 1

# protoc's Python output does not emit __init__.py anywhere, which is what we
# want: o11y_one/ and its subpackages stay PEP 420 implicit namespace packages,
# so the generated distribution (o11y-one-api) and the hand-written one
# (o11y-one, which owns o11y_one.sdk) can both contribute to o11y_one.*.
# Assert that no stray __init__.py appeared under the shared namespace root.
for py_ns in packages/gen-py-agentic/src/o11y_one; do
  if [[ -f "$py_ns/__init__.py" ]]; then
    echo "$py_ns/__init__.py exists — that would turn the" >&2
    echo "shared o11y_one namespace into a regular package and shadow o11y_one.sdk." >&2
    exit 1
  fi
done

# A plugin that silently produced nothing is a failure, not a clean run.
for out in "${OUTPUTS[@]}"; do
  if [[ ! -d "$out" ]] || [[ -z "$(find "$out" -type f -print -quit)" ]]; then
    echo "$out is empty after generation — a plugin produced no output" >&2
    exit 1
  fi
done

echo "==> generated:"
for out in "${OUTPUTS[@]}"; do
  printf '    %-28s %s files\n' "$out" "$(find "$out" -type f | wc -l | tr -d ' ')"
done
