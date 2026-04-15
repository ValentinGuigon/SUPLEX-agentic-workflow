# AGENTS.md

## Project identity

- Project: `{project_name}`
- Primary objective: reusable SUPLEX control-layer scaffold for bounded agentic work
- Use `./.suplex/docs/` as canonical SUPLEX control memory and `./.suplex/handoffs/` as bounded task-family entry points.

## Stable governance only

This file is the stable governance layer for the repository.
Keep it short.
Do not put long task-specific execution packets here.
Do not rewrite this file during routine work.

## Core operating rules

- Default to read-only / planning mode first.
- Work through bounded task families only.
- Do not broaden the current stage beyond the active handoff.
- SUPLEX runtime does not require a full audit at every pass; reconstruct only the minimum context needed for the current decision.
- Do not rename, move, or delete files unless explicitly instructed.
- Do not infer canonicality from filenames alone.
- If docs, assumptions, and proposed artifacts disagree, stop and return to planning.
- If a material blocker or ambiguity would likely affect scope, architecture, correctness, cost, or irreversible change, restate it to the user before proceeding and ask whether they want to resolve it directly or authorize supervisor / agent best judgment.
- Treat the target repo's `README.md` as the mandatory seed specification input for initialization.
- This template repo's own `README.md` is packaging documentation for the template itself, not a substitute seed specification for a future target repo.
- If the target repo's `README.md` is missing, halt initialization and ask the user either to add it or to provide a project description so one can be drafted first.
- Supervision may operate without direct repo access when it is given a current supervision packet, active handoff, and latest report or checkpoint.

## Source-of-truth rules

- Treat the target repo's `README.md` as the first required seed input for initialization.
- Treat `SUPLEX.md` as the root entrypoint into the installed SUPLEX workflow.
- Treat `./.suplex/docs/` as canonical SUPLEX control memory after initialization.
- Treat `./.suplex/docs/09_supervision_brief.md` as the portable supervision-state artifact when repo access is absent.
- Treat `./.suplex/handoffs/active/current_handoff.md` as the first execution-boundary artifact to resolve at startup.
- In `standard` mode, treat dated handoffs and execution reports in `./.suplex/handoffs/history/` as the canonical bounded-pass record.
- In `sans-sucre` mode, treat `./.suplex/handoffs/active/current_handoff.md` and `./.suplex/handoffs/active/current_execution_report.md` as the live bounded-pass record.
- Treat `./.suplex/docs/13_bounded_task_backlog.md` as the default next-task sequencing reference only after any active handoff is resolved.
- No new implementation phase should begin without a handoff document.
- If the user invokes the execution layer or says that a new task awaits, read the active handoff and treat it as the task source rather than asking the user to restate the task.
- If canonical docs and repo artifacts disagree, flag the discrepancy before proceeding.

## Durable architecture rules

- SUPLEX governs the agentic layer only.
- Do not scaffold computation, modeling, data, notebook, analysis, pipeline, publication, or deployment structure by default.
- Do not create `src/`, `scripts/`, `data/`, `notebooks/`, `site/`, `public/`, or `.github/workflows/` unless a later project-specific handoff justifies them explicitly.
- Design the control layer so it can wrap an existing repository without restructuring that repository.
- Existing computation and publication architecture remains project-owner territory unless separately specified.

## Evidence tagging

When drafting or updating project docs, mark claims as:

- `[E]` directly evidenced from repo artifacts or canonical docs
- `[I]` strong inference from those artifacts
- `[U]` unresolved / uncertain

## Working mode

- Allowed task-family modes:
  - audit
  - classify
  - specify
  - implement narrowly
  - validate
  - checkpoint
- No hidden extra work outside the active stage.
- No claim of readiness from one draft, one table, or one bounded pass alone.
- Supervision should not offer to execute an active bounded pass unless the user explicitly collapses the supervisor / execution split for that pass.

## Documentation-on-change rule

If workflow behavior, artifact expectations, canonical status, or repo structure changes, update at least one relevant repo-local doc before closing the task family.

Typical targets:

- `./.suplex/docs/10_supervision_layer_spec.md`
- `./.suplex/docs/11_execution_layer_spec.md`
- `./.suplex/docs/01_source_of_truth_and_provenance.md`
- `./.suplex/docs/08_status_checkpoint.md`
- `./.suplex/docs/13_bounded_task_backlog.md`
- `./.suplex/docs/validation_ledger.md`
- `./.suplex/docs/discrepancy_log.md`

## Mutable-learning rule

Do not rewrite the stable governance file during routine work.
If a repeated lesson emerges from execution, write it to `./.suplex/docs/local_lessons.md`.
If stable governance should change, write a proposal to `./.suplex/docs/governance_update_proposals.md`.

## Context-clear rule

At the end of any bounded task family, state explicitly whether context can be cleared.
If the active bounded task family is still open, state explicitly that context cannot yet be cleared.
Context can be cleared only if:

1. the bounded task family is closed
2. relevant docs are updated
3. unresolved issues are logged
4. outputs or diagnostics are saved if applicable
5. the next task family is different in kind
