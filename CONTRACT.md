# Portable workflow contract

The library routes work to the consuming workspace's sources and permissions.
It grants no account access, deployment authority or permission to send messages.
Read the workspace's instructions before execution. Configure only the routes a
workflow needs; a missing route returns a draft or recommendation, not a guessed
integration.

| Workflow | Successful result | Missing authority or uncertain result |
| --- | --- | --- |
| Meeting Runner | Private capture becomes stakeholder-safe outcomes, decisions and accountable actions in one synthesis table | Keep capture private; preserve an existing meeting; reconcile an ambiguous write before retry |
| Workflow Guide | One next useful skill or artifact grounded in available capabilities | Guidance alone does not start execution or install a skill |
| To Questionnaire | Answerable questions for the information that changes a decision | Draft or authorized save only; no implied delivery to the recipient |
| Retro | Ranked improvements grounded in actual session results and failures | Proposals do not edit skills, standards or memory automatically |
| To Spec | One decision-ready specification from approved context | Return a complete draft when the destination or publication route is unavailable |
| To Tickets / Triage | Vertical slices, complete briefs and verified native readiness | Never mark a parent plan or blocked work agent-ready; claims depend on the configured adapter |
| Handoff | Traceable continuation with unfinished work and next action | No implied permission to spawn, transfer or message an agent |
| Repo Review | Direct originating-task assessment against intent and repository standards | Report an independent-review requirement unmet when the repository requires it |
| Repo Document | Reader-focused documentation aligned with its owning sources | Keep operational receipts in evidence logs; external updates require destination authority |
| Diagnose | Reproduction, evidence, bounded correction and verified behavior | Missing reliable signal or access returns an evidence-bounded diagnosis |
| Codebase Design | A smaller useful interface and justified adapters | Repository architecture constraints remain authoritative |
| Writing for Agents | Discriminating invocation, explicit outcomes and authority, checkable completion | Instruction editing does not authorize the instructed side effects |
| Setup Agent Workflows | Explicit repository-local route and standards setup, with local-first persistence where authorized | Installation alone never invokes setup or selects external accounts |
| Qualify Opportunity | One supported recommendation, unanswered questions, information needed and next steps | Return an unsaved assessment when no write route is authorized; never invent numeric scores or customer acceptance |

## First useful workflow

Recipients install the public Organization OS plugin through their app. The
1.1.0 release contains the selected fifteen-skill suite; the earlier 1.0.0
starter contains Meeting Runner only. App-managed releases replace package
files, while consuming-workspace configuration stays separate. Skill updates
do not authorize account connections, new permissions or background work.

Meeting Runner is the recommended operations starter. Given permitted notes
from one completed meeting, return the shared three-column synthesis and flag
unknown owners/dates. Review and follow at least one concrete action before
expanding setup. A missing destination yields a draft; it does not justify a
guessed connector, task publication or message delivery. The existing public
Meeting Runner package and its outcome contract remain unchanged.

The wider package set is optional by workflow, with mandatory dependency closure
for selected skills. Specification and engineering workflows follow an actual
need; neither all fifteen skills nor a full toolchain is a prerequisite for use.

## Dependency bundles

`catalog.json` owns package resources, byte digests, provenance and dependencies.
To Spec includes Writing for Agents, Codebase Design and Handoff. To Tickets
includes Triage and Handoff; Diagnose includes Codebase Design and Handoff. Workflow Guide,
To Questionnaire and Retro include Handoff for its supporting persistence
reference. Codebase Design and Writing for Agents include Handoff for repository-context
and domain-discovery references. Handoff itself needs no repository setup. Qualify Opportunity owns
its business discovery resource and has no mandatory skill dependency.
Setup Agent Workflows remains an explicit repository workflow and includes
Handoff's persistence resource. Reading a supporting resource invokes neither
Handoff nor setup. Optional continuations require an available, authorized
workflow; otherwise return the artifact and remaining verification as a handoff.

## Repository Reference Context

