#!/usr/bin/env python3
"""Validate the portable catalog, resources, integrity and sensitive-content boundary."""

from __future__ import annotations

import os
import hashlib
import json
import stat
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "meeting-runner"
SKILL_FILE = SKILL_ROOT / "SKILL.md"
SKILL_NAMES = frozenset({"meeting-runner", "to-spec", "to-tickets", "triage", "handoff", "repo-review", "repo-document", "diagnose", "codebase-design", "writing-for-agents", "setup-agent-workflows", "qualify-opportunity", "workflow-guide", "to-questionnaire", "workflow-retro"})
EXACT_UPSTREAM = frozenset({"writing-for-agents", "codebase-design"})
ATTRIBUTED_SKILLS = frozenset({"to-spec", "to-tickets", "triage", "repo-review", "diagnose", "codebase-design", "writing-for-agents", "workflow-guide", "to-questionnaire", "workflow-retro"})
ADAPTED_SKILLS = ATTRIBUTED_SKILLS | {"handoff", "setup-agent-workflows"}
ROOT_FILES = frozenset({".github/workflows/check.yml", ".gitignore", "AGENTS.md", "LICENSE", "NOTICE.md", "LICENSES/Matt-Pocock-MIT.txt", "README.md", "CONTRACT.md", "catalog.json", "scripts/check.py", "scripts/install.py", "scripts/build_plugin.py", "distribution/plugin.json", "distribution/release.json", "distribution/upstream-exact-files.json", "tests/test_check.py", "tests/test_install.py", "tests/test_qualification.py", "tests/test_plugin.py", "tests/fixtures/plugin-1.0.0.json", "docs/ALIGNMENT.md", "docs/PLUGIN_DISTRIBUTION.md", ".agents/workspace-standards.md", ".agents/coding-standards.md", ".agents/review-standards.md", ".agents/document-standards.md"})


def is_linked_path(path: Path) -> bool:
    """Reject symlinks and Windows reparse points, including directory junctions."""
    if path.is_symlink():
        return True
    try:
        attributes = getattr(path.lstat(), "st_file_attributes", 0)
        return bool(attributes & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400))
    except FileNotFoundError:
        return False


def safe_regular_file(path: Path) -> bool:
    """Refuse a linked/special resource or any linked parent before reading it."""
    try:
        relative = path.relative_to(ROOT)
        current = ROOT
        for part in relative.parts:
            current = current / part
            if is_linked_path(current):
                return False
        return stat.S_ISREG(path.lstat().st_mode)
    except (ValueError, OSError):
        return False


def expected_files() -> frozenset[str]:
    """Read inventory safely; malformed catalogs are reported by validation."""
    catalog_path = ROOT / "catalog.json"
    if not safe_regular_file(catalog_path):
        return ROOT_FILES
    try:
        entries = json.loads(catalog_path.read_text())["skills"]
        resources = frozenset(
            f"skills/{name}/{path}"
            for name, entry in entries.items()
            for path in entry["files"]
        )
        return ROOT_FILES | resources
    except (ValueError, KeyError, TypeError, AttributeError, OSError):
        return ROOT_FILES


# A stable source inventory is useful for clean validation/installation fixtures.
EXPECTED_FILES = expected_files()


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def repository_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if (not path.is_dir() or is_linked_path(path))
        and ".git" not in path.parts
        and "__pycache__" not in path.parts
    )


def validate_shape() -> list[str]:
    errors: list[str] = []
    files = repository_files()
    actual_files = {path.relative_to(ROOT).as_posix() for path in files}
    declared_files = expected_files()
    errors.extend(
        f"missing required file: {relative_path}"
        for relative_path in sorted(declared_files - actual_files)
    )
    errors.extend(
        f"unexpected repository file: {relative_path}"
        for relative_path in sorted(actual_files - declared_files)
    )
    for path in files:
        relative_path = path.relative_to(ROOT)
        if is_linked_path(path) or not stat.S_ISREG(path.lstat().st_mode):
            errors.append(f"non-regular files or symbolic links are not allowed: {relative_path}")
            continue
        try:
            path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"non-UTF-8 or binary file is not allowed: {relative_path}")
    return errors


def validate_frontmatter() -> list[str]:
    return [error for name in sorted(SKILL_NAMES) for error in validate_skill_frontmatter(name)]


