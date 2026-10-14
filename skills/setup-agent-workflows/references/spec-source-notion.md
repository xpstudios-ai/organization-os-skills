# Spec Source: Notion

Use this starting point when stakeholder-facing PRDs, charters, engagement
context, governance notes, and reviewed evidence live in Notion.

## Source Of Truth

- Confirm the correct workspace, database, and parent page before reading
  or writing. Do not infer workspace ownership from a page title alone.
- Notion is the durable stakeholder source for specs and decision records.
- Implementation issues normally live in Linear, GitHub Issues, repo markdown,
  or another tracker selected in `.agents/workflows/issue-tracker.md`.
- Tracker issues should link back to the relevant Notion source page.
- Repo-local `.agents/work-items/` files are drafts or working notes only unless
  the repo explicitly says otherwise.

## Publishing Rules

- Do not publish unless the user asked to publish or approved the draft.
- Search the correct workspace before creating a new page.
- Update an existing canonical page instead of creating a duplicate.
- After any write, fetch the created or updated page and verify its title,
  body, database or parent location, and source links.
- Use plain bullets for acceptance criteria. Execution status belongs in the
  configured tracker, not duplicated task checkboxes in Notion.

## When a skill says "publish a PRD"

Publish or update the approved Notion page and record its URL in the final
response or linked tracker issue.
