import torch


def normalize_to_01(tensor: torch.Tensor, eps: float = 1e-8) -> torch.Tensor:
    min_v = tensor.amin(dim=tuple(range(1, tensor.ndim)), keepdim=True)
    max_v = tensor.amax(dim=tuple(range(1, tensor.ndim)), keepdim=True)
    return (tensor - min_v) / (max_v - min_v + eps)


def expected_heatmap_shape(inputs: torch.Tensor) -> tuple[int, ...]:
    return inputs.shape
