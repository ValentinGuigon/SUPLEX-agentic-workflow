# Phase Document

Use terse field values where explanation is not needed.
Prefer exact nouns over explanation, lists over paragraphs, and only the information that changes supervisory decisions.
Keep explanatory prose for fields that benefit humans, such as `Purpose`, `Goal`, `Why A Phase Is Needed`, and ambiguity or gating rationale.

## Phase Metadata
- phase_id:
- title:
- status: proposed / active / blocked / complete / abandoned
- issued_by:
- date_opened:
- last_updated:
- mode: standard
- current_phase_sync: yes/no

## Role Routing
- phase_authoring_role: supervision
- execution_role: none for this artifact
- handoff_required_for_project_execution: yes
- execution_may_modify_this_phase: no

## Purpose
State why this phase exists now.

## Goal
State the multi-pass objective in one sentence.

## Why A Phase Is Needed
State why this objective should be governed across multiple bounded handoffs rather than handled as a single pass.

## Prerequisites
List any conditions that must already be true before this phase can begin.

## Phase Scope
List what kinds of work are inside this phase.

## Phase Non-Scope
List what is explicitly outside this phase.

## Default Source Of Truth
List the canonical docs and artifacts that define this phase.

## Allowed Artifact Zones
List the files or directories this phase may authorize handoffs to touch.

## Forbidden Artifact Zones
List nearby files or directories that no handoff in this phase may touch unless governance is revised.

## Gates
For each gate, record:
- gate_id:
- condition:
- required evidence:
- status: open / satisfied / waived
- notes:

## Completion Condition
State what must be true for the phase itself to be closed.

## Current Status Summary
State the current state of the phase in a few lines.

For `./.suplex/phases/active/current_phase.md`, keep this as a compact live summary and use the dated phase record as the canonical detailed phase plan.

## Next Expected Bounded Pass
State the next likely bounded handoff this phase should produce, if known.
If a direct user instruction asks supervision to write or update this phase, supervision may perform that governance artifact work directly when scope is clear. Execution still requires a separate active handoff.

## Phase Closeout Requirements
List the docs, records, and validations that must be updated before the phase is closed.

## Optional Extension Sections
Add any of the following when they materially improve continuity, validation, gating, or closure discipline:
- phase acceptance criteria
- validation requirements
- metrics or outcome targets
- resolved items
- unresolved items
- risks and ambiguities
- user decisions and adopted assumptions
- evidence discipline
- dependency notes
