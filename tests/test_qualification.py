from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import check, install


class QualificationBundleTests(unittest.TestCase):
    def test_standalone_qualifier_has_complete_reachable_resources(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            self.assertEqual(['qualify-opportunity'], install.install(project, ['qualify-opportunity']))
            folder = project / '.agents/skills/qualify-opportunity'
            catalog = json.loads((check.ROOT / 'catalog.json').read_text())
            self.assertEqual(catalog['skills']['qualify-opportunity']['files'], install.file_digests(folder))
            # Every relative pointer must resolve within the actual selected bundle,
            # rather than accidentally succeeding through the full source checkout.
            with patch.object(check, 'ROOT', project):
                self.assertEqual([], check.validate_links(list((project / '.agents/skills').rglob('*.md'))))

    def test_hard_resource_references_survive_selected_installation(self) -> None:
        for selected in ['codebase-design', 'writing-for-agents', 'handoff', 'to-spec', 'to-tickets', 'diagnose', 'workflow-guide', 'to-questionnaire', 'workflow-retro']:
            with self.subTest(selected=selected), tempfile.TemporaryDirectory() as temporary:
                project = Path(temporary)
                names = install.install(project, [selected])
                files = [file for name in names for file in (project / '.agents/skills' / name).rglob('*.md')]
                with patch.object(check, 'ROOT', project):
                    self.assertEqual([], check.validate_links(files))

    def test_business_resources_do_not_install_repository_setup_or_replace_workspace(self) -> None:
        for selected in ("workflow-guide", "to-questionnaire", "workflow-retro", "qualify-opportunity"):
            with self.subTest(selected=selected), tempfile.TemporaryDirectory() as temporary:
                project = Path(temporary)
                protected = {"AGENTS.md": "existing instructions", "CLAUDE.md": "existing bridge",
                             "notes.txt": "business data", ".agents/skills/gstack/keep": "foreign",
                             ".agents/skills/retro/keep": "foreign retro"}
                for relative, text in protected.items():
                    path = project / relative
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text(text)
                for _ in range(2):
                    installed = install.install(project, [selected])
                    if selected == "qualify-opportunity":
                        self.assertEqual(["qualify-opportunity"], installed)
                        self.assertTrue((project / ".agents/skills/qualify-opportunity/references/business-workspace.md").is_file())
                    else:
                        self.assertIn("handoff", installed)
                        self.assertFalse((project / ".agents/skills/handoff/references/business-workspace.md").exists())
                    self.assertNotIn("setup-agent-workflows", installed)

                    for relative, text in protected.items():
                        self.assertEqual(text, (project / relative).read_text())

    def test_manual_setup_policy_and_automatic_qualifier_policy_are_consistent(self) -> None:
        for name in ['setup-agent-workflows', 'qualify-opportunity']:
            self.assertEqual([], check.validate_skill_frontmatter(name))
            self.assertEqual([], check.validate_skill_metadata(name))

    def test_missing_qualifier_resource_rejects_entire_source(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            root = base / 'source'
            for relative in check.EXPECTED_FILES:
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(check.ROOT / relative, target)
            (root / 'skills/qualify-opportunity/references/qualification-core.md').unlink()
            with patch.object(check, 'ROOT', root):
                with self.assertRaisesRegex(ValueError, 'source validation failed'):
                    install.install(base / 'consumer', ['qualify-opportunity'])
            self.assertFalse((base / 'consumer').exists())

    def test_shared_source_pin_and_package_attribution_are_required(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            catalog = json.loads((check.ROOT / 'catalog.json').read_text())
            catalog['skills']['handoff'].pop('packageNotice')
            catalog['skills']['to-spec']['provenance']['revision'] = 'main'
            (root / 'catalog.json').write_text(json.dumps(catalog))
            with patch.object(check, 'ROOT', root):
                errors = check.validate_catalog()
            self.assertTrue(any('required package attribution missing: handoff' in error for error in errors))
            self.assertTrue(any('invalid shared-kernel provenance: to-spec' in error for error in errors))


if __name__ == '__main__':
    unittest.main()
