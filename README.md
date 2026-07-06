# Env Drift Guard

> Audit .env files against an example contract

## Snapshot

<img src="assets/readme-cover.svg" alt="Env Drift Guard cover" width="100%" />

| Part | Notes |
| --- | --- |
| Area | delivery and infrastructure |
| Entry | `env-drift-guard` |
| Main files | src/, tests/, .gitignore, pyproject.toml |

## Use

```bash
git clone https://github.com/mertefekurt/env-drift-guard.git
cd env-drift-guard
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
env-drift-guard --help
```

## Notes

This project stays useful when the output is easy to read and the setup is easy to throw away after a quick check.
