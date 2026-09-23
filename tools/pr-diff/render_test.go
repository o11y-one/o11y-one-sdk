package main

import (
	"encoding/json"
	"errors"
	"os"
	"strings"
	"testing"
)

func loadFixture(t *testing.T, name string) DiffDocument {
	t.Helper()
	raw, err := os.ReadFile("testdata/" + name)
	if err != nil {
		t.Fatalf("reading fixture %s: %v", name, err)
	}
	var doc DiffDocument
	if err := json.Unmarshal(raw, &doc); err != nil {
		t.Fatalf("parsing fixture %s: %v", name, err)
	}
	return doc
}

// TestRenderIsPure asserts the render core has no hidden inputs: the same
// document renders to byte-identical markdown every time, with nothing drawn
// from the clock, the environment, or the network.
func TestRenderIsPure(t *testing.T) {
	doc := loadFixture(t, "improvement.json")
	first, err := Render(doc)
	if err != nil {
		t.Fatalf("Render: %v", err)
	}
	second, err := Render(doc)
	if err != nil {
		t.Fatalf("Render: %v", err)
	}
	if first != second {
		t.Fatalf("Render is not deterministic:\n--- first ---\n%s\n--- second ---\n%s", first, second)
	}
}

func TestRenderCarriesMarker(t *testing.T) {
	doc := loadFixture(t, "improvement.json")
	md, err := Render(doc)
	if err != nil {
		t.Fatalf("Render: %v", err)
	}
	if !strings.Contains(md, commentMarker) {
		t.Fatalf("rendered comment is missing the idempotency marker %q:\n%s", commentMarker, md)
	}
}

func TestRenderImprovement(t *testing.T) {
	doc := loadFixture(t, "improvement.json")
	md, err := Render(doc)
	if err != nil {
		t.Fatalf("Render: %v", err)
	}
	for _, want := range []string{
		"Improvement", "exit 0", "server decision: `RECOMMENDED`",
		"(via `server:GetEvaluationRunOverview.adopted_decision`)",
		"Quality delta (net improved-case rate)", "+0.05 rate",
		"Cost delta (USD)", "-0.003 USD",
		"Improved cases", "12 count",
	} {
		if !strings.Contains(md, want) {
			t.Errorf("rendered improvement comment missing %q:\n%s", want, md)
		}
	}
	// A pass must not carry the indeterminate/regression callout language, and
	// must not print a sample count this document declares absent.
	for _, mustNot := range []string{"Indeterminate", "the server blocked this candidate", "not a pass", "samples"} {
		if strings.Contains(md, mustNot) {
			t.Errorf("improvement comment wrongly contains %q:\n%s", mustNot, md)
		}
	}
}

func TestRenderRegressionCarriesCallout(t *testing.T) {
	doc := loadFixture(t, "regression.json")
	md, err := Render(doc)
	if err != nil {
		t.Fatalf("Render: %v", err)
	}
	for _, want := range []string{
		"Regression", "exit 1", "server decision: `BLOCKED`",
		"the server blocked this candidate",
		"-0.06 rate",
		"New failure reasons:", "`MIN_SCORE_NOT_MET`", "`MAX_COST_EXCEEDED`",
	} {
		if !strings.Contains(md, want) {
			t.Errorf("rendered regression comment missing %q:\n%s", want, md)
		}
	}
}

// verdict.decision_changed is structurally absent under the current runner, so
// no fixture carries it — but older documents still can, and the code path has
// to stay, saying what the field means rather than naming a gate that no longer
// exists.
func TestDecisionChangedNoteNamesNoGate(t *testing.T) {
	md, err := Render(DiffDocument{
		SchemaVersion: "o11y.eval.diff/v1",
		Verdict:       Verdict{Decision: "BLOCKED", Outcome: OutcomeRegression, DecisionChanged: true},
	})
	if err != nil {
		t.Fatalf("Render: %v", err)
	}
	if !strings.Contains(md, "the server's decision changed between the two evaluations") {
		t.Errorf("a document with decision_changed set must say so:\n%s", md)
	}
	if strings.Contains(md, "release-gate decision changed") {
		t.Errorf("the note must not name a release gate:\n%s", md)
	}
}

