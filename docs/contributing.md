## Contributing Guide

Dev setup
```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: .\.venv\Scripts\Activate.ps1
pip install -U pip
pip install -e .[dev]
```

Checks
- Lint: `ruff check .`
- Format: `black .`
- Types: `mypy src`
- Tests: `pytest`
- Docs: `mkdocs build` or `mkdocs serve`

Workflow
1) Fork and create a feature branch
2) Write clear commits and tests
3) Run all checks locally
4) Open a Pull Request with a concise summary and motivation

Code style
- Python 3.9+ typing
- Prefer explicit names and early returns
- Keep functions small and focused



