#!/usr/bin/env python3
"""Audit a Hengfa-style bilingual HTML manual project.

The script is intentionally conservative. It reports missing evidence and
customer-facing risk markers; it does not try to prove machine behavior.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED_DIRS = [
    "设备图片",
    "物理调节",
    "HMI界面",
    "双语标注图",
    "源稿",
    "项目管理",
    "输出",
    "临时文件",
]

REQUIRED_FILES = [
    Path("项目管理") / "项目看板.md",
    Path("项目管理") / "SFC时序审核稿.md",
    Path("源稿") / "图片双语注释清单.md",
    Path("源稿") / "HTML章节结构.md",
]

BAD_FINAL_TERMS = [
    "TODO",
    "待审核",
    "待确认",
    "草稿",
    "源稿",
    "内部",
    "Needs question",
    "Draft SFC",
    "待 SFC 审核",
    "参数联动",
    "PLC备忘",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def find_final_html(project: Path) -> Path | None:
    candidates = []
    for path in project.glob("*.html"):
        name = path.name
        if "草稿" in name or "备份" in name or "旧" in name:
            continue
        if "中英双语" in name:
            candidates.append(path)
    if not candidates:
        return None
    candidates.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return candidates[0]


def image_refs(html: str) -> list[str]:
    refs = []
    for match in re.finditer(r"""<img\b[^>]*\bsrc=["']([^"']+)["']""", html, re.I):
        src = match.group(1).strip()
        if src.startswith(("http://", "https://", "data:", "file:")):
            refs.append(src)
        else:
            refs.append(src.replace("/", "\\"))
    return refs


def audit(project: Path) -> dict:
    result: dict[str, object] = {
        "project": str(project),
        "checks": {},
        "warnings": [],
        "failures": [],
    }
    checks: dict[str, object] = result["checks"]  # type: ignore[assignment]
    failures: list[str] = result["failures"]  # type: ignore[assignment]
    warnings: list[str] = result["warnings"]  # type: ignore[assignment]

    if not project.exists():
        failures.append("Project path does not exist.")
        return result

    missing_dirs = [name for name in REQUIRED_DIRS if not (project / name).is_dir()]
    checks["missing_dirs"] = missing_dirs
    if missing_dirs:
        failures.append("Missing required folders: " + ", ".join(missing_dirs))

    missing_files = [str(path) for path in REQUIRED_FILES if not (project / path).is_file()]
    checks["missing_management_files"] = missing_files
    if missing_files:
        failures.append("Missing management/source files: " + ", ".join(missing_files))

    final_html = find_final_html(project)
    checks["final_html"] = str(final_html) if final_html else None
    if not final_html:
        failures.append("No final bilingual HTML found at project root.")
        return result

    html = read_text(final_html)
    refs = image_refs(html)
    missing_refs = []
    absolute_refs = []
    for ref in refs:
        if re.match(r"^[A-Za-z]:\\", ref) or ref.startswith(("http://", "https://", "file:")):
            absolute_refs.append(ref)
            continue
        if not (project / ref).exists():
            missing_refs.append(ref)
    checks["image_ref_count"] = len(refs)
    checks["missing_image_refs"] = missing_refs
    checks["absolute_or_external_image_refs"] = absolute_refs
    if missing_refs:
        failures.append("Final HTML has missing image references.")
    if absolute_refs:
        warnings.append("Final HTML has absolute or external image references.")

    bad_terms = [term for term in BAD_FINAL_TERMS if term in html]
    checks["bad_final_terms"] = bad_terms
    if bad_terms:
        failures.append("Final HTML contains customer-facing draft/internal terms.")

    en_markers = len(re.findall(r"\bEN:|class=\"en\"|UI English|English", html))
    zh_markers = len(re.findall(r"[\u4e00-\u9fff]", html))
    checks["english_marker_count"] = en_markers
    checks["chinese_character_count"] = zh_markers
    if en_markers < 10 or zh_markers < 100:
        warnings.append("Bilingual coverage markers look low; inspect manually.")

    checks["has_print_css"] = "@media print" in html
    checks["has_page_break_protection"] = "break-inside" in html or "page-break-inside" in html
    if not checks["has_print_css"]:
        warnings.append("No print CSS found.")

    sfc_path = project / "项目管理" / "SFC时序审核稿.md"
    if sfc_path.exists():
        sfc_text = read_text(sfc_path)
        checks["sfc_status_confirmed"] = "确认稿" in sfc_text and "已吸收用户审核意见" in sfc_text
        checks["sfc_confirmed_parameter_rows"] = sfc_text.count("已确认")
        if not checks["sfc_status_confirmed"]:
            warnings.append("SFC file does not look confirmed.")

    pdfs = list(project.glob("*中英双语.pdf")) + list((project / "输出").glob("*中英双语.pdf"))
    checks["pdf_count"] = len(pdfs)
    checks["pdf_files"] = [str(path) for path in pdfs]

    result["passed"] = not failures
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help="Path to the manual project folder")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    args = parser.parse_args()

    report = audit(Path(args.project))
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        status = "PASS" if report.get("passed") else "FAIL"
        print(f"Audit status: {status}")
        for key, value in report["checks"].items():  # type: ignore[index]
            print(f"- {key}: {value}")
        for warning in report["warnings"]:  # type: ignore[index]
            print(f"WARNING: {warning}")
        for failure in report["failures"]:  # type: ignore[index]
            print(f"FAILURE: {failure}")
    return 0 if report.get("passed") else 1


if __name__ == "__main__":
    sys.exit(main())

