import torch

# Placeholder example demonstrating expected API usage.
# Replace MyExplainer with a concrete implementation when available.
from torchxai.explainers.base import Explainer


class MyExplainer(Explainer):
    def explain(self, inputs: torch.Tensor, target: int | None = None) -> torch.Tensor:
        return torch.zeros_like(inputs)


def main() -> None:
    model = torch.nn.Sequential(torch.nn.Flatten(), torch.nn.Linear(28 * 28, 10)).eval()
    inputs = torch.randn(1, 1, 28, 28)
    explainer = MyExplainer(model)
    attr = explainer(inputs, target=0)
    print("Attribution shape:", tuple(attr.shape))


if __name__ == "__main__":
    main()
