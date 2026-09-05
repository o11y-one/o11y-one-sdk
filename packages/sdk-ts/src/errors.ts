/**
 * The O11y One error taxonomy, as the SDK must render it.
 *
 * From lane 50A's note: `UNAUTHENTICATED` vs `PERMISSION_DENIED` is the whole
 * reason this layer exists. "Your token is invalid" and "your token is fine but
 * this capability is not shipped / not granted" are different problems with
 * different fixes, and collapsing them into "auth error" is the failure mode
 * this file prevents.
 */
import { Code, ConnectError } from "@connectrpc/connect";

/** What a caller should DO about a failure. */
export type FailureDisposition =
  /** Credential is absent, malformed, unknown, expired, or revoked. Re-auth. Never retry. */
  | "reauthenticate"
  /** Credential is valid but lacks the scope, or was presented to a non-machine surface. Stop. */
  | "insufficient-scope"
  /** SDK/server version skew (unknown scope discriminant on a write). Stop. */
  | "version-skew"
  /** Auth backend is down. Retryable with backoff — deliberately not cached server-side. */
  | "retry-with-backoff"
  /** Anything else. The SDK does not guess. */
  | "unclassified";

export interface ClassifiedFailure {
  readonly disposition: FailureDisposition;
  readonly code: Code | undefined;
  readonly message: string;
  /**
   * For `insufficient-scope`, the canonical scope string the server named in
   * its message, when it named one: `eval:read`, `run:execute`, `dataset:write`,
   * `lease:submit`, `platform-annotation:write`.
   */
  readonly missingScope: string | undefined;
  readonly retryable: boolean;
}

const CANONICAL_SCOPES = [
  "eval:read",
  "run:execute",
  "dataset:write",
  "lease:submit",
  "platform-annotation:write",
] as const;

/** The five canonical machine-principal scope strings (50A, frozen taxonomy). */
export type MachineScope = (typeof CANONICAL_SCOPES)[number];

export const MACHINE_SCOPES: readonly MachineScope[] = CANONICAL_SCOPES;

/**
 * Classify a thrown error into the taxonomy above.
 *
 * Non-Connect errors pass through as `unclassified` rather than being forced
 * into a bucket — a DNS failure is not an auth failure and pretending otherwise
 * sends people down the wrong path.
 */
export function classify(err: unknown): ClassifiedFailure {
  if (!(err instanceof ConnectError)) {
    return {
      disposition: "unclassified",
      code: undefined,
      message: err instanceof Error ? err.message : String(err),
      missingScope: undefined,
      retryable: false,
    };
  }

  switch (err.code) {
    case Code.Unauthenticated:
      return {
        disposition: "reauthenticate",
        code: err.code,
        message: err.rawMessage,
        missingScope: undefined,
        retryable: false,
      };
    case Code.PermissionDenied: {
      // The server names the missing canonical scope in the message when the
      // cause is a scope gap. When it does not, the cause is the other
      // PERMISSION_DENIED case: a machine credential on a non-machine surface.
      const named = MACHINE_SCOPES.find((s) => err.rawMessage.includes(s));
      return {
        disposition: "insufficient-scope",
        code: err.code,
        message: err.rawMessage,
        missingScope: named,
        retryable: false,
      };
    }
    case Code.InvalidArgument:
      return {
        disposition: "version-skew",
        code: err.code,
        message: err.rawMessage,
        missingScope: undefined,
        retryable: false,
      };
    case Code.Unavailable:
      return {
        disposition: "retry-with-backoff",
        code: err.code,
        message: err.rawMessage,
        missingScope: undefined,
        retryable: true,
      };
    default:
      return {
        disposition: "unclassified",
        code: err.code,
        message: err.rawMessage,
        missingScope: undefined,
        retryable: false,
      };
  }
}
