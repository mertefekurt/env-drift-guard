![Project Banner](https://capsule-render.vercel.app/api?type=waving&color=timeGradient&height=180&section=header&text=env-drift-guard&fontSize=50&fontAlignY=38)

![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)

# env-drift-guard

`env-drift-guard` is a small CLI for catching configuration drift before it reaches production. It compares `.env` against `.env.example`, reports missing keys, unexpected keys, empty required values, and duplicate entries.

![Terminal Output](https://readme-typing-svg.demolab.com/?font=Fira+Code&weight=400&size=14&duration=4000&pause=1000&center=false&vCenter=false&multiline=true&width=600&height=200&lines=env-drift-guard+--example+.env.example+--env+.env;status+++++++++:+drift+found;missing++++++++:+STRIPE_SECRET_KEY;empty+required+:+DATABASE_URL)

## Why it exists

- `.env.example` often changes quietly during development.
- CI usually fails late, after a missing secret breaks runtime code.
- Teams need a simple report that is safe to print in logs.

## Install

```bash
pip install .
```

## Use

```bash
env-drift-guard --example .env.example --env .env
env-drift-guard --format json
```

Exit code is `0` when files match and `1` when drift is found.

## Project layout

- `src/env_drift_guard/` contains the parser, analyzer, renderer, and CLI.
- `tests/` covers parsing edge cases and drift detection.

## License

MIT
