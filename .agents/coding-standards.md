# Coding Standards

## Style And Architecture

Use standard-library Python and the existing explicit validators and installer.
Keep complete resources with their owning skill. Portable source must contain
no private workspace, account, customer or deployment facts.

## Testing And Commands

Run `python3 scripts/check.py`, `python3 -m unittest discover -s tests` and
`git diff --check`. Test selected and multiple bundles in temporary projects,
dependency closure, malformed-source rejection, unchanged-owner updates,
rollback, and refusal of foreign, modified or linked destinations.

## Security And Gotchas

Validation checks metadata, resources, digests, links and sensitive content.
Never weaken installer ownership or reseal during validation. Shared upstream
UI descriptions may be shorter than new-authoring guidance; preserve pinned
bytes and require nonempty bounded descriptions. New UI descriptions follow
the 25–64-character guidance.

## Pre-Completion

Verify complete pinned shared directories and the intentional Meeting Runner
variant. Inspect qualification scenarios and private-content exclusions;
local structural checks do not prove live connector acceptance.
