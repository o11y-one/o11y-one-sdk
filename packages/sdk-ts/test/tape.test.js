// Record and replay on the external lease plane, against a duck-typed stub of
// the generated service client. The stub keeps each trajectory's next step the
// way the server does, so a test can read what was stored and in what chunks.
import { strict as assert } from "node:assert";
import { test } from "node:test";

import { Code, ConnectError } from "@connectrpc/connect";
import { ExternalLeaseRefusalV1Schema } from "@o11y-one/api-agentic/o11y_one/agentic/v1/evaluation_pb";

import {
  AgenticEvaluationClient,
  CaseRecordingRejectedError,
  LeaseRefusedError,
  RecordingUnavailableError,
  ReplayDivergedError,
  ValidationError,
} from "../dist/index.js";

const MARGIN = 64 << 10;
const LEASE = { leaseId: "l1", leaseToken: "t1" };
const CASE_A = { cohortKey: "c", candidateKey: "k", caseRevisionId: "r1", trial: 0, attemptGeneration: 0 };
const CASE_B = { ...CASE_A, caseRevisionId: "r2" };
const SECRET = "sk-canary-0000";

function posture(overrides = {}) {
  const limits = {
    max_record_request_bytes: MARGIN + 1000,
    max_call_bytes: 600,
    max_chunks_per_request: 50,
    max_calls_per_request: 65536,
    max_tool_name_bytes: 128,
    ...overrides,
  };
  return {
    capabilityKey: "sdk_record_replay",
    state: 1, // AVAILABLE
    limits: Object.entries(limits).map(([limitKey, v]) => ({ limitKey, limitValue: BigInt(v) })),
  };
}

function stubServer(raw = {}, postures = [posture()]) {
  const requests = [];
  const next = new Map();
  const server = {
    requests,
    getAgenticEvaluationCapabilities: async () => ({ capabilities: { postures } }),
    recordEvaluationCaseSteps: async (req) => {
      requests.push(structuredClone(req));
      return {
        acks: req.chunks.map((c) => {
          const end = c.firstStep + c.calls.length;
          next.set(c.caseRevisionId, end);
          return { caseRevisionId: c.caseRevisionId, kind: 1, nextStep: end, complete: c.last };
        }),
      };
    },
    ...raw,
  };
  return { server, evalc: new AgenticEvaluationClient({ service: () => server }) };
}

const live = (body) => async () => body;

test("record buffers steps and sends one chunk per case on flush, last set by finish", async () => {
  const { server, evalc } = stubServer();
  const tape = await evalc.recordLease({ evaluationRunId: "run_1", lease: LEASE });
  const a = tape.case(CASE_A);
  const b = tape.case(CASE_B);
  assert.equal(await a.model('{"m":1}', live('{"r":1}')), '{"r":1}');
  assert.equal(await a.tool("search", '{"q":2}', live('{"r":2}')), '{"r":2}');
  assert.equal(await b.model('{"m":3}', live('{"r":3}')), '{"r":3}');
  assert.equal(server.requests.length, 0, "a step costs no round trip");
  a.finish();
  await tape.flush();

  assert.equal(server.requests.length, 1);
  const [ca, cb] = server.requests[0].chunks;
  assert.deepEqual(
    ca.calls.map((c) => [c.kind, c.toolName, c.requestJson, c.responseJson]),
    [
      [1, "", '{"m":1}', '{"r":1}'],
      [2, "search", '{"q":2}', '{"r":2}'],
    ],
  );
  assert.equal(ca.firstStep, 0);
  assert.equal(ca.last, true);
  assert.equal(cb.last, false);

  // Acknowledged calls are dropped: the next flush sends only what is new, from next_step.
  await b.model('{"m":4}', live('{"r":4}'));
  b.finish();
  await tape.flush();
  assert.equal(server.requests[1].chunks.length, 1);
  assert.equal(server.requests[1].chunks[0].firstStep, 1);
  assert.equal(server.requests[1].chunks[0].calls.length, 1);
  assert.equal(server.requests[1].chunks[0].last, true);

  await tape.flush();
  assert.equal(server.requests.length, 2, "nothing pending sends nothing");
});

test("record flushes before a call would carry the request past the published bound", async () => {
  const { server, evalc } = stubServer();
  const tape = await evalc.recordLease({ evaluationRunId: "run_1", lease: LEASE });
  const a = tape.case(CASE_A);
  const body = "x".repeat(200);
  // Budget is 1000 bytes less framing; each call is 400 bytes plus overhead, so two fit and a third does not.
  await a.model(body, live(body));
  await a.model(body, live(body));
  assert.equal(server.requests.length, 0);
  await a.model(body, live(body));
  assert.equal(server.requests.length, 1, "the third call flushed the first two");
  assert.equal(server.requests[0].chunks[0].calls.length, 2);
  a.finish();
  await tape.flush();
  assert.equal(server.requests[1].chunks[0].firstStep, 2);
  assert.equal(server.requests[1].chunks[0].calls.length, 1);
});

