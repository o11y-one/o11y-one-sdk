// Command o11y-eval is the O11y One CI runner.
//
// It is the thing a customer's pipeline invokes to launch an evaluation against
// a change, wait for it, compare the result to a baseline, and annotate the
// platform with what happened. It ships as a single static binary (CGO_ENABLED=0)
// so a pipeline can curl it and run it without a toolchain, a container, or a
// package manager.
//
// The runner DRIVES the code-first loop; it does not judge it. The verdict on a
// change comes from the decision the server adopted for the run
// (GetEvaluationRunOverview.adopted_decision); `diff` maps that decision onto
// the exit taxonomy and never recomputes it. See outcome.go for the taxonomy and
// diffdoc.go for the mapping.
package main

import (
	"context"
	"crypto/rand"
	"encoding/hex"
	"encoding/json"
	"errors"
	"flag"
	"fmt"
	"os"
	"strings"
	"time"

	"connectrpc.com/connect"
	agenticv1 "github.com/o11y-one/o11y-one-sdk/gen/go/o11y_one/agentic/v1"
	"google.golang.org/protobuf/types/known/timestamppb"
)

const usage = `o11y-eval — O11y One CI runner

Usage:
  o11y-eval <command> [flags]

Commands:
  run        launch an evaluation run against a definition or inline draft
  wait       block until a run's operation reaches a terminal state
  diff       return the server's adopted decision for a run as a verdict on one candidate
  annotate   record a platform annotation (deployment marker, event, highlight)

Exit codes (the verdict is the exit code):
  0  improvement     the server recommends the candidate under test
  1  regression      the server blocked the candidate under test
  2  indeterminate   no verdict reachable (not adopted, no clear winner, insufficient evidence,
                     or a run the preview blocked from launching)
  3  infra-failure   runner or platform failed, or a wait timed out
  64 usage-error     bad invocation

Global flags are per-command; run "o11y-eval <command> --help".
`

// commonFlags are the connection and identity flags every subcommand needs.
//
// The credential is read from the environment, never from a flag: a flag value
// lands in the process table, in CI logs that echo the command line, and in
// shell history. O11Y_API_KEY is the only supported channel.
type commonFlags struct {
	baseURL  string
	orgID    string
	tenantID string
	timeout  time.Duration
	jsonOut  bool
}

func (c *commonFlags) register(fs *flag.FlagSet) {
	fs.StringVar(&c.baseURL, "base-url", envOr("O11Y_BASE_URL", "https://grpc.o11y.one"),
		"O11y One API base URL (env: O11Y_BASE_URL)")
	fs.StringVar(&c.orgID, "org-id", os.Getenv("O11Y_ORG_ID"),
		"organization id, sent as x-o11y-org-id (env: O11Y_ORG_ID)")
	fs.StringVar(&c.tenantID, "tenant-id", os.Getenv("O11Y_TENANT_ID"),
		"tenant id, sent as x-o11y-tenant-id (env: O11Y_TENANT_ID)")
	fs.DurationVar(&c.timeout, "timeout", 30*time.Minute,
		"overall deadline for this command")
	fs.BoolVar(&c.jsonOut, "json", false,
		"emit machine-readable JSON on stdout instead of human text")
}

// credential returns the machine credential from the environment.
//
// Format is o11y_mach.<selector>.<secret>, presented in the x-o11y-key header.
// Validation here mirrors the SDKs (packages/sdk-ts/src/auth.ts,
// packages/sdk-py/src/o11y_one/sdk/auth.py) and is deliberately structural
// only — it catches an unset variable or a pasted session token before a
// network round trip, and claims nothing about whether the credential is live.
func (c *commonFlags) credential() (string, error) {
	raw := strings.TrimSpace(os.Getenv("O11Y_API_KEY"))
	if raw == "" {
		return "", errors.New("O11Y_API_KEY is not set (machine credential, o11y_mach.<selector>.<secret>)")
	}
	if len(raw) > 128 {
		return "", fmt.Errorf("O11Y_API_KEY is %d bytes, over the 128-byte server limit", len(raw))
	}
	if !strings.HasPrefix(raw, "o11y_mach.") || len(strings.Split(raw, ".")) != 3 {
		return "", errors.New(`O11Y_API_KEY is not a machine credential (expected "o11y_mach.<selector>.<secret>")`)
	}
	return raw, nil
}

