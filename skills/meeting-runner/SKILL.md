---
name: meeting-runner
description: Provider-neutral meeting workflow for date-specific Pre-Call Briefs and separate durable post-meeting records with decisions, actions, participants, owners, and due dates. Use for meeting preparation or synthesis when no organization-specific meeting adapter applies, and for configured destination, CRM, and action routes.
---

# Meeting Runner

Prepare useful date-specific Pre-Call Briefs, turn completed capture into
separate durable post-meeting records, and keep unresolved execution work moving
without duplicating state.

## 1. Load The Routes

Read:

1. `AGENTS.md`
2. `.agents/workflows/meeting-records.md`
3. `.agents/workflows/issue-tracker.md` when actions may become tracked work
4. `.agents/document-standards.md` when the meeting changes canonical docs

Use the meeting-records workflow as the default destination adapter and the
issue-tracker workflow as the execution adapter. Treat exact preparation or
post-meeting destinations supplied by the user, together with an available
connector or API, as per-run destination adapters for that request. The meeting
adapter must resolve two distinct routes: a preparation destination for
Pre-Call Briefs and a post-meeting destination for completed meeting records.
When it configures CRM follow-through for external meetings, it must also
resolve the person-identity and activity-index destinations, identity
precedence, relation fields, and read-back rules. Do not infer a provider,
workspace, project, database, work-thread parent, record parent, or CRM relation
from a familiar name.

If neither a configured meeting-records workflow nor a per-run destination
adapter is available, preparation and draft synthesis may continue, but do not
perform an external write. Ask for the destination or ask the user to configure
the adapter. A missing workflow file alone must not block a targeted update
when the exact destination is supplied, the write tool is available, and the
user requested or approved the write.

Completion criterion: the route for the selected mode is resolved, preparation
and post-meeting destinations cannot be conflated, configured CRM routes are
deterministic, and execution follow-through has one source of truth.

## 2. Resolve The Meeting

Ask only for inputs that cannot be resolved from approved context:

1. Mode: preparation for an upcoming meeting or synthesis of a completed one.
2. Exact meeting: title and date/time, supplied transcript or capture, meeting
   link, or existing notes record.
3. Preparation work-thread parent or post-meeting record parent when the
   adapter cannot resolve the selected mode.
4. Previous notes or current actions only when carry-forward state is not
   visible in the destination or supplied context.

If multiple candidate meetings or records remain, show a short dated list and
ask the user to choose.

Completion criterion: the exact meeting, mode, and destination are unambiguous.

## 3. Choose One Mode

- **Preparation:** create a date-specific Pre-Call Brief (Meeting Guide) with
  the meeting goal, opening, prioritized questions, likely objections and
  responses, minimum safe data ask, and desired exit. Then read
  [preparation-workflow.md](references/preparation-workflow.md) and use
  [pre-call-brief-template.md](assets/pre-call-brief-template.md).
