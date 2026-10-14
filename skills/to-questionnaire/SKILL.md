---
name: to-questionnaire
description: Draft a questionnaire to obtain missing facts or decisions from someone else.
disable-model-invocation: false
metadata:
  invocation: auto
---

# To Questionnaire

Turn information the user cannot supply alone into focused questions for a
recipient. Infer known context; ask only for missing recipient expertise,
the decision riding on the answers, or constraints that change the document.

Map each necessary fact or decision to one answerable question. Put critical
questions first, group related questions, and include answer space. State
purpose, relevant context and how answers will be used; include a deadline or
effort estimate only when known. Partial answers and uncertainty are useful.
Avoid compound questions, invented facts and unnecessary sensitive information.

Follow [persistence](../handoff/references/persistence.md).
Attach an authorised questionnaire to the owning task/spec; otherwise return
a complete draft. Report the saved path and readback, or that it remains in chat.
Drafting grants no authority to send email, message the recipient, or publish
to another account. Completion: every named information gap has a question and
the recipient can answer without access to the original conversation.

Example: “Draft a questionnaire for the operator about these unresolved loads.”

## Provenance

Adapted from Matt Pocock's `to-questionnaire`, MIT License,
Copyright (c) 2026 Matt Pocock.
