# 01 Source of Truth and Provenance

Use this file to track what currently counts as source material, what is inferred, and what remains unresolved.

## Evidence tag definitions

- `[E]` directly evidenced from repo artifacts or canonical docs
- `[I]` strong inference from those artifacts
- `[U]` unresolved / uncertain

## Tier 1 canonical sources

- The target repo's `README.md` is the mandatory seed specification input for initialization. [E]
- This template repo's own `README.md` is packaging documentation for the standalone template repository. It is not the target-repo seed specification. [E]
- After initialization, repo-local canonical control memory lives in `docs/`. [E]
- If the target repo's `README.md` is missing, initialization must halt and request either the file itself or enough project description to draft it first. [E]

## Tier 2 derived control artifacts

- `AGENTS.md` and `CLAUDE.md` define stable governance for bounded agentic execution. [E]
- `docs/00_project_scope.md` records the scoped purpose of the SUPLEX layer. [E]
- `docs/08_status_checkpoint.md`, `docs/validation_ledger.md`, and `docs/discrepancy_log.md` are derived control-memory artifacts rather than project-domain sources of truth. [E]
- `handoffs/` artifacts define bounded execution packets and are historical records once closed. [E]

## Tier 3 controlled support artifacts if any

- `.suplex/init_state.yaml` is internal system state maintained by the control layer. [E]
- Additional support artifacts may be introduced later only when a bounded handoff justifies them explicitly. [I]

## Source hierarchy rules

- The target repo's `README.md` is the required first source for initialization. [E]
- If later canonical docs in `docs/` refine or supersede earlier assumptions, the explicit canonical doc layer takes precedence. [I]
- Handoffs constrain execution scope but do not override stable governance. [E]
- Internal state files inform agent behavior but do not replace canonical prose docs. [E]

## Inference rules

- Use `[I]` only when a conclusion is strongly supported by repo structure, explicit documentation, or linked artifacts. [E]
- Do not infer computation architecture, publication architecture, or artifact contracts from filenames alone. [E]
- Infer `overlay` when the repo already contains substantive code, docs, notebooks, data, app, site, or publication structure. [E]
- Infer `greenfield` only when the repo is empty or near-empty aside from basic repo metadata. [E]
- Infer `fullstack` only when SUPLEX is wrapping an already substantial computation and/or publication system. [E]
- Workflow profile changes control-layer strictness only; it does not justify computation or publication scaffolding. [E]

## Unresolved provenance questions

1. [U] Which project-specific documents beyond the target repo's `README.md` should become Tier 1 canonical sources in a given overlay repo?
2. [U] Whether a later bounded pass warrants an explicit artifact-schema document.
3. [U] Whether the wrapped repo requires compiled validation conventions beyond the default validation ledger.

## Downstream artifact dependency rules

- `docs/00_project_scope.md` should derive from `README.md` and any approved canonical project inputs. [E]
- `docs/08_status_checkpoint.md` should derive from actual bounded-pass work performed in the repo. [E]
- `docs/validation_ledger.md` should derive from concrete bounded-pass acceptance checks. [E]
- `docs/discrepancy_log.md` should derive from operational mismatches actually observed. [E]
- SUPLEX does not define computation architecture unless a separate bounded handoff and canonical decision explicitly add that responsibility. [E]
