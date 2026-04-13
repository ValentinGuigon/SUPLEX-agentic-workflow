# SUPLEX-agentic-workflow

`SUPLEX-agentic-workflow` installs the SUPLEX control layer into an existing repository.

Use it when you want to add a standard supervision and handoff structure for agentic work without changing the underlying architecture of the target project.

## What is SUPLEX

SUPLEX is a supervised pipeline with layered execution. It consists in a lightweight agentic control layer and is purposed for AI-assisted bounded repository work. It provides governance files, canonical control-memory docs, and handoff structure so an agent can operate inside a repo with explicit scope, provenance, and closure rules.

SUPLEX separates the roles of goal-setting and decision-making (yours) from supervising and implementation (the models’).

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

SUPLEX init creates the supervision-execution layers, but it does not create or infer your project architecture. It does not add code, data or source files.

Successful `suplex init` always installs the same full control layer. After initialization, provide the first instruction to the supervisor to start working on your project.

If the repo was empty (SUPLEX as a 'greenfield'), you might need to interact with a Supervisor ("You are the supervisor") and an Architect ("You are the architect) to define your architectural needs. If the repo was already populated with code, data or source files (SUPLEX as an 'overlay'), you can start interacting with a Supervisor directly by defining your next goal.

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
