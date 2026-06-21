# Final Audit Checklist

Run this checklist before calling the manual complete.

## Project Management

- [ ] Project board exists and lists folder structure, delivery principles, task status, and outputs.
- [ ] Compact handoff summary exists and reflects the current confirmed phase state.
- [ ] SFC review draft exists.
- [ ] SFC status is confirmed or all uncertain sequence claims are excluded from final HTML.
- [ ] Image bilingual annotation list exists if any Chinese-only callout image is used.
- [ ] HTML chapter structure exists or is reflected in the project board.
- [ ] A4 page map exists and lists each page's operator purpose and content group.

## Final HTML

- [ ] Final HTML exists at the project root.
- [ ] It is not a draft or backup file.
- [ ] Image references are relative paths.
- [ ] Referenced image files exist.
- [ ] Chinese and English explanations appear as paired content.
- [ ] Original HMI UI English is preserved where shown in screenshots.
- [ ] No customer-facing draft markers remain.
- [ ] No internal-only project notes are visible.
- [ ] Content is grouped into explicit A4 page containers rather than relying only on automatic print breaks.

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
- [ ] A4 mechanism/HMI imagery remains legible at fitted-page size.
- [ ] Detailed primary images occupy at least 75% of A4 content width; narrow side-by-side detail images are avoided.

## Verification

- [ ] Mobile screenshot captured when feasible.
- [ ] Every A4 page has zero content overflow.
- [ ] Phone and PC preserve the same A4 page count, order, and composition without nested device frames.
- [ ] Static audit and A4 screen checks at desktop/phone viewport widths pass.
- [ ] Tool output is concise; full HTML and unchanged large files were not repeatedly printed.
- [ ] The approved HTML is the only customer deliverable.

