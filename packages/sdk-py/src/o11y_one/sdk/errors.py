"""The O11y One error taxonomy, as the SDK must render it.

From lane 50A's note: ``UNAUTHENTICATED`` vs ``PERMISSION_DENIED`` is the whole
reason this layer exists. "Your credential is invalid" and "your credential is
fine but this capability is not granted / not shipped" are different problems
with different fixes, and collapsing them into "auth error" is the failure mode
this module prevents.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from connectrpc.code import Code
from connectrpc.errors import ConnectError

__all__ = [
    "MACHINE_SCOPES",
    "ClassifiedFailure",
    "Disposition",
    "classify",
]

#: The five canonical machine-principal scope strings (50A, frozen taxonomy).
#: These are the exact strings that appear in the ``api_tokens.scopes`` array and
#: that a PERMISSION_DENIED message names.
MACHINE_SCOPES: tuple[str, ...] = (
    "eval:read",
    "run:execute",
    "dataset:write",
    "lease:submit",
    "platform-annotation:write",
)


class Disposition(Enum):
    """What a caller should DO about a failure."""

    #: Credential absent, malformed, unknown, expired, or revoked. Re-auth.
    #: Never retry — a retry cannot change the answer.
    REAUTHENTICATE = "reauthenticate"

    #: Credential valid but lacking the scope, or presented to a non-machine
    #: surface. Stop and surface the scope name.
    INSUFFICIENT_SCOPE = "insufficient-scope"

    #: Unknown scope discriminant on a write: SDK/server version skew.
    VERSION_SKEW = "version-skew"

    #: Auth backend down. Retryable with backoff — the server deliberately does
    #: not cache this outcome.
    RETRY_WITH_BACKOFF = "retry-with-backoff"

    #: Anything else. The SDK does not guess.
    UNCLASSIFIED = "unclassified"


@dataclass(frozen=True, slots=True)
class ClassifiedFailure:
    disposition: Disposition
    code: Code | None
    message: str
    #: For INSUFFICIENT_SCOPE, the canonical scope string the server named, when
    #: it named one.
    missing_scope: str | None
    retryable: bool


def classify(err: BaseException) -> ClassifiedFailure:
    """Map an exception onto the taxonomy above.

    Non-Connect exceptions pass through as UNCLASSIFIED rather than being forced
    into a bucket — a DNS failure is not an auth failure, and pretending
    otherwise sends people down the wrong path.
    """
    if not isinstance(err, ConnectError):
        return ClassifiedFailure(
            disposition=Disposition.UNCLASSIFIED,
            code=None,
            message=str(err),
            missing_scope=None,
            retryable=False,
        )

    message = err.message
    if err.code is Code.UNAUTHENTICATED:
        return ClassifiedFailure(Disposition.REAUTHENTICATE, err.code, message, None, False)
    if err.code is Code.PERMISSION_DENIED:
        # The server names the missing canonical scope when the cause is a scope
        # gap. When it names none, the cause is the other PERMISSION_DENIED
        # case: a machine credential presented to a non-machine surface.
        named = next((s for s in MACHINE_SCOPES if s in message), None)
        return ClassifiedFailure(Disposition.INSUFFICIENT_SCOPE, err.code, message, named, False)
    if err.code is Code.INVALID_ARGUMENT:
        return ClassifiedFailure(Disposition.VERSION_SKEW, err.code, message, None, False)
    if err.code is Code.UNAVAILABLE:
        return ClassifiedFailure(Disposition.RETRY_WITH_BACKOFF, err.code, message, None, True)
    return ClassifiedFailure(Disposition.UNCLASSIFIED, err.code, message, None, False)