func envOr(key, fallback string) string {
	if v := os.Getenv(key); v != "" {
		return v
	}
	return fallback
}

func main() {
	os.Exit(run(os.Args[1:]))
}

func run(args []string) int {
	if len(args) == 0 {
		fmt.Fprint(os.Stderr, usage)
		return OutcomeUsageError.ExitCode()
	}

	var err error
	switch args[0] {
	case "run":
		err = cmdRun(args[1:])
	case "wait":
		err = cmdWait(args[1:])
	case "diff":
		err = cmdDiff(args[1:])
	case "annotate":
		err = cmdAnnotate(args[1:])
	case "-h", "--help", "help":
		fmt.Print(usage)
		return 0
	case "version":
		fmt.Println(version)
		return 0
	default:
		fmt.Fprintf(os.Stderr, "unknown command %q\n\n%s", args[0], usage)
		return OutcomeUsageError.ExitCode()
	}

	if err == nil {
		return OutcomeImprovement.ExitCode()
	}
	return reportError(err)
}

// version is stamped at build time:
//
//	go build -ldflags "-X main.version=$(git describe --tags --always)"
var version = "dev"

// reportError prints an error and maps it onto the exit taxonomy.
//
// Anything that carries its own Outcome decides its own exit code; a bare flag
// parse error is a usage error; everything else is an infra failure, because a
// runner that does not recognise its own error has no business calling a change
// a regression.
func reportError(err error) int {
	var outcomeErr interface{ Outcome() Outcome }
	switch {
	case errors.As(err, &outcomeErr):
		o := outcomeErr.Outcome()
		fmt.Fprintf(os.Stderr, "o11y-eval: %s [%s]\n", err, o)
		return o.ExitCode()
	case errors.Is(err, flag.ErrHelp):
		return 0
	default:
		fmt.Fprintf(os.Stderr, "o11y-eval: %s [%s]\n", err, OutcomeInfraFailure)
		return OutcomeInfraFailure.ExitCode()
	}
}

// generatorStamp identifies this build inside emitted documents.
func generatorStamp() Generator { return Generator{Tool: "o11y-eval", Version: version} }

// newIdempotencyKey derives a stable-per-launch key when the caller did not
// supply one. Callers SHOULD pass a key tied to the change (a commit sha) so a
// retried pipeline dedupes; this fallback only guarantees the field is set.
func newIdempotencyKey() string {
	var b [16]byte
	if _, err := rand.Read(b[:]); err != nil {
		return fmt.Sprintf("o11y-eval-%d", nowUTC().UnixNano())
	}
	return "o11y-eval-" + hex.EncodeToString(b[:])
}

// --- run --------------------------------------------------------------------

func cmdRun(args []string) error {
	fs := flag.NewFlagSet("run", flag.ContinueOnError)
	var common commonFlags
	common.register(fs)

	definition := fs.String("definition", "", "evaluation definition id; without --preview-token the runner previews it (current revision, the definition's own mode) and launches with the preview's token, and a preview that blocks the launch exits 2 naming its blockers")
	previewToken := fs.String("preview-token", "", "preview token for an inline draft run (from PreviewEvaluationRun)")
	idempotencyKey := fs.String("idempotency-key", os.Getenv("GITHUB_SHA"), "idempotency key; a retry with the same key is deduped (env default: GITHUB_SHA)")
	waitFor := fs.Bool("wait", false, "block until the run's operation reaches a terminal state")
	budget := fs.Duration("budget", 0, "max time to spend waiting when --wait is set; 0 means bounded only by --timeout")
	poll := fs.Duration("poll-interval", 10*time.Second, "how often to poll for terminal state when --wait is set")

	if err := fs.Parse(args); err != nil {
		return err
	}
	if *definition == "" && *previewToken == "" {
		return &usageError{msg: "one of --definition or --preview-token is required"}
	}
	if *poll <= 0 {
		return &usageError{msg: "--poll-interval must be positive"}
	}
	cred, err := common.credential()
	if err != nil {
		return err
	}

	key := *idempotencyKey
	if strings.TrimSpace(key) == "" {
		key = newIdempotencyKey()
	}

	ctx, cancel := common.commandContext()
	defer cancel()

	clients := newClients(&common, cred)
	token := *previewToken
	if token == "" {
		if token, err = previewLaunch(ctx, clients, *definition); err != nil {
			return err
		}
	}
	resp, err := clients.eval.CreateEvaluationRun(ctx, connect.NewRequest(&agenticv1.CreateEvaluationRunRequest{
		DefinitionId:   *definition,
		PreviewToken:   token,
		IdempotencyKey: key,
	}))
	if err != nil {
		return fmt.Errorf("run: CreateEvaluationRun failed: %w", err)
	}
	runID := resp.Msg.GetRun().GetEvaluationRunId()
	op := resp.Msg.GetOperation()
	operationID := op.GetOperationId()

	if !*waitFor {
		return emitRun(&common, runID, operationID, resp.Msg.GetIdempotentReplay(), op)
	}

	fetch := func(fctx context.Context) (*agenticv1.EvaluationOperationV1, error) {
		r, ferr := clients.eval.GetEvaluationOperation(fctx, connect.NewRequest(&agenticv1.GetEvaluationOperationRequest{
			Selector: &agenticv1.GetEvaluationOperationRequest_OperationId{OperationId: operationID},
		}))
		if ferr != nil {
			return nil, ferr
		}
		return r.Msg.GetOperation(), nil
	}
	terminal, err := waitForOperation(ctx, "run", *poll, *budget, fetch)
	if err != nil {
		return err
	}
	if err := outcomeForOperation("run", terminal); err != nil {
		return err
	}
	return emitRun(&common, runID, operationID, resp.Msg.GetIdempotentReplay(), terminal)
}

