from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

import torch


class Metric(ABC):
    """
    Base class for quantitative evaluation of explanations.
    """

    @abstractmethod
    def evaluate(
        self,
        model: torch.nn.Module,
        inputs: torch.Tensor,
        attributions: torch.Tensor,
        **kwargs: Any,
    ) -> dict[str, float]:
        """
        Return a dictionary of scalar metrics (e.g., {"faithfulness": 0.83}).
        """
        raise NotImplementedError

    def get_config(self) -> dict[str, Any]:
        return {"metric": self.__class__.__name__}
