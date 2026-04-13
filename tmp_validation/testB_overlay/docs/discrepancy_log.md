# Discrepancy Log

Use this file to record operational mismatches, ambiguities, or conflicts that matter to bounded execution.

Suggested fields:
- date
- task family
- discrepancy
- impact
- current status
- next action

## Current status

| date | task family | discrepancy | impact | current status | next action |
|---|---|---|---|---|---|
| 2026-04-13 | `kernel_scaffold_packaging_pass` | The template repo now includes its own packaging `README.md`, which could be confused with the target repo's required seed `README.md` unless the distinction is made explicit. | Misreading the packaging README as initialization input could cause an incorrect future initialization pass. | Resolved. [E] | Keep the distinction explicit in template packaging docs and initialization behavior. [E] |
