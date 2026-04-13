# Handoff Template

## Handoff Metadata
- task_id:
- issued_by:
- date:
- task_family:
- current_handoff_sync: yes/no

## This Is The Only Task In This Pass

State the single bounded task in one sentence.

## Why Now

State why this pass exists and what dependency it resolves.

## Objective

State the exact bounded deliverable in one sentence.

## Hard Scope Constraints

Touch only:
- file or folder
- file or folder

Do not touch:
- file or folder
- file or folder

## Source Of Truth

List the canonical docs and artifacts the execution layer must follow.

## Files To Read

List the exact files the execution layer should read before acting.

## Files Expected To Be Modified

List the files that should normally change if the pass is completed cleanly.

## Blockers Or Ambiguities

List known ambiguities at handoff issuance time, or write `none at handoff issuance time`.

## Files In Scope

List the only files or folders the execution layer may modify.

## Files Out Of Scope

List nearby files or folders that must not be modified in this pass.

## Reconstruction Requirement

State whether this pass requires:
- full audit
- local reconstruction
- no audit

Explain why that level is sufficient.

## Execution Requirements

List the specific actions the execution layer must perform.

## Required Deliverables

List the outputs that must exist by the end of the pass.

## Validation Required

List the checks, dry runs, or evidence the execution layer must produce.

## Immediate Next Action

State what the execution layer should do immediately after reading and restating the handoff.
This should remove ambiguity between startup alignment and actual execution.

## Most Likely Misread

State the most likely wrong interpretation of the task.

## Guardrail Against Misread

State the sentence or rule that prevents that interpretation.

## Acceptance Criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Stop Conditions

List the conditions under which the execution layer must stop and report rather than improvise.

## Escalate If

List the blockers that require supervision to redefine scope or strategy.

## Docs To Update If Changed

List the docs that must be updated if the pass changes workflow behavior, status, or artifact expectations.

## Execution Report Path

State where the execution layer should write its report for this pass.

## Current Handoff Update

State how `handoffs/active/current_handoff.md` should reference this handoff.

## End-Of-Pass Report

State the exact sections or reminders the execution report should include if this pass needs special reporting discipline.

## Completion Rule

State explicitly that reading the handoff and restating scope are startup steps, not completion, unless that is the bounded deliverable.