For repository design or instruction authoring, read
[repository context](skills/handoff/references/repository-context.md) before
using Codebase Design or Writing for Agents, including their direct references.
Read AGENTS.md, relevant existing .agents/*-standards.md, configured domain docs
and ADRs. Preserve the coding-only .claude/coding-standards.md fallback and
legacy CONTEXT.md / CONTEXT-MAP.md routes. Local instructions govern generic
GLOSSARY.md examples, delegation and test-replacement guidance.

Explicit Setup Agent Workflows carefully merges a startup pointer into existing
AGENTS.md. Ordinary installers preserve user instructions; installing dependency
resources alone is not proof that a fresh runtime reads the pointer. Verify it
in a new session. This preflight invokes no Handoff or setup workflow and grants
no new write or delegation authority. Non-repository work uses supplied context
without creating repository scaffolding.

## Business Setup And Recall

Business users install the plugin, connect Notion and provide their template-home
link. Setup manages storage; never ask them to select a local working folder or
edit configuration files. Repository users retain their existing project,
standards and adapters. An app's required workspace or file-access dialog is a
host permission step, not a new Organization OS folder-creation task.

On an explicit request to remember setup:

1. Verify the connected account and workspace. Follow the supplied home's
   native links to Source of Truth Map and verify both belong to the intended
   copy. Search results and familiar titles alone are insufficient.
2. Inspect the client's effective personal instructions before editing. Merge a
   short, clearly labeled Organization OS section; preserve all other content.
   Use Codex's effective personal AGENTS.override.md or AGENTS.md in its Codex
   home, or Claude Code's personal CLAUDE.md. Respect managed policy, overrides
   and existing settings. Use the client's configured location; do not guess a
   Windows AppData path or write into the plugin installation.
3. Save only the business label, verified home/map links and a narrow trigger:
   use these for Organization OS business work when no explicit project route
   applies. Existing repository adapters and a destination specified for the
   current task take precedence. If multiple saved businesses fit, ask which
   business; do not silently replace the selection or choose a folder.
4. Read the saved section back. Start a fresh chat in another ordinary app
   context, without resupplying the links, and verify that it recalls the copy
   and opens the current map with the intended account. Report saved preference,
   model recall and live service access as separate checks. If saving is denied
   or recall fails, use the home link for this chat and keep writes pending.

The map owns destinations, required formats, people and review. A startup
preference grants neither service access nor per-write consent. Recheck current
identity and destination before an authorized save and read back its result.
Wrong-account, inaccessible or ambiguous routes produce an unsaved draft.
Drafts stay in chat; create local files only when requested and ask for their
location only when it matters. Credentials stay host-managed.

Without Notion, the agent can save a small settings document in the client's
personal configuration area and point the same startup section to it. Keep one
settings owner. Personal setup is local to that client/profile; do not promise
cross-client or cross-device synchronization. Plugin updates must preserve it.
On a request to forget or change setup, edit only the managed section and its
owned settings after reading them; preserve unrelated instructions and files.

Setup is independent of qualification. Reading this guide invokes neither
Qualify Opportunity, Handoff nor repository-only Setup Agent Workflows. The
packaged guide supports a first Meeting Runner setup without an extra skill.

## Opportunity And Engagement

Use [the qualification core](skills/qualify-opportunity/references/qualification-core.md)
for a concrete customer job, project or commercial partnership. When useful, the existing questions
register has six fields: Question, What we know, Information needed, Who will
check, Why it matters, Notes. Detailed assessment belongs in one child page
under the Engagement. Workspace holds reusable guides, policies, processes and
reference material. Technical, buying and commercial
sections appear only when relevant. A company-only lead or noncommercial
relationship does not require an assessment.

The [Engagement shape](skills/qualify-opportunity/references/engagement-shape.md)
owns the reusable Records / Overview / Updates contract, with child pages
at the top under Records. It avoids copying
properties or assessment detail. It is a resource used only for authorized
parent edits; no separate engagement skill is included in this package.
The default assessment briefly considers four configurable areas: customer
need, expected value, ability to deliver, and buying decision/timing. A per-run
subset or skip is allowed; excluded areas are unassessed. An approved save may
update matching Qualification Verdict and Assessment Date after identity and
mapping verification. Evidence State and Pursue stay unchanged unless explicitly
instructed; skipping assessment leaves all qualification fields unchanged.

Meeting Runner retains the public three-column outcome contract and ordinary
manual meetings remain supported. Neither qualification nor engagement setup
is needed for the first meeting follow-through result.

## Configuration example

A consuming workspace might route meeting records to its permitted knowledge
system, specifications to its product documents, issues to its chosen tracker,
and source review to Git. Define the destination, record identity, permitted
writes, readback, and failure/retry behavior in that workspace. Use synthetic
records to test the route before any real publication or delivery.

## Distribution status

Version 1.1.0 delivers the selected fifteen-skill suite through the public Git
marketplace and release ZIP. Meeting Runner preserves its three-column outcome
contract. Public app directories and web-client routes remain pending. Validate
selected packages and dependencies before installation; local checks do not prove
live connector access or authenticated Claude Code inference.
