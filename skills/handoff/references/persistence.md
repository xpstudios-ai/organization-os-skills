# Local-First Persistence

Read the configured specification, tracker, and documentation routes before
choosing a destination. Search active records first; update their canonical
owner instead of creating a parallel plan. Existing repository routes win.

For an explicitly requested setup in an unconfigured personal repository,
default specification and tickets to in-repo Markdown and record that choice.
Ordinary invocation does not scaffold agent configuration. Multi-step work
uses a PRD/spec and executable tickets where useful; a small task needs only
one record with intent, decisions and rationale, acceptance criteria, state,
verification, and next action. Preserve consequential architectural decisions
in the configured ADR route.

Use the established layout. With no layout, prefer
`.agents/work-items/active/<slug>/PRD.md` and `issues/<NNN>-<slug>.md` for
parallel workstreams, or `PRD.md` for one effort. Update records at meaningful
checkpoints and before handoff. Reading archive/history is for archaeology,
not routine active-context loading.

In non-repository work, use an authorised named working folder without
requiring Git or creating `.agents/` scaffolding. For cloud or temporary
filesystems, establish retention or export capability; file creation alone is
not proof of persistence. If no authorised durable destination is available,
return a destination-ready continuation record in chat and say it is unsaved.
Review-only requests stay draft-only. Read back authorised writes.

## Execution Mode

`workflow.execution_mode = "interactive"` uses durable task records without
worker readiness or claims. Triage may recommend an action but must not
publish `ready-for-agent`. Persist scope, decisions, status and verification;
a duplicate Agent Brief is unnecessary.

`workflow.execution_mode = "worker"` requires the configured admission
contract, current brief, holding/readback/readiness ordering, claim or named
serialization, stop and terminal cleanup. An absent mode preserves the
existing legacy contract; it does not infer worker capability or authority.
Changing to interactive is an explicit adapter migration. Switching back to
worker requires admission review before any readiness transition.

Reading this resource does not invoke Handoff or repository setup. Return drafts
in chat by default; create requested files only in an authorised working folder.
