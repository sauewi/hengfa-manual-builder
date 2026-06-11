# Publishing Checklist

Use this before making `hengfa-manual-builder` public.

## Remove Local Data

- [ ] No personal Windows username appears in skill files.
- [ ] No customer-only project path appears in skill files.
- [ ] No private machine photo, HMI screenshot, PDF, or feedback image is bundled.
- [ ] Examples describe expected inputs without exposing private files or exact customer project names.

## Keep The Skill Useful

- [ ] `SKILL.md` explains when to trigger the skill.
- [ ] The workflow reference is inside `references/`.
- [ ] Templates are reusable and do not contain one-project-only facts.
- [ ] The audit script works with any compatible manual project path.
- [ ] Eval prompts cover SFC, bilingual image annotation, and final PDF/page-break verification.

## License

- [ ] Confirm `LICENSE` matches the intended open-source license.
- [ ] Keep generated customer deliverables outside this repository.
