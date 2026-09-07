/**
 * The typed-refusal vocabulary.
 *
 * The generated messages carry refusal *kinds* as numeric proto enums. A caller
 * branching on a bare number is a caller reading a magic constant, so this
 * module lifts each one to its WIRE ENUM MEMBER NAME — the SCREAMING_SNAKE
 * string the proto itself declares (`LEASE_EXPIRED`, `PREVIEW_MALFORMED`, …).
 * No name is invented here: the reverse map of the generated `enum` is the
 * single source, so this SDK and the Python SDK that mirrors it cannot drift
 * apart or drift from the server.
 *
 * Each refusal is a small, flat, discriminated record: a `type` naming the
 * refusal FAMILY (which verb refused), a `reason` naming the wire kind WITHIN
 * that family, the structured fields the server attached, and `raw` — the
 * untouched generated message — for the caller who needs a field this shape
 * did not lift.
 */
import { ConnectError } from "@connectrpc/connect";
import type { DescMessage, MessageShape } from "@bufbuild/protobuf";

import {
  ExternalLeaseRefusalKindV1,
  ExternalSubmissionAckKindV1,
  EvaluationLaunchRejectionKindV1,
  EvaluationCaptureRefusalKindV1,
  EvaluationDatasetVersionRejectionKindV1,
  EvaluationResyncReasonV1,
  PlatformAnnotationRejectionReasonV1,
  PlatformAnnotationKindV1,
  RecoveryActionV1,
  type ExternalLeaseRefusalV1,
  type EvaluationLaunchRejectionV1,
  type EvaluationCaptureRefusalV1,
  type EvaluationDatasetVersionRejectionV1,
  type PlatformAnnotationRejectionV1,
  type EvaluationCursorResyncV1,
  type ExternalCaseOutputAckV1,
} from "@o11y-one/api-agentic/o11y_one/agentic/v1/evaluation_pb";

/**
 * The member name of a numeric proto enum value, e.g.
 * `enumName(ExternalLeaseRefusalKindV1, 4)` → `"LEASE_EXPIRED"`. Unknown or
 * absent values (a discriminant added server-side after this SDK was built)
 * fold to `"UNSPECIFIED"` rather than a raw number, so a newer server never
 * makes an older client emit a bare integer.
 */
function enumName(enumObj: Record<number, string>, value: number): string {
  return enumObj[value] ?? "UNSPECIFIED";
}

/** The one remedial action the server named, as a wire enum member name. */
export type RecoveryAction =
  | "UNSPECIFIED"
  | "RETRY"
  | "RE_PREVIEW"
  | "EDIT_DEFINITION"
  | "WAIT"
  | "CONTACT_SUPPORT";

function recoveryName(value: RecoveryActionV1 | undefined): RecoveryAction {
  if (value === undefined) {
    return "UNSPECIFIED";
  }
  return enumName(RecoveryActionV1 as unknown as Record<number, string>, value) as RecoveryAction;
}

// ---------------------------------------------------------------------------
// External-execution loop: lease → heartbeat → submit → release.
// These refusals arrive ON A 200, as the optional `refusal` field of the
// response. `LEASE_NOT_HELD` is abandonment, `LEASE_EXPIRED` is expiry,
// `RENEWAL_BUDGET_EXHAUSTED` is budget exhaustion, `SCOPE_MISSING` is a token
// that lost its scope — the whole J8 recovery vocabulary, verbatim.
// ---------------------------------------------------------------------------

export type LeaseRefusalReason =
  | "UNSPECIFIED"
  | "RUN_NOT_EXECUTABLE"
  | "CANDIDATE_NOT_EXTERNALLY_EXECUTED"
  | "LEASE_NOT_HELD"
  | "LEASE_EXPIRED"
  | "RENEWAL_BUDGET_EXHAUSTED"
  | "BOUNDS_EXCEEDED"
  | "SCOPE_MISSING";

export interface LeaseRefusal {
  readonly type: "lease-refusal";
  readonly reason: LeaseRefusalReason;
  readonly message: string;
  /** Set on `SCOPE_MISSING`: the canonical scope the credential lacks. */
  readonly missingScope: string | undefined;
  readonly recovery: RecoveryAction;
  readonly raw: ExternalLeaseRefusalV1;
}

export function toLeaseRefusal(m: ExternalLeaseRefusalV1): LeaseRefusal {
  return {
    type: "lease-refusal",
    reason: enumName(
      ExternalLeaseRefusalKindV1 as unknown as Record<number, string>,
      m.kind,
    ) as LeaseRefusalReason,
    message: m.message,
    missingScope: m.missingScope,
    recovery: recoveryName(m.recovery),
    raw: m,
  };
}

// ---------------------------------------------------------------------------
// Per-case submission acks. A batch never fails whole for one bad case: each
// coordinate lands, is a duplicate, or is rejected — reported on its own line.
// ---------------------------------------------------------------------------

export type CaseAckKind = "UNSPECIFIED" | "ACCEPTED" | "ALREADY_SUBMITTED" | "REJECTED";

