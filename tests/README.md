# Tests

This directory is the repo-owned testing area for `SUPLEX-agentic-workflow`.

Use it for:
- stable fixtures
- minimal seed repos
- a small number of full initialized snapshots
- reproducible bootstrap and runtime validation scenarios
- test-support artifacts that should be tracked in Git

Do not use it for:
- one-off probes
- disposable smoke-test outputs
- personal scratch validation work

Suggested convention:
- `seeds/` for minimal input repos used to exercise bootstrap behavior
- `snapshots/` for a small number of tracked post-init states where the initialized output shape itself matters
- `interpreter_validation/` and `interpreter_validation_ps/` for interpreter-selection validation assets