// previewLaunch mints the token CreateEvaluationRun requires; the server has no
// definition-only launch. A preview that does not allow the launch is the
// platform answering "no run": not a regression, not an infra failure, and no
// verdict, so it is indeterminate.
//
// A retry with the same idempotency key still replays: the run records the
// digest of the definition as re-resolved at launch, which carries no nonce or
// expiry, so a fresh preview of an unchanged definition matches it.
func previewLaunch(ctx context.Context, clients *apiClients, definitionID string) (string, error) {
	resp, err := clients.eval.PreviewEvaluationRun(ctx, connect.NewRequest(&agenticv1.PreviewEvaluationRunRequest{
		DefinitionId: definitionID,
	}))
	if err != nil {
		return "", fmt.Errorf("run: PreviewEvaluationRun failed: %w", err)
	}
	if !resp.Msg.GetLaunchAllowed() {
		var blockers []string
		for _, b := range resp.Msg.GetBlockers() {
			kind := strings.TrimPrefix(b.GetKind().String(), "EVALUATION_PREVIEW_BLOCKER_KIND_V1_")
			blockers = append(blockers, kind+": "+b.GetDetail())
		}
		return "", &verdictError{outcome: OutcomeIndeterminate, decision: "preview blocked the launch: " + strings.Join(blockers, "; ")}
	}
	return resp.Msg.GetPreviewToken(), nil
}

func emitRun(common *commonFlags, runID, operationID string, replay bool, op *agenticv1.EvaluationOperationV1) error {
	state := operationStateString(op.GetState())
	if common.jsonOut {
		return emitJSON(map[string]any{
			"run_id":            runID,
			"operation_id":      operationID,
			"idempotent_replay": replay,
			"state":             state,
		})
	}
	fmt.Printf("run_id=%s operation_id=%s state=%s idempotent_replay=%t\n", runID, operationID, state, replay)
	return nil
}

// --- wait -------------------------------------------------------------------

