package main

import (
	"fmt"
	"slices"
	"strconv"
	"strings"
)

// commentMarker is the stable anchor embedded (as an HTML comment, invisible
// in the rendered PR comment) in every render. The GitHub-side upsert code in
// comment.go greps for this marker to find and edit a prior comment instead of
// stacking a new one on every re-run. It is versioned so a future breaking
// change to the comment's own shape can still find old comments deliberately,
// rather than silently failing to match them.
const commentMarker = "<!-- o11y-one:pr-diff:v1 -->"

// Render is the pure render core for a real diff document: DiffDocument in,
// GitHub-flavored markdown out. No I/O, no network, no clock reads
// (GeneratedAt/generator come from the document, not from calling time.Now()
// here) — this is what render_test.go exercises directly over fixtures, and
// what makes the GitHub-posting path in comment.go testable without a server.
//
// Every value printed here is read directly off doc; nothing is recomputed,
// thresholded, or second-guessed, per the L3 contract's "What L4 must NOT
// do."
func Render(doc DiffDocument) (string, error) {
	var b strings.Builder

	b.WriteString(commentMarker)
	b.WriteString("\n")

	writeHeadline(&b, doc.Verdict)
	writeVerdictCallout(&b, doc.Verdict)

	writeNotes(&b, doc.Notes, doc.Verdict.DecisionChanged)
	writeFailureReasons(&b, doc.FailureReasons)

	writeIdentity(&b, doc.Identity, !absent(doc, "identity.sample_count"))

	if len(doc.Metrics) > 0 {
		b.WriteString("\n")
		writeMetricsTable(&b, doc.Metrics)
	}

	writeAbsencesFootnote(&b, doc.Absences)
	writeFooter(&b, doc.SchemaVersion, doc.Generator, doc.GeneratedAt)

	return b.String(), nil
}

// RenderInfraFailure renders the headline for the case a diff document could
// never be produced at all — the runner failed before reaching the server
// comparison (network, auth, an unimplemented RPC; see
// tools/ci-runner.OutcomeInfraFailure) or the invocation itself was wrong
// (tools/ci-runner.OutcomeUsageError). Neither state exists as a value of
// `verdict.outcome` in L3's schema, because the schema only describes a
// document the server *did* produce a comparison for. This is deliberately a
// separate function, not a fake DiffDocument with invented fields, so the two
// code paths — "here is what the server said" vs. "the server was never
// reached" — stay visibly distinct in the source, not blurred through a
// shared struct.
func RenderInfraFailure(usageError bool, reason string, exitCode int) string {
	var b strings.Builder
	b.WriteString(commentMarker)
	b.WriteString("\n")

	label, calloutTitle, calloutBody := "Infra failure", "Infra failure — the runner or platform failed.",
		"This says nothing about the change under test."
	if usageError {
		label, calloutTitle, calloutBody = "Usage error", "Usage error — the invocation was wrong.", ""
	}

	fmt.Fprintf(&b, "## \U0001F6A7 %s — eval diff (exit %d)\n\n", label, exitCode)
	fmt.Fprintf(&b, "> **%s** %s", calloutTitle, calloutBody)
	if reason != "" {
		fmt.Fprintf(&b, " %s", reason)
	} else {
		b.WriteString(" No reason was given.")
	}
	b.WriteString("\n")
	return b.String()
}

func verdictDisplay(o Outcome) (emoji, label string) {
	switch o {
	case OutcomeImprovement:
		return "✅", "Improvement"
	case OutcomeRegression:
		return "\U0001F534", "Regression"
	case OutcomeIndeterminate:
		return "⚠️", "Indeterminate"
	default:
		// Schema says L4 must tolerate unknown enum members rather than
		// erroring. An outcome this build has never seen is rendered
		// honestly as unknown, not silently folded into one of the three
		// known states.
		return "❓", fmt.Sprintf("Unknown outcome (%q)", string(o))
	}
}

