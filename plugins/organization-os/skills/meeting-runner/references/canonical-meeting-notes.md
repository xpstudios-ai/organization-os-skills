# Canonical Meeting Notes Format

Use this compact format for post-meeting records. A destination may change the
surrounding headings or prose, but it must preserve the single-table synthesis
contract below. Never use this format for preparation.

## Date

`YYYY-MM-DD`

## Participants

Use a checklist:

```markdown
- [ ] Name
- [ ] Name
- [ ] Name
```

Use the participant checklist for attendance or review. Put action ownership
in the single synthesis table. When the destination has separate
internal-person and external-contact relation fields, resolve each participant:
internal workspace participants use the internal-person field, while confirmed
external participants use their canonical external person records. Reuse those
same external person records for configured CRM activity follow-through.

## Outcomes, Decisions, And Actions

The single-table synthesis contract requires exactly one table with these three
columns, in this order:

| Topic | Outcome / Decision | Actions |
| --- | --- | --- |
| Topic name | Decision, outcome, or current status. | **Owner — `YYYY-MM-DD` or `TBC`:** Concrete next action. Link the canonical tracker, or write `Not tracked`. |

When a tracked work item exists, link it and keep priority and mutable status
canonical in the configured execution tracker. The meeting record preserves
the commitment made at the meeting, not a second live status copy.

### Row Rules

- Use one row per meaningful topic. Merge repeated discussion into its resulting
  decision or unresolved state.
- Put every accountable next step, owner, due date, and tracker link in that
  topic's final `Actions` cell. Separate multiple actions with `<br>` when the
  destination supports it.
- Promote still-open items from prior meetings into the relevant topic's
  `Actions` cell only when they remain active. Mark intentionally inactive work
  as `Deferred/Parked` in the same cell.
- Write `None` when a topic has no action. Never add an actions row, a separate
  actions table, or a fourth tracker column.
- Avoid "discussed" as the only outcome. State what changed or what remains
  blocked.
- Avoid ownerless or dateless actions. Use `Owner TBC` or `TBC` when the action
  is real but the meeting did not resolve accountability or timing.
- Do not include prep, agendas, scripts, attendee research, question lists,
  objection handling, the full qualification master table, or copied
  qualification evidence.

## Related Info

Use a short bullet list of stakeholder-safe links only.

Allowed examples:

- Current destination-space pages.
- Public or approved stakeholder documents.
- Configured tracker records.
- Official file-storage links.

Do not include private capture-source links unless the user explicitly asks and
the destination audience is allowed to see them.
