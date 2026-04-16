
# No Active Handoff

There is currently no active bounded pass.

In `sans-sucre` mode, supervision should:
1. read this file first
2. confirm that no unfinished bounded pass exists
3. consult `docs/13_bounded_task_backlog.md` as the default next-task sequencing reference unless a blocker, discrepancy, or fresh validation result justifies a deviation
4. issue exactly one new active handoff in this file before execution work begins
5. use `handoffs/active/current_execution_report.md` as the matching live execution-report artifact for the pass
