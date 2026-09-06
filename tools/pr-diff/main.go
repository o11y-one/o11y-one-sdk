// Command pr-diff renders a GitHub-flavored-markdown PR comment from an eval
// diff document. It is the thinnest lane in the T1 SDK wave: it CONSUMES the
// machine-readable diff document lane L3 produces (scratchpad/l3-diff-schema.md,
// schema_version "o11y.eval.diff/v1") and formats it. It recomputes nothing —
// every number and verdict in the rendered comment comes straight out of the
// document. See doc.go for the field-for-field binding to L3's schema.
package main

import (
	"context"
	"encoding/json"
	"errors"
	"flag"
	"fmt"
	"io"
	"os"
)

const usage = `pr-diff — render an eval diff document as a PR comment

Usage:
  pr-diff render  [flags]   render a diff document to markdown (pure, no network)
  pr-diff comment [flags]   render and idempotently upsert it onto a GitHub PR

Both commands normally take --input, a path to an L3 diff document JSON
(schema o11y.eval.diff/v1). When the eval runner failed before it could
produce a document at all — a network/auth/RPC failure, or a bad invocation —
pass --infra-failure or --usage-error instead of --input to render that state
honestly. Those are NOT values of the document's own verdict.outcome; the
schema only describes a document the server *did* return a comparison for.

Run "pr-diff <command> -h" for flags on that command.
`

func main() {
	os.Exit(run(os.Args[1:]))
}

func run(args []string) int {
	if len(args) == 0 {
		fmt.Fprint(os.Stderr, usage)
		return 64
	}
	var err error
	switch args[0] {
	case "render":
		err = cmdRender(args[1:])
	case "comment":
		err = cmdComment(args[1:])
	case "-h", "--help", "help":
		fmt.Print(usage)
		return 0
	default:
		fmt.Fprintf(os.Stderr, "unknown command %q\n\n%s", args[0], usage)
		return 64
	}
	if err == nil {
		return 0
	}
	var withCode interface{ ExitCode() int }
	if errors.As(err, &withCode) {
		fmt.Fprintf(os.Stderr, "pr-diff: %s\n", err)
		return withCode.ExitCode()
	}
	if errors.Is(err, flag.ErrHelp) {
		return 0
	}
	fmt.Fprintf(os.Stderr, "pr-diff: %s\n", err)
	return 1
}

// usageError carries GNU/sysexits-style exit code 64, matching
// tools/ci-runner's convention for "the invocation itself was wrong."
type usageError struct{ msg string }

func (e *usageError) Error() string { return e.msg }
func (e *usageError) ExitCode() int { return 64 }

// verdictExitError lets `render --exit-with-verdict` propagate the diff
// document's own exit code as the process's exit code. The code is read
// directly off doc.Verdict.ExitCode — never re-derived from doc.Verdict.Outcome
// or any other field, per the schema doc's "do not re-map or second-guess
// verdict.outcome / verdict.exit_code."
type verdictExitError struct {
	outcome Outcome
	code    int
}

func (e *verdictExitError) Error() string {
	return fmt.Sprintf("diff document verdict is %s (exit %d)", e.outcome, e.code)
}
func (e *verdictExitError) ExitCode() int { return e.code }

// infraExitError is the analogous propagation for the --infra-failure /
// --usage-error path, where there is no document to read a code from — the
// caller states its own exit code (typically ci-runner's own process exit
// code from the failed step, e.g. 3 or 64).
type infraExitError struct {
	label string
	code  int
}

func (e *infraExitError) Error() string { return fmt.Sprintf("%s (exit %d)", e.label, e.code) }
func (e *infraExitError) ExitCode() int { return e.code }

func readInput(path string) ([]byte, error) {
	if path == "" || path == "-" {
		return io.ReadAll(os.Stdin)
	}
	return os.ReadFile(path)
}

func writeOutput(path string, data []byte) error {
	if path == "" || path == "-" {
		_, err := os.Stdout.Write(data)
		return err
	}
	return os.WriteFile(path, data, 0o644)
}

func loadDoc(path string) (DiffDocument, error) {
	raw, err := readInput(path)
	if err != nil {
		return DiffDocument{}, fmt.Errorf("reading diff document: %w", err)
	}
	var doc DiffDocument
	if err := json.Unmarshal(raw, &doc); err != nil {
		return DiffDocument{}, fmt.Errorf("parsing diff document as JSON: %w", err)
	}
	if doc.Verdict.Outcome == "" {
		return DiffDocument{}, &usageError{msg: "diff document has no \"verdict.outcome\" field"}
	}
	major, err := schemaMajor(doc.SchemaVersion)
	if err != nil {
		return DiffDocument{}, fmt.Errorf("diff document: %w", err)
	}
	if major != supportedSchemaMajor {
		return DiffDocument{}, &unsupportedSchemaError{got: doc.SchemaVersion}
	}
	return doc, nil
}