export interface CaseAck {
  readonly cohortKey: string;
  readonly candidateKey: string;
  readonly caseRevisionId: string;
  readonly trial: number;
  readonly kind: CaseAckKind;
  /** The frozen execution state the server sees this coordinate in. */
  readonly observedState: number;
  readonly raw: ExternalCaseOutputAckV1;
}

export function toCaseAck(m: ExternalCaseOutputAckV1): CaseAck {
  return {
    cohortKey: m.cohortKey,
    candidateKey: m.candidateKey,
    caseRevisionId: m.caseRevisionId,
    trial: m.trial,
    kind: enumName(
      ExternalSubmissionAckKindV1 as unknown as Record<number, string>,
      m.kind,
    ) as CaseAckKind,
    observedState: m.observedState,
    raw: m,
  };
}

/**
 * The partial-batch outcome of a `submitCaseOutputs`. This is not an error even
 * when `rejected` is non-empty: the accepted cases DID land, and the caller
 * resubmits only the rejected coordinates. `refusal`, when present, is a
 * WHOLE-request refusal (the fence was lost) and no per-case answer is
 * meaningful — the two are never both set.
 */
export interface SubmissionOutcome {
  readonly acceptedCount: number;
  readonly alreadySubmittedCount: number;
  readonly rejectedCount: number;
  readonly acks: readonly CaseAck[];
  readonly accepted: readonly CaseAck[];
  readonly alreadySubmitted: readonly CaseAck[];
  readonly rejected: readonly CaseAck[];
  readonly remainingLeasedCaseCount: number;
  /** Whole-request refusal; set only when the lease fence was lost. */
  readonly refusal: LeaseRefusal | undefined;
}

// ---------------------------------------------------------------------------
// Launch rejection. Arrives in `Status.details` on a FAILED_PRECONDITION, not
// on a 200 — the wrapper decodes the detail and folds it into an `err(...)`.
// ---------------------------------------------------------------------------

export type LaunchRejectionReason =
  | "UNSPECIFIED"
  | "PREVIEW_EXPIRED"
  | "PREVIEW_MALFORMED"
  | "DEFINITION_REVISION_MOVED"
  | "DEPENDENCY_VERSIONS_MOVED"
  | "CARDINALITY_MOVED"
  | "CAPABILITY_SET_MOVED"
  | "IDEMPOTENCY_KEY_REUSED";

export interface LaunchRejection {
  readonly type: "launch-rejection";
  readonly reason: LaunchRejectionReason;
  readonly expectedDigest: string;
  readonly observedDigest: string;
  /** Set on `IDEMPOTENCY_KEY_REUSED`: the run the key already named. */
  readonly existingEvaluationRunId: string | undefined;
  readonly recovery: RecoveryAction;
  readonly detail: string;
  readonly raw: EvaluationLaunchRejectionV1;
}

export function toLaunchRejection(m: EvaluationLaunchRejectionV1): LaunchRejection {
  return {
    type: "launch-rejection",
    reason: enumName(
      EvaluationLaunchRejectionKindV1 as unknown as Record<number, string>,
      m.kind,
    ) as LaunchRejectionReason,
    expectedDigest: m.expectedDigest,
    observedDigest: m.observedDigest,
    existingEvaluationRunId: m.existingEvaluationRunId,
    recovery: recoveryName(m.recovery),
    detail: m.detail,
    raw: m,
  };
}

// ---------------------------------------------------------------------------
// Capture refusal. Arrives in `Status.details` on the capture verb.
// ---------------------------------------------------------------------------

export type CaptureRefusalReason =
  | "UNSPECIFIED"
  | "SOURCE_NOT_FOUND"
  | "SOURCE_PLANE_NOT_SHIPPED"
  | "REQUIRED_FIELD_UNMAPPED"
  | "MAPPING_RESOLVED_NOTHING"
  | string;

export interface CaptureRefusal {
  readonly type: "capture-refusal";
  readonly reason: CaptureRefusalReason;
  readonly detail: string;
  readonly missingTargetPaths: readonly string[];
  readonly recovery: RecoveryAction;
  /** Set on `IDEMPOTENCY_KEY_REUSED`: the case the key already captured. */
  readonly existingProposedCaseId: string | undefined;
  readonly raw: EvaluationCaptureRefusalV1;
}

export function toCaptureRefusal(m: EvaluationCaptureRefusalV1): CaptureRefusal {
  return {
    type: "capture-refusal",
    reason: enumName(EvaluationCaptureRefusalKindV1 as unknown as Record<number, string>, m.kind),
    detail: m.detail,
    missingTargetPaths: m.missingTargetPaths,
    recovery: recoveryName(m.recovery),
    existingProposedCaseId: m.existingProposedCaseId,
    raw: m,
  };
}

// ---------------------------------------------------------------------------
// Dataset-version rejection. Arrives in `Status.details`.
// ---------------------------------------------------------------------------

