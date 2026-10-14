---
name: triage
description: Classify configured work items and prepare the next safe human or agent action through the repository's state adapter.
disable-model-invocation: false
metadata:
  invocation: auto
---

# Triage

Classify the next action and prepare a durable handoff. Handle one item by
default; bulk triage requires an explicit request.

## 1. Load The Record And Route

Read `AGENTS.md`, the configured tracker and triage adapters, the full item and
comments, linked source, and:

- [Triage state machine](references/triage-state-machine.md)
- [Agent Brief](references/agent-brief.md)
- [Execution admission](references/execution-admission.md) for readiness,
  execution claims, stop conditions, or terminal moves

If a route, native mapping, authority, or readback capability is absent,
continue read-only and return a recommendation.
Completion criterion: evidence, adapter capabilities, exact mappings, and
mutation authority are known.

For explicit interactive mode, maintain the ordinary task state and next action.
Do not publish `ready-for-agent` or worker claims; readiness/brief steps below
apply only to worker/legacy routes. Missing mode grants no worker capability.

## 2. Classify The Next Action

Confirm scope, observable acceptance criteria, verification, risks,
dependencies, priority, parent/source links, and required metadata. Search for
semantic duplicates and related open work, prior rejection, and, when the
adapter supports them, linked PRs or change requests. Prefer one owning record
with explicit relationships; do not create a parallel source of truth. For
bugs, reproduce or record why reproduction is unavailable. For other requests,
verify the claimed gap against current behavior. When external PR triage is
explicitly enabled by the adapter, read the diff and verify its claim with
focused checks in an isolated checkout; do not execute untrusted PR code in a
credential-bearing workspace. Already implemented work is distinct from a
rejected request and does not enter the rejection knowledge base.

Use the adapter's category vocabulary. Choose the next action, not a later
consequential action:

- `needs-triage`
- `needs-info`
- `ready-for-agent`
- `ready-for-human`
- an adapter-defined terminal state

`ready-for-human` means the current next action is genuinely human-only.

Completion criterion: category, priority, duplicate disposition, and state are
evidence-backed; missing inputs are specific and answerable.

## 3. Prepare And Publish Readiness

Before `ready-for-agent`, persist the complete current Agent Brief in the
configured location and read back the brief, non-admissible holding state,
metadata, and source links. Only then publish and read back readiness.
Regression-test expectations belong in the brief when appropriate.

Blocked work is not agent-ready. A completed blocker causes triage to reassess
its dependants. Triage never starts a subagent, creates a separate task, or
edits code.

For `ready-for-human`, provide the decision or action the human must take.

Completion criterion: the durable handoff can be executed without chat history
and no readiness label was applied before verified persistence.

## 4. Apply An Authorized Transition

Mutate only when the user or approved source grants the exact action and the
adapter permits publication. Use only the configured adapter.
Acquire and read back an execution claim only when multiple workers can
compete; a serialized adapter may instead name its single-worker authority.
Fetch after every write.

Before a terminal transition, clear all active and readiness labels plus the
current execution claim, then read back the terminal state and absence of
`ready-for-agent`, `ready-for-human`, the claimant, and the claim token.

Completion criterion: the fetched record matches one authorized state with no
conflicting workflow marker, or the exact unapplied mutation is reported.

## Output

Report evidence, category, priority, recommended state, Agent Brief or
tracker-ready content, actual mutations, readback, and the next blocker/action.

## Provenance

Adapted from Matt Pocock's `triage` skill in `mattpocock/skills`, MIT License,
Copyright (c) 2026 Matt Pocock.
