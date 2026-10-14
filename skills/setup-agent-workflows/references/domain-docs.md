# Domain Docs

Generic engineering skills should read the repo's domain docs before making
architecture-sensitive changes.

## Default Layout

- Root `AGENTS.md` is the primary provider-neutral contract.
- Optional root `GLOSSARY.md` contains domain vocabulary; existing canonical
  `CONTEXT.md` files remain supported.
- Optional `docs/adr/` contains architecture decisions.
- Optional `.agents/workflows/` contains issue tracker, triage, and domain-doc
  config for skills.

## Multi-Context Repos

If the repo has subprojects or packages with their own `AGENTS.md` /
domain glossary, read the nearest relevant file first, then the root file.

## Consumer Rules

- Use vocabulary from `AGENTS.md` and the configured canonical glossary.
- Respect ADRs unless the user explicitly asks to revisit them.
- Create glossaries and ADRs lazily when a real term or decision needs capture.

## Filename Compatibility

Honor configured domain-document paths first. Otherwise follow GLOSSARY-MAP.md
to the relevant context; fall back to CONTEXT-MAP.md for existing repos. Without
a map, use the nearest relevant GLOSSARY.md, then legacy CONTEXT.md. Read legacy
files in place on every machine; a sync never renames domain files.

When new and legacy files both exist, compare their content and surface
conflicting definitions before writing. Select one canonical destination; keep
other files as pointers only after authorized migration. New glossaries use
GLOSSARY.md. Existing canonical legacy files retain their name until explicitly
migrated. Create files only when a real term or decision needs capture.
