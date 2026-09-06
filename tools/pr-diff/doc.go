package main

import (
	"fmt"
	"strconv"
	"strings"
)

// This file binds, field-for-field, to lane L3's contract at
// scratchpad/l3-diff-schema.md ("L3 → L4 contract: the evaluation diff
// document", schema_version "o11y.eval.diff/v1", STABLE). JSON tags below are
// copied verbatim from that document's field reference; nothing here is
// invented. Where L3's document is silent on a field this renderer would like
// to have, that goes in scratchpad/l4-needs.md — it is not added here as a
// guess.
//
// supportedSchemaMajor is the only major version this build understands, per
// "L4 should hard-check the vN major and refuse a major it doesn't
// recognize." Unknown *fields* within a recognized major are tolerated
// (json.Unmarshal already ignores them); unknown *enum members* are passed
// through by the render code rather than rejected, per "L4 must tolerate
// unknown codes."
const supportedSchemaMajor = 1

// OptionalNumber is L3's `OptionalNumber` wrapper: a value is either present
// (a real float, which may legitimately be 0.0) or explicitly not present.
// Present is the only field the renderer may branch on — Value is meaningless
// when Present is false, and MUST NOT be treated as 0 in that case. This is
// the single rule the schema doc calls out as the one L4 must honor.
type OptionalNumber struct {
	Present bool    `json:"present"`
	Value   float64 `json:"value,omitempty"`
}

// Outcome is L3's mapped CI taxonomy (`verdict.outcome`): improvement,
// regression, or indeterminate. There is no "infra-failure" or "usage-error"
// member here — the schema doc is explicit that those aren't values this
// field takes, because a diff document only exists once the server has
// returned an authoritative comparison. A runner-level failure that happens
// *before* a document exists is handled separately in render.go
// (RenderInfraFailure) and never invents an Outcome value to describe it.
type Outcome string

const (
	OutcomeImprovement   Outcome = "improvement"
	OutcomeRegression    Outcome = "regression"
	OutcomeIndeterminate Outcome = "indeterminate"
)

// Verdict is `verdict` in the document — the load-bearing, server-authored
// object. L4 renders it; it never re-derives or second-guesses it (per
// "What L4 must NOT do": don't re-map verdict.outcome/exit_code).
type Verdict struct {
	Decision        string  `json:"decision"`
	DecisionSource  string  `json:"decision_source"`
	Outcome         Outcome `json:"outcome"`
	ExitCode        int     `json:"exit_code"`
	DecisionChanged bool    `json:"decision_changed"`
	Authoritative   bool    `json:"authoritative"`
	Coercible       bool    `json:"coercible"`
}

// EvalSide is one side (baseline or candidate) of `identity`.
type EvalSide struct {
	EvaluationID         string         `json:"evaluation_id"`
	DeploymentID         string         `json:"deployment_id"`
	BaselineSource       string         `json:"baseline_source"`
	UsedFallbackBaseline bool           `json:"used_fallback_baseline"`
	Simulated            bool           `json:"simulated"`
	SampleCount          int            `json:"sample_count"`
	AvgScore             OptionalNumber `json:"avg_score"`
	AvgCostUSD           OptionalNumber `json:"avg_cost_usd"`
}

// Identity is `identity`: which gate, which metric, and which two evaluations
// (baseline vs candidate) this document compares.
type Identity struct {
	GateID     string   `json:"gate_id"`
	MetricName string   `json:"metric_name"`
	Baseline   EvalSide `json:"baseline"`
	Candidate  EvalSide `json:"candidate"`
}

// MetricRow is one entry of `metrics[]`: the flat, render-ready table. Delta
// is candidate minus baseline as reported by the server's own comparison —
// never recomputed here, and independently typed-absent from Baseline and
// Candidate (a document can report a delta with no visible baseline value, or
// vice versa; the renderer shows exactly what it's given).
type MetricRow struct {
	Key            string         `json:"key"`
	Label          string         `json:"label"`
	Unit           string         `json:"unit"`
	HigherIsBetter bool           `json:"higher_is_better"`
	Baseline       OptionalNumber `json:"baseline"`
	Candidate      OptionalNumber `json:"candidate"`
	Delta          OptionalNumber `json:"delta"`
}

