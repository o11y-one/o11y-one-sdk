package main

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"net/http"
	"net/http/httptest"
	"os"
	"slices"
	"strings"
	"testing"
	"time"

	"connectrpc.com/connect"
	"google.golang.org/protobuf/proto"

	agenticv1 "github.com/o11y-one/o11y-one-sdk/gen/go/o11y_one/agentic/v1"
	"github.com/o11y-one/o11y-one-sdk/gen/go/o11y_one/agentic/v1/agenticv1connect"
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
// only translates the adopted decision into an exit code. The grid below is
// outcome x availability x candidate-match, because all three gate the verdict
// and the interesting bugs live where they disagree — a RECOMMENDED decision
// for a DIFFERENT candidate is not a pass for the candidate under test, and an
// unavailable decision is not a pass no matter what the revision says.
func TestOutcomeForAdoptedDecisionGrid(t *testing.T) {
	const under = "cand_under_test"

	for _, tc := range []struct {
		name         string
		availability agenticv1.MetricAvailabilityStateV1
		outcome      agenticv1.EvaluationDecisionOutcomeV1
		recommended  string
		nilDecision  bool
		nilAdopted   bool
		want         Outcome
	}{
		{name: "available/recommended/matching candidate", availability: availAvailable, outcome: outRecommended, recommended: under, want: OutcomeImprovement},
		{name: "available/recommended/other candidate", availability: availAvailable, outcome: outRecommended, recommended: "some_other", want: OutcomeIndeterminate},
		{name: "available/recommended/no candidate named", availability: availAvailable, outcome: outRecommended, want: OutcomeIndeterminate},
		{name: "available/blocked/matching candidate", availability: availAvailable, outcome: outBlocked, recommended: under, want: OutcomeRegression},
		{name: "available/blocked/other candidate", availability: availAvailable, outcome: outBlocked, recommended: "some_other", want: OutcomeRegression},
		{name: "available/no clear winner", availability: availAvailable, outcome: outNoClearWinner, want: OutcomeIndeterminate},
		{name: "available/insufficient evidence", availability: availAvailable, outcome: outInsufficient, want: OutcomeIndeterminate},
		{name: "available/unspecified", availability: availAvailable, outcome: outUnspecified, want: OutcomeIndeterminate},
		{name: "available/unknown future enum", availability: availAvailable, outcome: agenticv1.EvaluationDecisionOutcomeV1(42), want: OutcomeIndeterminate},
		{name: "not observed/recommended/matching candidate", availability: agenticv1.MetricAvailabilityStateV1_METRIC_AVAILABILITY_STATE_V1_NOT_OBSERVED, outcome: outRecommended, recommended: under, want: OutcomeIndeterminate},
		{name: "pending/recommended/matching candidate", availability: agenticv1.MetricAvailabilityStateV1_METRIC_AVAILABILITY_STATE_V1_PENDING, outcome: outRecommended, recommended: under, want: OutcomeIndeterminate},
		{name: "pending/blocked", availability: agenticv1.MetricAvailabilityStateV1_METRIC_AVAILABILITY_STATE_V1_PENDING, outcome: outBlocked, want: OutcomeIndeterminate},
		{name: "unspecified availability/recommended/matching candidate", availability: agenticv1.MetricAvailabilityStateV1_METRIC_AVAILABILITY_STATE_V1_UNSPECIFIED, outcome: outRecommended, recommended: under, want: OutcomeIndeterminate},
		{name: "available/no revision at all", availability: availAvailable, nilDecision: true, want: OutcomeIndeterminate},
		{name: "no adopted decision at all", nilAdopted: true, want: OutcomeIndeterminate},
	} {
		t.Run(tc.name, func(t *testing.T) {
			var ad *agenticv1.EvaluationAdoptedDecisionV1
			if !tc.nilAdopted {
				ad = adoptedDecision(tc.availability, tc.outcome, tc.recommended)
				if tc.nilDecision {
					ad.Revision = nil
				}
			}
			if got := outcomeForAdoptedDecision(ad, under); got != tc.want {
				t.Errorf("outcomeForAdoptedDecision = %s, want %s", got, tc.want)
			}
		})
	}
}

