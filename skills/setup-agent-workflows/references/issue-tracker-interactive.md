<!-- agent-skills:interactive:v1 -->

# Interactive Local Tasks

This route is paired with `workflow.execution_mode = "interactive"`.
Specifications and decisions follow the configured specification/domain route.
Tickets live under `.agents/work-items/active/<slug>/issues/` and completed
workstreams move to `.agents/work-items/archive/<slug>/` with references updated.

Search existing active records before creating a task. Record intent, decisions
and rationale, scope, plain-bullet acceptance criteria, dependencies, status,
verification and next action. Use one task for small work; split by independently
observable outcomes when useful. Update the record at checkpoints and read back
each write. Respect `publish_by_default = false` and review-only requests.

Status describes `needs-triage`, `needs-info`, `in-progress`, `completed`,
`wontfix`, or `archived`. `ready-for-human` may identify a human decision.
Do not publish `ready-for-agent`, worker claims or an automated execution brief
through this route. Changing to worker requires the admission contract to be
reviewed and the worker adapter to be installed explicitly.
