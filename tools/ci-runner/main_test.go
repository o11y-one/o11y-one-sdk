package main

import (
	"context"
	"encoding/json"
	"strings"
	"testing"
	"time"

	agenticv1 "github.com/o11y-one/o11y-one-sdk/gen/go/o11y_one/agentic/v1"
)

// The exit-code taxonomy is the runner's entire contract with CI. These numbers
// get baked into customers' workflow files, so a later renumbering is a breaking
// change to somebody's pipeline.
func TestOutcomeExitCodesAreStable(t *testing.T) {
	for _, tc := range []struct {
		outcome Outcome
		code    int
		name    string
	}{
		{OutcomeImprovement, 0, "improvement"},
		{OutcomeRegression, 1, "regression"},
		{OutcomeIndeterminate, 2, "indeterminate"},
		{OutcomeInfraFailure, 3, "infra-failure"},
		{OutcomeUsageError, 64, "usage-error"},
	} {
		if got := tc.outcome.ExitCode(); got != tc.code {
			t.Errorf("%s: exit code = %d, want %d", tc.name, got, tc.code)
		}
		if got := tc.outcome.String(); got != tc.name {
			t.Errorf("String() = %q, want %q", got, tc.name)
		}
	}
}

// The verdict mapping is the heart of the runner: the server decides, the runner
// only translates the decision into an exit code. The guarantee under test is
// that INDETERMINATE can never be coerced into pass or fail, and pass/fail can
// never be conjured from an absent decision.
func TestOutcomeForDecisionMapping(t *testing.T) {
	for _, tc := range []struct {
		decision agenticv1.ReleaseGateDecisionV1
		want     Outcome
		name     string
	}{
		{agenticv1.ReleaseGateDecisionV1_RELEASE_GATE_DECISION_V1_PASS, OutcomeImprovement, "pass->improvement"},
		{agenticv1.ReleaseGateDecisionV1_RELEASE_GATE_DECISION_V1_FAIL, OutcomeRegression, "fail->regression"},
		{agenticv1.ReleaseGateDecisionV1_RELEASE_GATE_DECISION_V1_INSUFFICIENT_DATA, OutcomeIndeterminate, "insufficient->indeterminate"},
		{agenticv1.ReleaseGateDecisionV1_RELEASE_GATE_DECISION_V1_UNSPECIFIED, OutcomeIndeterminate, "unspecified->indeterminate"},
	} {
		t.Run(tc.name, func(t *testing.T) {
			if got := outcomeForDecision(tc.decision); got != tc.want {
				t.Errorf("outcomeForDecision(%v) = %s, want %s", tc.decision, got, tc.want)
			}
		})
	}
}

// The seeded-indeterminate corpus: every decision that is not an explicit PASS or
// FAIL — INSUFFICIENT_DATA, UNSPECIFIED, and any unknown future enum value — must
// map to indeterminate and MUST NOT be coercible to improvement or regression.
func TestIndeterminateCannotBeCoerced(t *testing.T) {
	corpus := []agenticv1.ReleaseGateDecisionV1{
		agenticv1.ReleaseGateDecisionV1_RELEASE_GATE_DECISION_V1_UNSPECIFIED,
		agenticv1.ReleaseGateDecisionV1_RELEASE_GATE_DECISION_V1_INSUFFICIENT_DATA,
		agenticv1.ReleaseGateDecisionV1(42),  // an enum value this build does not know
		agenticv1.ReleaseGateDecisionV1(-1),  // a nonsense value
		agenticv1.ReleaseGateDecisionV1(999), // far out of range
	}
	for _, d := range corpus {
		got := outcomeForDecision(d)
		if got != OutcomeIndeterminate {
			t.Errorf("decision %d mapped to %s, want indeterminate", int32(d), got)
		}
		if got == OutcomeImprovement || got == OutcomeRegression {
			t.Errorf("decision %d was coerced to a verdict (%s)", int32(d), got)
		}
		if got.ExitCode() != 2 {
			t.Errorf("decision %d exit = %d, want 2", int32(d), got.ExitCode())
		}
	}
}

