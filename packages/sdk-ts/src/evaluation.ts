/**
 * The agentic-evaluation journey surface: thin, typed, validated wrappers over
 * the generated `AgenticEvaluationService` client.
 *
 * Every method here is one of two things and nothing else:
 *   - a request SHAPED and VALIDATED before it leaves (validate.ts), or
 *   - a response whose refusal is DECODED to a typed value (refusals.ts) rather
 *     than thrown away.
 *
 * No server logic is reimplemented. The backend does the work; this class binds
 * to its verbs, guards their inputs, and names their outcomes. The generated
 * client is reachable as `.raw` for any verb this surface has not lifted.
 */
import type { Client } from "@connectrpc/connect";
import { timestampFromDate } from "@bufbuild/protobuf/wkt";
import type { Timestamp } from "@bufbuild/protobuf/wkt";

import {
  AgenticEvaluationService,
  MachinePrincipalScopeV1,
  PlatformAnnotationKindV1,
  EvaluationLaunchRejectionV1Schema,
  EvaluationCaptureRefusalV1Schema,
  EvaluationDatasetVersionRejectionV1Schema,
  PlatformAnnotationRejectionV1Schema,
  type CreateEvaluationRunResponse,
  type PreviewEvaluationRunResponse,
  type GetCallerPrincipalResponse,
  type MachinePrincipalV1,
  type MachinePrincipalWithCredentialsV1,
  type MachineCredentialV1,
  type ExternalCaseLeaseV1,
  type ExternalCaseOutputV1,
  type LeasedEvaluationCaseV1,
  type CreateEvaluationDatasetVersionResponse,
  type CaptureEvaluationCaseResponse,
  type PublishDatasetCaseDraftsResponse,
  type RecordPlatformAnnotationResponse,
  type PlatformAnnotationV1,
  type PlatformAnnotationAttributeV1,
  type PlatformAnnotationLinkV1,
  type EvaluationCaptureSpanSourceV1,
  type EvaluationCaptureCellSourceV1,
  type DatasetFieldMappingV1,
} from "@o11y-one/api/o11y_one/agentic/v1/evaluation_pb";

import type { O11yClient } from "./client.js";
import type { MachineScope } from "./errors.js";
import { ok, err, type Result } from "./result.js";
import {
  findDetail,
  toLaunchRejection,
  toCaptureRefusal,
  toDatasetVersionRejection,
  toAnnotationRejection,
  toLeaseRefusal,
  toCaseAck,
  toCursorResync,
  type LaunchRejection,
  type CaptureRefusal,
  type DatasetVersionRejection,
  type AnnotationRejection,
  type LeaseRefusal,
  type CursorResync,
  type SubmissionOutcome,
  type CaseAck,
} from "./refusals.js";
import {
  requireNonEmpty,
  requireIdempotencyKey,
  requireExactlyOne,
  rejectUnspecified,
} from "./validate.js";

// --- scope vocabulary bridge ------------------------------------------------
// The five canonical scope strings (errors.ts, frozen taxonomy) <-> the proto's
// numeric MachinePrincipalScopeV1. Callers speak strings; the wire speaks the
// enum; neither leaks into the other.

const SCOPE_TO_ENUM: Record<MachineScope, MachinePrincipalScopeV1> = {
  "eval:read": MachinePrincipalScopeV1.EVAL_READ,
  "run:execute": MachinePrincipalScopeV1.RUN_EXECUTE,
  "dataset:write": MachinePrincipalScopeV1.DATASET_WRITE,
  "lease:submit": MachinePrincipalScopeV1.LEASE_SUBMIT,
  "platform-annotation:write": MachinePrincipalScopeV1.PLATFORM_ANNOTATION_WRITE,
};

