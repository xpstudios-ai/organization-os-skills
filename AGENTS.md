# AGENTS.md

## Purpose

This repository is the portable source for skills that may accompany private
Organization OS installations. The skills must remain useful across many
organizations, providers, and work-management systems.

## Boundaries

- Keep exactly one distributed skill: `skills/meeting-runner`.
- Do not add client or source-organization data, personal email addresses,
  workspace or database identifiers, credentials, recordings, transcripts,
  private URLs, or machine-local paths.
- Keep provider, workspace, tracker, CRM, and destination choices in the
  consuming repository's route files. Never encode a specific deployment here.
- A skill's `SKILL.md` frontmatter contains only `name` and `description`.
- Keep reusable instructions in `SKILL.md`, detailed guidance in `references/`,
  and output templates in `assets/`. Do not add documentation inside the skill.
- The repository stays private until an explicit publication review passes.
  Do not change visibility or create a release tag without approval.

## Commands

```bash
python3 scripts/check.py
python3 -m unittest discover -s tests
git diff --check
```

## Publication gate

Before public visibility or a release tag, require a passing local check, a
passing CI run, an independent fresh-context review, a secret scan, and a
confirmation that the repository contains no deployment-specific material.
