"""The refusal-on-a-200 shape, rendered as a Python-idiomatic typed union.

Several RPCs on ``AgenticEvaluationService`` never turn a business refusal into
an RPC error: a lease that expired, a run that is not executable, a scope the
caller's credential lacks — all of these come back as a normal ``200``-shaped
response with the success field ABSENT and a typed refusal sub-message present
instead (``LeaseEvaluationCasesResponse.refusal``, and siblings). See
DESIGN-AGENT-START-HERE.md §3 ("findDetails typed refusals", "refusals-on-a-200").

Forcing every caller to remember to check ``response.HasField("refusal")``
before touching the success field is exactly the class of mistake this module
exists to prevent. Every ergonomic method on :mod:`o11y_one.sdk.agentic` that
wraps such an RPC returns ``T | Refusal`` instead of the raw generated
response, so a caller either has the thing it asked for or a :class:`Refusal`
it can branch on — never both, never neither.

Python's structural ``match`` makes the branch read like the wire shape it
mirrors::

    match client.lease_cases(...):
        case Refusal(reason_code=code, field=field):
            ...
        case LeaseEvaluationCasesResponse() as ok:
            ...
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar

__all__ = ["Refusal"]

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class Refusal:
    """A typed business refusal returned on an otherwise-successful RPC.

    Attributes:
        reason_code: The server's stable discriminant for why the request was
            refused, lowercased and hyphenated (e.g. ``"lease-expired"``,
            ``"scope-missing"``). Derived from the wire enum's variant name so
            it survives an enum rename only in the sense that both sides regen
            from the same proto; it is NOT guaranteed stable across a proto
            change that renames the variant.
        field: The request field the refusal is about, when the server named
            one (e.g. ``"missing_scope"``, ``"preview_token"``). ``None`` when
            the refusal is about the request as a whole rather than one field.
        message: The server-authored, sanitized human-readable message. Safe
            to surface to an operator; never contains secret material.
        missing_scope: The canonical machine-principal scope string the server
            named, when the refusal was a scope gap. ``None`` otherwise.
    """

    reason_code: str
    message: str
    field: str | None = None
    missing_scope: str | None = None
