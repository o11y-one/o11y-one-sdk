// The Loop rollout client against the statuses the server sends.
//
// A stub fetch answers in gRPC-web, and each refusal is the server's own: its
// gRPC code, its sentence, and its LoopRolloutRejectionV1 in
// grpc-status-details-bin, as the server sends it. Timers and Date are
// node:test's mocks, so the paused-run retries never sleep.
import { strict as assert } from "node:assert";
import { test } from "node:test";
import { inspect } from "node:util";

import { create, fromBinary, toBinary } from "@bufbuild/protobuf";
import { anyPack } from "@bufbuild/protobuf/wkt";
import { BinaryWriter } from "@bufbuild/protobuf/wire";
import {
  CloseLoopRolloutRequestSchema,
  CloseLoopRolloutResponseSchema,
  ForkLoopRolloutRequestSchema,
  ForkLoopRolloutResponseSchema,
  LoopRolloutRejectionV1Schema,
  ResetLoopRolloutRequestSchema,
  ResetLoopRolloutResponseSchema,
  StepLoopRolloutRequestSchema,
  StepLoopRolloutResponseSchema,
} from "@o11y-one/api-agentic/o11y_one/agentic/v1/rollout_pb";

import { classify } from "../dist/index.js";
import { LoopClient, RolloutRefused } from "@o11y-one/sdk/loop";

const CREDENTIAL = "o11y_mach.AAAAAAAAAAAAAAAAAAAAAA.BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBA";
const RUN = "trn_06AZ3XN1YQF4KD2M8RP7TV5W9C";

// [reason code, gRPC status, the server's sentence], as the server sends them.
const RECORDED = [
  ["run_paused", 14, "the run is paused; resets wait until it resumes"],
  ["plan_concurrency_reached", 8, "the organization has as many environments open as its plan allows"],
  ["run_concurrency_reached", 8, "the run has as many environments open as it allows"],
  ["run_stopped", 9, "the run was stopped, so it starts no rollout"],
  ["run_spend_cap_reached", 8, "the run's spend cap is reached; raise it to go on"],
  ["rate_limited", 8, "resets are arriving faster than the run's environments allow"],
  ["capacity_unavailable", 14, "no environment came up within the reset's wait; not billed"],
  ["step_in_progress", 9, "the rollout runs one step at a time"],
  ["loop_rollouts_unavailable", 9, "capability `loop_rollouts` is not available"],
];

const VERBS = {
  ResetLoopRollout: [ResetLoopRolloutRequestSchema, ResetLoopRolloutResponseSchema],
  StepLoopRollout: [StepLoopRolloutRequestSchema, StepLoopRolloutResponseSchema],
  CloseLoopRollout: [CloseLoopRolloutRequestSchema, CloseLoopRolloutResponseSchema],
  ForkLoopRollout: [ForkLoopRolloutRequestSchema, ForkLoopRolloutResponseSchema],
};

function frame(flags, bytes) {
  const out = new Uint8Array(5 + bytes.length);
  out[0] = flags;
  new DataView(out.buffer).setUint32(1, bytes.length);
  out.set(bytes, 5);
  return out;
}

// A refusal as tonic sends it: trailers-only, its google.rpc.Status in grpc-status-details-bin.
function refusal(reason, { retryAfterMillis, limit } = {}) {
  const [, status, message] = RECORDED.find(([r]) => r === reason);
  const detail = create(LoopRolloutRejectionV1Schema, { reasonCode: reason, retryAfterMillis, limit });
  const any = anyPack(LoopRolloutRejectionV1Schema, detail);
  const anyBytes = new BinaryWriter().uint32(10).string(any.typeUrl).uint32(18).bytes(any.value).finish();
  const rpcStatus = new BinaryWriter().uint32(8).int32(status).uint32(18).string(message).uint32(26).bytes(anyBytes).finish();
  return {
    headers: {
      "grpc-status": String(status),
      "grpc-message": encodeURIComponent(message),
      "grpc-status-details-bin": Buffer.from(rpcStatus).toString("base64"),
    },
  };
}

function bare(status, message) {
  return { headers: { "grpc-status": String(status), "grpc-message": encodeURIComponent(message) } };
}

// A stub fetch answering each verb from its own queue, recording [verb, request, headers].
function server(answers) {
  const calls = [];
  const fetch = async (input, init) => {
    const verb = String(input).split("/").pop();
    const [requestSchema, responseSchema] = VERBS[verb];
    const body = new Uint8Array(init.body);
    calls.push([verb, fromBinary(requestSchema, body.subarray(5)), new Headers(init.headers)]);
    const answer = answers[verb].shift();
    const headers = { "content-type": "application/grpc-web+proto" };
    if (answer.headers) {
      return new Response(null, { status: 200, headers: { ...headers, ...answer.headers } });
    }
    const message = toBinary(responseSchema, create(responseSchema, answer));
    const trailer = new TextEncoder().encode("grpc-status: 0\r\n");
    const bytes = new Uint8Array([...frame(0, message), ...frame(0x80, trailer)]);
    return new Response(bytes, { status: 200, headers });
  };
  return { calls, fetch };
}

