# Triage States

Generic skills speak in canonical triage states. This repo maps those states to
Linear status plus the `Agent Workflow` issue-label group so triage state stays
filterable even when delivery statuses are broad.

## Core Active States

| Canonical state   | Meaning                                | Tracker value                                     |
| ----------------- | -------------------------------------- | ------------------------------------------------- |
| `needs-triage`    | Maintainer needs to evaluate           | Linear status `Backlog` plus label `needs-triage` |
| `needs-info`      | Waiting on reporter                    | Linear status `Backlog` plus label `needs-info`   |
| `ready-for-agent` | Fully specified and AFK-ready through completion or, when applicable, a named stop condition | Linear status `Todo` plus label `ready-for-agent` |
| `ready-for-human` | No safe agent-executable work remains before the next human-only action | Linear status `Todo` plus label `ready-for-human` |

## Optional Terminal/Archive States

Use Linear's native terminal statuses unless the repo explicitly maps extra
labels.

| Canonical state | Meaning                                  | Tracker value                              |
| --------------- | ---------------------------------------- | ------------------------------------------ |
| `wontfix`       | Will not be actioned                     | Linear status `Canceled`                   |
| `completed`     | Work has shipped or the record is closed | Linear status `Done`                       |
| `archived`      | Historical record retained for reference | Linear status `Canceled` plus archive note |

## Agent-Ready Admission Protocol

- Candidate holding state: Linear status `Backlog` plus label `needs-triage`.
- Execution claim: a conditional claimant-and-token transition, or an explicit
  single-worker serialization authority when concurrency is unsupported.
  Linear status `In Progress` alone is not a lease; remove every readiness
  label and fetch the issue before boundary-bearing work starts.
- Agent Brief persistence: a top-level issue comment headed `Agent Brief`.
  Read it back through the issue-comment route before publishing readiness.
- Supported ordering: holding state, holding read-back, Agent Brief write,
  Agent Brief read-back, readiness transition, readiness read-back. If the
  configured Linear tools cannot perform that sequence, agent-ready
  publication is unsupported.
- Stop cleanup: clear and read back the current execution claim before a
  superseding Agent Brief can become ready.
- Terminal cleanup: set the native terminal status, remove every
  `Agent Workflow` label, and clear the current execution claim in the same
  update when supported, then fetch the issue and verify no active workflow
  label, claimant, or claim token remains.

## Rules

- Keep exactly one `Agent Workflow` label on active triaged issues.
- Claimed/in-progress and terminal issues have no `Agent Workflow` readiness
  label; terminal issues also have no claimant or claim token. Verify absence
  after the transition.
- Use Linear statuses for broad delivery flow: backlog, todo, in progress,
  review, done, canceled, duplicate.
- Use `Duplicate` only for true duplicate issues; otherwise rejected work maps
  to `Canceled` with no active workflow label.
- Classify the next required action, not a later consequential action. Keep
  fully specified preparation `ready-for-agent` and name any later stop
  condition and prohibited actions in the Agent Brief.
- Use `ready-for-human` only when no safe agent-executable work remains.
- A readiness state does not authorize execution; repository routes and current
  user authority still govern mutations. Re-triage at every stop condition.
- Do not use task-list checkboxes as workflow state or completion tracking.
- Preserve the existing category/type system for bugs vs enhancements.
- If two states conflict, stop and ask before changing the issue.