// buildDiffDocument reads the server's authoritative comparison; it never
// recomputes the verdict. This asserts the mapping end-to-end AND the typed
// absence contract L4 depends on: a nil optional is Present=false, a real 0.0 is
// Present=true with value 0.
func TestBuildDiffDocumentIndeterminateAndTypedAbsence(t *testing.T) {
	f := func(v float64) *float64 { return &v }
	cmp := &agenticv1.ReleaseGateEvaluationComparisonV1{
		Gate: &agenticv1.ReleaseGateV1{GateId: "gate_1"},
		BaselineEvaluation: &agenticv1.ReleaseGateEvaluationV1{
			EvaluationId:       "eval_base",
			GateId:             "gate_1",
			MetricName:         "answer_correctness",
			Decision:           agenticv1.ReleaseGateDecisionV1_RELEASE_GATE_DECISION_V1_PASS,
			CurrentAvgScore:    f(0.0), // a genuine measured zero, NOT absence
			CurrentSampleCount: 10,
			// CurrentAvgCostUsd left nil -> must serialize as absent
		},
		ComparisonEvaluation: &agenticv1.ReleaseGateEvaluationV1{
			EvaluationId:       "eval_cand",
			GateId:             "gate_1",
			MetricName:         "answer_correctness",
			Decision:           agenticv1.ReleaseGateDecisionV1_RELEASE_GATE_DECISION_V1_INSUFFICIENT_DATA,
			CurrentAvgScore:    f(0.5),
			CurrentSampleCount: 3,
		},
		DecisionChanged:      true,
		CurrentAvgScoreDelta: f(0.5),
		// CurrentAvgCostUsdDelta left nil -> absent delta
	}

	doc := buildDiffDocument(cmp, Generator{Tool: "o11y-eval", Version: "test"})

	if doc.SchemaVersion != SchemaVersion {
		t.Errorf("schema_version = %q, want %q", doc.SchemaVersion, SchemaVersion)
	}
	if doc.Verdict.Decision != "INSUFFICIENT_DATA" {
		t.Errorf("decision = %q, want INSUFFICIENT_DATA", doc.Verdict.Decision)
	}
	if doc.Verdict.Outcome != "indeterminate" || doc.Verdict.ExitCode != 2 {
		t.Errorf("outcome=%q exit=%d, want indeterminate/2", doc.Verdict.Outcome, doc.Verdict.ExitCode)
	}
	if !doc.Verdict.Authoritative {
		t.Error("verdict must be marked authoritative (server-decided)")
	}
	if doc.Verdict.Coercible {
		t.Error("verdict must be marked non-coercible")
	}

	// Typed absence: baseline score is a real 0.0; baseline cost is absent.
	baseScore := findMetric(t, doc, "avg_score").Baseline
	if !baseScore.Present || baseScore.Value == nil || *baseScore.Value != 0.0 {
		t.Errorf("baseline avg_score should be present zero, got %+v", baseScore)
	}
	baseCost := findMetric(t, doc, "avg_cost_usd").Baseline
	if baseCost.Present {
		t.Errorf("baseline avg_cost_usd should be absent, got %+v", baseCost)
	}
	costDelta := findMetric(t, doc, "avg_cost_usd").Delta
	if costDelta.Present {
		t.Errorf("avg_cost_usd delta should be absent, got %+v", costDelta)
	}
	scoreDelta := findMetric(t, doc, "avg_score").Delta
	if !scoreDelta.Present || scoreDelta.Value == nil || *scoreDelta.Value != 0.5 {
		t.Errorf("avg_score delta should be present 0.5, got %+v", scoreDelta)
	}

	// The absence must also be advertised in the absences list.
	if !hasAbsence(doc, "identity.baseline.avg_cost_usd") {
		t.Errorf("expected absence entry for baseline avg_cost_usd, got %+v", doc.Absences)
	}
}

