# 13 Bounded Task Backlog

## Purpose

This document is the canonical prioritized backlog for bounded task selection.

It exists to:
- keep the next several bounded passes visible in one place
- preserve ordering rationale
- prevent the next task from being re-inferred from scratch each time
- separate what should happen next from the broader narrative in status docs

This is not a changelog and not a substitute for an active handoff.

The active execution contract still belongs in `./.suplex/handoffs/active/current_handoff.md`.

## Usage Rules

- Supervision should consult this backlog only after resolving whether an active handoff already exists.
- A backlog item is not active until it is turned into a dated handoff and mirrored in `./.suplex/handoffs/active/current_handoff.md`.
- Reorder this backlog only when repo state, validation results, or blocking dependencies materially change.
- Keep items bounded enough that one item can become one handoff without broad reinterpretation.
- When an item is completed, update this file and `./.suplex/docs/08_status_checkpoint.md`.

## Current Priority Queue

### Now

#### 1. Run the first repo-specific architecture-planning or structure-confirmation pass
- task family: `specify`
- why this is next:
  - initialization ends with supervision rather than direct execution
  - if `project_mode` is `greenfield`, the next safe step is usually architecture-planning or structure-confirmation before implementation
  - if `project_mode` is `overlay`, the next safe step is usually repo-state audit or local reconstruction before implementation
- likely deliverables:
  - in `standard` mode, one dated handoff for the first bounded supervisory pass
  - in `sans-sucre` mode, one active handoff plus one active execution-report placeholder update for the first bounded supervisory pass
  - one explicit decision on whether the first bounded pass should be architecture-planning, repo-state audit, or local reconstruction
  - one proposed next bounded task only
- likely files in scope:
  - `README.md`
  - `.suplex/init_state.yaml`
  - `./.suplex/docs/00_project_scope.md`
  - `./.suplex/docs/08_status_checkpoint.md`
  - `./.suplex/docs/09_supervision_brief.md`
  - `./.suplex/docs/13_bounded_task_backlog.md`
  - `./.suplex/handoffs/active/current_handoff.md`

### Next

#### 2. Validate one full handoff-to-report-to-checkpoint cycle in the target repo
- task family: `validate`
- why this follows:
  - the stricter runtime should be exercised on one real bounded pass before being treated as proven
- likely deliverables:
  - in `standard` mode, one dated handoff
  - in `standard` mode, one dated execution report
  - in `sans-sucre` mode, one active handoff and one active execution report
  - one validation-ledger entry if actual validation evidence is produced

#### 3. Refine backlog sequencing after the first real bounded pass
- task family: `checkpoint`
- why this follows:
  - once the first real pass exists, the default queue can be grounded in evidence rather than initialization assumptions

## Current Selection Rule

Unless a newer active handoff, blocker, or validation result creates a stronger dependency, the default next bounded pass should be:

`Read project_mode from .suplex/init_state.yaml, then run the first repo-specific architecture-planning pass for greenfield repos or the first repo-state audit/reconstruction pass for overlay repos.`
