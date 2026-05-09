from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EnvEntry:
    key: str
    value: str
    line: int
    raw: str
    required: bool


@dataclass(frozen=True)
class DriftReport:
    missing: tuple[str, ...]
    extra: tuple[str, ...]
    empty_required: tuple[str, ...]
    duplicate_keys: tuple[str, ...]

    @property
    def has_drift(self) -> bool:
        return any((self.missing, self.extra, self.empty_required, self.duplicate_keys))

    @property
    def status(self) -> str:
        return "drift found" if self.has_drift else "clean"

