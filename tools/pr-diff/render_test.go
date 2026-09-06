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
		"Improvement", "exit 0", "server decision: `PASS`",
		"Average score", "0.81 score", "0.86 score", "+0.05 score",
		"Sample count", "200 count",
		"Resolved failure reasons:", "`empty_answer`",
	} {
		if !strings.Contains(md, want) {
			t.Errorf("rendered improvement comment missing %q:\n%s", want, md)
		}
	}
	// A pass must not carry the indeterminate/regression callout language.
	for _, mustNot := range []string{"Indeterminate", "the gate failed on evidence", "not a pass"} {
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
		"Regression", "exit 1", "server decision: `FAIL`",
		"the gate failed on evidence",
		"-0.06 score",
		"decision flipped from PASS to FAIL",
		"New failure reasons:", "`latency_p95_regressed`",
		"the release-gate decision changed between the baseline and candidate evaluations",
	} {
		if !strings.Contains(md, want) {
			t.Errorf("rendered regression comment missing %q:\n%s", want, md)
		}
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
		"Indeterminate", "exit 2", "server decision: `INSUFFICIENT_DATA`",
		"no verdict reachable", "not a pass", "not coercible into a pass or fail",
		"Only 3 comparable cases",
	} {
		if !strings.Contains(md, want) {
			t.Errorf("rendered indeterminate comment missing %q:\n%s", want, md)
		}
	}
	if strings.Contains(md, "✅") {
		t.Errorf("indeterminate comment must not carry the pass emoji:\n%s", md)
	}
	if strings.Contains(md, "the gate failed on evidence") {
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
	md := RenderInfraFailure(true, "--baseline is required", 64)
	for _, want := range []string{"Usage error", "exit 64", "--baseline is required"} {
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

	// bad_outcomes_count's row has baseline and candidate both absent, but a
	// present delta of -3. Absence in the neighboring cells must not leak a
	// "0" into that row.
	for _, line := range strings.Split(md, "\n") {
		if !strings.HasPrefix(line, "|") || !strings.Contains(line, "Bad outcomes") {
			continue
		}
		cells := strings.Split(line, "|")
		for _, cell := range cells {
			trimmed := strings.TrimSpace(cell)
			if trimmed == "0" || trimmed == "0.0" || trimmed == "0count" {
				t.Errorf("absent cell rendered as zero in row %q: cell %q", line, trimmed)
			}
		}
		if !strings.Contains(line, "-3 count") {
			t.Errorf("Bad outcomes row should still show its present delta -3count: %q", line)
		}
	}
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
