
# 09 Supervision Brief

## 1. Purpose of the supervision brief

This file is the portable supervision packet for debug_target when the supervisor does not have direct repository access.

## 2. How this file should be used

- Read this file together with the active handoff and latest checkpoint or report.
- Use it to decide the next bounded supervisory action without assuming unseen repo context.
- This brief was rewritten during target-repo initialization and is not a verbatim template copy. [E]

## 3. Project identity

- Project: `debug_target`
- Purpose: debug_target is the target repository for SUPLEX initialization.
- Scope boundary: control-layer initialization and supervision only; no computation or publication scaffolding by default

## 4. SUPLEX workflow summary

- The first active layer after initialization is supervision.
- Reconstruction level is chosen explicitly.
- Execution remains bounded by handoffs.

## 5. Current bounded task family

- Task family: initialization complete; awaiting supervision bootstrap
- Active mode set: `checkpoint`

## 6. Active source-of-truth rule

- `docs/` is canonical control memory.
- `handoffs/` defines bounded task packets.
- Stable governance remains in `AGENTS.md` and `CLAUDE.md`.

## 7. Active handoff summary

- Initialization prepared the control layer and rewrote target-state docs before supervision bootstrap. [E]

## 8. Latest validated state

- The repo was initialized in `greenfield` mode from its own `README.md`. [E]
- `docs/00_project_scope.md`, `docs/01_source_of_truth_and_provenance.md`, `docs/08_status_checkpoint.md`, and this brief now describe the target repo rather than the template. [E]
- No computation or publication scaffolding was introduced. [E]

## 9. Latest execution report summary

- Initialization completed and left the repo ready for the first supervisory decision. [E]

## 10. Open discrepancies / blockers

- No blocker is currently recorded inside the control layer. [E]

## 11. Exact next supervisory decision

- Bootstrap supervision and define the first bounded task for debug_target. [E]

## 12. Update rule

- Refresh this file whenever supervisory state changes materially.
