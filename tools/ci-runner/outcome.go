package main

import "fmt"

// Outcome is the typed verdict this runner returns to CI, and its integer value
// IS the process exit code. CI systems only see the exit code, so the taxonomy
// has to live in the number itself rather than in log output nobody parses.
//
// The distinction that matters — and the reason this is an enum and not a
// bool — is between "the evidence says the change is worse" (Regression) and
// "there is not enough evidence to say" (Indeterminate) and "the machinery
// broke" (InfraFailure). Collapsing the last two into the first turns a flaky
// network into a blocked merge and trains people to bypass the gate; collapsing
// them into success makes the gate a decoration.
type Outcome int

const (
	// OutcomeImprovement: the gate passes. Quality improved, or held within the
	// configured tolerance. Zero, so `set -e` and every CI default treat it as
	// success without special-casing.
	OutcomeImprovement Outcome = 0

	// OutcomeRegression: the gate fails on evidence. A comparison completed and
	// the result is worse than the baseline by more than the tolerance. This is
	// the only exit code that means "this change is bad".
	OutcomeRegression Outcome = 1

	// OutcomeIndeterminate: the comparison could not reach a verdict — too few
	// cases, a baseline that does not exist yet, a run that produced no
	// scoreable output. NOT a regression. Whether this blocks a merge is a
	// policy decision for the calling workflow, which is exactly why it gets its
	// own code instead of being folded into 1.
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
