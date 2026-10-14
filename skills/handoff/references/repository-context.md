# Repository Context Preflight

Read this before repository module/interface design or agent-instruction
creation, including direct use of Codebase Design or Writing for Agents.
Reading this reference invokes neither Handoff nor repository setup.

1. Read root and applicable nested AGENTS.md. Follow the repository's discovery
   index and approved task scope. Repository rules override generic examples.
2. Read the relevant existing .agents/coding-standards.md,
   .agents/review-standards.md, .agents/document-standards.md and
   .agents/workspace-standards.md. Use .claude/coding-standards.md only when the
   preferred coding overlay is absent. Keep these names and their owners;
   do not rename them to an upstream convention or invent missing standards.
3. Resolve vocabulary through [domain discovery](domain-docs.md) and read
   applicable ADRs from the configured route. Pass the resolved vocabulary and
   local constraints into the design brief; an upstream example naming
   GLOSSARY.md means the repository's canonical domain source, including
   CONTEXT.md when that is its existing owner. Surface conflicts before writes.
4. Preserve the user's and harness's delegation limits. When an upstream
   technique requests unavailable or unauthorized subagents, compare designs
   directly or report the missing capability. It grants no task creation,
   messaging, implementation or publication authority.
5. Apply the repository's test and compatibility policy. Before replacing tests,
   prove the replacement preserves useful observable coverage; a generic
   recommendation does not authorize deleting still-useful regression cases.

If routes or standards are missing, state the exact gap and continue with a
bounded draft or explanation where safe. Read-only discovery does not create
configuration, glossaries or ADRs. In non-repository work, use only the user's
supplied context and authorised persistence route; this preflight does not
require Git or scaffold a repository.

Completion: local standards, canonical vocabulary, relevant decisions, task
scope and available capabilities govern the reference workflow before design
or edits begin. Each proposed interface cites any material local constraint.
