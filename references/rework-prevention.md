# Rework Prevention and Token Efficiency

## Freeze Before Full Build

1. Delivery matrix: final HTML filename, device, and language.
2. Novice task: one sentence stating what the operator must accomplish.
3. Material flow: evidence-backed chain from pickup to final handoff.
4. Outline: ordered by the novice's next observation or decision.
5. One representative HMI/mechanism section: approve the information pattern before repeating it.

## Common Rework Causes

| Symptom | Cause | Prevention |
|---|---|---|
| Generic, lengthy outline | Template chosen before the user task | Start from the novice's job and observable flow |
| Wrong transfer point | Mechanism inferred from convention | Confirm each handoff from photos, video, HMI, or user evidence |
| Missing downstream action | Scope endpoint left implicit | Write start and final handoff before outlining |
| HMI feels abstract | Screen separated from mechanism | Pair HMI and real structure in the same step |
| Operator cannot set a value | Meaning explained, acquisition omitted | Add value-acquisition method to the parameter model |
| Too many deliverables | Optional formats treated as defaults | Produce only the frozen primary file |
| Duplicate deliverables | Conversion treated as part of manual writing | Stop at the approved HTML; handle conversion outside this skill |

## Token-Saving Workflow

- Inventory sources once and maintain a concise evidence map.
- Batch uncertain mechanism and timing questions instead of interrupting row by row.
- Do not write full HTML before the outline and one representative section are accepted.
- Absorb a feedback batch into source-of-truth notes, then revise HTML once.
- At each phase boundary, rewrite `项目管理/交接摘要.md` within 1,200 Chinese characters or roughly 800 English words.
- Continue from the handoff summary and only the files named there; do not reread unchanged source trees.
- Prefer targeted `rg`, line-range reads, and concise script output over printing complete HTML or long logs.
- Batch independent reads and combine static checks into one PASS/FAIL command.
- Run quick static checks during drafting; run full mobile-browser verification only for completed HTML or substantive layout changes.
- Recommend a fresh thread after outline approval or HTML approval, using the handoff summary as the entrypoint; never create one without an explicit request.
- Reuse the bundled HTML audit instead of reconstructing checks in each project.
