# Triage State Machine

These are role names. The actual tracker value may be a markdown field, native
status, label, property, or another repo-defined mapping.

## Categories

- `bug`
- `enhancement`
- `program-work`
- `governance`
- `evaluation`
- `documentation`

## Core States

- `needs-triage`: maintainer needs to evaluate the record.
- `needs-info`: waiting for specific input.
- `ready-for-agent`: fully specified and safe for an agent to handle through
  completion or, when applicable, a named stop condition.
- `ready-for-human`: no safe agent-executable work remains before the next
  human judgment, external access, approval, or manual-validation step.

## Terminal States

- `wontfix`: deliberately not actioned.
- `completed`: work is done and verified.
- `archived`: historical record retained for reference.

## Rules

- Each active issue should have one category and one state.
- Do not move a bug to `ready-for-agent` without reproduction evidence or a
  clear reason reproduction is impossible.
- `needs-info` questions must be specific and answerable.
- `ready-for-agent` records need acceptance criteria, verification, risks, and
  non-goals.
- Classify the next required action, not a later consequential action. A future
  human gate does not make fully specified preparation human-only.
- If a later human gate exists, a `ready-for-agent` record must name the exact
  stop condition, prohibited actions, and evidence that triggers re-triage.
- Use `ready-for-human` when the human decision is needed to define the current
  scope or when no safe agent-executable work remains.
- Readiness classifies the next work tranche; it does not authorize execution.
  The repository route and current user authority still govern every mutation.
- At a stop condition, re-triage from the recorded evidence. Move to
  `ready-for-human` only when the next action is human-only; otherwise use the
  matching active or terminal state.
- A terminal item has no core active workflow label or readiness marker. Clear
  and read back those markers before considering the transition complete.
- Use terminal states only when the repo or tracker maps them.