const ENUM_TO_SCOPE: Partial<Record<number, MachineScope>> = {
  [MachinePrincipalScopeV1.EVAL_READ]: "eval:read",
  [MachinePrincipalScopeV1.RUN_EXECUTE]: "run:execute",
  [MachinePrincipalScopeV1.DATASET_WRITE]: "dataset:write",
  [MachinePrincipalScopeV1.LEASE_SUBMIT]: "lease:submit",
  [MachinePrincipalScopeV1.PLATFORM_ANNOTATION_WRITE]: "platform-annotation:write",
};

/** Canonical scope strings for a set of wire discriminants; UNSPECIFIED drops. */
export function scopesToCanonical(values: readonly number[]): MachineScope[] {
  const out: MachineScope[] = [];
  for (const v of values) {
    const s = ENUM_TO_SCOPE[v];
    if (s !== undefined) {
      out.push(s);
    }
  }
  return out;
}

// --- one-time credential material -------------------------------------------

/**
 * The plaintext credential returned exactly once by `createMachineCredential`.
 *
 * It is a DISTINCT type the caller must consume deliberately: `reveal()` hands
 * over the string, and every accidental-logging path — `toString`,
 * `toJSON`, Node's `util.inspect` — returns a redaction instead. The server
 * keeps no read-back copy, so this object is the only place the material ever
 * exists; the redaction is there so a stray `console.log(result)` cannot leak
 * it into a CI log.
 */
export class OneTimeCredential {
  readonly #plaintext: string;
  /** The credential-id this token belongs to, safe to log. */
  readonly credentialId: string;

  constructor(plaintext: string, credentialId: string) {
    this.#plaintext = plaintext;
    this.credentialId = credentialId;
  }

  /** Hand over the plaintext. Store it in your secret manager; never log it. */
  reveal(): string {
    return this.#plaintext;
  }

  toString(): string {
    return "[o11y one-time credential — redacted; call reveal()]";
  }

  toJSON(): string {
    return "[o11y one-time credential — redacted]";
  }

  [Symbol.for("nodejs.util.inspect.custom")](): string {
    return this.toString();
  }
}

// --- typed views ------------------------------------------------------------

/** Who the credential authenticates as, and what it may do — before any run. */
export interface CallerIdentity {
  readonly tenantId: string;
  readonly orgId: string;
  /** Absent for a browser session; present for a machine credential. */
  readonly machinePrincipalId: string | undefined;
  /** The credential id that authorized this request; absent for a session. */
  readonly credentialId: string | undefined;
  /** The credential's scopes, as canonical strings. */
  readonly scopes: readonly MachineScope[];
  /** True when the credential carries `scope`. The pre-run gate `doctor` needs. */
  readonly hasScope: (scope: MachineScope) => boolean;
  readonly raw: GetCallerPrincipalResponse;
}

/** The outcome of a lease attempt that was not refused. */
export interface LeaseOutcome {
  /** The fenced hold, or absent when nothing was claimable. */
  readonly lease: ExternalCaseLeaseV1 | undefined;
  readonly cases: readonly LeasedEvaluationCaseV1[];
  readonly remainingUnleasedCaseCount: number;
  /**
   * True when the lease is absent AND nothing remains: the honest "you are
   * done" answer, distinct from "held by another runtime" (lease absent,
   * remaining > 0).
   */
  readonly exhausted: boolean;
}

// --- the client -------------------------------------------------------------

export class AgenticEvaluationClient {
  readonly raw: Client<typeof AgenticEvaluationService>;

  constructor(client: O11yClient) {
    this.raw = client.service(AgenticEvaluationService);
  }

  // -- 1. identity ----------------------------------------------------------

  /**
   * Answer "is my credential valid, and which scopes does it carry?" BEFORE a
   * run. An UNAUTHENTICATED / PERMISSION_DENIED here is a thrown `ConnectError`
   * the caller renders with `classify()`; a success carries the scope set that
   * turns a minute-40 failure into a minute-0 one.
   */
  async whoami(): Promise<CallerIdentity> {
    const res = await this.raw.getCallerPrincipal({});
    const scopes = scopesToCanonical(res.machinePrincipal?.scopes ?? []);
    const scopeSet = new Set<MachineScope>(scopes);
    return {
      tenantId: res.tenantId,
      orgId: res.orgId,
      machinePrincipalId: res.machinePrincipal?.machinePrincipalId,
      credentialId: res.credential?.credentialId,
      scopes,
      hasScope: (scope) => scopeSet.has(scope),
      raw: res,
    };
  }