function clientOn(stub, open) {
  const client = new LoopClient({ run: RUN, credential: CREDENTIAL, baseUrl: "https://api.invalid", fetch: stub.fetch });
  if (open) client.open = open;
  return client;
}

const rollout = (rolloutId) => ({ rollout: { rolloutId, runId: RUN } });

async function refusedBy(promise) {
  try {
    await promise;
  } catch (error) {
    return error;
  }
  assert.fail("expected a refusal");
}

// Runs `promise` to its end, the clock jumping to each timer it waits on.
async function drive(timers, promise) {
  let settled = false;
  promise.then(
    () => (settled = true),
    () => (settled = true),
  );
  while (!settled) {
    for (let i = 0; i < 20; i++) await new Promise((resolve) => setImmediate(resolve));
    if (!settled) timers.runAll();
  }
  return promise;
}

for (const [reason, , message] of RECORDED) {
  test(`${reason}, as the server sends it, raises RolloutRefused with its stable code`, async () => {
    const stub = server({ StepLoopRollout: [refusal(reason, { retryAfterMillis: 1500n, limit: 8 })] });
    const refused = await refusedBy(clientOn(stub, "r-1").step([]));
    assert.ok(refused instanceof RolloutRefused);
    assert.deepEqual([refused.code, refused.retryAfterMs], [reason, 1500]);
    assert.equal(refused.message, `${reason}: ${message}`);
    assert.equal(classify(refused.cause).code, RECORDED.find(([r]) => r === reason)[1]);
  });
}

test("a refusal without a retry-after says undefined", async () => {
  const stub = server({ StepLoopRollout: [refusal("step_in_progress")] });
  const refused = await refusedBy(clientOn(stub, "r-1").step([]));
  assert.equal(refused.retryAfterMs, undefined);
});

test("a status without a rollout refusal is thrown as the server sent it", async () => {
  const stub = server({
    StepLoopRollout: [bare(5, "no rollout in this organization has that id"), bare(16, "Authentication failed")],
  });
  const client = clientOn(stub, "r-1");
  const unknown = await refusedBy(client.step([]));
  assert.ok(!(unknown instanceof RolloutRefused));
  assert.equal(unknown.rawMessage, "no rollout in this organization has that id");
  assert.equal(classify(await refusedBy(client.step([]))).disposition, "reauthenticate");
});

test("plan_concurrency_reached raises at once", async () => {
  const stub = server({ ResetLoopRollout: [refusal("plan_concurrency_reached", { limit: 200 })] });
  const refused = await refusedBy(clientOn(stub).reset());
  assert.equal(refused.code, "plan_concurrency_reached");
  assert.equal(stub.calls.length, 1);
});

test("a paused run is retried after each retry-after under one request id", async (t) => {
  t.mock.timers.enable({ apis: ["setTimeout", "Date"], now: 0 });
  const paused = Array.from({ length: 3 }, () => refusal("run_paused", { retryAfterMillis: 60_000n }));
  const stub = server({ ResetLoopRollout: [...paused, rollout("r-1")] });
  const client = clientOn(stub);
  const reset = await drive(t.mock.timers, client.reset({ groupSize: 4 }));
  assert.equal(reset.rolloutId, "r-1");
  assert.equal(Date.now(), 180_000);
  const requests = stub.calls.map(([, request]) => request);
  assert.equal(new Set(requests.map((request) => request.requestId)).size, 1);
  assert.deepEqual(new Set(requests.map((request) => `${request.runId}/${request.groupSize}`)), new Set([`${RUN}/4`]));
  assert.equal(client.rolloutId, "r-1");
});

test("a paused run is retried for 30 minutes, then raised", async (t) => {
  t.mock.timers.enable({ apis: ["setTimeout", "Date"], now: 0 });
  const paused = Array.from({ length: 40 }, () => refusal("run_paused", { retryAfterMillis: 60_000n }));
  const stub = server({ ResetLoopRollout: paused });
  const refused = await refusedBy(drive(t.mock.timers, clientOn(stub).reset()));
  assert.equal(refused.code, "run_paused");
  assert.equal(stub.calls.length, 31);
  assert.equal(Date.now(), 30 * 60_000);
});

