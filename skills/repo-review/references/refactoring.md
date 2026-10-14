# Refactoring While Green

Refactor only after the focused tests pass. Useful candidates include:

- Duplication with a stable shared meaning
- Long methods with multiple responsibilities
- Shallow modules whose interface exposes most implementation complexity
- Feature envy or logic owned by the wrong domain object
- Primitive values that hide a durable domain invariant
- Missing seams around external systems

Use `codebase-design` when the change affects module depth, interfaces, seams,
adapters, leverage, or locality. Run the relevant tests after every refactor
step and stop if observable behavior changes unexpectedly.
