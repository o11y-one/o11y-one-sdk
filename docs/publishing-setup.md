# Publishing setup: the one-time steps before the first tag

`publish.yml` publishes four packages and the `o11y-eval` binaries from a `v*`
tag with no long-lived credentials. That only works once the registries know
this repository. This document is the ordered list of one-time steps, checked
against the registries' current documentation on 2026-09-24. The README's
"Publishing" section describes the steady state; this is how to get there.

## Order of operations

1. Server side: the platform-token confinement in o11y-api (merged 2026-09-22)
   is deployed to production. Nothing here depends on it directly, but the
   Terraform provider's README does, and both repositories go public together.
2. This repository: the steps in "npm" and "PyPI" below. The npm bootstrap
   publish happens while the repository is still private.
3. Make the repository public ("Going public" below). npm provenance is
   generated only from public repositories, and the `release` environment's
   required reviewer can only be added on a public repository under the Team
   plan.
4. Tag `v0.1.0`. Approve the environment deployment when GitHub asks. Verify
   ("After the first release" below).

## npm

### Why there is a bootstrap publish

A trusted publisher is configured on the package's settings page on npmjs.com,
so the package has to exist before OIDC can be enabled for it
(npm/cli issue 8544 is the open request to lift this). The first version of
each package is therefore published once from a laptop with a short-lived
granular token; every later version comes from `publish.yml` with no token at
all.

### Steps

1. **Account and organisation.** Sign in to npmjs.com with 2FA enabled on the
   account. Create the organisation `o11y-one` (Add Organization, free plan).
   The `@o11y-one` scope belongs to that organisation.

2. **Bootstrap publish, version 0.0.0.** From a clean checkout of `main`:

   ```sh
   mise install && just install && just build
   just pack-check                       # the same tarball inspection CI runs
   npm login                             # 2-hour session token; 2FA prompt
   npm_config_provenance=false pnpm --filter @o11y-one/api-agentic publish --access public --no-git-checks
   npm_config_provenance=false pnpm --filter @o11y-one/sdk         publish --access public --no-git-checks
   npm logout
   ```

   Order matters: `@o11y-one/sdk` depends on `@o11y-one/api-agentic`.
   Provenance is switched off for this one publish because it cannot be
   attested from a laptop; `publishConfig.provenance` in each `package.json`
   restores it for every workflow publish. npm prompts for the OTP on each
   publish. No granular token is created at any point.

3. **Trusted publisher, once per package.** npmjs.com > Packages >
   `@o11y-one/api-agentic` > Settings > Trusted Publisher > Select your
   publisher > GitHub Actions:

   | field | value |
   |---|---|
   | Organization or user | `o11y-one` |
   | Repository | `o11y-one-sdk` |
   | Workflow filename | `publish.yml` |
   | Environment name | `release` |

   Leave **Allowed actions** at its default, `npm stage publish`; the
   workflow stages, it never publishes directly. Repeat for `@o11y-one/sdk`.
   A configuration cannot be edited afterwards, only deleted and recreated.
   The `repository.url` in each `package.json` already matches
   `https://github.com/o11y-one/o11y-one-sdk`, which npm requires for
   provenance.

4. **Close the token door.** On each package's Settings page, under Publishing
   access, choose **Require two-factor authentication and disallow tokens**.
   From this point the only way to publish is the workflow.

5. **Mark the bootstrap version.** After `v0.1.0` is out:

   ```sh
   npm deprecate @o11y-one/api-agentic@0.0.0 "bootstrap release; use 0.1.0 or later"
   npm deprecate @o11y-one/sdk@0.0.0         "bootstrap release; use 0.1.0 or later"
   ```

### Approving a release

The workflow packs both packages with pnpm (which rewrites the workspace
dependency to the real version) and runs `npm stage publish --provenance` on
the tarballs. Nothing is installable until you approve, from any machine,
signed in to npm with 2FA. The dependency goes first:

```sh
npm stage list @o11y-one/api-agentic     # shows the staged version and its stage id
npm stage approve <stage-id>             # prompts for the OTP
npm stage list @o11y-one/sdk
npm stage approve <stage-id>
```