// The document must survive a JSON round trip byte-for-byte: it is a wire
// contract, so marshal->unmarshal->marshal has to be stable.
func TestDiffDocumentRoundTrip(t *testing.T) {
	f := func(v float64) *float64 { return &v }
	cmp := &agenticv1.ReleaseGateEvaluationComparisonV1{
		Gate:                  &agenticv1.ReleaseGateV1{GateId: "gate_x"},
		BaselineEvaluation:    &agenticv1.ReleaseGateEvaluationV1{EvaluationId: "b", Decision: agenticv1.ReleaseGateDecisionV1_RELEASE_GATE_DECISION_V1_PASS, CurrentAvgScore: f(0.8)},
		ComparisonEvaluation:  &agenticv1.ReleaseGateEvaluationV1{EvaluationId: "c", Decision: agenticv1.ReleaseGateDecisionV1_RELEASE_GATE_DECISION_V1_FAIL, CurrentAvgScore: f(0.6)},
		CurrentAvgScoreDelta:  f(-0.2),
		AddedFailureReasons:   []string{"latency_regressed"},
		RemovedFailureReasons: []string{},
		BaselineSourceChanged: true,
	}
	doc := buildDiffDocument(cmp, Generator{Tool: "o11y-eval", Version: "test"})

	first, err := json.Marshal(doc)
	if err != nil {
		t.Fatalf("marshal: %v", err)
	}
	var back DiffDocument
	if err := json.Unmarshal(first, &back); err != nil {
		t.Fatalf("unmarshal: %v", err)
	}
	second, err := json.Marshal(back)
	if err != nil {
		t.Fatalf("re-marshal: %v", err)
	}
	if string(first) != string(second) {
		t.Errorf("round trip not stable:\n first=%s\nsecond=%s", first, second)
	}
	// FAIL candidate must render as regression/1.
	if back.Verdict.Outcome != "regression" || back.Verdict.ExitCode != 1 {
		t.Errorf("outcome=%q exit=%d, want regression/1", back.Verdict.Outcome, back.Verdict.ExitCode)
	}
}

// A wait that runs out of time is an infra-failure, never a verdict: a slow
// platform must not read as a bad change.
func TestWaitTimeoutIsInfraFailure(t *testing.T) {
	running := &agenticv1.EvaluationOperationV1{State: agenticv1.EvaluationOperationStateV1_EVALUATION_OPERATION_STATE_V1_RUNNING}
	fetch := func(ctx context.Context) (*agenticv1.EvaluationOperationV1, error) { return running, nil }

	_, err := waitForOperation(context.Background(), "wait", 2*time.Millisecond, 20*time.Millisecond, fetch)
	if err == nil {
		t.Fatal("expected a timeout error, got nil")
	}
	oc, ok := err.(interface{ Outcome() Outcome })
	if !ok || oc.Outcome() != OutcomeInfraFailure {
		t.Fatalf("timeout outcome = %v, want infra-failure", err)
	}
	if got := reportError(err); got != 3 {
		t.Fatalf("reportError(timeout) = %d, want 3", got)
	}
	if !strings.Contains(err.Error(), "timed out") {
		t.Errorf("timeout error should say so: %q", err.Error())
	}
}

// A run that reaches SUCCEEDED is a clean exit; FAILED/CANCELLED are infra
// failures (the machinery finished but produced nothing scoreable).
func TestWaitTerminalStates(t *testing.T) {
	seq := func(states ...agenticv1.EvaluationOperationStateV1) fetchOperation {
		i := 0
		return func(ctx context.Context) (*agenticv1.EvaluationOperationV1, error) {
			s := states[i]
			if i < len(states)-1 {
				i++
			}
			return &agenticv1.EvaluationOperationV1{State: s}, nil
		}
	}

	op, err := waitForOperation(context.Background(), "wait", time.Millisecond, time.Second,
		seq(
			agenticv1.EvaluationOperationStateV1_EVALUATION_OPERATION_STATE_V1_RUNNING,
			agenticv1.EvaluationOperationStateV1_EVALUATION_OPERATION_STATE_V1_SUCCEEDED,
		))
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if outErr := outcomeForOperation("wait", op); outErr != nil {
		t.Errorf("SUCCEEDED should map to nil (exit 0), got %v", outErr)
	}

	failed := &agenticv1.EvaluationOperationV1{State: agenticv1.EvaluationOperationStateV1_EVALUATION_OPERATION_STATE_V1_FAILED}
	outErr := outcomeForOperation("wait", failed)
	if outErr == nil {
		t.Fatal("FAILED should map to an infra-failure error")
	}
	oc, ok := outErr.(interface{ Outcome() Outcome })
	if !ok || oc.Outcome() != OutcomeInfraFailure {
		t.Errorf("FAILED outcome = %v, want infra-failure", outErr)
	}
}

