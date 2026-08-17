#!/usr/bin/env python3
"""Validate the repository's single portable skill without extra packages."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "meeting-runner"
SKILL_FILE = SKILL_ROOT / "SKILL.md"
EXPECTED_FILES = frozenset(
    {
        ".github/workflows/check.yml",
        ".gitignore",
        "AGENTS.md",
        "LICENSE",
        "README.md",
        "scripts/check.py",
        "skills/meeting-runner/SKILL.md",
        "skills/meeting-runner/agents/openai.yaml",
        "skills/meeting-runner/assets/pre-call-brief-template.md",
        "skills/meeting-runner/references/canonical-meeting-notes.md",
        "skills/meeting-runner/references/preparation-workflow.md",
        "skills/meeting-runner/references/synthesis-workflow.md",
        "skills/meeting-runner/references/transcript-ingestion.md",
        "tests/test_check.py",
    }
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def repository_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if (path.is_file() or path.is_symlink())
        and ".git" not in path.parts
        and "__pycache__" not in path.parts
    )


def validate_shape() -> list[str]:
    errors: list[str] = []
    files = repository_files()
    actual_files = {path.relative_to(ROOT).as_posix() for path in files}
    errors.extend(
        f"missing required file: {relative_path}"
        for relative_path in sorted(EXPECTED_FILES - actual_files)
    )
    errors.extend(
        f"unexpected repository file: {relative_path}"
        for relative_path in sorted(actual_files - EXPECTED_FILES)
    )
    for path in files:
        relative_path = path.relative_to(ROOT)
        if path.is_symlink():
            errors.append(f"symbolic links are not allowed: {relative_path}")
            continue
        try:
            path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"non-UTF-8 or binary file is not allowed: {relative_path}")
    return errors


def validate_frontmatter() -> list[str]:
    if not SKILL_FILE.is_file():
        return ["cannot validate missing skills/meeting-runner/SKILL.md"]

    text = SKILL_FILE.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        return ["SKILL.md must begin with closed YAML frontmatter"]

    fields: dict[str, str] = {}
    for line in parts[1].splitlines():
        if not line.strip():
            continue
        match = re.fullmatch(r"([a-z][a-z0-9_-]*):\s*(.+)", line)
        if not match:
            return [f"unsupported SKILL.md frontmatter line: {line!r}"]
        if match.group(1) in fields:
            return [f"duplicate SKILL.md frontmatter field: {match.group(1)}"]
        fields[match.group(1)] = match.group(2).strip()

    errors: list[str] = []
    if set(fields) != {"name", "description"}:
        errors.append("SKILL.md frontmatter must contain only name and description")
    if fields.get("name") != "meeting-runner":
        errors.append("SKILL.md name must be meeting-runner")
    if not fields.get("description"):
        errors.append("SKILL.md description must be non-empty")
    return errors


def validate_agent_metadata() -> list[str]:
    metadata_file = SKILL_ROOT / "agents" / "openai.yaml"
    if not metadata_file.is_file():
        return ["cannot validate missing agents/openai.yaml"]

    lines = [
        line
        for line in metadata_file.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    expected_patterns = [
        r"interface:",
        r'  display_name: "([^"]+)"',
        r'  short_description: "([^"]+)"',
        r'  default_prompt: "([^"]+)"',
        r"policy:",
        r"  allow_implicit_invocation: true",
    ]
    if len(lines) != len(expected_patterns):
        return ["agents/openai.yaml must contain the required interface and policy"]

    matches = [
        re.fullmatch(pattern, line)
        for pattern, line in zip(expected_patterns, lines)
    ]
    if not all(matches):
        return ["agents/openai.yaml has malformed or unsupported metadata"]

    display_name = matches[1].group(1)
    short_description = matches[2].group(1)
    default_prompt = matches[3].group(1)
    errors: list[str] = []
    if not display_name.strip():
        errors.append("agents/openai.yaml display_name must be non-empty")
    if not 25 <= len(short_description) <= 64:
        errors.append("agents/openai.yaml short_description must be 25-64 characters")
    if "$meeting-runner" not in default_prompt:
        errors.append("agents/openai.yaml default_prompt must mention $meeting-runner")
    return errors


def validate_links(files: list[Path]) -> list[str]:
    errors: list[str] = []
    link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for path in files:
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for raw_target in link_pattern.findall(text):
            target = raw_target.strip().split("#", 1)[0]
            if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                continue
            resolved = (path.parent / unquote(target)).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(
                    f"relative link escapes repository in "
                    f"{path.relative_to(ROOT)}: {raw_target}"
                )
                continue
            if not resolved.exists():
                errors.append(
                    f"broken relative link in {path.relative_to(ROOT)}: {raw_target}"
                )
    return errors


def validate_sensitive_content(files: list[Path]) -> list[str]:
    errors: list[str] = []
    built_in_patterns = {
        "macOS user path": re.compile(re.escape("/" + "Users/")),
        "Windows user path": re.compile(re.escape("C:" + "\\Users\\"), re.I),
        "private Notion page URL": re.compile(
            re.escape("app." + "notion.com/p/"), re.I
        ),
        "legacy Notion page URL": re.compile(re.escape("notion." + "so/"), re.I),
        "32-character hexadecimal identifier": re.compile(r"\b[0-9a-f]{32}\b", re.I),
        "UUID-like identifier": re.compile(
            r"\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-"
            r"[89ab][0-9a-f]{3}-[0-9a-f]{12}\b",
            re.I,
        ),
        "private key header": re.compile("BE" + "GIN " + ".*PRI" + "VATE KEY"),
        "GitHub token": re.compile(r"\bgh" + r"[opsu]_[A-Za-z0-9]{20,}\b"),
        "GitHub fine-grained token": re.compile(
            r"\bgithub_" + r"pat_[A-Za-z0-9_]{20,}\b"
        ),
        "OpenAI-style secret": re.compile(r"\bsk" + r"-[A-Za-z0-9_-]{20,}\b"),
        "Slack token": re.compile(r"\bxo" + r"x[baprs]-[A-Za-z0-9-]{10,}\b"),
        "bearer token": re.compile(
            r"\bBear" + r"er\s+[A-Za-z0-9._~+/-]{20,}\b", re.I
        ),
        "credential assignment": re.compile(
            r"\b(?:pass(?:word)?|api[_-]?key|secret|token)\s*[:=]\s*"
            r"[\"']?[A-Za-z0-9_./+=-]{12,}",
            re.I,
        ),
        "AWS access key": re.compile(r"\bAKIA" + r"[A-Z0-9]{16}\b"),
    }
    configured_terms = [
        term.strip()
        for term in os.environ.get("ORGOS_SKILLS_PROHIBITED_TERMS", "").split(",")
        if term.strip()
    ]
    patterns = dict(built_in_patterns)
    patterns.update(
        {
            f"configured prohibited term {term!r}": re.compile(re.escape(term), re.I)
            for term in configured_terms
        }
    )

    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in patterns.items():
            if pattern.search(text):
                errors.append(f"{label} found in {path.relative_to(ROOT)}")
    return errors


def main() -> int:
    files = repository_files()
    errors = []
    errors.extend(validate_shape())
    errors.extend(validate_frontmatter())
    errors.extend(validate_agent_metadata())
    errors.extend(validate_links(files))
    errors.extend(validate_sensitive_content(files))
    if errors:
        for error in errors:
            fail(error)
        return 1
    print("Validated one portable skill: meeting-runner")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
