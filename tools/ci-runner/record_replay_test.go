package main

import (
	"encoding/json"
	"strings"
	"testing"

	agenticv1 "github.com/o11y-one/o11y-one-sdk/gen/go/o11y_one/agentic/v1"
)

// The runner never executes a harness; the SDK tape records and replays.
// --record and --replay only assert, from the previewed manifest, that the
// candidate the harness step will lease is the kind that mode needs.
func tapeManifest() *agenticv1.EvaluationRunManifestV1 {
	return &agenticv1.EvaluationRunManifestV1{Candidates: []*agenticv1.EvaluationCandidateV1{
		{CandidateKey: "ext", Config: &agenticv1.EvaluationCandidateV1_ExternallyExecuted{
			ExternallyExecuted: &agenticv1.ExternallyExecutedCandidateV1{RuntimeKey: "rt"},
		}},
		{CandidateKey: "rep", Config: &agenticv1.EvaluationCandidateV1_Replay{Replay: &agenticv1.ReplayCandidateV1{
			Execution:             &agenticv1.ExternallyExecutedCandidateV1{RuntimeKey: "rt"},
			SourceEvaluationRunId: "run_src",
			SourceCandidateKey:    "cand_src",
		}}},
		{CandidateKey: "pp", Config: &agenticv1.EvaluationCandidateV1_ProviderPrompt{
			ProviderPrompt: &agenticv1.ProviderPromptCandidateV1{},
		}},
	}}
}

func TestRunRecordReplayFlagMisuseIsAUsageError(t *testing.T) {
	t.Setenv("O11Y_API_KEY", "o11y_mach.selector.secret")
	for _, tc := range []struct {
		name string
		args []string
	}{
		{"record and replay together", []string{"run", "--definition", "d1", "--candidate", "ext", "--record", "--replay"}},
		{"record without candidate", []string{"run", "--definition", "d1", "--record"}},
		{"replay without candidate", []string{"run", "--definition", "d1", "--replay"}},
		{"candidate without a mode", []string{"run", "--definition", "d1", "--candidate", "ext"}},
		{"replay with a caller's preview token", []string{"run", "--definition", "d1", "--preview-token", "pv:d1:x", "--candidate", "rep", "--replay"}},
	} {
		t.Run(tc.name, func(t *testing.T) {
			if got := run(tc.args); got != 64 {
				t.Errorf("run(%v) = %d, want 64", tc.args, got)
			}
		})
	}
}

func TestRunReplayAssertsAReplayCandidateAndNamesItsSource(t *testing.T) {
	f := &fakeEval{keys: map[string]bool{}, manifest: tapeManifest()}
	code, stdout, stderr := runCaptured(t, "run", append(serveFake(t, f), "--definition", "d1", "--idempotency-key", "k1", "--candidate", "rep", "--replay")...)

	if code != 0 {
		t.Fatalf("exit = %d, want 0; stderr: %s", code, stderr)
	}
	for _, want := range []string{"candidate_key=rep", "mode=replay", "source_evaluation_run_id=run_src", "source_candidate_key=cand_src"} {
		if !strings.Contains(stdout, want) {
			t.Errorf("stdout %q does not carry %q", stdout, want)
		}
	}
	if len(f.creates) != 1 {
		t.Errorf("CreateEvaluationRun calls = %d, want 1", len(f.creates))
	}
}

func TestRunRecordAssertsAnExternallyExecutedCandidate(t *testing.T) {
	f := &fakeEval{keys: map[string]bool{}, manifest: tapeManifest()}
	code, stdout, stderr := runCaptured(t, "run", append(serveFake(t, f), "--definition", "d1", "--idempotency-key", "k1", "--candidate", "ext", "--record", "--json")...)

	if code != 0 {
		t.Fatalf("exit = %d, want 0; stderr: %s", code, stderr)
	}
	var out map[string]any
	if err := json.Unmarshal([]byte(stdout), &out); err != nil {
		t.Fatalf("stdout is not JSON: %v\n%s", err, stdout)
	}
	if out["candidate_key"] != "ext" || out["mode"] != "record" {
		t.Errorf("JSON = %v, want candidate_key=ext mode=record", out)
	}
	if _, ok := out["source_evaluation_run_id"]; ok {
		t.Errorf("a record run names no replay source: %v", out)
	}
}

// A candidate the manifest does not hold, or holds as another kind, launches
// nothing: the fix is the invocation or the definition.
func TestRunRecordReplayWrongCandidateLaunchesNothing(t *testing.T) {
	for _, tc := range []struct {
		name, candidate, mode, wantErr string
	}{
		{"replay on an externally executed candidate", "ext", "--replay", `candidate "ext" is not a replay candidate`},
		{"record on a replay candidate", "rep", "--record", `candidate "rep" is not an externally executed candidate`},
		{"record on a provider prompt", "pp", "--record", `candidate "pp" is not an externally executed candidate`},
		{"a candidate the definition does not hold", "nope", "--replay", `definition d1 has no candidate "nope"`},
	} {
		t.Run(tc.name, func(t *testing.T) {
			f := &fakeEval{keys: map[string]bool{}, manifest: tapeManifest()}
			code, _, stderr := runCaptured(t, "run", append(serveFake(t, f), "--definition", "d1", "--idempotency-key", "k1", "--candidate", tc.candidate, tc.mode)...)
			if code != 64 {
				t.Errorf("exit = %d, want 64; stderr: %s", code, stderr)
			}
			if len(f.creates) != 0 {
				t.Errorf("CreateEvaluationRun was called %d times", len(f.creates))
			}
			if !strings.Contains(stderr, tc.wantErr) {
				t.Errorf("stderr %q does not say %q", stderr, tc.wantErr)
			}
		})
	}
}