`npm stage reject <stage-id>` discards a staged version; the same version
can then be staged again, which is how a failed run is retried without a new
tag. Approval can also be done on npmjs.com; an OIDC token from the workflow
can never approve, which is the point. Staging needs npm 11.15 or later; the
Node pinned in `mise.toml` ships 11.19.

## PyPI

PyPI supports trusted publishers for projects that do not exist yet ("pending
publishers"), so there is no bootstrap publish.

1. **Account.** Sign in to pypi.org with 2FA enabled. The account that adds the
   pending publisher becomes the project owner on first upload.

2. **Pending publisher, once per project.** Account sidebar > Publishing
   (`https://pypi.org/manage/account/publishing/`) > GitHub:

   | field | `o11y-one-api-agentic` | `o11y-one` |
   |---|---|---|
   | PyPI project name | `o11y-one-api-agentic` | `o11y-one` |
   | Owner | `o11y-one` | `o11y-one` |
   | Repository name | `o11y-one-sdk` | `o11y-one-sdk` |
   | Workflow name | `publish.yml` | `publish.yml` |
   | Environment name | `release` | `release` |

   The environment field is optional on PyPI's side and filled in here on
   purpose: without it any job in any workflow file of that name could publish.

3. Nothing else. The first `uv publish --trusted-publishing always` from the
   `publish-pypi` job creates both projects and converts the pending publishers
   into ordinary ones.

Known gap, stated in the README as well: `uv publish` uploads PEP 740
attestations if they exist next to the distributions but does not generate
them. Adding `astral-sh/attest-action` before the publish step closes it; it is
not a blocker for the first release.

## Go

Nothing to register, but one extra tag. `gen/go` is a module in a
subdirectory, and Go resolves a nested module's versions from tags prefixed
with its directory: `gen/go/v0.1.0`, not `v0.1.0`. The release tagging below
pushes both tags at the same commit; the `release tags` ruleset protects
both patterns. Once the module proxy has served a version, `sum.golang.org`
records it permanently, which is why the surface reduction in
`docs/proto-subsetting.md` had to land before the repository went public: a
module version cannot be unpublished.

## Repository protections

Configured on the GitHub repository, not in this tree. Verify with the commands
shown; re-apply if a listing comes back empty.

| protection | what it enforces | verify |
|---|---|---|
| Ruleset `main` (branch) | pull request required, the `check` job green, no force-push, no deletion | `gh api repos/o11y-one/o11y-one-sdk/rulesets --jq '.[].name'` |
| Ruleset `release tags` (tag, `v*`) | only repository Admin and Maintain roles can create a `v*` tag; nobody can move or delete one | same listing |
| Environment `release` | deployments only from `v*` tags; required reviewer added once public | `gh api repos/o11y-one/o11y-one-sdk/environments/release` |
| Code-security configuration `Public SDK repos` | Dependabot alerts and security updates, dependency graph, secret scanning with push protection, private vulnerability reporting; no paid features | `gh api repos/o11y-one/o11y-one-sdk/code-security-configuration` |
| `SECURITY.md` | reporters use GitHub's private advisory form | in this tree |
| `.github/dependabot.yml` | weekly grouped version updates with a 7-day cooldown, mirroring `minimumReleaseAge` | in this tree |

Secret scanning and push protection are free on public repositories only and
are not switched on automatically for organisation-owned repositories, so the
configuration is applied as part of going public. The full history, every ref,
was scanned with `gitleaks git --log-opts=--all` on 2026-09-24. The 56 hits are
all `generic-api-key` matches on protobuf enum names containing `KEY` in
generated code and on the fake `o11y_mach.AAAA.SECRET` fixture token in
`packages/sdk-py/tests/test_agentic.py`; none is a credential.

## Going public

1. Make the repository public: Settings > General > Danger Zone > Change
   visibility. Rulesets, the environment and the security configuration
   survive the change.

2. Add the required reviewer to the `release` environment:

   ```sh
   gh api -X PUT repos/o11y-one/o11y-one-sdk/environments/release --input - <<'EOF'
   {"reviewers":[{"type":"User","id":10788442}],"prevent_self_review":false,
    "deployment_branch_policy":{"protected_branches":false,"custom_branch_policies":true}}
   EOF
   ```

   `prevent_self_review` stays `false` while there is one maintainer.

3. Confirm the free security features came on:

   ```sh
   gh api repos/o11y-one/o11y-one-sdk --jq '.security_and_analysis | {secret_scanning, secret_scanning_push_protection}'
   gh api repos/o11y-one/o11y-one-sdk/private-vulnerability-reporting
   ```

   If they read `disabled`, the repository is still attached to the
   organisation's enforced "No paid GitHub security" configuration. Create the
   free-features configuration once and attach both publishing repositories
   (needs `gh auth refresh -h github.com -s admin:org`):

   ```sh
   ID=$(gh api -X POST orgs/o11y-one/code-security/configurations --input - <<'EOF' --jq .id
   {"name":"Public SDK repos",
    "description":"Free GitHub security features for the public SDK and Terraform provider repositories; paid features stay off.",
    "advanced_security":"disabled","dependency_graph":"enabled",
    "dependabot_alerts":"enabled","dependabot_security_updates":"enabled",
    "secret_scanning":"enabled","secret_scanning_push_protection":"enabled",
    "private_vulnerability_reporting":"enabled","enforcement":"unenforced"}
   EOF
   )
   gh api -X POST orgs/o11y-one/code-security/configurations/$ID/attach --input - <<EOF
   {"scope":"selected","selected_repository_ids":[$(gh api repos/o11y-one/o11y-one-sdk --jq .id),$(gh api repos/o11y-one/terraform-provider-o11y --jq .id)]}
   EOF
   ```

4. Tag from a maintainer's checkout of an up-to-date `main` (the tag ruleset
   refuses anyone else):

   ```sh
   git switch main && git pull --ff-only
   git tag -a v0.1.0 -m "v0.1.0" && git push origin v0.1.0
   git tag -a gen/go/v0.1.0 -m "gen/go v0.1.0" v0.1.0^{commit} && git push origin gen/go/v0.1.0
   ```

   The second tag is what `go get github.com/o11y-one/o11y-one-sdk/gen/go@v0.1.0`
   resolves; without it the proxy answers "unknown revision gen/go/v0.1.0".
   It does not start a workflow run (the publish trigger is `v*`).

   Approve the `release` environment deployment in the Actions run when asked;
   `verify` must be green before any publish job starts. When the run is
   green, approve the two staged npm versions ("Approving a release" above).

