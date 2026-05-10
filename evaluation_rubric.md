# Evaluation rubric

Use this rubric for plans, command briefs, or LLM-as-judge calibration. Score each item from 0 to 2 unless a project uses a different scale.

## Executability

2: Every dispatch has feasible route, valid center, valid mode, and available resources.  
1: Minor missing details, but the plan can be repaired locally.  
0: Uses impossible route, nonexistent center, unavailable resource, or ungrounded spatial claim.

## Evidence grounding

2: Key claims cite valid evidence IDs or tool outputs.  
1: Some claims are grounded, but important claims are unsupported.  
0: Evidence is absent, invalid, or fabricated.

## Conflict handling

2: Names conflicts, judges reliability, and changes action accordingly.  
1: Mentions conflict but does not connect it to the plan.  
0: Ignores conflict or trusts low-confidence text over stronger evidence without reason.

## Uncertainty disclosure

2: States unknowns, explains impact, and asks actionable human questions.  
1: States unknowns but gives weak follow-up.  
0: Hides uncertainty or guesses.

## Human handoff

2: Escalates when needed and names who should confirm what.  
1: Handoff is present but vague.  
0: Fails to escalate in a safety-critical uncertain case.

## Backup planning

2: Gives realistic backup plan with trigger condition.  
1: Backup plan exists but trigger or action is vague.  
0: No backup for high-priority or uncertain incident.

## Command clarity

2: A commander can identify priorities and next actions within 30 seconds.  
1: Understandable but too verbose or under-prioritized.  
0: Generic prose with no operational decision.

## Hallucination risk

2: No spatial, knowledge, resource, or evidence hallucination.  
1: Minor unsupported phrasing that does not affect action.  
0: Unsupported claim affects route, resource, priority, or safety.

