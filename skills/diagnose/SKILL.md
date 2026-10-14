---
name: diagnose
description: Diagnose hard, unclear, intermittent, or performance defects with a reproduce-minimise-instrument-evidence loop.
disable-model-invocation: false
metadata:
  invocation: auto
---

# Diagnose

Find the root failure mode before changing behavior. Do not invoke this full
workflow for an ordinary, already-understood failing test.

For repository diagnosis, read the configured documentation adapter and follow
[repository context](../handoff/references/repository-context.md) and
[domain discovery](../handoff/references/domain-docs.md), including
legacy filenames. Merely reading vocabulary authorizes no glossary write.

## 1. Resolve Authorization And Signal

Choose one mode from the request:

- **Diagnosis only:** reproduce, minimise, test hypotheses, and report the
  cause. Do not make a permanent fix or add permanent tests.
- **Diagnose and fix:** after implementation authorization, add a regression
  test when practical, fix the owning invariant, and verify the original signal.

Read available repository rules, domain context, supplied logs/traces, and
`codebase-design` when module ownership or seams matter. Establish a command,
test, request, replay, telemetry query, or harness that reaches the actual
symptom. Read [feedback-loop.md](references/feedback-loop.md) for intermittent,
performance, captured-production, or human-controlled signals.

Completion criterion: mode and mutation boundary are explicit, and one
trustworthy signal captures the reported failure or baseline.

## 2. Reproduce And Minimise

Run the signal enough to establish behavior and variance. Remove inputs,
callers, configuration, data, and steps one at a time. Captured telemetry or
replay evidence may substitute when production cannot be reproduced safely.

Prove the signal detects failure with a safe deliberate mutation when practical.
Inspect the diff and restore the exact prior candidate before trusting red;
distinguish the real symptom from failure caused by the probe itself.

If there is no trustworthy signal, stop with attempts, confidence, missing
access/artifact, and the smallest next probe. Do not invent a cause.

Completion criterion: remaining elements are load-bearing, or the no-signal
boundary is documented.

## 3. Test Falsifiable Hypotheses

Rank three to five competing explanations. For each, predict an observation
that would distinguish it. Probe one variable at a time, preferring debugger or
REPL inspection and targeted seam instrumentation.

For performance, preserve workload, environment, timing distribution, and
baseline. Subjective speed is not evidence.

Completion criterion: evidence falsifies alternatives and identifies the
failed assumption, owning module or seam, and affected variants.

## 4. Redact And Clean Up

Keep raw logs, HAR files, traces, credentials, private captures, and sensitive
payloads local. Publish only minimal redacted evidence. Tag temporary
instrumentation, then remove it and any throwaway harness before handoff.

Completion criterion: no temporary diagnostic or sensitive raw artifact enters
the diff or published output.

## 5. Finish The Selected Mode

For diagnosis only, report the confirmed cause, evidence, confidence, affected
surface, containment options, and next authorized action.

For diagnose and fix, turn the minimised reproducer into the smallest useful
failing regression test when practical, watch it fail, fix the root invariant,
watch it pass, rerun the original signal, and use `repo-review` and
`repo-document` as applicable.

If no correct seam exists, record the architecture gap and smallest safe
containment; recommend `improve-codebase-architecture` separately rather than
starting a refactor.

No subagent or parallel mutable debugging is used by default.

Completion criterion: the authorized mode is complete, the original signal is
explained or green, and residual risk is explicit.

## Provenance

Adapted from Matt Pocock's debugging skills in `mattpocock/skills`, MIT
License, Copyright (c) 2026 Matt Pocock.
