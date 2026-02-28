# Contributing to AppForge

Thanks for helping AppForge grow.

This guide is optimized for **fast first contribution**, especially for adding new model adapters.

## Ways to Contribute

- Add new LLM/VLM adapters under `examples/LLMs/`
- Improve evaluation reliability and logs
- Improve docs and quickstart usability
- Report reproducible bugs with environment details

## Development Setup

```bash
git clone https://github.com/TongmingLAIC/AppForge
cd AppForge
pip install -e .[example]
```

Optional: syntax check before opening PR

```bash
python -m py_compile setup.py AppForge/appforge.py examples/test.py
```

## Add a New Model Adapter (Template)

### 1) Copy the template

Use `examples/LLMs/Template.py` as your starting point.

### 2) Implement adapter class

Requirements:
- Keep output contract consistent with existing wrappers:
  - return dict with `parsed_output`
  - optionally include `token_usage` and `raw_response`
- Keep constructor simple (`api_key` or `api_key_path`)
- Avoid breaking existing adapters

### 3) Register adapter

Edit `examples/LLMs/__init__.py` and export your adapter class.

### 4) Wire adapter into runner

Edit `examples/test.py`:
- Add your model name to argparse `choices`
- Add branch that initializes your adapter

### 5) Smoke test one task

```bash
python examples/test.py --use_docker --model=<your_model> \
  --runs=smoke_<your_model> --api_key_path=<api_key_file> \
  --start_id 63 --end_id 63 --self_fix_attempts 0
```

## PR Checklist

- [ ] Scope is focused (single feature/fix)
- [ ] No unrelated formatting changes
- [ ] Docs updated (`readme.md` and/or this file)
- [ ] Local syntax check passes
- [ ] Added/updated minimal usage example when applicable

## Community Standards

- Be respectful and constructive: see `CODE_OF_CONDUCT.md`
- Use issue templates in `.github/ISSUE_TEMPLATE/`
- Use PR checklist in `.github/PULL_REQUEST_TEMPLATE.md`

## Issue Template (recommended)

When filing a bug, include:
- OS + Python version
- Docker/local emulator mode
- Full command used
- Task ID(s)
- Key logs from `runs/<run_name>/`

## Code Style

- Keep changes minimal and readable
- Preserve existing public behavior unless intentionally changed
- Prefer explicit errors over silent failures
- Avoid adding new heavyweight dependencies without discussion
