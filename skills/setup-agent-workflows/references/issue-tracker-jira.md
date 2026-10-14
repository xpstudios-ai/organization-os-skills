<!-- agent-skills:execution-admission:v1 -->

# Issue Tracker: Jira / Atlassian

Implementation issues live in Jira. Use Atlassian/Jira tools when available. If
tools are unavailable in the current runtime, draft exact Jira-ready issue
content and ask the user to publish it. PRDs/specs are governed by the selected
spec-source section.

## Conventions

- Resolve project key, issue type, component, fix version, priority, Epic
  relationship, and workflow statuses from repo or workspace instructions.
- Use Jira workflow statuses for triage state when possible. Use labels only
  when the Jira project already uses labels for triage.
- Use plain bullets for acceptance criteria, not task-list checkboxes. Workflow
  state belongs in Jira status/labels and comments.
- If Confluence pages or ADRs are linked from the Jira issue, read them before
  drafting work.
- If `.agents/skills.toml` sets `[workflow].publish_by_default = false`, draft
  Jira-ready content and wait for an explicit publish request.

## Agent-Ready Admission Mechanics

- Candidate holding: the configured `needs-triage` status or label, with
  `ready-for-agent` absent; fetch and verify the issue.
- Execution claim for boundary-bearing work: native `In Progress` is not an
  atomic lease. Unless the committed route provides a conditional
  claimant-and-token transition, declare concurrent agent execution unsupported
  and name the human or orchestrator that serializes one worker; then remove
  readiness and fetch the non-admissible state before work starts.
- Agent Brief location: Jira comment headed `Agent Brief`; read back the comment
  before publishing readiness or consuming a stop boundary.
- If the Jira route cannot guarantee these ordered transitions and read-backs,
  agent-ready publication is unsupported.

## When a skill says "publish to the issue tracker"

Create Jira issues for implementation slices using the project's convention.
Link each issue to the configured PRD/spec source. If the spec source is also
Jira, create or update the configured product/spec issue type or Epic first and
link implementation issues to it.

For a `ready-for-agent` candidate, create it first in the mapped non-admissible
holding status. Persist and read back its complete current Agent Brief, then
route the authorized transition through `triage`. If exact publication
authority or guaranteed ordering/read-back is absent, return a draft instead
of publishing the candidate.

## When a skill says "fetch the relevant issue"

Read the Jira issue, description, comments, status, issue type, priority,
labels, components, linked issues, and attachments or linked Confluence pages
when available.

## When a skill says "comment"

Add a Jira comment using the skill's template.

## When a skill says "transition state"

Before applying `ready-for-agent`, keep the issue non-admissible, persist and
read back the current or superseding Agent Brief, and verify any completed
boundary is marked consumed and only the remaining executable tranche is
current. Only then apply the agent-ready status or label. If the Jira tools
cannot guarantee that ordering and read-back, do not publish the transition.

At a stop condition, clear the current execution claim, fetch the issue, and
verify that the claimant and claim token are absent before persisting or
publishing a superseding Agent Brief.

For a terminal transition, move to the verified terminal status, remove every
core active triage label, and clear the current execution claim before or in
the same supported update. Fetch the issue and verify that no active workflow
label or active triage status remains and the claimant and claim token are
absent.

For an active transition, move the issue to the mapped Jira workflow status,
or apply the mapped label if the workspace uses labels.
