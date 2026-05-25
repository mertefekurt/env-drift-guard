from __future__ import annotations

from pathlib import Path

from env_drift_guard.models import EnvEntry


def parse_env_file(path: Path) -> tuple[dict[str, EnvEntry], tuple[str, ...]]:
    """Parse dotenv-style assignments and return the final entry for each key."""
    entries: dict[str, EnvEntry] = {}
    duplicates: list[str] = []

    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        parsed = _parse_line(raw_line, line_number)
        if parsed is None:
            continue

        if parsed.key in entries and parsed.key not in duplicates:
            duplicates.append(parsed.key)
        entries[parsed.key] = parsed

    return entries, tuple(sorted(duplicates))


def _parse_line(raw_line: str, line_number: int) -> EnvEntry | None:
    stripped = raw_line.strip()
    if not stripped or stripped.startswith("#"):
        return None

    if stripped.startswith("export "):
        stripped = stripped.removeprefix("export ").lstrip()

    if "=" not in stripped:
        return None

    key, value_with_comment = stripped.split("=", 1)
    key = key.strip()
    if not key or not key.replace("_", "").isalnum() or key[0].isdigit():
        return None

    value, comment = _split_comment(value_with_comment.strip())
    value = _unquote(value.strip())
    required = value == "" or "required" in comment.lower()

    return EnvEntry(key=key, value=value, line=line_number, raw=raw_line, required=required)


def _split_comment(value: str) -> tuple[str, str]:
    """Split an inline comment without treating hashes inside quotes as comments."""
    quote: str | None = None
    for index, char in enumerate(value):
        if char in {"'", '"'}:
            quote = None if quote == char else char if quote is None else quote
        if char == "#" and quote is None:
            return value[:index].rstrip(), value[index + 1 :].strip()
    return value, ""


def _unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value
