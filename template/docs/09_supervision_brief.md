# 09 Supervision Brief

## 1. Purpose of the supervision brief

This file is the portable supervision packet for cases where the supervisor cannot read repository files in the current session. It captures the minimum current-state information needed to govern the next bounded decision.

## 2. How this file should be used

- Read this file together with the active handoff and the latest execution report or status checkpoint.
- Use it to decide the next bounded supervisory action without assuming unseen repo context.
- Refresh it whenever supervision-relevant state changes materially.
- When this template is applied to a target repo, rewrite the repo-state sections below so they reflect that target repo's current state before using this file as a portable packet.
- During initialization, that rewrite must happen after control-layer copy and before supervision bootstrap.
- At minimum, the paired target-state rewrite set is `docs/00_project_scope.md`, `docs/08_status_checkpoint.md`, and this file.
- A verbatim copy of the template repo's own brief is not a valid supervision packet for another repo.

## 3. Project identity

- Project: `suplex-template`
- Purpose: reusable SUPLEX control-layer scaffold for bounded agentic work
- Scope boundary: control-layer runtime and governance only; no computation or publication scaffolding by default

## 4. SUPLEX workflow summary

- SUPLEX runs as a supervised bounded-pass system.
- The first active layer after initialization is supervision.
- Successful init always installs the same full SUPLEX agentic control layer regardless of target-repo shape.
- Each pass does not require a full audit by default.
- Active-handoff resolution happens before backlog-driven next-task selection.
- Reconstruction level must be chosen explicitly as one of:
  - full audit
  - local reconstruction
  - no audit
- Supervision decides whether architecture planning is needed before implementation begins.
- Execution is bounded by handoffs and closes through validation and checkpointing.

## 5. Current bounded task family

- Task family: add the missing SUPLEX runtime workflow layer to the template
- Active mode set: `implement narrowly`, `validate`, `checkpoint`

## 6. Active source-of-truth rule

- `docs/` is canonical control memory.
- `handoffs/active/current_handoff.md` is the first execution-boundary artifact to resolve.
- `standard` mode uses dated handoffs and execution reports in `handoffs/history/`; `sans-sucre` mode uses `handoffs/active/current_handoff.md` plus `handoffs/active/current_execution_report.md`.
- `docs/13_bounded_task_backlog.md` is the default next-task sequencing artifact only after any active handoff is resolved.
- Stable governance remains in `AGENTS.md` and `CLAUDE.md`.
- Handoffs constrain execution but do not override stable governance.
- Repeated operational lessons flow through `docs/local_lessons.md`, while stable-governance changes flow through `docs/governance_update_proposals.md`.

## 7. Active handoff summary

- The current runtime-layer pass added `docs/02_suplex_operating_workflow.md` as the runtime workflow document.
- The current runtime-layer pass added `docs/09_supervision_brief.md` as the portable supervision-state artifact.
- Governance and handoff files were aligned only where required by the runtime layer.
- The bounded pass did not broaden into computation scaffolding, publication scaffolding, or project-specific initialization logic.

## 8. Latest validated state

- The template already contains the governance kernel, canonical control-memory docs, handoff structure, and initialization state.
- The runtime operating protocol for post-init supervision and bounded execution is now documented.
- The template now distinguishes `full audit`, `local reconstruction`, and `no audit`.
- The template now includes a portable supervision packet for cases where the supervisor lacks repo access.

## 9. Latest execution report summary

- The runtime-layer pass added the workflow document and portable supervision brief.
- Governance and handoff docs were updated narrowly to align with reconstruction modes, supervision bootstrap, and non-repo-access supervision.
- Validation passed against the bounded acceptance criteria without adding computation or publication scaffolding.

## 10. Open discrepancies / blockers

- No open blocker remains inside the runtime layer itself.
- Future downstream validation is still needed when the template is extracted or applied to a target repository.

## 11. Exact next supervisory decision

- Read `handoffs/active/current_handoff.md` first and determine whether an unfinished bounded pass already exists.
- If there is no active pass, use `docs/13_bounded_task_backlog.md` as the default sequencing reference unless a blocker or discrepancy justifies a deviation.
- If you can read the repository files in the current session, inspect the repo and `README.md` before deciding what happens next.
- If you cannot read the repository files in the current session, do not guess hidden repo state; use this brief, the latest checkpoint, and the active handoff as your working state instead.
- Ask the user what they want to do next.
- Read `project_mode` from `.suplex/init_state.yaml`.
- If the mode is `greenfield`, ask whether the user wants to provide more project detail and treat architecture-planning or structure-confirmation as the default first bounded pass unless current information already makes that unnecessary.
- If the mode is `overlay`, ask whether the user wants to provide more project detail and treat repo-state audit or local reconstruction as the default first bounded pass so the next task is defined from current repo evidence rather than assumptions.
- Propose exactly one next bounded task.

## 12. Update rule

- Refresh this file whenever the active handoff, latest validated state, latest execution report summary, blockers, or exact next supervisory decision changes materially.
- The supervisor or the executor acting under an explicit documentation step may update it.
- `docs/08_status_checkpoint.md` remains the fuller validated checkpoint record; this file is the portable supervisory state packet derived from that checkpoint and the active handoff.
