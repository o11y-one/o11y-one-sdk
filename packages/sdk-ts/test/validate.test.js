// Unit tests for the synchronous contract-guard.
import { strict as assert } from "node:assert";
import { test } from "node:test";

import {
  ValidationError,
  requireNonEmpty,
  requireIdempotencyKey,
  requireExactlyOne,
  rejectUnspecified,
  requireWithinBytes,
  byteLength,
} from "../dist/index.js";

test("requireNonEmpty rejects empty and whitespace, returns the value otherwise", () => {
  assert.throws(() => requireNonEmpty("f", ""), ValidationError);
  assert.throws(() => requireNonEmpty("f", "   "), ValidationError);
  assert.throws(() => requireNonEmpty("f", undefined), ValidationError);
  assert.equal(requireNonEmpty("f", "ok"), "ok");
});

test("requireIdempotencyKey demands a caller-minted key", () => {
  assert.throws(() => requireIdempotencyKey("idempotencyKey", ""), ValidationError);
  assert.equal(requireIdempotencyKey("idempotencyKey", "k1"), "k1");
});

test("requireExactlyOne enforces one-of-N", () => {
  assert.throws(
    () => requireExactlyOne("src", [
      { name: "a", present: false },
      { name: "b", present: false },
    ]),
    (e) => e instanceof ValidationError && /none was supplied/.test(e.message),
  );
  assert.throws(
    () => requireExactlyOne("src", [
      { name: "a", present: true },
      { name: "b", present: true },
    ]),
    (e) => e instanceof ValidationError && /exactly one/.test(e.message),
  );
  assert.doesNotThrow(() =>
    requireExactlyOne("src", [
      { name: "a", present: true },
      { name: "b", present: false },
    ]),
  );
});

test("rejectUnspecified names the offending index", () => {
  assert.throws(
    () => rejectUnspecified("scopes", [1, 0, 3]),
    (e) => e instanceof ValidationError && /scopes\[1\]/.test(e.message),
  );
  assert.doesNotThrow(() => rejectUnspecified("scopes", [1, 2, 3]));
});

test("byteLength counts UTF-8 bytes, not code units", () => {
  assert.equal(byteLength("abc"), 3);
  assert.equal(byteLength("é"), 2); // U+00E9
  assert.equal(byteLength("€"), 3); // U+20AC
  assert.equal(byteLength("😀"), 4); // U+1F600, surrogate pair
});

test("requireWithinBytes uses a real published limit, not an invented one", () => {
  assert.equal(requireWithinBytes("f", "abc", 8), "abc");
  assert.throws(() => requireWithinBytes("f", "abcdefghij", 4), ValidationError);
});
