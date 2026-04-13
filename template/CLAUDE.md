# CLAUDE.md

## Project identity

- Project: `suplex-template`
- Primary objective: reusable SUPLEX control-layer scaffold for bounded agentic work
- `AGENTS.md` and `CLAUDE.md` are both core governance files and must remain materially aligned and non-conflicting.

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
- Treat the target repo's `README.md` as the mandatory seed specification input for initialization.
- This template repo's own `README.md` is packaging documentation for the template itself, not a substitute seed specification for a future target repo.
- If the target repo's `README.md` is missing, halt initialization and ask the user either to add it or to provide a project description so one can be drafted first.
- Supervision may operate without direct repo access when it is given a current supervision packet, active handoff, and latest report or checkpoint.

## Source-of-truth rules

- Treat the target repo's `README.md` as the first required seed input for initialization.
- Treat `docs/` as canonical control memory after initialization.
- Treat `docs/09_supervision_brief.md` as the portable supervision-state artifact when repo access is absent.
- Treat stage handoffs in `handoffs/` as the execution boundary for bounded tasks.
- No new implementation phase should begin without a handoff document.
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

## Documentation-on-change rule

If workflow behavior, artifact expectations, canonical status, or repo structure changes, update at least one relevant repo-local doc before closing the task family.

Typical targets:

- `docs/01_source_of_truth_and_provenance.md`
- `docs/08_status_checkpoint.md`
- `docs/validation_ledger.md`
- `docs/discrepancy_log.md`

## Mutable-learning rule

Do not rewrite the stable governance file during routine work.
If a repeated lesson emerges from execution, write it to `local_lessons.md`.
If stable governance should change, write a proposal to `governance_update_proposals.md`.

## Context-clear rule

At the end of any bounded task family, state explicitly whether context can be cleared.
Context can be cleared only if:

1. the bounded task family is closed
2. relevant docs are updated
3. unresolved issues are logged
4. outputs or diagnostics are saved if applicable
5. the next task family is different in kind
