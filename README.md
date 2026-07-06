<img src="assets/readme-cover.svg" alt="Env Drift Guard cover" width="100%" />

# Env Drift Guard

Audit .env files against an example contract.

![stack](https://img.shields.io/badge/stack-Python-be185d?style=flat-square) ![python](https://img.shields.io/badge/python-3.10-4b5563?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-2563eb?style=flat-square) ![tests](https://img.shields.io/badge/tests-pytest-16a34a?style=flat-square)

| Question | Answer |
| --- | --- |
| What is it? | A focused Python utility for environment drift. |
| How does it run? | `env-drift-guard` |
| Why keep it small? | Easier review, easier tests, fewer moving parts. |

## Command

```bash
python -m pip install -e ".[dev]"
env-drift-guard --help
python -m env_drift_guard --help
```

## Verify

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m env_drift_guard --help
```