test("record flushes at the published calls-per-request bound", async () => {
  const { server, evalc } = stubServer({}, [posture({ max_calls_per_request: 2 })]);
  const tape = await evalc.recordLease({ evaluationRunId: "run_1", lease: LEASE });
  const a = tape.case(CASE_A);
  const b = tape.case(CASE_B);
  await a.model("{}", live("{}"));
  await b.model("{}", live("{}"));
  assert.equal(server.requests.length, 0);
  await a.model("{}", live("{}"));
  assert.equal(server.requests.length, 1);
  assert.equal(server.requests[0].chunks.length, 2);
});

test("a call over the per-call bound is refused locally, naming sizes and never its content", async () => {
  const { server, evalc } = stubServer();
  const tape = await evalc.recordLease({ evaluationRunId: "run_1", lease: LEASE });
  const a = tape.case(CASE_A);
  const big = `"${SECRET}${"x".repeat(700)}"`;
  const e = await a.model("{}", live(big)).catch((x) => x);
  assert.ok(e instanceof ValidationError);
  assert.match(e.message, /\d+ bytes, over the 600-byte bound/);
  assert.equal(e.message.includes(SECRET), false);
  await assert.rejects(() => a.tool("t".repeat(129), "{}", live("{}")), ValidationError);
  await tape.flush();
  assert.equal(server.requests.length, 0);
});

test("a recording_conflict keeps the chunk for the next flush; another rejection throws", async () => {
  let reject = "recording_conflict";
  const { server, evalc } = stubServer({
    recordEvaluationCaseSteps: async (req) => {
      server.requests.push(structuredClone(req));
      return { acks: [{ kind: 3, nextStep: 0, rejection: { code: reject, message: "m" } }] };
    },
  });
  const tape = await evalc.recordLease({ evaluationRunId: "run_1", lease: LEASE });
  const a = tape.case(CASE_A);
  await a.model("{}", live("{}"));
  await tape.flush();
  reject = "case_already_submitted";
  const e = await tape.flush().catch((x) => x);
  assert.equal(server.requests[1].chunks[0].calls.length, 1, "the conflicted call was resent");
  assert.ok(e instanceof CaseRecordingRejectedError);
  assert.equal(e.code, "case_already_submitted");
  assert.equal(e.caseRevisionId, "r1");
  await tape.flush();
  assert.equal(server.requests.length, 2, "a rejected case is never resent");
});

test("RECORDING_UNAVAILABLE on FAILED_PRECONDITION is a non-retryable typed error naming no configuration", async () => {
  const { evalc } = stubServer({
    recordEvaluationCaseSteps: async () => {
      throw new ConnectError("recording and replay are unavailable", Code.FailedPrecondition, undefined, [
        { desc: ExternalLeaseRefusalV1Schema, value: { kind: 8, message: "recording and replay are unavailable" } },
      ]);
    },
  });
  const tape = await evalc.recordLease({ evaluationRunId: "run_1", lease: LEASE });
  await tape.case(CASE_A).model("{}", live("{}"));
  const e = await tape.flush().catch((x) => x);
  assert.ok(e instanceof RecordingUnavailableError);
  assert.ok(e instanceof LeaseRefusedError);
  assert.equal(e.retryable, false);
  assert.equal(e.refusal.reason, "RECORDING_UNAVAILABLE");
  assert.equal(e.message, "recording and replay are unavailable on this deployment (RECORDING_UNAVAILABLE)");
});

test("RECORDING_UNAVAILABLE on UNAVAILABLE stays a ConnectError and keeps the buffer", async () => {
  let fail = true;
  const { server, evalc } = stubServer({
    recordEvaluationCaseSteps: async (req) => {
      server.requests.push(structuredClone(req));
      if (fail) {
        throw new ConnectError("store", Code.Unavailable, undefined, [
          { desc: ExternalLeaseRefusalV1Schema, value: { kind: 8 } },
        ]);
      }
      return { acks: [{ kind: 1, nextStep: 1, complete: false }] };
    },
  });
  const tape = await evalc.recordLease({ evaluationRunId: "run_1", lease: LEASE });
  await tape.case(CASE_A).model("{}", live("{}"));
  const e = await tape.flush().catch((x) => x);
  assert.ok(e instanceof ConnectError);
  assert.equal(e instanceof RecordingUnavailableError, false);
  fail = false;
  await tape.flush();
  assert.equal(server.requests[1].chunks[0].calls.length, 1, "the resend carries the kept call");
  assert.equal(server.requests[1].chunks[0].firstStep, 0);
});