func cmdWait(args []string) error {
	fs := flag.NewFlagSet("wait", flag.ContinueOnError)
	var common commonFlags
	common.register(fs)

	operationID := fs.String("operation-id", "", "operation id to wait on")
	idempotencyKey := fs.String("idempotency-key", "", "idempotency key of the launch to wait on (alternative to --operation-id)")
	budget := fs.Duration("budget", 0, "max time to spend waiting; 0 means bounded only by --timeout")
	poll := fs.Duration("poll-interval", 10*time.Second, "how often to poll for terminal state")

	if err := fs.Parse(args); err != nil {
		return err
	}
	if *operationID == "" && *idempotencyKey == "" {
		return &usageError{msg: "one of --operation-id or --idempotency-key is required"}
	}
	if *operationID != "" && *idempotencyKey != "" {
		return &usageError{msg: "--operation-id and --idempotency-key are mutually exclusive"}
	}
	if *poll <= 0 {
		return &usageError{msg: "--poll-interval must be positive"}
	}
	cred, err := common.credential()
	if err != nil {
		return err
	}

	ctx, cancel := common.commandContext()
	defer cancel()

	clients := newClients(&common, cred)
	reqMsg := &agenticv1.GetEvaluationOperationRequest{}
	if *operationID != "" {
		reqMsg.Selector = &agenticv1.GetEvaluationOperationRequest_OperationId{OperationId: *operationID}
	} else {
		reqMsg.Selector = &agenticv1.GetEvaluationOperationRequest_IdempotencyKey{IdempotencyKey: *idempotencyKey}
	}
	fetch := func(fctx context.Context) (*agenticv1.EvaluationOperationV1, error) {
		r, ferr := clients.eval.GetEvaluationOperation(fctx, connect.NewRequest(reqMsg))
		if ferr != nil {
			return nil, ferr
		}
		return r.Msg.GetOperation(), nil
	}
	terminal, err := waitForOperation(ctx, "wait", *poll, *budget, fetch)
	if err != nil {
		return err
	}
	if err := outcomeForOperation("wait", terminal); err != nil {
		return err
	}
	return emitRun(&common, terminal.GetEvaluationRunId(), terminal.GetOperationId(), false, terminal)
}

// --- diff -------------------------------------------------------------------

func cmdDiff(args []string) error {
	fs := flag.NewFlagSet("diff", flag.ContinueOnError)
	var common commonFlags
	common.register(fs)

	runID := fs.String("run", "", "evaluation run id whose adopted decision is the verdict; the run subcommand prints it (required)")
	candidate := fs.String("candidate", "", "candidate key under test (required)")
	out := fs.String("out", "", "also write the diff document JSON to this file")

	if err := fs.Parse(args); err != nil {
		return err
	}
	if *runID == "" {
		return &usageError{msg: "--run is required"}
	}
	if *candidate == "" {
		return &usageError{msg: "--candidate is required"}
	}
	cred, err := common.credential()
	if err != nil {
		return err
	}

	ctx, cancel := common.commandContext()
	defer cancel()

	clients := newClients(&common, cred)
	resp, err := clients.eval.GetEvaluationRunOverview(ctx, connect.NewRequest(&agenticv1.GetEvaluationRunOverviewRequest{
		EvaluationRunId: *runID,
		// INITIAL, not FULL: the adopted decision rides on both profiles and is
		// read inside the INITIAL statement, so the verdict costs no extra
		// round trip and no extra query. Nothing here reads a FULL-only section.
		Profile: agenticv1.EvaluationRunOverviewProfileV1_EVALUATION_RUN_OVERVIEW_PROFILE_V1_INITIAL,
	}))
	if err != nil {
		return fmt.Errorf("diff: GetEvaluationRunOverview failed: %w", err)
	}

	doc := buildDiffDocument(resp.Msg, *candidate, generatorStamp())

	// The document always goes to stdout (it is L4's input); the exit code
	// carries the verdict. --out additionally persists it for archival.
	payload, err := json.MarshalIndent(doc, "", "  ")
	if err != nil {
		return fmt.Errorf("diff: serializing diff document: %w", err)
	}
	fmt.Println(string(payload))
	if *out != "" {
		if werr := os.WriteFile(*out, append(payload, '\n'), 0o644); werr != nil {
			return fmt.Errorf("diff: writing --out %q: %w", *out, werr)
		}
	}

	outcome := outcomeForAdoptedDecision(resp.Msg.GetAdoptedDecision(), *candidate)
	if outcome == OutcomeImprovement {
		return nil
	}
	return &verdictError{outcome: outcome, decision: doc.Verdict.Decision}
}

// verdictError carries a non-improvement verdict out to the exit taxonomy. It is
// not a failure of the runner — the tool did its job — so its message states the
// server's decision plainly rather than sounding like a crash.
type verdictError struct {
	outcome  Outcome
	decision string
}

func (e *verdictError) Error() string {
	return fmt.Sprintf("verdict %s (server decision: %s)", e.outcome, e.decision)
}

func (e *verdictError) Outcome() Outcome { return e.outcome }

// --- annotate ---------------------------------------------------------------

