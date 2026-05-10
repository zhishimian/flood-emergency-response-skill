# Flood Emergency Response Skill

This repository packages a Codex/Claude-style skill for flood emergency response and rescue-plan generation.

The skill distills prompt-engineering and workflow patterns from the FloodAgent project into a reusable agent guide for:

- multi-source flood disaster intelligence
- GIS-constrained rescue dispatch
- evidence conflict handling
- uncertainty disclosure
- main and backup rescue plans
- human handoff advice
- hallucination-aware plan review

## Repository layout

```text
flood-emergency-response-skill/
├── flood-emergency-response/   # installable skill source
│   ├── SKILL.md
│   ├── references/
│   ├── assets/
│   └── scripts/
└── dist/                       # packaged .skill file after packaging
```

## Install from source

Copy the skill folder into your local skills directory:

```powershell
Copy-Item -Recurse -Force ".\flood-emergency-response" "$env:USERPROFILE\.codex\skills\flood-emergency-response"
```

Then call it in a new session:

```text
[$flood-emergency-response] Generate a flood rescue command brief from this text bundle and GIS route output...
```

## Install from package

Use the packaged file in `dist/flood-emergency-response.skill` if your environment supports skill import.

## Minimal validation

The skill includes a lightweight JSON plan checker:

```powershell
D:/ac/envs/py1/python.exe .\flood-emergency-response\scripts\validate_rescue_plan.py .\plan.json --pretty
```

This checker only validates structure. GIS, resource, and evidence verification should still be performed by the host project.

## Note

No open-source license is declared in this package. Add a license before public reuse if the project team decides to release it as open source.

