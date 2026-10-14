# Execution Admission

Use this contract whenever a tracked item is prepared for agent execution, a
later human stop condition divides the work, or a terminal transition closes
the item. Repository workflow adapters provide the concrete tracker values and
mutation tools; this reference owns the portable ordering and safety rules.

## Required Inputs

Before admitting a tranche, require all of the following:

- exact authority for each state, label, comment, or record mutation;
- a complete current [Agent Brief](agent-brief.md);
- a concrete non-admissible holding value;
- a claimant-bound execution claim with a unique worker identity and claim
  token, or an explicit adapter declaration that concurrent execution is
  unsupported and names the authority that serializes one worker;
- a durable Agent Brief location and read-back mechanism; and
- a re-triage route for stop conditions and failed verification.

Ordinary approval to do the work is not exact tracker-mutation authority. If an
input or adapter capability is missing, fail closed before execution or
publication and report the exact pending authority or configuration.

## Publish An Agent-Ready Candidate

1. Create or move the candidate into the adapter's non-admissible holding
   state. Never create it directly as `ready-for-agent`.
2. Persist the complete current Agent Brief.
3. Fetch the record and verify the brief, holding state, metadata, source links,
   and absence of conflicting workflow markers.
4. Only then apply the authorized `ready-for-agent` transition through
   `triage` and read it back.

Completion criterion: the candidate is agent-ready only after its complete
brief and exact execution tranche are durable and verified.

## Start Execution

1. Before the first implementation step, conditionally acquire the adapter's
   execution claim from the verified agent-ready state while recording this
   worker's identity and unique claim token.
2. Atomically remove `ready-for-agent` with that acquisition when the adapter
   supports it, then fetch the record and verify the exact claimant, token,
   non-admissible state, and absence of readiness.
3. A generic `in-progress` status plus read-back is not a lease. When the
   adapter cannot provide conditional atomic acquisition, proceed only if it
   explicitly declares concurrent execution unsupported and the named human or
   orchestration authority serializes this exact worker before source mutation.
4. Do not execute while the item remains agent-admissible, another claimant is
   present, the claim cannot be verified, or the serialization authority is
   absent.
5. Execute only the current tranche. Do not cross its stop condition or perform
   prohibited actions.

Completion criterion: this worker holds the unique verified claim, or the
adapter's explicit single-worker boundary has been verified; readiness is
cleared and the executable boundary is unambiguous before source mutation.

## Reach A Stop Condition

1. Record the transition evidence and stop without crossing the boundary.
2. Clear the current execution claim and fetch the record to verify that the
   claimant and claim token are absent.
3. Persist a superseding Agent Brief that marks the prior boundary consumed,
   names already-complete work that must not be replayed, and defines only the
   next executable tranche.
4. Keep the item non-admissible until the superseding brief is fetched and
   verified.
5. Re-triage from current evidence. Use `ready-for-human` only when the next
   action is human-only; use `ready-for-agent` only for safe, fully specified
   remediation or follow-on work.

Completion criterion: the consumed boundary cannot be replayed, and the next
state reflects the next action rather than a later consequential action.

## Complete Or Terminate

Before applying a terminal state, remove every core active workflow label or
readiness marker and clear the current execution claim before or atomically
with the terminal transition. Fetch the record and verify the terminal state,
closing evidence, metadata, absence of active workflow markers, and absence of
the claimant and claim token.

Completion criterion: the item is terminal and cannot still be discovered as
active or agent-ready.
