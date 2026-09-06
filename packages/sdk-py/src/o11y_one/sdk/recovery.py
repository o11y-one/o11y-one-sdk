"""The two refusal-delivery channels ``AgenticEvaluationService`` uses, and the
one discriminant convention both channels render through.

Per DESIGN-AGENT-START-HERE.md §3 and lane L1's notes (TypeScript, same wire):
a business refusal on this surface arrives one of two ways —

1. **On an otherwise-successful response** (a ``200``-shaped message with a
   ``refusal``/``rejection`` sub-message populated instead of the success
   field) — the externally-executed lease loop
   (``LeaseEvaluationCasesResponse.refusal`` and siblings). Handled directly
   in :mod:`o11y_one.sdk.agentic` via ``HasField``.
2. **As a typed detail on a thrown ``ConnectError``**
   (``google.rpc.Status.details``, a ``google.protobuf.Any`` the server packs
   a specific rejection message into) — run launch (``EvaluationLaunchRejectionV1``),
   dataset case capture (``EvaluationCaptureRefusalV1``), dataset version
   publish (``EvaluationDatasetVersionRejectionV1``), and platform annotation
   recording (``PlatformAnnotationRejectionV1``). :func:`find_error_detail` is
   this module's equivalent of connect-es's ``ConnectError.findDetails`` /
   lane L1's ``findDetail`` helper.

**Discriminant convention (matches lane L1 exactly — this is the wire
contract between the two SDKs, not a per-language choice):** a
:class:`~o11y_one.sdk.results.Refusal.reason_code` is always the wire enum
member's name with its own type's common prefix stripped — e.g.
``ExternalLeaseRefusalKindV1`` value
``EXTERNAL_LEASE_REFUSAL_KIND_V1_LEASE_EXPIRED`` renders as ``"LEASE_EXPIRED"``
— derived mechanically via :func:`bare_enum_name`, never a hand-picked label.
An unrecognized discriminant (version skew: the SDK is older than the server)
folds to ``"UNSPECIFIED"`` rather than a bare int, exactly as lane L1 does.

This module deliberately does NOT introduce its own taxonomy for the
externally-executed lease's five illustrative recovery states named in the
task brief (lease-expiry / abandonment / budget-exhaustion / indeterminacy /
token-revocation): lane L1 checked and none of the wire enums carry a
five-state cut that matches those names, so it rendered the seven REAL
``ExternalLeaseRefusalKindV1`` variants verbatim instead
(``RUN_NOT_EXECUTABLE``, ``CANDIDATE_NOT_EXTERNALLY_EXECUTED``,
``LEASE_NOT_HELD``, ``LEASE_EXPIRED``, ``RENEWAL_BUDGET_EXHAUSTED``,
``BOUNDS_EXCEEDED``, ``SCOPE_MISSING``). This module follows that resolution
rather than the task brief's illustrative names, because "same names L1 uses"
and "the illustrative five" turned out to be mutually exclusive once L1 read
the proto, and cross-SDK parity on the wire-facing string wins. See
``l2-notes.md`` for the full accounting, including how ``token-revocation``
(a credential problem, not a lease problem) is instead reported by
:func:`o11y_one.sdk.errors.classify` returning ``Disposition.REAUTHENTICATE``,
and how ``indeterminacy`` (a submit whose outcome is unknown after a transport
error) has no refusal message to decode at all — it is a ``ConnectError``
with no matching Any packed into it, and the caller's only correct move is
"retry with the same idempotency key and reconcile against
``already_submitted_count``", not a discriminant this module can name.
"""

from __future__ import annotations

from typing import TypeVar

from connectrpc.errors import ConnectError
from google.protobuf import message as _message
from google.protobuf.internal.enum_type_wrapper import EnumTypeWrapper

__all__ = ["bare_enum_name", "find_error_detail"]

_M = TypeVar("_M", bound=_message.Message)


def bare_enum_name(enum_type: EnumTypeWrapper, value: int) -> str:
    """The wire enum member's name with its type's own common prefix stripped.

    ``enum_type`` is the generated module-level ``EnumTypeWrapper`` (e.g.
    ``ExternalLeaseRefusalKindV1``). The prefix is computed as the longest
    common prefix across ALL of the enum's member names (trimmed back to the
    last underscore) rather than derived from the type's Python class name —
    this is exact by construction (every proto enum's ``_UNSPECIFIED`` member
    alone guarantees a shared prefix) and needs no CamelCase-to-SNAKE guess
    that could drift from how a given proto happens to be named.

    An unrecognized discriminant — an int with no matching name, the version
    skew case where this SDK is older than the server that sent it — folds to
    ``"UNSPECIFIED"``, matching lane L1's convention exactly.
    """
    names = list(enum_type.keys())
    prefix = _common_prefix(names)
    try:
        name = enum_type.Name(value)
    except ValueError:
        return "UNSPECIFIED"
    return name[len(prefix) :] if prefix and name.startswith(prefix) else name


def _common_prefix(names: list[str]) -> str:
    if not names:
        return ""
    prefix = names[0]
    for name in names[1:]:
        while not name.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    cut = prefix.rfind("_")
    return prefix[: cut + 1] if cut != -1 else ""


def find_error_detail(err: ConnectError, message_cls: type[_M]) -> _M | None:
    """Look for a typed detail of type ``message_cls`` packed into ``err``.

    Returns ``None`` when no detail of that type is present — the caller
    should then treat ``err`` as an ordinary transport error (classify it with
    :func:`o11y_one.sdk.errors.classify` and re-raise or handle accordingly),
    never assume absence means success.
    """
    for any_detail in err.details:
        if any_detail.Is(message_cls.DESCRIPTOR):
            decoded = message_cls()
            any_detail.Unpack(decoded)
            return decoded
    return None
