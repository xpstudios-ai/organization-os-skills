# Source Alignment

This is the 1.1.0 source baseline for the public fifteen-skill release.
Meeting Runner 1.0.0 stays immutable. Template records, installed user skills
and ordinary consumers keep their separate owners and propagation gates. The public source starts at
`9fb3efe16fb269c4320d26e08dea6a330e3374af`; XP starts at
`866b8af7471ec56d1b64b5349bd9bc4746ab4d1b`. Candidate folders and resource digests
are recorded explicitly in the catalog; these base revisions alone do not
identify the changed candidate. Bind publication to the reviewed source snapshot.
The adopted XP source is the isolated reviewed commit `572c9d2ab17bb074d92f6e95d8ca31bd4872b078`.

## Dispositions And Closure

| Identifier | Disposition | Mandatory dependencies | Complete-folder comparison |
| --- | --- | --- | --- |
| codebase-design | Exact pinned Matt folder | handoff | Complete XP/public folder parity |
| diagnose | Retain approved portable adaptation | codebase-design, handoff | Complete XP/public folder parity |
| handoff | Retain approved portable adaptation | None | Complete XP/public folder parity |
| repo-document | Retain approved portable adaptation | None | Complete XP/public folder parity |
| repo-review | Retain approved portable adaptation | None | Complete XP/public folder parity |
| setup-agent-workflows | Retain approved portable adaptation | handoff | Complete XP/public folder parity |
| to-questionnaire | Retain approved portable adaptation | handoff | Complete XP/public folder parity |
| to-spec | Retain approved portable adaptation | codebase-design, handoff, writing-for-agents | Complete XP/public folder parity |
| to-tickets | Retain approved portable adaptation | handoff, triage | Complete XP/public folder parity |
| triage | Retain approved portable adaptation | None | Complete XP/public folder parity |
| workflow-guide | Retain approved portable adaptation | handoff | Complete XP/public folder parity |
| workflow-retro | Retain approved portable adaptation | handoff | Complete XP/public folder parity |
| writing-for-agents | Exact pinned Matt folder | handoff | Complete XP/public folder parity |
| meeting-runner | Retain each package's variant | None | XP generic; public unchanged seven-file, three-column Topic, Outcome / Decision, Actions contract |
| qualify-opportunity | Public-only portable workflow | None | Absent from XP; four configurable areas and independent property writes |

Writing for Agents and Codebase Design match complete Matt Pocock directories
at `49dd158d1076134a641b33efb035946536778336` with no added notices, metadata
rewrites or resources. Actual callers use `SKILL-MECHANICS.md`, `DEEPENING.md`
and `DESIGN-IT-TWICE.md`. Their full MIT notice remains outside exact folders
and is delivered by folder and plugin installers. Other retained adaptations
preserve persistence, direct review, worker admission, portability and invocation
boundaries; repo/package facts remain in adapters and overlays. Repo Document
is the maintainer's original workflow. README acknowledgement is retained.

The 13 shared folders are complete-directory identical across XP and public.
Meeting Runner is the sole shared-name exception. Retro keeps identifier
`workflow-retro` and display name Retro. Setup Agent Workflows remains explicit
and repository-only. Persistence moved into Handoff; reading its references
does not invoke Handoff. Workflow Guide, To Questionnaire and Retro therefore
have no absent generic-setup dependency for future organization adoption.
Organization adoption, parity and runtime acceptance remain a separate tranche.

## Business Workspace Contract

The public product guide and public-only qualification resource own business
setup. Shared Handoff remains generic. The default business flow asks for the
Notion home and verifies account/copy ancestry, then the agent saves a narrow
personal startup preference using the client's supported instruction discovery.
No folder selection or repository scaffolding is required. Existing project
routes take precedence. Drafts remain in chat; credentials stay app-managed;
user settings and records stay outside replaceable plugin resources.

Codex fresh-process recall from a different empty directory passed with a local
fictional map. Claude Code's documented personal-instruction route is available,
but authenticated inference remains unverified because the test client is not
signed in. Saving, fresh-model recall, live account/copy access and plugin-update
preservation are distinct checks. Failed recall uses a per-chat home link and
unsaved drafts, never a guessed route. Setup is client/profile-local.

## Qualification Contract

Briefly consider customer need, expected value, ability to deliver and buying
decision/timing by default. Workspace configuration and per-run subsets or skips
are allowed. Excluded areas are unassessed, never positive. Return a concise
decision, recommendation, facts, material questions and useful next step. Use
the existing questions table when useful. Pricing, technical and operations
detail appears only when material or requested; no mandatory sales framework,
industrial checks, private strategy or numeric score is introduced.

An approved save may update matching Qualification Verdict and Assessment Date
with verified mapping and readback. Evidence State and Pursue remain unchanged
unless explicitly instructed. A skipped assessment leaves all fields unchanged.
Keep one assessment child under Engagement Records without a duplicate parent
summary. The template/website owner controls their separate implementations.

## Repository Compatibility

