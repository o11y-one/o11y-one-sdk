# Security policy

## Reporting a vulnerability

Do not open a public issue for a security problem.

Report it through GitHub's private channel: **Security > Report a vulnerability**
on this repository (`https://github.com/o11y-one/o11y-one-sdk/security/advisories/new`).
Only the maintainers can read what you submit there.

Include the package and version (`@o11y-one/sdk`, `@o11y-one/api-agentic`,
`o11y-one`, `o11y-one-api-agentic`, the Go module, or an `o11y-eval` binary), how
to reproduce, and what an attacker gains.

## What to expect

- Acknowledgement within 3 business days.
- A fix or a stated mitigation before any public disclosure, coordinated with you.
- Credit in the advisory unless you prefer none.

## Scope

This repository publishes client code that runs in your environment. A finding
about the hosted O11y One service itself belongs to the same channel; we route it.

## Verifying what you install

Every release is published from `.github/workflows/publish.yml` on a `v*` tag
with no long-lived credentials. The README's "Supply-chain posture" section
documents how to verify npm provenance and the cosign signature on `o11y-eval`.
