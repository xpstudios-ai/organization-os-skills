from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import check


class CheckTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.base = Path(self.temporary_directory.name)
        self.root = self.base / "repository"
        for relative_path in check.EXPECTED_FILES:
            source = check.ROOT / relative_path
            destination = self.root / relative_path
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        self.skill_root = self.root / "skills" / "meeting-runner"
        self.skill_file = self.skill_root / "SKILL.md"
        self.patch = patch.multiple(
            check,
            ROOT=self.root,
            SKILL_ROOT=self.skill_root,
            SKILL_FILE=self.skill_file,
        )
        self.patch.start()

    def tearDown(self) -> None:
        self.patch.stop()
        self.temporary_directory.cleanup()

    def test_valid_fixture_passes_every_validator(self) -> None:
        files = check.repository_files()
        errors = [
            *check.validate_shape(),
            *check.validate_frontmatter(),
            *check.validate_agent_metadata(),
            *check.validate_links(files),
            *check.validate_sensitive_content(files),
        ]
        self.assertEqual([], errors)

    def test_rejects_duplicate_frontmatter_field(self) -> None:
        content = self.skill_file.read_text(encoding="utf-8")
        self.skill_file.write_text(
            content.replace("description:", "name: duplicate\ndescription:", 1),
            encoding="utf-8",
        )

        self.assertIn(
            "duplicate SKILL.md frontmatter field: name",
            check.validate_frontmatter(),
        )

    def test_rejects_malformed_agent_metadata(self) -> None:
        metadata = self.skill_root / "agents" / "openai.yaml"
        content = metadata.read_text(encoding="utf-8")
        metadata.write_text(
            content.replace("allow_implicit_invocation: true", "enabled: maybe"),
            encoding="utf-8",
        )

        self.assertTrue(check.validate_agent_metadata())

    def test_rejects_an_extra_skill(self) -> None:
        extra_skill = self.root / "skills" / "extra-skill"
        extra_skill.mkdir()
        (extra_skill / "SKILL.md").write_text("unexpected\n", encoding="utf-8")

        self.assertTrue(check.validate_shape())

    def test_rejects_an_unexpected_skill_file(self) -> None:
        (self.root / "skills" / "README.md").write_text(
            "undeclared\n", encoding="utf-8"
        )

        self.assertTrue(check.validate_shape())

    def test_rejects_an_unexpected_binary_file(self) -> None:
        (self.root / "private-transcript.bin").write_bytes(b"\xff\xfe\x00")

        errors = check.validate_shape()
        self.assertTrue(any("unexpected repository file" in error for error in errors))
        self.assertTrue(any("binary file is not allowed" in error for error in errors))

    def test_rejects_a_symbolic_link(self) -> None:
        link = self.root / "linked-notes.md"
        try:
            link.symlink_to(self.root / "README.md")
        except OSError as error:
            self.skipTest(f"symbolic links unavailable: {error}")

        self.assertTrue(
            any("symbolic links are not allowed" in error for error in check.validate_shape())
        )

    def test_rejects_a_broken_relative_link(self) -> None:
        self.skill_file.write_text(
            self.skill_file.read_text(encoding="utf-8")
            + "\n[Broken](references/missing.md)\n",
            encoding="utf-8",
        )

        self.assertTrue(check.validate_links(check.repository_files()))

    def test_rejects_relative_links_outside_the_repository(self) -> None:
        outside = self.base / "outside.md"
        outside.write_text("private adjacent content\n", encoding="utf-8")
        original = self.skill_file.read_text(encoding="utf-8")
        targets = [
            "../../../outside.md",
            "%2e%2e/%2e%2e/%2e%2e/outside.md",
        ]
        for target in targets:
            with self.subTest(target=target):
                self.skill_file.write_text(
                    original + f"\n[Outside]({target})\n", encoding="utf-8"
                )
                errors = check.validate_links(check.repository_files())
                self.assertTrue(
                    any("relative link escapes repository" in error for error in errors)
                )

    def test_rejects_a_private_path(self) -> None:
        (self.root / "notes.md").write_text(
            "/" + "Users/example/private.txt\n",
            encoding="utf-8",
        )

        self.assertTrue(check.validate_sensitive_content(check.repository_files()))

    def test_rejects_common_secret_families(self) -> None:
        secrets = [
            "github_" + "pat_" + "A" * 30,
            "sk" + "-" + "A" * 32,
            "xo" + "xb-" + "A" * 20,
            "Authorization: Bear" + "er " + "A" * 24,
            "api" + "_key = " + "A" * 24,
        ]
        secret_file = self.root / "secret.txt"
        for secret in secrets:
            with self.subTest(secret_family=secret[:6]):
                secret_file.write_text(secret + "\n", encoding="utf-8")
                self.assertTrue(
                    check.validate_sensitive_content(check.repository_files())
                )

    def test_meeting_runner_preserves_privacy_and_targeted_destinations(
        self,
    ) -> None:
        document = (check.ROOT / "skills" / "meeting-runner" / "SKILL.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("Treat private capture as a silent input", document)
        self.assertIn("never reveal the\n  capture provider", document)
        self.assertIn(
            "A missing workflow file alone must not block a targeted update",
            document,
        )
        self.assertNotIn("notion", document.lower())

    def test_meeting_runner_uses_one_three_column_synthesis_table(self) -> None:
        skill = (check.ROOT / "skills" / "meeting-runner" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        notes = (
            check.ROOT
            / "skills"
            / "meeting-runner"
            / "references"
            / "canonical-meeting-notes.md"
        ).read_text(encoding="utf-8")

        self.assertIn("**Single-table synthesis contract:**", skill)
        self.assertIn("not this table contract", skill)
        self.assertIn("| Topic | Outcome / Decision | Actions |", notes)
        self.assertEqual(1, notes.count("| --- | --- | --- |"))
        self.assertIn("single-table synthesis contract", notes)
        self.assertIn("final `Actions` cell", notes)
        self.assertIn("Never add an actions row, a separate\n  actions table", notes)
        self.assertNotIn("## Actions\n", notes)


if __name__ == "__main__":
    unittest.main()
