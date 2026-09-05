/**
 * Credential handling for machine principals.
 *
 * The wire contract below is SETTLED — it is read out of the running server, not
 * designed here. Source: lane 50A's credential-shape note (w50d handoff), which
 * in turn cites `shared/src/lib.rs:70` for the header name and
 * `server/src/services/api_tokens/crypto.rs` for the encoding.
 */

/**
 * The header a machine credential is presented in.
 *
 * `O11Y_ONE_API_KEY_HEADER_NAME` in o11y-api (`shared/src/lib.rs:70`).
 * `x-api-key` is accepted server-side as a fallback alias; this SDK always sends
 * the canonical name.
 *
 * Deliberately NOT `authorization: Bearer` — that path carries the browser
 * session JWT, and a machine credential presented there is rejected.
 */
export const CREDENTIAL_HEADER = "x-o11y-key";

/** Org scoping header (`O11Y_ONE_ORG_ID_HEADER_NAME`). */
export const ORG_ID_HEADER = "x-o11y-org-id";

/** Tenant scoping header (`O11Y_ONE_TENANT_ID_HEADER_NAME`). */
export const TENANT_ID_HEADER = "x-o11y-tenant-id";

/** Prefix carried by machine-principal credentials (`APITokenType::prefix()`). */
export const MACHINE_CREDENTIAL_PREFIX = "o11y_mach";

/** Server-side cap on the presented credential string (`API_TOKEN_MAX_LEN`). */
export const CREDENTIAL_MAX_LEN = 128;

/**
 * A credential string, opaque to the client.
 *
 * Shape is `o11y_mach.<selector>.<secret>` where selector is 16 random bytes and
 * secret is 32 random bytes, both base64url without padding. The SDK does not
 * parse past the prefix and must never try to: verification is Argon2id +
 * blake3 on the server and none of that is the client's business.
 *
 * It is returned exactly once, by `CreateMachineCredential`. There is no
 * read-back RPC and no recovery path.
 */
export type MachineCredential = string & { readonly __brand: "MachineCredential" };

/**
 * Cheap, local, structural validation. Catches the overwhelmingly common
 * mistakes — an empty env var, a session JWT pasted into the wrong variable, a
 * credential truncated by a copy-paste — before a network round trip turns them
 * into an opaque UNAUTHENTICATED.
 *
 * It is NOT authentication. A string that passes here can still be revoked,
 * expired, or unknown; only the server can say.
 */
export function assertLooksLikeMachineCredential(raw: string): MachineCredential {
  // The server trims whitespace and strips one layer of surrounding quotes
  // (`normalize_api_token_input`) so a value pasted out of a shell still works.
  // We normalise the same way rather than relying on it.
  let value = raw.trim();
  if (value.length >= 2) {
    const first = value[0];
    const last = value[value.length - 1];
    if ((first === '"' && last === '"') || (first === "'" && last === "'")) {
      value = value.slice(1, -1).trim();
    }
  }

  if (value.length === 0) {
    throw new Error("o11y credential is empty — set the credential env var or pass it explicitly");
  }
  if (value.length > CREDENTIAL_MAX_LEN) {
    throw new Error(
      `o11y credential is ${value.length} bytes, over the ${CREDENTIAL_MAX_LEN}-byte server limit; ` +
        "this is not a valid credential",
    );
  }
  if (!value.startsWith(`${MACHINE_CREDENTIAL_PREFIX}.`)) {
    throw new Error(
      `o11y credential does not start with "${MACHINE_CREDENTIAL_PREFIX}." — ` +
        "machine credentials do. If this is a browser session token it will not work here.",
    );
  }
  if (value.split(".").length !== 3) {
    throw new Error(
      "o11y credential is malformed: expected <prefix>.<selector>.<secret>, three dot-separated parts",
    );
  }
  return value as MachineCredential;
}
