import torch


def ensure_tensor(
    x: torch.Tensor | float | int, device: torch.device | None = None
) -> torch.Tensor:
    if not isinstance(x, torch.Tensor):
        x = torch.as_tensor(x)
    if device is not None and x.device != device:
        x = x.to(device)
    return x


def to_device(tensor: torch.Tensor, device: torch.device) -> torch.Tensor:
    if tensor.device != device:
        return tensor.to(device)
    return tensor
