# Preparation Workflow

Load this reference only when the meeting is upcoming or the user asks to prep
for a future meeting.

## Goal

Create a useful, date-specific Pre-Call Brief before the meeting happens. Keep
it separate from the post-meeting record. Do not invent outcomes, decisions,
attendance, or completed actions.

## Inputs

Use whatever is available:

- upcoming meeting link, title, date, organizer, or calendar context,
- previous meeting notes page,
- current open actions,
- linked tracker items, documentation records, documents, or project notes,
- user-supplied goals, agenda items, risks, or stakeholder context.

If no previous meeting page or action list is available, ask whether the user
wants to provide one. Continue without it only when the user confirms the prep
can be made from the current context.

## Steps

1. Resolve the meeting, the configured preparation destination, and its
   approved work-thread parent. Do not use a post-meeting database as the prep
   destination.
2. Read previous meeting notes, current action rows, linked issues, durable
   qualification or decision records, and supplied stakeholder context.
3. Identify carried-forward actions:
   - open actions from previous notes,
   - owner and due date when known,
   - status if the user or linked issue indicates progress,
   - blockers or missing owners.
4. When the durable source is a qualification master, select only the unresolved
   rows relevant to this conversation. Link those rows or their canonical
   source instead of copying the full master table, project status, or account
   history into the brief.
5. Draft the prep content from
   [../assets/pre-call-brief-template.md](../assets/pre-call-brief-template.md):
   - meeting goal,
   - selected unresolved source rows,
   - concise opening,
   - prioritized live questions,
   - likely objections and safe responses,
   - minimum safe data ask,
   - desired exit,
   - useful stakeholder-safe source links.
6. Adapt the questions to the actual relationship:
   - `Direct`: emphasize the client's problem, operational user, source and
     access, success measure, buyer, action path, and next decision.
   - `Partner` or `Channel`: emphasize the partner's concrete commitment,
     named end-client problem, access to the end-user and source owner,
     conversion path, security owner, data-rights authority, and next decision.
   - `OEMEmbedded`: additionally emphasize product integration boundaries,
     deployment and update ownership, security approval, rights for derived
     learning, and the split between OEM authority and end-client permission.
   Never treat an intermediary as the end client unless it is itself the buyer
   and user for the scope.
7. Publish only when the user explicitly asks for or approves an external
   write, then fetch the destination again to verify it.

## Output Shape

Use [../assets/pre-call-brief-template.md](../assets/pre-call-brief-template.md).
Do not use the post-meeting notes format or label planned decisions as completed
decisions.
