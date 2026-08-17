# Organization OS Skills

Provider-neutral skills that can accompany private Organization OS
installations. This repository currently contains one skill:

- [Meeting Runner](skills/meeting-runner/SKILL.md) prepares date-specific
  pre-call briefs and turns completed meeting capture into durable decisions,
  actions, participants, owners, and due dates.

## Install

Copy or link `skills/meeting-runner` into a skill directory supported by your
agent runtime. Keep the whole folder so its `references/`, `assets/`, and
`agents/` metadata remain available.

The skill is intentionally provider-neutral. Configure its destinations in the
consuming repository, especially `.agents/workflows/meeting-records.md` and,
when applicable, `.agents/workflows/issue-tracker.md`.

## Validate

```bash
python3 scripts/check.py
python3 -m unittest discover -s tests
```

## Contributing

Keep changes provider-neutral and limited to Meeting Runner. Never contribute
deployment routes, private links or identifiers, customer material, capture
content, credentials, or another skill. Run both validation commands before
opening a pull request.

Licensed under the [Apache License 2.0](LICENSE).
