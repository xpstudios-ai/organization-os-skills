from __future__ import annotations

import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

from scripts import build_plugin, check


class PluginTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.previous = check.ROOT / "tests/fixtures/plugin-1.0.0.json"

    def build(self, output: Path, previous: Path | None = None) -> dict:
        return build_plugin.build(output, previous or self.previous)

    def test_complete_suite_and_provider_identity_are_deterministic(self) -> None:
        first = self.build(self.root / 'first')
        second = self.build(self.root / 'second')
        self.assertEqual(first, second)
        name = f"organization-os-{first['version']}.zip"
        self.assertEqual((self.root / 'first' / name).read_bytes(), (self.root / 'second' / name).read_bytes())
        with zipfile.ZipFile(self.root / 'first' / name) as archive:
            files = set(archive.namelist())
            catalog = json.loads((check.ROOT / 'catalog.json').read_text())
            expected = {f'skills/{skill}/{path}' for skill, entry in catalog['skills'].items() for path in entry['files']}
            self.assertEqual(15, len(first['selectedSkills']))
            self.assertEqual(sum(len(e["files"]) for e in catalog["skills"].values()), len(expected))
            self.assertIn('NOTICE.md', files)
            self.assertEqual((check.ROOT / 'LICENSES/Matt-Pocock-MIT.txt').read_bytes(), archive.read('LICENSES/Matt-Pocock-MIT.txt'))
            self.assertEqual(expected, {path for path in files if path.startswith('skills/')})
            for path in expected:
                self.assertEqual((check.ROOT / path).read_bytes(), archive.read(path))
            identities = [json.loads(archive.read(path)) for path in ['plugin.json', '.claude-plugin/plugin.json', '.codex-plugin/plugin.json']]
            self.assertEqual({'organization-os'}, {value['name'] for value in identities})
            self.assertEqual({first['version']}, {value['version'] for value in identities})
            self.assertFalse(any('mcp' in path or 'hooks/' in path for path in files))

    def test_repository_context_is_included_only_with_reference_bundle(self) -> None:
        manifest, _, catalog, selected = build_plugin.release_inputs()
        full = build_plugin.payload_files(manifest, catalog, selected)
        reference = 'skills/handoff/references/repository-context.md'
        self.assertIn(reference, full)
        self.assertIn(reference, full['README.md'].decode())
        self.assertIn('legacy CONTEXT.md', full['README.md'].decode())
        meeting = build_plugin.payload_files(manifest, catalog, ['meeting-runner'])
        self.assertNotIn(reference, meeting)
        self.assertNotIn(reference, meeting['README.md'].decode())
        self.assertIn('## Business setup and recall', meeting['README.md'].decode())

    def test_missing_product_setup_guide_rejects_build_before_output_creation(self) -> None:
        original = Path.read_text
        def missing(path: Path, *args: object, **kwargs: object) -> str:
            if path == check.ROOT / "CONTRACT.md":
                return "# Workflow contract\n\nSetup route is unavailable.\n"
            return original(path, *args, **kwargs)
        output = self.root / "missing-guide"
        with patch.object(Path, "read_text", missing):
            with self.assertRaisesRegex(ValueError, "business routing product guide is missing"):
                self.build(output)
        self.assertFalse(output.exists())

    def test_existing_or_linked_output_is_preserved(self) -> None:
        target = self.root / 'owned'
        target.mkdir()
        (target / 'keep').write_text('foreign')
        with self.assertRaisesRegex(ValueError, 'existing output'):
            build_plugin.build(target)
        linked = self.root / 'linked'
        linked.symlink_to(target, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'linked output'):
            build_plugin.build(linked)
        self.assertEqual('foreign', (target / 'keep').read_text())

    def test_build_cannot_write_into_canonical_source(self) -> None:
        with self.assertRaisesRegex(ValueError, 'outside canonical'):
            self.build(check.ROOT / 'dist-test')

    def test_pending_clearance_blocks_dependency_bundle(self) -> None:
        original = Path.read_text
        def selected(path: Path, *args: object, **kwargs: object) -> str:
            text = original(path, *args, **kwargs)
            if path == check.ROOT / 'distribution/release.json':
                value = json.loads(text)
                value['skills'] = ['to-spec']
                return json.dumps(value)
            if path == check.ROOT / 'catalog.json':
                value = json.loads(text)
                value['skills']['handoff']['provenance']['clearance'] = 'pending'
                return json.dumps(value)
            return text
        with patch.object(Path, 'read_text', selected):
            with self.assertRaisesRegex(ValueError, 'clearance pending: handoff'):
                self.build(self.root / 'blocked')
        self.assertFalse((self.root / 'blocked').exists())

    def test_manifest_version_and_channel_activation_fail_closed(self) -> None:
        original = Path.read_text
        for mode in ['version', 'channel', 'hooks']:
            def changed(path: Path, *args: object, **kwargs: object) -> str:
                text = original(path, *args, **kwargs)
                if mode == 'version' and path == check.ROOT / 'distribution/plugin.json':
                    value = json.loads(text)
                    value['version'] = 'latest'
                    return json.dumps(value)
                if mode == 'hooks' and path == check.ROOT / 'distribution/plugin.json':
                    value = json.loads(text)
                    value['extensions']['com.openai']['hooks'] = './hooks/hooks.json'
                    return json.dumps(value)
                if mode == 'channel' and path == check.ROOT / 'distribution/release.json':
                    value = json.loads(text)
                    value['channels']['openaiDirectory'] = {'status': 'live', 'installUrl': 'https://example.com'}
                    return json.dumps(value)
                return text
            with self.subTest(mode=mode), patch.object(Path, 'read_text', changed):
                with self.assertRaises(ValueError):
                    self.build(self.root / mode)

    def test_failure_during_archive_write_leaves_no_partial_output(self) -> None:
        with patch.object(zipfile.ZipFile, 'writestr', side_effect=OSError('simulated archive failure')):
            with self.assertRaisesRegex(OSError, 'simulated archive failure'):
                self.build(self.root / 'failed')
        self.assertEqual([], list(self.root.iterdir()))

    def test_directory_submission_limits_are_checked_before_building(self) -> None:
        original = Path.read_text
        for field, value in [('shortDescription', 'x' * 31), ('displayName', 'x' * 31),
                             ('developerName', 'x' * 81), ('longDescription', 'x' * 4001),
                             ('shortDescription', 'two\nlines'), ('defaultPrompt', ['x' * 129])]:
            def changed(path: Path, *args: object, **kwargs: object) -> str:
                text = original(path, *args, **kwargs)
                if path == check.ROOT / 'distribution/plugin.json':
                    manifest = json.loads(text)
                    manifest['extensions']['com.openai']['interface'][field] = value
                    return json.dumps(manifest)
                return text
            with self.subTest(field=field, value=value), patch.object(Path, 'read_text', changed):
                with self.assertRaisesRegex(ValueError, 'directory listing field invalid: ' + field):
                    self.build(self.root / 'invalid')
                self.assertFalse((self.root / 'invalid').exists())

    def test_marketplaces_point_only_to_the_complete_suite(self) -> None:
        self.build(self.root / 'release')
        root = self.root / 'release/marketplace'
        for path in ['.agents/plugins/marketplace.json', '.claude-plugin/marketplace.json']:
            catalog = json.loads((root / path).read_text())
            self.assertEqual('xpstudios', catalog['name'])
            self.assertEqual(1, len(catalog['plugins']))
            entry = catalog['plugins'][0]
            self.assertNotIn('version', entry)
            source = entry['source']
            relative = source['path'] if isinstance(source, dict) else source
            self.assertTrue((root / relative / 'skills/meeting-runner/SKILL.md').is_file())

    def test_changed_release_requires_forward_version_and_previous_receipt(self) -> None:
        self.build(self.root / 'first')
        previous = self.root / 'first/RELEASE.json'
        original = Path.read_text
        for version in ['1.1.0', '1.1.1']:
            def changed(path: Path, *args: object, **kwargs: object) -> str:
                text = original(path, *args, **kwargs)
                if path == check.ROOT / 'distribution/plugin.json':
                    value = json.loads(text)
                    value['description'] += ' Updated.'
                    value['version'] = version
                    return json.dumps(value)
                return text
            with self.subTest(version=version), patch.object(Path, 'read_text', changed):
                if version == '1.1.0':
                    with self.assertRaisesRegex(ValueError, 'higher plugin version'):
                        self.build(self.root / 'same', previous)
                    self.assertFalse((self.root / 'same').exists())
                else:
                    with self.assertRaisesRegex(ValueError, 'previous approved'):
                        build_plugin.build(self.root / 'missing')
                    result = self.build(self.root / 'updated', previous)
                    self.assertEqual('1.1.1', result['version'])


if __name__ == '__main__':
    unittest.main()
