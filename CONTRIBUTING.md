Contributing to torchxai

Thank you for your interest in contributing! This guide covers setup, coding standards, and the PR process.

Set up your environment
1) Create a virtual environment and install dev deps:
```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: .\.venv\Scripts\Activate.ps1
pip install -U pip
pip install -e .[dev]
```

Requirements
- Python 3.13+

Run checks locally
- Lint: `ruff check .`
- Format: `black .`
- Types: `mypy src`
- Tests: `pytest`
- Docs: `mkdocs build` (or `mkdocs serve`)

Code style
- Python 3.13+ with type hints
- Prefer explicit, descriptive names
- Keep functions small; use early returns
- Add minimal, high-value comments where necessary

Submitting a Pull Request
1) Fork and create a feature branch
2) Write tests for new functionality
3) Ensure all checks pass locally
4) Open a PR with a clear title and description (problem, solution, trade-offs)
5) Be responsive to review feedback

Community
- Please follow our Code of Conduct (CODE_OF_CONDUCT.md)
- Use discussions or issues for proposals and ideas



