# `@o11y-one/sdk`

The TypeScript client for the O11y One API. A thin, hand-written layer over the
generated [`@o11y-one/api-agentic`](../gen-ts-agentic) package.

## Install

```sh
pnpm add @o11y-one/sdk
```

That is the only package to install. The generated service descriptors,
message schemas and enums are re-exported from `@o11y-one/sdk/api`, so you
never import `@o11y-one/api-agentic` directly.

## Use

```ts
import { O11yClient, classify } from "@o11y-one/sdk";
import { AgenticEvaluationService } from "@o11y-one/sdk/api";

const o11y = new O11yClient({
  baseUrl: "https://grpc.o11y.one",
  credential: process.env.O11Y_API_KEY, // o11y_mach.<selector>.<secret>
  orgId: process.env.O11Y_ORG_ID,
});

const evals = o11y.service(AgenticEvaluationService);

try {
  const defs = await evals.listEvaluationDefinitions({});
} catch (err) {
  const failure = classify(err);
  if (failure.disposition === "insufficient-scope") {
    throw new Error(`credential is missing scope ${failure.missingScope}`);
  }
  throw err;
}
```

## What is here, and what deliberately is not

Three modules and nothing else:

| module | responsibility |
|---|---|
| `client.ts` | transport construction, credential and scoping header injection |
| `auth.ts`   | the credential wire format and local structural validation |
| `errors.ts` | the failure taxonomy: reauthenticate / insufficient-scope / version-skew / retry / unclassified |

Service methods are **not** wrapped. connect-es turns any generated descriptor
into a fully typed client; a hand-written facade over every service would be a
second API surface to keep in sync with the proto, and it would rot the first
time a field is added upstream.

## The distinction this package exists to preserve

`UNAUTHENTICATED` and `PERMISSION_DENIED` are different problems:

* **`UNAUTHENTICATED`** — the credential is absent, malformed, unknown, expired,
  or revoked. Re-auth. Retrying cannot change the answer.
* **`PERMISSION_DENIED`** — the credential is fine; it lacks a scope (the server
  names which one) or it was presented to a non-machine surface.

`classify()` keeps them apart, along with `UNAVAILABLE` (auth backend down —
retry with backoff) and `INVALID_ARGUMENT` (SDK/server version skew). Collapsing
these into a single "auth error" is the failure mode this module exists to
prevent.

## Credentials

A machine credential is `o11y_mach.<selector>.<secret>`, presented in the
`x-o11y-key` header. It is returned exactly once at creation (no read-back RPC,
no recovery path), rotated create-then-revoke rather than atomically, revoked
effective on the next request, and expires at +365 days by default with a
three-year cap.

Never send it as `authorization: Bearer` — that path carries the browser session
JWT and a machine credential presented there is rejected.

## Runtime support

The default transport is gRPC-web via `@connectrpc/connect-web`, which needs
only a spec-compatible `fetch`. That covers browsers, Node 26, Deno, Bun and
Cloudflare Workers. `@connectrpc/connect-node` is a dependency for callers who
want the Node-specific HTTP/2 transport and construct it themselves; pass the
resulting transport's options through `ClientOptions` or build your own
transport and install `credentialInterceptor()` on it. The API serves gRPC and
gRPC-web only, so a transport you build must speak one of those, not the
Connect protocol.
