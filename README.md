torchxai — Explainability Toolkit for PyTorch

torchxai is an library providing a unified and modular framework for explainable AI (XAI) in 

Features
- Unified explainer interface (gradient- and perturbation-based)
- Metrics to quantify explanation reliability (faithfulness, infidelity, stability, sparsity)
- Visualization for vision, tabular, and NLP (incl. token-level attribution)
- Benchmarking across models/datasets with structured reports
- Plugin/registry system for third-party explainers and metrics
- Batch and distributed explainability workflows

Quickstart
1) Install (development)
```bash
pip install -e .[dev]
```

2) Basic usage (API skeleton)
```python
import torch
from torchxai.explainers.base import Explainer

class MyExplainer(Explainer):
    def explain(self, inputs: torch.Tensor, target: int | None = None) -> torch.Tensor:
        # return relevance map with same shape as inputs
        return torch.zeros_like(inputs)

model = torch.nn.Linear(10, 2).eval()
inputs = torch.randn(1, 10)
explainer = MyExplainer(model=model)
attribution = explainer(inputs, target=1)
```

Documentation
- Getting started: docs/getting_started.md
- Architecture: docs/architecture.md
- Explainers: docs/explainers.md
- Metrics: docs/metrics.md
- Visualization: docs/visualization.md
- Benchmarking: docs/benchmarking.md
- Roadmap: docs/roadmap.md

Contributing
Please read CONTRIBUTING.md for environment setup, coding standards, and contribution workflow. We welcome new explainers, metrics, docs improvements, and examples.
