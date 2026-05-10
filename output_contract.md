# Output contract

Prefer strict JSON for machine-facing outputs. Use Markdown only when the user asks for a command brief or report prose.

## JSON shape

```json
{
  "items": [
    {
      "event_id": "EVT_001",
      "decision": "dispatch",
      "selected_option_id": "opt_01",
      "center_id": "main_center",
      "mode": "road",
      "reason": "Reason grounded in route, resource, and evidence.",
      "evidence_ids": ["GIS_ROUTE_01", "POLICY_01"]
    }
  ],
  "risk_notes": ["Known execution risk."],
  "situation_assessment": "Current situation in one short paragraph.",
  "change_assessment": "What changed from the previous step, if available.",
  "incident_profiles": [
    {
      "event_id": "EVT_001",
      "location_summary": "Known or uncertain location.",
      "need_summary": "People and resource needs.",
      "vulnerability_note": "Elderly, disabled, medical dependency, children, or unknown.",
      "priority_rationale": "Why this incident is ranked here."
    }
  ],
  "conflict_report": [
    {
      "conflict_id": "CONFLICT_001",
      "event_id": "EVT_001",
      "sources": ["CITIZEN_01", "GIS_ROUTE_01"],
      "conflict": "What disagrees.",
      "judgment": "Which source is trusted for action and why.",
      "action_implication": "How the conflict changes the plan."
    }
  ],
  "uncertainty_registry": [
    {
      "uncertainty_id": "UNC_001",
      "event_id": "EVT_001",
      "field": "location",
      "description": "What is unknown.",
      "impact": "Why it matters.",
      "temporary_posture": "Act, wait, route around, or hand off."
    }
  ],
  "pending_questions": [
    {
      "question_id": "Q_001",
      "event_id": "EVT_001",
      "question": "What a human should confirm.",
      "reason": "Why this matters.",
      "urgency": "high",
      "suggested_human_role": "dispatcher"
    }
  ],
  "alternative_plans": [
    {
      "plan_id": "ALT_001",
      "event_id": "EVT_001",
      "label": "Backup route from backup center",
      "plan_type": "route_switch",
      "trigger_condition": "When to activate it.",
      "rationale": "Why this backup is safe or useful.",
      "risk_notes": ["Remaining risks."]
    }
  ],
  "commander_summary": {
    "situation_overview": "What is happening.",
    "priority_ranking": ["EVT_001", "EVT_002"],
    "main_plan_summary": "What to do now.",
    "alternative_plan_summary": "What to do if conditions change.",
    "uncertainty_summary": "What remains unknown.",
    "recommended_actions": ["Immediate next action."]
  }
}
```

## Decision values

Allowed `decision` values:

- `dispatch`
- `maintain`
- `switch_center`
- `switch_mode`
- `request_support`
- `escalate_to_human`
- `resolve`

## Field discipline

- `selected_option_id` must come from candidate options when dispatching or switching.
- `center_id` must be a provided center ID.
- `mode` must be a provided mode.
- `evidence_ids` must be provided IDs.
- If a field cannot be grounded, use `null` and explain in `reason`, `uncertainty_registry`, or `pending_questions`.

