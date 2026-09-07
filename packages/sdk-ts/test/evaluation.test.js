// Unit tests for the agentic-evaluation journey surface.
//
// No network and no server: the wrapper is exercised against a duck-typed stub
// standing in for the generated service client. What these prove is the only
// thing the wrapper owns — that inputs are validated before a call, that a
// refusal (on a 200 or in Status.details) becomes a typed Result rather than a
// throw, and that the one-time credential cannot be logged by accident.
import { strict as assert } from "node:assert";
import { test } from "node:test";
import { inspect } from "node:util";

import { Code, ConnectError } from "@connectrpc/connect";
import {
  EvaluationLaunchRejectionV1Schema,
  PlatformAnnotationRejectionV1Schema,
  PlatformAnnotationKindV1,
} from "@o11y-one/api-agentic/o11y_one/agentic/v1/evaluation_pb";

import {
  AgenticEvaluationClient,
  OneTimeCredential,
  ValidationError,
} from "../dist/index.js";

// A stub O11yClient: AgenticEvaluationClient only calls `client.service(desc)`.
function clientWith(raw) {
  return new AgenticEvaluationClient({ service: () => raw });
}

test("whoami lifts machine scopes to canonical strings and answers hasScope", async () => {
  const evalc = clientWith({
    getCallerPrincipal: async () => ({
      tenantId: "t1",
      orgId: "o1",
      machinePrincipal: { machinePrincipalId: "mp1", scopes: [1, 3] }, // EVAL_READ, DATASET_WRITE
      credential: { credentialId: "cred1" },
    }),
  });
  const me = await evalc.whoami();
  assert.deepEqual(me.scopes, ["eval:read", "dataset:write"]);
  assert.equal(me.hasScope("eval:read"), true);
  assert.equal(me.hasScope("run:execute"), false);
  assert.equal(me.machinePrincipalId, "mp1");
  assert.equal(me.credentialId, "cred1");
});

test("createMachinePrincipal validates the display name and maps scopes to the wire enum", async () => {
  let seen;
  const evalc = clientWith({
    createMachinePrincipal: async (req) => {
      seen = req;
      return { principal: { machinePrincipalId: "x" } };
    },
  });
  await assert.rejects(() => evalc.createMachinePrincipal({ displayName: "  ", scopes: [] }), ValidationError);
  const p = await evalc.createMachinePrincipal({ displayName: "ci", scopes: ["run:execute", "lease:submit"] });
  assert.equal(p.machinePrincipalId, "x");
  assert.deepEqual(seen.scopes, [2, 4]); // RUN_EXECUTE, LEASE_SUBMIT
});

test("createMachineCredential wraps the plaintext in a non-logging OneTimeCredential", async () => {
  const PLAINTEXT = "o11y_mach.SELECTORSELECTOR.SECRETSECRETSECRETSECRETSECRET";
  const evalc = clientWith({
    createMachineCredential: async () => ({
      credential: { credentialId: "cred_9" },
      plaintextTokenOnce: PLAINTEXT,
    }),
  });
  const { token } = await evalc.createMachineCredential({ machinePrincipalId: "mp1" });
  assert.ok(token instanceof OneTimeCredential);
  assert.equal(token.reveal(), PLAINTEXT);
  assert.equal(token.credentialId, "cred_9");
  // The plaintext must never appear through any accidental-logging path.
  assert.equal(String(token).includes(PLAINTEXT), false);
  assert.equal(JSON.stringify(token).includes(PLAINTEXT), false);
  assert.equal(inspect(token).includes(PLAINTEXT), false);
  assert.equal(`${token}`.includes("redacted"), true);

  await assert.rejects(() => evalc.createMachineCredential({ machinePrincipalId: "" }), ValidationError);
});

