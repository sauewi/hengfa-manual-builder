# Final Audit Checklist

Run this checklist before calling the manual complete.

## Project Management

- [ ] Project board exists and lists folder structure, delivery principles, task status, and outputs.
- [ ] SFC review draft exists.
- [ ] SFC status is confirmed or all uncertain sequence claims are excluded from final HTML.
- [ ] Image bilingual annotation list exists if any Chinese-only callout image is used.
- [ ] HTML chapter structure exists or is reflected in the project board.

## Final HTML

- [ ] Final HTML exists at the project root.
- [ ] It is not a draft or backup file.
- [ ] Image references are relative paths.
- [ ] Referenced image files exist.
- [ ] Chinese and English explanations appear as paired content.
- [ ] Original HMI UI English is preserved where shown in screenshots.
- [ ] No customer-facing draft markers remain.
- [ ] No internal-only project notes are visible.

## Content

- [ ] SFC sequence supports HMI parameter explanations.
- [ ] Important HMI parameters have a confirmation table or equivalent internal mapping.
- [ ] HMI explanations preserve original UI English when visible on the screen.
- [ ] Each customer-facing HMI explanation has function, use scenario, and verification when possible.
- [ ] Rows that would be `Needs question` are excluded from final customer HTML.
- [ ] Timing parameters identify their action point or time origin.
- [ ] Safety bypass controls are described as debugging-only / not for normal production.
- [ ] Uninstalled or unused mechanisms are not written as normal operation steps.
- [ ] No unconfirmed numeric setpoints are invented.

## Images

- [ ] Chinese-only images have bilingual output images or HTML-side English explanation.
- [ ] Image-generation outputs are not used if they redraw or distort machine structure.
- [ ] Final images remain readable on mobile.

## Verification

- [ ] Desktop screenshot captured when feasible.
- [ ] Mobile screenshot captured when feasible.
- [ ] PDF exported only if requested or useful.
- [ ] PDF is A4 when requested.
- [ ] PDF page breaks do not split critical cards, figures, or safety tips.

