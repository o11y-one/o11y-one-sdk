"""Unit tests for the two refusal-delivery channels: bare-enum-name rendering
and typed-detail extraction from a thrown ``ConnectError``."""

from __future__ import annotations

from connectrpc.code import Code
from connectrpc.errors import ConnectError
from google.protobuf.any_pb2 import Any
from o11y_one.agentic.v1.evaluation_pb2 import (
    EvaluationLaunchRejectionKindV1,
    EvaluationLaunchRejectionV1,
    ExternalLeaseRefusalKindV1,
    PlatformAnnotationRejectionV1,
)
from o11y_one.sdk.recovery import bare_enum_name, find_error_detail


def test_bare_enum_name_strips_the_shared_type_prefix() -> None:
    kind = ExternalLeaseRefusalKindV1.EXTERNAL_LEASE_REFUSAL_KIND_V1_LEASE_EXPIRED
    assert bare_enum_name(ExternalLeaseRefusalKindV1, kind) == "LEASE_EXPIRED"


def test_bare_enum_name_covers_every_declared_member() -> None:
    expected = {
        "UNSPECIFIED",
        "RUN_NOT_EXECUTABLE",
        "CANDIDATE_NOT_EXTERNALLY_EXECUTED",
        "LEASE_NOT_HELD",
        "LEASE_EXPIRED",
        "RENEWAL_BUDGET_EXHAUSTED",
        "BOUNDS_EXCEEDED",
        "SCOPE_MISSING",
    }
    actual = {
        bare_enum_name(ExternalLeaseRefusalKindV1, v) for v in ExternalLeaseRefusalKindV1.values()
    }
    assert actual == expected


def test_bare_enum_name_folds_unrecognized_discriminant_to_unspecified() -> None:
    # A discriminant with no matching name at all (version skew: this SDK is
    # older than the server that sent it).
    assert bare_enum_name(ExternalLeaseRefusalKindV1, 999) == "UNSPECIFIED"


def test_find_error_detail_returns_none_when_no_matching_detail() -> None:
    err = ConnectError(Code.FAILED_PRECONDITION, "no detail here")
    assert find_error_detail(err, EvaluationLaunchRejectionV1) is None


def test_find_error_detail_returns_none_when_a_different_detail_type_is_present() -> None:
    other = PlatformAnnotationRejectionV1(reason=1)
    err = ConnectError(Code.FAILED_PRECONDITION, "wrong detail type", details=[other])
    assert find_error_detail(err, EvaluationLaunchRejectionV1) is None


def test_find_error_detail_unpacks_the_matching_typed_detail() -> None:
    rejection = EvaluationLaunchRejectionV1(
        kind=EvaluationLaunchRejectionKindV1.EVALUATION_LAUNCH_REJECTION_KIND_V1_PREVIEW_EXPIRED,
        detail="the preview token expired",
    )
    err = ConnectError(Code.FAILED_PRECONDITION, "launch rejected", details=[rejection])

    decoded = find_error_detail(err, EvaluationLaunchRejectionV1)

    assert decoded is not None
    assert decoded.detail == "the preview token expired"
    assert bare_enum_name(EvaluationLaunchRejectionKindV1, decoded.kind) == "PREVIEW_EXPIRED"


def test_find_error_detail_accepts_a_prepacked_any_too() -> None:
    rejection = EvaluationLaunchRejectionV1(detail="already-Any")
    packed = Any()
    packed.Pack(rejection, type_url_prefix="type.googleapis.com/")
    err = ConnectError(Code.FAILED_PRECONDITION, "launch rejected", details=[packed])

    decoded = find_error_detail(err, EvaluationLaunchRejectionV1)

    assert decoded is not None
    assert decoded.detail == "already-Any"
