# SUPLEX-agentic-workflow

`SUPLEX-agentic-workflow` is the distributable project repository for the SUPLEX control layer. The repo root is packaging space. The payload copied into target repositories lives under `template/`, and the bootstrap layer under `bootstrap/` applies that payload to the current working directory.

## Layout

- `bootstrap/`: thin install wrappers plus the Python initializer
- `template/`: the target-repo payload

## Payload

`template/` contains the SUPLEX kernel only:

- `AGENTS.md`
- `CLAUDE.md`
- `.suplex/init_state.yaml`
- `docs/`
- `handoffs/`
- `local_lessons.md`
- `governance_update_proposals.md`

No computation, modeling, data, notebook, pipeline, publication, deployment, or workflow scaffolding is introduced by default.

## Run

Run the bootstrap from inside the target repository. The target repository must already have its own `README.md`; this repo's `README.md` is packaging documentation only.

PowerShell:

```powershell
irm https://raw.githubusercontent.com/ValentinGuigon/SUPLEX-agentic-workflow/main/bootstrap/install.ps1 | iex
```

POSIX shell:

```sh
curl -fsSL https://raw.githubusercontent.com/ValentinGuigon/SUPLEX-agentic-workflow/main/bootstrap/install.sh | sh
```

For local validation from this checkout, point the bootstrap at the project root; the initializer will source the payload from `template/`.
