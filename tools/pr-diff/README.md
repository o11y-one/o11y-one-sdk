# `pr-diff`: the eval diff as a pull-request comment

A composite GitHub Action that renders an O11y One eval diff document (the
JSON `o11y-eval diff --out` writes) as a GitHub-flavored-markdown comment and
upserts it onto the pull request. It recomputes nothing: every number and the
verdict come from the document. It runs `go run .` from this directory, so the
source a workflow executes is the source you can read here; there is no
prebuilt binary to trust.

## Usage

```yaml
permissions:
  contents: read
  pull-requests: write   # the only write the action needs

steps:
  - uses: actions/checkout@v4
  - run: o11y-eval diff --run "$RUN_ID" --candidate challenger --out eval-diff.json
  - uses: o11y-one/o11y-one-sdk/tools/pr-diff@v0.1.3
    with:
      diff-document-path: eval-diff.json
```

Pin the tag, not `main`. Every release tag of this repository carries the
action at the same version as the SDK packages.

| input | default | meaning |
|---|---|---|
| `diff-document-path` | required | Path to the diff document. Relative paths are resolved against the caller's checkout (`GITHUB_WORKSPACE`). On `v0.1.0` pass an absolute path, `${{ github.workspace }}/eval-diff.json`; later tags accept relative paths. |
| `github-token` | `${{ github.token }}` | Needs `pull-requests: write` (or `issues: write`). |
| `pr-number` | the triggering pull request | Set it when the workflow is not a `pull_request` event. |
| `exit-with-verdict` | `"false"` | `"true"` fails the step with the document's own exit code after posting, so a regression blocks the job. |

Output `comment-body` is the rendered markdown, for later steps.

## Behaviour

- One comment per pull request: a rerun updates the existing comment instead of
  adding another.
- The document's `verdict` is rendered as is; `improvement`, `regression` and
  `indeterminate` are the only outcomes it carries. A runner that failed before
  producing a document is rendered as an infrastructure failure by the
  `--infra-failure` path of the CLI, never as a verdict.
- With `exit-with-verdict: "false"` the step exits 0 once the comment is
  posted; gate on the document in a separate step if you want the job to fail.

## Running it by hand

```sh
go run . render  --input eval-diff.json --output comment.md
go run . comment --input eval-diff.json --owner ORG --repo REPO --pr 123
```

`render` is pure and needs no network. `comment` reads `GITHUB_TOKEN`.
