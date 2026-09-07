// Smoke test for the hand-written TS SDK.
//
// It makes exactly one call, against a stub fetch — no network. What it proves
// is the only thing the wrapper can get wrong on its own: that the credential
// and scoping headers actually land on the wire, and that a server error maps
// onto the right disposition.
import { strict as assert } from "node:assert";
import { test } from "node:test";

import { AgenticEvaluationService } from "@o11y-one/api-agentic/o11y_one/agentic/v1/evaluation_pb";

import { O11yClient, assertLooksLikeMachineCredential, classify } from "../dist/index.js";

const CREDENTIAL = "o11y_mach.AAAAAAAAAAAAAAAAAAAAAA.BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBA";

test("credential validation rejects the common mistakes locally", () => {
  assert.throws(() => assertLooksLikeMachineCredential(""), /empty/);
  assert.throws(() => assertLooksLikeMachineCredential("eyJhbGciOi.JWT.looking"), /o11y_mach/);
  assert.throws(() => assertLooksLikeMachineCredential("o11y_mach.onlytwo"), /malformed/);
  // Quoted values survive, matching the server's normalize_api_token_input.
  assert.equal(assertLooksLikeMachineCredential(`"${CREDENTIAL}"`), CREDENTIAL);
});

test("the transport stamps credential and scoping headers on every request", async () => {
  let seen = null;
  const stubFetch = async (input, init) => {
    seen = new Headers(init?.headers ?? (input instanceof Request ? input.headers : undefined));
    // Answer with a Connect error so the call terminates deterministically
    // without us having to hand-encode a valid binary response body.
    return new Response(JSON.stringify({ code: "permission_denied", message: "missing scope eval:read" }), {
      status: 403,
      headers: { "content-type": "application/json" },
    });
  };

  const o11y = new O11yClient({
    baseUrl: "https://api.invalid",
    credential: CREDENTIAL,
    orgId: "org_123",
    tenantId: "tenant_456",
    fetch: stubFetch,
  });

  const svc = o11y.service(AgenticEvaluationService);
  let thrown;
  try {
    await svc.listEvaluationDefinitions({});
  } catch (err) {
    thrown = err;
  }

  assert.ok(seen, "fetch was never called");
  assert.equal(seen.get("x-o11y-key"), CREDENTIAL);
  assert.equal(seen.get("x-o11y-org-id"), "org_123");
  assert.equal(seen.get("x-o11y-tenant-id"), "tenant_456");

  const classified = classify(thrown);
  assert.equal(classified.disposition, "insufficient-scope");
  assert.equal(classified.missingScope, "eval:read");
  assert.equal(classified.retryable, false);
});
