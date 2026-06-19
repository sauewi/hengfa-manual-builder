---
name: hengfa-manual-builder
version: 0.3.0
description: >
  Use this skill whenever creating, revising, auditing, installing, or
  open-sourcing a Hengfa-style heat-transfer machine manual skill workflow,
  especially for bilingual HTML manuals, project folder management, SFC/timing
  review drafts, HMI parameter explanations, bilingual image annotations,
  Playwright/PDF verification, and reusable skill handoff. Trigger strongly for
  恒发, 热转印机说明书, 平面热转印机, 大幅面热转印, 中英双语HTML,
  SFC时序审核, HMI参数, 图片双语标注, 项目管理, 说明书技能, and 做成技能.
---

# Hengfa Manual Builder

This skill turns a Hengfa-style heat-transfer machine manual project into a repeatable skill-driven production workflow. It owns the project structure, chapter template, HMI/SFC parameter explanation, verification gates, and handoff rules inside one skill so manual creation does not require chaining a second HMI-parameter skill.

## Operating Rules

1. Treat the final customer deliverable as a bilingual HTML file unless the user asks for an additional export.
2. Keep the project folder managed from the start: source drafts, project management files, bilingual annotation images, temporary files, and outputs must be separated.
3. Build the SFC / timing layer before freezing HMI parameter explanations. The SFC is the backbone for parameter cards, manual debugging steps, and troubleshooting.
4. Preserve original machine evidence. When a photo only has Chinese labels, add English annotations without replacing or redrawing the real device image. Use image generation only as a wording/layout aid if it distorts the equipment.
5. Do not invent unconfirmed temperature, pressure, speed, capacity, PLC internals, hidden options, or numeric setpoints.
6. Keep internal reasoning out of the final HTML. Project notes may record linkage logic, but customer pages should use concise operator-facing wording.
7. Verify the HTML as a real artifact: relative image paths, bilingual coverage, mobile readability, browser screenshots, and PDF pagination when exporting PDF.

## Project Folder Contract

Use this structure unless the existing project already has a compatible structure:

```text
项目根目录/
  设备图片/
  物理调节/
  HMI界面/
  双语标注图/
  源稿/
  项目管理/
  输出/
  临时文件/
```

Required management artifacts:

- `项目管理/项目看板.md`: current phase, folder map, delivery principles, task status, outputs.
- `项目管理/SFC时序审核稿.md`: SFC draft/confirmed sequence, evidence sources, parameter-to-step mapping.
- `源稿/图片双语注释清单.md`: original image, bilingual output image, English annotations, and image-generation decisions.
- `源稿/HTML章节结构.md`: chapter plan, final file name, review status, and post-review changes.

## Workflow

### 1. Intake and Inventory

List all source files and classify them as machine overview, mechanical adjustment, HMI screens, manual buttons, IO/electrical, control panel, air circuit, feedback, source drafts, and outputs.

Create or update the project board before writing the final manual. Record:

- final deliverable type,
- folder purpose,
- delivery principles,
- current task status,
- known source material,
- verification outputs.

### 2. Evidence-Based SFC Gate

Create the SFC review draft before final HMI explanations. Include:

- evidence source table,
- machine action overview,
- numbered SFC steps,
- HMI parameter-to-SFC mapping,
- manual button-to-SFC mapping,
- key review questions or already-confirmed review points.

For timing parameters, state the time origin. If the user later submits feedback, absorb it into the SFC document and change the status to confirmed before using it in final customer content.

If the user asks not to pause for confirmation, still save the review gate as a project artifact and proceed only with evidence-backed or mechanism-safe wording. Do not publish uncertain details as fact.

### 2.5 Integrated HMI Parameter Explanation

Explain HMI parameters through machine behavior, not translation alone. For each meaningful parameter or manual button, build or mentally complete this model:

| ID | UI Chinese | UI English from screen | Unit/value | Controlled mechanism | SFC step | Confirmed behavior | Adjustment effect | Use scenario | Verification | Evidence | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|

Status rules:

- `Confirmed`: backed by screenshot, user confirmation, project file, photo, SFC, or visible machine evidence.
- `Mechanism-safe`: generally safe explanation without hidden options, numeric ranges, or unconfirmed sequence claims.
- `Needs question`: keep out of final customer HTML until confirmed.

Write customer-facing parameter explanations in this order:

1. Chinese label plus original UI English.
2. SFC step or transition.
3. Controlled action, mechanism, or process.
4. Adjustment effect.
5. Use scenario.
6. Verification method.
7. Caution only when safety, collision, heating, pressure, or timing risk exists.

Preserve original UI English as the anchor even if it is imperfect. Add a clearer explanation after it instead of replacing it. If a parameter changes timing, mode, speed, position, sensor handling, or actuator behavior, locate it on the SFC before writing final manual text. See `references/hmi-parameter-explanation.md` for the full integrated workflow.

### 3. Image Bilingualization

For each image:

- If the image already has bilingual labels or readable UI English, use it directly.
- If it has only Chinese callouts, create an English annotation plan first.
- Prefer local overlay on the original image for final output so the machine remains faithful.
- If an image-generation model is used, record whether it changed equipment structure. Use it for wording/layout only when fidelity is not good enough.

### 4. Manual Build

Use a concise customer-facing bilingual structure:

1. 设备概览 / Machine Overview
2. 安全事项 / Safety
3. 快速上手 / Quick Start
4. 机械调节 / Mechanical Adjustment
5. HMI 参数 / HMI Parameters
6. SFC 自动循环时序 / SFC Automatic Sequence
7. 手动调试 / Manual Debugging
8. 故障排查 / Troubleshooting
9. 附录 / Appendix

Use the original UI English as the anchor for HMI cards, then add clearer English explanation below it. Keep bilingual pairs close together.

### 5. Feedback Absorption

When feedback arrives:

- categorize it as SFC/timing, wording, visual layout, image annotation, missing content, or final export;
- update project management documents first if the feedback changes the authoritative logic;
- revise the HTML only after the source of truth is updated;
- preserve useful backups, but make the final file easy to identify.

### 6. Verification

Before final delivery, run an artifact audit:

- final HTML exists and uses relative image paths;
- no referenced image is missing;
- Chinese and English explanations are both present;
- no draft/internal/project-only wording is visible in final HTML;
- SFC is confirmed or uncertainty is excluded from customer pages;
- screenshots have been captured for desktop/mobile when feasible;
- exported PDF is A4 and page breaks do not split important cards or figures.

If this skill package is available, run:

```powershell
python scripts/audit_manual_project.py "C:\path\to\project"
```

## Output Shape

When producing a new project, finish with a concise status report:

```markdown
已完成：
- 项目管理文件：
- 最终 HTML：
- 双语标注图：
- 验证输出：

需要保留给后续复用的经验：
- [mechanism/SFC/image/verification note]
```

Do not end with a generic offer. Name the next concrete artifact if more work remains.

## Related References

- `references/manual-builder-workflow.md`: full workflow with stage gates and checklists.
- `references/hmi-parameter-explanation.md`: integrated HMI/SFC parameter explanation workflow.
- `references/project-structure.md`: project folder and file naming standard.
- `references/audit-checklist.md`: final verification checklist.
- `templates/项目看板.md`: reusable project board template.
- `templates/SFC时序审核稿.md`: reusable SFC review draft template.
