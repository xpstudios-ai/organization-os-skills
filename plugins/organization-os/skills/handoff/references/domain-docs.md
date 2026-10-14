# Domain-Document Discovery

Read the repository's domain-document adapter and explicit paths first.
Those paths govern both vocabulary and the canonical write destination.

When no path is configured:

1. Read `GLOSSARY-MAP.md` when present; otherwise read legacy `CONTEXT-MAP.md`.
   Follow its links to the context relevant to this task. Ask only if the
   relevant context cannot be inferred.
2. Without a map, read the nearest relevant `GLOSSARY.md`, falling back to
   `CONTEXT.md`; then read root `GLOSSARY.md`, falling back to root `CONTEXT.md`, for shared
   vocabulary.
3. If both conventions exist, compare definitions. Report contradictory terms
   before editing; honor the explicit canonical route and keep one write owner.

This rule applies on every machine, in cloud fallbacks, and through installed
links. Reading legacy files never requires renaming them. Update an existing
canonical legacy file in place; use `GLOSSARY.md` for new glossaries. A filename
migration requires explicit scope, updates to callers/maps, and verification.

Create glossaries and ADRs lazily, only when authorized capture has content.
Merely reading vocabulary adds no persistence authority.
