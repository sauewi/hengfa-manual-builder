# Integrated HMI Parameter Explanation

This reference is bundled inside `mg-industrial-equipment-manual-builder` so a manual project can handle HMI parameters, SFC timing, manual-operation screens, mode selectors, and customer-ready bilingual explanations without calling a separate HMI parameter skill.

## Purpose

Explain HMI parameters for non-standard heat-transfer and hot-stamping equipment in a way operators, customers, and service engineers can trust.

A good parameter explanation says:

- what the parameter controls,
- why it matters,
- when to adjust it,
- how to verify it,
- what evidence supports the explanation.

Do not treat HMI work as translation only. Translation is one layer; the main work is explaining machine behavior through the sequence.

## Required Input Model

Before writing final customer content, build the machine context from available evidence.

Minimum inputs:

- HMI screenshot or parameter list.
- Visible Chinese labels.
- Visible UI English labels, copied exactly.
- Machine type and main process.
- User-confirmed explanations for ambiguous parameters when available.
- Basic action sequence or SFC draft when parameters affect timing or debugging.

Strongly preferred inputs:

- Machine photos with key mechanisms labeled.
- Cycle description or action sequence.
- SFC / Sequential Function Chart showing steps, actions, transitions, and resets.
- Pneumatic, electrical, servo, sensor, or IO relationship when relevant.
- Known modes, hidden options, and safety limits.
- Customer audience and target language style.

If inputs are missing, do not fill gaps with confident-looking guesses. Create a prerequisite list, or if the user asked to continue without pausing, keep uncertain rows out of final customer HTML and use mechanism-safe wording only.

## SFC Layer

For non-standard automation equipment, build an SFC layer before final parameter explanations whenever possible.

Useful SFC draft:

| Step | Name | Entry condition | Active actions | Completion/transition | Related HMI parameters | Common debug symptom |
|---|---|---|---|---|---|---|
| S0 | Standby / 待机 | Power on, reset complete | Heater ready, air ready | Start command | Counter, reset | Cannot start |
| S1 |  |  |  |  |  |  |

Then map parameters to the SFC:

| HMI parameter | SFC step | What it changes | Upstream dependency | Downstream effect | Verification |
|---|---|---|---|---|---|
| Printing time | Pressing / hot stamping step | Contact/holding duration | Cylinder has reached position | Adhesion, overheat, cycle time | Single-cycle test and inspect first piece |

Use the SFC to answer:

- Which step does this parameter affect?
- Does it change an action, wait, transition, mode, reset, or alarm?
- What must happen before this parameter matters?
- What downstream defect or alarm appears if it is wrong?
- What manual action proves the adjustment worked?

Without the SFC layer, do not overstate timing parameters. Explain only the visible label and supported mechanism.

## Parameter Confirmation Table

Always make or mentally complete this table before final writing:

| ID | UI Chinese | UI English from screen | Unit/value | Controlled mechanism | SFC step | Confirmed behavior | Adjustment effect | Use scenario | Verification | Evidence | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 |  |  |  |  | S? |  |  |  |  | Screenshot/User/Photo/SFC/Inference | Confirmed/Needs question |

Status rules:

- `Confirmed`: backed by screenshot, user confirmation, project file, photo, SFC, or visible machine evidence.
- `Mechanism-safe`: general explanation is safe, but no specific hidden option, numeric range, or sequence claim is added.
- `Needs question`: do not publish as customer-facing fact.

## Professional Explanation Pattern

For each customer-ready parameter, explain in this order:

1. **Name**: Chinese label + original UI English.
2. **SFC position**: step or transition affected.
3. **Function**: mechanism, action, or process controlled.
4. **Adjustment effect**: what changes when value/mode changes.
5. **Use scenario**: when operators or service engineers adjust it.
6. **Verification**: how to test after adjustment.
7. **Caution**: only when safety, collision, heating, pressure, or timing risk exists.

Recommended bilingual shape:

```markdown
### 卷膜模式 / Eye/Time
中文：选择卷膜控制方式。Time 用于按时间控制卷膜距离；Eye 用于光电开关定位卷膜。
EN: Selects the film rewinding mode. Time controls rewinding by timed movement; Eye uses the photoelectric switch for positioning.
SFC: Film rewinding step / 收膜步骤.
使用场景 / Use: Time is suitable for fixed-distance rewinding; Eye is used when photoelectric positioning is required.
验证 / Check: Run a manual rewinding test and confirm the film stop position is stable.
```

Use the interface English as the anchor even if it is imperfect. If needed, add a clearer explanation after it, not instead of it.

## Evidence Discipline

Every explanation should fit one evidence type:

| Evidence type | How to write |
|---|---|
| Screenshot fact | Copy labels, options, units, and values exactly. |
| User-confirmed fact | Write confidently when the machine owner confirmed it. |
| Photo/mechanism fact | Explain visible mechanisms and actions. |
| SFC/timing fact | Explain where the parameter acts in the sequence and what transition it affects. |
| Similar-machine pattern | Use internally as a likely pattern; do not publish unless compatible and low-risk. |
| General mechanism | Use cautious wording and avoid hidden details. |
| Unknown | Ask or exclude from final customer text. |

## Must-Confirm Conditions

Confirm before finalizing, or keep out of final customer HTML, when a parameter involves:

- timing sequence: delay, reset, origin, return, entering seat, cylinder timing;
- mode switching: circular/profiling, timer/photoelectric, manual/auto, slow/fast;
- motion output: servo, fixture rotation, mold rotation, film rewinding, pressing, stamping;
- sensors: photoelectric switch, color mark, limit switch, origin sensor;
- process result: adhesion, overheat, missing print, wrinkles, dragging, registration drift;
- safety: hot parts, pneumatic pressure, manual jog, guards, emergency stop, interlocks;
- hidden options not shown in screenshots;
- ambiguous UI English such as `Delay Enter`, `Eye/Time`, `fill`, `RVE`, or misspelled labels.

Batch questions when the user wants confirmation. If the user asked to proceed without stopping, save the review gate as a project artifact and continue only with evidence-backed or mechanism-safe wording.

## Customer HTML Standard

When the final deliverable is customer-facing HTML:

- The HTML itself is the deliverable.
- Do not add timestamps, file paths, print/export advice, or internal uncertainty notes.
- Use deterministic text rendering; do not rely on image generation for Chinese/English text.
- Keep bilingual text readable on phone and desktop.
- Make parameter explanations self-contained enough for operators and service engineers.
- Do not include rows marked `Needs question`.
- Do not invent numeric setpoints, pressure values, temperatures, speed ranges, valve types, tube sizes, or hidden mode lists.

## Common Mistakes

- Treating HMI explanation as translation only.
- Explaining timing parameters without locating them in the SFC.
- Explaining every button, including obvious return/navigation keys.
- Turning a reasonable guess into a confident manual statement.
- Replacing original UI English with polished English and losing the screen anchor.
- Writing use scenarios before knowing the actual mechanism.
- Mixing internal confirmation notes into customer HTML.
- Letting downstream conversion concerns drive HTML content.

## Completion Checklist

- [ ] All visible parameters/buttons have been listed or intentionally excluded.
- [ ] Timing, delay, mode, reset, and motion parameters have been mapped to SFC steps or marked for confirmation.
- [ ] UI English has been copied from the screen when available.
- [ ] Ambiguous rows have been confirmed, kept mechanism-safe, or excluded.
- [ ] Each customer-facing explanation includes function, use scenario, and verification when possible.
- [ ] No unconfirmed machine behavior is written as fact.
- [ ] Final HTML is clean customer work.
