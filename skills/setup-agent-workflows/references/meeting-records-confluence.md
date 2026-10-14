# Meeting Records: Confluence

Date-specific Pre-Call Briefs and completed meeting records use separate routes
inside a configured Confluence site and space.

## Preparation Destination

- Record the site, space, approved parent, and deterministic title/date rule in
  `.agents/workflows/meeting-records.md`.
- Search by page ID when supplied, then exact meeting identity and date before
  creating or updating the brief.
- Do not use the post-meeting parent or page as the preparation destination.

## Post-Meeting Destination

- Record the site, space, approved parent, and deterministic title/date rule in
  `.agents/workflows/meeting-records.md`.
- Create or update a post-meeting page only after the meeting has occurred.
- Preserve human edits, comments, links, deliberate page structure, prior
  decisions, and active carried-forward actions.
- Keep preparation, agendas, scripts, attendee research, question lists,
  objection handling, and copied qualification evidence out of the record.

## Synthesis Rendering

- Keep exactly one table with `Topic`, `Outcome / Decision`, and `Actions` in
  that order.
- In every `Outcome / Decision` cell, encode one native ADF `bulletList` whose
  `listItem` children hold the discrete outcomes or decisions. Do not submit a
  paragraph containing bullet characters.
- In every `Actions` cell with active work, encode one native ADF `taskList`
  whose `taskItem` children each contain one accountable next step and owner.
  Add a due date or tracker link only when it is known and useful; do not add a
  placeholder date or untracked-status label. New active actions use the exact
  ADF unchecked state formed by joining the uppercase strings `TO` and `DO`
  without a separator; preserve an existing task item's state when updating it.
- For a topic with no action, write `None`; do not create a checkable task that
  represents the absence of work.
- Use stable unique `localId` values required by ADF. Do not replace native task
  items with bullet lists, paragraphs, `<br>` separators, or Unicode checkbox
  characters.

## Publication And Verification

- Respect `[workflow].publish_by_default` and update the canonical page in
  place when the user supplies it.
- Prefer an ADF-capable Confluence API or connector for synthesis writes.
- After writing, fetch the page in ADF and verify its page ID, title, date,
  parent/space, links, and table structure.
- Inspect every topic row: the middle cell must contain `bulletList`; each
  actionable final cell must contain `taskList`; and expected children must be
  `listItem` and `taskItem` nodes. Markdown read-back may flatten table-cell
  blocks and is not sufficient structural verification.

## Execution Follow-Through

Use `.agents/workflows/issue-tracker.md` for tracked actions. Link the work item
from each relevant task item and do not duplicate its mutable status.
