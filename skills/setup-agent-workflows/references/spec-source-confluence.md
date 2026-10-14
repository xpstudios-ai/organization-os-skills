# Spec Source: Confluence

Use this starting point when stakeholder-facing PRDs, charters, governance
notes, and reviewed evidence live in Confluence.

## Source Of Truth

- Confluence is the stakeholder-facing source for specs and decision records.
- Implementation issues may live in Jira, Linear, GitHub Issues, repo markdown,
  or another tracker selected in `.agents/workflows/issue-tracker.md`.
- Tracker issues should link back to the relevant Confluence source page.
- Repo-local `.agents/work-items/` files are drafts or working notes only unless
  the repo explicitly says otherwise.

## Publishing Rules

- Do not publish to Confluence unless the user asked to publish or approved the
  draft.
- Search Confluence before creating a new page.
- After any write, fetch the created/updated page and verify title, body,
  parent location, and source links.
- Use plain bullets for acceptance criteria. Completion belongs in the execution
  tracker, not Confluence task checkboxes.

## When a skill says "publish a PRD"

Publish or update the Confluence page and record the URL in the final response
or linked tracker issue.
