# SUPLEX-agentic-workflow

![Introducing SUPLEX](demo/img/suplex_logo_cropped.png)

`SUPLEX-agentic-workflow` installs the SUPLEX control layer into an existing repository.

Use it when you want to add a standard supervision and handoff structure for agentic work. SUPLEX doesn't change the underlying architecture of the target project and doesn't collide with common host-governance paths such as root `AGENTS.md`, `CLAUDE.md`, `docs/`, or `handoffs/`.

SUPLEX can be initialized in two infrastructure modes:

- `standard`: full bounded-pass history with dated handoffs and dated execution reports in `./.suplex/handoffs/history/`, plus optional phase artifacts for multi-pass objectives
- `sans-sucre`: lighter live-pass infrastructure with `./.suplex/handoffs/active/current_handoff.md` plus `./.suplex/handoffs/active/current_execution_report.md`, and no dated history directory

## What is SUPLEX

SUPLEX is a supervised pipeline with layered execution. It consists of a lightweight agentic control layer and is meant for AI-assisted bounded repository work. It provides governance files, canonical control-memory docs, and handoff structure so an agent can operate inside a repo with explicit scope, provenance, and closure rules.

SUPLEX requires explicit role routing. An undesignated agent should not operate on the repo. The supervision role writes phases, handoffs, reviews, checkpoints, and governance records. The execution role only executes the active handoff and writes the required execution report.

SUPLEX separates the roles of goal-setting and decision-making (yours) from supervising and implementation (the models).

## Demo

See [demo/README.md](demo/README.md) for a screenshot-based walkthrough of the standard SUPLEX workflow.

Human-readable example artifacts are also available in [demo/examples/example_handoff.md](demo/examples/example_handoff.md) and [demo/examples/example_execution_report.md](demo/examples/example_execution_report.md).

## Who It Is For

SUPLEX is for work that benefits from tight control, explicit bounded passes, and regular user oversight.

It is a better fit for:

- research workflows
- complex or ambiguous projects where requirements need to be clarified as work proceeds
- repositories where provenance, scope control, and validation matter more than raw speed
- work where the user wants to stay in the loop before and after each bounded pass

It is a worse fit for:

- loose exploratory coding with minimal process
- broad parallel task farming
- situations where the user wants the agent to improvise across many unrelated tasks without repeated supervision

## What It Does

Running the bootstrap from inside a target repository adds the SUPLEX control layer:

- `SUPLEX.md`
- `.suplex/init_state.yaml`
- `.suplex/AGENTS.md`
- `.suplex/CLAUDE.md`
- `.suplex/docs/`
- `.suplex/handoffs/`
- `.suplex/docs/local_lessons.md`
- `.suplex/docs/governance_update_proposals.md`

The write contract is intentionally narrow:

- SUPLEX writes root `SUPLEX.md`
- SUPLEX writes and updates files under `./.suplex/`
- SUPLEX leaves untouched canonical governance (typically at root: `AGENTS.md`, `CLAUDE.md`, `docs/`)

The installed runtime includes:

- supervision and execution specs in `.suplex/docs/10_supervision_layer_spec.md` and `.suplex/docs/11_execution_layer_spec.md`
- a canonical backlog in `.suplex/docs/13_bounded_task_backlog.md`
- an active handoff pointer in `.suplex/handoffs/active/current_handoff.md`
- in `standard` mode, handoff and execution-report history in `.suplex/handoffs/history/`
- in `standard` mode, optional phase records under `.suplex/phases/` for multi-pass supervisory continuity
- in `sans-sucre` mode, a live execution report in `.suplex/handoffs/active/current_execution_report.md`
- reusable handoff templates in `.suplex/handoffs/templates/`, plus the execution-report template in `standard` mode

## Scope

SUPLEX init creates the supervision-execution layers, but it does not create or infer your project architecture. It does not add code, data, or source files.

For overlay installs, this means SUPLEX is designed to preserve the host repository's existing project structure while adding its own control layer. The installer treats root `SUPLEX.md` and `./.suplex/` as SUPLEX-owned paths, so those paths may be created or refreshed during installation; the non-collision guarantee applies to common host-governance locations outside that namespace.

Successful `suplex init` always installs the same full control layer. After initialization, `.suplex/handoffs/active/current_handoff.md` starts as a no-active-handoff placeholder, so the first active layer is supervision. The first supervision pass should read that file first, inspect the repo if it has repo access, ask what you want to do next, and define exactly one bounded task.

If the repo was empty (SUPLEX as a greenfield), that first supervision pass will often need an architecture-planning or structure-confirmation step before implementation begins. If the repo was already populated with code, data, or source files (SUPLEX as an overlay), that first supervision pass should reconstruct enough of the current repo state to define the next bounded task safely. Architecting is an expected supervision escalation mode when structure decisions need to be made, not a permanent parallel role.

`standard` and `sans-sucre` differ in infrastructure weight. Both modes keep the supervisor / executor split, bounded-task logic, checkpointing, validation, and discrepancy handling. `standard` may also use optional phases for multi-pass objectives. `sans-sucre` mainly removes dated handoff and report history and does not use phase artifacts, so the repo carries less pass-by-pass archival overhead.

## Skills And Agents

SUPLEX is intended to sit above project-specific skills and agents as a control layer, not replace them.

