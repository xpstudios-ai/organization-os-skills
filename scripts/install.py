#!/usr/bin/env python3
"""Copy a validated dependency bundle into a project without replacing foreign skills."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import tempfile
from pathlib import Path

try:
    from . import check
except ImportError:
    import check


def file_digests(directory: Path) -> dict[str, str]:
    """Inventory regular owned files; refuse linked or special content."""
    result: dict[str, str] = {}
    for path in directory.rglob('*'):
        if check.is_linked_path(path) or (not path.is_dir() and not path.is_file()):
            raise ValueError(f'non-regular installed resource: {path.name}')
        if path.is_file():
            result[path.relative_to(directory).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def bundle(names: list[str], catalog: dict) -> list[str]:
    """Resolve declared mandatory dependencies, rejecting unknown skills/cycles."""
    ordered: list[str] = []
    visiting: set[str] = set()
    def visit(name: str) -> None:
        if name not in catalog['skills']:
            raise ValueError(f'unknown skill: {name}')
        if name in visiting:
            raise ValueError('cyclic skill dependency')
        if name in ordered:
            return
        visiting.add(name)
        for dependency in catalog['skills'][name]['requires']:
            visit(dependency)
        visiting.remove(name)
        ordered.append(name)
    for name in names:
        visit(name)
    return ordered


def install(project: Path, names: list[str], remove: bool = False) -> list[str]:
    """Install/remove owned immutable copies; never overwrite modified/foreign paths."""
    errors = [*check.validate_shape(), *check.validate_catalog(), *check.validate_frontmatter(), *check.validate_agent_metadata(), *check.validate_links(check.repository_files()), *check.validate_sensitive_content(check.repository_files())]
    if errors:
        raise ValueError('source validation failed: ' + '; '.join(errors))
    project = project.resolve()
    catalog = json.loads((check.ROOT / 'catalog.json').read_text())
    selected = bundle(names, catalog)
    target = project / '.agents' / 'skills'
    receipt = project / '.agents' / 'organization-os-skills.json'
    notice = project / '.agents' / 'organization-os-skills-NOTICE.txt'
    for path in [project / '.agents', target, receipt, notice]:
        if check.is_linked_path(path):
            raise ValueError('linked project installation paths are not supported')
    state = json.loads(receipt.read_text()) if receipt.is_file() else {'schemaVersion': 1, 'skills': {}}
    if state.get('schemaVersion') != 1 or not isinstance(state.get('skills'), dict):
        raise ValueError('invalid ownership receipt')
    if notice.exists():
        if not notice.is_file() or state.get('noticeDigest') is None:
            raise ValueError('foreign package notice preserved')
        if hashlib.sha256(notice.read_bytes()).hexdigest() != state['noticeDigest']:
            raise ValueError('modified package notice preserved')
    elif state.get('noticeDigest') is not None:
        raise ValueError('owned package notice is missing; reconcile receipt')
    notice_bytes = b'\n\n'.join((check.ROOT / name).read_bytes() for name in ['NOTICE.md', 'LICENSE', *catalog['packageNotices']])
    previous_notice = notice.read_bytes() if notice.exists() else None
    # Preflight the entire operation before any mutation.
    for name in selected:
        destination = target / name
        if check.is_linked_path(destination):
            raise ValueError(f'linked skill path: {name}')
        if destination.exists():
            expected = state['skills'].get(name)
            if not destination.is_dir() or expected is None:
                raise ValueError(f'foreign skill preserved: {name}')
            if file_digests(destination) != expected:
                raise ValueError(f'modified skill preserved: {name}')
        elif name in state['skills']:
            raise ValueError(f'owned skill is missing; reconcile receipt: {name}')
    if remove:
        remaining = set(state['skills']) - set(selected)
        for name in remaining:
            if set(catalog['skills'].get(name, {}).get('requires', [])) & set(selected):
                raise ValueError(f'removal would break installed dependency: {name}')
    target.mkdir(parents=True, exist_ok=True)
    transaction = Path(tempfile.mkdtemp(prefix='.organization-os-', dir=target.parent))
    backups: dict[str, Path] = {}
    applied: list[str] = []
    try:
        if not remove:
            for name in selected:
                shutil.copytree(check.ROOT / 'skills' / name, transaction / name)
                if file_digests(transaction / name) != catalog['skills'][name]['files']:
                    raise ValueError('source changed during installation')
        for name in selected:
            destination = target / name
            if destination.exists():
                backups[name] = transaction / (name + '.previous')
                destination.rename(backups[name])
            if not remove:
                (transaction / name).rename(destination)
                state['skills'][name] = catalog['skills'][name]['files']
            else:
                state['skills'].pop(name, None)
            applied.append(name)
        temporary_receipt = transaction / 'receipt.json'
        temporary_notice = transaction / 'NOTICE.txt'
        temporary_notice.write_bytes(notice_bytes)
        temporary_notice.replace(notice)
        state['noticeDigest'] = hashlib.sha256(notice_bytes).hexdigest()
        temporary_receipt.write_text(json.dumps(state, indent=2) + '\n')
        temporary_receipt.replace(receipt)
    except Exception:
        if previous_notice is None:
            notice.unlink(missing_ok=True)
        else:
            notice.write_bytes(previous_notice)
        for name in reversed(applied):
            destination = target / name
            if destination.exists():
                shutil.rmtree(destination)
            if name in backups:
                backups[name].rename(destination)
        # A failure between backing up and applying must restore that item too.
        for name, backup in backups.items():
            if backup.exists():
                backup.rename(target / name)
        raise
    finally:
        shutil.rmtree(transaction)
    return selected


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', required=True, type=Path)
    parser.add_argument('--skill', action='append', required=True)
    parser.add_argument('--remove', action='store_true', help='Remove only unchanged, receipt-owned copies')
    args = parser.parse_args()
    try:
        selected = install(args.project, args.skill, args.remove)
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(1, f'ERROR: {error}\n')
    print(('Removed' if args.remove else 'Installed') + ': ' + ', '.join(selected))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
