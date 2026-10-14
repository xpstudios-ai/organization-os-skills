---
name: repo-document
description: Assess and update repository documentation after a passing review or meaningful change, including stale references and agent guidance.
disable-model-invocation: false
user-invocable: true
argument-hint: "[version or description of changes]"
metadata:
  invocation: auto
---

# Repo Document

Keep human documentation, agent guidance, discovery, and standards aligned
after a passing review or meaningful change.

## 1. Load The Documentation Contract

Find the repository root and read `AGENTS.md`, then applicable documentation,
review, coding, and workspace standards. Inspect the current diff, staged diff,
and recent commits.

If no documentation overlay exists, use the repository's established README,
agent guidance, changelog, docs, and skill-index surfaces. State the missing
overlay when repository-specific publication rules matter.

For each affected document, establish its audience, reader question, allowed
content, owning sources, and update trigger from its existing purpose or
declared contract. Distinguish guides and references from operational status
surfaces and task/evidence records. Load linked document contracts when the
overlay routes to them; preserve each repository's own standards and triggers.

Completion criterion: destination purpose, changed claims, owning sources,
publication authority, and generated or external boundaries are known.

## 2. Assess The Delta

Start from changed terms, paths, commands, config keys, skill names, interfaces,
and behavior. Run targeted `rg` sweeps for their stale references. Widen the
sweep only when evidence shows the impact is broader.

For each affected surface, identify what its reader must understand or do
differently, then update it or record a specific no-change reason. A completed
task or matching review trigger alone does not require a document write.
Translate the delta into the destination's purpose: guides describe the current
operating model and reader actions; status surfaces summarize current readiness;
task/evidence records retain execution history and verification receipts.

Keep detailed evidence in its owning record and link it when needed. Include a
limitation in a guide only when it changes the reader's action. Preserve required
machine correlation metadata and version bindings in their declared fields;
they are not narrative history. Revise and
consolidate the affected section, removing obsolete caveats and duplication;
do not preserve task history by inserting it into an existing section.
Preserve one source of truth and the destination's unrelated useful content.
Never edit generated, vendored, linked, or installed views as canonical source.

Completion criterion: every affected surface is updated or explicitly assessed,
with no known stale active reference or task receipt substituted for guidance.

## 3. Maintain Standards Once

Update a `.agents/*-standards.md` overlay only when the change or review proves
a durable rule about coding, review, documentation, or workspace ownership.
Do not encode one-off task history, speculate, or invoke this workflow
recursively.

For a repeated failure, prefer a deterministic check when a tool can decide
correctness reliably. Put judgment-based guidance in the owning standards
overlay, with a concrete trigger. Avoid adding a prose rule that duplicates
an existing automated gate.

Completion criterion: durable standards changes are captured once and
validated, or no standards maintenance is warranted.

## 4. Handle External Destinations

An external destination write requires authority for that exact destination
and mutation. Fetch the current record first, revise the affected canonical
section in place, and read it back after writing. Do not append a session log
unless the destination is explicitly append-only.

If destination identity, workspace, access, or publication authority cannot be
verified, return destination-ready content and the exact blocker instead of
writing or claiming alignment.

Completion criterion: every authorized external update is read back and
verified, or remains an unapplied draft with a precise blocker.

## 5. Verify And Route Review

Run structural checks for edited Markdown, config, manifests, links, indexes,
and discovery metadata. Review the final document against its reader question:
each added paragraph must support that purpose, evidence links must resolve to
their owners, and growth must reflect new reader needs rather than accumulated
work. Apply this check to replacements as well as appended content.
A semantic docs, standards, contract, or skill change
invalidates the prior candidate verdict and returns to the required review
route. Plain non-semantic documentation may use direct review unless repository
policy requires independence.

Completion criterion: the final candidate fits its document purpose, is
structurally valid, and has the review evidence required for its semantics.

## Completion

Report docs updated or assessed, standards maintenance, stale-reference sweeps,
external write/readback results, checks, review route, and exact skips.
Keep this completion report in the work record, not inside a guide or reference.
