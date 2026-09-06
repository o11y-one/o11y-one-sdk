"""Fast, synchronous, pre-wire input validation for the agentic surface.

Every check here runs BEFORE a request leaves the process. The contract is the
same one lane L1 (TypeScript) enforces on its side of the same wire messages:
required fields, mutually exclusive oneofs, and selector shape. None of this
duplicates server-side validation — the server still checks everything, and
still wins on any disagreement — it only turns the common mistakes into an
immediate, actionable :class:`ValidationError` instead of a round trip that
comes back ``INVALID_ARGUMENT`` a network hop later.

What this module deliberately does NOT do: invent numeric byte/length caps
that are not written down anywhere reachable from this repo. The vendored
proto (``proto/o11y_one/agentic/v1/evaluation.proto``) names several bounds by
symbol only (``MAX_IDEMPOTENCY_KEY_LEN``, ``max_output_bytes``,
``max_preview_field_bytes``, ...) without carrying their numeric values across
the wire or into the generated stubs — those constants live server-side. A
client-side cap invented here would either be wrong (drift from the real
value) or a lie (a number nobody asked for). See ``l2-notes.md`` for the full
accounting of which caps this module enforces and which it cannot.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
from typing import Any

__all__ = ["ValidationError", "require_exactly_one", "require_non_empty", "require_not_unspecified"]


class ValidationError(ValueError):
    """A request would fail server-side validation; raised before the wire call.

    Attributes:
        field: The request field that failed validation.
    """

    def __init__(self, field: str, message: str) -> None:
        self.field = field
        super().__init__(f"{field}: {message}")


def require_non_empty(value: str | None, *, field: str) -> str:
    """A required string field must be present and non-blank.

    Returns the value unchanged (after confirming it) so call sites can do
    ``x = require_non_empty(x, field="...")`` inline.
    """
    if value is None or not value.strip():
        raise ValidationError(field, "is required and must not be empty")
    return value


def require_not_unspecified(value: int, *, field: str, unspecified: int = 0) -> int:
    """Reject the zero-value (``*_UNSPECIFIED``) discriminant on a required enum.

    An unspecified discriminant sent over the wire is ``INVALID_ARGUMENT``
    server-side (0a §6.4, as the vendored proto puts it for
    ``CreateMachinePrincipalRequest.scopes``). Catching it here turns that into
    an immediate, local error with the field name attached.
    """
    if value == unspecified:
        raise ValidationError(field, "must not be the UNSPECIFIED discriminant")
    return value


def require_exactly_one(fields: Mapping[str, Any], *, oneof: str) -> str:
    """Exactly one of ``fields`` (name -> value) must be truthy.

    Used for proto ``oneof`` groups this SDK must not let a caller straddle or
    skip client-side — e.g. ``ExternalCaseOutputV1.result``
    (``output_payload_json`` XOR ``failure``): a case output that is neither a
    payload nor a failure, or claims to be both, is not a case the server can
    make sense of, and there is no reason to make it ask.

    Returns the name of the populated field.
    """
    present = [name for name, value in fields.items() if value is not None]
    if len(present) != 1:
        names = ", ".join(fields)
        got = ", ".join(present) or "none"
        message = f"exactly one of [{names}] is required, got {len(present)} ({got})"
        raise ValidationError(oneof, message)
    return present[0]


def require_non_empty_sequence(values: Sequence[Any] | None, *, field: str) -> Sequence[Any]:
    """A required repeated field must carry at least one element.

    Used for batch submissions (``SubmitEvaluationCaseOutputsRequest.outputs``)
    where an empty batch is a caller mistake, not a legitimate no-op — the RPC
    has no other way to say "I meant to submit zero cases".
    """
    if not values:
        raise ValidationError(field, "must contain at least one element")
    return values


def require_valid_enum_choices(
    values: Iterable[int], *, field: str, valid: frozenset[int], unspecified: int = 0
) -> list[int]:
    """Every element of a repeated enum field must be a known, non-zero discriminant.

    Catches the same "unknown discriminant is a version-skew bug, not a
    request the server should have to parse before rejecting" class of mistake
    as :func:`require_not_unspecified`, for repeated fields (e.g.
    ``CreateMachinePrincipalRequest.scopes``).
    """
    result = list(values)
    for value in result:
        if value == unspecified or value not in valid:
            raise ValidationError(
                field, f"contains an unknown or UNSPECIFIED discriminant: {value!r}"
            )
    return result
