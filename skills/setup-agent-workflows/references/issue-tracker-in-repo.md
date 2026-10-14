<!-- agent-skills:execution-admission:v1 -->

# Issue Tracker: In-Repo Markdown

Implementation issues for this repo live in version-controlled markdown under
`.agents/work-items/`. PRDs/specs are governed by the selected spec-source
section and may live in `PRD.md`, a work-item PRD, docs, or an external system.

## Conventions

- Active workstreams live under `.agents/work-items/active/<slug>/`.
- Closed or historical workstreams live under
  `.agents/work-items/archive/<slug>/`.
- Issue path: `.agents/work-items/active/<slug>/issues/<NNN>-<slug>.md`
- Preserved migrated context path:
  `.agents/work-items/<active-or-archive>/<slug>/history/original-plan.md`
- Issue state is stored near the top of each issue file:

```text
Status: needs-triage
Type: enhancement
```

- Comments, triage notes, and agent briefs are appended under `## Comments`.
- Acceptance criteria in issue bodies and agent briefs use plain bullets, not
  task-list checkboxes. Workflow state lives in `Status:` and comments.
- Link between issues with relative markdown links.
- Read the configured PRD/spec source first. Read issue files only when
  implementing or triaging that slice. Read `history/original-plan.md` only for
  archaeology or when the PRD says required context is missing.
- Do not search `archive/` for active work unless the user asks for
  history/archive or no active match exists.
- If `.agents/skills.toml` sets `[workflow].publish_by_default = false`, draft
  markdown content and wait for an explicit publish request before creating
  files.

## Agent-Ready Admission Mechanics

- Candidate holding: `Status: needs-triage`; reread the file and verify no
  `ready-for-agent` value remains.
- Execution claim for boundary-bearing work: `Status: in-progress` is not an
  atomic lease. Unless the committed route provides an atomic claimant and
  unique token update, declare concurrent agent execution unsupported and name
  the human or orchestrator that serializes one worker; then record the claim,
  remove readiness, and reread the file before work starts.
- Agent Brief location: the current `Agent Brief` subsection under
  `## Comments`; reread the full section before publishing readiness or
  consuming a stop boundary.
- Use one atomic file replacement per state/brief update. If the repository
  cannot guarantee atomic replacement and read-back, agent-ready publication
  is unsupported.

## When a skill says "publish to the issue tracker"

Create or update the appropriate markdown file under
`.agents/work-items/active/`, then report the path to the user. Use
`.agents/work-items/archive/` only for completed, superseded, or historical
workstreams.

For a `ready-for-agent` candidate, create the file first with the mapped
non-admissible holding status. Persist and read back its complete current Agent
Brief, then route the authorized transition through `triage`. If exact
publication authority or guaranteed ordering/read-back is absent, return a
draft instead of publishing the candidate.

## When a skill says "fetch the relevant issue"

Read the referenced markdown file. If the user gives only a slug or number,
search `.agents/work-items/active/` first. Search `.agents/work-items/archive/`
only if the user asks for archived/history context or no active match exists.

## When a skill says "comment"

Append a dated note under `## Comments` in the issue file.

## When a skill says "transition state"

Before applying `ready-for-agent`, keep the work item non-admissible, persist
and read back the current or superseding Agent Brief, and verify any completed
boundary is marked consumed and only the remaining executable tranche is
current. Only then update `Status:` to the agent-ready value. If the file
workflow cannot guarantee that ordering and read-back, do not publish the
transition.

At a stop condition, clear the current execution claim, reread the file, and
verify that the claimant and claim token are absent before persisting or
publishing a superseding Agent Brief.

On any terminal transition, replace `Status:` with the mapped terminal value,
clear the current execution claim, and do not retain a core active state
elsewhere in the file. For `wontfix`, `completed`, or `archived`, move the whole
workstream directory from `active/` to `archive/` and update links that point to
it. Reread the archived record after the move and verify that no active
workflow marker remains and the claimant and claim token are absent.

For an active transition, update the `Status:` line using
`.agents/workflows/triage-states.md`.
