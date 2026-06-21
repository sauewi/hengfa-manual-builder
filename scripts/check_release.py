#!/usr/bin/env python3
"""Check that this skill repository is ready for public release."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


TEXT_EXTENSIONS = {
    ".md",
    ".py",
    ".json",
    ".yml",
    ".yaml",
    ".txt",
    ".gitignore",
}

TEXT_FILENAMES = {"LICENSE", ".gitignore"}

REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "README.md",
    "LICENSE",
    "PUBLISHING.md",
    "evals/evals.json",
    "references/manual-builder-workflow.md",
    "references/hmi-parameter-explanation.md",
    "references/project-structure.md",
    "references/audit-checklist.md",
    "references/html-only-delivery.md",
    "references/a4-page-layout.md",
    "references/rework-prevention.md",
    "scripts/audit_manual_project.py",
    "scripts/check_release.py",
    "templates/项目看板.md",
    "templates/SFC时序审核稿.md",
    "templates/交接摘要.md",
    "templates/A4分页规划.md",
]

LOCAL_USER_FRAGMENT = "114" + "05"
LOCAL_PROJECT_NAME = "大面板" + "热转印机说明书"
SOURCE_PROJECT_MODEL = "HF-" + "1000"
LEGACY_SKILL_NAME = "thermal-transfer-" + "manual"
MERGED_HMI_SKILL_NAME = "hmi-param-" + "explainer"
CURRENT_SKILL_NAME = "mg-industrial-equipment-manual-builder"
OLD_SKILL_NAME = "hengfa-manual-" + "builder"
OLD_SKILL_TITLE = "Hengfa Manual " + "Builder"
CREDENTIAL_PATTERN = (
    "api[_-]?key|sec" + "ret|pass" + "word|(?:access|auth|bearer|refresh)[_-]?to" + "ken"
)

SENSITIVE_PATTERNS = [
    (re.compile(r"C:\\Users\\[^\\\s]+", re.I), "personal Windows user path"),
    (re.compile(re.escape(LOCAL_USER_FRAGMENT)), "local Windows username fragment"),
    (re.compile(re.escape(LOCAL_PROJECT_NAME)), "specific local project name"),
    (re.compile(re.escape(SOURCE_PROJECT_MODEL)), "specific source-project model"),
    (re.compile(CREDENTIAL_PATTERN, re.I), "credential keyword"),
]

BINARY_SUFFIXES = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".pdf",
    ".docx",
    ".pptx",
    ".xlsx",
    ".zip",
}


def iter_files(root: Path) -> list[Path]:
    return [
        p
        for p in root.rglob("*")
        if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts
    ]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def check_repo(root: Path) -> dict:
    failures: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            failures.append(f"Missing required file: {rel}")

    files = iter_files(root)
    binary_files = [
        str(p.relative_to(root)).replace("\\", "/")
        for p in files
        if p.suffix.lower() in BINARY_SUFFIXES
    ]
    if binary_files:
        failures.append("Binary/private-source candidates are bundled: " + ", ".join(binary_files))

    text_hits: list[dict[str, str]] = []
    external_skill_hits: list[str] = []
    for path in files:
        rel = str(path.relative_to(root)).replace("\\", "/")
        if path.suffix.lower() not in TEXT_EXTENSIONS and path.name not in TEXT_FILENAMES:
            warnings.append(f"Review non-standard file type: {rel}")
            continue
        text = read_text(path)
        for regex, label in SENSITIVE_PATTERNS:
            for match in regex.finditer(text):
                line_no = text.count("\n", 0, match.start()) + 1
                text_hits.append({"file": rel, "line": str(line_no), "kind": label})
        if path.name != "check_release.py":
            if OLD_SKILL_NAME in text or OLD_SKILL_TITLE in text:
                external_skill_hits.append(f"{rel}: old skill identity")
            if MERGED_HMI_SKILL_NAME in text:
                external_skill_hits.append(f"{rel}: merged HMI skill reference")
            if LEGACY_SKILL_NAME in text:
                external_skill_hits.append(f"{rel}: legacy manual skill reference")

    if text_hits:
        failures.append("Sensitive text patterns found.")
    if external_skill_hits:
        failures.append("External skill dependency references found: " + ", ".join(external_skill_hits))

    try:
        evals = json.loads(read_text(root / "evals/evals.json"))
        if evals.get("skill_name") != CURRENT_SKILL_NAME:
            failures.append("evals/evals.json skill_name mismatch.")
        if len(evals.get("evals", [])) < 3:
            failures.append("Expected at least 3 eval prompts.")
    except Exception as exc:  # noqa: BLE001 - report validation details.
        failures.append(f"Invalid evals/evals.json: {exc}")

    skill_text = read_text(root / "SKILL.md") if (root / "SKILL.md").exists() else ""
    if LEGACY_SKILL_NAME in skill_text or MERGED_HMI_SKILL_NAME in skill_text:
        failures.append("SKILL.md still references an external skill that should be integrated.")
    if not re.search(rf"(?m)^name:\s*{re.escape(CURRENT_SKILL_NAME)}\s*$", skill_text):
        failures.append("SKILL.md name does not match the release identity.")
    if not re.search(r'(?m)^\s+version:\s*["\']?0\.7\.0["\']?\s*$', skill_text):
        failures.append("SKILL.md version is not 0.7.0.")

    agent_path = root / "agents/openai.yaml"
    if agent_path.is_file():
        agent_text = read_text(agent_path)
        if "MG Industrial Equipment Manual Builder" not in agent_text:
            failures.append("agents/openai.yaml display name mismatch.")
        if f"${CURRENT_SKILL_NAME}" not in agent_text:
            failures.append("agents/openai.yaml default prompt does not invoke this skill.")

    return {
        "passed": not failures,
        "file_count": len(files),
        "failures": failures,
        "warnings": warnings,
        "sensitive_hits": text_hits,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", nargs="?", default=".", help="Repository root")
    parser.add_argument("--json", action="store_true", help="Print JSON report")
    args = parser.parse_args()

    report = check_repo(Path(args.repo).resolve())
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("Release check:", "PASS" if report["passed"] else "FAIL")
        print(f"Files checked: {report['file_count']}")
        for warning in report["warnings"]:
            print("WARNING:", warning)
        for failure in report["failures"]:
            print("FAILURE:", failure)
        for hit in report["sensitive_hits"]:
            print(f"SENSITIVE: {hit['file']}:{hit['line']} {hit['kind']}")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
