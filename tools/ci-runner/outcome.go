package main

import "fmt"

// Outcome is the typed verdict this runner returns to CI, and its integer value
// IS the process exit code. CI systems only see the exit code, so the taxonomy
// has to live in the number itself rather than in log output nobody parses.
//
// The distinction that matters — and the reason this is an enum and not a
// bool — is between "the server said this candidate is blocked" (Regression)
// and "the server did not say" (Indeterminate) and "the machinery broke"
// (InfraFailure). Collapsing the last two into the first turns a flaky network
// into a blocked merge and trains people to bypass the check; collapsing them
// into success makes it a decoration.
//
// Every one of these comes from a single fact — the run's adopted decision, as
// GetEvaluationRunOverview reports it. The runner translates that decision; it
// never thresholds, averages, or otherwise recomputes one. See
// outcomeForAdoptedDecision in diffdoc.go, which is the only place the mapping
// below is applied.
type Outcome int

const (
	// OutcomeImprovement: the server's adopted decision is available AND
	// explicitly RECOMMENDED, naming the candidate this invocation put under
	// test. Nothing weaker earns it. Zero, so `set -e` and every CI default
	// treat it as success without special-casing.
	OutcomeImprovement Outcome = 0

	// OutcomeRegression: the server's adopted decision is available and
	// explicitly BLOCKED. This is the only exit code that means "this change is
	// bad", and only the server can say so.
	OutcomeRegression Outcome = 1

	// OutcomeIndeterminate: everything else — a decision that is PENDING,
	// NOT_OBSERVED or absent, a RECOMMENDED naming some other candidate,
	// NO_CLEAR_WINNER, INSUFFICIENT_EVIDENCE, or an enum this build does not
	// recognise. NOT a regression, and never a pass. Whether it blocks a merge
	// is a policy decision for the calling workflow, which is exactly why it
	// gets its own code instead of being folded into 1.
	OutcomeIndeterminate Outcome = 2

	// OutcomeInfraFailure: the runner or the platform failed — network,
	// authentication, an unimplemented path. Says nothing about the change under
	// test. A workflow that blocks merges on this is blocking on its own
	// plumbing.
	OutcomeInfraFailure Outcome = 3

	// OutcomeUsageError: the invocation itself was wrong (bad flags, missing
	// required argument). 64 is EX_USAGE from sysexits.h — deliberately outside
	// the verdict range so it can never be mistaken for one.
	OutcomeUsageError Outcome = 64
)

func (o Outcome) String() string {
	switch o {
	case OutcomeImprovement:
		return "improvement"
	case OutcomeRegression:
		return "regression"
	case OutcomeIndeterminate:
		return "indeterminate"
	case OutcomeInfraFailure:
		return "infra-failure"
	case OutcomeUsageError:
		return "usage-error"
	default:
		return fmt.Sprintf("unknown(%d)", int(o))
	}
}

// ExitCode is the process exit status for this outcome.
func (o Outcome) ExitCode() int { return int(o) }
