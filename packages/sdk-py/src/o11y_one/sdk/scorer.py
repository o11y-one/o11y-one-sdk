"""The ``score(input, context)`` contract a code scorer implements, as types.

The sandbox runs a code scorer's bundle under CPython with no network and no
third-party packages, so this SDK is not installed there: annotate under
``TYPE_CHECKING`` and the bundle still imports nothing but the standard
library::

    from __future__ import annotations

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from o11y_one.sdk.scorer import ScorerContext, ScorerInput, ScorerOutput


    def score(input: ScorerInput, context: ScorerContext) -> ScorerOutput:
        ok = input.get("candidate_output") == input.get("reference_output")
        return {"score": 1.0 if ok else 0.0, "verdict": "pass" if ok else "fail"}

What the harness enforces, so a scorer that type-checks against these is
refused only for its values: ``score`` in ``[0, 1]`` and finite, ``verdict``
``"pass"`` or ``"fail"``, ``label`` at most 256 bytes, ``explanation`` at most
4 KiB, at most 32 ``metrics`` whose names are at most 128 bytes, and nothing
else in the dict. Anything else ends the attempt as ``invalid_output``.
"""

# No `from __future__ import annotations`: TypedDict reads NotRequired only when evaluated.
from typing import Any, Literal, NotRequired, Protocol, TypedDict

__all__ = ["Scorer", "ScorerContext", "ScorerInput", "ScorerOutput"]


class ScorerInput(TypedDict, total=False):
    """The case fields the scorer reads, each the JSON the case holds.

    A field is present only when the scorer's ``input_fields`` name it (the
    first three by default) and the case has a value for it.
    """

    case_input: Any
    candidate_output: Any
    reference_output: Any
    correction: Any
    original_context: Any


class ScorerContext(TypedDict):
    """Fixed per job, and per publication for its repeatability trials, so a
    seeded scorer's retries and trials see the same values."""

    seed: int
    frozen_evaluation_time_unix_nanos: int


class ScorerOutput(TypedDict):
    score: float
    verdict: Literal["pass", "fail"]
    label: NotRequired[str]
    explanation: NotRequired[str]
    metrics: NotRequired[dict[str, float | str]]


class Scorer(Protocol):
    def __call__(self, input: ScorerInput, context: ScorerContext, /) -> ScorerOutput: ...
