# Discrepancy Log

Use this file to record operational mismatches, ambiguities, or conflicts that matter to bounded execution.

Suggested fields:
- date
- task family
- discrepancy
- impact
- current status
- next action

## Current status

| date | task family | discrepancy | impact | current status | next action |
|---|---|---|---|---|---|
| 2026-04-13 | `kernel_scaffold_packaging_pass` | The template repo now includes its own packaging `README.md`, which could be confused with the target repo's required seed `README.md` unless the distinction is made explicit. | Misreading the packaging README as initialization input could cause an incorrect future initialization pass. | Resolved. [E] | Keep the distinction explicit in template packaging docs and initialization behavior. [E] |
| 2026-04-13 | `controlled_target_repo_validation_pass` | Applying the current template by straight control-layer copy leaves repo-state docs such as `docs/00_project_scope.md` and `docs/09_supervision_brief.md` describing `suplex-template` instead of the target repo. | Supervision with repo access becomes inconsistent and the portable supervision packet is not trustworthy without extra reconstruction, which blocks safe first real-world use. | Resolved by revalidated init behavior. [E] | During target-repo init, rewrite `docs/00_project_scope.md`, `docs/08_status_checkpoint.md`, and `docs/09_supervision_brief.md` before supervision bootstrap or portable-packet use. [E] |
