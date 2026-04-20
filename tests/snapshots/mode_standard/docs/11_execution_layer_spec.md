# 11 Execution Layer Spec

## Purpose

Define the stable duties, boundaries, inputs, and outputs of the execution layer.

The execution layer performs one bounded pass at a time inside the repo.
It executes the active contract, validates its work, records evidence, and stops at the task boundary.

It is not the default planning or governance layer.

## Core Responsibilities

The execution layer must:
- read the minimum files required by the active handoff
- restate the task family, exact deliverable, scope, and validation plan before substantial work
- treat that restatement as startup discipline rather than task completion
- change only the files explicitly in scope
- perform the bounded task without broadening scope
- validate its result before claiming completion
- produce a structured execution report
- record discrepancies instead of silently redesigning workflow or governance

## Required Inputs

Before acting, the execution layer should read:
- `AGENTS.md`
- `handoffs/active/current_handoff.md`
- `docs/11_execution_layer_spec.md`
- only the additional files explicitly named by the active handoff or required by the bounded task

If `handoffs/active/current_handoff.md` points to a dated handoff, that dated handoff is the active contract.

If chat instructions conflict with the active handoff, stop and surface the mismatch rather than choosing implicitly.

The execution layer should not read the entire repo by default.

## Mandatory Startup Restatement

Before substantial work, the execution layer must make explicit:
1. task family
2. exact deliverable in one sentence
3. files in scope
4. files out of scope
5. validation that will be performed
6. any blocker or ambiguity already visible from the contract
7. any user-authorized best-judgment assumption recorded in the handoff

Reading the handoff, listing scope, and stating alignment do not complete the pass by themselves.

## Evidence Discipline

When the handoff or task type requires source grounding, the execution layer should:
- say when it is uncertain instead of guessing
- quote or extract the relevant source text before analyzing it when the task depends on documents
- tie factual claims to cited repo artifacts or quoted passages
- state assumptions and evidence basis before conclusions when reasoning quality matters
- stay within the named materials unless the handoff explicitly allows broader knowledge

These rules are especially appropriate for:
- `audit`
- `classify`
- `validate`
- discrepancy review
- long-document analysis
- source-of-truth comparisons

These rules should not be imposed mechanically on every narrow implementation pass when they add noise without improving accuracy.

## Required Outputs

Each bounded pass should leave behind:
- the in-scope repo changes
- in `standard` mode, one execution report in `handoffs/history/`
- in `sans-sucre` mode, one live execution report in `handoffs/active/current_execution_report.md`
- validation notes or artifacts sufficient to support supervisory review
- doc updates required by the handoff when workflow behavior, status, or mismatches changed

Only passes that actually produce validation evidence should expect an entry in `docs/validation_ledger.md`.

The required execution report is a mandatory output artifact, not an optional chat summary.
A pass is not complete until the report exists at the exact path required by the active handoff.

If the pass updates closeout state such as `handoffs/active/current_handoff.md`, `phases/active/current_phase.md`, or checkpoint docs that imply completion, the execution layer must still ensure the required report artifact is written before claiming success.

## Mandatory Operating Rules

During execution, the layer must:
- preserve the stated task family
- avoid adjacent helpful changes
- continue from alignment into the bounded deliverable unless a stop condition or blocker is reached
- stop and report blockers instead of substituting a lossy alternative
- treat validation as part of completion, not optional follow-up
- treat report writing as part of completion, not optional follow-up
- write the required execution report before ending the pass in chat
- avoid redefining the task into an easier nearby task

Examples:
- In an `audit` pass, the deliverable is the actual comparison and recorded verdicts, not only a summary that the audit criteria were read.
- In a `specify` pass, the deliverable is the requested contract, recommendation set, or decision document, not only alignment language.
- In an `implement narrowly` pass, the deliverable is the bounded implementation plus the required validation, not only partial edits.
- In a `checkpoint` pass, the deliverable is the updated canonical state record, not only a claim that state was reviewed.

## Minimal-Edit Exception

The default rule is that the execution layer performs the bounded edits itself.

As a narrow exception, if the required change is minimal, mechanically obvious, low-risk, and easy for the user to apply directly, the execution layer may present the exact edit instructions and ask whether the user prefers to make the change manually.

This exception should be used only when:
- the edit is very small in scope
- the required change can be specified exactly
- little or no validation is needed
- asking the user is cheaper and clearer than running a full execution cycle

The execution layer should not use this exception to avoid substantive bounded work.

If the user does not want to apply the change manually, the execution layer should perform the edit itself.

## Report Format

Every execution report should include:
1. files read
2. files created
3. files modified
4. exact work completed
5. validation performed
6. acceptance-criteria verdict
7. what was not done and why
8. discrepancies found
 9. any material assumption used under user-authorized best judgment
 10. recommended next task family
 11. context-clear assessment

If any acceptance item failed, the report should say so explicitly.

## Prohibited Behavior

The execution layer should not:
- redefine the task
- broaden scope without authorization
- modify governance docs unless explicitly instructed
- claim success without validation
- leave silent scope shrinkage
- declare system-level readiness from one bounded pass
- use chat as a substitute for the required execution report
- leave the required execution-report artifact unwritten while presenting the pass as complete
- clear or replace active-pass artifacts in a way that implies closure while the required execution report is still missing
- silently resolve source-of-truth conflicts by choosing one side

## Default Stop Conditions

The execution layer should stop and report when:
- the requested task requires files outside approved scope
- source-of-truth docs disagree materially
- the deliverable cannot be completed without changing governance or schema
- validation fails
- a blocker requires supervision to choose between multiple strategies
- chat instructions and the active handoff conflict materially
- the active handoff is missing, stale, or ambiguous enough that scope cannot be determined safely

## Validation Standard

Validation should be appropriate to the task family.

Examples:
- `audit`: verify current state against named files
- `implement narrowly`: run the narrowest relevant check, dry run, or direct verification
- `validate`: record direct evidence and verdict
- `checkpoint`: confirm docs reflect actual repo state

Prefer direct evidence over narrative assurance.

## Relationship To Project Memory

The execution layer contributes to project memory but does not define system law.

Repeated operational lessons should go to `docs/local_lessons.md` only when explicitly instructed or when the handoff requires it.

Stable governance changes should be proposed, not silently embedded.
