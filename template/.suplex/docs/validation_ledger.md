# Validation Ledger

## 2026-04-14 - Template Source Payload Namespace Alignment Pass

| Check | Result | Notes |
|---|---|---|
| Source template payload now lives under `template/.suplex/` except for root `template/SUPLEX.md` | PASS | Source governance files, canonical docs, and handoff assets were moved under `template/.suplex/` |
| Bootstrap initializer still installs the same target-repo layout | PASS | Controlled local init still produced root `SUPLEX.md` plus the canonical payload under target `./.suplex/` |
| First supervision prompt still includes governance coexistence handling and correct mode-specific artifact guidance | PASS | Controlled local init in `standard` mode printed the expected overlay prompt with root-governance inspection guidance |
| Source-template layout documentation now matches the new namespace layout | PASS | `README.md`, `template/.suplex/init_state.yaml`, and the active handoff artifacts were updated to reflect the moved source layout |

## 2026-04-14 - Supervisor Material Ambiguity Decision Rule Pass

| Check | Result | Notes |
|---|---|---|
| Stable governance requires surfacing material blockers or ambiguities before proceeding under judgment | PASS | `template/.suplex/AGENTS.md` now requires the supervisor to restate material blockers or ambiguities and ask whether the user wants to resolve them directly or authorize best judgment |
| Runtime workflow requires the supervisor to ask for a decision path on material ambiguity | PASS | `template/.suplex/docs/02_suplex_operating_workflow.md` now defines the user-choice branch and requires reporting the adopted assumption during close or checkpoint |
| Supervision-layer spec records the adopted assumption when best judgment is authorized | PASS | `template/.suplex/docs/10_supervision_layer_spec.md` now requires the assumption to be captured in the handoff, report, checkpoint, or discrepancy trail |
| Bootstrap-generated first-supervision prompts carry the new rule into fresh installs | PASS | File inspection of `bootstrap/init_suplex.py` confirms the IDE and browser startup prompts now instruct supervisors not to silently make user-owned material judgment calls |

## 2026-04-14 - Handoff Template Material Ambiguity Record Pass

| Check | Result | Notes |
|---|---|---|
| Handoff template includes a dedicated field for material ambiguity decision paths | PASS | `template/.suplex/handoffs/templates/00_handoff_template.md` now includes `User Decision Path On Material Ambiguities` with the blocker, impact, user choice, and adopted assumption fields |
| Handoff guidance requires storing user-authorized best-judgment decisions in the handoff record | PASS | `template/.suplex/handoffs/README.md` now states that the decision path and adopted assumption should be recorded in the handoff itself |
| Execution startup restatement includes any user-authorized best-judgment assumption from the handoff | PASS | `template/.suplex/docs/11_execution_layer_spec.md` now requires executors to restate any recorded best-judgment assumption before substantial work |
| Execution reports include any material assumption used under user-authorized best judgment | PASS | `template/.suplex/docs/11_execution_layer_spec.md` now includes this as an explicit execution-report item |

## 2026-04-14 - Workflow Mode Split Pass

| Check | Result | Notes |
|---|---|---|
| Bootstrap initializer accepts explicit `standard` and `sans-sucre` workflow modes | PASS | `bootstrap/init_suplex.py` now accepts `--workflow-mode` and records `workflow_mode` in generated `.suplex/init_state.yaml` |
| Thin bootstrap wrappers can select `sans-sucre` during installation | PASS | `bootstrap/install.ps1` and `bootstrap/install.sh` now pass workflow mode through to the initializer |
| `sans-sucre` layout keeps separate active handoff and active execution-report artifacts without dated history | PASS | `bootstrap/init_suplex.py` now removes `handoffs/history/`, removes the dated execution-report template, and writes `handoffs/active/current_execution_report.md` in `sans-sucre` mode |
| Canonical docs describe both workflow modes and moved lesson / governance-memory paths | PASS | `README.md`, `template/.suplex/AGENTS.md`, `template/.suplex/docs/02_suplex_operating_workflow.md`, `template/.suplex/docs/09_supervision_brief.md`, `template/.suplex/docs/10_supervision_layer_spec.md`, `template/.suplex/docs/11_execution_layer_spec.md`, `template/.suplex/docs/13_bounded_task_backlog.md`, and handoff docs now reflect the split |
| Lesson and governance-memory artifacts now live under `./.suplex/docs/` | PASS | Added `template/.suplex/docs/local_lessons.md` and `template/.suplex/docs/governance_update_proposals.md` and removed the root-level copies |

## 2026-04-13 - Always-Full Init Semantics Pass

