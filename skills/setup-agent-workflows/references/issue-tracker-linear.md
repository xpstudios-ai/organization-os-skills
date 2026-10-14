<!-- agent-skills:execution-admission:v1 -->

# Issue Tracker: Linear

Implementation issues for this repo live in Linear. Use the Linear app/MCP
tools when available. If tools are unavailable, draft the exact issue content
and ask the user to publish it. PRDs/specs are governed by the selected
spec-source section.

## Conventions

- Resolve team, project, cycle, milestone, priority, labels, and other required
  fields from repo-local config such as `.agents/projects.json` and
  `.agents/workflows/*`.
- Use Linear status for broad delivery flow and an `Agent Workflow` issue-label
  group for canonical triage state unless the team has distinct statuses for
  every canonical state.
- Do not use task-list checkboxes for acceptance criteria in Linear descriptions
  or comments. Acceptance criteria are the done contract; completion belongs in
  Linear status/labels and closing comments.
- If `.agents/skills.toml` sets `[workflow].publish_by_default = false`, draft
  Linear-ready content and wait for an explicit publish request.

## Agent-Ready Admission Mechanics

- Candidate holding: status `Backlog` plus `needs-triage`; fetch the issue and
  verify `ready-for-agent` is absent.
- Execution claim for boundary-bearing work: a generic `In Progress` status is
  not an atomic lease. Unless the committed route provides a conditional
  claimant-and-token field transition, declare concurrent agent execution
  unsupported and name the human or orchestrator that serializes one worker;
  then remove every readiness label and fetch before work starts.
- Agent Brief location: top-level issue comment headed `Agent Brief`; read back
  the comment before publishing readiness or consuming a stop boundary.
- If the available Linear route cannot replace the full workflow-label set and
  read back issues and comments in this order, agent-ready publication and
  boundary-bearing execution are unsupported.

## When a skill says "publish to the issue tracker"

Create Linear issues for implementation slices using the repo conventions. Link
each issue to the configured PRD/spec source. If the spec source is also Linear,
create or update the parent/spec issue first and link implementation issues to
it where the workspace supports that relationship.

For a `ready-for-agent` candidate, create it first in the mapped non-admissible
holding state. Persist and read back its complete current Agent Brief, then
route the authorized transition through `triage`. If exact publication
authority or guaranteed ordering/read-back is absent, return a draft instead
of publishing the candidate.

When repo-local config requires priority, assign it at creation from the
PRD/spec, roadmap lane, dependency role, customer/user impact, severity, and
workspace priority taxonomy. Do not publish unprioritized active issues unless
the tracker has no priority field or the maintainer explicitly asks for a
draft/unprioritized holding record.

## When a skill says "fetch the relevant issue"

Fetch the full Linear issue, including description, comments, labels, project,
status, priority, assignee, and linked issues.

## When a skill says "comment"

Post a Linear comment, following the skill's template and the repo's verbosity
rules.

## When a skill says "transition state"

Before applying `ready-for-agent`, keep the issue non-admissible, persist and
read back the current or superseding Agent Brief, and verify any completed
boundary is marked consumed and only the remaining executable tranche is
current. Only then apply the agent-ready label/status. If Linear tools cannot
guarantee that ordering and read-back, do not publish the transition.

At a stop condition, clear the current execution claim, fetch the issue, and
verify that the claimant and claim token are absent before persisting or
publishing a superseding Agent Brief.

For a terminal transition such as `completed`, `archived`, or `wontfix`, remove
every core active `Agent Workflow` label and clear the current execution claim
before or in the same full-label-set update as the terminal status. Fetch the
issue afterward and verify that no active workflow label remains and the
claimant and claim token are absent.

For an active transition, move the Linear issue to the mapped status and apply
exactly one mapped `Agent Workflow` label from
`.agents/workflows/triage-states.md`, removing conflicting workflow labels by
full-label-set replacement.
