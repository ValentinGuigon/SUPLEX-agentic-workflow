# Example Handoff

The following example shows the structure of a bounded handoff.

```md
# Portfolio Public Surface Implementation Pass

## Task Family

- Mode: `implement narrowly`
- Task name: `portfolio_public_surface_implementation_pass`

## Objective

- Add one dedicated public `Portfolio` page.
- Move portfolio out of `Technical Reports`.

## Verified Starting State

- [E] No top-level public `Portfolio` page exists in `site/`.
- [E] The navbar exposes `Technical Reports` but no standalone `Portfolio` item.

## Files to Read

- `site/_quarto.yml`
- `site/technical_reports.qmd`
- `./.suplex/docs/08_status_checkpoint.md`
- `./.suplex/docs/validation_ledger.md`

## Files Expected to Be Modified

- `site/_quarto.yml`
- `site/portfolio.qmd`
- `site/technical_reports.qmd`
- `./.suplex/docs/08_status_checkpoint.md`
- `./.suplex/docs/validation_ledger.md`

## Scope Constraints

Touch only:

- navbar placement
- portfolio page creation
- minimal copy or link updates needed to preserve the new boundary
- required control docs

Do not touch:

- underlying portfolio notebooks
- broad public-site redesign

## Deliverables

- one new top-level `Portfolio` page
- updated navbar placement
- updated checkpoint and validation docs

## Validation

- inspect navbar placement directly
- inspect the compiled `Portfolio` page directly
- confirm portfolio is no longer classified under `Technical Reports`
```
