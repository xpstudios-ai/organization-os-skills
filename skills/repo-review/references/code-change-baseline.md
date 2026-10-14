# Code-Change Review Baseline

Use this compact baseline only when the candidate changes executable code.
Repository standards and the originating Spec remain authoritative.

Check for evidence of:

- incorrect boundaries, error handling, cleanup, or state transitions;
- duplicated knowledge or behavior that can drift;
- Long Function, Large Class, or deeply nested control flow that obscures the
  changed behavior;
- Long Parameter List, Primitive Obsession, or Data Clumps that reveal a
  missing interface;
- Feature Envy, Shotgun Surgery, or Divergent Change across the touched seam;
- hidden mutation, unsafe shared state, temporal coupling, or surprising side
  effects; and
- tests that assert implementation details instead of observable behavior.

Report only candidate-scoped, evidence-backed findings. Do not require a
refactor solely because a catalog label could apply.

This baseline is informed by Martin Fowler's public refactoring catalog.

## Impact And Reversibility

When a change affects public behaviour or operations, describe the affected
users/systems, before/after evidence, whether reversal is practical, and the
rollback or recovery route. Scale this to the consequence; do not invent release
ceremony for a small reversible change.
