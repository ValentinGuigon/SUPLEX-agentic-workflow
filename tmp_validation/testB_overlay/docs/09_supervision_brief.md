# 09 Supervision Brief

## 1. Purpose of the supervision brief

This file is the portable supervision packet for cases where the supervisor does not have direct repository access. It captures the minimum current-state information needed to govern the next bounded decision.

## 2. How this file should be used

- Read this file together with the active handoff and the latest execution report or status checkpoint.
- Use it to decide the next bounded supervisory action without assuming unseen repo context.
- Refresh it whenever supervision-relevant state changes materially.

## 3. Project identity

- Project: `suplex-template`
- Purpose: reusable SUPLEX control-layer scaffold for bounded agentic work
- Scope boundary: control-layer runtime and governance only; no computation or publication scaffolding by default

## 4. SUPLEX workflow summary

- SUPLEX runs as a supervised bounded-pass system.
- The first active layer after initialization is supervision.
- Each pass does not require a full audit by default.
- Reconstruction level must be chosen explicitly as one of:
  - full audit
  - local reconstruction
  - no audit
- Execution is bounded by handoffs and closes through validation and checkpointing.

## 5. Current bounded task family

- Task family: add the missing SUPLEX runtime workflow layer to the template
- Active mode set: `implement narrowly`, `validate`, `checkpoint`

## 6. Active source-of-truth rule

- `docs/` is canonical control memory.
- `handoffs/` defines bounded execution packets.
- Stable governance remains in `AGENTS.md` and `CLAUDE.md`.
- Handoffs constrain execution but do not override stable governance.

## 7. Active handoff summary

- The current runtime-layer pass added `docs/02_suplex_operating_workflow.md` as the runtime workflow document.
- The current runtime-layer pass added `docs/09_supervision_brief.md` as the portable supervision-state artifact.
- Governance and handoff files were aligned only where required by the runtime layer.
- The bounded pass did not broaden into computation scaffolding, publication scaffolding, or project-specific initialization logic.

## 8. Latest validated state

- The template already contains the governance kernel, canonical control-memory docs, handoff structure, and initialization state.
- The runtime operating protocol for post-init supervision and bounded execution is now documented.
- The template now distinguishes `full audit`, `local reconstruction`, and `no audit`.
- The template now includes a portable supervision packet for cases where the supervisor lacks repo access.

## 9. Latest execution report summary

- The runtime-layer pass added the workflow document and portable supervision brief.
- Governance and handoff docs were updated narrowly to align with reconstruction modes, supervision bootstrap, and non-repo-access supervision.
- Validation passed against the bounded acceptance criteria without adding computation or publication scaffolding.

## 10. Open discrepancies / blockers

- No open blocker remains inside the runtime layer itself.
- Future downstream validation is still needed when the template is extracted or applied to a target repository.

## 11. Exact next supervisory decision

- Decide whether to validate the runtime-enabled template in extracted standalone form or during first application to a target repository.

## 12. Update rule

- Refresh this file whenever the active handoff, latest validated state, latest execution report summary, blockers, or exact next supervisory decision changes materially.
- The supervisor or the executor acting under an explicit documentation step may update it.
- `docs/08_status_checkpoint.md` remains the fuller validated checkpoint record; this file is the portable supervisory state packet derived from that checkpoint and the active handoff.
