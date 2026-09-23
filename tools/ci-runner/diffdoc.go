package main

import (
	"fmt"
	"strings"

	agenticv1 "github.com/o11y-one/o11y-one-sdk/gen/go/o11y_one/agentic/v1"
)

// SchemaVersion is the versioned contract this runner emits for the L4 PR-diff
// renderer. See scratchpad l3-diff-schema.md. Breaking changes bump the major.
const SchemaVersion = "o11y.eval.diff/v1"

// OptionalNumber is the typed-absence primitive that makes the whole document
// safe to render: a missing value is Present=false, a real zero is
// {Present:true, Value:0}. A renderer that treats absence as zero is the exact
// bug this type exists to prevent, so nothing downstream should ever have to
// guess. omitempty is deliberately NOT set on Present — false must serialize.
type OptionalNumber struct {
	Present bool     `json:"present"`
	Value   *float64 `json:"value,omitempty"`
}

func absent() OptionalNumber { return OptionalNumber{Present: false} }

func numFrom(v float64) OptionalNumber {
	x := v
	return OptionalNumber{Present: true, Value: &x}
}

func numFromInt[T ~int32 | ~uint32 | ~int | ~int64](v T) OptionalNumber {
	return numFrom(float64(v))
}

// DiffDocument is the machine-readable diff — the L4 renderer's sole input.
type DiffDocument struct {
	SchemaVersion  string         `json:"schema_version"`
	GeneratedAt    string         `json:"generated_at"`
	Generator      Generator      `json:"generator"`
	Identity       DiffIdentity   `json:"identity"`
	Verdict        DiffVerdict    `json:"verdict"`
	Metrics        []DiffMetric   `json:"metrics"`
	FailureReasons FailureReasons `json:"failure_reasons"`
	Notes          []DiffNote     `json:"notes"`
	Absences       []DiffAbsence  `json:"absences"`
}

type Generator struct {
	Tool    string `json:"tool"`
	Version string `json:"version"`
}

type DiffIdentity struct {
	GateID     string   `json:"gate_id"`
	MetricName string   `json:"metric_name"`
	Baseline   DiffSide `json:"baseline"`
	Candidate  DiffSide `json:"candidate"`
}

type DiffSide struct {
	EvaluationID         string         `json:"evaluation_id"`
	DeploymentID         string         `json:"deployment_id"`
	BaselineSource       string         `json:"baseline_source,omitempty"`
	UsedFallbackBaseline bool           `json:"used_fallback_baseline"`
	Simulated            bool           `json:"simulated"`
	SampleCount          uint32         `json:"sample_count"`
	AvgScore             OptionalNumber `json:"avg_score"`
	AvgCostUSD           OptionalNumber `json:"avg_cost_usd"`
}

type DiffVerdict struct {
	Decision        string `json:"decision"`
	DecisionSource  string `json:"decision_source"`
	Outcome         string `json:"outcome"`
	ExitCode        int    `json:"exit_code"`
	DecisionChanged bool   `json:"decision_changed"`
	Authoritative   bool   `json:"authoritative"`
	Coercible       bool   `json:"coercible"`
}

type DiffMetric struct {
	Key            string         `json:"key"`
	Label          string         `json:"label"`
	Unit           string         `json:"unit"`
	HigherIsBetter bool           `json:"higher_is_better"`
	Baseline       OptionalNumber `json:"baseline"`
	Candidate      OptionalNumber `json:"candidate"`
	Delta          OptionalNumber `json:"delta"`
}

type FailureReasons struct {
	Added   []string `json:"added"`
	Removed []string `json:"removed"`
}

type DiffNote struct {
	Code     string `json:"code"`
	Severity string `json:"severity"`
	Message  string `json:"message"`
}

type DiffAbsence struct {
	Field  string `json:"field"`
	Reason string `json:"reason"`
}

const reasonNotReported = "not_reported_by_server"

// --- the verdict mapping: the one place a server decision becomes an exit code -

// The decision strings surfaced verbatim in the document, keyed by the server
// enum. These are stable wire values L4 switches on, so an outcome this build
// does not recognise renders as UNSPECIFIED rather than leaking a raw number a
// renderer could mistake for a decision.
func decisionString(o agenticv1.EvaluationDecisionOutcomeV1) string {
	switch o {
	case agenticv1.EvaluationDecisionOutcomeV1_EVALUATION_DECISION_OUTCOME_V1_RECOMMENDED:
		return "RECOMMENDED"
	case agenticv1.EvaluationDecisionOutcomeV1_EVALUATION_DECISION_OUTCOME_V1_NO_CLEAR_WINNER:
		return "NO_CLEAR_WINNER"
	case agenticv1.EvaluationDecisionOutcomeV1_EVALUATION_DECISION_OUTCOME_V1_INSUFFICIENT_EVIDENCE:
		return "INSUFFICIENT_EVIDENCE"
	case agenticv1.EvaluationDecisionOutcomeV1_EVALUATION_DECISION_OUTCOME_V1_BLOCKED:
		return "BLOCKED"
	default:
		return "UNSPECIFIED"
	}
}

