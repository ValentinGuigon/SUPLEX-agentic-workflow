
        # 09 Supervision Brief

        ## 1. Purpose of the supervision brief

        This file is the portable supervision packet for Mode Standard`n`nStandard mode validation target. when the supervisor cannot read the repository files in the current session.

        ## 2. How this file should be used

        - Read this file together with the active handoff and latest checkpoint or report.
        - Use it to decide the next bounded supervisory action without assuming unseen repo context.
        - This brief was rewritten during target-repo initialization and is not a verbatim template copy. [E]

        ## 3. Project identity

        - Project: `Mode Standard`n`nStandard mode validation target.`
        - Purpose: Mode Standard`n`nStandard mode validation target. is the target repository for SUPLEX initialization.
        - Scope boundary: full control-layer initialization and supervision only; no computation or publication scaffolding by default

        ## 4. SUPLEX workflow summary

        - The first active layer after initialization is supervision.
        - Workflow infrastructure: `standard` mode with dated handoff / execution-report history. [E]
        - Reconstruction level is chosen explicitly.
        - Supervision must decide whether an architecture-planning pass is needed before implementation work begins.
        - Execution remains bounded by handoffs.

        ## 5. Current bounded task family

        - Task family: initialization complete; awaiting supervision bootstrap
        - Active mode set: `checkpoint`

        ## 6. Active source-of-truth rule

        - `docs/` is canonical control memory.
        - `handoffs/` defines bounded task packets.
        - Dated handoffs and execution reports should be read from `handoffs/history/` when present. [E]
        - Stable governance remains in `AGENTS.md` and `CLAUDE.md`.

        ## 7. Active handoff summary

        - Initialization prepared the control layer and rewrote target-state docs before supervision bootstrap. [E]

        ## 8. Latest validated state

        - The repo was initialized in `greenfield` mode from its own `README.md`. [E]
        - `docs/00_project_scope.md`, `docs/01_source_of_truth_and_provenance.md`, `docs/08_status_checkpoint.md`, and this brief now describe the target repo rather than the template. [E]
        - The same full SUPLEX agentic control layer was installed regardless of target-repo shape. [E]
        - No computation or publication scaffolding was introduced. [E]

        ## 9. Latest execution report summary

        - Initialization completed and left the repo ready for the first supervisory decision. [E]

        ## 10. Open discrepancies / blockers

        - No blocker is currently recorded inside the control layer. [E]

        ## 11. Exact next supervisory decision

        - If you can read the repository files in this session, inspect the repo and `README.md` before deciding what happens next. [E]
        - If you cannot read the repository files in this session, do not guess hidden repo state; use this brief, `docs/08_status_checkpoint.md`, and `handoffs/initialization.md` as your working state instead. [E]
        - Ask the user what they want to do next. [E]
        - Ask the user whether they want to provide more detail about the project before planning begins. [E]
- Treat architecture-planning or structure-confirmation as the default first bounded supervisory pass unless the user already provided enough detail to make that unnecessary. [E]
        - Propose exactly one next bounded task for Mode Standard`n`nStandard mode validation target.. [E]

        ## 12. Update rule

        - Refresh this file whenever supervisory state changes materially.
