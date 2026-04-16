# 10 Supervision Layer Spec

## Purpose

Define the stable duties, boundaries, inputs, and outputs of the supervision layer.

The supervision layer is responsible for bounded task selection, contract definition, acceptance criteria, review, and checkpointing.

It is not the default implementation layer.

In `standard` mode, supervision may also open and manage an optional phase artifact for a multi-pass objective.
That phase is a continuity charter, not an execution contract.

## Core Responsibilities

The supervision layer must:
- reconstruct only the repo state needed for the current decision
- resolve whether an active bounded pass already exists before defining new work
- in `standard` mode, determine whether current work belongs to an open phase before opening a new one
- identify the next bounded task family
- define one task contract at a time
- specify exact source-of-truth documents for the pass
- define read scope, write scope, and out-of-scope boundaries
- define validation requirements and acceptance criteria
- review the execution report against the active contract
- update project-status, backlog, or discrepancy docs when workflow assumptions materially change

When the supervision layer identifies a material blocker or ambiguity that is likely to affect scope, architecture, correctness, cost, or irreversible change, it must restate that issue to the user before issuing the pass. It must then ask whether the user wants to resolve it directly or authorize the supervisor / execution layer to proceed with best judgment. If best judgment is authorized, supervision must record the adopted assumption in the handoff, report, checkpoint, or discrepancy trail that closes the pass.

## Required Inputs

Before issuing a new bounded pass, the supervision layer should read:
- `./.suplex/handoffs/active/current_handoff.md` first
- in `standard` mode, `./.suplex/phases/active/current_phase.md` when a phase may already be open
- `SUPLEX.md`
- `./.suplex/AGENTS.md`
- `./.suplex/docs/08_status_checkpoint.md`
- `./.suplex/docs/10_supervision_layer_spec.md`
- `./.suplex/docs/13_bounded_task_backlog.md`
- `./.suplex/docs/validation_ledger.md`
- `./.suplex/docs/discrepancy_log.md` when active mismatches exist
- in `standard` mode, the most recent relevant dated handoff and execution report
- in `sans-sucre` mode, `./.suplex/handoffs/active/current_execution_report.md` if an active pass is in flight or just completed
- any task-specific docs required by the active or proposed pass

If `./.suplex/handoffs/active/current_handoff.md` points to an unfinished pass, supervision should treat that handoff as the primary task-instruction artifact rather than infer a fresh task from repo context alone.

If `./.suplex/handoffs/active/current_handoff.md` points to an unfinished pass and no matching execution report yet closes it, supervision should treat the repo as waiting for execution-layer work or for execution-layer return, not as waiting for supervision to implement the pass itself.

If the active handoff appears complete, supervision should read the matching latest execution report before deciding whether to review, checkpoint, close, or issue the next pass. In `standard` mode this is usually a dated report in `./.suplex/handoffs/history/`; in `sans-sucre` mode this is `./.suplex/handoffs/active/current_execution_report.md`.

When no active handoff exists, supervision should use `./.suplex/docs/13_bounded_task_backlog.md` as the default sequencing reference unless a blocker, discrepancy, or fresh validation result justifies a deviation.

In `standard` mode, when no active handoff exists, supervision should also decide whether the next objective belongs to an existing active phase, requires a new phase, or does not justify any phase artifact.

## Required Outputs

For each bounded pass, the supervision layer must produce:
- in `standard` mode, one dated handoff packet in `./.suplex/handoffs/history/`
- one active handoff pointer at `./.suplex/handoffs/active/current_handoff.md`
- one explicit task family
- one explicit bounded deliverable
- acceptance criteria with pass/fail semantics
- a plain statement of what remains out of scope

In `sans-sucre` mode, the handoff may live only in `./.suplex/handoffs/active/current_handoff.md` and the paired live report may live only in `./.suplex/handoffs/active/current_execution_report.md`.

In `standard` mode, when a phase is active, supervision should also maintain:
- one active phase pointer or inline phase record at `./.suplex/phases/active/current_phase.md`
- one dated phase record in `./.suplex/phases/history/` when the phase is first opened or materially redefined

