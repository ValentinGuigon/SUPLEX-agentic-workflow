# 10 Supervision Layer Spec

## Purpose

Define the stable duties, boundaries, inputs, and outputs of the supervision layer.

The supervision layer is responsible for bounded task selection, contract definition, acceptance criteria, review, and checkpointing.

It is not the default implementation layer.

## Core Responsibilities

The supervision layer must:
- reconstruct only the repo state needed for the current decision
- resolve whether an active bounded pass already exists before defining new work
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
- `handoffs/active/current_handoff.md` first
- `AGENTS.md`
- `docs/08_status_checkpoint.md`
- `docs/10_supervision_layer_spec.md`
- `docs/13_bounded_task_backlog.md`
- `docs/validation_ledger.md`
- `docs/discrepancy_log.md` when active mismatches exist
- in `standard` mode, the most recent relevant dated handoff and execution report
- in `sans-sucre` mode, `handoffs/active/current_execution_report.md` if an active pass is in flight or just completed
- any task-specific docs required by the active or proposed pass

If `handoffs/active/current_handoff.md` points to an unfinished pass, supervision should treat that handoff as the primary task-instruction artifact rather than infer a fresh task from repo context alone.

If the active handoff appears complete, supervision should read the matching latest execution report before deciding whether to review, checkpoint, close, or issue the next pass. In `standard` mode this is usually a dated report in `handoffs/history/`; in `sans-sucre` mode this is `handoffs/active/current_execution_report.md`.

When no active handoff exists, supervision should use `docs/13_bounded_task_backlog.md` as the default sequencing reference unless a blocker, discrepancy, or fresh validation result justifies a deviation.

## Required Outputs

For each bounded pass, the supervision layer must produce:
- in `standard` mode, one dated handoff packet in `handoffs/history/`
- one active handoff pointer at `handoffs/active/current_handoff.md`
- one explicit task family
- one explicit bounded deliverable
- acceptance criteria with pass/fail semantics
- a plain statement of what remains out of scope

In `sans-sucre` mode, the handoff may live only in `handoffs/active/current_handoff.md` and the paired live report may live only in `handoffs/active/current_execution_report.md`.

After reviewing the pass, the supervision layer must:
- decide whether the task family is closed
- update `docs/08_status_checkpoint.md` when validated project state changed
- update `docs/13_bounded_task_backlog.md` when pass ordering or completion status changed
- append to `docs/validation_ledger.md` when a pass produced actual validation evidence worth preserving
- log unresolved mismatches in `docs/discrepancy_log.md` when needed

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

If the answer to question 1 reveals a material blocker or ambiguity, supervision should also answer:
10. Does the user want to resolve this directly, or authorize best judgment?
11. If best judgment is authorized, what explicit assumption will be adopted and later reported back?

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

## Prohibited Behavior

The supervision layer should not:
- ask for broad open-ended work
- issue multiple unrelated deliverables in one pass
- delegate strategy to the execution layer
- silently make a user-owned material judgment call without first surfacing it and asking for a decision path
- treat chat history as canonical memory
- declare a system-ready state from one successful draft or one partial run
- silently change governance expectations without updating docs

When a pass is truly trivial and mechanically obvious, supervision may allow execution to offer a user-applied minimal-edit option instead of immediately editing files itself.

## Review Standard

The supervision layer should review the execution report by checking:
- whether the required execution-report artifact exists at the exact path named by the handoff
- whether the declared files read match the contract
- whether out-of-scope files stayed untouched
- whether every acceptance criterion is clearly pass or fail
- whether validation was actually performed rather than assumed
- whether "what was not done and why" is complete
- whether new discrepancies were recorded when needed

If the required execution-report artifact is missing, the pass should not be treated as complete even if repo-state edits appear coherent.

If any acceptance item fails, the pass should not be treated as complete.

## Escalation Conditions

The supervision layer should stop and return to planning when:
- source-of-truth docs conflict materially
- requested outputs do not match the artifact schema or handoff contract
- a pass would require redefining workflow behavior without doc updates
- the execution layer reports a blocker that changes scope or assumptions

## Learning Escalation Rule

When supervision identifies a repeated operational lesson that does not yet warrant stable governance change, it should require that the lesson be recorded in `docs/local_lessons.md`.

When supervision determines that a repeated lesson implies a change to stable governance, it should require a proposal in `docs/governance_update_proposals.md` rather than silently changing repo law.

Execution may record a repeated lesson in `docs/local_lessons.md` only when the handoff explicitly requires it or supervision directs it to do so.

## Handoff Discipline

The supervision layer communicates bounded work through handoff packets, not through ad hoc conversation alone.

The standard execution entry point is `handoffs/active/current_handoff.md`.

On startup, supervision should resolve task precedence in this order:
1. `handoffs/active/current_handoff.md`
2. the matching latest execution report if the active pass appears complete
3. canonical status, discrepancy, and backlog docs only after the active pass is resolved

The supervision layer should:
- write the dated handoff for the pass
- update `handoffs/active/current_handoff.md` as a compact pointer or summary to the active pass rather than a full duplicate of the dated handoff
- preserve prior dated handoffs and reports as history rather than overwriting them
- store reusable templates in `handoffs/templates/`
- put execution instructions into the handoff artifact before or instead of restating them in chat
- use chat only to confirm that the handoff was updated or to highlight blockers, not as the sole instruction channel
- in normal cases, confirm the updated artifact path and give a one-sentence operational summary rather than restating the full contract in chat

After a bounded pass is reviewed and accepted as complete, supervision should:
- in `standard` mode, leave the dated handoff and execution report in `handoffs/history/`
- remove the completed task contract from `handoffs/active/current_handoff.md`
- replace `handoffs/active/current_handoff.md` with an explicit no-active-handoff placeholder
- in `sans-sucre` mode, also clear or replace `handoffs/active/current_execution_report.md` so stale report content does not carry forward

Supervision should not formally accept, checkpoint-close, or phase-close a pass whose required execution report is missing, even if other closeout documents were updated.

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
- use terse field values where explanation is not needed
- keep explanatory prose for fields such as objective, purpose, ambiguity rationale, or other human-judgment context

Reading repo instructions and canonical docs without checking the active handoff is startup discipline only. It does not establish the bounded task by itself.

## Context-Clear Rule

The supervision layer may state that context can be cleared only when:
1. the bounded task family is closed
2. relevant docs are updated
3. unresolved issues are logged
4. outputs or diagnostics are saved
5. the next task family is different in kind
