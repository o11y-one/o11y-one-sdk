"""Credential handling for machine principals.

The wire contract below is SETTLED — it is read out of the running server, not
designed here. Source: lane 50A's credential-shape note, which cites
``shared/src/lib.rs:70`` for the header name and
``server/src/services/api_tokens/crypto.rs`` for the encoding.
"""

from __future__ import annotations

__all__ = [
    "CREDENTIAL_HEADER",
    "CREDENTIAL_MAX_LEN",
    "MACHINE_CREDENTIAL_PREFIX",
    "ORG_ID_HEADER",
    "TENANT_ID_HEADER",
    "assert_looks_like_machine_credential",
]

#: The header a machine credential is presented in
#: (``O11Y_ONE_API_KEY_HEADER_NAME``, o11y-api ``shared/src/lib.rs:70``).
#: ``x-api-key`` is accepted server-side as a fallback alias; this SDK always
#: sends the canonical name.
#:
#: Deliberately NOT ``authorization: Bearer`` — that path carries the browser
#: session JWT, and a machine credential presented there is rejected.
CREDENTIAL_HEADER = "x-o11y-key"

#: Org scoping header (``O11Y_ONE_ORG_ID_HEADER_NAME``).
ORG_ID_HEADER = "x-o11y-org-id"

#: Tenant scoping header (``O11Y_ONE_TENANT_ID_HEADER_NAME``).
TENANT_ID_HEADER = "x-o11y-tenant-id"

#: Prefix carried by machine-principal credentials (``APITokenType::prefix()``).
MACHINE_CREDENTIAL_PREFIX = "o11y_mach"

#: Server-side cap on the presented credential string (``API_TOKEN_MAX_LEN``).
CREDENTIAL_MAX_LEN = 128


def assert_looks_like_machine_credential(raw: str) -> str:
    """Validate a credential string locally and return it normalised.

    The credential's shape is ``o11y_mach.<selector>.<secret>`` where selector is
    16 random bytes and secret is 32 random bytes, both base64url without
    padding. The SDK does not parse past the prefix and must never try to:
    verification is Argon2id plus a blake3 constant-time compare on the server,
    and none of that is the client's business.

    This is NOT authentication. A string that passes here can still be revoked,
    expired, or unknown; only the server can say. What it catches is the
    overwhelmingly common class of mistake — an empty environment variable, a
    browser session token pasted into the wrong place, a value truncated by a
    copy-paste — before a network round trip turns it into an opaque
    UNAUTHENTICATED.

    Raises:
        ValueError: if the string cannot possibly be a machine credential.
    """
    # The server trims whitespace and strips one layer of surrounding quotes
    # (``normalize_api_token_input``) so a value pasted out of a shell still
    # works. We normalise the same way rather than relying on it.
    value = raw.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
        value = value[1:-1].strip()

    if not value:
        raise ValueError(
            "o11y credential is empty - set the credential environment variable "
            "or pass it explicitly"
        )
    if len(value) > CREDENTIAL_MAX_LEN:
        raise ValueError(
            f"o11y credential is {len(value)} bytes, over the "
            f"{CREDENTIAL_MAX_LEN}-byte server limit; this is not a valid credential"
        )
    if not value.startswith(f"{MACHINE_CREDENTIAL_PREFIX}."):
        raise ValueError(
            f'o11y credential does not start with "{MACHINE_CREDENTIAL_PREFIX}." - '
            "machine credentials do. If this is a browser session token it will "
            "not work here."
        )
    if len(value.split(".")) != 3:
        raise ValueError(
            "o11y credential is malformed: expected <prefix>.<selector>.<secret>, "
            "three dot-separated parts"
        )
    return value