  // -- 2. machine credentials ----------------------------------------------

  async createMachinePrincipal(args: {
    displayName: string;
    description?: string;
    scopes: readonly MachineScope[];
  }): Promise<MachinePrincipalV1> {
    requireNonEmpty("displayName", args.displayName);
    const scopes = args.scopes.map((s) => SCOPE_TO_ENUM[s]);
    rejectUnspecified("scopes", scopes);
    const res = await this.raw.createMachinePrincipal({
      displayName: args.displayName,
      ...(args.description !== undefined ? { description: args.description } : {}),
      scopes,
    });
    if (res.principal === undefined) {
      throw new Error("createMachinePrincipal: server returned no principal");
    }
    return res.principal;
  }

  async listMachinePrincipals(args?: {
    pageSize?: number;
    pageToken?: string;
  }): Promise<{ principals: MachinePrincipalWithCredentialsV1[]; nextPageToken: string | undefined }> {
    const res = await this.raw.listMachinePrincipals({
      ...(args?.pageSize !== undefined ? { pageSize: args.pageSize } : {}),
      ...(args?.pageToken !== undefined ? { pageToken: args.pageToken } : {}),
    });
    return { principals: res.principals, nextPageToken: res.nextPageToken };
  }

  /**
   * Mint a credential. The plaintext comes back once, wrapped in a
   * {@link OneTimeCredential} the caller must `reveal()` to read and can never
   * accidentally log.
   */
  async createMachineCredential(args: {
    machinePrincipalId: string;
    description?: string;
    expiresAt?: Date;
  }): Promise<{ credential: MachineCredentialV1; token: OneTimeCredential }> {
    requireNonEmpty("machinePrincipalId", args.machinePrincipalId);
    const res = await this.raw.createMachineCredential({
      machinePrincipalId: args.machinePrincipalId,
      ...(args.description !== undefined ? { description: args.description } : {}),
      ...(args.expiresAt !== undefined ? { expiresAt: timestampFromDate(args.expiresAt) } : {}),
    });
    if (res.credential === undefined) {
      throw new Error("createMachineCredential: server returned no credential metadata");
    }
    return {
      credential: res.credential,
      token: new OneTimeCredential(res.plaintextTokenOnce, res.credential.credentialId),
    };
  }

  async revokeMachineCredential(args: {
    credentialId: string;
    revokeReason?: string;
  }): Promise<MachineCredentialV1> {
    requireNonEmpty("credentialId", args.credentialId);
    const res = await this.raw.revokeMachineCredential({
      credentialId: args.credentialId,
      ...(args.revokeReason !== undefined ? { revokeReason: args.revokeReason } : {}),
    });
    if (res.credential === undefined) {
      throw new Error("revokeMachineCredential: server returned no credential");
    }
    return res.credential;
  }

  async revokeMachinePrincipal(args: {
    machinePrincipalId: string;
    revokeReason?: string;
  }): Promise<{ principal: MachinePrincipalV1; revokedCredentials: MachineCredentialV1[] }> {
    requireNonEmpty("machinePrincipalId", args.machinePrincipalId);
    const res = await this.raw.revokeMachinePrincipal({
      machinePrincipalId: args.machinePrincipalId,
      ...(args.revokeReason !== undefined ? { revokeReason: args.revokeReason } : {}),
    });
    if (res.principal === undefined) {
      throw new Error("revokeMachinePrincipal: server returned no principal");
    }
    return { principal: res.principal, revokedCredentials: res.revokedCredentials };
  }

  // -- 3. run submission ----------------------------------------------------

