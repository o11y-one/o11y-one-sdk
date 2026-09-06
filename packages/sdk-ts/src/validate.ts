/**
 * Client-side input validation — the SDK's contract-guard.
 *
 * It fails FAST, SYNCHRONOUSLY, and TYPED, before a wire call is made, on the
 * mistakes the server would otherwise turn into an opaque `INVALID_ARGUMENT` a
 * round trip later: a missing required field, both arms of a mutually-exclusive
 * oneof set at once (or neither), an `UNSPECIFIED` enum discriminant the server
 * refuses, an idempotency key a CI retry forgot to mint.
 *
 * It is NOT the server's validation and never duplicates the authoritative
 * byte-caps — those are published on the capability envelope and enforced
 * server-side, and this layer surfaces the resulting typed rejection rather
 * than second-guessing the number. What it checks is STRUCTURE the SDK can be
 * certain of without the network.
 */

/**
 * A local, pre-flight validation failure. `field` names the offending input in
 * the caller's terms so the message is actionable without reading the proto.
 */
export class ValidationError extends Error {
  readonly field: string;

  constructor(field: string, message: string) {
    super(message);
    this.name = "ValidationError";
    this.field = field;
  }
}

/** Trim-aware non-empty string check. */
export function requireNonEmpty(field: string, value: string | undefined): string {
  if (value === undefined || value.trim().length === 0) {
    throw new ValidationError(field, `${field} is required and must not be empty`);
  }
  return value;
}

/**
 * An idempotency key the caller must supply. Required on every write that a CI
 * job could retry — a retry that forgot its key is exactly how a run, a case,
 * or a marker gets created twice.
 */
export function requireIdempotencyKey(field: string, value: string | undefined): string {
  if (value === undefined || value.trim().length === 0) {
    throw new ValidationError(
      field,
      `${field} is required: a retry-safe write needs a caller-minted idempotency key`,
    );
  }
  return value;
}

/**
 * Exactly-one-of, for a proto `oneof` the SDK exposes as separate arguments.
 * `entries` lists each arm and whether the caller supplied it; zero or two-plus
 * present is a `ValidationError` naming what was seen.
 */
export function requireExactlyOne(
  label: string,
  entries: ReadonlyArray<{ readonly name: string; readonly present: boolean }>,
): void {
  const present = entries.filter((e) => e.present).map((e) => e.name);
  if (present.length === 1) {
    return;
  }
  const names = entries.map((e) => e.name).join(", ");
  if (present.length === 0) {
    throw new ValidationError(
      label,
      `exactly one of {${names}} is required — none was supplied`,
    );
  }
  throw new ValidationError(
    label,
    `exactly one of {${names}} is allowed — got {${present.join(", ")}}`,
  );
}

/**
 * Reject an `UNSPECIFIED` (zero) discriminant in a set the server refuses
 * outright. An `UNSPECIFIED` scope on a principal-create, or inside a list
 * filter, is `INVALID_ARGUMENT` server-side; catching it here names the
 * position instead of the whole call.
 */
export function rejectUnspecified(field: string, values: readonly number[]): void {
  const at = values.indexOf(0);
  if (at !== -1) {
    throw new ValidationError(
      field,
      `${field}[${at}] is UNSPECIFIED (0); the server refuses an unspecified discriminant`,
    );
  }
}

/**
 * UTF-8 byte length, for the size guards a caller can opt into. Computed
 * without `TextEncoder` so this module pulls in neither the DOM lib nor
 * `@types/node` — it runs identically in a browser, a Worker and Node.
 */
export function byteLength(value: string): number {
  let bytes = 0;
  for (let i = 0; i < value.length; i++) {
    const code = value.codePointAt(i);
    if (code === undefined) {
      continue;
    }
    if (code > 0xffff) {
      i++; // a surrogate pair spans two UTF-16 code units
    }
    bytes += code <= 0x7f ? 1 : code <= 0x7ff ? 2 : code <= 0xffff ? 3 : 4;
  }
  return bytes;
}

/**
 * An optional upper byte-bound. Used only where the SDK holds a published limit
 * (e.g. the 128-byte credential cap in auth.ts); never with an invented number.
 */
export function requireWithinBytes(field: string, value: string, maxBytes: number): string {
  const len = byteLength(value);
  if (len > maxBytes) {
    throw new ValidationError(
      field,
      `${field} is ${len} bytes, over the ${maxBytes}-byte limit`,
    );
  }
  return value;
}