// outcomeForAdoptedDecision maps the run's adopted decision onto the CI exit
// taxonomy. This is the guarantee the whole runner turns on:
//
//   - ONLY a decision the server marked AVAILABLE is read at all. An adopted
//     decision that is PENDING, NOT_OBSERVED, absent, or carries no revision is
//     indeterminate, whatever the rest of the message says.
//   - ONLY an explicit RECOMMENDED *naming the candidate under test* becomes
//     Improvement (exit 0). A recommendation for a DIFFERENT candidate is not a
//     pass for this one, and an unset recommended key never matches.
//   - ONLY an explicit BLOCKED becomes Regression (exit 1).
//   - EVERYTHING else — NO_CLEAR_WINNER, INSUFFICIENT_EVIDENCE, UNSPECIFIED, or
//     any enum value this build does not recognise — becomes Indeterminate
//     (exit 2).
//
// Indeterminate is therefore never reachable *from* pass or fail and pass/fail
// are never reachable from an absent decision: the runner cannot be coerced into
// calling a change good or bad when the server did not say so. The runner does
// not threshold, average, or otherwise recompute — it reads one decision.
func outcomeForAdoptedDecision(ad *agenticv1.EvaluationAdoptedDecisionV1, candidateKey string) Outcome {
	if ad.GetAvailability().GetState() != agenticv1.MetricAvailabilityStateV1_METRIC_AVAILABILITY_STATE_V1_AVAILABLE {
		return OutcomeIndeterminate
	}
	decision := ad.GetRevision().GetDecision()
	switch decision.GetOutcome() {
	case agenticv1.EvaluationDecisionOutcomeV1_EVALUATION_DECISION_OUTCOME_V1_RECOMMENDED:
		if candidateKey != "" && decision.GetRecommendedCandidateKey() == candidateKey {
			return OutcomeImprovement
		}
		return OutcomeIndeterminate
	case agenticv1.EvaluationDecisionOutcomeV1_EVALUATION_DECISION_OUTCOME_V1_BLOCKED:
		return OutcomeRegression
	default:
		return OutcomeIndeterminate
	}
}

// buildDiffDocument serializes the run's adopted decision into the L4 contract.
// It reads the decision; it never re-derives the verdict.
func buildDiffDocument(resp *agenticv1.GetEvaluationRunOverviewResponse, candidateKey string, gen Generator) DiffDocument {
	ad := resp.GetAdoptedDecision()
	decision := ad.GetRevision().GetDecision()
	outcome := outcomeForAdoptedDecision(ad, candidateKey)
	tradeoff := tradeoffFor(decision, candidateKey)
	metrics, metricAbsences := buildMetrics(tradeoff)

	doc := DiffDocument{
		SchemaVersion: SchemaVersion,
		GeneratedAt:   nowUTC().Format("2006-01-02T15:04:05Z07:00"),
		Generator:     gen,
	}

	doc.Verdict = DiffVerdict{
		Decision:       decisionString(decision.GetOutcome()),
		DecisionSource: "server:GetEvaluationRunOverview.adopted_decision",
		Outcome:        outcome.String(),
		ExitCode:       outcome.ExitCode(),
		// DecisionChanged stays false: one run's adopted decision has no
		// "changed against the previous one" fact. Declared in Absences.
		Authoritative: true,
		Coercible:     false,
	}

	// Both sides here are candidate keys — the reference the server decided
	// against, and the candidate this invocation put under test. They ride in
	// the schema's evaluation_id because that field IS the side's identity;
	// under this verb the identity of a side is its candidate key.
	doc.Identity = DiffIdentity{
		Baseline:  candidateSide(decision.GetReferenceCandidateKey()),
		Candidate: candidateSide(candidateKey),
	}

	doc.Metrics = metrics
	doc.FailureReasons = FailureReasons{Added: blockerKinds(decision, candidateKey), Removed: []string{}}
	doc.Notes = buildNotes(ad)
	doc.Absences = append(collectAbsences(ad, tradeoff), metricAbsences...)
	return doc
}

func candidateSide(key string) DiffSide {
	return DiffSide{EvaluationID: key, AvgScore: absent(), AvgCostUSD: absent()}
}

