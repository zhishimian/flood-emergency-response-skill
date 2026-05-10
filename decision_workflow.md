# Decision workflow

## Goal

Generate a flood emergency response plan that is executable, evidence-grounded, and honest about uncertainty.

## Step 1: Parse inputs

Separate inputs into five groups:

- Structured disaster state: incident IDs, category, severity, demand, POI, time step.
- Text intelligence: dispatch brief, citizen reports, field reports, official notices, historical cases.
- GIS constraints: candidate routes, water depth, road blockage, accessible shelters or hospitals.
- Resource state: centers, vehicle stock, boats, medical teams, shelters, supplies.
- Knowledge constraints: policies, emergency plans, historical case lessons, knowledge-graph facts.

Keep planner-visible intelligence separate from hidden truth. Hidden truth is for verification and scoring, not for plan generation.

## Step 2: Build incident profiles

For each incident, write:

- event ID and location description
- people affected and vulnerable groups
- urgency and rescue category
- known constraints
- unresolved uncertainty
- current recommended posture

Use short operational language. Example:

`EVT_003`: school shelter request near a low-lying road segment. GIS route from main center is shorter but crosses 0.35 m water depth. Elderly evacuees reported. Prefer backup-center road route unless field team confirms the shallow segment is passable.

## Step 3: Detect conflict and uncertainty

Classify each hard case:

- `source_conflict`: two reports disagree.
- `gis_text_conflict`: text says passable, GIS says blocked or high risk.
- `location_ambiguity`: place name or address is vague.
- `demand_ambiguity`: people count or resource need is unclear.
- `resource_ambiguity`: stock or dispatch capacity is unclear.
- `temporal_staleness`: a report may be outdated.

Do not force a single answer when the input does not support it.

## Step 4: Choose action posture

Use these actions:

- `dispatch`: route and resources are available and risk is acceptable.
- `maintain`: previous action remains valid.
- `switch_center`: another center is safer or better resourced.
- `switch_mode`: change transport mode, such as road to boat.
- `request_support`: local resources are insufficient.
- `escalate_to_human`: location, safety, or authority is too uncertain for autonomous dispatch.
- `resolve`: event is already handled.

Prefer conservative executable action for high-uncertainty flood scenes. If the system can act safely while awaiting confirmation, pair a temporary action with a pending question.

## Step 5: Produce main and backup plans

For high-priority incidents, include:

- Main plan: selected route, center, mode, resources, and evidence.
- Backup plan: trigger condition and alternate action.
- Human handoff: who should confirm what, and why.

Backup plans should be conditional, not decorative. Example trigger: `if field team confirms Main Road water depth > 0.3 m, switch to backup_center via opt_02`.

## Step 6: Final command brief

Write for a commander, not for a benchmark. Include:

- situation overview
- priority ranking
- main dispatch decisions
- unresolved risks
- questions requiring human confirmation
- immediate next actions

