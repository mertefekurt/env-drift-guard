import unittest

from env_drift_guard.analyzer import analyze
from env_drift_guard.models import EnvEntry


def entry(key: str, value: str, required: bool = False) -> EnvEntry:
    return EnvEntry(key=key, value=value, line=1, raw=f"{key}={value}", required=required)


class AnalyzerTest(unittest.TestCase):
    def test_analyze_detects_drift(self) -> None:
        example = {
            "DATABASE_URL": entry("DATABASE_URL", "", required=True),
            "REDIS_URL": entry("REDIS_URL", "redis://localhost:6379"),
        }
        env = {
            "DATABASE_URL": entry("DATABASE_URL", ""),
            "DEBUG": entry("DEBUG", "true"),
        }

        report = analyze(example, env, ("DEBUG",))

        self.assertEqual(report.missing, ("REDIS_URL",))
        self.assertEqual(report.extra, ("DEBUG",))
        self.assertEqual(report.empty_required, ("DATABASE_URL",))
        self.assertEqual(report.duplicate_keys, ("DEBUG",))
        self.assertTrue(report.has_drift)


if __name__ == "__main__":
    unittest.main()
