---
name: setup-agent-workflows
description: Configure a repository's agent discovery, workflow adapters, and standards overlays for local or team-shared work.
metadata:
  invocation: manual
disable-model-invocation: true
---

# Setup Agent Workflows

Explicitly bootstrap repository workflow configuration. This skill is for a
repository; do not invent `AGENTS.md` or `.agents/` scaffolding for software
whose own runtime manages skills, routines, or configuration.

## 1. Discover The Repository And Harnesses

Read repository remotes, root and nested instructions, package/build files,
existing agent configuration, skills, overlays, workflow files, docs, ignored
runtime state, and verification commands.

Detect the harnesses actually used. Examples include:

- Codex: `AGENTS.md` and repository `.agents/skills/`;
- Claude-compatible tools: `CLAUDE.md` and `.claude/skills/`, with a thin
  import of canonical instructions when supported;
- Cursor or Grok Build: their documented project skill/discovery locations;
- Copilot: `.github/copilot-instructions.md` when the repository uses it.

Treat these as compatibility examples, not universal requirements.

Completion criterion: canonical instructions, used harnesses, existing routes,
and generated versus human-owned files are known.

## 2. Select Local-Only Or Team-Shared Mode

Infer the mode from the request and repository. Local-only configuration stays
untracked and user-scoped. Team-shared configuration uses committed,
provider-neutral source plus only the thin bridges required by used harnesses.

Ask only when the choice would change tracked files or visibility and cannot be
inferred. Do not ask the user to choose defaults already established by the
repository.

Completion criterion: ownership, visibility, and propagation for every planned
file are explicit.

## 3. Resolve Workflow Routes

Read [the adapter catalog](references/adapter-catalog.md). Resolve independently:

1. specification source;
2. execution tracker;
3. triage mapping, Agent Brief persistence, admission claim or serialized
   worker authority, readback, and terminal cleanup;
4. domain documentation;
5. separate meeting preparation and post-meeting destinations, plus optional
   CRM mappings; and
6. publication defaults.

Use repository evidence and configured defaults. Ask one short question only
for a genuinely missing destination identity or policy choice. Never infer an
external workspace, project, database, parent, or credentials from a familiar
name.

For unconfigured personal work, default spec and tickets to in-repo Markdown
and `workflow.execution_mode = "interactive"`. Preserve existing routes and
legacy admission until explicitly migrated. Follow [persistence](../handoff/references/persistence.md).
Interactive setup needs durable task/readback routes, not worker claims;
worker setup must resolve all admission mechanics below.

Do not leave `holding state`, `execution claim`, `Agent Brief location`, or
`read back` as abstract placeholders. Mark agent-ready publication unsupported
when the selected adapter cannot guarantee the required ordering.

Completion criterion: each enabled workflow has one deterministic search,
fetch, write, readback, and failure route; unsupported workflows are explicit.

## 4. Resolve Standards And Discovery

Prepare only needed overlays:

- `.agents/coding-standards.md`: Style, Testing, Architecture, Security,
  Commands, and Gotchas;
- `.agents/review-standards.md`: in-task review, external independence requirements, gates,
  changed surfaces, and severity;
- `.agents/document-standards.md`: canonical docs, publication, and
  stale-reference sweeps;
- `.agents/workspace-standards.md`: planes, ownership, generated views, and
  propagation.

Read [repository context](../handoff/references/repository-context.md). Merge a
short startup pointer into the canonical AGENTS.md: before repository design or
instruction authoring, read .agents/SKILLS.md's Repository Context section (or
point directly to the configured package's repository-context.md). Preserve
existing instructions and overlay names. Verify direct Codebase Design/Writing
for Agents use loads those rules; preserve CONTEXT.md and custom domain routes.
Keep provider bridges thin and create them only for detected harnesses.

Completion criterion: every selected skill can resolve repository facts without
duplicating its generic workflow.

## 5. Write The Approved Setup

An explicit invocation authorizes the requested repository-local setup. Show a
compact change summary before writing only when a derived choice would create a
surprising tracked or external effect. External account connection, workspace
selection, publication, and credential changes still require their own
authority.

Build workflow files from the selected references, replace placeholders with
verified facts, and delete unused adapter branches. Do not store credentials or
machine-specific paths in tracked configuration.

Completion criterion: only canonical, mode-appropriate files are written and
no unused provider or adapter configuration remains.

## 6. Verify

Run repository checks, read every edited file back, inspect discovery for each
used harness, and exercise or structurally verify holding state → Agent Brief
readback → readiness → claim/serialization → claim release at stop or terminal
cleanup.

Completion criterion: routing is discoverable and deterministic, validation
passes, and every unsupported or externally gated route is named.

## Completion

Report mode, configured routes and standards, harness bridges, verification,
and exact remaining external identities or authority.
