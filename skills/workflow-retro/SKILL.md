---
name: workflow-retro
description: Review session evidence and propose changes that improve future agent work.
disable-model-invocation: false
metadata:
  invocation: auto
---

# Retro

Use the named session, or the current session when unspecified. Read its actual
outputs, failures, verification and relevant rules; distinguish observed issues
from missing evidence. Evaluate navigation, checks, instruction clarity, tool
cost, information access and continuation quality.

Read existing checks before proposing another. Prefer a deterministic check for
a mechanical failure and judgment guidance for decisions a check cannot make.
For every proposed change, give the observed failure, owning surface, expected
benefit and smallest useful validation. Remove no rule merely because it was
not exercised in this session. Avoid turning one task's particulars into global
policy. A clean session may need no change.

Follow [persistence](../handoff/references/persistence.md) for an
authorised report. Proposals alone do not edit skills, hooks, standards, memory
or access. Approved standing documentation changes flow through `repo-document`
when available; otherwise name the owning document and remaining authority.
Completion: recommendations are evidence-backed, ranked by consequence, and
separate from applied changes and their verification.

Example: “Run a workflow-retro on this migration and suggest the smallest useful fixes.”

## Provenance

Adapted from Matt Pocock's `retro`, MIT License, Copyright (c) 2026 Matt Pocock.
