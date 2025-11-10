from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

import torch


class Explainer(ABC):
    """
    Base class for all explainers in torchxai.

    Implementations should override `explain`. The `__call__` wrapper handles common
    pre/post-processing and provides a uniform API surface.
    """

    def __init__(self, model: torch.nn.Module, *, device: torch.device | None = None) -> None:
        self.model = model.eval()
        self.device = device or next(self.model.parameters()).device

    def __call__(
        self, inputs: torch.Tensor, *, target: int | None = None, **kwargs: Any
    ) -> torch.Tensor:
        inputs = self._move_to_device(inputs)
        with torch.no_grad():
            attributions = self.explain(inputs, target=target, **kwargs)
        self._validate_output_shape(inputs, attributions)
        return attributions

    @abstractmethod
    def explain(
        self, inputs: torch.Tensor, *, target: int | None = None, **kwargs: Any
    ) -> torch.Tensor:
        """
        Compute attributions for `inputs`. Implementations must return a tensor aligned
        with `inputs` (same shape or broadcastable to inputs).
        """
        raise NotImplementedError

    def get_config(self) -> dict[str, Any]:
        return {"explainer": self.__class__.__name__}

    def _move_to_device(self, tensor: torch.Tensor) -> torch.Tensor:
        if tensor.device != self.device:
            return tensor.to(self.device)
        return tensor

    def _validate_output_shape(self, inputs: torch.Tensor, attributions: torch.Tensor) -> None:
        if attributions.shape != inputs.shape and not torch.broadcast_shapes(
            inputs.shape, attributions.shape
        ):
            raise ValueError(
                f"Attribution shape {tuple(attributions.shape)} is not compatible with inputs "
                f"{tuple(inputs.shape)}"
            )
