# Spec Source: In-Repo Markdown

Use this starting point when PRDs, project notes, decisions, and implementation
plans live in version-controlled repo files, including a local `PRD.md`.

## Source Of Truth

- PRDs and plans live under the repo's documented work-item or docs path. Common
  shapes include root `PRD.md`, `.agents/work-items/<slug>/PRD.md`,
  `.agents/work-items/active/<slug>/PRD.md`, or `docs/prd/<slug>.md`.
- Implementation issues may also live in repo markdown, or may be published to a
  separate tracker selected in `.agents/workflows/issue-tracker.md`.
- External tracker records should link back to the repo markdown source when
  both exist.

## Publishing Rules

- Do not create work-item files unless the repo standards allow local markdown
  records or the user explicitly asks to publish.
- Use relative repo paths in local docs.
- Keep acceptance criteria as plain bullets. Completion belongs in tracker
  state and comments, not task-list checkboxes.

## When a skill says "publish a PRD"

Create or update the configured markdown PRD path, then report the path. If the
repo has no established work-item hierarchy, prefer a local `PRD.md` for a
single active effort and `.agents/work-items/active/<slug>/PRD.md` when multiple
parallel workstreams need separate records.
