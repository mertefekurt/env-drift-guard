import tempfile
import unittest
from pathlib import Path

from env_drift_guard.parser import parse_env_file


class ParserTest(unittest.TestCase):
    def test_parse_env_file_supports_export_quotes_and_comments(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            env_file = Path(directory) / ".env.example"
            env_file.write_text(
                "\n".join(
                    [
                        "# ignored",
                        "export DATABASE_URL= # required",
                        "API_NAME='billing service' # optional",
                        'TOKEN="abc#123"',
                    ]
                ),
                encoding="utf-8",
            )

            entries, duplicates = parse_env_file(env_file)

        self.assertEqual(duplicates, ())
        self.assertTrue(entries["DATABASE_URL"].required)
        self.assertEqual(entries["API_NAME"].value, "billing service")
        self.assertEqual(entries["TOKEN"].value, "abc#123")

    def test_parse_env_file_reports_duplicates(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            env_file = Path(directory) / ".env"
            env_file.write_text("API_KEY=one\nAPI_KEY=two\n", encoding="utf-8")

            entries, duplicates = parse_env_file(env_file)

        self.assertEqual(entries["API_KEY"].value, "two")
        self.assertEqual(duplicates, ("API_KEY",))


if __name__ == "__main__":
    unittest.main()
