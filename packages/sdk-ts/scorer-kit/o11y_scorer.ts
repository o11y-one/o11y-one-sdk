// The `score(input, context)` contract the sandbox's TypeScript harness calls, as types. Copy this file into your
// bundle beside score.ts and import it with `import type`: Node strips the import, so the bundle loads nothing for it.

/**
 * The case fields the scorer reads, each the JSON value the case holds. A field is present only when the scorer's
 * input fields name it (the first three by default) and the case has a value for it.
 */
export interface ScorerInput {
  case_input?: unknown;
  candidate_output?: unknown;
  reference_output?: unknown;
  correction?: unknown;
  original_context?: unknown;
}

/**
 * Fixed per job, and per publication for its repeatability trials, so a seeded scorer's retries and trials see the
 * same values. Both are unsigned 64-bit integers, so they arrive as bigint: a number would round them past 2^53.
 */
export interface ScorerContext {
  seed: bigint;
  frozen_evaluation_time_unix_nanos: bigint;
}

/**
 * What the harness accepts: `score` finite in [0, 1]; `label` at most 256 UTF-8 bytes; `explanation` at most 4 KiB;
 * at most 32 `metrics`, each named in at most 128 bytes and a finite number or a string of at most 256 bytes; and no
 * other field. Anything else ends the attempt as `invalid_output`.
 */
export interface ScorerOutput {
  score: number;
  verdict: "pass" | "fail";
  label?: string;
  explanation?: string;
  metrics?: Record<string, number | string>;
}

export type Scorer = (input: ScorerInput, context: ScorerContext) => ScorerOutput | Promise<ScorerOutput>;
