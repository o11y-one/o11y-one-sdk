/**
 * `@o11y-one/sdk` — hand-written client layer over the generated `@o11y-one/api`.
 *
 * The foundation:
 *   - transport construction (client.ts)
 *   - credential injection and its local validation (auth.ts)
 *   - the failure taxonomy an SDK exists to render (errors.ts)
 *
 * The agentic-evaluation journey surface (evaluation.ts) binds the code-first
 * loop's verbs — identity, machine credentials, run submission, the
 * externally-executed lease loop, dataset drafts, annotations — as thin, typed,
 * validated wrappers. Its refusals are TYPED VALUES (refusals.ts) returned in a
 * `Result` (result.ts), not thrown-away errors; its inputs are guarded
 * synchronously (validate.ts) before a wire call. The generated client stays
 * reachable for any verb the surface has not lifted.
 */
export {
  O11yClient,
  createTransport,
  credentialInterceptor,
  type ClientOptions,
} from "./client.js";

export {
  assertLooksLikeMachineCredential,
  CREDENTIAL_HEADER,
  CREDENTIAL_MAX_LEN,
  MACHINE_CREDENTIAL_PREFIX,
  ORG_ID_HEADER,
  TENANT_ID_HEADER,
  type MachineCredential,
} from "./auth.js";

export {
  classify,
  MACHINE_SCOPES,
  type ClassifiedFailure,
  type FailureDisposition,
  type MachineScope,
} from "./errors.js";

// --- the journey surface ----------------------------------------------------

export {
  AgenticEvaluationClient,
  OneTimeCredential,
  scopesToCanonical,
  type CallerIdentity,
  type LeaseOutcome,
} from "./evaluation.js";

export {
  ok,
  err,
  isOk,
  isErr,
  unwrap,
  type Result,
  type Ok,
  type Err,
} from "./result.js";

export {
  ValidationError,
  requireNonEmpty,
  requireIdempotencyKey,
  requireExactlyOne,
  rejectUnspecified,
  requireWithinBytes,
  byteLength,
} from "./validate.js";

export {
  findDetail,
  toLeaseRefusal,
  toCaseAck,
  toLaunchRejection,
  toCaptureRefusal,
  toDatasetVersionRejection,
  toAnnotationRejection,
  toCursorResync,
  type RecoveryAction,
  type LeaseRefusal,
  type LeaseRefusalReason,
  type CaseAck,
  type CaseAckKind,
  type SubmissionOutcome,
  type LaunchRejection,
  type LaunchRejectionReason,
  type CaptureRefusal,
  type CaptureRefusalReason,
  type DatasetVersionRejection,
  type DatasetVersionRejectionReason,
  type AnnotationRejection,
  type AnnotationRejectionReason,
  type CursorResync,
  type CursorResyncReason,
} from "./refusals.js";