test("launchRun folds an in-detail rejection into err(), and validates its inputs", async () => {
  const rejecting = clientWith({
    createEvaluationRun: async () => {
      throw new ConnectError("preview moved", Code.FailedPrecondition, undefined, [
        {
          desc: EvaluationLaunchRejectionV1Schema,
          value: { kind: 3, expectedDigest: "aaa", observedDigest: "bbb", recovery: 2, detail: "revision moved" },
        },
      ]);
    },
  });
  const r = await rejecting.launchRun({ definitionId: "d1", idempotencyKey: "k1", previewToken: "tok" });
  assert.equal(r.ok, false);
  assert.equal(r.refusal.type, "launch-rejection");
  assert.equal(r.refusal.reason, "DEFINITION_REVISION_MOVED");
  assert.equal(r.refusal.recovery, "RE_PREVIEW");

  // A missing idempotency key never reaches the wire.
  await assert.rejects(
    () => rejecting.launchRun({ definitionId: "d1", idempotencyKey: "", previewToken: "tok" }),
    ValidationError,
  );

  // A non-detail transport error still throws.
  const throwing = clientWith({
    createEvaluationRun: async () => {
      throw new ConnectError("boom", Code.Unavailable);
    },
  });
  await assert.rejects(
    () => throwing.launchRun({ definitionId: "d1", idempotencyKey: "k1", previewToken: "tok" }),
    ConnectError,
  );
});

test("launchRun returns ok with the run on acceptance", async () => {
  const evalc = clientWith({
    createEvaluationRun: async () => ({ run: { evaluationRunId: "run_1" }, idempotentReplay: false }),
  });
  const r = await evalc.launchRun({ definitionId: "d1", idempotencyKey: "k1", previewToken: "tok" });
  assert.equal(r.ok, true);
  assert.equal(r.value.run.evaluationRunId, "run_1");
});

test("leaseCases maps an on-200 refusal to err and distinguishes exhaustion from no-work", async () => {
  const refused = clientWith({
    leaseEvaluationCases: async () => ({ refusal: { kind: 7, message: "no scope", missingScope: "lease:submit" } }),
  });
  const r = await refused.leaseCases({ evaluationRunId: "run_1", candidateKey: "c", runtimeKey: "rt" });
  assert.equal(r.ok, false);
  assert.equal(r.refusal.reason, "SCOPE_MISSING");
  assert.equal(r.refusal.missingScope, "lease:submit");

  const done = clientWith({
    leaseEvaluationCases: async () => ({ lease: undefined, cases: [], remainingUnleasedCaseCount: 0 }),
  });
  const d = await done.leaseCases({ evaluationRunId: "run_1", candidateKey: "c", runtimeKey: "rt" });
  assert.equal(d.ok, true);
  assert.equal(d.value.exhausted, true);

  const heldElsewhere = clientWith({
    leaseEvaluationCases: async () => ({ lease: undefined, cases: [], remainingUnleasedCaseCount: 5 }),
  });
  const h = await heldElsewhere.leaseCases({ evaluationRunId: "run_1", candidateKey: "c", runtimeKey: "rt" });
  assert.equal(h.value.exhausted, false);

  await assert.rejects(
    () => refused.leaseCases({ evaluationRunId: "", candidateKey: "c", runtimeKey: "rt" }),
    ValidationError,
  );
});

