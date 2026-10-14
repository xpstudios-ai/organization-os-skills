# Organization OS Skills

Provider-neutral workflows for connected operating records and authorized agent
work. **Organization OS 1.1.0 includes fifteen skills.** The Notion template and
these skills have separate ownership and release processes.

Several workflows are adapted from [Matt Pocock’s skills](https://github.com/mattpocock/skills). His MIT copyright and licence notices are retained; see [NOTICE.md](NOTICE.md).

For repository design and agent-instruction authoring, preserve the existing
`.agents/*-standards.md` overlays and legacy `CONTEXT.md` routes. Read
[repository context](skills/handoff/references/repository-context.md) before
using the unchanged upstream reference folders. Explicit Setup Agent Workflows
merges a startup pointer into existing instructions; installation alone does
not rewrite them.

## Choose your agent

**Codex** and **Claude Code** are suggested starting points. Other Agent Skills
clients may also load the complete skill folders; check their installation,
Notion access and setup recall. Plugin marketplaces are client-specific.

Connect your Notion copy and ask the agent
to remember it in your personal settings. Business setup requires no folder
selection, Git knowledge or configuration-file editing. For software work, keep
the existing project and its instructions.

**[Install Organization OS 1.1.0](https://github.com/xpstudios-ai/organization-os-skills/releases/tag/organization-os-plugin-v1.1.0)**
from the public release marketplace or its complete ZIP. Public app-directory
listings, ChatGPT web and Claude web routes remain pending acceptance.
Version 1.0.0 remains available as the earlier Meeting Runner-only starter.

**In Codex, ask the agent to install it for you:**

> Install Organization OS from [https://github.com/xpstudios-ai/organization-os-skills](https://github.com/xpstudios-ai/organization-os-skills), using its plugin-release marketplace. Handle the installation for me, preserve my existing skills and settings, and confirm Meeting Runner and Workflow Guide are ready.

On the tested macOS Codex client, the agent registers the marketplace and installs
the plugin using the installed host tools. You do not open a terminal or choose a
business folder. Approve the app's normal permission prompts if shown. Start a
new chat afterward; reopen the app only if the skills do not appear. Managed
restrictions or a client without the supported installer can still prevent setup;
the agent must report that limitation rather than silently copy skills elsewhere.

**Claude Code alternative:** use the in-chat `/plugin` commands under Advanced.
Native installation and updates passed; the full setup and meeting flow remains
unverified. Use Codex for the verified route. Windows and web-client
acceptance are also separate. Use one installation method per skill; preserve
and identify any existing copy before changing it.

Follow Start Here in your own Notion copy to connect services separately. Give
the agent that copy's home link and ask:

> Connect this Organization OS copy and remember it for future business work.
> Confirm the connected account and workspace. Find Source of Truth Map through
> this home and verify it belongs to this copy. Preserve my existing settings.
> Keep drafts in chat and show what you saved.

The agent manages a short personal startup preference, outside the replaceable
plugin. Start a new chat and ask which copy and map it is using, without giving
the links again. Have it check the live Notion account and workspace with the
current-account tool; a saved label or workspace member list is insufficient.
If recall or access fails, provide the home link for that chat;
keep drafts unsaved until the destination is verified. Changing computers or
clients requires a new setup check. See the [business setup and recall contract](CONTRACT.md#business-setup-and-recall).
Qualification and repository scaffolding are not setup prerequisites. The map
owns destinations, formats, responsible people and review; credentials stay in
the connected app. Local settings can supply the same facts without Notion.

Approved releases reach users through their chosen installation channel. Custom
Claude Code marketplaces need auto-update enabled; Codex custom sources and ZIP
or folder copies must be checked and refreshed through their supported route.
See the [distribution and update contract](docs/PLUGIN_DISTRIBUTION.md).

<details>
<summary>Advanced: released plugin installation and updates</summary>

For **Claude Code**, enter these commands in its chat:

```text
/plugin marketplace add xpstudios-ai/organization-os-skills#plugin-release
/plugin install organization-os@xpstudios
```

Choose Install in the plugin panel if prompted, then verify it is enabled.

Enable auto-update under `/plugin → Marketplaces → xpstudios` if desired;
custom marketplaces have it off by default.

For **Codex**, with the Codex CLI installed, run:

```sh
codex plugin marketplace add xpstudios-ai/organization-os-skills --ref plugin-release
```

Restart the desktop app, open Plugins, select the xpstudios **local source** and
install Organization OS. This route is separate from the pending public
app-directory listing. To refresh the tracked source, use
`codex plugin marketplace upgrade xpstudios`, then confirm the installed version
in the app and start a new session. Do not assume custom-source automatic updates.
If the client does not expose the local source, use the complete-folder route or
a technical helper; do not substitute a pending public listing.

Released ZIP imports and copied folders need manual updates. A GitHub push does
not update an OpenAI directory package; the publisher submits the new ZIP through
its separate release process. Installation does not connect Notion or migrate
recipient records.

</details>

## Workflow catalog

| Skill | Use it for |
| --- | --- |
| [Meeting Runner](skills/meeting-runner/SKILL.md) | Prepare a meeting or turn completed capture into accountable outcomes |
| [Workflow Guide](skills/workflow-guide/SKILL.md) | Choose the next available workflow or useful artifact |
| [Qualify Opportunity](skills/qualify-opportunity/SKILL.md) | Assess a customer job or commercial partnership from evidence and next gates |
| [To Questionnaire](skills/to-questionnaire/SKILL.md) | Draft questions for missing customer or colleague information |
| [Retro](skills/workflow-retro/SKILL.md) | Improve repeated agent work from actual session evidence |
| [To Spec](skills/to-spec/SKILL.md) | Turn approved context into a decision-ready specification |
| [To Tickets](skills/to-tickets/SKILL.md) | Slice approved work into executable issues |
| [Triage](skills/triage/SKILL.md) | Classify work and verify readiness through the configured tracker |
| [Handoff](skills/handoff/SKILL.md) | Preserve continuation context across an interruption or transfer |
| [Repo Review](skills/repo-review/SKILL.md) | Review a stable candidate against intent and repository standards |
| [Repo Document](skills/repo-document/SKILL.md) | Reconcile reader-focused documentation with its owning sources |
| [Diagnose](skills/diagnose/SKILL.md) | Investigate unclear defects with reproduction and evidence |
| [Codebase Design](skills/codebase-design/SKILL.md) | Improve module interfaces and meaningful boundaries |
| [Writing for Agents](skills/writing-for-agents/SKILL.md) | Author predictable instructions; supports To Spec |
| [Setup Agent Workflows](skills/setup-agent-workflows/SKILL.md) | Explicitly configure repository routes; business setup follows the workspace map |

## Start with meeting follow-through

For a team adding agents to its operations, start with Meeting Runner in the
agent it already uses. Turn permitted notes from one completed meeting into
reviewed decisions and owned next actions. Return a draft when no destination
is configured; a connector or automated task system is not required for first
value. Confirm the result and follow one action through the existing workflow.

The fifteen skills are optional by workflow. Add Qualify Opportunity
when a concrete enquiry needs a proceed, pause or decline decision. Its
[shared core](skills/qualify-opportunity/references/qualification-core.md) keeps
the detailed assessment in one child page under the Engagement; its
[Engagement shape](skills/qualify-opportunity/references/engagement-shape.md)
puts Records first, followed by a short Overview and Updates. Workspace
holds reusable knowledge. Add To Spec / To Tickets / Triage
when approved work needs specification and delivery tracking; add repository
and diagnosis workflows when engineering needs them. Install only the selected
workflow and its required resources/dependencies. No agent runtime is bundled.

<details>
<summary>Advanced: project-local editable installation</summary>

From a reviewed checkout, select one or more workflows. The installer copies
complete folders and resolves mandatory dependencies:

```sh
python3 scripts/check.py
python3 scripts/install.py --project /path/to/project --skill meeting-runner
python3 scripts/install.py --project /path/to/project --skill to-spec
python3 scripts/install.py --project /path/to/project --skill to-tickets --skill diagnose
python3 scripts/install.py --project /path/to/project --skill qualify-opportunity
```

Copies live in the project's `.agents/skills`; an adjacent ownership receipt
records their resource digests. An owned adjacent notice preserves the package
license and attribution. The installer refuses foreign, modified or linked
skills and notice files before changing any selected skill. Re-running against a
new reviewed checkout updates only unchanged, receipt-owned copies. Keep the
previous reviewed checkout for rollback, and run that checkout's installer to
restore its package bytes. A changed local copy must be reconciled manually.

Remove an unchanged owned bundle with the same selection and `--remove`.
Removal refuses to break another receipt-owned dependency. These commands do
not install into a global skill directory or configure account access.

The pinned skills CLI was evaluated for project-local copy installation, but
its selection does not guarantee dependency or foreign-install protection.
Use the validated installer for editable copies. These editable copies are an
advanced alternative to the managed public plugin. Choose one installation
method for a given skill; preserve and reconcile any existing local copy first.

</details>

## Maintain plugin releases

Maintainers build the cleared 1.1.0 suite with `scripts/build_plugin.py`. Its single
versioned manifest produces portable, Codex and Claude metadata, a complete
fifteen-skill payload, marketplace catalogs and an immutable ZIP
digest. The builder excludes pending catalog entries and writes only to a new
external output directory. Follow the [release runbook](docs/PLUGIN_DISTRIBUTION.md)
for native validation, update acceptance, publication and rollback.

## Configure and use

Read [the workflow contract](CONTRACT.md), then configure the consuming
workspace's meeting, specification, tracker and documentation routes. Invoke a
skill in an agent that supports the skill format. Small approved work need not
pass through every workflow. Instructions guide existing authorized agents;
installation does not grant new permissions or provide an autonomous manager.

## Validate and contribute

```sh
python3 scripts/check.py
python3 -m unittest discover -s tests
```

Keep resources, dependency declarations, metadata and catalog digests aligned.
Use synthetic fixtures; do not contribute organizational routes, capture content,
private links, identifiers or credentials. See [notices](NOTICE.md) and the
[Apache-2.0 license](LICENSE); publication clearance remains a separate gate.