- **Synthesis:** use a transcript, recording, capture notes, or pasted text to
  extract decisions, outcomes, participants, and actions. Then read
  [synthesis-workflow.md](references/synthesis-workflow.md) and apply the
  single-table synthesis contract under [Canonical Formats](#canonical-formats).

If both modes are requested, create the Pre-Call Brief before the meeting and a
separate post-meeting record after capture becomes available. Cross-link them
when the adapter supports it; never turn the prep page into the meeting record
or copy the prep into the post-meeting database.

Completion criterion: the selected workflow has produced every required
section for its mode, and synthesis satisfies the single-table synthesis
contract.

## 4. Preserve The Destination

Follow `.agents/workflows/meeting-records.md` for exact search, create, update,
field, parent, publication, and verification behavior for the selected route.

- Search the selected route before creating; update the canonical brief or
  post-meeting record instead of duplicating it.
- Preserve human edits, comments, links, and deliberate structure.
- Publish only when the user requested the write or approved the draft.
- After a write, fetch or read the record again and verify the adapter's
  required identity, location, content, fields, and links.
- Never write preparation, agendas, scripts, attendee research, or copied
  qualification evidence into a post-meeting record.

Completion criterion: the canonical record is updated or a destination-ready
draft is returned, with no duplicate mutable record created.

## 5. Ingest Capture Safely

Use supplied transcript or notes content directly. Do not re-export a recording
when the full content is already available.

For recordings, meeting links, or exported transcript files, read
[transcript-ingestion.md](references/transcript-ingestion.md). Prefer the
configured connector or provider interface over browser scraping. Do not scan
broad calendars, mailboxes, workspaces, or recording folders without a
user-supplied scope.

Normalize capture before synthesis:

- preserve speaker names when present;
- remove timestamp noise unless timing changes the meaning;
- treat speaker labels as evidence, not guaranteed attendance;
- never infer a decision, owner, or due date from vague discussion;
- mark unresolved ownership or wording as `TBC`;
- do not summarize a partial capture as complete unless the user accepts it.

If capture cannot be retrieved, ask for a transcript or notes export. Do not
invent a recording workaround or request broader account access than the
specific meeting requires.

Completion criterion: the synthesis is traceable to available capture in
private working context and its completeness is explicit.

## 6. Carry Forward Execution Work

- Promote unresolved actions from prior notes into the latest meeting record.
- Give each active action a current owner, concrete next step, or explicit
  `Deferred/Parked` status.
- Follow `.agents/workflows/issue-tracker.md` for searches and mutations.
- Search for existing work before proposing or creating a new item.
- Mutate tracked work only when the user requested or approved it.
- Link tracked work from the meeting record without duplicating mutable status.
- After a tracker write, fetch or read the item and verify the adapter's
  required fields and relationships.

Completion criterion: every active action has one owner/status source and all
external mutations are verified.

## 7. Reconcile External Meeting CRM

Run this step after synthesizing a completed external meeting when the committed
meeting adapter configures CRM follow-through. Skip it for internal-only
meetings.

- Resolve the canonical organization and engagement before any CRM write.
  Never guess a missing relation; report it as unresolved.
- Reconcile confirmed external participants only. Search the configured person
  store before creating: use exact verified email first, then the adapter's
  exact name-plus-organization rule. Do not create speculative people or
  duplicates.
- Update only newly verified person fields. Preserve existing values, human
  notes, and deliberate relations; report conflicts instead of overwriting
  them.
- Keep internal workspace participants in the destination's internal-person
  field. Put resolved external person records in its external-contact field.
  Never substitute one relation type for the other.
- Reuse those exact resolved external person records on the activity index.
- Search the activity destination by the adapter's meeting identity, date, and
  engagement rule. Create or update exactly one concise activity row for the
  meeting, then verify it by reading it back.
- Keep the activity row to identity, date, organization, engagement, confirmed
  external contacts, activity type, and evidence-backed outcome. Do not copy
  the detailed notes, transcript, actions, qualification master, or mutable
  follow-up status.

If the CRM contract, organization, engagement, or contact identity remains
unresolved, the post-meeting record may still be completed, but do not perform
the unresolved CRM mutation. Report the missing route or relation explicitly.

Completion criterion: confirmed external people are deduplicated, the same
resolved person records are linked from both the meeting and its one activity
index row, and every configured write has been read back and verified.

## Canonical Formats

- For preparation, use
  [pre-call-brief-template.md](assets/pre-call-brief-template.md). When a
  qualification master exists, select only its relevant unresolved rows for
  this meeting and link the canonical record. Add live wording in the brief;
  do not make it a master qualification, project, or account record.
- **Single-table synthesis contract:** for synthesis, use
  [canonical-meeting-notes.md](references/canonical-meeting-notes.md). Render
  exactly one table, with the columns `Topic`, `Outcome / Decision`, and
  `Actions` in that order. Put every accountable next step in the final
  `Actions` column; do not create a separate actions table or transpose the
  three columns into rows. A destination-specific template may change
  surrounding headings or prose, but not this table contract. Capture only the
  completed meeting's date, participants, outcomes, decisions, actions, owners,
  due dates, and approved links.
- After a relevant interaction changes durable qualification state, reconcile
  or propose an update to the owning qualification master through its
  configured workflow. Do not copy the full master table into the meeting
  record.
- For tracked actions, link the work item and record the meeting-time commitment
  rather than duplicating its mutable status history.

## Privacy

Treat transcripts, recordings, capture records, source links, and capture
provenance as confidential by default.

- Treat private capture as a silent input. Publish only the synthesized meeting
  content. Disclose source provenance only when the source is not personal,
  governing routes permit disclosure, and the user explicitly approves that
  exact disclosure to that audience.
- Do not name, cite, link, embed, attach, or describe a private capture system,
  workspace, page, recording, transcript, metadata, or capture mechanism in a
  stakeholder-facing record or team correspondence.
- When private or personal capture feeds a team destination, never reveal the
  capture provider or source provenance in the destination, even when the
  source content itself is authorized for synthesis.
- Keep source traceability in private working notes or a private status report
  to the requester, not in the meeting record or generated correspondence.
- Before publishing, inspect the outgoing payload for capture-provider names,
  source domains, links, page or recording identifiers, source titles, and
  unnecessary raw excerpts; remove them unless governing routes permit and the
  user approved that exact disclosure to that audience.
- Do not publish raw transcripts, internal reasoning, local paths, auth data,
  connector output, or draft clutter.
- Do not change sharing, retention, or permissions unless explicitly requested
  and within scope.

## Completion

Report:

1. Sources read and records drafted or updated, using destination-safe wording;
   never include private source provenance in stakeholder artifacts or team
   correspondence.
2. Items carried forward.
3. Pre-Call Brief content or post-meeting outcomes, decisions, actions, and
   execution follow-through captured for the selected mode.
4. For a completed external meeting, CRM people and the single activity row
   reconciled, or each unresolved relation reported.
5. Verification performed after external writes.
6. Missing access, capture, destination, owner, relation, or approval.
