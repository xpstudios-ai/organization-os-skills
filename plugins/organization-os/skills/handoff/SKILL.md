---
name: handoff
description: Prepare continuation context for a reset, interruption or authorized transfer.
disable-model-invocation: false
metadata:
  invocation: auto
---

# Handoff

Create a concise continuity package so work can continue without rereading the
conversation. This is not a generic project-summary workflow.

## 1. Gather Traceable State

Collect only what continuation needs:

- approved decisions, constraints, non-goals, and stop conditions;
- plans, issues, PRDs, docs, commits, diffs, branches, and revisions;
- dirty or staged files, pending mutations, and publication state;
- verification already run, exact failures/skips, and residual risks;
- open questions and the immediate next action.

Reference existing artifacts by stable path, URL, or identifier instead of
copying them. Use an absolute local checkout path only when same-host worktree
identity matters.

Completion criterion: every important fact is traceable to an artifact or the
current verified working state.

## 2. Separate Facts From Uncertainty

State verified facts directly. Put assumptions, missing evidence, and unresolved
choices under Open Questions. Remove internal reasoning, false starts, filler,
secrets, PII, sensitive artifact contents, and stakeholder-irrelevant local
paths.

Completion criterion: a receiver cannot mistake uncertainty for a decision or
private working context for publishable content.

Update the authorised canonical task/spec at a meaningful checkpoint before
returning the continuation package. Follow
[persistence](references/persistence.md); when no
durable route exists, return chat context and state that it has not been saved.

## 3. Preserve Delegation Return Paths

When work was delegated, name the originating task, delegated scope, expected
return artifact, integration owner, verification still required, and how the
origin closes the loop. Suggested Skills may be included when they materially
help the receiver.

Prepare the content when a continuation boundary is approaching. Use an
existing harness handoff or compaction facility when it already carries this
state; add only missing decisions, evidence, or return instructions.

Return content in chat by default. Creating agents or chats, sending messages,
saving files, and publishing require authority under the active task and harness
rules. This skill grants none of those permissions and does not require renewed
permission for a transfer already authorized.

Completion criterion: delegated work has an explicit Return Path and the
originating task retains closure responsibility.

## Output

Return the package in chat by default:

```markdown
# Handoff

## Task State
## Decisions Locked
## Key Outputs
## Current Working State
## Open Questions
## Suggested Skills
## Return Path
## Next Action
```

Omit Suggested Skills or Return Path when they do not apply.

Completion criterion: a new agent or teammate can continue from Next Action
without the original conversation and without replaying completed work.
