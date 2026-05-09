from __future__ import annotations

import json

from env_drift_guard.models import DriftReport


def render_table(report: DriftReport) -> str:
    rows = [
        ("status", report.status),
        ("missing", _join(report.missing)),
        ("extra", _join(report.extra)),
        ("empty required", _join(report.empty_required)),
        ("duplicates", _join(report.duplicate_keys)),
    ]
    width = max(len(label) for label, _ in rows)
    return "\n".join(f"{label.ljust(width)} : {value}" for label, value in rows)


def render_json(report: DriftReport) -> str:
    payload = {
        "status": report.status,
        "missing": report.missing,
        "extra": report.extra,
        "empty_required": report.empty_required,
        "duplicate_keys": report.duplicate_keys,
    }
    return json.dumps(payload, indent=2)


def _join(values: tuple[str, ...]) -> str:
    return ", ".join(values) if values else "-"

