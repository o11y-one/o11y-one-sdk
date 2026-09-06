package main

import (
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

func numFromPtr(p *float64) OptionalNumber {
	if p == nil {
		return absent()
	}
	v := *p
	return OptionalNumber{Present: true, Value: &v}
}

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
// enum. These are stable wire values L4 switches on.
func decisionString(d agenticv1.ReleaseGateDecisionV1) string {
	switch d {
	case agenticv1.ReleaseGateDecisionV1_RELEASE_GATE_DECISION_V1_PASS:
		return "PASS"
	case agenticv1.ReleaseGateDecisionV1_RELEASE_GATE_DECISION_V1_FAIL:
		return "FAIL"
	case agenticv1.ReleaseGateDecisionV1_RELEASE_GATE_DECISION_V1_INSUFFICIENT_DATA:
		return "INSUFFICIENT_DATA"
	default:
		return "UNSPECIFIED"
	}
}

// outcomeForDecision maps the server's authoritative decision onto the CI exit
// taxonomy. This is the guarantee the whole runner turns on:
//
//   - ONLY an explicit PASS becomes Improvement (exit 0).
//   - ONLY an explicit FAIL becomes Regression (exit 1).
//   - EVERYTHING else — INSUFFICIENT_DATA, UNSPECIFIED, or any enum value this
//     build does not recognise — becomes Indeterminate (exit 2).
//
// Indeterminate is therefore never reachable *from* pass or fail and pass/fail
// are never reachable from an absent decision: the runner cannot be coerced into
// calling a change good or bad when the server did not say so. The runner does
// not threshold, average, or otherwise recompute — it reads one field.
func outcomeForDecision(d agenticv1.ReleaseGateDecisionV1) Outcome {
	switch d {
	case agenticv1.ReleaseGateDecisionV1_RELEASE_GATE_DECISION_V1_PASS:
		return OutcomeImprovement
	case agenticv1.ReleaseGateDecisionV1_RELEASE_GATE_DECISION_V1_FAIL:
		return OutcomeRegression
	default:
		return OutcomeIndeterminate
	}
}

// buildDiffDocument serializes the server's authoritative comparison into the
// L4 contract. It reads the comparison; it never re-derives the verdict.
func buildDiffDocument(cmp *agenticv1.ReleaseGateEvaluationComparisonV1, gen Generator) DiffDocument {
	doc := DiffDocument{
		SchemaVersion:  SchemaVersion,
		GeneratedAt:    nowUTC().Format("2006-01-02T15:04:05Z07:00"),
		Generator:      gen,
		Metrics:        []DiffMetric{},
		FailureReasons: FailureReasons{Added: []string{}, Removed: []string{}},
		Notes:          []DiffNote{},
		Absences:       []DiffAbsence{},
	}

	base := cmp.GetBaselineEvaluation()
	cand := cmp.GetComparisonEvaluation()

	doc.Identity = DiffIdentity{
		GateID:     gateID(cmp, cand, base),
		MetricName: metricName(cand, base),
		Baseline:   sideFrom(base),
		Candidate:  sideFrom(cand),
	}

	// The verdict is the candidate's server-decided gate decision, mapped.
	decision := agenticv1.ReleaseGateDecisionV1_RELEASE_GATE_DECISION_V1_UNSPECIFIED
	if cand != nil {
		decision = cand.GetDecision()
	}
	outcome := outcomeForDecision(decision)
	doc.Verdict = DiffVerdict{
		Decision:        decisionString(decision),
		DecisionSource:  "server:CompareReleaseGateEvaluations",
		Outcome:         outcome.String(),
		ExitCode:        outcome.ExitCode(),
		DecisionChanged: cmp.GetDecisionChanged(),
		Authoritative:   true,
		Coercible:       false,
	}

	doc.Metrics = buildMetrics(cmp, base, cand)
	doc.FailureReasons = FailureReasons{
		Added:   orEmpty(cmp.GetAddedFailureReasons()),
		Removed: orEmpty(cmp.GetRemovedFailureReasons()),
	}
	doc.Notes = buildNotes(cmp, cand)
	doc.Absences = collectAbsences(base, cand)
	return doc
}

func gateID(cmp *agenticv1.ReleaseGateEvaluationComparisonV1, cand, base *agenticv1.ReleaseGateEvaluationV1) string {
	if g := cmp.GetGate(); g != nil && g.GetGateId() != "" {
		return g.GetGateId()
	}
	if cand != nil && cand.GetGateId() != "" {
		return cand.GetGateId()
	}
	if base != nil {
		return base.GetGateId()
	}
	return ""
}

func metricName(cand, base *agenticv1.ReleaseGateEvaluationV1) string {
	if cand != nil && cand.GetMetricName() != "" {
		return cand.GetMetricName()
	}
	if base != nil {
		return base.GetMetricName()
	}
	return ""
}

func sideFrom(e *agenticv1.ReleaseGateEvaluationV1) DiffSide {
	if e == nil {
		return DiffSide{AvgScore: absent(), AvgCostUSD: absent()}
	}
	s := DiffSide{
		EvaluationID:         e.GetEvaluationId(),
		DeploymentID:         e.GetDeploymentId(),
		UsedFallbackBaseline: e.GetUsedFallbackBaseline(),
		Simulated:            e.GetSimulated(),
		SampleCount:          e.GetCurrentSampleCount(),
		AvgScore:             numFromPtr(e.CurrentAvgScore),
		AvgCostUSD:           numFromPtr(e.CurrentAvgCostUsd),
	}
	if e.BaselineSource != nil {
		s.BaselineSource = e.GetBaselineSource()
	}
	return s
}

func buildMetrics(cmp *agenticv1.ReleaseGateEvaluationComparisonV1, base, cand *agenticv1.ReleaseGateEvaluationV1) []DiffMetric {
	baseScore, candScore := absent(), absent()
	baseCost, candCost := absent(), absent()
	baseSamples, candSamples := absent(), absent()
	if base != nil {
		baseScore = numFromPtr(base.CurrentAvgScore)
		baseCost = numFromPtr(base.CurrentAvgCostUsd)
		baseSamples = numFromInt(base.GetCurrentSampleCount())
	}
	if cand != nil {
		candScore = numFromPtr(cand.CurrentAvgScore)
		candCost = numFromPtr(cand.CurrentAvgCostUsd)
		candSamples = numFromInt(cand.GetCurrentSampleCount())
	}

	return []DiffMetric{
		{
			Key: "avg_score", Label: "Average score", Unit: "score", HigherIsBetter: true,
			Baseline: baseScore, Candidate: candScore,
			// server-reported delta; absent when the server did not compute it.
			Delta: numFromPtr(cmp.CurrentAvgScoreDelta),
		},
		{
			Key: "avg_cost_usd", Label: "Average cost (USD)", Unit: "usd", HigherIsBetter: false,
			Baseline: baseCost, Candidate: candCost,
			Delta: numFromPtr(cmp.CurrentAvgCostUsdDelta),
		},
		{
			Key: "sample_count", Label: "Sample count", Unit: "count", HigherIsBetter: true,
			Baseline: baseSamples, Candidate: candSamples,
			Delta: numFromInt(cmp.GetCurrentSampleCountDelta()),
		},
		{
			Key: "bad_outcomes_count", Label: "Bad outcomes", Unit: "count", HigherIsBetter: false,
			Baseline: badOutcomes(base), Candidate: badOutcomes(cand),
			Delta: numFromInt(cmp.GetBadOutcomesCountDelta()),
		},
	}
}

func badOutcomes(e *agenticv1.ReleaseGateEvaluationV1) OptionalNumber {
	if e == nil {
		return absent()
	}
	return numFromInt(e.GetBadOutcomesCount())
}

func buildNotes(cmp *agenticv1.ReleaseGateEvaluationComparisonV1, cand *agenticv1.ReleaseGateEvaluationV1) []DiffNote {
	notes := []DiffNote{}
	if cmp.GetBaselineSourceChanged() {
		notes = append(notes, DiffNote{
			Code: "baseline_source_changed", Severity: "warn",
			Message: "Baseline source changed between the two evaluations; the comparison spans different baselines.",
		})
	}
	if cmp.GetUsedFallbackBaselineChanged() {
		notes = append(notes, DiffNote{
			Code: "used_fallback_baseline_changed", Severity: "warn",
			Message: "Fallback-baseline usage changed between the two evaluations.",
		})
	}
	if cmp.GetDecisionChanged() {
		notes = append(notes, DiffNote{
			Code: "decision_changed", Severity: "info",
			Message: "The gate decision differs between baseline and candidate.",
		})
	}
	if cand != nil && cand.GetSimulated() {
		notes = append(notes, DiffNote{
			Code: "simulated_evaluation", Severity: "info",
			Message: "The candidate evaluation was simulated.",
		})
	}
	return notes
}

func collectAbsences(base, cand *agenticv1.ReleaseGateEvaluationV1) []DiffAbsence {
	out := []DiffAbsence{}
	check := func(side string, e *agenticv1.ReleaseGateEvaluationV1) {
		if e == nil {
			out = append(out, DiffAbsence{Field: "identity." + side, Reason: reasonNotReported})
			return
		}
		if e.CurrentAvgScore == nil {
			out = append(out, DiffAbsence{Field: "identity." + side + ".avg_score", Reason: reasonNotReported})
		}
		if e.CurrentAvgCostUsd == nil {
			out = append(out, DiffAbsence{Field: "identity." + side + ".avg_cost_usd", Reason: reasonNotReported})
		}
	}
	check("baseline", base)
	check("candidate", cand)
	return out
}

func orEmpty(s []string) []string {
	if s == nil {
		return []string{}
	}
	return s
}