  /**
   * Resolve and freeze what a launch WOULD do: the preview token, its digest
   * and expiry, the frozen manifest, the estimates and any blockers. Launch
   * from the token this returns.
   *
   * NOTE: the wire contract launches from a definition (+ optional revision)
   * through a preview token; there is no inline-draft launch path in the proto
   * at this capability. See l1-notes.
   */
  async previewRun(args: {
    definitionId: string;
    revisionId?: string;
  }): Promise<PreviewEvaluationRunResponse> {
    requireNonEmpty("definitionId", args.definitionId);
    return await this.raw.previewEvaluationRun({
      definitionId: args.definitionId,
      ...(args.revisionId !== undefined ? { revisionId: args.revisionId } : {}),
    });
  }

  /**
   * Launch a run from an accepted preview token. Returns `err(LaunchRejection)`
   * when a binding moved under the token (the refusal rides in `Status.details`
   * on a FAILED_PRECONDITION); any other transport error rethrows.
   */
  async launchRun(args: {
    definitionId: string;
    idempotencyKey: string;
    previewToken: string;
  }): Promise<Result<CreateEvaluationRunResponse, LaunchRejection>> {
    requireNonEmpty("definitionId", args.definitionId);
    requireIdempotencyKey("idempotencyKey", args.idempotencyKey);
    requireNonEmpty("previewToken", args.previewToken);
    try {
      const res = await this.raw.createEvaluationRun({
        definitionId: args.definitionId,
        idempotencyKey: args.idempotencyKey,
        previewToken: args.previewToken,
      });
      return ok(res);
    } catch (e) {
      const detail = findDetail(e, EvaluationLaunchRejectionV1Schema);
      if (detail !== undefined) {
        return err(toLaunchRejection(detail));
      }
      throw e;
    }
  }

  // -- 4/5. externally-executed loop: lease -> renew -> submit -> release ----

  /**
   * Claim a bounded set of prepared cases. `err(LeaseRefusal)` when the server
   * refuses on a 200 (`SCOPE_MISSING`, `RUN_NOT_EXECUTABLE`, …). `ok` otherwise
   * — and an `ok` with no lease is not a failure: check `exhausted`.
   */
  async leaseCases(args: {
    evaluationRunId: string;
    candidateKey: string;
    runtimeKey: string;
    maxCases?: number;
    leaseSeconds?: number;
  }): Promise<Result<LeaseOutcome, LeaseRefusal>> {
    requireNonEmpty("evaluationRunId", args.evaluationRunId);
    requireNonEmpty("candidateKey", args.candidateKey);
    requireNonEmpty("runtimeKey", args.runtimeKey);
    const res = await this.raw.leaseEvaluationCases({
      evaluationRunId: args.evaluationRunId,
      candidateKey: args.candidateKey,
      runtimeKey: args.runtimeKey,
      maxCases: args.maxCases ?? 0,
      leaseSeconds: args.leaseSeconds ?? 0,
    });
    if (res.refusal !== undefined) {
      return err(toLeaseRefusal(res.refusal));
    }
    return ok({
      lease: res.lease,
      cases: res.cases,
      remainingUnleasedCaseCount: res.remainingUnleasedCaseCount,
      exhausted: res.lease === undefined && res.remainingUnleasedCaseCount === 0,
    });
  }

  /** Heartbeat a held lease. `err(LeaseRefusal)` when the fence was lost. */
  async renewLease(args: {
    evaluationRunId: string;
    leaseId: string;
    leaseToken: string;
    leaseSeconds?: number;
  }): Promise<Result<ExternalCaseLeaseV1, LeaseRefusal>> {
    requireNonEmpty("evaluationRunId", args.evaluationRunId);
    requireNonEmpty("leaseId", args.leaseId);
    requireNonEmpty("leaseToken", args.leaseToken);
    const res = await this.raw.renewEvaluationCaseLease({
      evaluationRunId: args.evaluationRunId,
      leaseId: args.leaseId,
      leaseToken: args.leaseToken,
      leaseSeconds: args.leaseSeconds ?? 0,
    });
    if (res.refusal !== undefined) {
      return err(toLeaseRefusal(res.refusal));
    }
    if (res.lease === undefined) {
      throw new Error("renewEvaluationCaseLease: neither lease nor refusal was returned");
    }
    return ok(res.lease);
  }

