from __future__ import annotations

from typing import TypeVar

from torchxai.explainers.base import Explainer
from torchxai.metrics.base import Metric

E = TypeVar("E", bound=Explainer)
M = TypeVar("M", bound=Metric)


class _Registry:
    def __init__(self) -> None:
        self._explainers: dict[str, type[Explainer]] = {}
        self._metrics: dict[str, type[Metric]] = {}

    def register_explainer(self, name: str):
        def decorator(cls: type[E]) -> type[E]:
            self._explainers[name] = cls
            return cls

        return decorator

    def register_metric(self, name: str):
        def decorator(cls: type[M]) -> type[M]:
            self._metrics[name] = cls
            return cls

        return decorator

    def get_explainer(self, name: str) -> type[Explainer]:
        return self._explainers[name]

    def get_metric(self, name: str) -> type[Metric]:
        return self._metrics[name]

    def list_explainers(self) -> dict[str, type[Explainer]]:
        return dict(self._explainers)

    def list_metrics(self) -> dict[str, type[Metric]]:
        return dict(self._metrics)


registry = _Registry()
