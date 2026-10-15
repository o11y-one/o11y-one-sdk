#!/usr/bin/env bash
#
# internal-text-check.sh — fail if a file in this repository carries internal
# engineering notes: work-stream, iteration and phase labels, plan and
# notes-file references, or server source paths.
#
#   ./tools/internal-text-check.sh [path]
#
# Everything here is public, and the vendored protos are published as API
# documentation in every generated package. Their comments, and the SDKs' own,
# describe the contract a client relies on; how and where the server was built
# does not belong in them.
#
# Scans the files git knows about under [path] (default: the whole repository):
# tracked files, plus untracked files that are not ignored, so a proto sync that
# has just rewritten proto/ is scanned before anything is committed. Outside a
# git checkout it scans every file under [path]. Lockfiles and binaries are
# skipped. Prints each hit as file:line:text and exits 1 if there is any.
#
# The patterns are precise on purpose, so there is no allowlist. Upstream issue
# refs (ABC-123, #123) are accepted text and deliberately not matched; neither
# are the trace timeline's "lanes" or latency percentiles (p50, p95, p99).
set -euo pipefail

patterns=(
  # Work-stream labels: "lane" followed by a capital letter or a number, as in
  # "Lane X" or "lane 12B". The timeline's "lane" alone is customer vocabulary.
  '\b[Ll]ane ([A-Z][0-9]?|[0-9]+[A-Z]?)\b'
  # The same labels and handoff ids written alone: "12B", "w12a", "W12A-3".
  '\b[0-9]{2}[A-D]\b'
  '\b[Ww][0-9]{2}[A-Za-z]\b'
  # Iteration numbers and planning vocabulary.
  '\b[Ww]ave [0-9]+'
  '\b[Rr]uling\b'
  '\b[Dd]ocket\b'
  'RECORDED AMENDMENT'
  '\bNN[0-9]+\b'
  'PLAN:[0-9]+'
  '§'
  # Phase labels: P1, P2.5, P1.8d. Upper case only, so p50/p95/p99 never match.
  '\bP[0-9](\.[0-9]+[a-z]?)?\b'
  # Server source paths: src/foo.rs, foo.rs:12.
  '\b[A-Za-z0-9_/]+\.rs(:[0-9]+)?\b'
  # Private pull requests, and plan, spec and notes files.
  'o11y-api #[0-9]+'
  'docs/specs/'
  'scratchpad/'
  '\b[A-Za-z0-9_]+-notes\.md\b'
)

skip='(^|/)(pnpm-lock\.yaml|uv\.lock|go\.sum|internal-text-check\.sh)$'

root="${1:-.}"
args=()
for p in "${patterns[@]}"; do args+=(-e "$p"); done

if git -C "$root" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  list() { git ls-files -z --cached --others --exclude-standard -- "$root"; }
else
  list() { find "$root" -type f -print0; }
fi

# -I skips binaries; -s quiets a tracked file the working tree no longer has.
hits="$(list | grep -zvE "$skip" | xargs -0 grep -HnIsE "${args[@]}" -- || true)"

if [[ -n "$hits" ]]; then
  printf '%s\n' "$hits"
  echo "internal-text-check: $(printf '%s\n' "$hits" | wc -l | tr -d ' ') line(s) carry internal engineering notes; reword them for a public reader" >&2
  exit 1
fi
echo "internal-text-check: no internal engineering notes in ${root}"