// TestRenderIndeterminateIsNeverSoftenedToAPass is the load-bearing assertion
// for "indeterminate renders as its own clearly-marked state, never softened
// to a pass," and for the schema doc's own "coercible is always false, do not
// treat indeterminate as failure either — it is its own state."
func TestRenderIndeterminateIsNeverSoftenedToAPass(t *testing.T) {
	doc := loadFixture(t, "indeterminate.json")
	md, err := Render(doc)
	if err != nil {
		t.Fatalf("Render: %v", err)
	}
	for _, want := range []string{
		"Indeterminate", "exit 2", "server decision: `UNSPECIFIED`",
		"no verdict reachable", "not a pass", "not coercible into a pass or fail",
		"The run has no adopted decision available",
		"`verdict.decision` (decision_not_yet_adopted)",
	} {
		if !strings.Contains(md, want) {
			t.Errorf("rendered indeterminate comment missing %q:\n%s", want, md)
		}
	}
	if strings.Contains(md, "✅") {
		t.Errorf("indeterminate comment must not carry the pass emoji:\n%s", md)
	}
	if strings.Contains(md, "the server blocked this candidate") {
		t.Errorf("indeterminate comment must not carry the regression callout either — it is its own state:\n%s", md)
	}
}

func TestRenderInfraFailure(t *testing.T) {
	md := RenderInfraFailure(false, "the run-comparison RPC returned 503 twice; giving up after 2 retries.", 3)
	for _, want := range []string{
		commentMarker,
		"Infra failure", "exit 3",
		"says nothing about the change under test",
		"503 twice",
	} {
		if !strings.Contains(md, want) {
			t.Errorf("rendered infra-failure comment missing %q:\n%s", want, md)
		}
	}
	if strings.Contains(md, "| Metric |") {
		t.Errorf("infra-failure comment (no document) should not render a metric table:\n%s", md)
	}
}

func TestRenderUsageError(t *testing.T) {
	md := RenderInfraFailure(true, "--run is required", 64)
	for _, want := range []string{"Usage error", "exit 64", "--run is required"} {
		if !strings.Contains(md, want) {
			t.Errorf("rendered usage-error comment missing %q:\n%s", want, md)
		}
	}
}

// TestTypedAbsenceNeverRendersAsZero is the other load-bearing assertion:
// missing != zero. A metric OptionalNumber the server didn't report must show
// up as an explicit "not available", never as "0", "0.0", or a blank cell —
// per the schema doc's own rule verbatim.
func TestTypedAbsenceNeverRendersAsZero(t *testing.T) {
	doc := loadFixture(t, "typed-absent.json")
	md, err := Render(doc)
	if err != nil {
		t.Fatalf("Render: %v", err)
	}

	if strings.Count(md, "_not available_") < 3 {
		t.Fatalf("expected at least 3 typed-absent cells rendered as \"not available\", got:\n%s", md)
	}

	// The absences[] footnote must appear, without the renderer trying to
	// path-match each absence back to a table cell (the schema doc's own
	// guidance: "a single N fields unavailable footnote... without walking
	// the tree").
	if !strings.Contains(md, "3 field(s) not reported by the server") {
		t.Errorf("rendered comment missing the absences footnote:\n%s", md)
	}

	// Both directions, in adjacent cells of the same rows: the quality delta is
	// a genuine measured 0.0 and must render as a number, while the baseline
	// and candidate levels the server never reported must render as absent —
	// and the improved-case count is a real 0 next to an absent baseline.
	for _, tc := range []struct{ row, baseline, candidate, delta string }{
		{"Quality delta", "_not available_", "_not available_", "0 rate"},
		{"Improved cases", "_not available_", "0 count", "_not available_"},
	} {
		line := metricRow(t, md, tc.row)
		cells := strings.Split(line, "|")
		if len(cells) < 5 {
			t.Fatalf("row %q is not a 4-column metric row: %q", tc.row, line)
		}
		for i, want := range []string{tc.baseline, tc.candidate, tc.delta} {
			if got := strings.TrimSpace(cells[i+2]); got != want {
				t.Errorf("row %q cell %d = %q, want %q (line %q)", tc.row, i+2, got, want, line)
			}
		}
	}
}

