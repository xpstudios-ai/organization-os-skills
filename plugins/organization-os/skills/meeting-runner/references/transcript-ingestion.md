# Transcript Ingestion

Read this reference only when meeting capture is not already supplied as text.

## Preferred Inputs

Use the least-invasive source that provides the full capture:

1. User-supplied `.vtt`, `.txt`, `.md`, `.docx`, or pasted transcript.
2. A specific recording or transcript link accessible through an approved
   connector.
3. A provider API scoped to the identified meeting and the signed-in user's
   existing access.
4. A user-exported transcript when the current runtime lacks access.

Do not request tenant-wide or workspace-wide access when a supplied file,
specific link, or user-delegated connection is enough.

## Retrieval Rules

- Resolve the exact meeting title and date/time before fetching.
- Prefer transcript text over audio/video processing when both exist.
- Prefer approved connectors or official provider APIs over browser scraping.
- Do not scan unrelated calendars, mailboxes, drives, or recording folders.
- If the source requires a connector that is unavailable, name the missing
  access and ask for an export. Do not invent a local recording pipeline.
- If only a partial transcript is available, label the result partial and ask
  whether to proceed.

## Normalization

- Preserve speaker names and utterance order.
- Remove timestamps unless timing is decision-relevant.
- Keep exact dates, amounts, identifiers, and commitments.
- Mark unclear speakers, owners, dates, and decisions as `TBC`.
- Treat transcript labels as evidence, not as a complete attendance record.

The normalized transcript is private working context. Publish only the approved
meeting record, never the raw capture, unless the user explicitly asks and the
destination audience is authorized.
