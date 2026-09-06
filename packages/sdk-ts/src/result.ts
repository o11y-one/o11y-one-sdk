/**
 * A `Result<T, E>` discriminated union.
 *
 * This is the SDK's answer to the compendium's key shape: many verbs on the
 * agentic-evaluation surface refuse ON A 200 — the refusal is a field on the
 * response message, not a transport error. Throwing on it would erase a typed,
 * structured, actionable value and hand the caller a stack trace instead. So
 * the journey methods that can be refused this way return a `Result`: `ok` on
 * acceptance, `err` carrying a TYPED refusal the caller branches on.
 *
 * Errors that arrive as a transport failure (a real non-200 with a
 * `google.rpc.Status`) are a different axis and still throw a `ConnectError` —
 * `classify()` in errors.ts renders those. A method whose refusal rides in
 * `Status.details` (launch, annotation, dataset-version) catches that throw and
 * folds it back into an `err(...)` so the caller has ONE branch to write, not
 * two. Which methods do which is documented on each.
 */

/** The acceptance arm. */
export interface Ok<T> {
  readonly ok: true;
  readonly value: T;
}

/** The refusal arm. `refusal` is always one of the typed unions in refusals.ts. */
export interface Err<E> {
  readonly ok: false;
  readonly refusal: E;
}

export type Result<T, E> = Ok<T> | Err<E>;

export function ok<T>(value: T): Ok<T> {
  return { ok: true, value };
}

export function err<E>(refusal: E): Err<E> {
  return { ok: false, refusal };
}

export function isOk<T, E>(r: Result<T, E>): r is Ok<T> {
  return r.ok;
}

export function isErr<T, E>(r: Result<T, E>): r is Err<E> {
  return !r.ok;
}

/**
 * Unwrap or throw. A convenience for scripts and tests that WANT the throw —
 * the library itself never calls this. The thrown error names the refusal so a
 * stack trace is still legible.
 */
export function unwrap<T, E>(r: Result<T, E>): T {
  if (r.ok) {
    return r.value;
  }
  throw new Error(`o11y call was refused: ${JSON.stringify(r.refusal)}`);
}
