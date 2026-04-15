# SUPLEX

This repository has a SUPLEX control layer installed.

Canonical SUPLEX workflow files live under `./.suplex/`.

Read in this order:
- `./.suplex/handoffs/active/current_handoff.md`
- `./.suplex/AGENTS.md`
- `./.suplex/CLAUDE.md`
- relevant files under `./.suplex/docs/`

If the user invokes the execution layer or says that a new task awaits, treat `./.suplex/handoffs/active/current_handoff.md` as the task source and continue from there rather than asking the user to restate the task.

If root `AGENTS.md` or `CLAUDE.md` also exist, treat them as host-repository governance unless they explicitly delegate bounded-task workflow control to SUPLEX.

SUPLEX governance is canonical for the bounded supervision / execution workflow.
