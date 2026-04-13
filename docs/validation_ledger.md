# Validation Ledger

## 2026-04-13 - Runtime Workflow Layer Pass

| Check | Result | Notes |
|---|---|---|
| `docs/02_suplex_operating_workflow.md` exists | PASS | Added as the runtime workflow document |
| `docs/02_suplex_operating_workflow.md` fully specifies the runtime workflow | PASS | Includes purpose, roles, lifecycle, reconstruction policy, portable-supervision rule, relay contract, architecture escalation, context-clear rule, and post-init startup sequence |
| `docs/09_supervision_brief.md` exists | PASS | Added as the portable supervision packet |
| `docs/09_supervision_brief.md` is usable without repo access | PASS | Includes bounded-task state, source-of-truth rule, active handoff summary, latest validated state, blockers, next supervisory decision, and update rule |
| Reconstruction policy distinguishes `full audit`, `local reconstruction`, and `no audit` | PASS | Explicitly defined in the workflow doc |
| Full audit is not treated as mandatory at every pass | PASS | Explicitly rejected as the default rule in the workflow doc and reinforced in governance/handoff docs |
| Workflow supports supervision without repo access | PASS | Workflow plus supervision brief define the portable operating packet |
| First active role after init is the supervision layer | PASS | Explicitly stated in `docs/02_suplex_operating_workflow.md` and aligned in `handoffs/initialization.md` |
| Governance files remain aligned with the runtime layer | PASS | `AGENTS.md` and `CLAUDE.md` now include the reconstruction and portable-supervision rules |
| Handoff files remain aligned with the runtime layer | PASS | `handoffs/README.md`, `_handoff_template.md`, and `initialization.md` were updated narrowly to match runtime behavior |
| No computation-layer scaffolding was created | PASS | No new computation directories or files were added |
| No publication-layer scaffolding was created | PASS | No new publication directories or files were added |
| No March Madness-specific language was introduced | PASS | Wording remains template-generic |

## 2026-04-13 - Controlled Target-Repo Validation Pass

| Check | Result | Notes |
|---|---|---|
| Test A: greenfield target with `README.md` can receive only the SUPLEX control layer | PASS | `tmp_validation/testA_greenfield` contains only `README.md`, `AGENTS.md`, `CLAUDE.md`, `.suplex/`, `docs/`, and `handoffs/` after init simulation |
| Test A: no computation/publication scaffolding is created in greenfield init | PASS | No `src/`, `scripts/`, `data/`, `notebooks/`, `site/`, `public/`, or `.github/workflows/` were introduced in `tmp_validation/testA_greenfield` |
| Test A: first active layer after init is supervision, not execution | PASS | Confirmed by `docs/02_suplex_operating_workflow.md` and `handoffs/initialization.md` |
| Test B: overlay target preserves existing project structure | PASS | `tmp_validation/testB_overlay` retained preexisting `src/`, `data/`, `notebooks/`, and `site/` directories and their seed files |
| Test B: overlay init does not restructure or claim existing computation/publication-like directories | PASS | SUPLEX files were added alongside existing directories; no preexisting project directories were renamed, moved, deleted, or rewritten |
| Test C: supervision with repo access can rely on documented reconstruction modes | PASS | `docs/02_suplex_operating_workflow.md` explicitly distinguishes `full audit`, `local reconstruction`, and `no audit` |
| Test C: supervision with repo access produces a truthful current-state packet immediately after init | FAIL | In both initialized targets, copied `docs/00_project_scope.md` and `docs/09_supervision_brief.md` still described `suplex-template` rather than the target repo |
| Test D: supervision without repo access works from the portable packet alone | FAIL | The copied `docs/09_supervision_brief.md` was stale template state, so the packet was not sufficient without additional repo-access reconstruction |
| Test E: missing `README.md` halts initialization | PASS | `handoffs/initialization.md` prohibits silent continuation when `README.md` is missing, and no control layer was applied to `tmp_validation/testE_missing_readme` |
| Test E: missing `README.md` behavior asks for either a `README.md` or project description | PASS | `README.md`, `AGENTS.md`, and `docs/01_source_of_truth_and_provenance.md` all require halting and requesting the file or enough project description to draft one |
| Minimum correction for stale target-repo state is now documented | PASS | `README.md`, `docs/02_suplex_operating_workflow.md`, `docs/09_supervision_brief.md`, and `handoffs/initialization.md` now require rewriting copied repo-state docs during init |

## 2026-04-13 - Target-Repo Initialization Revalidation Pass

| Check | Result | Notes |
|---|---|---|
| Init behavior now requires rewriting the minimum target-state doc set before supervision bootstrap | PASS | `handoffs/initialization.md` and `docs/02_suplex_operating_workflow.md` now explicitly require rewriting `docs/00_project_scope.md`, `docs/08_status_checkpoint.md`, and `docs/09_supervision_brief.md` before supervision uses them |
| Test C: supervision with repo access produces a truthful current-state packet immediately after init | PASS | Fresh targets in `tmp_validation/reval_A_greenfield` and `tmp_validation/reval_B_overlay` have target-specific `docs/00_project_scope.md`, `docs/08_status_checkpoint.md`, and `docs/09_supervision_brief.md` after init simulation |
| Test D: supervision without repo access works from the portable packet alone | PASS | In both fresh targets, `docs/09_supervision_brief.md` plus `handoffs/initialization.md` and the latest `docs/08_status_checkpoint.md` form a truthful portable supervision packet without extra repo inspection |
| Spot check A: greenfield target with `README.md` still receives only the SUPLEX control layer | PASS | `tmp_validation/reval_A_greenfield` contains only `README.md`, `AGENTS.md`, `CLAUDE.md`, `.suplex/`, `docs/`, and `handoffs/` |
| Spot check A: greenfield init still adds no computation/publication scaffolding | PASS | No `src/`, `scripts/`, `data/`, `notebooks/`, `site/`, `public/`, or `.github/workflows/` were introduced in `tmp_validation/reval_A_greenfield` |
| Spot check B: overlay init still preserves existing project structure | PASS | `tmp_validation/reval_B_overlay` retained its preexisting `src/`, `data/`, `notebooks/`, and `site/` directories and seed files |
| Spot check B: overlay init still introduces no extra computation/publication scaffolding | PASS | The repair added only the control layer and target-state doc rewrites; no new project-architecture directories were introduced |
| Spot check E: missing `README.md` still halts initialization | PASS | `tmp_validation/reval_E_missing_readme` remained untouched and received no control-layer files |
| No computation/publication scaffolding was introduced by the repair pass | PASS | Validation targets remained limited to control-layer files plus the overlay target's preexisting directories |
