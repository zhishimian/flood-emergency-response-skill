#!/usr/bin/env python3
"""Validate a flood emergency response JSON plan.

This is a lightweight structural checker for outputs produced with the
flood-emergency-response skill. It does not replace GIS, resource, or evidence
verification. It only catches missing fields, invalid decisions, and obviously
malformed sections before a human or project-specific verifier reviews the plan.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


VALID_DECISIONS = {
    "dispatch",
    "maintain",
    "switch_center",
    "switch_mode",
    "request_support",
    "escalate_to_human",
    "resolve",
}

REQUIRED_TOP_LEVEL = [
    "risk_notes",
    "situation_assessment",
    "incident_profiles",
    "conflict_report",
    "uncertainty_registry",
    "pending_questions",
    "alternative_plans",
    "commander_summary",
]


def _load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _is_nonempty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate(plan: dict[str, Any]) -> dict[str, list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for key in REQUIRED_TOP_LEVEL:
        if key not in plan:
            errors.append(f"missing top-level field: {key}")

    items = plan.get("items", plan.get("action_items"))
    if not isinstance(items, list) or not items:
        errors.append("missing non-empty items/action_items list")
        items = []

    for idx, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"item[{idx}] is not an object")
            continue
        event_id = item.get("event_id")
        if not _is_nonempty_text(event_id):
            errors.append(f"item[{idx}] missing event_id")
        decision = item.get("decision")
        if decision not in VALID_DECISIONS:
            errors.append(f"item[{idx}] invalid decision: {decision!r}")
        if not _is_nonempty_text(item.get("reason")):
            warnings.append(f"item[{idx}] missing or empty reason")
        evidence_ids = item.get("evidence_ids")
        if evidence_ids is None:
            warnings.append(f"item[{idx}] missing evidence_ids")
        elif not isinstance(evidence_ids, list) or not all(isinstance(x, str) for x in evidence_ids):
            errors.append(f"item[{idx}] evidence_ids must be a list of strings")

        if decision in {"dispatch", "switch_center", "switch_mode"}:
            if not _is_nonempty_text(item.get("selected_option_id")):
                warnings.append(f"item[{idx}] dispatch/switch action lacks selected_option_id")
            if not _is_nonempty_text(item.get("center_id")):
                warnings.append(f"item[{idx}] dispatch/switch action lacks center_id")
            if not _is_nonempty_text(item.get("mode")):
                warnings.append(f"item[{idx}] dispatch/switch action lacks mode")

    if not _is_nonempty_text(plan.get("situation_assessment")):
        warnings.append("situation_assessment is empty")

    alt = plan.get("alternative_plans")
    if isinstance(alt, list) and not alt:
        warnings.append("alternative_plans is empty")

    pending = plan.get("pending_questions")
    if isinstance(pending, list):
        for idx, q in enumerate(pending):
            if not isinstance(q, dict):
                errors.append(f"pending_questions[{idx}] is not an object")
                continue
            if not _is_nonempty_text(q.get("question")):
                warnings.append(f"pending_questions[{idx}] missing question")
            if not _is_nonempty_text(q.get("reason")):
                warnings.append(f"pending_questions[{idx}] missing reason")

    return {"errors": errors, "warnings": warnings}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("plan_json", type=Path)
    parser.add_argument("--pretty", action="store_true", help="Pretty-print validation result")
    args = parser.parse_args()

    try:
        payload = _load_json(args.plan_json)
    except Exception as exc:  # pragma: no cover - CLI guard
        print(json.dumps({"errors": [f"failed to read JSON: {exc}"], "warnings": []}, ensure_ascii=False), file=sys.stderr)
        return 2

    if not isinstance(payload, dict):
        print(json.dumps({"errors": ["top-level JSON must be an object"], "warnings": []}, ensure_ascii=False), file=sys.stderr)
        return 2

    result = validate(payload)
    indent = 2 if args.pretty else None
    print(json.dumps(result, ensure_ascii=False, indent=indent))
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())