test("a paused run without a retry-after waits the default", async (t) => {
  t.mock.timers.enable({ apis: ["setTimeout", "Date"], now: 0 });
  const paused = Array.from({ length: 400 }, () => refusal("run_paused"));
  const stub = server({ ResetLoopRollout: paused });
  await refusedBy(drive(t.mock.timers, clientOn(stub).reset()));
  assert.equal(stub.calls.length, 30 * 60_000 / 5_000 + 1);
  assert.equal(Date.now(), 30 * 60_000);
});

test("reset closes the open rollout before the next reset", async () => {
  const stub = server({
    ResetLoopRollout: [rollout("r-1"), rollout("r-2")],
    CloseLoopRollout: [{ ...rollout("r-1"), pending: true }, rollout("r-1")],
  });
  const client = clientOn(stub);
  await client.reset();
  await client.reset();
  assert.deepEqual(
    stub.calls.map(([verb, request]) => [verb, request.rolloutId ?? ""]),
    [
      ["ResetLoopRollout", ""],
      ["CloseLoopRollout", "r-1"],
      ["CloseLoopRollout", "r-1"],
      ["ResetLoopRollout", ""],
    ],
  );
  assert.equal(client.rolloutId, "r-2");
});

test("close answers the rewarded rollout and leaves none open", async () => {
  const stub = server({ CloseLoopRollout: [rollout("r-1")] });
  const client = clientOn(stub, "r-1");
  assert.equal((await client.close()).rolloutId, "r-1");
  assert.equal(client.rolloutId, undefined);
  assert.equal(await client.close(), undefined);
  assert.equal(stub.calls.length, 1);
});

test("step sends the calls and model message on the open rollout, with the key", async () => {
  const stub = server({ StepLoopRollout: [{ step: 1 }] });
  const call = { timeoutMillis: 1000, call: { case: "exec", value: { argv: ["true"] } } };
  assert.equal((await clientOn(stub, "r-1").step([call], '{"role":"assistant"}')).step, 1);
  const [[, request, headers]] = stub.calls;
  assert.equal(request.rolloutId, "r-1");
  assert.deepEqual(request.calls[0].call.value.argv, ["true"]);
  assert.equal(request.modelMessageJson, '{"role":"assistant"}');
  assert.equal(headers.get("x-o11y-key"), CREDENTIAL);
});

test("step without an open rollout is refused locally", async () => {
  await assert.rejects(clientOn(server({})).step([]), /reset/);
});

test("fork answers a client per copy, the rollout itself first", async () => {
  const stub = server({
    ForkLoopRollout: [{ rollouts: [{ rolloutId: "r-1" }, { rolloutId: "r-2" }] }],
    StepLoopRollout: [{ step: 4 }],
  });
  const client = clientOn(stub, "r-1");
  const forks = await client.fork(2);
  assert.equal(forks[0], client);
  assert.deepEqual(forks.map((fork) => fork.rolloutId), ["r-1", "r-2"]);
  await forks[1].step([]);
  const [[, forked], [, stepped]] = stub.calls;
  assert.deepEqual([forked.rolloutId, forked.copies, stepped.rolloutId], ["r-1", 2, "r-2"]);
  assert.equal(client.rolloutId, "r-1");
});

test("run and credential fall back to the environment, and the key is never shown", async (t) => {
  t.after(() => {
    delete process.env.O11Y_RUN;
    delete process.env.O11Y_API_KEY;
  });
  assert.throws(() => new LoopClient({ credential: CREDENTIAL }), /O11Y_RUN/);
  assert.throws(() => new LoopClient({ run: RUN }), /empty/);
  process.env.O11Y_RUN = RUN;
  process.env.O11Y_API_KEY = CREDENTIAL;
  const stub = server({ ResetLoopRollout: [refusal("run_stopped")] });
  const client = new LoopClient({ baseUrl: "https://api.invalid", fetch: stub.fetch });
  const refused = await refusedBy(client.reset());
  const [[, request, headers]] = stub.calls;
  assert.deepEqual([request.runId, headers.get("x-o11y-key")], [RUN, CREDENTIAL]);
  const shown = [inspect(client, { depth: 8 }), JSON.stringify(client), String(client), inspect(refused), String(refused)];
  assert.deepEqual(shown.filter((text) => text.includes("BBBBBBBB")), []);
});

test("a plain http endpoint off this machine is refused, naming only its scheme", () => {
  for (const baseUrl of ["http://grpc.example", "http://user:secret@grpc.example"]) {
    assert.throws(
      () => new LoopClient({ run: RUN, credential: CREDENTIAL, baseUrl }),
      (error) => /'http'/.test(error.message) && !error.message.includes("secret") && !error.message.includes(CREDENTIAL),
    );
  }
});

test("https, and plain http to this machine, are allowed", () => {
  for (const baseUrl of ["https://grpc.example", "http://127.0.0.1:9", "http://localhost:9", "http://[::1]:9"]) {
    new LoopClient({ run: RUN, credential: CREDENTIAL, baseUrl });
  }
});
