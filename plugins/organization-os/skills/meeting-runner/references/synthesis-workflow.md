# Synthesis Workflow

Load this reference only when the meeting has already occurred or the user asks
to summarize a transcript, recording, capture notes, or pasted meeting text.

## Goal

Turn completed meeting capture material into stakeholder-ready meeting notes
with the date, participants, decisions, outcomes, action items, owners, due
dates, and carry-forward updates. Keep preparation, agendas, scripts, attendee
research, and qualification evidence out of the post-meeting record.

## Inputs

Use whatever is available:

- full pasted transcript,
- exported `.vtt`, `.txt`, or `.docx` transcript,
- meeting, recording, or transcript link supported by an approved connector,
- capture notes,
- previous meeting notes or current action list,
- destination page or parent page.

If transcript retrieval fails through the available approved connector, link,
or storage path, ask the user to provide a transcript or notes export.

## Steps

1. Fetch or ingest the transcript/capture source and extract:
   - actual decisions,
   - new action items,
   - owners and due dates when stated,
   - deferred topics,
   - attendees or participants,
   - risks, blockers, and follow-up meetings.
2. Fetch the destination record through the configured meeting adapter, or
   prepare a creation draft from its approved parent and requested title/date.
3. Fetch previous notes only when carry-forward items are not already visible
   on the destination page or supplied by the user.
4. Classify items as:
   - `Done` - closed in the current meeting or already completed.
   - `Carried Forward` - still open and should appear on the latest notes page.
   - `Deferred/Parked` - acknowledged but intentionally not active this cycle.
   - `New` - created from the current meeting.
5. Rewrite or draft the latest notes page using
   [canonical-meeting-notes.md](canonical-meeting-notes.md).
6. Preserve human edits already present on the destination page. Merge rather
   than overwrite rows, images, links, comments, or manually added notes.
7. Publish only when the user explicitly asks for or approves an external
   write. Otherwise provide the destination-ready draft and a concise change
   summary. After publishing, fetch the page again and verify the result.
8. When the completed interaction changes durable qualification state, update
   or propose an update to the owning qualification master through its
   configured workflow. Reconcile its existing rows in place; do not copy the
   full master table into the post-meeting record.
9. For a completed external meeting with configured CRM follow-through:
   - resolve the organization and engagement before writing;
   - reconcile only confirmed external participants using the adapter's
     search-before-create identity precedence;
   - keep internal workspace participants and resolved external person records
     in their distinct destination fields;
   - reuse the same resolved external person records on the meeting and the
     activity index;
   - search by meeting identity, date, and engagement, then create or update
     exactly one concise activity row;
   - read back and verify every mutation.
   Leave unresolved relations unwritten and report them rather than guessing.

## Extraction Rules

- Treat repeated discussion as context; write only what changed, was decided,
  remains blocked, or needs action.
- Do not copy the Pre-Call Brief, agenda, opening, question list, objection
  handling, full qualification master table, or qualification evidence into
  the post-meeting record. Link the canonical source only when useful.
- Do not infer owners from who spoke unless ownership is explicitly stated.
- Use `Owner TBC` when the action is real but accountability is unclear.
- Keep sensitive transcript details out of stakeholder-facing notes unless the
  user confirms the audience may see them.
- Do not summarize from partial snippets unless the user explicitly says a
  partial summary is acceptable.
- Do not create a person record from an unconfirmed attendee name, overwrite
  existing person data or human notes, or copy full meeting content into an
  activity index.
