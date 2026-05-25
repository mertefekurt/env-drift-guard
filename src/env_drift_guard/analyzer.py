"""Core utilities for this package."""
from __future__ import annotations

from env_drift_guard.models import DriftReport, EnvEntry


def analyze(
    example_entries: dict[str, EnvEntry],
    env_entries: dict[str, EnvEntry],
    duplicate_keys: tuple[str, ...] = (),
) -> DriftReport:
    """Compare expected and actual env entries and summarize configuration drift."""
    example_keys = set(example_entries)
    env_keys = set(env_entries)

    missing = tuple(sorted(example_keys - env_keys))
    extra = tuple(sorted(env_keys - example_keys))
    empty_required = tuple(
        sorted(
            key
            for key, entry in example_entries.items()
            if entry.required and key in env_entries and env_entries[key].value == ""
        )
    )

    return DriftReport(
        missing=missing,
        extra=extra,
        empty_required=empty_required,
        duplicate_keys=tuple(sorted(duplicate_keys)),
    )
