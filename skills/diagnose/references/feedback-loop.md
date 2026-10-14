# Diagnostic Feedback Loops

Read this reference when the failure lacks a fast deterministic reproducer, is
intermittent, is performance-sensitive, or requires a human-controlled step.

## Loop Shapes

Try these in roughly this order:

1. failing unit, integration, or end-to-end test at the seam that reaches the
   bug;
2. HTTP or CLI invocation with asserted output;
3. headless browser assertion over DOM, console, or network behavior;
4. replay of a captured trace, request, payload, event, or job input;
5. minimal harness around the relevant runtime slice;
6. property or fuzz loop for intermittent wrong output;
7. bisection across commits, datasets, dependencies, or configuration;
8. differential loop across versions or configurations; or
9. a human-in-the-loop harness when an unavoidable manual action remains.

For the human-in-the-loop case, adapt the platform-matched template so the
manual action, ready signal, observation, and cleanup are explicit:

- [Bash template](../scripts/hitl-loop.template.sh)
- [PowerShell template](../scripts/hitl-loop.template.ps1)

Treat the loop as a product: make it faster, more deterministic, sharper, and
runnable without hidden steps. For intermittent failures, raise reproduction
frequency with repetition, controlled concurrency, stress, or timing probes
until hypotheses can be distinguished.

## Performance Regressions

Measure before changing behavior. Use a timing harness, profiler, query plan,
browser performance trace, or service telemetry, then test one variable at a
time. Preserve the baseline, workload, environment, and variance needed to tell
an improvement from noise.

## When No Loop Is Possible

Stop and report what was tried, which missing access or artifact prevents a
red-capable signal, and the smallest captured input, temporary instrumentation,
or human step needed next. Do not proceed to untestable hypotheses.

## Evidence Privacy

Keep raw logs, HAR files, traces, credentials, tokens, private captures, and
sensitive payloads local. Persist or publish only the smallest redacted excerpt
needed to support the diagnosis. Remove temporary captures and instrumentation
unless the user explicitly names a safe retained destination.
