from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass

import torch

from torchxai.explainers.base import Explainer
from torchxai.metrics.base import Metric


@dataclass
class BenchmarkResult:
    metrics: dict[str, float]
    runtime_seconds: float


class BenchmarkRunner:
    """
    Minimal benchmarking scaffold: run an explainer and evaluate with metrics.
    """

    def __init__(
        self,
        model: torch.nn.Module,
        explainer_cls: type[Explainer],
        metrics: Iterable[Metric],
        *,
        device: torch.device | None = None,
    ) -> None:
        self.model = model.eval()
        self.explainer_cls = explainer_cls
        self.metrics = list(metrics)
        self.device = device or next(self.model.parameters()).device

    def run(self, inputs: torch.Tensor, target: int | None = None) -> BenchmarkResult:
        import time

        inputs = inputs.to(self.device)
        explainer = self.explainer_cls(self.model, device=self.device)
        t0 = time.perf_counter()
        attributions = explainer(inputs, target=target)
        dt = time.perf_counter() - t0

        aggregated: dict[str, float] = {}
        for metric in self.metrics:
            scores = metric.evaluate(self.model, inputs, attributions, target=target)
            aggregated.update(scores)
        return BenchmarkResult(metrics=aggregated, runtime_seconds=dt)