// The seeded-indeterminate corpus: every decision that is not an explicit
// RECOMMENDED-for-this-candidate or BLOCKED must map to indeterminate and MUST
// NOT be coercible to improvement or regression.
func TestIndeterminateCannotBeCoerced(t *testing.T) {
	const under = "cand_under_test"
	corpus := []agenticv1.EvaluationDecisionOutcomeV1{
		outUnspecified,
		outNoClearWinner,
		outInsufficient,
		agenticv1.EvaluationDecisionOutcomeV1(42),  // an enum value this build does not know
		agenticv1.EvaluationDecisionOutcomeV1(-1),  // a nonsense value
		agenticv1.EvaluationDecisionOutcomeV1(999), // far out of range
	}
	for _, o := range corpus {
		// Even with the decision marked AVAILABLE and this candidate named as
		// the recommendation, a non-RECOMMENDED outcome stays indeterminate.
		got := outcomeForAdoptedDecision(adoptedDecision(availAvailable, o, under), under)
		if got != OutcomeIndeterminate {
			t.Errorf("outcome %d mapped to %s, want indeterminate", int32(o), got)
		}
		if got == OutcomeImprovement || got == OutcomeRegression {
			t.Errorf("outcome %d was coerced to a verdict (%s)", int32(o), got)
		}
		if got.ExitCode() != 2 {
			t.Errorf("outcome %d exit = %d, want 2", int32(o), got.ExitCode())
		}
	}
}