If a target repository already contains skills, agents, or similar execution helpers, SUPLEX should usually preserve them as project-domain assets. Successful initialization adds only the SUPLEX control layer and does not restructure existing `src/`, `data/`, `notebooks/`, `site/`, `public/`, or similar project directories.

However, compatibility is not automatically seamless when the target repo already has its own governance layer. SUPLEX now installs its canonical files under `./.suplex/` and uses root `SUPLEX.md` as the entrypoint, which avoids direct file collisions with existing root `AGENTS.md`, `CLAUDE.md`, `docs/`, or `handoffs/`. This is a coexistence improvement, not a claim that all governance ambiguity disappears. In overlay repos that already have root governance files, the first supervision pass should inspect those files early, explain any coexistence risk, and determine with the user whether a bounded governance-alignment pass is needed.

The integration model is:

- SUPLEX provides supervision, bounded-task definition, handoff discipline, validation, and checkpointing.
- project-specific skills provide reusable execution capabilities
- project-specific agents perform bounded execution work under SUPLEX supervision

So:

- adding SUPLEX to a repo that already has skills or agents is usually structurally compatible if those assets do not depend on conflicting governance rules
- adding skills or agents to a SUPLEX-managed repo is usually compatible if they are treated as project-domain components governed by the active handoff and stable SUPLEX rules
- layering SUPLEX on top of another repo-wide governance system with competing ownership expectations should still be treated as an explicit integration task, even though SUPLEX now keeps its canonical files under `./.suplex/`

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

PowerShell on Windows, `sans-sucre` mode:

```powershell
$env:SUPLEX_WORKFLOW_MODE='sans-sucre'
irm https://raw.githubusercontent.com/ValentinGuigon/SUPLEX-agentic-workflow/main/bootstrap/install.ps1 | iex
```

POSIX shell on macOS, Linux, or a real POSIX shell:

```sh
curl -fsSL https://raw.githubusercontent.com/ValentinGuigon/SUPLEX-agentic-workflow/main/bootstrap/install.sh | sh
```

POSIX shell, `sans-sucre` mode:

```sh
curl -fsSL https://raw.githubusercontent.com/ValentinGuigon/SUPLEX-agentic-workflow/main/bootstrap/install.sh | SUPLEX_WORKFLOW_MODE=sans-sucre sh
```

The bootstrap looks for Python 3 automatically:

- PowerShell bootstrap tries `py -3` first, then `python`
- POSIX bootstrap tries `python3` first, then `python`
- if neither candidate can execute Python 3, the bootstrap stops with an explicit remediation message

## What Success Looks Like

After installation, the target repository should contain the SUPLEX control layer alongside the project's existing files.

In an overlay repo, existing root governance files such as `AGENTS.md` or `CLAUDE.md` may still be present exactly as before. The intended result is coexistence: root `SUPLEX.md` points into the canonical SUPLEX layer under `./.suplex/`, while host-governance files remain host-owned unless the repo explicitly delegates otherwise.

At minimum, you should see:

- `SUPLEX.md`
- `.suplex/`
- `.suplex/AGENTS.md`
- `.suplex/CLAUDE.md`
- `.suplex/docs/`
- `.suplex/handoffs/`

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

- Interact with the supervision layer before each handoff so the next bounded pass is scoped correctly.
- Interact with the supervision layer again after each execution report so the result can be reviewed, validated, and either closed or turned into the next bounded pass.
- Each task enters through a handoff document in `.suplex/handoffs/` with a defined scope, blocker list, acceptance criteria, and validation plan.
- Each bounded task returns an execution report describing what was read, what was done, what was not done, validation result, blockers, and the likely next bounded task.
- In `standard` mode, the workflow maintains dated handoff and execution-report history.
- In `standard` mode, supervision may also open an optional phase for multi-pass objectives that need continuity, inherited constraints, or gates across several handoffs.
- In `sans-sucre` mode, the workflow keeps only the live active handoff and live active execution report.
- The workflow maintains canonical control-memory docs including the checkpoint, validation ledger, and discrepancy log.
- Where provenance matters, project docs may tag claims with evidence level: `[E]` directly evidenced, `[I]` strong inference, `[U]` unresolved.
- No implementation proceeds without an active handoff document and evidence that the prior stage was validated.
- If canonical docs and code artifacts disagreed, the discrepancy is logged before proceeding. `.suplex/docs/` is the canonical SUPLEX project memory; `.suplex/handoffs/` define the execution boundary.

In practice, SUPLEX works best when the user treats supervision as the decision layer:

- tell supervision what you want next - interact with it like you would normally to query the repo, define objectives, ask questions, make suggestions
- direct instructions such as "write the phase", "open a phase", "write the handoff", or "update the handoff" are supervision-layer artifact work
- let supervision restate blockers, ambiguities, and the bounded task
- let execution do only that bounded pass
- return to supervision to interpret the result before starting the next pass

## Demo

A screenshot-based walkthrough of the standard operating loop is available in [demo/README.md](demo/README.md).

## Repository Layout

This repository is the distribution source for the installer.

- `bootstrap/`: install wrappers plus the Python initializer
- `tests/`: repo-owned testing area, including minimal seed repos and a small number of full snapshots
- `template/`: the install payload source, with `template/SUPLEX.md` plus the canonical control layer under `template/.suplex/`

The repository root is for packaging and distribution. The files that get installed into target repositories are sourced from `template/`.

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
