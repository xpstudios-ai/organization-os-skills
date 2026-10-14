# Meeting Records: Notion

Date-specific Pre-Call Briefs and completed meeting records use separate routes
inside a configured Notion workspace.

## Preparation Destination

- Record the correct workspace and deterministic rule for resolving the
  approved preparation parent in `.agents/workflows/meeting-records.md`.
- When the domain has an Engagement or work-thread container, resolve that
  exact record and create the date-specific Pre-Call Brief under its configured
  work-thread parent.
- Search by meeting identity and date before creating the brief.
- Do not use the post-meeting database as the preparation destination.
- Update the canonical brief rather than creating a duplicate.
- Keep qualification, account, project, and tracker state in their canonical
  records; link them from the brief without copying mutable detail.

## Post-Meeting Destination

- Record the correct workspace, Meetings database or parent, identity fields,
  and deterministic resolution rule in `.agents/workflows/meeting-records.md`.
- Create or update a post-meeting record only after the meeting has occurred.
- Limit the record to the date, participants, outcomes, decisions, actions,
  owners, due dates, and approved links.
- Do not copy preparation, agendas, scripts, attendee research, question lists,
  objection handling, or qualification evidence into the post-meeting record.
- Search by meeting identity and date before creating a record.
- Preserve human edits, comments, links, and deliberate page structure.

## Optional External-Meeting CRM Follow-Through

When completed external meetings must also update a CRM, record the exact
person and activity data sources, field mappings, identity precedence, and
relation targets in `.agents/workflows/meeting-records.md` or a linked
organization-owned contract.

- Search the person data source before creating. Define exact verified email as
  the first identity key and an exact name-plus-organization fallback.
- Reconcile confirmed external participants only. Preserve existing values and
  human notes; update only newly verified fields. Never create a speculative or
  duplicate person.
- Define distinct fields for internal workspace participants and external CRM
  people when the Meetings schema supports both. Reuse the same resolved
  external person rows for the meeting relation and activity relation.
- Search the activity data source by meeting identity, date, and engagement
  before creating. Create or update exactly one concise activity row.
- Keep the activity row to identity, date, organization, engagement, confirmed
  external people, type, and evidence-backed outcome. Do not copy full notes,
  transcripts, actions, qualification state, or mutable follow-up status.
- Never guess organization, engagement, or person relations. Leave unresolved
  relations unwritten and report them.

## Publication

- Respect `[workflow].publish_by_default`.
- When access is unavailable, return destination-ready content rather than
  choosing a different workspace.
- After a write, fetch the page and verify its title, date, workspace,
  configured preparation or post-meeting parent, content, fields, and important
  links.

## Synthesis Rendering

- Keep exactly one `Topic | Outcome / Decision | Actions` table in the meeting
  page body.
- Preserve one list entry per discrete outcome or decision.
- Preserve one distinct action entry per accountable next step, including its
  owner. Add a due date or tracker link only when it is known and useful; do not
  add placeholder dates or untracked-status labels. Use native to-do blocks
  when the selected Notion surface supports them inside the required structure;
  otherwise use one explicit unchecked marker per action in the table cell.
- Read the page back through the connector and verify that separate outcomes
  and actions were not flattened into prose. Do not claim native checkability
  when the selected Notion table surface stores only rich text.

## Execution Follow-Through

Use `.agents/workflows/issue-tracker.md` for tracked actions. Link the work item
from the meeting page and do not duplicate its mutable status.
