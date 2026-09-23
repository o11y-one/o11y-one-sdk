#!/usr/bin/env bash
#
# sync-proto.sh — re-vendor the .proto source of truth from o11y-api and regenerate.
#
#   ./tools/sync-proto.sh <path-to-o11y-api-checkout> [--allow-dirty-pin]
#
# The proto files under proto/ in THIS repo are a read-only snapshot. They are
# never hand-edited here; o11y-api is the source of truth. This script is the
# only sanctioned way to move the snapshot forward, and it is deliberately
# manual — there is no automatic sync, no submodule, no CI bot.
#
# What it does, in order:
#   1. Verifies the given o11y-api checkout is at the commit named in PROTO_PIN.
#   2. Copies <checkout>/proto/o11y_one/ into ./proto/o11y_one/.
#   3. Applies the ONE deterministic transform this repo makes (see below).
#   4. Verifies every remaining import resolves locally or to a well-known type.
#   5. Runs `buf lint` and `buf generate`.
#
# ---------------------------------------------------------------------------
# The import re-rooting transform  (the only edit made to vendored bytes)
# ---------------------------------------------------------------------------
# In o11y-api the buf module root is proto/o11y_one, so imports inside the tree
# are written WITHOUT the o11y_one prefix:
#
#     import "common/v1/common.proto";        // file path: common/v1/common.proto
#     package o11y_one.common.v1;
#
# That is fine inside o11y-api, but it makes the generated file paths — and
# therefore the Python top-level package names — `common/`, `billing/`, `auth/`
# and so on. A published PyPI distribution cannot squat those names on sys.path.
#
# So this repo roots the buf module at proto/ instead, and rewrites each
# intra-tree import to carry the o11y_one/ prefix that the file already lives
# under on disk:
#
#     import "o11y_one/common/v1/common.proto";
#
# Consequences, all intended:
#   * Python top-level package becomes `o11y_one` — a PEP 420 namespace package
#     shared with the hand-written SDK (o11y_one.sdk).
#   * Go and TS paths gain the same prefix; managed mode maps Go onto the module
#     path regardless.
#   * `buf lint`'s STANDARD PACKAGE_DIRECTORY_MATCH rule now actually passes,
#     because o11y_one/common/v1/common.proto matches package o11y_one.common.v1.
#   * NOTHING on the wire changes: RPC full names come from the proto `package`
#     statement, which is untouched. Only descriptor file names move.
#
# The transform is deterministic, so re-running this script at the same pin
# produces a byte-identical tree — which is exactly what CI's gen-check asserts.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

allow_dirty_pin=0
src=""
for arg in "$@"; do
  case "$arg" in
    --allow-dirty-pin) allow_dirty_pin=1 ;;
    -*) echo "unknown flag: $arg" >&2; exit 2 ;;
    *) src="$arg" ;;
  esac
done

if [[ -z "$src" ]]; then
  echo "usage: tools/sync-proto.sh <path-to-o11y-api-checkout> [--allow-dirty-pin]" >&2
  exit 2
fi

src="$(cd "$src" && pwd)"
if [[ ! -d "$src/proto/o11y_one" ]]; then
  echo "not an o11y-api checkout (no proto/o11y_one): $src" >&2
  exit 2
fi

# --- 1. pin check ----------------------------------------------------------
pin="$(grep -v '^#' PROTO_PIN | tr -d '[:space:]')"
head_sha="$(git -C "$src" rev-parse --short=8 HEAD)"
if [[ "$head_sha" != "$pin"* && "$pin" != "$head_sha"* ]]; then
  if [[ "$allow_dirty_pin" -eq 1 ]]; then
    echo "WARNING: $src is at $head_sha, PROTO_PIN says $pin — continuing (--allow-dirty-pin)." >&2
    echo "         Update PROTO_PIN to $head_sha in the SAME commit as the regenerated code." >&2
  else
    echo "PROTO_PIN mismatch: PROTO_PIN=$pin but $src is at $head_sha." >&2
    echo "Either check out $pin there, or pass --allow-dirty-pin and update PROTO_PIN." >&2
    exit 1
  fi
fi

# --- 2. vendor -------------------------------------------------------------
#
# Extracted with `git archive` from the COMMIT, never copied from the working
# tree. o11y-api is worked on continuously and its tree is routinely dirty — a
# lane mid-edit on evaluation.proto is normal, not exceptional. Copying the
# working tree would vendor somebody's half-finished change under a PROTO_PIN
# that claims it came from a specific commit, and the resulting snapshot would
# be unreproducible: nobody could ever regenerate it.
echo "==> vendoring $src @ $pin -> proto/o11y_one"
if [[ -n "$(git -C "$src" status --porcelain -- proto/o11y_one)" ]]; then
  echo "    note: $src has uncommitted changes under proto/o11y_one." >&2
  echo "    They are IGNORED — this vendors the committed tree at $pin." >&2
fi
rm -rf proto/o11y_one
mkdir -p proto
# Only the agentic closure is vendored. The rest of the o11y-api contract never
# enters this repository, so going public cannot expose it.
git -C "$src" archive --format=tar "$pin" proto/o11y_one/agentic proto/o11y_one/common | tar -xf - -C proto --strip-components=1
find proto/o11y_one -type f ! -name '*.proto' -delete
find proto/o11y_one -type d -empty -delete

# --- 3. re-root imports ----------------------------------------------------
echo "==> re-rooting intra-tree imports under o11y_one/"
while IFS= read -r f; do
  # Any import that is not a google/ well-known type is an intra-tree import
  # written relative to the o11y_one module root upstream; prefix it.
  perl -pi -e 's{^import "(?!google/|o11y_one/)([^"]+)";}{import "o11y_one/$1";}' "$f"
done < <(find proto/o11y_one -name '*.proto')

# --- 4. import audit -------------------------------------------------------
echo "==> auditing imports"
bad=0
while IFS= read -r imp; do
  case "$imp" in
    google/protobuf/*) ;;                      # well-known, carried by buf itself
    o11y_one/*)
      [[ -f "proto/$imp" ]] || { echo "  MISSING local import: $imp" >&2; bad=1; }
      ;;
    *)
      echo "  UNRESOLVED import: $imp" >&2
      echo "  This is not a well-known type and not in the vendored tree." >&2
      echo "  Add the owning module to buf.yaml deps: and run 'buf dep update'." >&2
      bad=1
      ;;
  esac
done < <(grep -rho '^import "[^"]*"' proto/o11y_one | sed 's/^import "//; s/"$//' | sort -u)
[[ "$bad" -eq 0 ]] || { echo "import audit failed" >&2; exit 1; }

# --- 5. build + generate ---------------------------------------------------
# `buf build`, not `buf lint`: see the comment in buf.yaml. Style belongs to
# o11y-api; all this repo owns is "the snapshot compiles".
echo "==> buf build"
buf build -o /dev/null
echo "==> buf generate"
exec "$repo_root/tools/generate.sh"
