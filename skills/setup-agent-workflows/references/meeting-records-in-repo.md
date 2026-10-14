# Meeting Records: In-Repo Markdown

Date-specific Pre-Call Briefs and completed meeting records live under separate
documented repository routes.

## Preparation Destination

- Define one canonical preparation directory and dated filename convention.
- Place the brief under the configured work-thread directory when the domain
  uses one.
- Use relative links to source docs and tracked work.
- Search by meeting identity and date before creating a new brief.
- Do not copy mutable qualification, project, account, or tracker state.

## Post-Meeting Destination

- Define a separate canonical directory and dated filename convention for
  completed meeting records.
- Create a record only after the meeting. Store the date, participants,
  outcomes, decisions, actions, owners, due dates, and approved links.
- Do not copy preparation, agendas, scripts, attendee research, question lists,
  objection handling, or qualification evidence.
- Search by meeting identity and date before creating a new record.
- Preserve prior decisions, human edits, and carry-forward actions when updating.

## Publication

- Respect `[workflow].publish_by_default`.
- Write only inside the configured preparation or post-meeting path for the
  selected mode.
- After writing, read the file back and verify its path, meeting identity,
  date, content, and links.

## Synthesis Rendering

- Keep exactly one `Topic | Outcome / Decision | Actions` table.
- In each outcome cell, preserve one visible list entry per discrete outcome or
  decision.
- In each actions cell, preserve one Markdown task item (`- [ ]`) per
  accountable next step and owner. Add a due date or tracker link only when it
  is known and useful; do not add placeholder dates or untracked-status labels.
- Use a table-safe Markdown or HTML representation supported by the repository's
  renderer. Read the rendered or parsed record back and verify that outcomes
  remain distinct and actions remain checkable; do not accept flattened prose.

## Execution Follow-Through

Use `.agents/workflows/issue-tracker.md` for tracked actions. Link the work item
from the meeting record and do not duplicate its mutable status.
