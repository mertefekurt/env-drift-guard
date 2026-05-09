"""public package interface for env-drift-guard."""

from env_drift_guard.analyzer import analyze
from env_drift_guard.models import DriftReport, EnvEntry
from env_drift_guard.parser import parse_env_file

__all__ = ["DriftReport", "EnvEntry", "analyze", "parse_env_file"]
