---
name: to-tickets
description: Turn an approved plan or specification into independently executable tickets through the configured tracker.
disable-model-invocation: false
metadata:
  invocation: auto
---

# To Tickets

Create independently executable vertical slices without losing source intent
or publishing unsafe readiness.

## 1. Load The Source And Route

Accept an approved plan, PRD/spec, Codex plan, another approved plan artifact,
or approved conversation context. Read `AGENTS.md`, the configured tracker and
triage routes, and:

- [Issue template](assets/issue-template.md)
- [Triage state machine](../triage/references/triage-state-machine.md)
- [Agent Brief](../triage/references/agent-brief.md)
- [Execution admission](../triage/references/execution-admission.md)

Search for semantic duplicates and related open work. Update or relate the
existing owner when appropriate; do not create a parallel source of truth. If
route, mapping, readback, or publication authority is absent, prepare drafts
only.
Completion criterion: source, destination, authority, duplicate disposition,
and native state mapping are explicit.

Read [persistence](../handoff/references/persistence.md). Interactive
tickets persist intent, decisions, criteria, state and verification without
worker readiness. Agent Brief/admission steps apply only to worker/legacy routes.

## 2. Build The Dependency Graph

Slice by observable outcome, not file or technical layer. Prefer tracer bullets
that cross the useful seam. Use expand–migrate–contract when compatibility or
data movement requires ordered rollout.

For wide refactors, expand the new form, migrate callers in bounded batches,
then contract the old form. If batches cannot stay green independently, name
one integration branch and a final integrate-and-verify ticket; intermediate
batches carry explicit limited verification and are not independently releasable.

Record blockers explicitly. Only the unblocked frontier can be considered for
agent readiness; completing a blocker returns its dependants to `triage`.
Completion criterion: every slice is independently understandable and the
blocker graph has no hidden execution order.

## 3. Draft Each Issue And Agent Brief

Include source links, current tranche, scope/non-goals, plain-bullet observable
acceptance criteria, verification/testing, risks, dependencies, priority,
parent relationship, prohibited actions, and stop conditions; prepare its
complete current Agent Brief before worker publication.

The parent plan or specification is never `ready-for-agent`. Blocked issues
remain non-admissible, normally `needs-triage`. Use `ready-for-human` only when
the current next action is human-only.
Completion criterion: each issue can be executed, tested, reviewed, and closed
without another issue body or chat history.

## 4. Publish Only Through The Adapter

For interactive mode, write and read back ordinary non-admissible task records;
no duplicate brief or readiness transition is required. For worker/legacy mode:
Create records only when authorized. For an unblocked candidate, publish to the
non-admissible holding state, persist and read back the Agent Brief, then ask
`triage` to apply and verify `ready-for-agent`. Never publish directly into an
agent-admissible state.
This skill creates records only. It does not start implementation agents,
create separate tasks, or write tests.
Completion criterion: every published record is read back and verified, or
every draft states its exact blocker.
## Provenance

Adapted from Matt Pocock's issue-slicing workflows in `mattpocock/skills`, MIT
License, Copyright (c) 2026 Matt Pocock.