test("submitCaseOutputs partitions a batch into accepted / duplicate / rejected", async () => {
  const evalc = clientWith({
    submitEvaluationCaseOutputs: async () => ({
      acks: [
        { cohortKey: "a", candidateKey: "x", caseRevisionId: "r1", trial: 0, kind: 1, observedState: 2 },
        { cohortKey: "a", candidateKey: "x", caseRevisionId: "r2", trial: 0, kind: 2, observedState: 3 },
        { cohortKey: "a", candidateKey: "x", caseRevisionId: "r3", trial: 0, kind: 3, observedState: 9 },
      ],
      acceptedCount: 1,
      alreadySubmittedCount: 1,
      rejectedCount: 1,
      remainingLeasedCaseCount: 4,
    }),
  });
  const outcome = await evalc.submitCaseOutputs({
    evaluationRunId: "run_1",
    leaseId: "l1",
    leaseToken: "tok",
    outputs: [{ cohortKey: "a", candidateKey: "x", caseRevisionId: "r1", trial: 0 }],
    idempotencyKey: "k1",
  });
  assert.equal(outcome.accepted.length, 1);
  assert.equal(outcome.alreadySubmitted.length, 1);
  assert.equal(outcome.rejected.length, 1);
  assert.equal(outcome.accepted[0].kind, "ACCEPTED");
  assert.equal(outcome.rejected[0].kind, "REJECTED");
  assert.equal(outcome.refusal, undefined);

  // Empty batch and missing idempotency key are refused locally.
  await assert.rejects(
    () =>
      evalc.submitCaseOutputs({ evaluationRunId: "run_1", leaseId: "l1", leaseToken: "tok", outputs: [], idempotencyKey: "k1" }),
    ValidationError,
  );
});

test("createDatasetVersion enforces exactly-one ingest source", async () => {
  const evalc = clientWith({ createEvaluationDatasetVersion: async () => ({ version: { id: "v1" } }) });
  await assert.rejects(
    () => evalc.createDatasetVersion({ idempotencyKey: "k1" }),
    (e) => e instanceof ValidationError && /exactly one/.test(e.message),
  );
  await assert.rejects(
    () => evalc.createDatasetVersion({ idempotencyKey: "k1", jsonl: new Uint8Array([1]), draftId: "d1" }),
    ValidationError,
  );
  const okr = await evalc.createDatasetVersion({ idempotencyKey: "k1", jsonl: new Uint8Array([1]) });
  assert.equal(okr.ok, true);
});

test("captureCase enforces exactly-one source and maps a capture refusal", async () => {
  const evalc = clientWith({ captureEvaluationCase: async () => ({ proposedCase: { id: "p1" } }) });
  await assert.rejects(
    () => evalc.captureCase({ datasetCollectionId: "dc1", idempotencyKey: "k1" }),
    ValidationError,
  );
  const okr = await evalc.captureCase({ datasetCollectionId: "dc1", idempotencyKey: "k1", span: { spanId: "s1" } });
  assert.equal(okr.ok, true);
});

test("recordAnnotation validates inputs and folds an in-detail rejection to err", async () => {
  const rejecting = clientWith({
    recordPlatformAnnotation: async () => {
      throw new ConnectError("too big", Code.InvalidArgument, undefined, [
        { desc: PlatformAnnotationRejectionV1Schema, value: { reason: 2, field: "title" } },
      ]);
    },
  });
  const r = await rejecting.recordAnnotation({
    kind: PlatformAnnotationKindV1.DEPLOYMENT,
    title: "deploy v2",
    idempotencyKey: "k1",
  });
  assert.equal(r.ok, false);
  assert.equal(r.refusal.reason, "TITLE_TOO_LARGE");
  assert.equal(r.refusal.field, "title");

  await assert.rejects(
    () => rejecting.recordAnnotation({ kind: PlatformAnnotationKindV1.DEPLOYMENT, title: "", idempotencyKey: "k1" }),
    ValidationError,
  );
  // UNSPECIFIED kind is refused locally.
  await assert.rejects(
    () => rejecting.recordAnnotation({ kind: 0, title: "x", idempotencyKey: "k1" }),
    ValidationError,
  );
});

test("listAnnotations surfaces a cursor-resync directive", async () => {
  const evalc = clientWith({
    listPlatformAnnotations: async () => ({ annotations: [], resync: { reason: 1 }, page: { nextPageToken: undefined, hasMore: false } }),
  });
  const res = await evalc.listAnnotations({ windowStart: new Date(0), windowEnd: new Date(1000) });
  assert.equal(res.resync.type, "cursor-resync");
  assert.equal(res.resync.reason, "SNAPSHOT_SUPERSEDED");
});
