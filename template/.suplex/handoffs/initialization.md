Initialization prepares the SUPLEX control layer for a target repository.

Sources to read first:
- `README.md`
- `SUPLEX.md`
- `./.suplex/AGENTS.md`
- `./.suplex/CLAUDE.md`
- `.suplex/init_state.yaml`
- `./.suplex/handoffs/active/current_handoff.md`
- relevant canonical docs already present in `./.suplex/docs/`, if any

Bounded objective:
1. confirm the `README.md` precondition
2. infer whether the repo is `greenfield` or `overlay`
3. install the same full SUPLEX agentic control layer in every successful init case
4. allow a thin bootstrap wrapper to fetch template assets temporarily from the project repo's `template/` payload without cloning the full project repo into the target repo
5. rewrite copied repo-state docs so they truthfully describe the target repo rather than this template repo
6. complete that repo-state rewrite before supervision bootstrap or portable-packet use
7. write `.suplex/init_state.yaml` for the initialized current working directory
8. print a ready message and the first supervision prompt
9. prepare the repo for supervision bootstrap rather than direct execution
10. record bounded status and validation outcomes

Allowed changes:
- create or update control-layer docs
- create or update handoffs
- create or update `SUPLEX.md`
- update `.suplex/init_state.yaml`
- record discrepancies and validation results

Prohibited changes:
- do not continue silently if `README.md` is missing
- do not scaffold computation, modeling, data, notebook, analysis, pipeline, publication, or deployment directories by default
- do not create `src/`, `scripts/`, `data/`, `notebooks/`, `site/`, `public/`, or `.github/workflows/` unless a later project-specific handoff explicitly justifies them
- do not restructure an existing repository during initialization
- do not let init decide the project architecture
- do not let init decide whether stronger workflow structure is needed beyond installing the full control layer

Required outputs:
- updated `.suplex/init_state.yaml`
- updated `SUPLEX.md` only if initialization semantics for the root entrypoint change
- updated `./.suplex/docs/00_project_scope.md` if initialization learns more about the project
- updated `./.suplex/docs/01_source_of_truth_and_provenance.md`
- updated `./.suplex/docs/09_supervision_brief.md` if a portable supervision packet is needed for immediate handoff; it must not retain stale template-repo state
- updated `./.suplex/docs/10_supervision_layer_spec.md` and `./.suplex/docs/11_execution_layer_spec.md` only if initialization semantics change in a way that affects runtime behavior
- updated `./.suplex/docs/08_status_checkpoint.md`
- updated `./.suplex/docs/13_bounded_task_backlog.md` only if the initialization result changes the default next-task sequencing rule
- updated `./.suplex/docs/validation_ledger.md`
- updated `./.suplex/docs/discrepancy_log.md` if any mismatch or blocker is found
- initialized `./.suplex/handoffs/active/current_handoff.md` in an explicit no-active-handoff state unless initialization is handing off directly into a dated bounded pass

Required repo-state rewrite before supervision bootstrap:
- `./.suplex/docs/00_project_scope.md` must be rewritten from the target repo's `README.md` and init findings so project identity, scope, and current task family are target-specific.
- `./.suplex/docs/01_source_of_truth_and_provenance.md` must be rewritten so the source hierarchy refers to the target repo's seed inputs and control-memory state rather than the template repo's packaging context.
- `./.suplex/docs/08_status_checkpoint.md` must be rewritten so the latest checkpoint reflects the target repo's actual initialization pass rather than template history.
- `./.suplex/docs/09_supervision_brief.md` must be rewritten so the portable supervision packet reflects the target repo's current supervisory state.
- If any other copied state doc would still make the supervisory picture untruthful, rewrite that doc too before claiming init is complete.

Reporting requirements:
- summarize exactly what was updated
- list unresolved questions
- name the exact next bounded task
- state that the first active layer after init is supervision, not execution
- state that supervision must read `./.suplex/handoffs/active/current_handoff.md` first, then `README.md`, inspect the repo if it can read repo files in the current session, otherwise use the portable supervision packet without guessing hidden state, ask the user what they want to do next, decide whether architecture planning is required, and propose exactly one next bounded task
- state that if no active handoff exists, supervision should use `./.suplex/docs/13_bounded_task_backlog.md` as the default sequencing reference unless a blocker or discrepancy justifies a deviation
- state explicitly that copied repo-state docs were rewritten or why initialization halted before they could be made truthful
- state explicitly which repo-state docs were rewritten during init
- state explicitly that the bootstrap staged template assets only temporarily and did not clone the template repo into the target repo
- state explicitly whether context can be cleared

Reminder:
- initialization must not create computation or publication layers by default
- initialization must install the same full SUPLEX agentic control layer in greenfield and overlay repos alike
- initialization should leave the repo ready for supervision bootstrap and first bounded-task definition
