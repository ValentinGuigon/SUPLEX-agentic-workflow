# 02 SUPLEX Operating Workflow

## 1. Purpose of this workflow document

This document defines how SUPLEX runs after initialization. It adds the runtime operating protocol that sits on top of stable governance and bounded handoffs.

The workflow is for control-layer operation only. It does not authorize computation scaffolding, publication scaffolding, or project-domain implementation outside the active bounded task.

## 2. Role definitions

### User

- Owns goals, quality standards, approval thresholds, and final decisions.
- May accept, reject, refine, or redirect supervisory proposals.
- Remains the authority over scope broadening and structural change.

### Scaffolder

- Initializes the SUPLEX control layer in a target repository.
- Establishes the initial control-memory docs, handoff structure, and internal init state.
- Stops after the repo is ready for supervision bootstrap.

### Supervisor

- Governs scope after initialization.
- Interprets canonical docs, handoffs, execution reports, checkpoints, and validation state.
- Decides what level of reconstruction is needed for the current decision.
- Issues the next bounded task to the execution layer.
- May operate with or without direct repo access.

### Executor

- Performs the bounded task defined by the supervisor.
- Works only within the active handoff and stable governance rules.
- Returns a written execution report instead of deciding the next task autonomously.

### Architect as escalation mode

- Architect is not a permanent parallel role.
- It is a supervision escalation mode used when governance, structure, canonical status, or operating protocol must change before further implementation can proceed safely.

## 3. The SUPLEX pass lifecycle

### Initialization

- SUPLEX is initialized in the target repo.
- The scaffolder confirms the target repo seed inputs and prepares the control layer.
- Copied control docs that contain repo-specific state must be rewritten to the target repo before supervision uses them as current state.
- At minimum, initialization rewrites `docs/00_project_scope.md`, `docs/08_status_checkpoint.md`, and `docs/09_supervision_brief.md` from target-repo evidence before supervision bootstrap.
- Initialization ends when the repo is ready for supervision bootstrap.

### Supervision bootstrap

- The first active layer after `suplex init` is supervision, not execution.
- The supervisor reviews the seed state needed to decide the first bounded task.
- That review may use full audit, local reconstruction, or no audit depending on what is required.

### Bounded execution

- The supervisor issues a bounded execution prompt tied to an active handoff.
- The executor performs only that bounded task.

### Execution report

- The executor returns a written report to the supervisor.
- The report must be sufficient for supervisory interpretation even if the supervisor does not have repo access.

### Supervisor interpretation

- The supervisor restates the important reported facts.
- The supervisor interprets validation state, discrepancies, unresolved items, and scope impact.
- The supervisor decides whether to close the task family, request validation, request checkpointing, issue a follow-on bounded task, or escalate into architecture mode.

### Validation / checkpoint

- Validation confirms whether the bounded pass met its acceptance criteria.
- Checkpointing records the latest validated state, next decision boundary, and context-clear status.

### Next bounded task or context-clear

- If more bounded work is needed, the supervisor defines the next handoff or activates the next bounded pass.
- If closure conditions are met, the supervisor explicitly states that the task family is closed and whether context can be cleared.

## 4. Reconstruction policy

Full audit is not the default at every pass.

### When full audit is required

Use full audit when:

- initialization or re-initialization is being performed
- canonical source-of-truth status is unclear or disputed
- governance or structural changes may affect multiple layers of the repo
- there is evidence that prior checkpoints, reports, or handoffs are stale, inconsistent, or insufficient
- the supervisor cannot safely determine scope from narrower reconstruction

### When local reconstruction is sufficient

Use local reconstruction when:

- the active handoff is clear and bounded
- the next decision depends only on a limited subset of docs, files, reports, or artifacts
- the supervisor needs to verify a recent change, discrepancy, or validation result without re-auditing the whole repo
- the task family is continuing from an already validated checkpoint

Local reconstruction means rebuilding only the minimum context needed for the current supervisory decision.

### When no audit is required

Use no audit when:

- the supervisor already has sufficient current state from the supervision brief, active handoff, and latest validated report or checkpoint
- the next action is a direct continuation with no new ambiguity about scope, provenance, or structure
- the decision is procedural rather than reconstructive

### Default rule

- Full audit is exceptional, not automatic.
- The supervisor must reconstruct only what is necessary for the current decision.

## 5. Non-repo-access supervision rule

- The supervisor may operate without direct repository access.
- In that case, the supervision packet must be sufficient for bounded supervision.
- A verbatim copy of this template repo's own supervision brief is not a valid packet for another repo; the packet must be refreshed to reflect the target repo's current state.
- The minimum required packet is:
  - `docs/09_supervision_brief.md`
  - the active handoff
  - the latest execution report and/or latest checkpoint
- When repo access is absent, the supervisor should avoid guessing hidden repo state and should govern only from the validated packet it has.

## 6. Supervisor-to-executor relay

- The supervisor issues execution prompts.
- The executor returns a written report.
- The supervisor restates the important points from that report, interprets their meaning, and defines the next bounded step.
- The executor should not silently promote itself into supervision.

### Execution report contract

Every execution-layer pass must return a written report containing at least:

- What was done
- What was not done
- Why it was not done
- Files read
- Files created or changed
- Validation result
- Current blockers
- Recommended next bounded task

## 7. Architectural escalation rule

Escalate supervision into architecture mode before further implementation when:

- governance files need to change materially
- source-of-truth rules are incomplete or conflicting
- repo structure or control-memory structure must be revised
- the active task reveals that bounded implementation would otherwise make structural decisions implicitly
- the current handoff no longer matches the true decision boundary

Architecture mode should resolve the governance or structure decision first, then return to normal supervision for bounded execution.

## 8. Context-clear rule in workflow terms

A task family can be closed only when:

- the bounded objective is satisfied or explicitly failed with recorded reason
- required docs, validation records, and checkpoints are updated
- unresolved issues are logged
- outputs or diagnostics required by the handoff are saved
- the supervisor has stated the exact next bounded task or that no further task in the family remains

Context can be cleared only when:

- the task family is closed
- the latest validated state is recorded
- open blockers or discrepancies are logged
- the next task family is different in kind

## 9. Minimal post-init startup sequence

Immediately after `suplex init`:

1. confirm the control-layer initialization outputs exist
2. confirm the copied repo-state docs have been rewritten to the target repo's current state
3. bootstrap supervision using the canonical control docs and init state
4. determine the minimum required reconstruction level for the first decision
5. identify or draft the first active bounded handoff
6. issue the first execution prompt only after supervision has defined scope

The first active agent after init is the supervision layer, not the execution layer.

The repo is not ready for supervision bootstrap if those target-state docs still describe `suplex-template` or any other stale source repo.
