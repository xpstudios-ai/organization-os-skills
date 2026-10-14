#!/usr/bin/env python3
"""Build a deterministic, cleared plugin without installing or publishing it."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import tempfile
import zipfile
from pathlib import Path

try:
    from . import check, install
except ImportError:
    import check
    import install


CLEARED = frozenset({'existing-public-package', 'notice-retained', 'approved-public-reuse'})


def json_bytes(value: object) -> bytes:
    """Serialize generated metadata consistently across platforms."""
    return (json.dumps(value, indent=2, ensure_ascii=False) + '\n').encode('utf-8')


def release_inputs() -> tuple[dict, dict, dict, list[str]]:
    """Validate source and select only complete, publication-cleared bundles."""
    files = check.repository_files()
    errors = [*check.validate_shape(), *check.validate_catalog(),
              *check.validate_frontmatter(), *check.validate_agent_metadata(),
              *check.validate_links(files), *check.validate_sensitive_content(files)]
    if errors:
        raise ValueError('source validation failed: ' + '; '.join(errors))
    manifest = json.loads((check.ROOT / 'distribution/plugin.json').read_text())
    release = json.loads((check.ROOT / 'distribution/release.json').read_text())
    catalog = json.loads((check.ROOT / 'catalog.json').read_text())
    if set(manifest) != {'$schema', 'name', 'version', 'description', 'author', 'homepage', 'repository', 'license', 'keywords', 'extensions'}:
        raise ValueError('skills-only manifest fields required')
    extensions = manifest['extensions']
    if set(extensions) != {'com.openai'} or set(extensions['com.openai']) != {'interface'}:
        raise ValueError('skills-only manifest cannot add hooks or service connections')
    if set(extensions['com.openai']['interface']) != {'displayName', 'shortDescription', 'longDescription', 'developerName', 'category', 'defaultPrompt'}:
        raise ValueError('unexpected plugin interface fields')
    interface = extensions['com.openai']['interface']
    for field, limit in {'displayName': 30, 'shortDescription': 30, 'longDescription': 4000, 'developerName': 80}.items():
        value = interface[field]
        if not isinstance(value, str) or not value.strip() or len(value) > limit or any(
            ord(character) < 32 and not (field == 'longDescription' and character == '\n') for character in value
        ):
            raise ValueError(f'directory listing field invalid: {field}')
    prompts = interface['defaultPrompt']
    if not isinstance(prompts, list) or not 1 <= len(prompts) <= 3 or any(
        not isinstance(value, str) or not value.strip() or len(value) > 128 or any(ord(character) < 32 for character in value)
        for value in prompts
    ):
        raise ValueError('directory listing field invalid: defaultPrompt')
    if manifest.get('name') != 'organization-os' or not re.fullmatch(
        r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)', str(manifest.get('version', ''))
    ):
        raise ValueError('stable plugin identity and semantic version required')
    if set(release) != {'schemaVersion', 'skills', 'marketplace', 'stableBranch', 'tagPrefix', 'channels'} or release['schemaVersion'] != 1:
        raise ValueError('invalid release contract')
    if release['marketplace'] != 'xpstudios' or release['stableBranch'] != 'plugin-release' or release['tagPrefix'] != 'organization-os-plugin-v':
        raise ValueError('stable marketplace and release channel required')
    if not isinstance(release['skills'], list) or not release['skills'] or any(not isinstance(name, str) for name in release['skills']):
        raise ValueError('select at least one skill')
    if len(set(release['skills'])) != len(release['skills']):
        raise ValueError('duplicate selected skill')
    selected = install.bundle(release['skills'], catalog)
    for name in selected:
        if catalog['skills'][name]['provenance']['clearance'] not in CLEARED:
            raise ValueError(f'publication clearance pending: {name}')
    if set(release['channels']) != {'openaiDirectory', 'claudeDirectory'}:
        raise ValueError('declare both public channel states')
    for channel in release['channels'].values():
        if channel != {'status': 'pending', 'installUrl': None}:
            raise ValueError('live channel activation requires a separately reviewed release change')
    return manifest, release, catalog, selected


def payload_files(manifest: dict, catalog: dict, selected: list[str]) -> dict[str, bytes]:
    """Derive provider manifests and copy only the selected canonical resources."""
    payload = {'plugin.json': json_bytes(manifest), 'LICENSE': (check.ROOT / 'LICENSE').read_bytes(),
               'NOTICE.md': (check.ROOT / 'NOTICE.md').read_bytes()}
    common = {key: value for key, value in manifest.items() if key not in {'$schema', 'extensions'}}
    payload['.claude-plugin/plugin.json'] = json_bytes(common)
    payload['.codex-plugin/plugin.json'] = json_bytes({
        **common, 'skills': './skills/',
        'interface': manifest['extensions']['com.openai']['interface'],
    })
    notices: set[str] = set()
    for name in selected:
        entry = catalog['skills'][name]
        if entry.get('packageNotice'):
            notices.add(entry['packageNotice'])
        for relative, expected in entry['files'].items():
            source = check.ROOT / 'skills' / name / relative
            if not check.safe_regular_file(source):
                raise ValueError('source changed during build')
            data = source.read_bytes()
            if hashlib.sha256(data).hexdigest() != expected:
                raise ValueError('source changed during build')
            payload[f'skills/{name}/{relative}'] = data
    for relative in sorted(notices):
        payload[relative] = (check.ROOT / relative).read_bytes()
    workflow_names = [re.search(r'  display_name: "([^"]+)"', payload[f'skills/{name}/agents/openai.yaml'].decode()).group(1)
                      for name in selected]
    routing = re.search(r"(?ms)^## Business Setup And Recall\n\n(.*?)(?=^## |\Z)",
                        (check.ROOT / 'CONTRACT.md').read_text())
    if routing is None:
        raise ValueError('business routing product guide is missing')
    context = ''
    if {'codebase-design', 'writing-for-agents'} & set(selected):
        context = ('## Repository context\n\nBefore repository design or agent-instruction authoring, read '
                   'skills/handoff/references/repository-context.md. Preserve AGENTS.md, '
                   '.agents/*-standards.md and legacy CONTEXT.md routes. Explicit repository '
                   'setup merges a startup pointer into existing instructions; installation '
                   'alone does not rewrite them. Reading the reference invokes no setup or '
                   'Handoff workflow and grants no delegation or test deletion authority.\n\n')
    payload['README.md'] = (
        '# Organization OS\n\n'
        + manifest['description'] + '\n\n'
        'Included workflows: ' + ', '.join(workflow_names) + '.\n\n'
        'Start with Meeting Runner for one meeting, or use Workflow Guide when available to choose the next useful step. '
        'Use Codex or Claude Code; business setup manages storage without asking for a folder. '
        f"This {manifest['version']} package includes the selected complete workflow suite. "
        'Codex uses its configured local marketplace source and desktop app; Claude Code uses /plugin. '
        'Public directory and web routes, agent-assisted installation and a complete recipient walkthrough remain under acceptance. '
        'Connect services separately, verify the intended account/workspace and Source of Truth Map, review drafts, '
        'authorize saves and read back results. This skills-only plugin grants no account access.\n\n'
        'Keep the installed plugin managed by the app. Store your workspace choices separately. '
        'Receive approved releases through your installation channel; standalone ZIP imports require replacement.\n\n'
        + context + '## Business setup and recall\n\n' + routing.group(1).strip() + '\n\n'
        'Several workflows are adapted from Matt Pocock’s skills (https://github.com/mattpocock/skills). '
        'His MIT copyright and licence notices are retained; see NOTICE.md and LICENSES/Matt-Pocock-MIT.txt.\n'
    ).encode('utf-8')
    return payload


def verify_version(receipt: dict, previous: Path | None) -> None:
    """Require a forward version for changed releases; never rewrite a version."""
    current = tuple(int(part) for part in receipt['version'].split('.'))
    if previous is None:
        if current != (1, 0, 0):
            raise ValueError('supply the previous approved release receipt')
        return
    if check.is_linked_path(previous) or not previous.is_file():
        raise ValueError('invalid previous release receipt')
    old = json.loads(previous.read_text())
    if not isinstance(old, dict) or old.get('name') != receipt['name'] or not re.fullmatch(
        r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)', str(old.get('version', ''))
    ) or not re.fullmatch(r'[0-9a-f]{64}', str(old.get('zipSha256', ''))):
        raise ValueError('invalid previous release receipt')
    old_version = tuple(int(part) for part in old['version'].split('.'))
    if current < old_version or (current == old_version and receipt['zipSha256'] != old['zipSha256']):
        raise ValueError('changed release requires a higher plugin version')


def build(output: Path, previous: Path | None = None) -> dict:
    """Write a new release tree and ZIP; preserve every existing output path."""
    manifest, release, catalog, selected = release_inputs()
    absolute = output.absolute()
    if any(check.is_linked_path(path) for path in [absolute, *absolute.parents]):
        raise ValueError('linked output path preserved')
    absolute = absolute.resolve()
    if absolute.exists():
        raise ValueError('existing output preserved')
    if absolute.is_relative_to(check.ROOT.resolve()):
        raise ValueError('build output must be outside canonical source')
    payload = payload_files(manifest, catalog, selected)
    plugin_path = 'plugins/' + manifest['name']
    codex_market = {
        'name': release['marketplace'], 'interface': {'displayName': 'xpstudios'},
        'plugins': [{'name': manifest['name'], 'source': {'source': 'local', 'path': './' + plugin_path},
                     'policy': {'installation': 'AVAILABLE', 'authentication': 'ON_INSTALL'}, 'category': 'Productivity'}],
    }
    claude_market = {
        'name': release['marketplace'], 'owner': manifest['author'],
        'description': 'Organization OS workflows for reviewed decisions and owned next actions.',
        'plugins': [{'name': manifest['name'], 'source': './' + plugin_path,
                     'description': manifest['description'], 'category': 'productivity'}],
    }
    digests = {name: hashlib.sha256(data).hexdigest() for name, data in sorted(payload.items())}
    absolute.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix='.orgos-plugin-', dir=absolute.parent))
    try:
        for relative, data in payload.items():
            target = temporary / 'marketplace' / plugin_path / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        for relative, market in [('.agents/plugins/marketplace.json', codex_market), ('.claude-plugin/marketplace.json', claude_market)]:
            target = temporary / 'marketplace' / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(json_bytes(market))
        archive_name = f"{manifest['name']}-{manifest['version']}.zip"
        archive_path = temporary / archive_name
        with zipfile.ZipFile(archive_path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for relative, data in sorted(payload.items()):
                entry = zipfile.ZipInfo(relative, date_time=(1980, 1, 1, 0, 0, 0))
                entry.create_system = 3
                entry.external_attr = 0o100644 << 16
                entry.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(entry, data)
        receipt = {
            'schemaVersion': 1, 'name': manifest['name'], 'version': manifest['version'],
            'selectedSkills': selected, 'files': digests,
            'zipSha256': hashlib.sha256(archive_path.read_bytes()).hexdigest(),
            'stableBranch': release['stableBranch'], 'tag': release['tagPrefix'] + manifest['version'],
            'channels': release['channels'], 'status': 'built-package',
        }
        verify_version(receipt, previous)
        (temporary / 'RELEASE.json').write_bytes(json_bytes(receipt))
        (temporary / 'marketplace/RELEASE.json').write_bytes(json_bytes(receipt))
        temporary.rename(absolute)
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)
    return receipt


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--previous-release', type=Path)
    args = parser.parse_args()
    try:
        result = build(args.output, args.previous_release)
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(1, str(error) + '\n')
    print(f"Built {result['name']} {result['version']}; no installation or publication performed")


if __name__ == '__main__':
    main()
