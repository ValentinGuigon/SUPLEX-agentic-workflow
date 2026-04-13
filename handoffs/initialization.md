Initialization prepares the SUPLEX control layer for a target repository.

Sources to read first:
- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `.suplex/init_state.yaml`
- relevant canonical docs already present in `docs/`, if any

Bounded objective:
1. confirm the `README.md` precondition
2. infer whether the repo is `greenfield` or `overlay`
3. infer whether the control profile is `lite`, `standard`, or `fullstack`
4. initialize or refine only the agentic control layer
5. rewrite copied repo-state docs so they truthfully describe the target repo rather than this template repo
6. complete that repo-state rewrite before supervision bootstrap or portable-packet use
7. prepare the repo for supervision bootstrap rather than direct execution
8. record bounded status and validation outcomes

Allowed changes:
- create or update control-layer docs
- create or update handoffs
- update `.suplex/init_state.yaml`
- record discrepancies and validation results

Prohibited changes:
- do not continue silently if `README.md` is missing
- do not scaffold computation, modeling, data, notebook, analysis, pipeline, publication, or deployment directories by default
- do not create `src/`, `scripts/`, `data/`, `notebooks/`, `site/`, `public/`, or `.github/workflows/` unless a later project-specific handoff explicitly justifies them
- do not restructure an existing repository during initialization

Required outputs:
- updated `.suplex/init_state.yaml`
- updated `docs/00_project_scope.md` if initialization learns more about the project
- updated `docs/01_source_of_truth_and_provenance.md`
- updated `docs/09_supervision_brief.md` if a portable supervision packet is needed for immediate handoff; it must not retain stale template-repo state
- updated `docs/08_status_checkpoint.md`
- updated `docs/validation_ledger.md`
- updated `docs/discrepancy_log.md` if any mismatch or blocker is found

Required repo-state rewrite before supervision bootstrap:
- `docs/00_project_scope.md` must be rewritten from the target repo's `README.md` and init findings so project identity, scope, and current task family are target-specific.
- `docs/08_status_checkpoint.md` must be rewritten so the latest checkpoint reflects the target repo's actual initialization pass rather than template history.
- `docs/09_supervision_brief.md` must be rewritten so the portable supervision packet reflects the target repo's current supervisory state.
- If any other copied state doc would still make the supervisory picture untruthful, rewrite that doc too before claiming init is complete.

Reporting requirements:
- summarize exactly what was updated
- list unresolved questions
- name the exact next bounded task
- state that the first active layer after init is supervision, not execution
- state explicitly that copied repo-state docs were rewritten or why initialization halted before they could be made truthful
- state explicitly which repo-state docs were rewritten during init
- state explicitly whether context can be cleared

Reminder:
- initialization must not create computation or publication layers by default
- initialization should leave the repo ready for supervision bootstrap and first bounded-task definition
