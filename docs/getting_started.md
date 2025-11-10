## Getting Started

Requires: Python 3.13+

Installation (development)
```bash
pip install -e .[dev]
```

Minimal usage
```python
import torch
from torchxai.explainers.base import Explainer

class MyExplainer(Explainer):
    def explain(self, inputs: torch.Tensor, target: int | None = None) -> torch.Tensor:
        return torch.zeros_like(inputs)

model = torch.nn.Linear(10, 2).eval()
inputs = torch.randn(1, 10)
explainer = MyExplainer(model)
attr = explainer(inputs, target=1)
```

Development workflow
- Lint: `ruff check .` and format: `black .`
- Type-check: `mypy src`
- Test: `pytest`
- Build docs (MkDocs): `mkdocs build` or `mkdocs serve`



