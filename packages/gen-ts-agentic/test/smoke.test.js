// Smoke test for the generated agentic-subset TypeScript package.
//
// This does not test protoc-gen-es — Buf tests their own compiler. It tests the
// two things THIS repo can break: that the built output actually loads under
// the package's own module resolution, and that the wire-visible service names
// survived both the import re-rooting (see tools/sync-proto.sh) and the
// --path-scoped generation that produces this subset.
//
// It also guards the subset boundary: importing a domain that is NOT in the
// agentic closure (e.g. billing) must fail, because this package deliberately
// does not carry it.
//
// It runs against dist/, not src/, so it exercises the artifact that ships.
import { strict as assert } from "node:assert";
import { test } from "node:test";

import { create, toBinary, fromBinary, toJson } from "@bufbuild/protobuf";

import { PageRequestV1Schema } from "../dist/o11y_one/common/v1/common_pb.js";
import { AgenticEvaluationService } from "../dist/o11y_one/agentic/v1/evaluation_pb.js";

test("common/v1 descriptors load and round-trip through the runtime", () => {
  const page = create(PageRequestV1Schema, { limit: 25 });
  const bytes = toBinary(PageRequestV1Schema, page);
  const back = fromBinary(PageRequestV1Schema, bytes);
  assert.equal(back.limit, 25);
  assert.deepEqual(toJson(PageRequestV1Schema, back), { limit: 25 });
});

test("agentic service descriptors carry the wire-stable full name", () => {
  assert.equal(
    AgenticEvaluationService.typeName,
    "o11y_one.agentic.v1.AgenticEvaluationService",
  );
});

test("the subset does not carry non-agentic domains", async () => {
  await assert.rejects(
    () => import("../dist/o11y_one/billing/v1/billing_pb.js"),
    "billing must not be present in the agentic subset",
  );
});
