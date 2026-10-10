// An example TypeScript code scorer. Its bundle is this file, o11y_scorer.ts and o11y_prng.ts.
//
// It spot-checks five of the reference's lines against the candidate's. The lines come from `context.seed`, so every
// retry and repeatability trial checks the same ones.
import { seededRandom } from "./o11y_prng.ts";
import type { ScorerContext, ScorerInput, ScorerOutput } from "./o11y_scorer.ts";

const SAMPLED_LINES = 5;

export function score(input: ScorerInput, context: ScorerContext): ScorerOutput {
  const candidate = String(input.candidate_output ?? "").split("\n");
  const reference = String(input.reference_output ?? "").split("\n");
  const random = seededRandom(context.seed);
  const sampled = Array.from({ length: SAMPLED_LINES }, () => Math.floor(random() * reference.length));
  const matched = sampled.filter((line) => candidate[line] === reference[line]).length;
  return {
    score: matched / SAMPLED_LINES,
    verdict: matched === SAMPLED_LINES ? "pass" : "fail",
    label: `${matched} of ${SAMPLED_LINES} sampled lines match`,
    metrics: { reference_lines: reference.length },
  };
}