// buildDiffDocument reads the run's adopted decision; it never recomputes the
// verdict. This asserts the mapping end-to-end AND the typed absence contract L4
// depends on: a nil optional is Present=false, a real 0.0 is Present=true with
// value 0.
func TestBuildDiffDocumentIndeterminateAndTypedAbsence(t *testing.T) {
	const under = "cand_b"

	ad := adoptedDecision(availAvailable, outNoClearWinner, "")
	ad.Revision.Decision.ReferenceCandidateKey = strptr("cand_a")
	ad.Revision.Decision.Tradeoffs = []*agenticv1.CandidateTradeoffV1{
		{
			CandidateKey:       under,
			QualityDelta:       0.0, // a genuine measured zero, NOT absence
			ImprovedCaseCount:  0,
			RegressedCaseCount: 4,
			// CostDelta left nil -> must serialize as absent
		},
	}

	resp := &agenticv1.GetEvaluationRunOverviewResponse{AdoptedDecision: ad}
	doc := buildDiffDocument(resp, under, Generator{Tool: "o11y-eval", Version: "test"})

	if doc.SchemaVersion != SchemaVersion {
		t.Errorf("schema_version = %q, want %q", doc.SchemaVersion, SchemaVersion)
	}
	if doc.Verdict.Decision != "NO_CLEAR_WINNER" {
		t.Errorf("decision = %q, want NO_CLEAR_WINNER", doc.Verdict.Decision)
	}
	if doc.Verdict.DecisionSource != "server:GetEvaluationRunOverview.adopted_decision" {
		t.Errorf("decision_source = %q, want the run-overview adopted decision", doc.Verdict.DecisionSource)
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

	// Both sides are named by candidate key: the reference the server compared
	// against, and the candidate this invocation put under test.
	if doc.Identity.Baseline.EvaluationID != "cand_a" || doc.Identity.Candidate.EvaluationID != under {
		t.Errorf("identity sides = %q / %q, want cand_a / %s",
			doc.Identity.Baseline.EvaluationID, doc.Identity.Candidate.EvaluationID, under)
	}

	// Typed absence: quality delta is a real 0.0; cost delta is absent.
	qd := findMetric(t, doc, "quality_delta").Delta
	if !qd.Present || qd.Value == nil || *qd.Value != 0.0 {
		t.Errorf("quality_delta should be present zero, got %+v", qd)
	}
	cd := findMetric(t, doc, "cost_delta_usd").Delta
	if cd.Present {
		t.Errorf("cost_delta_usd should be absent, got %+v", cd)
	}
	regressed := findMetric(t, doc, "regressed_case_count").Candidate
	if !regressed.Present || regressed.Value == nil || *regressed.Value != 4 {
		t.Errorf("regressed_case_count should be present 4, got %+v", regressed)
	}

	// The absence must also be advertised in the absences list: this verb has no
	// decision-changed concept and reports no per-side sample counts.
	for _, field := range []string{"verdict.decision_changed", "identity.sample_count"} {
		if !hasAbsence(doc, field) {
			t.Errorf("expected absence entry for %s, got %+v", field, doc.Absences)
		}
	}
}

// An adopted decision the server could not make available is the indeterminate
// arm, and the document has to say why rather than render an empty verdict that
// reads like a pass.
func TestBuildDiffDocumentUnavailableDecisionIsExplained(t *testing.T) {
	ad := adoptedDecision(agenticv1.MetricAvailabilityStateV1_METRIC_AVAILABILITY_STATE_V1_PENDING, outRecommended, "cand_b")
	ad.Availability.ReasonCode = strptr("decision_not_yet_adopted")

	doc := buildDiffDocument(&agenticv1.GetEvaluationRunOverviewResponse{AdoptedDecision: ad}, "cand_b",
		Generator{Tool: "o11y-eval", Version: "test"})

	if doc.Verdict.ExitCode != 2 {
		t.Errorf("exit = %d, want 2 — an unavailable decision is never a pass", doc.Verdict.ExitCode)
	}
	if !hasAbsence(doc, "verdict.decision") {
		t.Errorf("an unavailable decision must be listed as an absence, got %+v", doc.Absences)
	}
	var found bool
	for _, a := range doc.Absences {
		if a.Field == "verdict.decision" && a.Reason == "decision_not_yet_adopted" {
			found = true
		}
	}
	if !found {
		t.Errorf("the absence must carry the server's reason code, got %+v", doc.Absences)
	}
	if len(doc.Notes) == 0 {
		t.Error("an unavailable decision must be noted for the PR comment")
	}
}

// The document must survive a JSON round trip byte-for-byte: it is a wire
// contract, so marshal->unmarshal->marshal has to be stable.
func TestDiffDocumentRoundTrip(t *testing.T) {
	ad := adoptedDecision(availAvailable, outBlocked, "")
	ad.Revision.Decision.ReferenceCandidateKey = strptr("cand_a")
	ad.Revision.Decision.Blockers = []*agenticv1.DecisionBlockerV1{
		{Kind: agenticv1.DecisionBlockerKindV1_DECISION_BLOCKER_KIND_V1_MAX_COST_EXCEEDED, CandidateKey: "cand_b"},
		{Kind: agenticv1.DecisionBlockerKindV1_DECISION_BLOCKER_KIND_V1_MIN_SCORE_NOT_MET, CandidateKey: "someone_else"},
	}
	ad.Revision.Decision.Tradeoffs = []*agenticv1.CandidateTradeoffV1{
		{CandidateKey: "cand_b", QualityDelta: -0.2, CostDelta: &agenticv1.CostAmountV1{AmountMicros: 1_500_000, CurrencyCode: "USD"}},
	}
	doc := buildDiffDocument(&agenticv1.GetEvaluationRunOverviewResponse{AdoptedDecision: ad}, "cand_b",
		Generator{Tool: "o11y-eval", Version: "test"})

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
	// A BLOCKED decision must render as regression/1.
	if back.Verdict.Outcome != "regression" || back.Verdict.ExitCode != 1 {
		t.Errorf("outcome=%q exit=%d, want regression/1", back.Verdict.Outcome, back.Verdict.ExitCode)
	}
	// Only the blockers for the candidate under test are this candidate's
	// failure reasons; another candidate's blocker is not.
	if len(back.FailureReasons.Added) != 1 || back.FailureReasons.Added[0] != "MAX_COST_EXCEEDED" {
		t.Errorf("failure reasons = %v, want only this candidate's blocker", back.FailureReasons.Added)
	}
	// Cost is reported in USD, not micros: 1_500_000 micros is $1.50.
	cd := findMetric(t, back, "cost_delta_usd").Delta
	if !cd.Present || cd.Value == nil || *cd.Value != 1.5 {
		t.Errorf("cost_delta_usd = %+v, want present 1.5", cd)
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
		{"diff without candidate", []string{"diff", "--run", "run_1"}, 64},
		{"diff without run", []string{"diff", "--candidate", "cand_b"}, 64},
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
		{"diff", append([]string{"diff"}, append(append([]string{}, base...), "--run", "run_1", "--candidate", "cand_b")...)},
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

// The API serves gRPC and gRPC-web, not the Connect protocol.
func TestClientSpeaksGRPCWeb(t *testing.T) {
	var contentType, path string
	srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		contentType, path = r.Header.Get("Content-Type"), r.URL.Path
		// A gRPC-web trailers-only error: no body to hand-encode.
		w.Header().Set("Content-Type", "application/grpc-web+proto")
		w.Header().Set("Grpc-Status", "7")
	}))
	defer srv.Close()

	clients := newClients(&commonFlags{baseURL: srv.URL}, "o11y_mach.sel.sec")
	_, err := clients.eval.GetEvaluationRunOverview(context.Background(),
		connect.NewRequest(&agenticv1.GetEvaluationRunOverviewRequest{}))

	if contentType != "application/grpc-web+proto" {
		t.Errorf("content-type = %q, want application/grpc-web+proto", contentType)
	}
	if want := "/o11y_one.agentic.v1.AgenticEvaluationService/GetEvaluationRunOverview"; path != want {
		t.Errorf("path = %q, want %q", path, want)
	}
	if connect.CodeOf(err) != connect.CodePermissionDenied {
		t.Errorf("err = %v, want permission_denied read off the gRPC-web status", err)
	}
}

