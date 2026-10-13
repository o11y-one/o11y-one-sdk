/**
 * `@o11y-one/sdk/loop` — the Loop rollout client a trainer drives (#722).
 *
 * A person mints a run in the web and hands the trainer its id (`O11Y_RUN`,
 * not a secret) and an organization's machine key with the `rollout:drive`
 * scope (`O11Y_API_KEY`). `LoopClient` resets, steps, closes and forks that
 * run's rollouts over `LoopRolloutService`, one open rollout at a time.
 */
import type { MessageInitShape } from "@bufbuild/protobuf";
import type { Client } from "@connectrpc/connect";
import {
  LoopRolloutRejectionV1Schema,
  LoopRolloutService,
  type LoopRolloutV1,
  type LoopToolCallV1Schema,
  type ResetLoopRolloutRequest,
  type StepLoopRolloutResponse,
} from "@o11y-one/api-agentic/o11y_one/agentic/v1/rollout_pb";

import { assertLooksLikeMachineCredential } from "./auth.js";
import { O11yClient, type ClientOptions } from "./client.js";
import { findDetail } from "./refusals.js";

// Globals every runtime this package targets has; it compiles against ES2023 alone.
declare const setTimeout: (callback: () => void, ms: number) => unknown;
declare const crypto: { randomUUID(): string };

export const DEFAULT_BASE_URL = "https://grpc.o11y.one";
/** How long a reset retries a paused run before it throws `run_paused`. */
export const RUN_PAUSED_RETRY_MS = 30 * 60 * 1000;
/** The wait between those retries when the refusal names none. */
export const RUN_PAUSED_WAIT_MS = 5000;

/** Random per trainer process: a new one on a run reads as a reconnect. */
const SESSION_ID = crypto.randomUUID();

/**
 * A `LoopRolloutService` refusal: its stable `code`, e.g.
 * `plan_concurrency_reached`, and when a retry may be admitted, when the
 * server said. `cause` is the `ConnectError`.
 */
export class RolloutRefused extends Error {
  readonly code: string;
  readonly retryAfterMs: number | undefined;

  constructor(code: string, retryAfterMs: number | undefined, message: string, options?: ErrorOptions) {
    super(message ? `${code}: ${message}` : code, options);
    this.name = "RolloutRefused";
    this.code = code;
    this.retryAfterMs = retryAfterMs;
  }
}

/**
 * One RPC. A status carrying `LoopRolloutRejectionV1` throws `RolloutRefused`;
 * any other, e.g. UNAUTHENTICATED (which `classify()` reads as
 * `reauthenticate`), is thrown as the server sent it.
 */
async function call<T>(rpc: () => Promise<T>): Promise<T> {
  try {
    return await rpc();
  } catch (error) {
    const detail = findDetail(error, LoopRolloutRejectionV1Schema);
    if (detail === undefined) throw error;
    const retry = detail.retryAfterMillis === undefined ? undefined : Number(detail.retryAfterMillis);
    throw new RolloutRefused(detail.reasonCode, retry, (error as { rawMessage: string }).rawMessage, {
      cause: error,
    });
  }
}

export interface LoopClientOptions extends Partial<ClientOptions> {
  /** The run's id; defaults to `O11Y_RUN`. */
  run?: string;
}

/** `ResetLoopRolloutRequest`'s own fields: group, task, training step, experiment name. */
export type ResetFields = Partial<
  Pick<
    ResetLoopRolloutRequest,
    | "groupId"
    | "groupIndex"
    | "groupSize"
    | "caseRevisionId"
    | "trainerStep"
    | "trainerTotalSteps"
    | "experimentName"
  >
>;

/**
 * One run's rollouts, one open at a time. `run` and `credential` default to
 * `O11Y_RUN` and `O11Y_API_KEY`; the key is sent as `x-o11y-key` and is never
 * logged or shown.
 */
export class LoopClient {
  readonly run: string;
  private readonly service: Client<typeof LoopRolloutService>;
  private open: string | undefined;

  constructor(options: LoopClientOptions = {}) {
    const env = (globalThis as { process?: { env: Record<string, string | undefined> } }).process?.env ?? {};
    const run = options.run || env.O11Y_RUN;
    if (!run) throw new Error("no run: pass run or set O11Y_RUN");
    const credential = assertLooksLikeMachineCredential(options.credential || env.O11Y_API_KEY || "");
    const o11y = new O11yClient({ ...options, baseUrl: options.baseUrl ?? DEFAULT_BASE_URL, credential });
    this.service = o11y.service(LoopRolloutService);
    this.run = run;
  }

  /** The open rollout's id, or `undefined`. */
  get rolloutId(): string | undefined {
    return this.open;
  }

  /**
   * Closes the open rollout, then starts one and answers once its environment
   * is ready for its first step. A paused run is retried, under one request
   * id, after each refusal's `retryAfterMs` (or `RUN_PAUSED_WAIT_MS`) for up to
   * `RUN_PAUSED_RETRY_MS`; every other refusal throws at once.
   */
  async reset(fields: ResetFields = {}): Promise<LoopRolloutV1> {
    await this.close();
    const request = {
      ...fields,
      runId: this.run,
      requestId: crypto.randomUUID(),
      client: { sessionId: SESSION_ID },
    };
    const deadline = Date.now() + RUN_PAUSED_RETRY_MS;
    for (;;) {
      try {
        const { rollout } = await call(() => this.service.resetLoopRollout(request));
        this.open = rollout?.rolloutId;
        return rollout as LoopRolloutV1;
      } catch (error) {
        if (!(error instanceof RolloutRefused) || error.code !== "run_paused") throw error;
        const wait = error.retryAfterMs ?? RUN_PAUSED_WAIT_MS;
        if (Date.now() + wait > deadline) throw error;
        await new Promise<void>((resolve) => setTimeout(resolve, wait));
      }
    }
  }

  /**
   * Runs 1 to 16 tool calls at once on the open rollout. `modelMessage` is the
   * assistant message they came from, as JSON.
   */
  async step(
    calls: readonly MessageInitShape<typeof LoopToolCallV1Schema>[],
    modelMessage?: string,
  ): Promise<StepLoopRolloutResponse> {
    const request = { rolloutId: this.requireOpen(), calls: [...calls], modelMessageJson: modelMessage ?? "" };
    return call(() => this.service.stepLoopRollout(request));
  }

  /**
   * Closes the open rollout and answers with it once its verifier reported:
   * its `rewards`, `verdict` and any `failure`. `undefined` when none is open.
   */
  async close(): Promise<LoopRolloutV1 | undefined> {
    const rolloutId = this.open;
    this.open = undefined;
    if (rolloutId === undefined) return undefined;
    for (;;) {
      // Each close holds until the verifier reports or its wait ends.
      const closed = await call(() => this.service.closeLoopRollout({ rolloutId }));
      if (!closed.pending) return closed.rollout;
    }
  }

  /** Branches the open rollout into `copies` (2 to 64): a client per copy, this one first, each with its copy open. */
  async fork(copies: number): Promise<LoopClient[]> {
    const request = { rolloutId: this.requireOpen(), copies, requestId: crypto.randomUUID() };
    const { rollouts } = await call(() => this.service.forkLoopRollout(request));
    const forks = rollouts.slice(1).map((rollout) => {
      const fork = Object.assign(Object.create(LoopClient.prototype) as LoopClient, this);
      fork.open = rollout.rolloutId;
      return fork;
    });
    return [this, ...forks];
  }

  private requireOpen(): string {
    if (this.open === undefined) throw new Error("no rollout is open: reset() first");
    return this.open;
  }
}
