# Agent Brief

Use this reference when triage prepares an issue for `ready-for-agent` or
`ready-for-human`.

An agent brief is the execution contract attached to the issue. It must survive
handoff to another human or agent without relying on chat history.

## Principles

- Write behavioral acceptance criteria, not implementation chores.
- Keep acceptance criteria as plain bullets; completion belongs in tracker
  state and closing comments, not checked boxes in the issue body.
- Include the source PRD, documentation record, tracker parent, or local plan path.
- State priority, project/parent relationship, required labels or metadata, and blockers.
- Separate human judgment from agent-executable work.
- When a later human gate exists, name the exact stop condition, actions the
  agent must not take, and the evidence required before changing state.
- A superseding brief must identify the consumed prior boundary and define only
  the remaining executable tranche so a later worker cannot replay completed work.
- Keep sensitive evidence behind links when the target system already stores it.

## Template

```markdown
## Agent Brief

### Context

What problem this solves, who needs it, and which source artifact defines it.

### Current Tranche

- Supersedes: prior brief or tracker record, or none.
- Starts after: consumed boundary, or initial state.
- Agent-executable work now:
- Already complete; do not replay:

### Scope

- In scope:
- Out of scope:

### Acceptance Criteria

- Observable outcome.
- Edge case or non-goal that prevents overbuild.
- Required review or stakeholder sign-off, if any.

### Verification

- Command, review step, adapter read-back, or manual evidence.

### Stop Condition (when applicable)

Omit this section when the work can safely proceed through completion.

- Stop before: exact human-only decision, access, approval, mutation, or manual validation.
- Prohibited actions: actions the agent must not take implicitly.
- Transition evidence: evidence to record before re-triage; move to
  `ready-for-human` only when the next action is human-only.

### Risks And Dependencies

- Priority:
- Project/parent relationship:
- Required labels or metadata:
- Blocked by:
- Tracker-mutation authority: approval source and exact allowed state, label,
  comment, or record mutations; ordinary approval of the work is insufficient.
- Admission protocol: configured holding value, execution claim, Agent Brief
  persistence location, and read-back mechanism.
```