// CreateEvaluationRun has no definition-only launch: it refuses any token its
// preview did not mint for that definition. `run --definition` must preview the
// definition as it stands and launch with the token that preview returned.
func TestRunDefinitionPreviewsThenLaunchesWithTheMintedToken(t *testing.T) {
	f := &fakeEval{keys: map[string]bool{}}
	code, _, stderr := runCaptured(t, "run", append(serveFake(t, f), "--definition", "d1", "--idempotency-key", "k1")...)

	if code != 0 {
		t.Fatalf("exit = %d, want 0; stderr: %s", code, stderr)
	}
	// Current revision, the definition's own mode, no live-trace override.
	want := &agenticv1.PreviewEvaluationRunRequest{DefinitionId: "d1"}
	if len(f.previews) != 1 || !proto.Equal(f.previews[0], want) {
		t.Errorf("PreviewEvaluationRun requests = %v, want exactly %v", f.previews, want)
	}
	if want := []string{"pv:d1:1"}; !slices.Equal(f.creates, want) {
		t.Errorf("CreateEvaluationRun tokens = %q, want %q", f.creates, want)
	}
}

// A preview that does not allow the launch is the platform saying no: no run is
// created, so there is no verdict to reach (exit 2), and the blockers are the
// only thing that tells the pipeline owner what to fix.
func TestRunDefinitionBlockedPreviewDoesNotLaunch(t *testing.T) {
	f := &fakeEval{keys: map[string]bool{}, blockers: []*agenticv1.EvaluationPreviewBlockerV1{{
		Kind:     agenticv1.EvaluationPreviewBlockerKindV1_EVALUATION_PREVIEW_BLOCKER_KIND_V1_MISSING_DEPENDENCY,
		Severity: agenticv1.EvaluationBuilderReadinessSeverityV1_EVALUATION_BUILDER_READINESS_SEVERITY_V1_BLOCKING,
		Detail:   "dataset version 7 was archived",
	}}}
	code, _, stderr := runCaptured(t, "run", append(serveFake(t, f), "--definition", "d1", "--idempotency-key", "k1")...)

	if code != 2 {
		t.Fatalf("exit = %d, want 2 (indeterminate); stderr: %s", code, stderr)
	}
	if len(f.creates) != 0 {
		t.Errorf("CreateEvaluationRun was called %d times after a blocked preview", len(f.creates))
	}
	for _, want := range []string{"MISSING_DEPENDENCY", "dataset version 7 was archived"} {
		if !strings.Contains(stderr, want) {
			t.Errorf("stderr %q does not name the blocker (%q)", stderr, want)
		}
	}
}