test("a server with no sdk_record_replay posture is refused locally, before any step", async () => {
  for (const postures of [[], [{ ...posture(), state: 2 }]]) {
    const { evalc } = stubServer({}, postures);
    await assert.rejects(() => evalc.recordLease({ evaluationRunId: "run_1", lease: LEASE }), RecordingUnavailableError);
    await assert.rejects(() => evalc.replayLease({ evaluationRunId: "run_1", lease: LEASE }), RecordingUnavailableError);
  }
});

test("a whole-request refusal on a 200 throws LeaseRefusedError", async () => {
  const { evalc } = stubServer({
    recordEvaluationCaseSteps: async () => ({ acks: [], refusal: { kind: 4, message: "lease expired" } }),
  });
  const tape = await evalc.recordLease({ evaluationRunId: "run_1", lease: LEASE });
  await tape.case(CASE_A).model("{}", live("{}"));
  const e = await tape.flush().catch((x) => x);
  assert.ok(e instanceof LeaseRefusedError);
  assert.equal(e.refusal.reason, "LEASE_EXPIRED");
});

test("replay answers each step from the recording without calling live", async () => {
  const seen = [];
  const { evalc } = stubServer({
    lookupReplayStep: async (req) => {
      seen.push(req);
      return { outcome: { case: "responseJson", value: `{"step":${req.step}}` } };
    },
  });
  const tape = await evalc.replayLease({ evaluationRunId: "run_1", lease: LEASE });
  const a = tape.case(CASE_A);
  const never = async () => assert.fail("live must not run under replay");
  assert.equal(await a.model('{"m":1}', never), '{"step":0}');
  assert.equal(await a.tool("search", '{"q":1}', never), '{"step":1}');
  assert.deepEqual(
    seen.map((r) => [r.step, r.observed.kind, r.observed.toolName, r.caseRevisionId, r.leaseToken]),
    [
      [0, 1, "", "r1", "t1"],
      [1, 2, "search", "r1", "t1"],
    ],
  );
  a.finish();
  await tape.flush();
});

test("each divergence kind throws ReplayDivergedError carrying the step and both digests", async () => {
  const kinds = { 1: "MODEL_REQUEST_DIFFERS", 2: "TOOL_REQUEST_DIFFERS", 3: "RECORDING_EXHAUSTED", 4: "RECORDING_INCOMPLETE", 99: "UNSPECIFIED" };
  for (const [kind, reason] of Object.entries(kinds)) {
    const { evalc } = stubServer({
      lookupReplayStep: async (req) => ({
        outcome: {
          case: "divergence",
          value: { step: req.step, kind: Number(kind), expectedRequestDigest: "aa", observedRequestDigest: "bb" },
        },
      }),
    });
    const tape = await evalc.replayLease({ evaluationRunId: "run_1", lease: LEASE });
    const e = await tape.case(CASE_A).model(`{"k":"${SECRET}"}`, live("{}")).catch((x) => x);
    assert.ok(e instanceof ReplayDivergedError, reason);
    assert.deepEqual(
      [e.divergence.reason, e.divergence.step, e.divergence.expectedRequestDigest, e.divergence.observedRequestDigest],
      [reason, 0, "aa", "bb"],
    );
    assert.equal(e.message.includes(SECRET), false);
  }
});

test("replay refusals: CASE_ALREADY_SUBMITTED on a 200, RECORDING_UNAVAILABLE in the details", async () => {
  const { evalc } = stubServer({ lookupReplayStep: async () => ({ refusal: { kind: 9, message: "done" } }) });
  const tape = await evalc.replayLease({ evaluationRunId: "run_1", lease: LEASE });
  const e = await tape.case(CASE_A).model("{}", live("{}")).catch((x) => x);
  assert.ok(e instanceof LeaseRefusedError);
  assert.equal(e.refusal.reason, "CASE_ALREADY_SUBMITTED");

  const { evalc: off } = stubServer({
    lookupReplayStep: async () => {
      throw new ConnectError("x", Code.FailedPrecondition, undefined, [
        { desc: ExternalLeaseRefusalV1Schema, value: { kind: 8 } },
      ]);
    },
  });
  const offTape = await off.replayLease({ evaluationRunId: "run_1", lease: LEASE });
  await assert.rejects(() => offTape.case(CASE_A).model("{}", live("{}")), RecordingUnavailableError);
});
