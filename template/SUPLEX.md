# SUPLEX

This repository has a SUPLEX control layer installed.

Canonical SUPLEX workflow files live under `./.suplex/`.

Before repo work begins, the agent must know its SUPLEX role:
- `supervision`: may write and update SUPLEX phases, handoffs, reviews, checkpoints, and governance records.
- `execution`: may only execute the active handoff and write the required execution report.

If the role is not designated, ask whether the user wants supervision or execution before inspecting, editing, or running tools.

Read in this order:
- `./.suplex/handoffs/active/current_handoff.md`
- `./.suplex/AGENTS.md`
- `./.suplex/CLAUDE.md`
- relevant files under `./.suplex/docs/`

Direct instructions such as "write the phase", "open a phase", "write the handoff", or "update the handoff" are supervision-layer artifact work. The supervisor should perform that governance update if scope is clear, or ask for clarification if it is not.

If the user invokes the execution layer or says that a new task awaits, treat `./.suplex/handoffs/active/current_handoff.md` as the task source and continue from there rather than asking the user to restate the task.

Root `AGENTS.md` and `CLAUDE.md` may contain a short marked SUPLEX routing block so agents that auto-load root governance are directed here. Treat any other root-governance content as host-repository governance unless it explicitly conflicts with SUPLEX role routing, handoff scope, or execution boundaries.

SUPLEX governance is canonical for the bounded supervision / execution workflow.