// FailureReasons is `failure_reasons`: gate-failure-reason codes gained or
// lost between baseline and candidate.
type FailureReasons struct {
	Added   []string `json:"added"`
	Removed []string `json:"removed"`
}

// Note is one entry of `notes[]`: a non-fatal caveat about comparability.
// Known v1 codes are baseline_source_changed, used_fallback_baseline_changed,
// decision_changed, simulated_evaluation, but per the schema doc L4 must
// tolerate unknown codes — render Message and default Severity to "info".
type Note struct {
	Code     string `json:"code"`
	Severity string `json:"severity"`
	Message  string `json:"message"`
}

// Absence is one entry of `absences[]`: an explicit pointer to a field the
// server did not populate. This is redundant with the per-field
// {"present": false} markers, but exists so the renderer can show a single
// "N fields unavailable" footnote "without walking the tree" (the schema
// doc's own words) instead of trying to path-match each absence back to a
// specific table cell.
type Absence struct {
	Field  string `json:"field"`
	Reason string `json:"reason"`
}

// Generator is `generator`: which build of the runner produced this document.
type Generator struct {
	Tool    string `json:"tool"`
	Version string `json:"version"`
}

// DiffDocument is the full document. Every number and verdict the renderer
// prints comes from one of these fields — nothing is computed from another
// field, nothing is fetched over the network, and no clock is read.
type DiffDocument struct {
	SchemaVersion string    `json:"schema_version"`
	GeneratedAt   string    `json:"generated_at"`
	Generator     Generator `json:"generator"`

	Identity Identity `json:"identity"`
	Verdict  Verdict  `json:"verdict"`

	Metrics        []MetricRow    `json:"metrics"`
	FailureReasons FailureReasons `json:"failure_reasons"`
	Notes          []Note         `json:"notes"`
	Absences       []Absence      `json:"absences"`
}

// schemaMajor extracts N from a schema_version string of the form
// "o11y.eval.diff/vN". Returns an error for anything else, including a
// well-formed but different family (schema_version is a family+version
// string, not just a bare number, so an unrelated family is also a hard
// error rather than something to guess about).
func schemaMajor(schemaVersion string) (int, error) {
	const prefix = "o11y.eval.diff/v"
	if !strings.HasPrefix(schemaVersion, prefix) {
		return 0, fmt.Errorf("schema_version %q is not in the o11y.eval.diff/vN family", schemaVersion)
	}
	rest := strings.TrimPrefix(schemaVersion, prefix)
	// Accept "v1" and also "v1.2" / "v1.2.3" (major.minor.patch), taking only
	// the major component, in case L3 later qualifies the version further.
	major := rest
	if i := strings.IndexByte(rest, '.'); i >= 0 {
		major = rest[:i]
	}
	n, err := strconv.Atoi(major)
	if err != nil {
		return 0, fmt.Errorf("schema_version %q has a non-numeric major version: %w", schemaVersion, err)
	}
	return n, nil
}

// unsupportedSchemaError is returned when a document's schema major version
// is one this build does not recognize. It is a real error (exit 1): this
// tool cannot honestly claim to have rendered a document it does not
// understand, and it must not guess at a newer or older major's shape.
type unsupportedSchemaError struct {
	got string
}

func (e *unsupportedSchemaError) Error() string {
	return fmt.Sprintf(
		"diff document schema_version %q: this build of pr-diff only understands major version %d (o11y.eval.diff/v%d)",
		e.got, supportedSchemaMajor, supportedSchemaMajor,
	)
}
func (e *unsupportedSchemaError) ExitCode() int { return 1 }
