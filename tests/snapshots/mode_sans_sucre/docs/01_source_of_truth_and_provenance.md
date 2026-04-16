
# 01 Source of Truth and Provenance

Use this file to track what currently counts as source material, what is inferred, and what remains unresolved for `Mode Sans Sucre`n`nSans-sucre mode validation target.`.

## Evidence tag definitions

- `[E]` directly evidenced from repo artifacts or canonical docs
- `[I]` strong inference from those artifacts
- `[U]` unresolved / uncertain

## Tier 1 canonical sources

- The target repo's `README.md` is the mandatory seed specification input for initialization. [E]
- After initialization, repo-local canonical control memory lives in `docs/`. [E]
- If the target repo's `README.md` is missing, initialization must halt and request either the file itself or enough project description to draft it first. [E]

## Tier 2 derived control artifacts

- `AGENTS.md` and `CLAUDE.md` define stable governance for bounded agentic execution. [E]
- `docs/00_project_scope.md`, `docs/08_status_checkpoint.md`, `docs/09_supervision_brief.md`, `docs/validation_ledger.md`, and `docs/discrepancy_log.md` are control-memory artifacts derived during initialization. [E]
- `handoffs/` artifacts define bounded execution packets and remain subordinate to stable governance. [E]

## Tier 3 controlled support artifacts if any

- `.suplex/init_state.yaml` is internal system state maintained by the control layer. [E]

## Source hierarchy rules

- The target repo's `README.md` remains the first source for initialization and later reconstruction. [E]
- Repo-local canonical docs in `docs/` take precedence over stale assumptions once they are rewritten during initialization. [E]
- Handoffs constrain execution scope but do not override stable governance. [E]

## Unresolved provenance questions

1. [U] Which project-specific documents beyond `README.md` should be promoted to canonical sources during supervision bootstrap?
2. [U] Whether this repo will later require compiled validation conventions beyond the default validation ledger.
