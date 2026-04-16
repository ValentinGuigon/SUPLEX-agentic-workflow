# SUPLEX Template

SUPLEX is a lightweight agentic control layer for bounded repository work. It provides governance files, canonical control-memory docs, and handoff structure so an agent can operate inside a repo with explicit scope, provenance, and closure rules.

This repository is a reusable template for that control layer only. It is not a computation scaffold, publication scaffold, modeling scaffold, or project starter kit. It does not create `src/`, `scripts/`, `data/`, `notebooks/`, `site/`, `public/`, or workflow directories by default.

## What this template contains

- stable governance files for agent behavior
- canonical control-memory docs under `docs/`
- runtime operating workflow and portable supervision-state docs under `docs/`
- bounded task-family entry points under `handoffs/`
- internal initialization state under `.suplex/`

## What this template does not do

- initialize a target project by itself
- infer domain architecture from this template alone
- prescribe application, analysis, modeling, or publication structure
- replace the target repo's own project documentation

## README precondition for target repos

This template repo has its own human-facing `README.md` so the template can stand alone as a repository.

That file is not the seed specification for a future target repo.

When SUPLEX is applied to another repository, the target repository must already have its own `README.md`, or enough project description must be provided to draft one first. Initialization should halt if that seed input is missing.

## High-level initialization model

1. Start in the target repo, not in this template repo.
2. Confirm that the target repo has a usable `README.md` describing the project.
3. Copy or apply the SUPLEX control-layer files into that target repo.
4. Use the target repo's `README.md` as the first seed input for bounded initialization.
5. Bootstrap supervision first, then derive the first bounded execution task from that target-repo context without scaffolding computation or publication layers by default.

## Runtime layer

- `docs/02_suplex_operating_workflow.md` defines how SUPLEX runs after initialization.
- `docs/09_supervision_brief.md` is the portable supervision packet for cases where the supervisor does not have repo access.
- SUPLEX distinguishes `full audit`, `local reconstruction`, and `no audit`; full audit is not mandatory at every pass.

## Current status

This template now includes both the governance kernel and the runtime workflow layer, and is intended to be moved or extracted into its own standalone repository once downstream application validation is completed.