| Check | Result | Notes |
|---|---|---|
| Successful init always installs the same full SUPLEX control layer in greenfield repos | PASS | Controlled target `dev_validation/tmp_validation/always_full_init/A_greenfield` received `SUPLEX.md` plus the canonical payload under `./.suplex/` |
| Successful init always installs the same full SUPLEX control layer in overlay repos | PASS | Controlled target `dev_validation/tmp_validation/always_full_init/B_overlay` received the same SUPLEX control-layer payload; comparison excluding preexisting `src/`, `data/`, and `public` content showed no payload difference |
| Overlay init preserves existing repo structure | PASS | Seeded `src/`, `data/`, and `public` directories plus their files remained present and unchanged after init |
| Missing `README.md` still halts initialization | PASS | Controlled target `dev_validation/tmp_validation/always_full_init/C_missing_readme` exited with code `2` and remained empty |
| Emitted supervision prompt asks what should happen next | PASS | Successful runs printed `Check with the user what should happen next.` |
| Emitted supervision prompt asks whether architecture planning is needed | PASS | Successful runs printed `Decide whether an architecture-planning pass is needed before any implementation work proceeds.` |
| Emitted supervision prompt defers architecture determination to supervision | PASS | Successful runs printed `Determine whether an existing architecture is already present in the repo or described in README.md.` |
| Generated `.suplex/init_state.yaml` no longer carries payload-selection branching via `workflow_profile` | PASS | Generated init-state files for both successful targets contain no `workflow_profile` key |
| No remaining payload-selection references to `lite`, `standard`, or `fullstack` in the updated init path docs/code | PASS | File inspection across `bootstrap/init_suplex.py`, `README.md`, `template/.suplex/init_state.yaml`, `template/.suplex/docs/02_suplex_operating_workflow.md`, `template/.suplex/docs/09_supervision_brief.md`, and `template/.suplex/handoffs/initialization.md` found no remaining semantic references |

## 2026-04-13 - Bootstrap Interpreter Detection Repair Pass

| Check | Result | Notes |
|---|---|---|
| `bootstrap/install.sh` prefers `python3` over `python` | PASS | File inspection confirms the wrapper now probes `python3` first and selects `python` only if the first probe fails |
| `bootstrap/install.sh` fallback to `python` works when `python3` is unavailable | NOT RUN | Direct POSIX shell execution was blocked in this sandbox because Git `sh.exe`, `bash.exe`, and `dash.exe` each failed before script execution with `couldn't create signal pipe, Win32 error 5` |
| `bootstrap/install.ps1` prefers `py -3` over `python` | PASS | Wrapper now probes `py -3` first and only falls back to `python` if that probe is unusable |
| `bootstrap/install.ps1` fallback to `python` works when `py -3` is unavailable | PASS | Controlled local harness with a path-isolated fake `python.cmd` successfully ran the initializer after forcing the `py -3` probe to fail |
| Missing-interpreter path is explicit and actionable | PASS | PowerShell controlled execution emits the new Python 3 remediation message, and file inspection confirms the same explicit message structure in `bootstrap/install.sh` |
| Wrapper change does not alter init semantics after interpreter selection | PASS | Controlled local source-root runs for `bootstrap/install.ps1` still write the normal SUPLEX control-layer files and target-state artifacts without touching `bootstrap/init_suplex.py` |
| Live remote archive fetch path revalidated in this pass | NOT RUN | This bounded pass targeted interpreter discovery only and used controlled local source-root validation rather than network fetch |

## 2026-04-13 - Packaging Layout Refactor Pass

| Check | Result | Notes |
|---|---|---|
| Template payload lives under `template/` | PASS | The repo-root kernel files and directories were moved to `template/` |
| Root now represents the `SUPLEX-agentic-workflow` project rather than an initialized target repo | PASS | Root now contains project packaging materials plus `bootstrap/`, `template/`, and local dev validation artifacts |
| Bootstrap initializer sources kernel assets from `template/` | PASS | `bootstrap/init_suplex.py` now resolves required assets from `template/` before copying into the target repo |
| Greenfield target with `README.md` still initializes successfully | PASS | Controlled target under `dev_validation/tmp_validation/packaging_A_greenfield` received only the SUPLEX control layer |
| Overlay target with `README.md` still initializes successfully | PASS | Controlled target under `dev_validation/tmp_validation/packaging_B_overlay` preserved its seeded `src/`, `data/`, `notebooks/`, and `site/` directories |
| Missing `README.md` still halts initialization | PASS | Controlled target under `dev_validation/tmp_validation/packaging_E_missing_readme` remained untouched |
| Target-state doc rewrite still occurs | PASS | Initialized targets received target-specific `./.suplex/docs/00_project_scope.md`, `./.suplex/docs/01_source_of_truth_and_provenance.md`, `./.suplex/docs/08_status_checkpoint.md`, and `./.suplex/docs/09_supervision_brief.md` |
| Full repo is not cloned into the target repo | PASS | Initialized targets contain only copied SUPLEX kernel files/directories, not a `template/` or project-repo checkout |
| No computation/publication scaffolding introduced by the refactor | PASS | No new `src/`, `scripts/`, `data/`, `notebooks/`, `site/`, `public/`, or `.github/workflows/` directories were created by SUPLEX init |
| `tmp_validation/` no longer remains in the published root payload shape | PASS | Existing local targets were relocated to `dev_validation/tmp_validation/` |

