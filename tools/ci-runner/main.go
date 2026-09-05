// Command o11y-eval is the O11y One CI runner.
//
// It is the thing a customer's pipeline invokes to launch an evaluation against
// a change, wait for it, compare the result to a baseline, and annotate the
// platform with what happened. It ships as a single static binary (CGO_ENABLED=0)
// so a pipeline can curl it and run it without a toolchain, a container, or a
// package manager.
//
// STATUS: scaffold. Every subcommand parses its flags, validates them, and then
// returns an honest "not implemented" that exits 3 (infra-failure). Nothing here
// pretends to pass. See outcome.go for why not-implemented maps to
// infra-failure rather than to success or indeterminate.
//
// What each subcommand is blocked on is stated in its own not-implemented
// message, so `o11y-eval run --help` and a failing invocation both tell the
// truth about where the work actually is.
package main

import (
	"errors"
	"flag"
	"fmt"
	"os"
	"strings"
	"time"
)

const usage = `o11y-eval — O11y One CI runner

Usage:
  o11y-eval <command> [flags]

Commands:
  run        launch an evaluation run against a definition
  wait       block until a run reaches a terminal state
  diff       compare a run against a baseline and return a verdict
  annotate   record a platform annotation (deployment marker, custom event)

Exit codes (the verdict is the exit code):
  0  improvement     gate passes
  1  regression      comparison completed, result is worse than baseline
  2  indeterminate   no verdict reachable (too few cases, no baseline)
  3  infra-failure   runner or platform failed; says nothing about the change
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
	fs.StringVar(&c.baseURL, "base-url", envOr("O11Y_BASE_URL", "https://api.o11y.one"),
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

// --- run --------------------------------------------------------------------

func cmdRun(args []string) error {
	fs := flag.NewFlagSet("run", flag.ContinueOnError)
	var common commonFlags
	common.register(fs)

	definition := fs.String("definition", "", "evaluation definition id or slug (required)")
	dataset := fs.String("dataset", "", "dataset id; defaults to the definition's pinned dataset")
	label := fs.String("label", "", "human label for this run, e.g. the PR title")
	commit := fs.String("commit", os.Getenv("GITHUB_SHA"), "commit sha under test")
	waitFor := fs.Bool("wait", false, "block until the run reaches a terminal state")

	if err := fs.Parse(args); err != nil {
		return err
	}
	if *definition == "" {
		return &usageError{msg: "--definition is required"}
	}
	if _, err := common.credential(); err != nil {
		return err
	}
	_, _, _, _ = dataset, label, commit, waitFor

	return &errNotImplemented{
		subcommand: "run",
		blockedOn: "the machine-principal auth surface (lane 50A: CreateMachineCredential, " +
			"GetCallerPrincipal) and the run-launch RPC are not in the proto snapshot at PROTO_PIN",
	}
}

// --- wait -------------------------------------------------------------------

func cmdWait(args []string) error {
	fs := flag.NewFlagSet("wait", flag.ContinueOnError)
	var common commonFlags
	common.register(fs)

	runID := fs.String("run-id", "", "run id to wait on (required)")
	poll := fs.Duration("poll-interval", 10*time.Second, "how often to poll for terminal state")

	if err := fs.Parse(args); err != nil {
		return err
	}
	if *runID == "" {
		return &usageError{msg: "--run-id is required"}
	}
	if *poll <= 0 {
		return &usageError{msg: "--poll-interval must be positive"}
	}
	if _, err := common.credential(); err != nil {
		return err
	}

	return &errNotImplemented{
		subcommand: "wait",
		blockedOn:  "the run-status RPC is not in the proto snapshot at PROTO_PIN",
	}
}

// --- diff -------------------------------------------------------------------

func cmdDiff(args []string) error {
	fs := flag.NewFlagSet("diff", flag.ContinueOnError)
	var common commonFlags
	common.register(fs)

	runID := fs.String("run-id", "", "run id to evaluate (required)")
	baseline := fs.String("baseline", "", "baseline run id, or a ref like 'main' (required)")
	tolerance := fs.Float64("tolerance", 0.0,
		"score delta tolerated before a drop counts as a regression, 0..1")
	minCases := fs.Int("min-cases", 1,
		"below this many comparable cases the verdict is indeterminate, not a pass")

	if err := fs.Parse(args); err != nil {
		return err
	}
	if *runID == "" {
		return &usageError{msg: "--run-id is required"}
	}
	if *baseline == "" {
		return &usageError{msg: "--baseline is required"}
	}
	if *tolerance < 0 || *tolerance > 1 {
		return &usageError{msg: "--tolerance must be in [0, 1]"}
	}
	if *minCases < 1 {
		return &usageError{msg: "--min-cases must be at least 1"}
	}
	if _, err := common.credential(); err != nil {
		return err
	}

	// This is the subcommand that owns the verdict, and therefore the one that
	// must never guess. When it lands, "fewer than --min-cases comparable cases"
	// exits 2 (indeterminate); only a completed comparison may exit 1.
	return &errNotImplemented{
		subcommand: "diff",
		blockedOn:  "the run-comparison read RPC is not in the proto snapshot at PROTO_PIN",
	}
}

// --- annotate ---------------------------------------------------------------

func cmdAnnotate(args []string) error {
	fs := flag.NewFlagSet("annotate", flag.ContinueOnError)
	var common commonFlags
	common.register(fs)

	kind := fs.String("kind", "deployment",
		"annotation kind: deployment | event | range")
	title := fs.String("title", "", "annotation title (required)")
	body := fs.String("body", "", "annotation body")
	at := fs.String("at", "", "RFC3339 instant; defaults to now")
	until := fs.String("until", "", "RFC3339 end instant, for --kind=range")

	if err := fs.Parse(args); err != nil {
		return err
	}
	if *title == "" {
		return &usageError{msg: "--title is required"}
	}
	switch *kind {
	case "deployment", "event", "range":
	default:
		return &usageError{msg: fmt.Sprintf("unknown --kind %q (want deployment, event or range)", *kind)}
	}
	if *kind == "range" && *until == "" {
		return &usageError{msg: "--until is required with --kind=range"}
	}
	for name, value := range map[string]string{"--at": *at, "--until": *until} {
		if value == "" {
			continue
		}
		if _, err := time.Parse(time.RFC3339, value); err != nil {
			return &usageError{msg: fmt.Sprintf("%s is not a valid RFC3339 instant: %v", name, err)}
		}
	}
	if _, err := common.credential(); err != nil {
		return err
	}
	_ = body

	return &errNotImplemented{
		subcommand: "annotate",
		blockedOn: "RecordPlatformAnnotation is not in the proto snapshot at PROTO_PIN; it also " +
			"requires the platform-annotation:write scope (lane 50A discriminant 5)",
	}
}

// usageError is a bad invocation: the caller's fault, exit 64.
type usageError struct{ msg string }

func (e *usageError) Error() string    { return e.msg }
func (e *usageError) Outcome() Outcome { return OutcomeUsageError }
