# Evidence and hallucination control

## Grounding rules

Never invent:

- road names, coordinates, POIs, shelters, hospitals, centers
- route IDs, option IDs, water depths, ETA, distance
- vehicle or supply stock
- laws, emergency rules, policy clauses
- evidence IDs or source names
- casualty or demand numbers

If a detail is missing, use `unknown`, `not provided`, or a pending question.

## Spatial hallucination

Spatial hallucination occurs when a plan uses a location, route, road status, or spatial relation that is not supported by GIS/tool output or provided text.

Check every dispatch:

- Is the target location grounded?
- Is the route selected from provided candidate options?
- Is the route status feasible?
- Does the plan respect water-depth or blockage constraints?
- Does the plan avoid treating unqueried routes as failed routes?

When spatial evidence conflicts with text, prefer hard GIS/routing evidence unless a newer authoritative field source explains the discrepancy.

## Knowledge hallucination

Knowledge hallucination occurs when the plan cites or implies an emergency rule, historical lesson, or policy requirement that was not provided.

Check:

- Are policy claims linked to policy snippets or evidence IDs?
- Are historical cases used as analogy rather than proof?
- Are professional thresholds, such as passable depth, only used when provided?
- Are all evidence IDs valid for the current incident?

## Conflict handling pattern

Use this structure:

```text
Conflict: CITIZEN_02 says the road is passable, while GIS_ROUTE_01 marks the route high-risk because max_depth_m is 0.35.
Judgment: Treat the citizen report as low-confidence until field confirmation. Do not use this route for elderly evacuees.
Action: Select the backup-center route and ask field team to verify the disputed segment.
```

## Uncertainty disclosure pattern

Use this structure:

```text
Unknown: exact building entrance and number of trapped people are not confirmed.
Impact: dispatch type can be chosen, but resource quantity may be under-estimated.
Temporary action: send a small reconnaissance/rescue unit if route is safe.
Human question: ask dispatcher to confirm entrance, people count, and mobility constraints.
```

## Human handoff triggers

Escalate or request confirmation when:

- target location is ambiguous and no safe candidate can be selected
- GIS blocks all candidate routes
- text and GIS conflict on a life-critical route
- vulnerable groups are involved and route risk is not settled
- resources are insufficient for minimum safe response
- policy authority is unclear
- output would otherwise require guessing