## 2026-04-13 - Bootstrap Layer Pass

| Check | Result | Notes |
|---|---|---|
| Running from inside a target repo applies the kernel to the current working directory | PASS | `bootstrap/init_suplex.py` was run against controlled target repos using `--target-dir` pointing at each repo root |
| Missing `README.md` halts correctly | PASS | The missing-README target returned a halt message and received no SUPLEX files |
| Existing repo structure is preserved in overlay mode | PASS | The overlay target retained its seeded `src/`, `data/`, `notebooks/`, and `site/` directories unchanged |
| `suplex-template` is not cloned into the target repo | PASS | The initializer copies only root `SUPLEX.md` plus the canonical payload under `./.suplex/`; no template repo directory is created in the target |
| Only the control layer is added | PASS | Controlled greenfield init added only the SUPLEX kernel files and directories |
| Target-state docs are rewritten before supervision bootstrap | PASS | Initialized targets received target-specific `./.suplex/docs/00_project_scope.md`, `./.suplex/docs/01_source_of_truth_and_provenance.md`, `./.suplex/docs/08_status_checkpoint.md`, and `./.suplex/docs/09_supervision_brief.md` |
| `.suplex/init_state.yaml` is written for the target repo | PASS | Each successful init wrote target-specific mode and source metadata to `.suplex/init_state.yaml` |
| Ready message plus first supervision prompt are emitted | PASS | Successful runs printed a ready line followed by the supervision bootstrap prompt |
| Thin PowerShell installer path is implemented | PASS | `bootstrap/install.ps1` stages a temporary archive or local source root and delegates to `bootstrap/init_suplex.py` |
| Thin POSIX shell installer path is implemented | PASS | `bootstrap/install.sh` stages a temporary archive or local source root and delegates to `bootstrap/init_suplex.py` |
| Remote archive fetch path validated end to end in this pass | PARTIAL | The wrapper logic is implemented, but controlled validation in this environment used the local source-root path rather than live network fetch |

## 2026-04-13 - Runtime Workflow Layer Pass

| Check | Result | Notes |
|---|---|---|
| `./.suplex/docs/02_suplex_operating_workflow.md` exists | PASS | Added as the runtime workflow document |
| `./.suplex/docs/02_suplex_operating_workflow.md` fully specifies the runtime workflow | PASS | Includes purpose, roles, lifecycle, reconstruction policy, portable-supervision rule, relay contract, architecture escalation, context-clear rule, and post-init startup sequence |
| `./.suplex/docs/09_supervision_brief.md` exists | PASS | Added as the portable supervision packet |
| `./.suplex/docs/09_supervision_brief.md` is usable without repo access | PASS | Includes bounded-task state, source-of-truth rule, active handoff summary, latest validated state, blockers, next supervisory decision, and update rule |
| Reconstruction policy distinguishes `full audit`, `local reconstruction`, and `no audit` | PASS | Explicitly defined in the workflow doc |
| Full audit is not treated as mandatory at every pass | PASS | Explicitly rejected as the default rule in the workflow doc and reinforced in governance/handoff docs |
| Workflow supports supervision without repo access | PASS | Workflow plus supervision brief define the portable operating packet |
| First active role after init is the supervision layer | PASS | Explicitly stated in `./.suplex/docs/02_suplex_operating_workflow.md` and aligned in `./.suplex/handoffs/initialization.md` |
| Governance files remain aligned with the runtime layer | PASS | `./.suplex/AGENTS.md` and `./.suplex/CLAUDE.md` now include the reconstruction and portable-supervision rules |
| Handoff files remain aligned with the runtime layer | PASS | `./.suplex/handoffs/README.md`, `./.suplex/handoffs/templates/00_handoff_template.md`, and `./.suplex/handoffs/initialization.md` were updated narrowly to match runtime behavior |
| No computation-layer scaffolding was created | PASS | No new computation directories or files were added |
| No publication-layer scaffolding was created | PASS | No new publication directories or files were added |
| No March Madness-specific language was introduced | PASS | Wording remains template-generic |

## 2026-04-13 - Controlled Target-Repo Validation Pass

