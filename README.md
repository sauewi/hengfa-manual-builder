# hengfa-manual-builder

A reusable Codex skill for producing professional bilingual HTML manuals for Hengfa-style heat-transfer and hot-stamping equipment.

The skill focuses on the parts that make non-standard machine manuals hard to repeat well:

- managed project folders and source-of-truth documents,
- SFC / timing review before HMI parameter explanations,
- bilingual image annotation without redrawing real machine photos,
- concise customer-facing Chinese and English manual content,
- browser and PDF verification,
- release checks for safe reuse and open-source publishing.

No customer photos, HMI screenshots, PDFs, feedback images, private paths, or project deliverables are bundled in this repository.

## When To Use

Use this skill when a manual project involves:

- heat-transfer or hot-stamping equipment,
- bilingual Chinese / English HTML output,
- HMI parameter pages that need behavior explanations,
- SFC, timing, sensor, or actuator sequence review,
- Chinese-only machine callouts that need English annotations,
- final artifact verification, including PDF pagination.

## Repository Contents

```text
SKILL.md                              Main skill instructions
references/manual-builder-workflow.md Skill-internal workflow reference
references/project-structure.md       Folder and naming contract
references/audit-checklist.md         Manual delivery audit checklist
templates/项目看板.md                  Project board template
templates/SFC时序审核稿.md             SFC review draft template
scripts/audit_manual_project.py       Audit a real manual project
scripts/check_release.py              Audit this repository before release
evals/evals.json                      Lightweight skill evaluation prompts
```

## Install Locally

Copy this folder to your Codex skills directory:

```text
%USERPROFILE%\.codex\skills\hengfa-manual-builder
```

## Audit A Manual Project

```powershell
python scripts/audit_manual_project.py "C:\path\to\manual-project"
```

## Release Check

Before publishing or after changing repository files:

```powershell
python scripts/check_release.py .
python -m json.tool evals/evals.json
python -m py_compile scripts/audit_manual_project.py scripts/check_release.py
```

## Related Skills

- `hotfoil-tune`: mechanism-based heat-transfer tuning and troubleshooting.
- `hmi-param-explainer`: HMI parameter and SFC explanation.

## License

MIT. See `LICENSE`.