  /**
   * Submit a batch of case outputs — the recorded-output upload and the
   * external-loop submit are the same verb. Returns a {@link SubmissionOutcome}
   * that partitions the batch: which coordinates landed, which were duplicates,
   * which were rejected and why — never an all-or-nothing throw. A whole-request
   * refusal (fence lost) appears as `outcome.refusal`, with no per-case answers.
   *
   * Idempotent by lease identity and coordinate: a resubmit of the same batch
   * reports the landed cases as `ALREADY_SUBMITTED`.
   */
  async submitCaseOutputs(args: {
    evaluationRunId: string;
    leaseId: string;
    leaseToken: string;
    outputs: readonly ExternalCaseOutputV1[];
    idempotencyKey: string;
  }): Promise<SubmissionOutcome> {
    requireNonEmpty("evaluationRunId", args.evaluationRunId);
    requireNonEmpty("leaseId", args.leaseId);
    requireNonEmpty("leaseToken", args.leaseToken);
    requireIdempotencyKey("idempotencyKey", args.idempotencyKey);
    if (args.outputs.length === 0) {
      requireNonEmpty("outputs", "");
    }
    const res = await this.raw.submitEvaluationCaseOutputs({
      evaluationRunId: args.evaluationRunId,
      leaseId: args.leaseId,
      leaseToken: args.leaseToken,
      outputs: args.outputs as ExternalCaseOutputV1[],
      idempotencyKey: args.idempotencyKey,
    });
    const acks: CaseAck[] = res.acks.map(toCaseAck);
    return {
      acceptedCount: res.acceptedCount,
      alreadySubmittedCount: res.alreadySubmittedCount,
      rejectedCount: res.rejectedCount,
      acks,
      accepted: acks.filter((a) => a.kind === "ACCEPTED"),
      alreadySubmitted: acks.filter((a) => a.kind === "ALREADY_SUBMITTED"),
      rejected: acks.filter((a) => a.kind === "REJECTED"),
      remainingLeasedCaseCount: res.remainingLeasedCaseCount,
      refusal: res.refusal !== undefined ? toLeaseRefusal(res.refusal) : undefined,
    };
  }

  /** Release a held lease early. `err(LeaseRefusal)` when the fence was lost. */
  async releaseLease(args: {
    evaluationRunId: string;
    leaseId: string;
    leaseToken: string;
  }): Promise<Result<number, LeaseRefusal>> {
    requireNonEmpty("evaluationRunId", args.evaluationRunId);
    requireNonEmpty("leaseId", args.leaseId);
    requireNonEmpty("leaseToken", args.leaseToken);
    const res = await this.raw.releaseEvaluationCaseLease({
      evaluationRunId: args.evaluationRunId,
      leaseId: args.leaseId,
      leaseToken: args.leaseToken,
    });
    if (res.refusal !== undefined) {
      return err(toLeaseRefusal(res.refusal));
    }
    return ok(res.releasedCaseCount);
  }

  // -- 6. dataset drafts: create / append / publish -------------------------

