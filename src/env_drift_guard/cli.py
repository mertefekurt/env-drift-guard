from __future__ import annotations

import argparse
from pathlib import Path

from env_drift_guard.analyzer import analyze
from env_drift_guard.parser import parse_env_file
from env_drift_guard.render import render_json, render_table


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="env-drift-guard",
        description="Audit a .env file against a .env.example contract.",
    )
    parser.add_argument("--example", type=Path, default=Path(".env.example"))
    parser.add_argument("--env", type=Path, default=Path(".env"))
    parser.add_argument("--format", choices=("table", "json"), default="table")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    for path in (args.example, args.env):
        if not path.exists():
            raise SystemExit(f"file not found: {path}")

    example_entries, example_duplicates = parse_env_file(args.example)
    env_entries, env_duplicates = parse_env_file(args.env)
    report = analyze(example_entries, env_entries, example_duplicates + env_duplicates)

    renderer = render_json if args.format == "json" else render_table
    print(renderer(report))
    return 1 if report.has_drift else 0


if __name__ == "__main__":
    raise SystemExit(main())