// renderFlags are the flags shared by `render` and `comment` for choosing
// between an L3 document and the infra-failure/usage-error fallback.
type renderFlags struct {
	input        *string
	infraFailure *bool
	usageErr     *bool
	reason       *string
	exitCode     *int
}

func registerRenderFlags(fs *flag.FlagSet) renderFlags {
	return renderFlags{
		input:        fs.String("input", "-", "path to the diff document JSON, or - for stdin"),
		infraFailure: fs.Bool("infra-failure", false, "render an infra-failure comment instead of reading --input (no document exists)"),
		usageErr:     fs.Bool("usage-error", false, "render a usage-error comment instead of reading --input (no document exists)"),
		reason:       fs.String("reason", "", "reason text for --infra-failure / --usage-error"),
		exitCode:     fs.Int("exit-code", 3, "process exit code to report for --infra-failure / --usage-error (default 3, ci-runner's infra-failure code)"),
	}
}

// resolve produces the markdown either from an L3 document at --input, or
// from the --infra-failure/--usage-error fallback. It returns at most one of
// (doc, ok) set, so callers can tell which path was taken (only a real doc
// carries a verdict to propagate via --exit-with-verdict).
func (rf renderFlags) resolve() (md string, doc *DiffDocument, err error) {
	if *rf.infraFailure && *rf.usageErr {
		return "", nil, &usageError{msg: "--infra-failure and --usage-error are mutually exclusive"}
	}
	if *rf.infraFailure || *rf.usageErr {
		md := RenderInfraFailure(*rf.usageErr, *rf.reason, *rf.exitCode)
		return md, nil, nil
	}
	d, err := loadDoc(*rf.input)
	if err != nil {
		return "", nil, err
	}
	m, err := Render(d)
	if err != nil {
		return "", nil, fmt.Errorf("rendering: %w", err)
	}
	return m, &d, nil
}

// --- render ------------------------------------------------------------

func cmdRender(args []string) error {
	fs := flag.NewFlagSet("render", flag.ContinueOnError)
	rf := registerRenderFlags(fs)
	output := fs.String("output", "-", "path to write the rendered markdown, or - for stdout")
	exitWithVerdict := fs.Bool("exit-with-verdict", false,
		"exit with the reported exit code (from the document's verdict.exit_code, or --exit-code for --infra-failure/--usage-error) instead of always 0 on a clean render")
	if err := fs.Parse(args); err != nil {
		return err
	}

	md, doc, err := rf.resolve()
	if err != nil {
		return err
	}
	if err := writeOutput(*output, []byte(md)); err != nil {
		return fmt.Errorf("writing output: %w", err)
	}

	if *exitWithVerdict {
		if doc != nil {
			if doc.Verdict.ExitCode != 0 {
				return &verdictExitError{outcome: doc.Verdict.Outcome, code: doc.Verdict.ExitCode}
			}
		} else if *rf.exitCode != 0 {
			label := "infra failure"
			if *rf.usageErr {
				label = "usage error"
			}
			return &infraExitError{label: label, code: *rf.exitCode}
		}
	}
	return nil
}

// --- comment -------------------------------------------------------------

func cmdComment(args []string) error {
	fs := flag.NewFlagSet("comment", flag.ContinueOnError)
	rf := registerRenderFlags(fs)
	owner := fs.String("owner", "", "GitHub repo owner (required)")
	repo := fs.String("repo", "", "GitHub repo name (required)")
	prNumber := fs.Int("pr", 0, "pull request number (required)")
	tokenEnv := fs.String("token-env", "GITHUB_TOKEN", "env var holding the GitHub token")
	baseURL := fs.String("api-base-url", "", "override the GitHub API base URL (GHES)")
	exitWithVerdict := fs.Bool("exit-with-verdict", false,
		"exit with the reported exit code after a successful comment upsert")
	if err := fs.Parse(args); err != nil {
		return err
	}
	if *owner == "" {
		return &usageError{msg: "--owner is required"}
	}
	if *repo == "" {
		return &usageError{msg: "--repo is required"}
	}
	if *prNumber <= 0 {
		return &usageError{msg: "--pr is required and must be positive"}
	}
	token := os.Getenv(*tokenEnv)
	if token == "" {
		return &usageError{msg: fmt.Sprintf("%s is not set (need a GitHub token with issues:write)", *tokenEnv)}
	}

	md, doc, err := rf.resolve()
	if err != nil {
		return err
	}

	poster := NewGitHubComments(nil, *baseURL, token)
	if err := Upsert(context.Background(), poster, *owner, *repo, *prNumber, commentMarker, md); err != nil {
		return fmt.Errorf("posting PR comment: %w", err)
	}

	if *exitWithVerdict {
		if doc != nil {
			if doc.Verdict.ExitCode != 0 {
				return &verdictExitError{outcome: doc.Verdict.Outcome, code: doc.Verdict.ExitCode}
			}
		} else if *rf.exitCode != 0 {
			label := "infra failure"
			if *rf.usageErr {
				label = "usage error"
			}
			return &infraExitError{label: label, code: *rf.exitCode}
		}
	}
	return nil
}
