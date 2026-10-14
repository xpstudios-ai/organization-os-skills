# Spec Source: Execution Tracker

Use this starting point when the same tracker stores both specs/PRDs and
implementation issues.

## Source Of Truth

- Product/spec records and implementation issues both live in the execution
  tracker selected in `.agents/workflows/issue-tracker.md`.
- Use parent/child, linked issue, Epic, project, milestone, or label
  relationships according to the selected tracker.
- Repo-local `.agents/work-items/` files are drafts or working notes only unless
  the repo explicitly says otherwise.

## Publishing Rules

- Do not publish tracker records unless the user asked to publish or approved
  the draft.
- Search the tracker before creating a new spec or issue.
- Use plain bullets for acceptance criteria. Completion belongs in tracker
  state, labels, and comments.

## When a skill says "publish a PRD"

Create or update the tracker-native spec/parent record, then link implementation
issues to that source record.
