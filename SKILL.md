---
name: mg-industrial-equipment-manual-builder
description: >
  Use when creating, revising, auditing, installing, or open-sourcing A4-paged
  Chinese or bilingual HTML manuals for industrial or non-standard equipment,
  especially with machine photos, HMI parameter pages, SFC/timing review,
  material-flow evidence, fixture changeover, repeated rework, or high token usage.
metadata:
  version: "0.7.0"
---

# MG Industrial Equipment Manual Builder

## Core Principle

Build one evidence-backed HTML around the operator's task. Explicit A4 sheets are the single framework on every device; make important equipment and HMI images large inside each sheet.

## Non-Negotiable Rules

1. HTML is the only customer deliverable. Do not create PDF, PNG, a desktop edition, or duplicate HTML. Conversion is outside this skill.
2. Design the HTML with explicit `210 mm x 297 mm` A4 page containers and deliberate page groups. Do not rely on browser auto-pagination alone.
3. The A4 sheet is the only frame. Phone and PC keep the same page composition; only scale the sheet proportionally to the viewport. Do not create device-specific nested page systems or structural reflow.
4. Give detailed mechanism and HMI images at least 75% of the A4 content width. Prefer a full-width image band or dedicated image page over two narrow detailed images side by side.
5. Work inside the project folder, preserve original evidence, and do not invent numeric setpoints, PLC behavior, hidden modes, or transfer points.
6. Get outline approval before full HTML; keep internal reasoning out of customer pages.

## Required Project State

Maintain:

- `项目管理/项目看板.md`: phase, filename, status, sources, verification.
- `项目管理/交接摘要.md`: compact state for continuation.
- `项目管理/SFC时序审核稿.md`: evidence, sequence, mappings, status.
- `源稿/图片双语注释清单.md`: source, annotation, final image.
- `源稿/HTML章节结构.md`: approved task outline.
- `源稿/A4分页规划.md`: page purpose, content group, image share.

Use `references/project-structure.md` only when creating or repairing the folder structure.

## Three-Phase Workflow

### A. Evidence and Outline

Inventory once. Freeze the final HTML filename and language. Write:

- one sentence describing the novice's real job;
- one evidence-backed material-flow chain from pickup to final handoff;
- one batch of unresolved mechanism or timing questions.

Order the outline by what the novice must observe or decide next, not by generic machine chapters. Confirm each transfer point from evidence and build the SFC review before final parameter explanations. After outline approval, create the A4 page map before full HTML.

Read `references/manual-builder-workflow.md` for the full evidence and SFC gate.

### B. HTML Build and Feedback

For each important HMI item, connect label, mechanism, SFC step, adjustment effect, use scenario, value acquisition, verification, evidence, and confirmation status. Exclude unresolved claims.

For position values supported by live HMI travel data: jog in small steps, visually confirm the mechanism, read current position, enter the target, and retest. Do not copy live position into speed, time, or offset fields. Pair the HMI with the real mechanism and observation point.

Approve one representative HMI/mechanism A4 page before repeating the pattern. Keep related structure and HMI on the same page only when labels remain legible; otherwise use stacked full-width bands or consecutive pages. Split dense parameter groups at semantic boundaries. Then complete one A4-paged HTML and revise it once per feedback batch.

Read `references/a4-page-layout.md` for page and image-share rules, and `references/hmi-parameter-explanation.md` only for parameter-writing details.

### C. Final HTML Verification

Run the bundled audit, then verify A4 pages at desktop and phone viewport widths after the HTML is complete or after a substantive layout change:

```powershell
python scripts/audit_manual_project.py "C:\path\to\project"
```

Confirm zero page overflow, intact semantic blocks, identical composition across devices, detailed images at least 75% of content width, loaded relative assets, working language modes, and one customer-facing HTML. Screenshots and print checks are internal only. Read `references/audit-checklist.md` at closeout.

## Token and Context Control

At each phase boundary, rewrite `项目管理/交接摘要.md` within 1,200 Chinese characters or roughly 800 English words. Keep only the goal, confirmed flow, approved structure, unresolved questions, next files, and latest verification.

For later work:

- read the handoff summary first and only the files it names;
- do not repeat inventory or reread unchanged large files;
- use targeted search and line ranges instead of printing full HTML or logs;
- batch independent reads and combine checks into concise PASS/FAIL output;
- use targeted static checks for small wording changes;
- recommend a fresh thread after outline or HTML approval, using the handoff summary; never create one without explicit user request.

Read `references/rework-prevention.md` when rework or context growth appears.

## Delivery Report

Report only the project management files, final A4-paged HTML, internal verification result, and reusable confirmed knowledge. Do not list historical or internal artifacts as customer deliverables.

## References

- `references/html-only-delivery.md`: delivery boundary.
- `references/a4-page-layout.md`: single A4 framework, image-share rules, and verification.
- `references/manual-builder-workflow.md`: full workflow and SFC gates.
- `references/hmi-parameter-explanation.md`: integrated HMI/SFC explanation.
- `references/rework-prevention.md`: rework and token controls.
- `references/project-structure.md`: folders and naming.
- `references/audit-checklist.md`: final audit.
- `templates/项目看板.md`, `templates/SFC时序审核稿.md`, `templates/交接摘要.md`: reusable state files.