func writeHeadline(b *strings.Builder, v Verdict) {
	emoji, label := verdictDisplay(v.Outcome)
	fmt.Fprintf(b, "## %s %s — eval diff (exit %d)\n", emoji, label, v.ExitCode)
	fmt.Fprintf(b, "\nserver decision: `%s`", orDash(v.Decision))
	if v.DecisionSource != "" {
		fmt.Fprintf(b, " (via `%s`)", v.DecisionSource)
	}
	b.WriteString("\n")
}

// writeVerdictCallout renders the non-improvement states as their own
// clearly-marked callouts. Indeterminate in particular must never read as a
// softened pass: verdict.coercible is always false in v1 and this text says
// so.
func writeVerdictCallout(b *strings.Builder, v Verdict) {
	switch v.Outcome {
	case OutcomeIndeterminate:
		b.WriteString("\n> **Indeterminate — no verdict reachable.** This is not a pass; ")
		b.WriteString("the comparison is not coercible into a pass or fail. ")
		fmt.Fprintf(b, "Server decision: `%s`.\n", orDash(v.Decision))
	case OutcomeRegression:
		b.WriteString("\n> **Regression — the server blocked this candidate.**\n")
	}
}

func severityIcon(sev string) string {
	switch sev {
	case "warn":
		return "⚠️"
	default:
		// Unknown/empty severities default to info, per the schema doc.
		return "ℹ️"
	}
}

func writeNotes(b *strings.Builder, notes []Note, decisionChanged bool) {
	var lines []string
	if decisionChanged {
		// Kept for documents that still carry the flag. The current runner
		// declares verdict.decision_changed absent (one run's adopted decision
		// has nothing to have changed against), and there is no release gate
		// behind it any more, so the text names the field, not a gate.
		lines = append(lines, "⚠️ the server's decision changed between the two evaluations.")
	}
	for _, n := range notes {
		msg := n.Message
		if msg == "" {
			msg = n.Code
		}
		lines = append(lines, fmt.Sprintf("%s %s", severityIcon(n.Severity), msg))
	}
	if len(lines) == 0 {
		return
	}
	b.WriteString("\n")
	for _, l := range lines {
		fmt.Fprintf(b, "- %s\n", l)
	}
}

func writeFailureReasons(b *strings.Builder, fr FailureReasons) {
	if len(fr.Added) == 0 && len(fr.Removed) == 0 {
		return
	}
	b.WriteString("\n")
	if len(fr.Added) > 0 {
		fmt.Fprintf(b, "**New failure reasons:** %s\n", strings.Join(backtick(fr.Added), ", "))
	}
	if len(fr.Removed) > 0 {
		fmt.Fprintf(b, "**Resolved failure reasons:** %s\n", strings.Join(backtick(fr.Removed), ", "))
	}
}

func backtick(ss []string) []string {
	out := make([]string, len(ss))
	for i, s := range ss {
		out[i] = "`" + s + "`"
	}
	return out
}

// absent reports whether the document explicitly declares `field` unreported.
// The answer is read off absences[] — the document's own statement — and never
// inferred from a zero value, which is the one rule the schema doc insists on.
func absent(doc DiffDocument, field string) bool {
	return slices.ContainsFunc(doc.Absences, func(a Absence) bool { return a.Field == field })
}

func writeIdentity(b *strings.Builder, id Identity, showSamples bool) {
	var lines []string
	if id.GateID != "" {
		lines = append(lines, fmt.Sprintf("gate `%s`", id.GateID))
	}
	if id.MetricName != "" {
		lines = append(lines, fmt.Sprintf("metric `%s`", id.MetricName))
	}
	if len(lines) > 0 {
		b.WriteString("\n")
		b.WriteString(strings.Join(lines, " · "))
		b.WriteString("\n")
	}

	writeEvalSide(b, "Baseline", id.Baseline, showSamples)
	writeEvalSide(b, "Candidate", id.Candidate, showSamples)
}

