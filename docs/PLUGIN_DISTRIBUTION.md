# Public Plugin Distribution

Organization OS currently targets local Codex and Claude Code. Business users
connect their workspace and let the agent manage personal setup; no working-folder
selection is required. Repository users retain their existing project. In the
tested macOS Codex client, a plain-language installation request lets the agent
register the public Git marketplace and install through the existing host CLI;
the user does not open a terminal. Claude Code uses its marketplace and in-chat
`/plugin` commands. Terminal details and editable folder alternatives are under Advanced
in the README. Public directory and ChatGPT/Claude web routes remain pending.
The 1.1.0 release contains the selected fifteen generic workflows.
The earlier 1.0.0 release remains the immutable Meeting Runner-only starter. Adding a
workflow requires its complete dependency bundle and publication clearance.

## Current Release

[Organization OS 1.1.0](https://github.com/xpstudios-ai/organization-os-skills/releases/tag/organization-os-plugin-v1.1.0)
is published on `plugin-release`; the plugin folder is
`plugins/organization-os`. Its immutable tag is
`organization-os-plugin-v1.1.0`. The ZIP and `RELEASE.json` are release assets.
The earlier 1.0.0 tag and assets stay unchanged.
OpenAI and Claude directory listings remain pending. A public Git release is
available for custom marketplace consumers and manual ZIP imports; it is not a
direct install link for either public app directory.

## One Source, Reviewed Releases

`skills/` owns skill instructions and resources. `catalog.json` owns their exact
digests, dependencies and provenance. `distribution/plugin.json` owns the public
plugin identity and semantic version. `distribution/release.json` selects the
cleared workflows and records public-channel status. Provider manifests,
marketplace trees and ZIPs are derived outputs, never alternate skill sources.

Build into a new directory outside this source checkout:

```sh
python3 scripts/check.py
python3 -m unittest discover -s tests
python3 scripts/build_plugin.py --output /path/to/new/release-candidate --previous-release tests/fixtures/plugin-1.0.0.json
claude plugin validate --strict /path/to/new/release-candidate/marketplace
claude plugin validate --strict /path/to/new/release-candidate/marketplace/plugins/organization-os
```

The output contains a portable plugin ZIP, OpenAI and Claude compatibility
manifests, both marketplace catalogs, and a digest receipt. The ZIP contains the
selected complete skill folders, NOTICE and required licenses. It contains no account
configuration, MCP servers, hooks, credentials or autonomous update scripts.
Build twice and compare bytes. The builder refuses existing outputs, linked
paths, altered source resources and bundles with pending reuse clearance.
For every release after 1.0.0, pass `--previous-release` with the previous
approved `RELEASE.json`. The builder rejects a changed archive at the same
version or a lower version, and refuses a later release without that receipt.

## Current Recipient Experience

1. Use Codex or Claude Code. Preserve existing instructions and avoid duplicate
   same-name skill installations. No business working-folder choice is needed.
2. In Codex, paste the README's installation request and let the agent register
   the released `plugin-release` marketplace and install Organization OS. Approve
   normal host permission prompts. A restricted or unsupported client must
   report the missing capability. Manual commands are an Advanced alternative;
   they are not required user actions in the tested flow. Claude Code's in-chat
   `/plugin` route remains available with its authenticated-use limit below.
   Version 1.1.0 installs all fifteen skills. Confirm the version after updating.
3. Start a fresh session and confirm Meeting Runner with its supporting files.
4. Connect Notion separately, verify account/workspace, and discover the intended
   copy's Source of Truth Map through its home links. On a request to remember
   setup, merge a narrow personal startup preference. Verify recall in a new
   chat without giving the links again; use a per-chat link if recall fails.
   Local personal settings can supply the same routing contract without Notion.
5. Draft one meeting, approve its save and read back the saved record.

Native macOS Codex acceptance covers a plain-language public marketplace install,
preserved personal instructions, fresh-process recall from an ordinary directory
outside Git, and live account/home/map/Meetings verification. Meeting Runner
produced a draft without writes, then saved the approved fictional meeting through
the native Meeting template and fetched the completed table back. A correction
updated the same record, preserved a human note and left one matching meeting.
Normal host write approvals still apply. If a save is interrupted or denied,
inspect the existing page before retrying so a partial record is completed
without creating a duplicate.

These tests used an existing authenticated native Notion connection and fictional
records in the editable publisher template. They do not establish a new user's
OAuth sign-in or a human recipient walkthrough. Claude Code inference remains
unverified because the installed test client is signed out; native Windows and
web-client use remain unverified. Keep settings and files outside plugin resources.
See the business setup contract for the native personal-instruction route and
safe per-chat fallback; neither lifecycle hooks nor a custom settings service
is introduced. The skills-only package does not claim web-client persistence.

Public app-directory listings are a future route. Publish direct install links
only after approval, anonymous visibility and the actual recipient flow pass.
A local Git marketplace, ZIP import or source check does not establish that
route or its update behavior. Recipients should never edit a plugin cache.

## Delivery And Updates By Channel

| Channel | How approved changes reach users | Publisher work |
| --- | --- | --- |
| OpenAI public directory | The app manages the installed directory package. Do not promise a universal refresh interval. | Upload a new ZIP for changed skills or metadata; complete checks and the applicable review/publication flow. A GitHub push alone does not update directory skills. |
| Claude public discovery | The directory follows the submitted branch and plugin folder, scans each new commit and serves a published passing version. Auto-publish depends on Anthropic's approval and the listing's setting. | Submit `plugins/organization-os` on `plugin-release` through the developer portal. Raise the plugin version for changed bytes. A custom ZIP upload is not a substitute for a managed listing. |
| Codex configured local marketplace | Refresh the configured source with the supported marketplace upgrade command and verify the installed app version. Automatic update behavior is not assumed. | Advance only the approved release tree; test the actual client and fresh-session discovery separately from public-directory submission. |
| Public Git marketplace in Claude Code | Users enable auto-update in the marketplace's plugin-manager settings. Custom marketplaces have it off by default; a publisher cannot turn it on in marketplace.json. | Advance the reviewed release tree and bump the plugin manifest version for every changed package. |
| Organization-managed marketplace | The administrator's sync and approval policy controls delivery. This is a separate setup path with its own repository restrictions. | Review and sync approved versions. Do not present it as universal public onboarding. |
| Standalone ZIP or editable folders | Manual replacement or update. | Retain complete archives and explicit version notes; no automatic-update promise. |

Skill authoring, publisher releases, app delivery and account authorization are
separate operations. Use the host's built-in update mechanism. Do not add a hook,
cron task or background downloader to fetch instructions outside that channel.
Workspace routes and team preferences stay outside the managed plugin so an
update can replace package files without erasing configuration.

## Release And Recovery

1. Review the exact source delta, full resource/dependency digests, provenance
   and privacy boundary. Only explicitly cleared packages may enter the plugin.
2. Bump the single canonical plugin version for every shipped byte change.
   Patch versions fix compatible behavior; minor versions add compatible
   capabilities; major versions communicate breaking contracts and migration.
3. Require passing source checks, deterministic builds, provider validation and
   native install/use/update acceptance. Test a recipient with no private Git
   access. Bind the receipt to the reviewed source commit and archive hash.
4. After explicit publication approval, tag the immutable reviewed package as
   `organization-os-plugin-v<version>`. A Git marketplace release tree uses the
   `plugin-release` branch. Advance that branch only for a reviewed release;
   keep unrelated or uncleared source out of its payload.
5. Submit the ZIP to the intended public directory under the verified
   xpstudios publisher. A public Git marketplace does not imply directory
   approval or visibility. Complete any required publisher verification.
6. Once live, read back the listing, test install and updates, then replace
   pending channel state and Notion copy with the verified install links.
7. Keep each immutable archive and receipt. To recover from a bad update, use
   the previous known-good payload in a new, higher patch version and publish
   it through the same channel. Do not silently rewrite a released version or
   assume clients will accept a version downgrade. Give migration instructions
   when the old behavior cannot safely consume new state.

No source check or build publishes, installs, grants access, or certifies native
automatic updates. Public directory approval and real client acceptance remain
observable release gates.

## Official References

- [Codex personal instruction discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md#how-codex-discovers-guidance)
- [Claude Code personal instructions](https://code.claude.com/docs/en/memory)
- [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins)
- [OpenAI submission and skill updates](https://developers.openai.com/plugins/deploy/submission)
- [Claude plugin installation](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)
- [Claude directory submission and managed updates](https://claude.com/docs/plugins/submit)
- [Claude marketplace updates and versions](https://code.claude.com/docs/en/plugins/host-marketplace#keep-users-up-to-date)
