# Text bundle schema

`text_bundle` is planner-visible disaster intelligence. It is not hidden truth.

## Top-level shape

```json
{
  "dispatch_brief": "Short dispatcher-facing summary for this step.",
  "reports": [],
  "policy_snippets": [],
  "historical_case_cards": [],
  "pending_questions_seed": []
}
```

## `dispatch_brief`

Use 80-180 Chinese characters when possible. Emphasize the current text difficulty: conflict, missing location, vulnerable group, uncertain route, or resource ambiguity.

## `reports`

Recommended shape:

```json
{
  "report_id": "CITIZEN_PASSABLE",
  "event_id": "TXTCON_001",
  "source_type": "citizen_hotline",
  "summary": "A citizen says the road is passable.",
  "confidence": 0.28,
  "uncertainty": 0.86,
  "conflicts_with": ["GIS_ROUTE_BLOCK"]
}
```

Common `source_type` values:

- `citizen_hotline`
- `field_team`
- `dispatcher_brief`
- `official_notice`
- `gis_tool`
- `weather_warning`
- `historical_case`
- `policy_rule`

## `policy_snippets`

Short rules that constrain action under uncertainty. Do not turn policy snippets into broader rules unless the snippet says so.

## `historical_case_cards`

Use as analogy and caution. Historical cases should not override current GIS or field evidence.

## `pending_questions_seed`

Seed questions for human review. The model may refine or add questions when uncertainty affects safety or executability.

## Boundary with hidden truth

Do not expose these in the planner-visible bundle:

- exact hidden POI if the task tests ambiguous location handling
- canonical route truth used only by the verifier
- hidden coordinates
- scoring labels or expected answer