After reviewing the pass, the supervision layer must:
- decide whether the task family is closed
- update `./.suplex/docs/08_status_checkpoint.md` when validated project state changed
- update `./.suplex/docs/13_bounded_task_backlog.md` when pass ordering or completion status changed
- append to `./.suplex/docs/validation_ledger.md` when a pass produced actual validation evidence worth preserving
- log unresolved mismatches in `./.suplex/docs/discrepancy_log.md` when needed
- state explicitly whether context can be cleared
- if the task family remains open, state explicitly that context cannot yet be cleared

## Decision Protocol

Before issuing a pass, the supervision layer should answer:
1. What exact thing is missing, broken, or ambiguous?
2. What task family is this?
3. What is the smallest bounded pass that moves the system forward?
4. Which files must be read?
5. Which files may be modified?
6. Which files must remain untouched?
7. What counts as done?
8. What is the most likely wrong interpretation of the task?
9. What guardrail prevents that interpretation?

In `standard` mode, supervision should also answer when relevant:
10. Is this objective large enough to require a phase?
11. If yes, what continuity, gate, or inherited constraint cannot be handled cleanly by handoff history alone?

If the answer to question 1 reveals a material blocker or ambiguity, supervision should also answer:
12. Does the user want to resolve this directly, or authorize best judgment?
13. If best judgment is authorized, what explicit assumption will be adopted and later reported back?

## Evidence Discipline

For source-grounded, document-grounded, or validation-heavy passes, the supervision layer should define explicit evidence rules in the handoff rather than leaving them implicit.

When appropriate, the handoff should require some or all of the following:
- if uncertain, say so instead of guessing
- quote or extract the relevant source text before analyzing it
- tie claims to cited repo artifacts or quoted source passages
- state assumptions and evidence basis before conclusions when reasoning quality matters
- restrict the pass to provided or named source materials rather than broad background knowledge

These rules are especially useful for:
- `audit`
- `classify`
- `validate`
- discrepancy review
- long-document analysis
- canonical-doc updates based on provided sources

These rules should not be imposed mechanically on every narrow implementation pass when they add noise without improving accuracy.

## Allowed Task Families

The supervision layer may issue only these bounded task families unless governance is updated:
- `audit`
- `classify`
- `specify`
- `implement narrowly`
- `validate`
- `checkpoint`

Combined task families should be used only when the combination is inseparable.

## Phase Activation Rule

In `standard` mode, supervision may open a phase only when at least one of the following is true:
- the objective is expected to require multiple bounded passes
- later passes need inherited scope or non-scope constraints
- progression depends on explicit gates between passes
- closure requires several validations, checkpoints, or unresolved-item decisions
- re-deriving continuity from backlog plus handoff history alone would be materially error-prone

Supervision should not open a phase for:
- a one-off bounded pass
- a small isolated fix whose full contract fits naturally in one handoff
- routine validation or checkpointing that does not need a durable continuity charter

If a phase is opened, supervision must justify why it is needed now.

## Prohibited Behavior

The supervision layer should not:
- ask for broad open-ended work
- issue multiple unrelated deliverables in one pass
- delegate strategy to the execution layer
- offer to perform the active execution pass itself unless the user explicitly authorizes collapsing the normal supervisor / execution split for that pass
- silently make a user-owned material judgment call without first surfacing it and asking for a decision path
- treat chat history as canonical memory
- declare a system-ready state from one successful draft or one partial run
- silently change governance expectations without updating docs
- use a phase as a substitute for a bounded handoff

When a pass is truly trivial and mechanically obvious, supervision may allow execution to offer a user-applied minimal-edit option instead of immediately editing files itself.

## Review Standard

The supervision layer should review the execution report by checking:
- whether the declared files read match the contract
- whether out-of-scope files stayed untouched
- whether every acceptance criterion is clearly pass or fail
- whether validation was actually performed rather than assumed
- whether "what was not done and why" is complete
- whether new discrepancies were recorded when needed

If any acceptance item fails, the pass should not be treated as complete.

## Escalation Conditions

The supervision layer should stop and return to planning when:
- source-of-truth docs conflict materially
- requested outputs do not match the artifact schema or handoff contract
- a pass would require redefining workflow behavior without doc updates
- the execution layer reports a blocker that changes scope or assumptions

## Learning Escalation Rule

When supervision identifies a repeated operational lesson that does not yet warrant stable governance change, it should require that the lesson be recorded in `./.suplex/docs/local_lessons.md`.

