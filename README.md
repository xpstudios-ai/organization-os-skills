# Organization OS Skills

Fifteen practical workflows for your AI agent, from meeting follow-through and
customer decisions to software planning and review. Start with one useful
result, then use the other skills as you need them.

Several workflows are adapted from [Matt Pocock’s skills](https://github.com/mattpocock/skills). His MIT copyright and licence notices are retained; see [NOTICE.md](NOTICE.md).

## Choose your agent

**Codex** and **Claude Code** are suggested starting points. Other agents that
support Agent Skills may work too; installation, service connections and setup
recall depend on the client. See [compatibility details](docs/PLUGIN_DISTRIBUTION.md#current-recipient-experience).

The public [Organization OS 1.1.0 release](https://github.com/xpstudios-ai/organization-os-skills/releases/tag/organization-os-plugin-v1.1.0)
includes all fifteen skills through a custom marketplace or downloadable ZIP.
It is not yet listed in the OpenAI or Claude public directories.

## Install

**In Codex, paste this into your agent:**

> Install Organization OS from [https://github.com/xpstudios-ai/organization-os-skills](https://github.com/xpstudios-ai/organization-os-skills), using its plugin-release marketplace. Handle the installation for me, preserve my existing skills and settings, and confirm Meeting Runner and Workflow Guide are ready.

Review any permission prompts, then start a new chat. You do not need to open a
terminal or choose a business folder. If installation is unavailable in your
client, ask the agent to explain what is missing.

**In Claude Code**, use the in-chat commands under Advanced below. Codex is the
tested route for setup and Notion meetings; Claude Code installation and updates
are tested, but its full Notion flow is not yet verified.

<details>
<summary>Advanced: manual installation and updates</summary>

For **Claude Code**, enter these commands in its chat:

```text
/plugin marketplace add xpstudios-ai/organization-os-skills#plugin-release
/plugin install organization-os@xpstudios
```

Choose Install if prompted and confirm the plugin is enabled. To receive
updates automatically, enable auto-update under
`/plugin → Marketplaces → xpstudios`; custom marketplaces have it off by default.

For **Codex**, with the Codex CLI installed:

```sh
codex plugin marketplace add xpstudios-ai/organization-os-skills --ref plugin-release
```

Restart the desktop app, open Plugins, select the xpstudios **local source** and
install Organization OS. To refresh the source, run
`codex plugin marketplace upgrade xpstudios`, confirm the installed version in
the app and start a new chat. Custom-source automatic updates are not assured.

ZIP imports and copied skill folders need manual updates. Use one installation
method per skill and preserve any existing copy before replacing it. Installing
skills does not connect Notion or grant access to other services.
See [distribution and updates](docs/PLUGIN_DISTRIBUTION.md) for details.

</details>

## Connect your workspace

For business work, follow **Start Here** in your own Notion copy. Connect Notion
through your agent, then share your copy's home link and ask:

> Connect this Organization OS copy and remember it for future business work.
> Confirm the connected account and workspace, then find this copy's Source of
> Truth Map. Preserve my existing settings, keep drafts in chat and show what
> you saved.

Start a new chat and ask which workspace it is using. If the agent cannot
verify the connection or recall your setup, give it the home link again and
keep work as an unsaved draft until the destination is clear.

For software work, use your existing project and instructions. **Setup Agent
Workflows** can help configure repository workflows when you ask for it.
Without Notion, the agent can use local settings instead; see
[setup details](CONTRACT.md#business-setup-and-recall).

## Try your first meeting

Give your agent notes you have permission to use and ask:

> Use Meeting Runner to draft the decisions and actions from these notes.
> Flag missing owners or dates. Let me review the result before saving it.

Review the draft, approve where to save it, then follow through on one owned
action. If you are unsure what to do next, ask **Workflow Guide**.

## Workflow catalog

| Skill | Use it for |
| --- | --- |
| [Meeting Runner](skills/meeting-runner/SKILL.md) | Prepare meetings and turn notes into clear decisions and owned actions |
| [Workflow Guide](skills/workflow-guide/SKILL.md) | Choose the next useful skill or artifact |
| [Qualify Opportunity](skills/qualify-opportunity/SKILL.md) | Assess whether to pursue a customer enquiry or partnership |
| [To Questionnaire](skills/to-questionnaire/SKILL.md) | Draft questions to get missing information |
| [Retro](skills/workflow-retro/SKILL.md) | Improve recurring agent work using session evidence |
| [To Spec](skills/to-spec/SKILL.md) | Turn agreed context into a specification |
| [To Tickets](skills/to-tickets/SKILL.md) | Break approved work into executable issues |
| [Triage](skills/triage/SKILL.md) | Sort work and check whether it is ready to start |
| [Handoff](skills/handoff/SKILL.md) | Preserve context so work can continue after an interruption |
| [Repo Review](skills/repo-review/SKILL.md) | Review repository changes against intent and standards |
| [Repo Document](skills/repo-document/SKILL.md) | Keep repository documentation clear and current |
| [Diagnose](skills/diagnose/SKILL.md) | Investigate unclear defects through reproduction and evidence |
| [Codebase Design](skills/codebase-design/SKILL.md) | Improve module interfaces and boundaries |
| [Writing for Agents](skills/writing-for-agents/SKILL.md) | Write clear, useful agent instructions |
| [Setup Agent Workflows](skills/setup-agent-workflows/SKILL.md) | Configure repository workflows explicitly |

<details>
<summary>Advanced: editable project-local skills</summary>

From a reviewed checkout, select the skills you need. The installer copies
complete folders with their required dependencies and licence notices:

```sh
python3 scripts/check.py
python3 scripts/install.py --project /path/to/project --skill meeting-runner
python3 scripts/install.py --project /path/to/project --skill to-spec
```

Copies live in the project's `.agents/skills`. Re-run from an updated checkout
to update unchanged copies owned by this installer. It refuses to overwrite
foreign, modified or linked skills. Keep the previous checkout for rollback.

Use the same selection with `--remove` to remove an unchanged owned bundle.
Removal preserves dependencies needed by other installed skills. These commands
do not install globally or connect accounts. For workflow configuration, see
the [workflow contract](CONTRACT.md).

</details>

## Contribute

Use fictional examples and keep private records, credentials and workspace
configuration out of contributions. Before opening a pull request, run:

```sh
python3 scripts/check.py
python3 -m unittest discover -s tests
```

Maintainers: see the [release guide](docs/PLUGIN_DISTRIBUTION.md).
Licensed under [Apache-2.0](LICENSE), with third-party notices in [NOTICE.md](NOTICE.md).
