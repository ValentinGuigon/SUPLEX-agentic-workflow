# SUPLEX-agentic-workflow

`SUPLEX-agentic-workflow` is the distributable project repository for the SUPLEX control layer. The repo root is packaging space. The payload copied into target repositories lives under `template/`, and the bootstrap layer under `bootstrap/` applies that payload to the current working directory.

## Layout

- `bootstrap/`: thin install wrappers plus the Python initializer
- `template/`: the target-repo payload

## Payload

`template/` contains the SUPLEX control layer only:

- `AGENTS.md`
- `CLAUDE.md`
- `.suplex/init_state.yaml`
- `docs/`
- `handoffs/`
- `local_lessons.md`
- `governance_update_proposals.md`

No computation, modeling, data, notebook, pipeline, publication, deployment, or project-architecture scaffolding is introduced by default. Successful `suplex init` always installs this same full control layer; architecture planning is decided later by supervision after reading the target repo's `README.md` and checking with the user.

## Run

Run the bootstrap from inside the target repository. The target repository must already have its own `README.md`; this repo's `README.md` is packaging documentation only.

Requirements:

- PowerShell path: PowerShell with `Invoke-WebRequest` and `Expand-Archive`, plus Python 3 available via `py -3` preferred or `python` fallback
- POSIX path: `sh`, `curl` or `wget`, `unzip`, and Python 3 available via `python3` preferred or `python` fallback
- Python dependencies: none beyond the Python standard library

Windows users should normally use the PowerShell bootstrap. Use the POSIX bootstrap on Windows only when you are intentionally running inside a POSIX shell environment that provides the required tools and a usable `python3`.

PowerShell:

```powershell
irm https://raw.githubusercontent.com/ValentinGuigon/SUPLEX-agentic-workflow/main/bootstrap/install.ps1 | iex
```

POSIX shell:

```sh
curl -fsSL https://raw.githubusercontent.com/ValentinGuigon/SUPLEX-agentic-workflow/main/bootstrap/install.sh | sh
```

For local validation from this checkout, point the bootstrap at the project root; the initializer will source the payload from `template/`.

Interpreter selection:

- PowerShell bootstrap tries `py -3` first, then `python`
- POSIX bootstrap tries `python3` first, then `python`
- If neither candidate can execute Python 3, the wrapper stops with an explicit remediation message

PowerShell local source:

```powershell
powershell -ExecutionPolicy Bypass -File .\bootstrap\install.ps1 -SourceRoot .
```

POSIX local source:

```sh
SUPLEX_SOURCE_ROOT="$(pwd)" sh ./bootstrap/install.sh
```