def validate_skill_frontmatter(name: str) -> list[str]:
    skill_file = ROOT / "skills" / name / "SKILL.md"
    if not safe_regular_file(skill_file):
        return [f"cannot validate missing or linked skills/{name}/SKILL.md"]

    text = skill_file.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        return ["SKILL.md must begin with closed YAML frontmatter"]

    fields: dict[str, str] = {}
    in_metadata = False
    for line in parts[1].splitlines():
        if not line.strip():
            continue
        if in_metadata and line.startswith("  "):
            match = re.fullmatch(r"  invocation: (auto|manual)", line)
            if not match or "metadata.invocation" in fields:
                return [f"unsupported or duplicate metadata line: {line!r}"]
            fields["metadata.invocation"] = match.group(1)
            continue
        in_metadata = False
        if line == "metadata:":
            if "metadata" in fields:
                return ["duplicate SKILL.md frontmatter field: metadata"]
            fields["metadata"] = "mapping"
            in_metadata = True
            continue
        match = re.fullmatch(r"([a-z][a-z0-9_-]*):\s*(.+)", line)
        if not match:
            return [f"unsupported SKILL.md frontmatter line: {line!r}"]
        if match.group(1) in fields:
            return [f"duplicate SKILL.md frontmatter field: {match.group(1)}"]
        fields[match.group(1)] = match.group(2).strip()

    errors: list[str] = []
    allowed = {"name", "description", "disable-model-invocation", "metadata", "metadata.invocation", "user-invocable", "argument-hint"}
    if not {"name", "description"} <= fields.keys() or fields.keys() - allowed:
        errors.append("SKILL.md has missing required or unsupported frontmatter")
    for field in ("disable-model-invocation", "user-invocable"):
        if field in fields and fields[field] not in {"true", "false"}:
            errors.append(f"{field} must be true or false")
    if "metadata" in fields and "metadata.invocation" not in fields:
        errors.append("metadata requires invocation")
    if "metadata.invocation" in fields:
        expected_disable = "true" if fields["metadata.invocation"] == "manual" else "false"
        if fields.get("disable-model-invocation") != expected_disable:
            errors.append("invocation metadata and disable-model-invocation disagree")
    if fields.get("name") != name:
        errors.append(f"SKILL.md name must be {name}")
    if not fields.get("description"):
        errors.append("SKILL.md description must be non-empty")
    return errors


def validate_agent_metadata() -> list[str]:
    return [error for name in sorted(SKILL_NAMES) for error in validate_skill_metadata(name)]


def validate_skill_metadata(name: str) -> list[str]:
    metadata_file = ROOT / "skills" / name / "agents" / "openai.yaml"
    if not safe_regular_file(metadata_file):
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
        r"  allow_implicit_invocation: (?:true|false)",
    ]
    if name in EXACT_UPSTREAM:
        expected_patterns = expected_patterns[:3]
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
    default_prompt = matches[3].group(1) if name not in EXACT_UPSTREAM else ""
    errors: list[str] = []
    if not display_name.strip():
        errors.append("agents/openai.yaml display_name must be non-empty")
    if not short_description.strip() or len(short_description) > 64:
        errors.append("agents/openai.yaml short_description must be nonempty and at most 64 characters")
    if name not in EXACT_UPSTREAM and f"${name}" not in default_prompt:
        errors.append(f"agents/openai.yaml default_prompt must mention ${name}")
    skill_file = ROOT / "skills" / name / "SKILL.md"
    if not safe_regular_file(skill_file):
        return errors + [f"cannot check invocation policy: {name}"]
    parts = skill_file.read_text().split("---", 2)
    if len(parts) != 3:
        return errors + [f"cannot check malformed frontmatter policy: {name}"]
    frontmatter = parts[1]
    manual = "disable-model-invocation: true" in frontmatter
    if name not in EXACT_UPSTREAM and (lines[-1].endswith("false")) != manual:
        errors.append(f"invocation policy disagrees with frontmatter: {name}")
    return errors


def validate_links(files: list[Path]) -> list[str]:
    errors: list[str] = []
    link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for path in files:
        if path.suffix.lower() != ".md" or not safe_regular_file(path):
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
        if not safe_regular_file(path):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in patterns.items():
            if pattern.search(text):
                errors.append(f"{label} found in {path.relative_to(ROOT)}")
    return errors


