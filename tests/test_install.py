from __future__ import annotations

import shutil
import json
import hashlib
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import install


class InstallationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.project = Path(self.temporary.name) / 'project'
        self.project.mkdir()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_selected_and_multiple_bundles_include_required_resources(self) -> None:
        self.assertEqual(['handoff', 'codebase-design', 'writing-for-agents', 'to-spec'], install.install(self.project, ['to-spec']))
        self.assertEqual(['handoff', 'triage', 'to-tickets', 'codebase-design', 'diagnose'], install.install(self.project, ['to-tickets', 'diagnose']))
        for name in ['to-spec', 'writing-for-agents', 'handoff', 'triage', 'to-tickets', 'codebase-design', 'diagnose']:
            self.assertEqual(install.file_digests(install.check.ROOT / 'skills' / name), install.file_digests(self.project / '.agents/skills' / name))

    def test_foreign_skill_blocks_whole_bundle_before_mutation(self) -> None:
        foreign = self.project / '.agents/skills/to-spec'
        foreign.mkdir(parents=True)
        (foreign / 'SKILL.md').write_text('owned elsewhere')
        with self.assertRaisesRegex(ValueError, 'foreign skill preserved'):
            install.install(self.project, ['to-spec'])
        self.assertFalse((foreign.parent / 'writing-for-agents').exists())
        self.assertEqual('owned elsewhere', (foreign / 'SKILL.md').read_text())

    def test_modified_owned_skill_is_preserved(self) -> None:
        install.install(self.project, ['meeting-runner'])
        entry = self.project / '.agents/skills/meeting-runner/SKILL.md'
        entry.write_text(entry.read_text() + '\nlocal edit\n')
        with self.assertRaisesRegex(ValueError, 'modified skill preserved'):
            install.install(self.project, ['meeting-runner'])
        self.assertIn('local edit', entry.read_text())

    def test_reinstall_is_idempotent_and_owned_bundle_can_be_removed(self) -> None:
        install.install(self.project, ['to-spec'])
        receipt = self.project / '.agents/organization-os-skills.json'
        before = receipt.read_bytes()
        install.install(self.project, ['to-spec'])
        self.assertEqual(before, receipt.read_bytes())
        install.install(self.project, ['to-spec'], remove=True)
        self.assertFalse((self.project / '.agents/skills/to-spec').exists())
        self.assertFalse((self.project / '.agents/skills/writing-for-agents').exists())

    def test_removal_cannot_break_another_owned_skill(self) -> None:
        install.install(self.project, ['to-spec'])
        with self.assertRaisesRegex(ValueError, 'break installed dependency'):
            install.install(self.project, ['writing-for-agents'], remove=True)
        self.assertTrue((self.project / '.agents/skills/to-spec/SKILL.md').exists())

    def test_linked_destination_is_preserved(self) -> None:
        outside = self.project / 'foreign'
        outside.mkdir()
        (self.project / '.agents').symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'linked project'):
            install.install(self.project, ['meeting-runner'])
        self.assertEqual([], list(outside.iterdir()))

    def test_junction_destination_blocks_bundle_before_mutation(self) -> None:
        linked = self.project.resolve() / '.agents/skills/qualify-opportunity'
        original = install.check.is_linked_path
        with patch.object(install.check, 'is_linked_path', side_effect=lambda path: path == linked or original(path)):
            with self.assertRaisesRegex(ValueError, 'linked skill path'):
                install.install(self.project, ['qualify-opportunity', 'handoff'])
        self.assertFalse((self.project / '.agents').exists())

    def test_failed_receipt_write_restores_previous_copies(self) -> None:
        install.install(self.project, ['meeting-runner'])
        folder = self.project / '.agents/skills/meeting-runner'
        before = install.file_digests(folder)
        receipt = (self.project / '.agents/organization-os-skills.json').read_bytes()
        original = Path.replace
        def fail_receipt(path: Path, target: Path) -> Path:
            if path.name == 'receipt.json':
                raise OSError('simulated receipt failure')
            return original(path, target)
        with patch.object(Path, 'replace', fail_receipt):
            with self.assertRaisesRegex(OSError, 'simulated receipt'):
                install.install(self.project, ['meeting-runner'])
        self.assertEqual(before, install.file_digests(folder))
        self.assertEqual(receipt, (self.project / '.agents/organization-os-skills.json').read_bytes())

    def test_reviewed_update_and_rollback_restore_exact_package_bytes(self) -> None:
        install.install(self.project, ['handoff'])
        target = self.project / '.agents/skills/handoff'
        original = install.file_digests(target)
        candidate = Path(self.temporary.name) / 'candidate'
        for relative in install.check.EXPECTED_FILES:
            destination = candidate / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(install.check.ROOT / relative, destination)
        source = candidate / 'skills/handoff/SKILL.md'
        source.write_text(source.read_text() + '\nPreserve the reviewed revision on continuation.\n')
        catalog_path = candidate / 'catalog.json'
        catalog = json.loads(catalog_path.read_text())
        catalog['skills']['handoff']['files']['SKILL.md'] = hashlib.sha256(source.read_bytes()).hexdigest()
        catalog_path.write_text(json.dumps(catalog))
        with patch.object(install.check, 'ROOT', candidate):
            install.install(self.project, ['handoff'])
        self.assertNotEqual(original, install.file_digests(target))
        install.install(self.project, ['handoff'])
        self.assertEqual(original, install.file_digests(target))

    def test_unknown_skill_and_dependency_cycle_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, 'unknown skill'):
            install.install(self.project, ['unknown'])
        catalog = {'skills': {'a': {'requires': ['b']}, 'b': {'requires': ['a']}}}
        with self.assertRaisesRegex(ValueError, 'cyclic'):
            install.bundle(['a'], catalog)

    def test_package_notice_survives_installation_and_refuses_foreign_edits(self) -> None:
        install.install(self.project, ['handoff'])
        notice = self.project / '.agents/organization-os-skills-NOTICE.txt'
        self.assertIn('Copyright (c) 2026 Matt Pocock', notice.read_text())
        before = notice.read_bytes()
        install.install(self.project, ['handoff'])
        self.assertEqual(before, notice.read_bytes())
        notice.write_bytes(before + b'\nlocal change\n')
        with self.assertRaisesRegex(ValueError, 'modified package notice'):
            install.install(self.project, ['qualify-opportunity'])
        self.assertFalse((self.project / '.agents/skills/qualify-opportunity').exists())

    def test_foreign_package_notice_blocks_installation_before_mutation(self) -> None:
        notice = self.project / '.agents/organization-os-skills-NOTICE.txt'
        notice.parent.mkdir()
        notice.write_text('foreign')
        with self.assertRaisesRegex(ValueError, 'foreign package notice'):
            install.install(self.project, ['meeting-runner'])
        self.assertEqual('foreign', notice.read_text())
        self.assertFalse((notice.parent / 'skills').exists())

    def test_failed_receipt_write_removes_new_notice_and_skills(self) -> None:
        original = Path.replace
        def fail_receipt(path: Path, target: Path) -> Path:
            if path.name == 'receipt.json':
                raise OSError('simulated receipt failure')
            return original(path, target)
        with patch.object(Path, 'replace', fail_receipt):
            with self.assertRaisesRegex(OSError, 'simulated receipt'):
                install.install(self.project, ['qualify-opportunity'])
        self.assertFalse((self.project / '.agents/organization-os-skills-NOTICE.txt').exists())
        self.assertFalse((self.project / '.agents/skills/qualify-opportunity').exists())


if __name__ == '__main__':
    unittest.main()