// Argument validation happens before any credential or network work: a bad
// invocation is a usage error (64) and must not be masked by anything downstream.
func TestSubcommandFlagValidation(t *testing.T) {
	t.Setenv("O11Y_API_KEY", "o11y_mach.selector.secret")

	for _, tc := range []struct {
		name string
		args []string
		want int
	}{
		{"run without definition or preview-token", []string{"run"}, 64},
		{"wait without selector", []string{"wait"}, 64},
		{"wait with both selectors", []string{"wait", "--operation-id", "o1", "--idempotency-key", "k1"}, 64},
		{"diff without candidate", []string{"diff", "--baseline", "b1"}, 64},
		{"diff without baseline", []string{"diff", "--candidate", "c1"}, 64},
		{"annotate without title", []string{"annotate"}, 64},
		{"annotate with unknown kind", []string{"annotate", "--title", "t", "--kind", "nope"}, 64},
		{"annotate range without until", []string{"annotate", "--title", "t", "--kind", "range"}, 64},
		{"annotate with bad timestamp", []string{"annotate", "--title", "t", "--at", "yesterday"}, 64},
		{"unknown command", []string{"frobnicate"}, 64},
		{"no command", nil, 64},
	} {
		t.Run(tc.name, func(t *testing.T) {
			if got := run(tc.args); got != tc.want {
				t.Errorf("run(%v) = %d, want %d", tc.args, got, tc.want)
			}
		})
	}
}

// A valid invocation whose endpoint refuses the connection is an infra-failure
// (3), not a verdict and not a usage error. This proves the network wiring maps
// transport errors correctly without needing a live server.
func TestValidInvocationInfraFailureOffline(t *testing.T) {
	t.Setenv("O11Y_API_KEY", "o11y_mach.selector.secret")
	// 127.0.0.1:1 refuses immediately; a short timeout bounds the dial.
	base := []string{"--base-url", "http://127.0.0.1:1", "--timeout", "3s"}

	for _, tc := range []struct {
		name string
		args []string
	}{
		{"diff", append([]string{"diff"}, append(append([]string{}, base...), "--baseline", "b1", "--candidate", "c1")...)},
		{"annotate", append([]string{"annotate"}, append(append([]string{}, base...), "--title", "deploy abc123")...)},
		{"run", append([]string{"run"}, append(append([]string{}, base...), "--definition", "d1")...)},
	} {
		t.Run(tc.name, func(t *testing.T) {
			if got := run(tc.args); got != 3 {
				t.Errorf("run(%v) = %d, want 3 (infra-failure)", tc.args, got)
			}
		})
	}
}

func TestCredentialIsReadFromEnvAndStructurallyChecked(t *testing.T) {
	var c commonFlags

	t.Setenv("O11Y_API_KEY", "")
	if _, err := c.credential(); err == nil {
		t.Error("empty credential should be rejected")
	}

	t.Setenv("O11Y_API_KEY", "eyJhbGciOi.JWT.looking")
	if _, err := c.credential(); err == nil || !strings.Contains(err.Error(), "o11y_mach") {
		t.Errorf("a session token should be rejected with a pointed message, got %v", err)
	}

	t.Setenv("O11Y_API_KEY", "o11y_mach."+strings.Repeat("x", 200))
	if _, err := c.credential(); err == nil || !strings.Contains(err.Error(), "128") {
		t.Errorf("an oversized credential should name the limit, got %v", err)
	}

	t.Setenv("O11Y_API_KEY", "  o11y_mach.sel.sec  ")
	got, err := c.credential()
	if err != nil {
		t.Fatalf("valid credential rejected: %v", err)
	}
	if got != "o11y_mach.sel.sec" {
		t.Errorf("credential = %q, want it trimmed", got)
	}
}

// --- test helpers -----------------------------------------------------------

func findMetric(t *testing.T, doc DiffDocument, key string) DiffMetric {
	t.Helper()
	for _, m := range doc.Metrics {
		if m.Key == key {
			return m
		}
	}
	t.Fatalf("metric %q not found in document", key)
	return DiffMetric{}
}

func hasAbsence(doc DiffDocument, field string) bool {
	for _, a := range doc.Absences {
		if a.Field == field {
			return true
		}
	}
	return false
}
