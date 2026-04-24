from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
SCENARIO_DIR = ROOT / "behavioral_harness" / "scenarios"


def _load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _artifact_request_type(message: str) -> str | None:
    lowered = message.lower()
    if "write the handoff" in lowered or "create a handoff" in lowered or "update the handoff" in lowered:
        return "handoff"
    if "write the phase" in lowered or "create a phase" in lowered or "update the phase" in lowered:
        return "phase"
    return None


def evaluate_supervision_route(scenario: dict[str, Any]) -> dict[str, Any]:
    user_message = scenario["input"]["user_message"]
    artifact_type = _artifact_request_type(user_message)
    target_clear = scenario["input"].get("target_clear", False)
    actual = {
        "artifact_type": artifact_type,
        "response_type": "focused_clarification",
    }
    if artifact_type and target_clear:
        actual["response_type"] = "supervision_artifact_work"
    elif artifact_type:
        actual["response_type"] = "focused_clarification"
    return actual


def evaluate_supervision_handoff_fields(scenario: dict[str, Any]) -> dict[str, Any]:
    handoff = scenario["input"]["draft_handoff"]
    actual = {
        "selected_local_mechanisms_named": bool(handoff.get("relevant_local_skills"))
        or bool(handoff.get("relevant_local_agents_or_roles")),
        "pipeline_order_named": bool(handoff.get("required_pipeline_or_handoff_order")),
        "governance_constraints_named": bool(handoff.get("applicable_repo_governance_or_constraints")),
        "excluded_alternatives_named": bool(handoff.get("excluded_but_considered_local_alternatives")),
    }
    actual["response_type"] = (
        "handoff_contract_complete"
        if all(actual.values())
        else "handoff_contract_incomplete"
    )
    return actual


def evaluate_execution_startup(scenario: dict[str, Any]) -> dict[str, Any]:
    request_type = scenario["input"]["request_type"]
    if request_type in {"write_phase", "write_handoff"}:
        return {
            "response_type": "route_to_supervision",
            "requires_reconfirmation": False,
        }

    handoff = scenario["input"]["active_handoff"]
    exception = scenario["input"].get("exception_trigger", "none")
    startup_acknowledged = scenario["input"].get("startup_acknowledgement_produced", False)
    actual = {
        "startup_acknowledgement_required": True,
        "startup_acknowledgement_produced": startup_acknowledged,
        "requires_reconfirmation": False,
        "response_type": "blocked_missing_acknowledgement",
    }
    if not handoff.get("exists", False) or handoff.get("ambiguous", False):
        actual["requires_reconfirmation"] = True
        actual["response_type"] = "request_reconfirmation"
        return actual
    if not startup_acknowledged:
        return actual
    if exception != "none":
        actual["requires_reconfirmation"] = True
        actual["response_type"] = "request_reconfirmation"
        return actual
    actual["response_type"] = "proceed_after_acknowledgement"
    return actual


EVALUATORS = {
    "supervision_route": evaluate_supervision_route,
    "supervision_handoff_fields": evaluate_supervision_handoff_fields,
    "execution_startup": evaluate_execution_startup,
}


def compare_expected(actual: dict[str, Any], expected: dict[str, Any]) -> list[str]:
    mismatches: list[str] = []
    for key, expected_value in expected.items():
        actual_value = actual.get(key)
        if actual_value != expected_value:
            mismatches.append(
                f"{key}: expected {expected_value!r}, got {actual_value!r}"
            )
    return mismatches


def run_scenarios() -> int:
    scenario_paths = sorted(SCENARIO_DIR.glob("*.json"))
    if not scenario_paths:
        print(f"No scenarios found in {SCENARIO_DIR}")
        return 1

    failures = 0
    print(f"Behavioral harness: {len(scenario_paths)} scenario(s)")
    for path in scenario_paths:
        scenario = _load_json(path)
        evaluator = EVALUATORS[scenario["kind"]]
        actual = evaluator(scenario)
        mismatches = compare_expected(actual, scenario["expected"])
        status = "PASS" if not mismatches else "FAIL"
        print(f"[{status}] {scenario['id']}: {scenario['title']}")
        if mismatches:
            failures += 1
            for mismatch in mismatches:
                print(f"  - {mismatch}")

    if failures:
        print(f"\nResult: {failures} scenario(s) failed.")
        return 1

    print("\nResult: all scenarios passed.")
    return 0


if __name__ == "__main__":
    sys.exit(run_scenarios())
