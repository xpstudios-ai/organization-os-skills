# Triage States

Generic skills speak in canonical triage states. This repo maps those states to
the issue tracker's native representation.

## Core Active States

| Canonical state   | Meaning                                | Tracker value     |
| ----------------- | -------------------------------------- | ----------------- |
| `needs-triage`    | Maintainer needs to evaluate           | `needs-triage`    |
| `needs-info`      | Waiting on reporter                    | `needs-info`      |
| `ready-for-agent` | Fully specified and AFK-ready through completion or, when applicable, a named stop condition | `ready-for-agent` |
| `ready-for-human` | No safe agent-executable work remains before the next human-only action | `ready-for-human` |

## Optional Terminal/Archive States

Use these only when the repo's tracker maps them directly. In-repo markdown
trackers commonly use them to move workstreams from `active/` to `archive/`.

| Canonical state | Meaning                                  | Tracker value |
| --------------- | ---------------------------------------- | ------------- |
| `wontfix`       | Will not be actioned                     | `wontfix`     |
| `completed`     | Work has shipped or the record is closed | `completed`   |
| `archived`      | Historical record retained for reference | `archived`    |

## Agent-Ready Admission Protocol

- Candidate holding state: canonical `needs-triage`; tracker value
  `needs-triage`. A new candidate stays here until its complete Agent Brief is
  persisted and read back.
- Execution claim: claimant identity plus a unique token acquired
  conditionally, or an explicit single-worker serialization authority when
  concurrency is unsupported. A generic `in-progress` value alone is not a
  lease; readiness must also be removed and verified before work starts.
- Agent Brief persistence and read-back: resolve the concrete record location
  and fetch method in `.agents/workflows/issue-tracker.md`.
- Unsupported route: if the tracker cannot guarantee holding, claim,
  persistence, and read-back ordering, agent-ready publication is unsupported.
- Stop cleanup: clear and read back the current execution claim before a
  superseding Agent Brief can become ready.
- Terminal cleanup: a terminal item retains no core active workflow state,
  claimant, or claim token.

## Rules

- Use tracker-native values: markdown `Status:`, GitHub labels, Linear
  statuses/labels, or Jira workflow statuses.
- Every active triaged issue should have exactly one core active state.
- Use optional terminal/archive states only when the repo's tracker explicitly
  maps them.
- Clear every core active workflow label, readiness marker, claimant, and claim
  token before or atomically with a terminal transition, then read back their
  absence.
- Classify the next required action, not a later consequential action. Keep
  fully specified preparation `ready-for-agent` and name any later stop
  condition and prohibited actions in the Agent Brief.
- Use `ready-for-human` only when no safe agent-executable work remains.
- A readiness state does not authorize execution; repository routes and current
  user authority still govern mutations. Re-triage at every stop condition.
- Do not use task-list checkboxes as workflow state or completion tracking.
- Preserve the existing category/type system for bugs vs enhancements.
- If two states conflict, stop and ask before changing the issue.