Matt's exact folders remain unchanged. Package dependency closure carries
Handoff's repository-context and domain-discovery references. Before direct
Codebase Design or Writing for Agents use, the repository's startup instructions
must point to that preflight, either directly or through the generated skill
index. Explicit Setup Agent Workflows merges the pointer without replacing
existing instructions; ordinary installers do not rewrite AGENTS.md.

The preflight preserves existing .agents/*-standards.md names, the legacy
.claude/coding-standards.md fallback, configured vocabulary and ADR routes,
and CONTEXT.md / CONTEXT-MAP.md support. It applies local delegation and useful
regression-coverage policies to generic upstream examples. Reading supporting
references invokes no workflow and authorizes no setup or external write.

## Evidence And Outstanding Gates

Package validation, resource pins, privacy checks, complete-folder comparisons,
license delivery, dependency installations and preservation/rollback tests are
source evidence. Contained native plugin discovery or lifecycle checks are not
fresh inference or proof of connector writes. Record actual tests and skips in
the release receipt, including exact source digests and actual hosted-check
status. A fresh direct originating-chat review and repo-document assessment
precede publication. Windows native acceptance, live account/copy discovery,
authenticated Claude Code inference and customer writes remain distinct checks;
a Git marketplace release does not claim public app-directory acceptance.

## Complete-Folder Provenance

The source revision for every mapped Matt directory below is the full pin
`49dd158d1076134a641b33efb035946536778336`. Comparison includes all files,
not only SKILL.md. XP/public parity for each row is exact; these differences
are against the corresponding Matt folder. Package notices outside exact folders
are included separately in delivery verification.

| Identifier | Compared owner/path | Full resource difference |
| --- | --- | --- |
| codebase-design | `skills/engineering/codebase-design` at `49dd158` | Added: none; removed: none; changed: none |
| diagnose | `skills/engineering/diagnosing-bugs` at `49dd158` | Added: `UPSTREAM-LICENSE.txt`, `references/domain-docs.md`, `references/feedback-loop.md`, `scripts/hitl-loop.template.ps1`; removed: none; changed: `SKILL.md`, `agents/openai.yaml`, `scripts/hitl-loop.template.sh` |
| handoff | `skills/productivity/handoff` at `49dd158` | Added: `references/domain-docs.md`, `references/persistence.md`, `references/repository-context.md`; removed: none; changed: `SKILL.md`, `agents/openai.yaml` |
| repo-document | Original maintainer workflow | `SKILL.md`, `agents/openai.yaml` |
| repo-review | `skills/engineering/code-review` at `49dd158` | Added: `UPSTREAM-LICENSE.txt`, `references/code-change-baseline.md`, `references/refactoring.md`; removed: none; changed: `SKILL.md`, `agents/openai.yaml` |
| setup-agent-workflows | `skills/engineering/setup-matt-pocock-skills` at `49dd158` | Added: `references/adapter-catalog.md`, `references/domain-docs.md`, `references/issue-tracker-github.md`, `references/issue-tracker-in-repo.md`, `references/issue-tracker-interactive.md`, `references/issue-tracker-jira.md`, `references/issue-tracker-linear.md`, `references/meeting-records-confluence.md`, `references/meeting-records-draft-only.md`, `references/meeting-records-in-repo.md`, `references/meeting-records-notion.md`, `references/spec-source-confluence.md`, `references/spec-source-in-repo.md`, `references/spec-source-notion.md`, `references/spec-source-tracker.md`, `references/triage-states-linear.md`, `references/triage-states.md`; removed: `domain.md`, `issue-tracker-github.md`, `issue-tracker-gitlab.md`, `issue-tracker-local.md`, `triage-labels.md`; changed: `SKILL.md`, `agents/openai.yaml` |
| to-questionnaire | `skills/productivity/to-questionnaire` at `49dd158` | Added: `UPSTREAM-LICENSE.txt`; removed: none; changed: `SKILL.md`, `agents/openai.yaml` |
| to-spec | `skills/engineering/to-spec` at `49dd158` | Added: `UPSTREAM-LICENSE.txt`, `assets/prd-template.md`; removed: none; changed: `SKILL.md`, `agents/openai.yaml` |
| to-tickets | `skills/engineering/to-tickets` at `49dd158` | Added: `UPSTREAM-LICENSE.txt`, `assets/issue-template.md`; removed: none; changed: `SKILL.md`, `agents/openai.yaml` |
| triage | `skills/engineering/triage` at `49dd158` | Added: `UPSTREAM-LICENSE.txt`, `references/agent-brief.md`, `references/execution-admission.md`, `references/triage-state-machine.md`; removed: `AGENT-BRIEF.md`, `OUT-OF-SCOPE.md`; changed: `SKILL.md`, `agents/openai.yaml` |
| workflow-guide | `skills/engineering/ask-matt` at `49dd158` | Added: `UPSTREAM-LICENSE.txt`; removed: `PHASE-BOUNDARIES.md`; changed: `SKILL.md`, `agents/openai.yaml` |
| workflow-retro | `skills/engineering/retro` at `49dd158` | Added: `UPSTREAM-LICENSE.txt`; removed: none; changed: `SKILL.md`, `agents/openai.yaml` |
| writing-for-agents | `skills/productivity/writing-for-agents` at `49dd158` | Added: none; removed: none; changed: none |
