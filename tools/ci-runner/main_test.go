package main

import (
	"strings"
	"testing"
)

// The exit-code taxonomy is the runner's entire contract with CI. Nothing else
// about this scaffold is worth testing yet, and this is worth testing now:
// these numbers get baked into customers' workflow files, so a later
// renumbering is a breaking change to somebody's pipeline.
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

func TestNotImplementedIsInfraFailureNotSuccess(t *testing.T) {
	// A stub that exits 0 is a gate that silently passes. That is the single
	// worst thing this binary could do, so it is asserted rather than assumed.
	err := &errNotImplemented{subcommand: "diff", blockedOn: "the RPC does not exist yet"}
	if got := err.Outcome(); got != OutcomeInfraFailure {
		t.Fatalf("not-implemented outcome = %s, want infra-failure", got)
	}
	if got := reportError(err); got != 3 {
		t.Fatalf("reportError = %d, want 3", got)
	}
	if !strings.Contains(err.Error(), "not implemented") {
		t.Errorf("error message should say so plainly: %q", err.Error())
	}
}

func TestSubcommandsValidateFlagsBeforeClaimingNotImplemented(t *testing.T) {
	// Argument validation must happen first: "you forgot --run-id" is a usage
	// error (64) and must not be masked by the not-implemented infra failure.
	t.Setenv("O11Y_API_KEY", "o11y_mach.selector.secret")

	for _, tc := range []struct {
		name string
		args []string
		want int
	}{
		{"run without definition", []string{"run"}, 64},
		{"wait without run-id", []string{"wait"}, 64},
		{"diff without baseline", []string{"diff", "--run-id", "r1"}, 64},
		{"diff with out-of-range tolerance", []string{"diff", "--run-id", "r1", "--baseline", "main", "--tolerance", "2"}, 64},
		{"annotate with unknown kind", []string{"annotate", "--title", "t", "--kind", "nope"}, 64},
		{"annotate range without until", []string{"annotate", "--title", "t", "--kind", "range"}, 64},
		{"annotate with bad timestamp", []string{"annotate", "--title", "t", "--at", "yesterday"}, 64},
		{"unknown command", []string{"frobnicate"}, 64},
		{"no command", nil, 64},

		// Valid invocations reach the honest stub.
		{"valid run", []string{"run", "--definition", "d1"}, 3},
		{"valid wait", []string{"wait", "--run-id", "r1"}, 3},
		{"valid diff", []string{"diff", "--run-id", "r1", "--baseline", "main"}, 3},
		{"valid annotate", []string{"annotate", "--title", "deploy abc123"}, 3},
	} {
		t.Run(tc.name, func(t *testing.T) {
			if got := run(tc.args); got != tc.want {
				t.Errorf("run(%v) = %d, want %d", tc.args, got, tc.want)
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