export type DatasetVersionRejectionReason =
  | "UNSPECIFIED"
  | "COLLECTION_CAP_EXCEEDED"
  | "VERSION_CAP_ALL_PINNED"
  | "MALFORMED_JSONL_LINE"
  | "EMPTY_INGEST"
  | "INGEST_TOO_LARGE"
  | "DRAFT_NOT_FINALIZABLE"
  | "INGEST_BYTES_EXCEEDED"
  | "INGEST_CASE_COUNT_EXCEEDED"
  | "DRAFT_HAS_UNAPPROVED_CASES";

export interface DatasetVersionRejection {
  readonly type: "dataset-version-rejection";
  readonly reason: DatasetVersionRejectionReason;
  /** The server's stable `reason_code` string, carried alongside the kind. */
  readonly reasonCode: string;
  /** 1-based, set only on `MALFORMED_JSONL_LINE`. */
  readonly lineNumber: number | undefined;
  readonly observedCount: number;
  readonly maxCount: number;
  readonly detail: string;
  readonly recovery: RecoveryAction;
  readonly raw: EvaluationDatasetVersionRejectionV1;
}

export function toDatasetVersionRejection(
  m: EvaluationDatasetVersionRejectionV1,
): DatasetVersionRejection {
  return {
    type: "dataset-version-rejection",
    reason: enumName(
      EvaluationDatasetVersionRejectionKindV1 as unknown as Record<number, string>,
      m.kind,
    ) as DatasetVersionRejectionReason,
    reasonCode: m.reasonCode,
    lineNumber: m.lineNumber,
    observedCount: m.observedCount,
    maxCount: m.maxCount,
    detail: m.detail,
    recovery: recoveryName(m.recovery),
    raw: m,
  };
}

// ---------------------------------------------------------------------------
// Platform-annotation rejection. Arrives in `Status.details`.
// ---------------------------------------------------------------------------

export type AnnotationRejectionReason =
  | "UNSPECIFIED"
  | "KIND_UNKNOWN"
  | "TITLE_TOO_LARGE"
  | "ATTRIBUTE_TOO_LARGE"
  | "TOO_MANY_ATTRIBUTES"
  | "TOO_MANY_LINKS"
  | "LINK_REF_TOO_LARGE"
  | "RANGE_INVERTED"
  | "IDEMPOTENCY_KEY_REUSED"
  | "WINDOW_INVALID";

export interface AnnotationRejection {
  readonly type: "annotation-rejection";
  readonly reason: AnnotationRejectionReason;
  /** The field the server refused, when it named one. */
  readonly field: string | undefined;
  /** The bound that was exceeded, when the reason is a size/count cap. */
  readonly limitValue: bigint | undefined;
  /** On `KIND_UNKNOWN`: the kinds this server DOES support, as wire names. */
  readonly supportedKinds: readonly string[];
  readonly raw: PlatformAnnotationRejectionV1;
}

export function toAnnotationRejection(m: PlatformAnnotationRejectionV1): AnnotationRejection {
  return {
    type: "annotation-rejection",
    reason: enumName(
      PlatformAnnotationRejectionReasonV1 as unknown as Record<number, string>,
      m.reason,
    ) as AnnotationRejectionReason,
    field: m.field,
    limitValue: m.limitValue,
    supportedKinds: m.supportedKinds.map((k: number) =>
      enumName(PlatformAnnotationKindV1 as unknown as Record<number, string>, k),
    ),
    raw: m,
  };
}

// ---------------------------------------------------------------------------
// Cursor resync. NOT a refusal: a directive on a list response telling the
// caller its cursor cannot be honoured and it must restart the listing.
// ---------------------------------------------------------------------------

export type CursorResyncReason =
  | "UNSPECIFIED"
  | "SNAPSHOT_SUPERSEDED"
  | "FILTER_CHANGED"
  | "CURSOR_MALFORMED"
  | "BACKLOG_EXCEEDED";

export interface CursorResync {
  readonly type: "cursor-resync";
  readonly reason: CursorResyncReason;
  readonly raw: EvaluationCursorResyncV1;
}

export function toCursorResync(m: EvaluationCursorResyncV1): CursorResync {
  return {
    type: "cursor-resync",
    reason: enumName(
      EvaluationResyncReasonV1 as unknown as Record<number, string>,
      m.reason,
    ) as CursorResyncReason,
    raw: m,
  };
}

/**
 * Pull the first typed detail of a given schema off a thrown error.
 *
 * This is how a refusal that rides in `google.rpc.Status.details` (launch,
 * capture, dataset-version, annotation) is recovered: connect-es already
 * decodes `Status.details`, and `ConnectError.findDetails(schema)` hands back
 * the typed messages. A non-Connect error, or a Connect error with no such
 * detail, returns `undefined` and the caller rethrows.
 */
export function findDetail<Desc extends DescMessage>(
  error: unknown,
  schema: Desc,
): MessageShape<Desc> | undefined {
  if (!(error instanceof ConnectError)) {
    return undefined;
  }
  const details = error.findDetails(schema);
  return details.length > 0 ? details[0] : undefined;
}
