"""Unit tests for the pre-wire validation layer. Pure functions, no transport."""

from __future__ import annotations

import pytest
from o11y_one.sdk.validation import (
    ValidationError,
    require_exactly_one,
    require_non_empty,
    require_non_empty_sequence,
    require_not_unspecified,
    require_valid_enum_choices,
)


def test_require_non_empty_accepts_and_returns_value() -> None:
    assert require_non_empty("hello", field="x") == "hello"


@pytest.mark.parametrize("value", [None, "", "   "])
def test_require_non_empty_rejects_blank(value: str | None) -> None:
    with pytest.raises(ValidationError, match="x: is required"):
        require_non_empty(value, field="x")


def test_require_not_unspecified_rejects_zero() -> None:
    with pytest.raises(ValidationError, match="kind: must not be the UNSPECIFIED"):
        require_not_unspecified(0, field="kind")


def test_require_not_unspecified_accepts_nonzero() -> None:
    assert require_not_unspecified(3, field="kind") == 3


def test_require_exactly_one_accepts_single_populated_field() -> None:
    assert require_exactly_one({"a": "x", "b": None}, oneof="a|b") == "a"


def test_require_exactly_one_rejects_neither_populated() -> None:
    with pytest.raises(ValidationError, match="got 0"):
        require_exactly_one({"a": None, "b": None}, oneof="a|b")


def test_require_exactly_one_rejects_both_populated() -> None:
    with pytest.raises(ValidationError, match="got 2"):
        require_exactly_one({"a": "x", "b": "y"}, oneof="a|b")


def test_require_non_empty_sequence_rejects_empty() -> None:
    with pytest.raises(ValidationError, match="outputs: must contain"):
        require_non_empty_sequence([], field="outputs")
    with pytest.raises(ValidationError):
        require_non_empty_sequence(None, field="outputs")


def test_require_non_empty_sequence_accepts_nonempty() -> None:
    assert require_non_empty_sequence([1, 2], field="outputs") == [1, 2]


def test_require_valid_enum_choices_rejects_unspecified_and_unknown() -> None:
    valid = frozenset({1, 2, 3})
    with pytest.raises(ValidationError, match="scopes: contains"):
        require_valid_enum_choices([1, 0], field="scopes", valid=valid)
    with pytest.raises(ValidationError, match="scopes: contains"):
        require_valid_enum_choices([1, 99], field="scopes", valid=valid)


def test_require_valid_enum_choices_accepts_known_nonzero() -> None:
    valid = frozenset({1, 2, 3})
    assert require_valid_enum_choices([1, 2], field="scopes", valid=valid) == [1, 2]