## After the first release

Each check is run from an empty directory, not from this checkout.

```sh
# npm (after both stage approvals): provenance attested, no maps, sources or tests in the tarball
npm install @o11y-one/sdk@0.1.0 && npm audit signatures
find node_modules/@o11y-one \( -name '*.map' -o -name '*.test.*' -o -path '*/test/*' \)   # expect nothing

# PyPI: sources only
python -m venv v && . v/bin/activate && pip download --no-deps o11y-one==0.1.0 o11y-one-api-agentic==0.1.0
unzip -l o11y_one-0.1.0-*.whl | grep -Ei 'tests?/|fixtures|\.env'   # expect nothing

# o11y-eval: keyless signature (README "Verifying an o11y-eval binary")
cosign verify-blob o11y-eval-linux-amd64 --bundle o11y-eval-linux-amd64.cosign.bundle \
  --certificate-identity-regexp '^https://github.com/o11y-one/o11y-one-sdk/\.github/workflows/publish\.yml@' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com

# Go: the module resolves through the proxy and the checksum database
GOFLAGS=-mod=mod go list -m github.com/o11y-one/o11y-one-sdk/gen/go@v0.1.0

# Action: from a scratch repository, a workflow with
#   uses: o11y-one/o11y-one-sdk/tools/pr-diff@v0.1.0
#   permissions: { pull-requests: write }
```