func cmdAnnotate(args []string) error {
	fs := flag.NewFlagSet("annotate", flag.ContinueOnError)
	var common commonFlags
	common.register(fs)

	kind := fs.String("kind", "deployment",
		"annotation kind: deployment | event | range")
	title := fs.String("title", "", "annotation title (required)")
	body := fs.String("body", "", "annotation body, recorded as a 'body' attribute")
	at := fs.String("at", "", "RFC3339 instant; defaults to now")
	until := fs.String("until", "", "RFC3339 end instant, for --kind=range")
	idempotencyKey := fs.String("idempotency-key", "", "idempotency key; a retry with the same key is deduped")

	if err := fs.Parse(args); err != nil {
		return err
	}
	if *title == "" {
		return &usageError{msg: "--title is required"}
	}
	annKind, ok := annotationKind(*kind)
	if !ok {
		return &usageError{msg: fmt.Sprintf("unknown --kind %q (want deployment, event or range)", *kind)}
	}
	if *kind == "range" && *until == "" {
		return &usageError{msg: "--until is required with --kind=range"}
	}

	startAt := nowUTC()
	if *at != "" {
		t, perr := time.Parse(time.RFC3339, *at)
		if perr != nil {
			return &usageError{msg: fmt.Sprintf("--at is not a valid RFC3339 instant: %v", perr)}
		}
		startAt = t
	}
	var endAt *timestamppb.Timestamp
	if *until != "" {
		t, perr := time.Parse(time.RFC3339, *until)
		if perr != nil {
			return &usageError{msg: fmt.Sprintf("--until is not a valid RFC3339 instant: %v", perr)}
		}
		if t.Before(startAt) {
			return &usageError{msg: "--until must not precede --at"}
		}
		endAt = timestamppb.New(t)
	}
	cred, err := common.credential()
	if err != nil {
		return err
	}

	req := &agenticv1.RecordPlatformAnnotationRequest{
		Kind:           annKind,
		Title:          *title,
		StartAt:        timestamppb.New(startAt),
		EndAt:          endAt,
		IdempotencyKey: *idempotencyKey,
	}
	if *body != "" {
		req.Attributes = []*agenticv1.PlatformAnnotationAttributeV1{{Key: "body", Value: *body}}
	}

	ctx, cancel := common.commandContext()
	defer cancel()

	clients := newClients(&common, cred)
	resp, err := clients.eval.RecordPlatformAnnotation(ctx, connect.NewRequest(req))
	if err != nil {
		return fmt.Errorf("annotate: RecordPlatformAnnotation failed: %w", err)
	}

	ann := resp.Msg.GetAnnotation()
	if common.jsonOut {
		return emitJSON(map[string]any{
			"annotation_id":     ann.GetAnnotationId(),
			"kind":              *kind,
			"idempotent_replay": resp.Msg.GetIdempotentReplay(),
		})
	}
	fmt.Printf("annotation_id=%s kind=%s idempotent_replay=%t\n", ann.GetAnnotationId(), *kind, resp.Msg.GetIdempotentReplay())
	return nil
}

// annotationKind maps the CLI vocabulary onto the platform's annotation kinds:
// a deployment marker, a point-in-time event (MARKER), or a time-range
// highlight (HIGHLIGHT).
func annotationKind(kind string) (agenticv1.PlatformAnnotationKindV1, bool) {
	switch kind {
	case "deployment":
		return agenticv1.PlatformAnnotationKindV1_PLATFORM_ANNOTATION_KIND_V1_DEPLOYMENT, true
	case "event":
		return agenticv1.PlatformAnnotationKindV1_PLATFORM_ANNOTATION_KIND_V1_MARKER, true
	case "range":
		return agenticv1.PlatformAnnotationKindV1_PLATFORM_ANNOTATION_KIND_V1_HIGHLIGHT, true
	default:
		return agenticv1.PlatformAnnotationKindV1_PLATFORM_ANNOTATION_KIND_V1_UNSPECIFIED, false
	}
}

func emitJSON(v any) error {
	payload, err := json.MarshalIndent(v, "", "  ")
	if err != nil {
		return fmt.Errorf("serializing output: %w", err)
	}
	fmt.Println(string(payload))
	return nil
}

// usageError is a bad invocation: the caller's fault, exit 64.
type usageError struct{ msg string }

func (e *usageError) Error() string    { return e.msg }
func (e *usageError) Outcome() Outcome { return OutcomeUsageError }
