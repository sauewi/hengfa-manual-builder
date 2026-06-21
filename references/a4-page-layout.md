# Single-Framework A4 HTML

## A4 Is the Only Frame

Create explicit page containers, normally `.a4-sheet`, sized `210 mm x 297 mm`. Each page groups one operator decision, mechanism/HMI view, parameter family, or verification sequence. Do not merely add `@page { size: A4; }` to a continuous webpage.

Use the same page DOM and composition on phone, PC, screen preview, and print. A smaller viewport may proportionally scale or fit the A4 sheet, but must not introduce a second device frame, alternate page hierarchy, or structural reflow. The A4 page is already the framework.

Record the page map in `源稿/A4分页规划.md`:

| Page | Operator purpose | Content group | Primary image share |
|---:|---|---|---|
| 01 | Identify the manual | Cover and scope | Machine image at least 40% of page area |
| 02 | Inspect a mechanism | Structure image and observation notes | Image at least 75% of content width |

## Image-First Page Planning

Small images inside an A4 page become harder to inspect when the whole sheet is viewed on a phone. Fix this inside the A4 composition:

- give detailed mechanism photos and HMI screenshots at least 75% of A4 content width;
- prefer one full-width image band over two narrow detailed images side by side;
- when both mechanism and HMI need fine inspection, stack them as full-width bands or use consecutive pages;
- keep captions directly below images and shorten nearby prose;
- crop only irrelevant surroundings; do not crop away controlled mechanisms, labels, or observation points;
- use an image-first page followed by compact parameter cards when one page cannot keep both legible.

Two-column imagery is acceptable only when both images remain readable at the fitted A4 page size.

## Page Integrity

- Keep headings with their first content block.
- Do not split parameter cards, warnings, figures, table rows, or numbered steps.
- Use stable page numbers and deliberate safe margins.
- Measure every sheet; no content may cross the bottom safe area.
- Avoid decorative frames inside the A4 sheet. Use spacing and restrained rules instead of card-within-card composition.

## Verification

Test the same A4 pages at desktop and phone viewport widths:

- page count and content order stay identical;
- no alternate mobile page wrappers or duplicated content appear;
- every sheet preserves its aspect ratio and safe area;
- detailed primary images measure at least 75% of A4 content width;
- no page content overflows or is clipped;
- text, images, captions, and page numbers do not overlap;
- language modes and relative image loading still work.
