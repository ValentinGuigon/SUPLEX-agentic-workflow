# Handoffs README

## Purpose of handoffs

Use `./.suplex/handoffs/` for bounded task packets that define execution scope, required outputs, non-scope, and closure conditions.
Handoffs support supervised runtime operation; they do not imply that every pass starts with a full repo audit.

## Layout

- `./.suplex/handoffs/active/current_handoff.md`: the standard execution entry point
- `./.suplex/handoffs/history/`: dated handoffs and dated execution reports in `standard` mode
- `./.suplex/handoffs/active/current_execution_report.md`: live execution report artifact in `sans-sucre` mode
- `./.suplex/handoffs/templates/`: reusable handoff templates, plus the execution-report template in `standard` mode
- `./.suplex/phases/`: optional phase artifacts in `standard` mode only, for multi-pass supervisory continuity rather than direct execution

## When a handoff is required

- before a new implementation phase
- before a bounded audit, classify, specify, validate, or checkpoint pass
- whenever the next unit of work needs an explicit execution boundary

## Naming convention

- use short, descriptive, lowercase filenames
- prefer underscores between words
- name the handoff after the bounded task family it governs

## Difference between handoffs and stable governance

- `./.suplex/AGENTS.md` and `./.suplex/CLAUDE.md` are stable SUPLEX governance files
- handoffs are bounded execution packets
- phases, when used in `standard` mode, are supervisory continuity charters for multi-pass objectives
- handoffs may change frequently; stable governance should not
- `./.suplex/docs/09_supervision_brief.md` is the portable state packet that lets supervision operate from the active handoff plus latest validated/report state when repo access is absent
- `./.suplex/docs/13_bounded_task_backlog.md` is the default next-task sequencing artifact only after any active handoff is resolved

## Reconstruction rule

- not every pass begins with a full repo audit
- each bounded pass should state whether it requires `full audit`, `local reconstruction`, or `no audit`
- the supervisor should reconstruct only what is necessary for the current decision

## Historical retention rule

- keep completed handoffs as historical records unless a user explicitly asks for cleanup
- treat a closed handoff as evidence of what a bounded pass was authorized to do
- in `standard` mode, every bounded pass should have one dated handoff and one dated execution report in `./.suplex/handoffs/history/`
- in `standard` mode, if a phase is opened, keep its records under `./.suplex/phases/` as continuity artifacts rather than mixing them into handoff history
- when a pass proceeds under user-authorized best judgment on a material ambiguity, record that decision path and the adopted assumption in the handoff itself

## Active-handoff closure rule

- after a bounded pass is reviewed and accepted, remove the completed contract from `./.suplex/handoffs/active/current_handoff.md`
- replace it with an explicit no-active-handoff placeholder so startup does not mistake a completed pass for unfinished work
- in `sans-sucre` mode, also clear or replace `./.suplex/handoffs/active/current_execution_report.md`