  /**
   * Create a dataset version from EXACTLY ONE ingest source: raw JSONL bytes, or
   * a finalized capture draft by id. `err(DatasetVersionRejection)` on a typed
   * ingest refusal (rides in `Status.details`); any other error rethrows.
   */
  async createDatasetVersion(args: {
    datasetCollectionId?: string;
    collectionName?: string;
    label?: string;
    jsonl?: Uint8Array;
    draftId?: string;
    recordedOutputFieldPath?: string;
    expectedDraftVersion?: bigint;
    idempotencyKey: string;
  }): Promise<Result<CreateEvaluationDatasetVersionResponse, DatasetVersionRejection>> {
    requireIdempotencyKey("idempotencyKey", args.idempotencyKey);
    requireExactlyOne("ingest", [
      { name: "jsonl", present: args.jsonl !== undefined },
      { name: "draftId", present: args.draftId !== undefined },
    ]);
    const ingest =
      args.jsonl !== undefined
        ? ({ case: "jsonl", value: args.jsonl } as const)
        : ({ case: "draftId", value: args.draftId as string } as const);
    try {
      const res = await this.raw.createEvaluationDatasetVersion({
        ...(args.datasetCollectionId !== undefined
          ? { datasetCollectionId: args.datasetCollectionId }
          : {}),
        ...(args.collectionName !== undefined ? { collectionName: args.collectionName } : {}),
        ...(args.label !== undefined ? { label: args.label } : {}),
        ingest,
        ...(args.recordedOutputFieldPath !== undefined
          ? { recordedOutputFieldPath: args.recordedOutputFieldPath }
          : {}),
        ...(args.expectedDraftVersion !== undefined
          ? { expectedDraftVersion: args.expectedDraftVersion }
          : {}),
        idempotencyKey: args.idempotencyKey,
      });
      return ok(res);
    } catch (e) {
      const detail = findDetail(e, EvaluationDatasetVersionRejectionV1Schema);
      if (detail !== undefined) {
        return err(toDatasetVersionRejection(detail));
      }
      throw e;
    }
  }

  /**
   * Append one case to a collection's open draft, from EXACTLY ONE source: a
   * trace span or a matrix cell. `err(CaptureRefusal)` on a typed capture
   * refusal (rides in `Status.details`).
   */
  async captureCase(args: {
    datasetCollectionId: string;
    draftId?: string;
    span?: EvaluationCaptureSpanSourceV1;
    cell?: EvaluationCaptureCellSourceV1;
    fieldMappings?: readonly DatasetFieldMappingV1[];
    recordedOutputFieldPath?: string;
    baseDatasetVersionId?: string;
    expectedContentDigest?: string;
    idempotencyKey: string;
  }): Promise<Result<CaptureEvaluationCaseResponse, CaptureRefusal>> {
    requireNonEmpty("datasetCollectionId", args.datasetCollectionId);
    requireIdempotencyKey("idempotencyKey", args.idempotencyKey);
    requireExactlyOne("source", [
      { name: "span", present: args.span !== undefined },
      { name: "cell", present: args.cell !== undefined },
    ]);
    const source =
      args.span !== undefined
        ? ({ case: "span", value: args.span } as const)
        : ({ case: "cell", value: args.cell as EvaluationCaptureCellSourceV1 } as const);
    try {
      const res = await this.raw.captureEvaluationCase({
        datasetCollectionId: args.datasetCollectionId,
        ...(args.draftId !== undefined ? { draftId: args.draftId } : {}),
        source,
        fieldMappings: (args.fieldMappings ?? []) as DatasetFieldMappingV1[],
        ...(args.recordedOutputFieldPath !== undefined
          ? { recordedOutputFieldPath: args.recordedOutputFieldPath }
          : {}),
        ...(args.baseDatasetVersionId !== undefined
          ? { baseDatasetVersionId: args.baseDatasetVersionId }
          : {}),
        ...(args.expectedContentDigest !== undefined
          ? { expectedContentDigest: args.expectedContentDigest }
          : {}),
        idempotencyKey: args.idempotencyKey,
      });
      return ok(res);
    } catch (e) {
      const detail = findDetail(e, EvaluationCaptureRefusalV1Schema);
      if (detail !== undefined) {
        return err(toCaptureRefusal(detail));
      }
      throw e;
    }
  }

