# SUPLEX-agentic-workflow

`SUPLEX-agentic-workflow` installs the SUPLEX control layer into an existing repository.

Use it when you want to add a standard supervision and handoff structure for agentic work without changing the underlying architecture of the target project.

## What is SUPLEX

SUPLEX is a supervised pipeline with layered execution. It consists of a lightweight agentic control layer and is meant for AI-assisted bounded repository work. It provides governance files, canonical control-memory docs, and handoff structure so an agent can operate inside a repo with explicit scope, provenance, and closure rules.

SUPLEX separates the roles of goal-setting and decision-making (yours) from supervising and implementation (the models).

## What It Does

Running the bootstrap from inside a target repository adds the SUPLEX control layer:

- `AGENTS.md`
- `CLAUDE.md`
- `.suplex/init_state.yaml`
- `docs/`
- `handoffs/`
- `local_lessons.md`
- `governance_update_proposals.md`

The installed runtime includes:

- supervision and execution specs in `docs/10_supervision_layer_spec.md` and `docs/11_execution_layer_spec.md`
- a canonical backlog in `docs/13_bounded_task_backlog.md`
- an active handoff pointer in `handoffs/active/current_handoff.md`
- handoff and execution-report history in `handoffs/history/`
- reusable handoff and execution-report templates in `handoffs/templates/`

## Scope

SUPLEX init creates the supervision-execution layers, but it does not create or infer your project architecture. It does not add code, data, or source files.

Successful `suplex init` always installs the same full control layer. After initialization, `handoffs/active/current_handoff.md` starts as a no-active-handoff placeholder, so the first active layer is supervision. The first supervision pass should read that file first, inspect the repo if it has repo access, ask what you want to do next, and define exactly one bounded task.

If the repo was empty (SUPLEX as a greenfield), that first supervision pass will often need an architecture-planning or structure-confirmation step before implementation begins. If the repo was already populated with code, data, or source files (SUPLEX as an overlay), that first supervision pass should reconstruct enough of the current repo state to define the next bounded task safely. Architecting is an expected supervision escalation mode when structure decisions need to be made, not a permanent parallel role.

## Skills And Agents

SUPLEX is intended to sit above project-specific skills and agents as a control layer, not replace them.

If a target repository already contains skills, agents, or similar execution helpers, SUPLEX should usually preserve them as project-domain assets. Successful initialization adds only the SUPLEX control layer and does not restructure existing `src/`, `data/`, `notebooks/`, `site/`, `public/`, or similar project directories.

However, compatibility is not automatically seamless when the target repo already has its own governance layer. Initialization copies `AGENTS.md` and `CLAUDE.md`, merges `docs/` and `handoffs/`, and rewrites the target-state control docs that SUPLEX treats as canonical. In practice, this means there are likely collisions if the repo already uses root-level `AGENTS.md`, `CLAUDE.md`, `docs/`, or `handoffs/` for a different control system.

The integration model is:

- SUPLEX provides supervision, bounded-task definition, handoff discipline, validation, and checkpointing.
- project-specific skills provide reusable execution capabilities
- project-specific agents perform bounded execution work under SUPLEX supervision

So:

- adding SUPLEX to a repo that already has skills or agents is usually structurally compatible if those assets do not depend on conflicting root governance files
- adding skills or agents to a SUPLEX-managed repo is usually compatible if they are treated as project-domain components governed by the active handoff and stable SUPLEX rules
- layering SUPLEX on top of another repo-wide governance system with competing ownership of `AGENTS.md`, `CLAUDE.md`, `docs/`, or `handoffs/` should be treated as an explicit integration task as it will create collisions - SUPLEX overwriting the existing governance documents.

## Before You Run It

Run the bootstrap from inside the repository where you want SUPLEX installed.

Requirements:

- the target repository must already contain its own `README.md`
- Windows path: PowerShell with `Invoke-WebRequest` and `Expand-Archive`, plus Python 3 available via `py -3` preferred or `python` fallback
- POSIX path: `sh`, `curl` or `wget`, `unzip`, and Python 3 available via `python3` preferred or `python` fallback
- Python dependencies: none beyond the Python standard library

Windows users should normally use the PowerShell bootstrap. Use the POSIX bootstrap on Windows only if you are intentionally working inside a POSIX shell environment that already provides the required tools and a usable `python3`.

## Install

Use one of these commands from inside the repository where you want SUPLEX installed.

PowerShell on Windows:

```powershell
irm https://raw.githubusercontent.com/ValentinGuigon/SUPLEX-agentic-workflow/main/bootstrap/install.ps1 | iex
```

POSIX shell on macOS, Linux, or a real POSIX shell:

```sh
curl -fsSL https://raw.githubusercontent.com/ValentinGuigon/SUPLEX-agentic-workflow/main/bootstrap/install.sh | sh
```

The bootstrap looks for Python 3 automatically:

- PowerShell bootstrap tries `py -3` first, then `python`
- POSIX bootstrap tries `python3` first, then `python`
- if neither candidate can execute Python 3, the bootstrap stops with an explicit remediation message

## What Success Looks Like

After installation, the target repository should contain the SUPLEX control layer alongside the project's existing files.

At minimum, you should see:

- `AGENTS.md`
- `CLAUDE.md`
- `.suplex/`
- `docs/`
- `handoffs/`

The bootstrap then prints the ready message and the next supervision prompt.

## After Install

It is very likely that the first supervision pass suggests writing or revising documentation. Because files can be created or updated at each bounded task, it is useful to keep a clean baseline.

If the target repo is not already under version control, especially in a greenfield setup, it is good practice to initialize Git and commit the post-init state before running the first prompt:

```sh
git init
git add .
git commit -m "SUPLEX init"
```

## How To Use The Workflow

The repo is managed under a strict bounded task family discipline throughout construction:

- Each task enters through a handoff document in `handoffs/` with a defined scope, blocker list, acceptance criteria, and validation plan.
- Each bounded task returns an execution report describing what was read, what was done, what was not done, validation result, blockers, and the likely next bounded task.
- The workflow maintains canonical control-memory docs including the checkpoint, validation ledger, discrepancy log, and handoff history.
- Where provenance matters, project docs may tag claims with evidence level: `[E]` directly evidenced, `[I]` strong inference, `[U]` unresolved.
- No implementation proceeds without an active handoff document and evidence that the prior stage was validated.
- If canonical docs and code artifacts disagreed, the discrepancy is logged before proceeding. `docs/` is the canonical project memory; `handoffs/` define the execution boundary.

## Repository Layout

This repository is the distribution source for the installer.

- `bootstrap/`: install wrappers plus the Python initializer
- `template/`: the control-layer files copied into the target repository

The repository root is for packaging and distribution. The files that get installed into target repositories live under `template/`.

## Local Development Only

The commands below are for validating or testing the bootstrap from this checkout of `SUPLEX-agentic-workflow`. They are not the normal install path.

PowerShell local source:

```powershell
powershell -ExecutionPolicy Bypass -File .\bootstrap\install.ps1 -SourceRoot .
```

POSIX local source:

```sh
SUPLEX_SOURCE_ROOT="$(pwd)" sh ./bootstrap/install.sh
```