func writeEvalSide(b *strings.Builder, label string, s EvalSide, showSamples bool) {
	if s.EvaluationID == "" && s.DeploymentID == "" {
		return
	}
	var parts []string
	if s.EvaluationID != "" {
		parts = append(parts, fmt.Sprintf("eval `%s`", s.EvaluationID))
	}
	if s.DeploymentID != "" {
		parts = append(parts, fmt.Sprintf("deployment `%s`", s.DeploymentID))
	}
	if showSamples {
		parts = append(parts, fmt.Sprintf("%d samples", s.SampleCount))
	}
	if s.BaselineSource != "" {
		parts = append(parts, fmt.Sprintf("source `%s`", s.BaselineSource))
	}
	if s.UsedFallbackBaseline {
		parts = append(parts, "used fallback baseline")
	}
	if s.Simulated {
		parts = append(parts, "simulated")
	}
	fmt.Fprintf(b, "- **%s:** %s\n", label, strings.Join(parts, ", "))
}

func writeMetricsTable(b *strings.Builder, rows []MetricRow) {
	b.WriteString("| Metric | Baseline | Candidate | Delta |\n")
	b.WriteString("|---|---|---|---|\n")
	for _, r := range rows {
		name := r.Label
		if name == "" {
			name = r.Key
		}
		fmt.Fprintf(b, "| %s | %s | %s | %s |\n",
			name,
			renderOptional(r.Baseline, r.Unit),
			renderOptional(r.Candidate, r.Unit),
			renderDelta(r),
		)
	}
}

// renderOptional renders a single OptionalNumber cell. Absence is NEVER
// rendered as "0" or as a blank cell a reader could mistake for zero — per
// the schema doc, `{"present": false}` renders as "not available", never 0.
// This is the one piece of behavior render_test.go checks most aggressively.
func renderOptional(v OptionalNumber, unit string) string {
	if !v.Present {
		return "_not available_"
	}
	return formatFloat(v.Value) + unitSuffix(unit)
}

func renderDelta(r MetricRow) string {
	if !r.Delta.Present {
		return "_not available_"
	}
	arrow := ""
	switch {
	case r.Delta.Value > 0:
		if r.HigherIsBetter {
			arrow = " ⬆️"
		} else {
			arrow = " ⬆️⚠️"
		}
	case r.Delta.Value < 0:
		if r.HigherIsBetter {
			arrow = " ⬇️⚠️"
		} else {
			arrow = " ⬇️"
		}
	}
	sign := ""
	if r.Delta.Value > 0 {
		sign = "+"
	}
	return fmt.Sprintf("%s%s%s%s", sign, formatFloat(r.Delta.Value), unitSuffix(r.Unit), arrow)
}

// writeAbsencesFootnote renders `absences[]` as a single "N fields
// unavailable" footnote per-field, exactly as the schema doc suggests ("lets
// L4 show a single 'N fields unavailable' footnote without walking the
// tree") — it does not try to path-match an absence back to a specific table
// cell.
func writeAbsencesFootnote(b *strings.Builder, absences []Absence) {
	if len(absences) == 0 {
		return
	}
	items := make([]string, len(absences))
	for i, a := range absences {
		items[i] = fmt.Sprintf("`%s` (%s)", a.Field, orDash(a.Reason))
	}
	fmt.Fprintf(b, "\n<sub>%d field(s) not reported by the server: %s</sub>\n", len(absences), strings.Join(items, ", "))
}

func writeFooter(b *strings.Builder, schemaVersion string, gen Generator, generatedAt string) {
	var parts []string
	if schemaVersion != "" {
		parts = append(parts, "schema "+schemaVersion)
	}
	if gen.Tool != "" || gen.Version != "" {
		parts = append(parts, strings.TrimSpace(gen.Tool+" "+gen.Version))
	}
	if generatedAt != "" {
		parts = append(parts, generatedAt)
	}
	if len(parts) == 0 {
		return
	}
	fmt.Fprintf(b, "\n<sub>%s</sub>\n", strings.Join(parts, " · "))
}

func orDash(s string) string {
	if s == "" {
		return "-"
	}
	return s
}

func unitSuffix(unit string) string {
	switch unit {
	case "":
		return ""
	case "%":
		return "%"
	case "usd":
		return " USD"
	default:
		return " " + unit
	}
}

func formatFloat(f float64) string {
	return strconv.FormatFloat(f, 'f', -1, 64)
}
