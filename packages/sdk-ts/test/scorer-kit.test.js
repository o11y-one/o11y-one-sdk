// The TypeScript scorer kit authors copy into a bundle: the seeded PRNG and the example scorer, run as the sandbox's
// Node runs them, with their types stripped. `pnpm run typecheck` type-checks them.
import { strict as assert } from "node:assert";
import { test } from "node:test";

import { seededRandom } from "../scorer-kit/o11y_prng.ts";
import { score } from "../scorer-kit/score.ts";

const MAX_U64 = 2n ** 64n - 1n;
const draws = (seed, n = 1000) => Array.from({ length: n }, seededRandom(seed));

test("the same seed draws the same sequence, each draw in [0, 1)", () => {
  const sequence = draws(42n);
  assert.deepEqual(draws(42n), sequence);
  assert.ok(sequence.every((x) => x >= 0 && x < 1));
  assert.ok(new Set(sequence).size > 990, "a sequence, not a constant");
});

test("seeds past 2^53 that differ only in the low bit draw different sequences", () => {
  // A number would round both of each pair to the same value.
  for (const seed of [2n ** 53n, MAX_U64 - 1n]) {
    assert.equal(seed & 1n, 0n);
    assert.notDeepEqual(draws(seed, 4), draws(seed | 1n, 4));
  }
});

test("seeds that differ only in the high bit draw different sequences", () => {
  assert.notDeepEqual(draws(5n, 4), draws(5n | (1n << 63n), 4));
});

test("the example scorer answers what the harness accepts, the same for the same seed", async () => {
  const context = { seed: MAX_U64, frozen_evaluation_time_unix_nanos: 1_700_000_000_000_000_000n };
  const lines = Array.from({ length: 50 }, (_, i) => `line ${i}`).join("\n");
  const same = await score({ candidate_output: lines, reference_output: lines }, context);
  assert.equal(same.score, 1);
  assert.equal(same.verdict, "pass");

  const edited = lines.replaceAll("line", "LINE");
  const differs = await score({ candidate_output: edited, reference_output: lines }, context);
  assert.equal(differs.score, 0);
  assert.equal(differs.verdict, "fail");

  // Half the lines match, so which lines it samples decides the score: 20 runs agree only when the seed decides them.
  const half = lines.split("\n").map((line, i) => (i % 2 ? line : "x")).join("\n");
  const runs = [];
  for (let i = 0; i < 20; i++) runs.push(await score({ candidate_output: half, reference_output: lines }, context));
  assert.equal(new Set(runs.map((run) => JSON.stringify(run))).size, 1);
  for (const output of [same, differs, runs[0]]) {
    assert.ok(Number.isFinite(output.score) && output.score >= 0 && output.score <= 1);
    assert.ok(Buffer.byteLength(output.label) <= 256);
    assert.deepEqual(Object.keys(output).filter((k) => !["score", "verdict", "label", "metrics"].includes(k)), []);
  }
});
