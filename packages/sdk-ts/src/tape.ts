/**
 * Record and replay for an externally executed candidate: one tape per lease,
 * one case handle per leased case, and the same harness code in both modes.
 *
 * Recording buffers each model and tool call in memory and sends a lease's
 * cases together, one chunk per case, when the next call would cross a bound
 * the server publishes on `sdk_record_replay`, or on `flush()`. Record, then
 * submit: call `flush()` after `finish()` and before `submitCaseOutputs`.
 * Steps that never reached a flush are lost with the process; the case's
 * recording stays incomplete, and the server replays it as
 * `RECORDING_INCOMPLETE`.
 *
 * Replay answers each call from the recording through `LookupReplayStep`, and
 * never runs `live`. The first call that leaves the recording throws
 * {@link ReplayDivergedError}; the server has already made that the case's
 * verdict, so the harness stops the case and does not submit it.
 *
 * Redaction is the server's, before anything is digested or stored. Nothing
 * here logs a call, or puts a request or response body in an error.
 */
import { create, type MessageInitShape } from "@bufbuild/protobuf";
import {
  ExternalLeaseRefusalKindV1,
  ExternalLeaseRefusalV1Schema,
  ExternalSubmissionAckKindV1,
  RecordedCallKindV1,
  ReplayDivergenceKindV1,
  type ExternalCaseLeaseV1,
  type LeasedEvaluationCaseV1,
  type RecordedCallV1Schema,
  type ReplayDivergenceV1,
} from "@o11y-one/api-agentic/o11y_one/agentic/v1/evaluation_pb";

import type { AgenticEvaluationClient, RecordReplayLimits } from "./evaluation.js";
import { toLeaseRefusal, type LeaseRefusal } from "./refusals.js";
import { byteLength, ValidationError } from "./validate.js";

type RecordedCall = MessageInitShape<typeof RecordedCallV1Schema>;
type Coordinates = Pick<
  LeasedEvaluationCaseV1,
  "cohortKey" | "candidateKey" | "caseRevisionId" | "trial" | "attemptGeneration"
>;

/** The server's own margin between its request bound and its per-call bound. */
const FRAMING_MARGIN_BYTES = 64 << 10;
// ponytail: a flat per-call framing estimate rather than encoding the request on every step; the margin above
// absorbs it until calls get tiny and numerous enough to need an exact `toBinary` size.
const CALL_FRAMING_BYTES = 16;
const RECORDING_CONFLICT = "recording_conflict";

/** The lease plane refused the request. `refusal.reason` names the wire kind. */
export class LeaseRefusedError extends Error {
  readonly refusal: LeaseRefusal;

  constructor(refusal: LeaseRefusal, message = `the lease plane refused the request (${refusal.reason})`) {
    super(message);
    this.name = "LeaseRefusedError";
    this.refusal = refusal;
  }
}

/** This deployment cannot record or replay. Retrying will not change that. */
export class RecordingUnavailableError extends LeaseRefusedError {
  readonly retryable = false;

  constructor(refusal: LeaseRefusal = toLeaseRefusal(create(ExternalLeaseRefusalV1Schema, {
    kind: ExternalLeaseRefusalKindV1.RECORDING_UNAVAILABLE,
  }))) {
    super(refusal, "recording and replay are unavailable on this deployment (RECORDING_UNAVAILABLE)");
    this.name = "RecordingUnavailableError";
  }
}

/** The server stored none of one case's chunk, for a reason a resend will not fix. */
export class CaseRecordingRejectedError extends Error {
  readonly code: string;
  readonly case: Coordinates;

  constructor(code: string, at: Coordinates) {
    super(`the server rejected case ${at.caseRevisionId}'s recording (${code})`);
    this.name = "CaseRecordingRejectedError";
    this.code = code;
    this.case = at;
  }
}

export type ReplayDivergenceReason =
  | "UNSPECIFIED"
  | "MODEL_REQUEST_DIFFERS"
  | "TOOL_REQUEST_DIFFERS"
  | "RECORDING_EXHAUSTED"
  | "RECORDING_INCOMPLETE";

export interface ReplayDivergence {
  readonly step: number;
  readonly reason: ReplayDivergenceReason;
  /** sha256 hex of the recorded request; empty when the recording holds no such step. */
  readonly expectedRequestDigest: string;
  readonly observedRequestDigest: string;
  readonly raw: ReplayDivergenceV1;
}