  /**
   * Publish a reviewed changeset. A digest mismatch is a FAILED_PRECONDITION
   * transport error (never a silent rebase) and is thrown for `classify()`.
   */
  async publishDatasetDrafts(args: {
    changesetId: string;
    previewDigest: string;
    label?: string;
    idempotencyKey: string;
  }): Promise<PublishDatasetCaseDraftsResponse> {
    requireNonEmpty("changesetId", args.changesetId);
    requireNonEmpty("previewDigest", args.previewDigest);
    requireIdempotencyKey("idempotencyKey", args.idempotencyKey);
    return await this.raw.publishDatasetCaseDrafts({
      changesetId: args.changesetId,
      previewDigest: args.previewDigest,
      ...(args.label !== undefined ? { label: args.label } : {}),
      idempotencyKey: args.idempotencyKey,
    });
  }

  // -- 7. annotations -------------------------------------------------------

  /**
   * Record a deployment marker, custom event, or time-range highlight.
   * `err(AnnotationRejection)` on a typed rejection (rides in `Status.details`).
   * A `startAt`/`endAt` are `Date`s; omit `endAt` for an instant.
   */
  async recordAnnotation(args: {
    kind: PlatformAnnotationKindV1;
    title: string;
    startAt?: Date;
    endAt?: Date;
    attributes?: readonly PlatformAnnotationAttributeV1[];
    links?: readonly PlatformAnnotationLinkV1[];
    idempotencyKey: string;
  }): Promise<Result<RecordPlatformAnnotationResponse, AnnotationRejection>> {
    requireNonEmpty("title", args.title);
    requireIdempotencyKey("idempotencyKey", args.idempotencyKey);
    rejectUnspecified("kind", [args.kind]);
    try {
      const res = await this.raw.recordPlatformAnnotation({
        kind: args.kind,
        title: args.title,
        ...(args.startAt !== undefined ? { startAt: timestampFromDate(args.startAt) } : {}),
        ...(args.endAt !== undefined ? { endAt: timestampFromDate(args.endAt) } : {}),
        attributes: (args.attributes ?? []) as PlatformAnnotationAttributeV1[],
        links: (args.links ?? []) as PlatformAnnotationLinkV1[],
        idempotencyKey: args.idempotencyKey,
      });
      return ok(res);
    } catch (e) {
      const detail = findDetail(e, PlatformAnnotationRejectionV1Schema);
      if (detail !== undefined) {
        return err(toAnnotationRejection(detail));
      }
      throw e;
    }
  }

  /**
   * List annotations overlapping a window. `resync`, when present, is a typed
   * directive that the caller's cursor cannot be honoured and the listing must
   * be restarted — it arrives with an empty page, never as a transport error.
   */
  async listAnnotations(args: {
    windowStart: Date | Timestamp;
    windowEnd: Date | Timestamp;
    kinds?: readonly PlatformAnnotationKindV1[];
    limit?: number;
    pageToken?: string;
  }): Promise<{
    annotations: PlatformAnnotationV1[];
    nextPageToken: string | undefined;
    hasMore: boolean;
    resync: CursorResync | undefined;
  }> {
    const windowStart = args.windowStart instanceof Date ? timestampFromDate(args.windowStart) : args.windowStart;
    const windowEnd = args.windowEnd instanceof Date ? timestampFromDate(args.windowEnd) : args.windowEnd;
    if (args.kinds !== undefined) {
      rejectUnspecified("kinds", args.kinds);
    }
    const res = await this.raw.listPlatformAnnotations({
      windowStart,
      windowEnd,
      kinds: (args.kinds ?? []) as PlatformAnnotationKindV1[],
      page: {
        ...(args.limit !== undefined ? { limit: args.limit } : {}),
        ...(args.pageToken !== undefined ? { pageToken: args.pageToken } : {}),
      },
    });
    return {
      annotations: res.annotations,
      nextPageToken: res.page?.nextPageToken,
      hasMore: res.page?.hasMore ?? false,
      resync: res.resync !== undefined ? toCursorResync(res.resync) : undefined,
    };
  }
}