// A caller that passes --preview-token has already previewed; a second preview
// would launch against a token they never saw.
func TestRunPreviewTokenSkipsThePreview(t *testing.T) {
	f := &fakeEval{keys: map[string]bool{}}
	code, _, stderr := runCaptured(t, "run", append(serveFake(t, f), "--definition", "d1", "--preview-token", "pv:d1:caller", "--idempotency-key", "k1")...)

	if code != 0 {
		t.Fatalf("exit = %d, want 0; stderr: %s", code, stderr)
	}
	if len(f.previews) != 0 {
		t.Errorf("PreviewEvaluationRun was called %d times despite --preview-token", len(f.previews))
	}
	if want := []string{"pv:d1:caller"}; !slices.Equal(f.creates, want) {
		t.Errorf("CreateEvaluationRun tokens = %q, want %q", f.creates, want)
	}
}

// A retried pipeline re-runs `run` with the same key. Each attempt mints a fresh
// token, but an unchanged definition resolves to the same accepted preview
// digest, so the second launch replays the first instead of failing.
func TestRunDefinitionRetryWithTheSameKeyReplays(t *testing.T) {
	f := &fakeEval{keys: map[string]bool{}}
	base := serveFake(t, f)
	var outs []string
	for range 2 {
		code, stdout, stderr := runCaptured(t, "run", append(base, "--definition", "d1", "--idempotency-key", "sha1")...)
		if code != 0 {
			t.Fatalf("exit = %d, want 0; stderr: %s", code, stderr)
		}
		outs = append(outs, stdout)
	}

	if want := []string{"pv:d1:1", "pv:d1:2"}; !slices.Equal(f.creates, want) {
		t.Errorf("CreateEvaluationRun tokens = %q, want a fresh token per attempt %q", f.creates, want)
	}
	if !strings.Contains(outs[0], "idempotent_replay=false") || !strings.Contains(outs[1], "idempotent_replay=true") {
		t.Errorf("replay not reported: first %q, second %q", outs[0], outs[1])
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

// --- adopted-decision fixtures ----------------------------------------------

const (
	availAvailable   = agenticv1.MetricAvailabilityStateV1_METRIC_AVAILABILITY_STATE_V1_AVAILABLE
	outUnspecified   = agenticv1.EvaluationDecisionOutcomeV1_EVALUATION_DECISION_OUTCOME_V1_UNSPECIFIED
	outRecommended   = agenticv1.EvaluationDecisionOutcomeV1_EVALUATION_DECISION_OUTCOME_V1_RECOMMENDED
	outNoClearWinner = agenticv1.EvaluationDecisionOutcomeV1_EVALUATION_DECISION_OUTCOME_V1_NO_CLEAR_WINNER
	outInsufficient  = agenticv1.EvaluationDecisionOutcomeV1_EVALUATION_DECISION_OUTCOME_V1_INSUFFICIENT_EVIDENCE
	outBlocked       = agenticv1.EvaluationDecisionOutcomeV1_EVALUATION_DECISION_OUTCOME_V1_BLOCKED
)

func strptr(s string) *string { return &s }

// adoptedDecision builds the one server message the runner's verdict reads.
// recommended == "" leaves recommended_candidate_key unset, which is a different
// state from "set to the empty string" and has to stay so.
func adoptedDecision(state agenticv1.MetricAvailabilityStateV1, outcome agenticv1.EvaluationDecisionOutcomeV1, recommended string) *agenticv1.EvaluationAdoptedDecisionV1 {
	d := &agenticv1.EvaluationDecisionV1{Outcome: outcome}
	if recommended != "" {
		d.RecommendedCandidateKey = strptr(recommended)
	}
	return &agenticv1.EvaluationAdoptedDecisionV1{
		Availability: &agenticv1.MetricAvailabilityV1{State: state},
		Revision:     &agenticv1.EvaluationDecisionRevisionV1{Decision: d},
	}
}

// --- launch-path fake -------------------------------------------------------

// fakeEval is the evaluation service's launch path, served by the real
// generated handler so the client's gRPC-web framing is exercised. Like the
// server (o11y-api run_handlers.rs:170-174), CreateEvaluationRun refuses a
// token its preview did not mint for that definition.
type fakeEval struct {
	agenticv1connect.UnimplementedAgenticEvaluationServiceHandler
	blockers []*agenticv1.EvaluationPreviewBlockerV1
	previews []*agenticv1.PreviewEvaluationRunRequest
	creates  []string        // the preview token each launch carried
	keys     map[string]bool // idempotency keys that launched
}

func (f *fakeEval) PreviewEvaluationRun(_ context.Context, req *connect.Request[agenticv1.PreviewEvaluationRunRequest]) (*connect.Response[agenticv1.PreviewEvaluationRunResponse], error) {
	f.previews = append(f.previews, req.Msg)
	return connect.NewResponse(&agenticv1.PreviewEvaluationRunResponse{
		// Fresh per preview, as the server's carries a fresh expiry.
		PreviewToken:  fmt.Sprintf("pv:%s:%d", req.Msg.GetDefinitionId(), len(f.previews)),
		LaunchAllowed: len(f.blockers) == 0,
		Blockers:      f.blockers,
	}), nil
}

func (f *fakeEval) CreateEvaluationRun(_ context.Context, req *connect.Request[agenticv1.CreateEvaluationRunRequest]) (*connect.Response[agenticv1.CreateEvaluationRunResponse], error) {
	m := req.Msg
	f.creates = append(f.creates, m.GetPreviewToken())
	if !strings.HasPrefix(m.GetPreviewToken(), "pv:"+m.GetDefinitionId()+":") {
		return nil, connect.NewError(connect.CodeFailedPrecondition, errors.New("preview token is malformed"))
	}
	// A reused key replays: the server compares the re-resolved binding's
	// digest, which carries no nonce and no expiry (run_domain.rs:81-100), so a
	// fresh preview of an unchanged definition matches the accepted one.
	replay := f.keys[m.GetIdempotencyKey()]
	f.keys[m.GetIdempotencyKey()] = true
	return connect.NewResponse(&agenticv1.CreateEvaluationRunResponse{
		Run: &agenticv1.EvaluationRunV1{EvaluationRunId: "run_" + m.GetIdempotencyKey()},
		Operation: &agenticv1.EvaluationOperationV1{
			OperationId: "op_" + m.GetIdempotencyKey(),
			State:       agenticv1.EvaluationOperationStateV1_EVALUATION_OPERATION_STATE_V1_PENDING,
		},
		IdempotentReplay: replay,
	}), nil
}

// serveFake starts f and returns the flags that point the runner at it.
func serveFake(t *testing.T, f *fakeEval) []string {
	t.Helper()
	t.Setenv("O11Y_API_KEY", "o11y_mach.selector.secret")
	mux := http.NewServeMux()
	mux.Handle(agenticv1connect.NewAgenticEvaluationServiceHandler(f))
	srv := httptest.NewServer(mux)
	t.Cleanup(srv.Close)
	return []string{"--base-url", srv.URL, "--timeout", "10s"}
}

// runCaptured runs the CLI and returns its exit code, stdout and stderr.
func runCaptured(t *testing.T, command string, args ...string) (int, string, string) {
	t.Helper()
	var files [2]*os.File
	for i := range files {
		f, err := os.CreateTemp(t.TempDir(), "out")
		if err != nil {
			t.Fatal(err)
		}
		files[i] = f
	}
	stdout, stderr := os.Stdout, os.Stderr
	os.Stdout, os.Stderr = files[0], files[1]
	code := run(append([]string{command}, args...))
	os.Stdout, os.Stderr = stdout, stderr

	var got [2]string
	for i, f := range files {
		b, err := os.ReadFile(f.Name())
		if err != nil {
			t.Fatal(err)
		}
		got[i] = string(b)
		f.Close()
	}
	return code, got[0], got[1]
}
