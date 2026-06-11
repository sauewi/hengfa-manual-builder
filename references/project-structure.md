# Project Structure Standard

Use this standard for Hengfa-style heat-transfer manual projects.

## Folders

| Folder | Purpose | Notes |
|---|---|---|
| `设备图片` | Machine overview and structure images | Use original images as evidence. |
| `物理调节` | Mechanical adjustment photos | Chinese-only callouts usually need bilingual overlays. |
| `HMI界面` | HMI screenshots | Preserve original UI English. |
| `双语标注图` | Bilingual annotated output images | Final HTML should reference these when source images were Chinese-only. |
| `源稿` | Source drafts and structured lists | Keep chapter plans and image annotation lists here. |
| `项目管理` | Project board, SFC review, feedback handling | Treat as the source of truth for workflow state. |
| `输出` | Screenshots, PDFs, contact sheets, verification artifacts | Keep final checks here. |
| `临时文件` | Scripts and temporary generated samples | Do not reference temporary files in final HTML. |

## Naming

- Final HTML: `[机型]说明书_中英双语.html`
- Final PDF if requested: `[机型]说明书_中英双语.pdf`
- Draft HTML: append `_草稿`
- Backups: append reason, such as `_旧复杂版备份`
- Bilingual image: `[原图名]_双语.png`
- PDF pagination overview: `输出/PDF分页总览.png`

## Management Files

- `项目管理/项目看板.md`
- `项目管理/SFC时序审核稿.md`
- `项目管理/参数联动关系_PLC备忘.md` when internal timing/linkage logic needs preservation
- `源稿/图片双语注释清单.md`
- `源稿/HTML章节结构.md`

