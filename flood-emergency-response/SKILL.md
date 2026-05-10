---
name: flood-emergency-response
description: Generate, review, and repair hallucination-controlled flood emergency response and rescue plans. Use when working on  multi-source disaster intelligence, GIS-constrained rescue dispatch, command briefs, text-bundle based flood scenarios, evidence conflict handling, uncertainty disclosure, human handoff advice, or evaluation rubrics for LLM/GIS/knowledge-graph flood response agents.
---

# Flood Emergency Response

Use this skill to turn multi-source flood disaster intelligence into a grounded rescue plan. Keep the core stance clear:

- GIS, routing, water-depth rasters, and resource tools are the spatial execution layer.
- Emergency plans, policy snippets, historical cases, RAG, and knowledge graphs are the factual constraint layer.
- The LLM is the situation-understanding, evidence-reasoning, and command-briefing layer.

Do not invent locations, routes, water depths, resource stock, casualty numbers, policies, or evidence IDs. When information is incomplete or conflicting, say so, choose a conservative executable action, and recommend human confirmation when needed.

## First move

Identify the task type:

1. `plan`: create a flood rescue plan from structured state, text bundle, GIS outputs, and resources.
2. `review`: audit an existing plan for spatial, factual, resource, and evidence risks.
3. `repair`: revise an existing plan after verifier issues.
4. `brief`: write a commander-facing summary from an existing directive.
5. `evaluate`: score a plan with a rubric.

Then load only the reference file that matches the task:

- Planning workflow: `references/decision_workflow.md`
- Evidence and hallucination control: `references/evidence_and_hallucination_control.md`
- Output fields and JSON shape: `references/output_contract.md`
- Text bundle input schema: `references/text_bundle_schema.md`
- Evaluation rubric: `references/evaluation_rubric.md`

Use assets only when a user asks for a reusable template:

- Rescue plan template: `assets/rescue_plan_template.md`
- Hidden truth table template: `assets/truth_table_template.yaml`

## Planning workflow

For each incident, build a compact situation picture:

- confirmed facts
- uncertain facts
- conflicting reports
- vulnerable groups and time-sensitive needs
- GIS, route, water-depth, and access constraints
- available rescue resources
- relevant policy or historical-case evidence

Select actions only from the available candidate options and tool outputs. If no route was queried, do not treat that as proof of no feasible route. If a route is infeasible or resources are insufficient, use support request or human handoff instead of pretending the dispatch is executable.

## Evidence hierarchy

Use this order as a default, while considering recency and location specificity:

1. GIS/routing/water-depth tool output for spatial feasibility.
2. Official emergency notice, plan, or policy rule for command constraints.
3. Dispatcher or field-team report for operational state.
4. Historical case for analogy, not direct proof.
5. Citizen report or social-media text for early signal, usually requiring confirmation.

When evidence conflicts, name the conflict explicitly. Do not let a low-confidence citizen report override a hard GIS blockage unless a newer authoritative field report explains why the GIS state is stale.

## Required rescue-plan content

A complete output should include:

- `situation_assessment`: what is happening now.
- `items` or `action_items`: one decision per active incident.
- `risk_notes`: execution risks and safety concerns.
- `incident_profiles`: incident-level needs, vulnerabilities, and rationale.
- `conflict_report`: evidence conflicts and their handling.
- `uncertainty_registry`: unknown location, demand, route, resource, or evidence facts.
- `pending_questions`: questions for human confirmation.
- `alternative_plans`: backup plans with trigger conditions.
- `commander_summary`: a concise human-facing command brief.

Keep command-facing text short, concrete, and operational. Avoid generic disaster-management prose.

## Repair rules

When repairing a plan:

- Preserve unaffected incidents.
- Fix verifier issues first.
- Do not add new centers, routes, resources, or evidence IDs that were not provided.
- If evidence IDs are invalid, replace them with valid IDs for the same event or mark the item for human confirmation.
- If route or resource feasibility cannot be repaired from available data, switch to `request_support` or `escalate_to_human`.

## Self-check

Before finalizing, check:

- Are all locations grounded in provided input or marked uncertain?
- Does each dispatch have a feasible route or a stated reason for handoff?
- Are resource assignments within available stock?
- Does every action cite evidence IDs when available?
- Are conflicts and unknowns visible to the commander?
- Is there at least one backup plan for high-priority or uncertain incidents?
- Could a human commander understand what to do next within 30 seconds?

