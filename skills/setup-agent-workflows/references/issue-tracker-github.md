<!-- agent-skills:execution-admission:v1 -->

# Issue Tracker: GitHub Issues

Implementation issues for this repo live as GitHub issues. Use the native
GitHub connector/app tools or GitHub API for issue operations. PRDs/specs are
governed by the selected spec-source section.

In cloud runtimes, do not assume shell `gh` authentication is available. If
the GitHub connector is unavailable, ask the user for the repo/issue details or
draft exact GitHub-ready content for them to apply.

## Conventions

- **Create an issue**: use the GitHub connector create-issue tool with title,
  body, labels, assignees, and milestone as supported.
- **Read an issue**: use the GitHub connector fetch-issue tool, then fetch
  comments if comments are needed.
- **List issues**: use the GitHub connector issue search/list tool with repo,
  state, labels, and sort filters.
- **Comment on an issue**: use the GitHub connector add-comment tool.
- **Apply / remove labels**: use the GitHub connector label mutation tools.
- **Close**: use the GitHub connector update-issue tool with `state = closed`,
  adding a comment first when the close needs an explanation.
- Use plain bullets for acceptance criteria, not task-list checkboxes. Workflow
  state belongs in labels/status and comments.
- If `.agents/skills.toml` sets `[workflow].publish_by_default = false`, draft
  GitHub-ready content and wait for an explicit publish request.

Infer the repo from `GITHUB_REPOSITORY`, `git remote -v`, `AGENTS.md`, or the
user prompt. Do not require shell GitHub authentication just to identify the
repo.

## Agent-Ready Admission Mechanics

- Candidate holding: open issue with `needs-triage` and without
  `ready-for-agent`; fetch and verify the label set.
- Execution claim for boundary-bearing work: a generic `in-progress` label is
  not an atomic lease. Unless the committed route provides a conditional
  claimant-and-token transition, declare concurrent agent execution unsupported
  and name the human or orchestrator that serializes one worker; then replace
  readiness and fetch the non-admissible state before work starts.
- Agent Brief location: top-level issue comment headed `Agent Brief`; read back
  the comment before publishing readiness or consuming a stop boundary.
- The connector must support deterministic label replacement plus issue and
  comment read-back. Otherwise agent-ready publication is unsupported.

## When a skill says "publish to the issue tracker"

Create GitHub issues for implementation slices. Link each issue to the
configured PRD/spec source. If the spec source is also GitHub Issues, create or
update the parent/spec issue first and link implementation issues to it.

For a `ready-for-agent` candidate, create it first with the mapped
non-admissible holding label or status. Persist and read back its complete
current Agent Brief, then route the authorized transition through `triage`. If
exact publication authority or guaranteed ordering/read-back is absent, return
a draft instead of publishing the candidate.

## When a skill says "fetch the relevant issue"

Use the GitHub connector fetch-issue tool, then fetch issue comments if needed.

## When a skill says "transition state"

Before applying `ready-for-agent`, keep the issue non-admissible, persist and
read back the current or superseding Agent Brief, and verify any completed
boundary is marked consumed and only the remaining executable tranche is
current. Only then apply the agent-ready label. If the GitHub tools cannot
guarantee that ordering and read-back, do not publish the transition.

At a stop condition, clear the current execution claim, fetch the issue, and
verify that the claimant and claim token are absent before persisting or
publishing a superseding Agent Brief.

For a terminal transition, remove every core active workflow label and clear
the current execution claim before or atomically with closing the issue. Fetch
the closed issue and verify that no active workflow label remains and the
claimant and claim token are absent.

For an active transition, apply or remove labels according to
`.agents/workflows/triage-states.md` using the GitHub connector mutation tools.