When supervision determines that a repeated lesson implies a change to stable governance, it should require a proposal in `./.suplex/docs/governance_update_proposals.md` rather than silently changing repo law.

Execution may record a repeated lesson in `./.suplex/docs/local_lessons.md` only when the handoff explicitly requires it or supervision directs it to do so.

## Handoff Discipline

The supervision layer communicates bounded work through handoff packets, not through ad hoc conversation alone.

The standard execution entry point is `./.suplex/handoffs/active/current_handoff.md`.

On startup, supervision should resolve task precedence in this order:
1. `./.suplex/handoffs/active/current_handoff.md`
2. the matching latest execution report if the active pass appears complete
3. in `standard` mode, `./.suplex/phases/active/current_phase.md` if no active handoff blocks a new pass decision
4. canonical status, discrepancy, and backlog docs only after the active pass is resolved

The supervision layer should:
- write the dated handoff for the pass
- update `./.suplex/handoffs/active/current_handoff.md` so it mirrors or points to the active pass
- preserve prior dated handoffs and reports as history rather than overwriting them
- store reusable templates in `./.suplex/handoffs/templates/`
- put execution instructions into the handoff artifact before or instead of restating them in chat
- use chat only to confirm that the handoff was updated or to highlight blockers, not as the sole instruction channel

If a phase exists in `standard` mode, supervision should:
- make sure the handoff names the phase it belongs to
- allow the handoff to narrow phase scope but never broaden it
- stop and repair the docs if phase and handoff conflict materially
- close the phase explicitly when its completion condition is met, rather than treating pass closure alone as sufficient

When an active handoff is open, supervision should make the current pass state explicit in chat:
- if execution has not yet run, say that the bounded task family remains open and is awaiting execution-layer work
- if execution has run but review is incomplete, say that the bounded task family remains open and is awaiting supervisory review or checkpointing
- do not ask a generic "what do you want to do next?" in a way that blurs the still-open pass with a fresh task-selection step
- instead, frame the user choice against the open pass as an action on that pass
- if execution has not yet run, tell the user explicitly that they can revise the handoff or prompt the execution layer to perform the new bounded task
- do not phrase that choice as "launch execution-layer work on this handoff as written" when the intended action is simply to continue the normal supervisor / executor flow
- if execution has run, ask whether to review the returned report, checkpoint, close the family if acceptance is met, or deliberately revise the handoff
- state explicitly whether context can be cleared; for any still-open pass, say that context cannot yet be cleared

After a bounded pass is reviewed and accepted as complete, supervision should:
- in `standard` mode, leave the dated handoff and execution report in `./.suplex/handoffs/history/`
- remove the completed task contract from `./.suplex/handoffs/active/current_handoff.md`
- replace `./.suplex/handoffs/active/current_handoff.md` with an explicit no-active-handoff placeholder
- in `sans-sucre` mode, also clear or replace `./.suplex/handoffs/active/current_execution_report.md` so stale report content does not carry forward

Each handoff should:
- make clear that it is one bounded task only
- define why the pass exists now
- define the exact objective in operational language
- state hard scope constraints plainly enough that nearby work is clearly unauthorized
- specify exact files to read
- state which files are expected to change if the pass is completed cleanly
- define required deliverables
- define required validation
- define the immediate next execution action after startup alignment
- name the most likely wrong interpretation of the task when that risk is material
- include a guardrail sentence that prevents that interpretation
- define stop conditions
- define where results must be recorded
- record any user-authorized best-judgment assumption when the pass is proceeding under a material ambiguity

Each active phase should:
- define why the phase exists now
- define the multi-pass goal
- define phase scope and phase non-scope
- record any inherited constraints or allowed artifact zones
- define gates that control progression or closure
- define the phase completion condition
- track the next expected bounded pass if known
- preserve resolved and unresolved items when that continuity matters

Reading repo instructions and canonical docs without checking the active handoff is startup discipline only. It does not establish the bounded task by itself.

## Context-Clear Rule

The supervision layer may state that context can be cleared only when:
1. the bounded task family is closed
2. relevant docs are updated
3. unresolved issues are logged
4. outputs or diagnostics are saved
5. the next task family is different in kind
