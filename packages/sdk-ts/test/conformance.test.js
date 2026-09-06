// Fixture-replay conformance: decode real proto WIRE BYTES through the SDK's
// typed decoders and assert the lifted shape.
//
// The design-samples golden bundle is not vendored into this repo (it lives in
// the o11y-api tree), so rather than replay stored response fixtures we replay
// gen-ts round-trips: build each refusal/ack message, encode it to binary with
// the generated schema, decode it back, and run it through the SDK mapper the
// journey surface uses. This exercises the same fromBinary path a live response
// takes and proves the mappers agree with the wire contract at capability 48.
// If the golden bundle is later vendored, add its fixtures alongside these.
import { strict as assert } from "node:assert";
import { test } from "node:test";

import { create, toBinary, fromBinary } from "@bufbuild/protobuf";
import {
  ExternalLeaseRefusalV1Schema,
  ExternalCaseOutputAckV1Schema,
  EvaluationLaunchRejectionV1Schema,
  PlatformAnnotationRejectionV1Schema,
  EvaluationCursorResyncV1Schema,
} from "@o11y-one/api/o11y_one/agentic/v1/evaluation_pb";

import {
  toLeaseRefusal,
  toCaseAck,
  toLaunchRejection,
  toAnnotationRejection,
  toCursorResync,
} from "../dist/index.js";

// Encode with the generated schema, decode back — the wire round-trip.
function roundTrip(schema, init) {
  return fromBinary(schema, toBinary(schema, create(schema, init)));
}

test("ExternalLeaseRefusalV1 wire bytes decode to a typed lease refusal", () => {
  const msg = roundTrip(ExternalLeaseRefusalV1Schema, {
    kind: 4, // LEASE_EXPIRED
    message: "your lease expired",
    missingScope: undefined,
    recovery: 1, // RETRY
  });
  const r = toLeaseRefusal(msg);
  assert.equal(r.type, "lease-refusal");
  assert.equal(r.reason, "LEASE_EXPIRED");
  assert.equal(r.recovery, "RETRY");
  assert.equal(r.message, "your lease expired");
});

test("ExternalLeaseRefusalV1 SCOPE_MISSING carries the named scope", () => {
  const msg = roundTrip(ExternalLeaseRefusalV1Schema, {
    kind: 7, // SCOPE_MISSING
    message: "missing scope",
    missingScope: "lease:submit",
  });
  const r = toLeaseRefusal(msg);
  assert.equal(r.reason, "SCOPE_MISSING");
  assert.equal(r.missingScope, "lease:submit");
});

test("ExternalCaseOutputAckV1 wire bytes decode to a typed per-case ack", () => {
  const msg = roundTrip(ExternalCaseOutputAckV1Schema, {
    cohortKey: "a",
    candidateKey: "x",
    caseRevisionId: "rev_1",
    trial: 2,
    kind: 3, // REJECTED
    observedState: 9, // LEASE_EXPIRED
  });
  const ack = toCaseAck(msg);
  assert.equal(ack.kind, "REJECTED");
  assert.equal(ack.caseRevisionId, "rev_1");
  assert.equal(ack.trial, 2);
  assert.equal(ack.observedState, 9);
});

test("EvaluationLaunchRejectionV1 wire bytes decode to a typed launch rejection", () => {
  const msg = roundTrip(EvaluationLaunchRejectionV1Schema, {
    kind: 7, // IDEMPOTENCY_KEY_REUSED
    expectedDigest: "aaa",
    observedDigest: "bbb",
    existingEvaluationRunId: "run_prev",
    recovery: 2, // RE_PREVIEW
    detail: "key already used",
  });
  const r = toLaunchRejection(msg);
  assert.equal(r.reason, "IDEMPOTENCY_KEY_REUSED");
  assert.equal(r.existingEvaluationRunId, "run_prev");
  assert.equal(r.recovery, "RE_PREVIEW");
});

test("PlatformAnnotationRejectionV1 wire bytes decode, lifting supported kinds", () => {
  const msg = roundTrip(PlatformAnnotationRejectionV1Schema, {
    reason: 1, // KIND_UNKNOWN
    field: "kind",
    supportedKinds: [1, 2, 3], // DEPLOYMENT, MARKER, HIGHLIGHT
  });
  const r = toAnnotationRejection(msg);
  assert.equal(r.reason, "KIND_UNKNOWN");
  assert.equal(r.field, "kind");
  assert.deepEqual(r.supportedKinds, ["DEPLOYMENT", "MARKER", "HIGHLIGHT"]);
});

test("EvaluationCursorResyncV1 wire bytes decode to a typed resync directive", () => {
  const msg = roundTrip(EvaluationCursorResyncV1Schema, { reason: 3 }); // CURSOR_MALFORMED
  const r = toCursorResync(msg);
  assert.equal(r.type, "cursor-resync");
  assert.equal(r.reason, "CURSOR_MALFORMED");
});

test("an unknown discriminant folds to UNSPECIFIED, never a bare number", () => {
  const msg = roundTrip(ExternalLeaseRefusalV1Schema, { kind: 999, message: "future" });
  const r = toLeaseRefusal(msg);
  assert.equal(r.reason, "UNSPECIFIED");
});