// tradeoffFor picks the decision's row for one candidate. A decision that never
// scored this candidate has no row, and that is an absence, not a zero.
func tradeoffFor(d *agenticv1.EvaluationDecisionV1, candidateKey string) *agenticv1.CandidateTradeoffV1 {
	for _, t := range d.GetTradeoffs() {
		if t.GetCandidateKey() == candidateKey {
			return t
		}
	}
	return nil
}

// buildMetrics renders the candidate's tradeoff row. quality_delta and
// cost_delta are already signed deltas against the reference — the server does
// not report the two levels they were computed from, so both sides stay absent
// rather than being back-filled with a number nobody measured.
func buildMetrics(t *agenticv1.CandidateTradeoffV1) ([]DiffMetric, []DiffAbsence) {
	absences := []DiffAbsence{}
	qualityDelta, costDelta := absent(), absent()
	improved, regressed := absent(), absent()

	if t != nil {
		qualityDelta = numFrom(t.GetQualityDelta())
		improved = numFromInt(t.GetImprovedCaseCount())
		regressed = numFromInt(t.GetRegressedCaseCount())
		if c := t.GetCostDelta(); c != nil {
			// The row is denominated in USD. A cost the server priced in some
			// other currency is NOT converted here — a wrong number in a money
			// column is worse than a stated absence.
			if cur := c.GetCurrencyCode(); cur == "" || cur == "USD" {
				costDelta = numFrom(float64(c.GetAmountMicros()) / 1e6)
			} else {
				absences = append(absences, DiffAbsence{
					Field:  "metrics.cost_delta_usd",
					Reason: "cost_reported_in_" + cur,
				})
			}
		}
	}

	return []DiffMetric{
		{
			Key: "quality_delta", Label: "Quality delta (net improved-case rate)", Unit: "rate", HigherIsBetter: true,
			Baseline: absent(), Candidate: absent(), Delta: qualityDelta,
		},
		{
			Key: "cost_delta_usd", Label: "Cost delta (USD)", Unit: "usd", HigherIsBetter: false,
			Baseline: absent(), Candidate: absent(), Delta: costDelta,
		},
		{
			Key: "improved_case_count", Label: "Improved cases", Unit: "count", HigherIsBetter: true,
			Baseline: absent(), Candidate: improved, Delta: absent(),
		},
		{
			Key: "regressed_case_count", Label: "Regressed cases", Unit: "count", HigherIsBetter: false,
			Baseline: absent(), Candidate: regressed, Delta: absent(),
		},
	}, absences
}

// blockerKinds are the decision's stated reasons this candidate cannot be
// recommended. A blocker naming no candidate is run-wide and counts against
// every candidate; another candidate's blocker is not this one's failure.
func blockerKinds(d *agenticv1.EvaluationDecisionV1, candidateKey string) []string {
	out := []string{}
	for _, b := range d.GetBlockers() {
		if k := b.GetCandidateKey(); k != "" && k != candidateKey {
			continue
		}
		out = append(out, strings.TrimPrefix(b.GetKind().String(), "DECISION_BLOCKER_KIND_V1_"))
	}
	return out
}

func buildNotes(ad *agenticv1.EvaluationAdoptedDecisionV1) []DiffNote {
	notes := []DiffNote{}
	if ad.GetAvailability().GetState() != agenticv1.MetricAvailabilityStateV1_METRIC_AVAILABILITY_STATE_V1_AVAILABLE {
		msg := "The run has no adopted decision available, so no verdict is reachable. This is not a pass."
		if reason := ad.GetAvailability().GetReasonCode(); reason != "" {
			msg = fmt.Sprintf("%s Server reason: %s.", msg, reason)
		}
		notes = append(notes, DiffNote{Code: "adopted_decision_unavailable", Severity: "warn", Message: msg})
	}
	return notes
}

func collectAbsences(ad *agenticv1.EvaluationAdoptedDecisionV1, tradeoff *agenticv1.CandidateTradeoffV1) []DiffAbsence {
	out := []DiffAbsence{
		// This verb reports one run's adopted decision, not a change between two
		// gate evaluations, and it reports no per-side sample counts. Both
		// document fields are therefore structurally absent, every time.
		{Field: "verdict.decision_changed", Reason: reasonNotReported},
		{Field: "identity.sample_count", Reason: reasonNotReported},
	}
	if ad.GetAvailability().GetState() != agenticv1.MetricAvailabilityStateV1_METRIC_AVAILABILITY_STATE_V1_AVAILABLE {
		reason := ad.GetAvailability().GetReasonCode()
		if reason == "" {
			reason = reasonNotReported
		}
		out = append(out, DiffAbsence{Field: "verdict.decision", Reason: reason})
	}
	if tradeoff == nil {
		out = append(out, DiffAbsence{Field: "metrics", Reason: reasonNotReported})
	}
	return out
}
