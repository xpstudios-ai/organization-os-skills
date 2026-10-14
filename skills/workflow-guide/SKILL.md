---
name: workflow-guide
description: Choose the next skill or artifact when the user asks how to navigate an agent workflow.
disable-model-invocation: false
metadata:
  invocation: auto
---

# Workflow Guide

Recommend a route through capabilities actually available in this context.
This guides existing work; discovering or installing external skills belongs
to the environment's skill finder.

1. Identify the desired outcome, current artifact, unresolved question and
   approval boundary. Read available repository/workspace instructions and
   discovery indexes. Read a candidate skill's actual entrypoint before
   describing it or recommending that any of its steps be skipped.
2. Read [persistence](../handoff/references/persistence.md) and prefer the configured persistence route. Explain whether the next useful
   artifact is a question, prototype, decision map, spec, ticket, implementation,
   review or handoff. A small task need not traverse the entire chain.
3. Recommend one immediate action and explain what it produces. Link to the
   current skill or artifact instead of maintaining a second static catalog.
   State missing capabilities explicitly; do not invent installed skills or
   assume development instructions are visible to a separate runtime.

Guidance alone does not start implementation, create tasks, install packages,
or publish. Continue only when the user's request authorizes the broader work.
Completion: the user has a context-specific next action, artifact and authority
boundary grounded in the current skill source.

Example: “Use workflow-guide to decide how to turn this idea into durable work.”

## Provenance

Adapted from Matt Pocock's `ask-matt`, MIT License, Copyright (c) 2026 Matt Pocock.