export function toReplayDivergence(m: ReplayDivergenceV1): ReplayDivergence {
  return {
    step: m.step,
    reason: ((ReplayDivergenceKindV1 as unknown as Record<number, string>)[m.kind] ??
      "UNSPECIFIED") as ReplayDivergenceReason,
    expectedRequestDigest: m.expectedRequestDigest,
    observedRequestDigest: m.observedRequestDigest,
    raw: m,
  };
}

/** The replayed agent left its recording at `divergence.step`. Stop the case; do not submit it. */
export class ReplayDivergedError extends Error {
  readonly divergence: ReplayDivergence;

  constructor(divergence: ReplayDivergence) {
    super(`the replayed agent left its recording at step ${divergence.step} (${divergence.reason})`);
    this.name = "ReplayDivergedError";
    this.divergence = divergence;
  }
}

function leaseRefusedError(refusal: LeaseRefusal): LeaseRefusedError {
  return refusal.reason === "RECORDING_UNAVAILABLE"
    ? new RecordingUnavailableError(refusal)
    : new LeaseRefusedError(refusal);
}

function coordinates(leased: Coordinates): Coordinates {
  return {
    cohortKey: leased.cohortKey,
    candidateKey: leased.candidateKey,
    caseRevisionId: leased.caseRevisionId,
    trial: leased.trial,
    attemptGeneration: leased.attemptGeneration,
  };
}

interface Pending {
  readonly at: Coordinates;
  firstStep: number;
  calls: { call: RecordedCall; bytes: number }[];
  last: boolean;
  closed: boolean;
}

/** One lease's tape. Build it with `recordLease` or `replayLease`. */
export class LeaseTape {
  readonly #client: AgenticEvaluationClient;
  readonly #replay: boolean;
  readonly #evaluationRunId: string;
  readonly #lease: Pick<ExternalCaseLeaseV1, "leaseId" | "leaseToken">;
  readonly #limits: RecordReplayLimits;
  readonly #cases: Pending[] = [];
  #pendingBytes = 0;
  #pendingCalls = 0;
  #flushing: Promise<void> = Promise.resolve();

  constructor(
    client: AgenticEvaluationClient,
    replay: boolean,
    evaluationRunId: string,
    lease: Pick<ExternalCaseLeaseV1, "leaseId" | "leaseToken">,
    limits: RecordReplayLimits,
  ) {
    this.#client = client;
    this.#replay = replay;
    this.#evaluationRunId = evaluationRunId;
    this.#lease = lease;
    this.#limits = limits;
  }

