# AGENTS.md

## Repository Reference Context

Before repository module/interface design or agent-instruction authoring,
including direct Codebase Design or Writing for Agents use, read
[repository context](skills/handoff/references/repository-context.md).
Existing .agents/*-standards.md, configured domain routes and ADRs govern;
legacy CONTEXT.md remains supported. Reading the reference invokes no setup.

## Purpose and current scope

This repository is the portable source for Organization OS companion skills.
The selected fifteen-skill suite includes the earlier twelve workflows plus
Workflow Guide, To Questionnaire and Retro. Shared kernels are adopted
complete from the reviewed personal source; original workflows remain generic.
The 1.1.0 release contains the complete selected suite.

The default recipient distribution is a public Organization OS plugin. Its
1.1.0 release includes all fifteen workflows with complete dependencies and
notices. The earlier 1.0.0 starter contains only Meeting Runner and remains
immutable. Each subsequent publication retains its explicit release gate. Folder and
terminal installation are advanced alternatives. Never claim a listing is live
or automatic delivery works until its actual channel is verified.

## Boundaries

- Keep exactly the fifteen selected names declared by scripts/check.py and
  catalog.json. Catalog changes require an explicit scope decision.
- Keep provider, account, workspace, tracker and destination choices in consuming
  workspace configuration. Never include private records, captures, credentials,
  personal addresses, private URLs, machine-local paths or deployment identifiers.
- Preserve complete upstream frontmatter and invocation policy in shared kernels;
  UI metadata remains in agents/openai.yaml. Meeting Runner retains its public
  metadata and three-column contract as an intentional variant.
- Keep complete resources and upstream notices. Update catalog digests explicitly
  after a reviewed source change; validation must never reseal changed content.
- scripts/install.py copies only validated project-local bundles. Preserve foreign
  or modified same-name skills; do not install into personal consumers here.
- Publishing a reviewed source or plugin release requires explicit authority.
  That authority does not grant Notion sharing, account access, consumer migration
  or other external delivery.

Read `.agents/workspace-standards.md` before cross-plane work and the coding,
review and documentation overlays for their phases. `docs/ALIGNMENT.md` records
catalog decisions and outstanding provenance gates; skill resources own output
formats, not the website or template implementation.

## Commands

```sh
python3 scripts/check.py
python3 -m unittest discover -s tests
git diff --check
```

## Publication gate

Before publishing a release, require passing validation and tests,
source/provenance and sensitive-content review, qualified clean-consumer
installation, a fresh direct repository review under the XP maintainer policy,
and explicit publication approval. Record the exact hosted-check status; Actions
capacity exhaustion does not add a review blocker to passing local checks.
Require another independent reviewer only when XP or a non-waivable policy
explicitly requires it. Local review does not assert that hosted checks ran.
