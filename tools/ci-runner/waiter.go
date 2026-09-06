package main

import (
	"context"
	"fmt"
	"time"

	agenticv1 "github.com/o11y-one/o11y-one-sdk/gen/go/o11y_one/agentic/v1"
)

// errTimeout is what a bounded wait returns when the budget or the command
// deadline elapses before the run reaches a terminal state. It is an
// infra-failure, emphatically NOT indeterminate and NOT a regression: a wait
// that ran out of time has learned nothing about the change, only about the
// clock. Mapping it to anything in the verdict range would let a slow platform
// masquerade as a bad change.
type errTimeout struct {
	subcommand string
	waited     time.Duration
	lastState  string
}

func (e *errTimeout) Error() string {
	return fmt.Sprintf(
		"%s: timed out after %s waiting for a terminal state (last state: %s)",
		e.subcommand, e.waited.Round(time.Millisecond), e.lastState,
	)
}

func (e *errTimeout) Outcome() Outcome { return OutcomeInfraFailure }

// errRunFailed is a run that reached a terminal FAILED/CANCELLED state. The
// machinery finished but did not produce a scoreable result, so — like a
// timeout — it says nothing about the change and maps to infra-failure.
type errRunFailed struct {
	subcommand string
	state      string
	detail     string
}

func (e *errRunFailed) Error() string {
	if e.detail == "" {
		return fmt.Sprintf("%s: run reached terminal state %s", e.subcommand, e.state)
	}
	return fmt.Sprintf("%s: run reached terminal state %s: %s", e.subcommand, e.state, e.detail)
}

func (e *errRunFailed) Outcome() Outcome { return OutcomeInfraFailure }

// operationTerminal reports whether the operation state is one the runner should
// stop polling on.
func operationTerminal(s agenticv1.EvaluationOperationStateV1) bool {
	switch s {
	case agenticv1.EvaluationOperationStateV1_EVALUATION_OPERATION_STATE_V1_SUCCEEDED,
		agenticv1.EvaluationOperationStateV1_EVALUATION_OPERATION_STATE_V1_FAILED,
		agenticv1.EvaluationOperationStateV1_EVALUATION_OPERATION_STATE_V1_CANCELLED:
		return true
	default:
		return false
	}
}

func operationStateString(s agenticv1.EvaluationOperationStateV1) string {
	switch s {
	case agenticv1.EvaluationOperationStateV1_EVALUATION_OPERATION_STATE_V1_PENDING:
		return "PENDING"
	case agenticv1.EvaluationOperationStateV1_EVALUATION_OPERATION_STATE_V1_RUNNING:
		return "RUNNING"
	case agenticv1.EvaluationOperationStateV1_EVALUATION_OPERATION_STATE_V1_SUCCEEDED:
		return "SUCCEEDED"
	case agenticv1.EvaluationOperationStateV1_EVALUATION_OPERATION_STATE_V1_FAILED:
		return "FAILED"
	case agenticv1.EvaluationOperationStateV1_EVALUATION_OPERATION_STATE_V1_CANCELLED:
		return "CANCELLED"
	default:
		return "UNSPECIFIED"
	}
}

// fetchOperation is the injectable poll step. Real callers close over a connect
// client; tests close over a canned sequence.
type fetchOperation func(ctx context.Context) (*agenticv1.EvaluationOperationV1, error)

// waitForOperation polls until the operation is terminal or the wait is bounded
// out. The bound is the smaller of the command deadline on ctx and the explicit
// budget; whichever fires first yields a typed errTimeout. A transport error
// from a poll is returned as-is (it is already an infra failure by default).
func waitForOperation(ctx context.Context, subcommand string, poll, budget time.Duration, fetch fetchOperation) (*agenticv1.EvaluationOperationV1, error) {
	start := nowUTC()

	wctx := ctx
	var cancel context.CancelFunc
	if budget > 0 {
		wctx, cancel = context.WithTimeout(ctx, budget)
		defer cancel()
	}

	lastState := "UNSPECIFIED"
	for {
		op, err := fetch(wctx)
		if err != nil {
			// A poll that failed because the wait ran out of time is a timeout,
			// not an opaque transport error — report it as such.
			if wctx.Err() != nil {
				return nil, &errTimeout{subcommand: subcommand, waited: nowUTC().Sub(start), lastState: lastState}
			}
			return nil, err
		}
		if op != nil {
			lastState = operationStateString(op.GetState())
			if operationTerminal(op.GetState()) {
				return op, nil
			}
		}

		select {
		case <-wctx.Done():
			return nil, &errTimeout{subcommand: subcommand, waited: nowUTC().Sub(start), lastState: lastState}
		case <-time.After(poll):
		}
	}
}

// outcomeForOperation maps a terminal operation onto success or infra-failure.
// A run completing is not a verdict on the change — only `diff` renders a
// verdict — so the best a completed run yields is a clean exit 0.
func outcomeForOperation(subcommand string, op *agenticv1.EvaluationOperationV1) error {
	if op == nil {
		return &errRunFailed{subcommand: subcommand, state: "UNSPECIFIED", detail: "no operation returned"}
	}
	switch op.GetState() {
	case agenticv1.EvaluationOperationStateV1_EVALUATION_OPERATION_STATE_V1_SUCCEEDED:
		return nil
	case agenticv1.EvaluationOperationStateV1_EVALUATION_OPERATION_STATE_V1_FAILED,
		agenticv1.EvaluationOperationStateV1_EVALUATION_OPERATION_STATE_V1_CANCELLED:
		return &errRunFailed{
			subcommand: subcommand,
			state:      operationStateString(op.GetState()),
			detail:     failureDetail(op.GetFailure()),
		}
	default:
		// Non-terminal reaching this path means the caller stopped polling
		// early; treat it as an infra problem rather than a silent pass.
		return &errRunFailed{subcommand: subcommand, state: operationStateString(op.GetState()), detail: "operation not terminal"}
	}
}

func failureDetail(f *agenticv1.EvaluationFailureV1) string {
	if f == nil {
		return ""
	}
	if msg := f.GetSanitizedMessage(); msg != "" {
		if code := f.GetCode(); code != "" {
			return fmt.Sprintf("%s (%s)", msg, code)
		}
		return msg
	}
	return f.GetCode()
}
