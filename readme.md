# AppForge

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Benchmark](https://img.shields.io/badge/Focus-Android%20App%20Generation-orange)](tasks/tasks.json)

AppForge is a practical benchmark for evaluating the from-scratch software development capability of LLMs, with a focus on Android apps.

**From leaderboard engineering to real product engineering: AppForge evaluates whether agents can build software from 0 to 1, not just patch existing repos.**

## Why this benchmark matters

Most coding benchmarks reward **"fixing existing code"**.
Real product work is different: start from a blank slate, understand requirements, build architecture, implement features, pass tests, and survive runtime failures.

AppForge targets this exact gap.

## Why AppForge is different

- **Task definition is different**: no pre-existing project codebase; models start from requirements and implement complete apps.
- **Failure modes are different**: AppForge captures compilation, test, and runtime/fuzz failures instead of only patch correctness.
- **Signal quality is different**: low end-to-end success rates (best reported 18.8%) expose true capability ceilings for agentic coding.

This is why AppForge matters: it measures real-world software delivery ability, not only repository editing skill.

- **ICLR 2026 accepted**: AppForge introduces the first end-to-end benchmark for real App development from 0 to 1.
- **Reality check**: the best reported success rate is **18.8%** for full app delivery, showing how far current agentic coding still is from production-level autonomy.
- **New phase of agentic coding**: when evaluation moves from "bug-fix" to "build-from-scratch", model capability ceilings become explicit.

In short: AppForge is designed to measure what actually matters in software creation, not leaderboard-friendly shortcuts.

It provides:

- 101 real app tasks with structured feature specs.
- A template-based compile pipeline for reproducible builds.
- Test + fuzz based evaluation for quality and robustness.
- Docker-first workflow for quick, stable setup.

---

## Why AppForge

- **Reproducible**: fixed template + deterministic evaluation flow.
- **Actionable**: compile logs + test/fuzz results for clear failure diagnosis.
- **Model-agnostic**: easy to plug in different LLM backends.
- **Practical**: built around runnable Android projects, not toy outputs.

## The Core Question

If there is no existing codebase and only product requirements,
**can an AI agent build a working App like a human engineer?**

AppForge is built to answer this question with measurable outcomes.

---

## 5-Minute Quick Start (Docker, recommended)

### 0)  Prerequisite

Our docker image contains Android docker image from [budtmo/docker-android: Android in docker solution with noVNC supported and video recording](https://github.com/budtmo/docker-android). In short, our docker image can only be run under **Ubuntu OS** supporting **CPU Virtualization**. If you are using other systems, you can check `documentation/detailed_docker_installation.md` or use alternative Local Emulator Setup.

### 1) Install package

```bash
git clone https://github.com/TongmingLAIC/AppForge
cd AppForge
pip install -e '.[example]'
```

### 2) Pull runtime image

```bash
docker pull zenithfocuslight/appforge:latest
```

### 3) Checking environment installation immediately (no API key required)

```bash
python examples/quickstart.py --use_docker
```

This command runs with the `naive` baseline on one task and quickly checks the environment installation.

---

## Run with your own model

```bash
python examples/test.py --use_docker --docker_port=6080 \
    --model=<model_name> --runs=example_<model_name> \
    --api_key_path=<api_key_path> --start_id 63 --end_id 63 \
    --self_fix_attempts 0
```

Common `<model_name>` options in `examples/test.py`:

- `qwen3coder`
- `deepseekv3`
- `deepseekr1`
- `claude_code (access through CLI)` 
- `naive (which returns empty output for checking environment installation)`
- and more to be added!

`--start_id` and `--end_id`specify the range of tasks to test. To run tests on all tasks, set `--start_id 0 --end_id 100`.

`--self_fix_atttempts` determines how many times the model will attempt to fix code based on compilation error feedback.

You can always check https://appforge-bench.github.io/code-docs/modules.html and `documentation/detailed_docker_installation.md` for more information.

---

## Local Emulator Setup (alternative)

If you prefer local Android emulator/device testing, see:

- `documentation/detailed_local_installation.md`

---

## Results and Artifacts

By default outputs are saved under `runs/<run_name>/`, including:

- raw model output
- compile logs
- test/fuzz logs
- JSON summaries
- optional videos (`--record_video`)

---

## Project Layout

```text
AppForge/                 # core evaluator package
compiler/templates/       # Android template project
examples/                 # runnable examples and model adapters
tasks/tasks.json          # benchmark task definitions
documentation/            # setup guides
```

---

## Known Issues

- Docker path permission error (`Errno 13`):

```bash
sudo chmod -R 777 runs
```

---

## Citation / Docs

- Paper / announcement: (to be updated with official ICLR 2026 link)
- Code docs: https://appforge-bench.github.io/code-docs/modules.html
- Tasks: `tasks/tasks.json`
- Contributing: `CONTRIBUTING.md`
- Code of Conduct: `CODE_OF_CONDUCT.md`
- Issue templates: `.github/ISSUE_TEMPLATE/`
- PR template: `.github/PULL_REQUEST_TEMPLATE.md`