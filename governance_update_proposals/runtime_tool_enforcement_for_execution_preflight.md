# Runtime Tool Enforcement For Execution Preflight

## Status

Proposed.

## Context

SUPLEX governance now states that execution must acknowledge the active handoff's instructions, action surface, read/write scope, forbidden actions, validation plan, and relevant local skill, agent, governance, or pipeline constraints before substantial work. Execution should then proceed by default unless a defined exception trigger requires renewed confirmation before project-domain implementation, skill invocation, pipeline execution, command execution, or source mutation.

This is currently a governance and prompt-level rule. A compliant agent should follow it, but there is not yet a technical enforcement layer that blocks an agent, skill, or runner from proceeding without confirmation.

## Proposal

Add runtime or harness-level enforcement when SUPLEX has an execution runner, command wrapper, skill launcher, or comparable control point.

The enforcement layer should fail closed unless the execution preflight has been recorded and any required confirmation state for an exception-triggered pass is present.

## Desired Enforcement Behavior

- Refuse to invoke a skill or pipeline unless the active handoff has a recorded execution preflight and any exception-triggered confirmation required by that handoff.
- Refuse command execution or file writes outside the handoff's declared action surface.
- Require machine-readable fields for:
  - active handoff path
  - intended action surface
  - allowed read paths
  - allowed write paths
  - forbidden paths
  - source mutation policy
  - relevant skill or pipeline constraints
  - confirmation status
- Treat missing, stale, ambiguous, or contradictory confirmation state as not confirmed.
- For source documents or protected inputs, optionally hash files before and after execution and fail if mutation was not authorized.
- Record violations or aborted attempts in the execution report and discrepancy log.

## Example Machine-Readable Gate

```yaml
execution_preflight:
  handoff_path: ".suplex/handoffs/active/current_handoff.md"
  action_surface: "staged_artifact"
  allowed_reads:
    - "manuscripts/source.docx"
  allowed_writes:
    - "outputs/editing/"
    - ".suplex/handoffs/history/"
  forbidden_writes:
    - "manuscripts/source.docx"
  source_mutation_allowed: false
  skill_or_pipeline: "run-editing"
  user_confirmed: false
  reconfirmation_trigger: null
  confirmed_scope: null
```

## Acceptance Criteria

- Execution cannot start project-domain implementation without recorded preflight state.
- Skill or pipeline launch fails if required exception-triggered confirmation is missing.
- Writes outside declared paths are blocked or reported as violations.
- Source mutation is impossible unless both the user and the workflow explicitly authorize it.
- Tests cover missing confirmation, stale confirmation, ambiguous confirmation, and forbidden write attempts.

## Notes

This proposal is not required for the current document-governed SUPLEX workflow to operate. It is the stronger version needed if SUPLEX gains a runner, wrapper, or other execution harness that can mechanically enforce governance rules instead of relying only on agent compliance.