  /** The handle a harness routes one leased case's model and tool calls through. */
  case(leased: Coordinates): CaseTape {
    const pending: Pending = { at: coordinates(leased), firstStep: 0, calls: [], last: false, closed: false };
    this.#cases.push(pending);
    return new CaseTape(this, pending, this.#replay);
  }

  /** Sends every buffered call and every finished case. A no-op under replay. */
  flush(): Promise<void> {
    // Serialized, so two flushes never send overlapping chunks for one case.
    const next = this.#flushing.then(() => this.#flushOnce());
    this.#flushing = next.catch(() => undefined);
    return next;
  }

  /** @internal */
  async record(pending: Pending, call: RecordedCall): Promise<void> {
    const callBytes = byteLength(call.toolName ?? "") + byteLength(call.requestJson ?? "") +
      byteLength(call.responseJson ?? "");
    if (callBytes > this.#limits.maxCallBytes) {
      throw new ValidationError("call", `call is ${callBytes} bytes, over the ${this.#limits.maxCallBytes}-byte bound`);
    }
    const bytes = callBytes + CALL_FRAMING_BYTES;
    if (
      this.#pendingBytes + bytes > this.#limits.maxRecordRequestBytes - FRAMING_MARGIN_BYTES ||
      this.#pendingCalls + 1 > this.#limits.maxCallsPerRequest
    ) {
      await this.flush();
    }
    pending.calls.push({ call, bytes });
    this.#pendingBytes += bytes;
    this.#pendingCalls++;
  }

  /** @internal */
  checkToolName(toolName: string): void {
    const len = byteLength(toolName);
    if (len > this.#limits.maxToolNameBytes) {
      throw new ValidationError("toolName", `toolName is ${len} bytes, over the ${this.#limits.maxToolNameBytes}-byte bound`);
    }
  }

  /** @internal */
  async lookup(at: Coordinates, step: number, observed: RecordedCall): Promise<string> {
    const r = await this.#client.lookupReplayStep({
      evaluationRunId: this.#evaluationRunId,
      leaseId: this.#lease.leaseId,
      leaseToken: this.#lease.leaseToken,
      leased: at,
      step,
      observed,
    });
    if (!r.ok) {
      throw leaseRefusedError(r.refusal);
    }
    if (r.value.type === "divergence") {
      throw new ReplayDivergedError(r.value.divergence);
    }
    return r.value.responseJson;
  }

  #drop(p: Pending, count: number): void {
    for (const c of p.calls.splice(0, count)) {
      this.#pendingBytes -= c.bytes;
      this.#pendingCalls--;
    }
  }

  async #flushOnce(): Promise<void> {
    const sending = this.#cases.filter((p) => p.calls.length > 0 || (p.last && !p.closed));
    for (let i = 0; i < sending.length; i += this.#limits.maxChunksPerRequest) {
      const batch = sending.slice(i, i + this.#limits.maxChunksPerRequest);
      const sent = batch.map((p) => p.calls.length);
      const chunks = batch.map((p) => ({ ...p.at, firstStep: p.firstStep, calls: p.calls.map((c) => c.call), last: p.last }));
      const r = await this.#client.recordCaseSteps({
        evaluationRunId: this.#evaluationRunId,
        leaseId: this.#lease.leaseId,
        leaseToken: this.#lease.leaseToken,
        chunks,
      });
      if (!r.ok) {
        throw leaseRefusedError(r.refusal);
      }
      let rejected: CaseRecordingRejectedError | undefined;
      r.value.forEach((ack, index) => {
        const p = batch[index];
        if (p === undefined) {
          return;
        }
        if (ack.kind === ExternalSubmissionAckKindV1.REJECTED) {
          const code = ack.rejection?.code ?? "";
          // A conflict means the trajectory moved under the write; the calls stay for the next flush.
          if (code !== RECORDING_CONFLICT) {
            rejected ??= new CaseRecordingRejectedError(code, p.at);
            // Never resent: a rejection names a case this lease can no longer record.
            this.#drop(p, p.calls.length);
            p.closed = true;
          }
          return;
        }
        // Calls appended while the request was in flight sit after the ones sent, so a prefix is dropped.
        const stored = Math.min(Math.max(ack.nextStep - p.firstStep, 0), sent[index] ?? 0);
        this.#drop(p, stored);
        p.firstStep += stored;
        p.closed ||= ack.complete;
      });
      if (rejected !== undefined) {
        throw rejected;
      }
    }
  }
}

/** One leased case's calls. Make them one at a time: steps are numbered in the order they complete. */
export class CaseTape {
  readonly #tape: LeaseTape;
  readonly #pending: Pending;
  readonly #replay: boolean;
  #step = 0;

  /** @internal */
  constructor(tape: LeaseTape, pending: Pending, replay: boolean) {
    this.#tape = tape;
    this.#pending = pending;
    this.#replay = replay;
  }

  /** A model call: `live` runs and is recorded, or under replay the recorded response returns. */
  model(requestJson: string, live: () => Promise<string>): Promise<string> {
    return this.#call(RecordedCallKindV1.MODEL, "", requestJson, live);
  }

  /** A tool call, as `model`. */
  tool(toolName: string, requestJson: string, live: () => Promise<string>): Promise<string> {
    return this.#call(RecordedCallKindV1.TOOL, toolName, requestJson, live);
  }

  /** The case made its last call: its next flush completes the recording. */
  finish(): void {
    this.#pending.last = true;
  }

  async #call(
    kind: RecordedCallKindV1,
    toolName: string,
    requestJson: string,
    live: () => Promise<string>,
  ): Promise<string> {
    this.#tape.checkToolName(toolName);
    if (this.#replay) {
      const response = await this.#tape.lookup(this.#pending.at, this.#step, { kind, toolName, requestJson });
      this.#step++;
      return response;
    }
    const responseJson = await live();
    await this.#tape.record(this.#pending, { kind, toolName, requestJson, responseJson });
    return responseJson;
  }
}