def validate_catalog() -> list[str]:
    """Verify declared resources and dependency closure against source bytes."""
    errors: list[str] = []
    catalog_path = ROOT / "catalog.json"
    if not safe_regular_file(catalog_path):
        return ["catalog.json must be a regular file"]
    try:
        catalog = json.loads(catalog_path.read_text())
        entries = catalog["skills"]
        if catalog["schemaVersion"] != 1 or not isinstance(entries, dict):
            return ["unsupported catalog schema"]
        if set(entries) != SKILL_NAMES:
            errors.append("catalog must contain the selected fifteen skills")
        notices = catalog.get("packageNotices")
        if not isinstance(notices, dict) or set(notices) != {"LICENSES/Matt-Pocock-MIT.txt"}:
            errors.append("required package notice inventory missing")
            notices = {}
        for relative, digest in notices.items():
            path = ROOT / relative
            if not safe_regular_file(path) or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                errors.append(f"package notice digest mismatch: {relative}")
        for name, entry in entries.items():
            if name not in SKILL_NAMES:
                continue
            if not isinstance(entry, dict) or not isinstance(entry.get("files"), dict):
                errors.append(f"invalid resource inventory: {name}")
                continue
            if any(not isinstance(entry.get(field), list) or any(not isinstance(item, str) for item in entry[field]) for field in ("requires", "conditional")):
                errors.append(f"invalid dependencies: {name}")
                continue
            for dependency in entry["requires"] + entry["conditional"]:
                if dependency not in entries or dependency == name:
                    errors.append(f"unavailable dependency: {name} -> {dependency}")
            for relative, expected in entry["files"].items():
                path = Path(relative)
                if path.is_absolute() or ".." in path.parts or not path.parts:
                    errors.append(f"invalid resource path: {name}/{relative}")
                    continue
                resource = ROOT / "skills" / name / path
                if not safe_regular_file(resource):
                    errors.append(f"missing or non-regular resource: {name}/{relative}")
                elif not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected) or hashlib.sha256(resource.read_bytes()).hexdigest() != expected:
                    errors.append(f"resource digest mismatch: {name}/{relative}")
            if name in EXACT_UPSTREAM:
                pin_path = ROOT / "distribution/upstream-exact-files.json"
                if not safe_regular_file(pin_path):
                    errors.append("upstream pin inventory must be a regular file")
                    continue
                pins = json.loads(pin_path.read_text())[name]
                if entry["files"] != pins:
                    errors.append(f"complete upstream folder differs from pinned resources: {name}")
            notice = entry["upstreamNotice"]
            if name in ATTRIBUTED_SKILLS - EXACT_UPSTREAM and notice != "UPSTREAM-LICENSE.txt":
                errors.append(f"required upstream attribution missing: {name}")
            if notice is not None and notice not in entry["files"]:
                errors.append(f"missing attribution notice: {name}")
            if name in {"handoff", "setup-agent-workflows"} | EXACT_UPSTREAM and entry.get("packageNotice") not in notices:
                errors.append(f"required package attribution missing: {name}")
            provenance = entry.get("provenance")
            if not isinstance(provenance, dict) or not provenance.get("owner") or not provenance.get("clearance"):
                errors.append(f"missing source provenance: {name}")
            elif name not in {"meeting-runner", "qualify-opportunity"} and (
                provenance.get("mode") != "byte-identical" or provenance.get("owner") != "xp-skills"
                or not re.fullmatch(r"[0-9a-f]{40}", str(provenance.get("revision", "")))
            ):
                errors.append(f"invalid shared-kernel provenance: {name}")
            if name in ADAPTED_SKILLS and isinstance(provenance, dict):
                source = provenance.get("upstream")
                if not isinstance(source, dict) or set(source) != {"repository", "revision", "path", "license", "licenseFile"}:
                    errors.append(f"missing public upstream provenance: {name}")
                else:
                    relative = Path(str(source["path"]))
                    if (source["repository"] != "https://github.com/mattpocock/skills"
                            or not re.fullmatch(r"[0-9a-f]{40}", str(source["revision"]))
                            or relative.is_absolute() or ".." in relative.parts
                            or not str(source["path"]).startswith("skills/")
                            or source["license"] != "MIT" or source["licenseFile"] not in notices):
                        errors.append(f"invalid public upstream provenance: {name}")
        if not errors:
            visiting: set[str] = set()
            visited: set[str] = set()
            def visit(name: str) -> None:
                if name in visiting:
                    raise ValueError("cyclic mandatory dependency")
                if name in visited:
                    return
                visiting.add(name)
                for dependency in entries[name]["requires"]:
                    visit(dependency)
                visiting.remove(name)
                visited.add(name)
            for name in entries:
                visit(name)
    except (ValueError, KeyError, TypeError, OSError) as error:
        errors.append(f"invalid catalog: {error}")
    return errors


def main() -> int:
    files = repository_files()
    errors = []
    errors.extend(validate_shape())
    errors.extend(validate_catalog())
    errors.extend(validate_frontmatter())
    errors.extend(validate_agent_metadata())
    errors.extend(validate_links(files))
    errors.extend(validate_sensitive_content(files))
    if errors:
        for error in errors:
            fail(error)
        return 1
    print("Validated fifteen portable skills, resource digests and dependency closure")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
