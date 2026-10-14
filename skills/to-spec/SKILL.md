---
name: to-spec
description: Turn approved context into a specification through the configured route.
disable-model-invocation: false
metadata:
  invocation: auto
---

# To Spec

Synthesize established context into one decision-ready specification. Do not restart a
broad interview or invent missing facts.

## 1. Load The Source And Route

Accept approved conversation context, a plan, brief, issue, or existing
specification. Read `AGENTS.md`, documentation standards, and the configured
specification and execution routes. Search the canonical spec source before
creating another record.
Follow [persistence](../handoff/references/persistence.md): use
the existing durable route, with a local-first default for authorised setup.

If the route, destination identity, access, or publication authority is
missing, continue with a destination-ready draft.

Completion criterion: the approved source, existing-record disposition,
destination, and publication boundary are explicit.

## 2. Synthesize The Spec

For repository work, read [repository context](../handoff/references/repository-context.md)
before applying reference guidance. Read `writing-for-agents` and use
[the PRD template](assets/prd-template.md), pruning sections that do not affect
the decision. Use `codebase-design` only when approved scope includes
architecture, interfaces, seams, or adapters.

Include, when applicable:

- outcome, users/stakeholders, ownership, and success evidence;
- problem, scope, non-goals, requirements, and stable system boundaries;
- plain-bullet observable acceptance criteria and verification/testing seams;
- risks, dependencies, assumptions, unresolved questions, and decision owners;
- rollout, migration, support, governance, or operational controls when the
  work actually needs them.

Reference stable artifacts and interfaces rather than line numbers. Mark
unsupported assumptions as owned questions instead of silently resolving them.

Completion criterion: every material decision is represented, every applicable
section has useful content, and unresolved blockers have an owner or trigger.

## 3. Publish Or Return A Draft

Publish only through the configured adapter and only with exact authority.
Preserve canonical identity and parentage, then fetch and verify the written
record. Otherwise return the complete draft and exact missing route or approval.

Do not mark the parent PRD/spec `ready-for-agent` and do not create issues
merely because a PRD exists.

Completion criterion: one canonical specification is read back and verified, or one
destination-ready draft has a precise publication blocker.

## 4. Choose The Next Artifact

Small, already-approved work may flow directly to `implement`. Work that needs
independent executable slices may flow to `to-tickets`. Continue automatically
only when the user requested the broader workflow; otherwise stop with the
recommended next artifact.

## Provenance

Adapted from Matt Pocock's former `to-prd` and current `to-spec` skills in
`mattpocock/skills`, MIT License, Copyright (c) 2026 Matt Pocock.