func metricRow(t *testing.T, md, label string) string {
	t.Helper()
	for _, line := range strings.Split(md, "\n") {
		if strings.HasPrefix(line, "|") && strings.Contains(line, label) {
			return line
		}
	}
	t.Fatalf("no metric row for %q in:\n%s", label, md)
	return ""
}

func TestUnsupportedSchemaMajorIsRejected(t *testing.T) {
	for _, v := range []string{"something.else/v1", "", "o11y.eval.diff/vX"} {
		if _, err := schemaMajor(v); err == nil {
			t.Fatalf("schemaMajor(%q): expected an error for a malformed/foreign version string, got none", v)
		}
	}
	major, err := schemaMajor("o11y.eval.diff/v1")
	if err != nil || major != 1 {
		t.Fatalf("schemaMajor(o11y.eval.diff/v1) = (%d, %v), want (1, nil)", major, err)
	}
	major2, err := schemaMajor("o11y.eval.diff/v2")
	if err != nil || major2 != 2 {
		t.Fatalf("schemaMajor(o11y.eval.diff/v2) = (%d, %v), want (2, nil)", major2, err)
	}
	if major2 == supportedSchemaMajor {
		t.Fatalf("test fixture bug: v2 should not equal the currently supported major %d", supportedSchemaMajor)
	}
}

func TestLoadDocRejectsUnsupportedMajor(t *testing.T) {
	dir := t.TempDir()
	path := dir + "/v2.json"
	if err := os.WriteFile(path, []byte(`{"schema_version":"o11y.eval.diff/v2","verdict":{"outcome":"improvement","exit_code":0}}`), 0o600); err != nil {
		t.Fatalf("writing fixture: %v", err)
	}
	_, err := loadDoc(path)
	if err == nil {
		t.Fatal("loadDoc accepted an unsupported schema major, want an error")
	}
	var withCode interface{ ExitCode() int }
	if !errors.As(err, &withCode) {
		t.Fatalf("expected an error with an ExitCode(), got %v (%T)", err, err)
	}
	if withCode.ExitCode() != 1 {
		t.Fatalf("unsupportedSchemaError.ExitCode() = %d, want 1", withCode.ExitCode())
	}
}

// A document that declares identity.sample_count absent must not print a
// sample count for either side. The runner's current verb reports no per-side
// sample counts and says so in absences[]; rendering the zero-valued struct
// field anyway is the absent-as-zero bug moved out of the metrics table and
// into prose. The second half of this test pins the other direction: a
// document that does not declare the absence still gets its counts.
func TestAbsentSampleCountIsNotRenderedAsZero(t *testing.T) {
	doc := DiffDocument{
		SchemaVersion: "o11y.eval.diff/v1",
		Identity: Identity{
			Baseline:  EvalSide{EvaluationID: "cand_a"},
			Candidate: EvalSide{EvaluationID: "cand_b"},
		},
		Verdict:  Verdict{Decision: "RECOMMENDED", Outcome: OutcomeImprovement},
		Absences: []Absence{{Field: "identity.sample_count", Reason: "not_reported_by_server"}},
	}
	md, err := Render(doc)
	if err != nil {
		t.Fatalf("Render: %v", err)
	}
	if strings.Contains(md, "samples") {
		t.Errorf("document declares identity.sample_count absent; rendered a sample count anyway:\n%s", md)
	}

	reported := doc
	reported.Absences = nil
	reported.Identity.Baseline.SampleCount = 200
	reported.Identity.Candidate.SampleCount = 200
	md, err = Render(reported)
	if err != nil {
		t.Fatalf("Render: %v", err)
	}
	if !strings.Contains(md, "200 samples") {
		t.Errorf("document does not declare the absence; the sample count must still render:\n%s", md)
	}
}