| Check | Result | Notes |
|---|---|---|
| Test A: greenfield target with `README.md` can receive only the SUPLEX control layer | PASS | `tmp_validation/testA_greenfield` contains only `README.md`, `SUPLEX.md`, and the canonical payload under `./.suplex/` after init simulation |
| Test A: no computation/publication scaffolding is created in greenfield init | PASS | No `src/`, `scripts/`, `data/`, `notebooks/`, `site/`, `public/`, or `.github/workflows/` were introduced in `tmp_validation/testA_greenfield` |
| Test A: first active layer after init is supervision, not execution | PASS | Confirmed by `./.suplex/docs/02_suplex_operating_workflow.md` and `./.suplex/handoffs/initialization.md` |
| Test B: overlay target preserves existing project structure | PASS | `tmp_validation/testB_overlay` retained preexisting `src/`, `data/`, `notebooks/`, and `site/` directories and their seed files |
| Test B: overlay init does not restructure or claim existing computation/publication-like directories | PASS | SUPLEX files were added alongside existing directories; no preexisting project directories were renamed, moved, deleted, or rewritten |
| Test C: supervision with repo access can rely on documented reconstruction modes | PASS | `./.suplex/docs/02_suplex_operating_workflow.md` explicitly distinguishes `full audit`, `local reconstruction`, and `no audit` |
| Test C: supervision with repo access produces a truthful current-state packet immediately after init | FAIL | In both initialized targets, copied `./.suplex/docs/00_project_scope.md` and `./.suplex/docs/09_supervision_brief.md` still described `suplex-template` rather than the target repo |
| Test D: supervision without repo access works from the portable packet alone | FAIL | The copied `./.suplex/docs/09_supervision_brief.md` was stale template state, so the packet was not sufficient without additional repo-access reconstruction |
| Test E: missing `README.md` halts initialization | PASS | `./.suplex/handoffs/initialization.md` prohibits silent continuation when `README.md` is missing, and no control layer was applied to `tmp_validation/testE_missing_readme` |
| Test E: missing `README.md` behavior asks for either a `README.md` or project description | PASS | `README.md`, `./.suplex/AGENTS.md`, and `./.suplex/docs/01_source_of_truth_and_provenance.md` all require halting and requesting the file or enough project description to draft one |
| Minimum correction for stale target-repo state is now documented | PASS | `README.md`, `./.suplex/docs/02_suplex_operating_workflow.md`, `./.suplex/docs/09_supervision_brief.md`, and `./.suplex/handoffs/initialization.md` now require rewriting copied repo-state docs during init |

## 2026-04-13 - Target-Repo Initialization Revalidation Pass

| Check | Result | Notes |
|---|---|---|
| Init behavior now requires rewriting the minimum target-state doc set before supervision bootstrap | PASS | `./.suplex/handoffs/initialization.md` and `./.suplex/docs/02_suplex_operating_workflow.md` now explicitly require rewriting `./.suplex/docs/00_project_scope.md`, `./.suplex/docs/08_status_checkpoint.md`, and `./.suplex/docs/09_supervision_brief.md` before supervision uses them |
| Test C: supervision with repo access produces a truthful current-state packet immediately after init | PASS | Fresh targets in `tmp_validation/reval_A_greenfield` and `tmp_validation/reval_B_overlay` have target-specific `./.suplex/docs/00_project_scope.md`, `./.suplex/docs/08_status_checkpoint.md`, and `./.suplex/docs/09_supervision_brief.md` after init simulation |
| Test D: supervision without repo access works from the portable packet alone | PASS | In both fresh targets, `./.suplex/docs/09_supervision_brief.md` plus `./.suplex/handoffs/initialization.md` and the latest `./.suplex/docs/08_status_checkpoint.md` form a truthful portable supervision packet without extra repo inspection |
| Spot check A: greenfield target with `README.md` still receives only the SUPLEX control layer | PASS | `tmp_validation/reval_A_greenfield` contains only `README.md`, `SUPLEX.md`, and the canonical payload under `./.suplex/` |
| Spot check A: greenfield init still adds no computation/publication scaffolding | PASS | No `src/`, `scripts/`, `data/`, `notebooks/`, `site/`, `public/`, or `.github/workflows/` were introduced in `tmp_validation/reval_A_greenfield` |
| Spot check B: overlay init still preserves existing project structure | PASS | `tmp_validation/reval_B_overlay` retained its preexisting `src/`, `data/`, `notebooks/`, and `site/` directories and seed files |
| Spot check B: overlay init still introduces no extra computation/publication scaffolding | PASS | The repair added only the control layer and target-state doc rewrites; no new project-architecture directories were introduced |
| Spot check E: missing `README.md` still halts initialization | PASS | `tmp_validation/reval_E_missing_readme` remained untouched and received no control-layer files |
| No computation/publication scaffolding was introduced by the repair pass | PASS | Validation targets remained limited to control-layer files plus the overlay target's preexisting directories |
