---
name: repo-review
description: Review a stable repository candidate or verify incoming code-review findings against the code, standards, and original request.
disable-model-invocation: false
user-invocable: true
argument-hint: "[files, diff, PR, or description of changes]"
metadata:
  invocation: auto
---

# Repo Review

Review one stable candidate along two axes:

- **Standards:** repository rules, required gates, safety, and test adequacy.
- **Spec:** the originating request, issue, PRD, plan, or PR description.

The only route is direct review in the originating task. Do not launch a
subagent or separate task for this skill. Scale checks to the changed surfaces
and consequences, not diff size alone. If the user or repository requires an
independent opinion, report that the requirement remains unmet; an in-task
review cannot certify independence.

## 1. Identify The Candidate

Read `AGENTS.md` and applicable coding, review, documentation, and workspace
standards. Inspect:

- `git diff HEAD`
- `git diff --cached`
- `git status --short`
- every relevant untracked file
- the best available stable Spec source

Bind evidence to a commit or PR head when available; otherwise record a diff
hash plus status. For implementation completion, resolve known fixes before the
final verdict.

Completion criterion: scope, candidate identity, Standards, Spec, and available
gate evidence are explicit.

## 2. Review The Candidate

When incoming review findings are supplied, verify each against the current
candidate and originating request before accepting it. Report confirmed,
refuted, or unresolved, with code evidence and any missing reproduction.
Reassess severity from the actual consequence; rank confirmed issues and explain
refutations without assuming the reviewer lacks context. Verification alone
does not authorize fixes. Continue implementation only within existing scope.

Inspect correctness, safety, stale references, scope, and meaningful test
coverage. Run changed-surface checks plus repository-required gates. Use
structural validation for docs, configuration, policy, and skill changes rather
than irrelevant runtime tests.

For security, privacy, authority, data loss, persistence, migration,
deployment, production, external contracts, installer ownership, or broad
propagation, inspect the affected boundary and its failure paths explicitly.

For code changes, also apply the concise optional
[code-change baseline](references/code-change-baseline.md). Treat it as a
prompt for evidence, not a requirement to invent findings or refactor outside
the candidate's scope. When justified green refactoring is approved, read
[refactoring guidance](references/refactoring.md) and verify after each change.

Completion criterion: findings are evidence-backed and every required check
passed or has an exact skip reason. An implementation pass has no blocking
Standards or Spec finding.

Any source mutation invalidates the prior verdict. Review the updated candidate
and rerun affected checks after a fix. The originating implementation task owns
fixes and tests.

Review once per stable tranche, not after each thin implementation slice.
After a fix, reassess affected contracts and reuse still-valid evidence for
unchanged surfaces. Widen only for newly discovered impact. A short report is
not a token budget; this route launches no review agents or model escalations.

Completion criterion: the current candidate has a verdict backed by its scope,
Standards, Spec, and checks; any required independent opinion is marked unmet.

## Test Adequacy

For changed behavior, require happy and meaningful negative paths, exact stable
contract assertions, compatibility coverage only where compatibility is
promised, and at least one public-boundary path when adapters or persistence are
crossed. A review-only task reports gaps; an authorized implementation task
adds the smallest useful regression test before a fix when practical.

## Output

List findings first, ordered `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`:

```text
SEVERITY [Standards|Spec] file:line - Title
Why it matters.
Suggested fix.
```

On pass, report the in-task review, candidate identity, reviewed scope, checks
run or reused, and exact skips. Recommend `repo-document`
when docs, standards, discovery, or skill semantics may be affected.

## Provenance

Adapted from Matt Pocock's repository-review workflows in
`mattpocock/skills`, MIT License, Copyright (c) 2026 Matt Pocock. The optional
code-smell baseline is informed by Martin Fowler's published refactoring
catalog.
