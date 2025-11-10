## Explainers

Interface
- Base class: `torchxai.explainers.base.Explainer`
- Call pattern: `explainer(inputs, target=...)` → `torch.Tensor` attributions

Roadmap of built-ins
- Gradient-based: Integrated Gradients, DeepLift, GradCAM
- Perturbation-based: Occlusion, KernelSHAP
- Transformers: token-level and attention head aggregation

Adding a new explainer
```python
import torch
from torchxai.explainers.base import Explainer
from torchxai.registry import registry

@registry.register_explainer("MyExplainer")
class MyExplainer(Explainer):
    def explain(self, inputs: torch.Tensor, target: int | None = None) -> torch.Tensor:
        return torch.zeros_like(inputs)
```

### Planned Explainer Modules (detailed)
- Gradient-based
  - Integrated Gradients (IG), path-integrated variants, baselines (zeros, blur, blurred baseline ensembles), IG-SQ
  - DeepLift / DeepLiftShap
  - Input×Gradient, Gradient×Activation
  - SmoothGrad / VarGrad
  - Grad-CAM, Grad-CAM++, Score-CAM, XGrad-CAM
  - Guided Backpropagation, Guided Grad-CAM, DeconvNet
  - Layer-wise Relevance Propagation (LRP) rules (epsilon, gamma, z+), CNN and Transformer adaptations
- Perturbation and sampling
  - Occlusion (sliding window / multi-scale), Feature Ablation
  - RISE (randomized input sampling for explanation)
  - LIME (local surrogate), KernelSHAP (model-agnostic SHAP), DeepSHAP
  - Counterfactual perturbations (image inpainting masks; tabular constraints)
- Concept and causal
  - TCAV/TCAV+ (concept activation vectors), ACE (automatic concept extraction)
  - Causal attributions via interventional ablations or SCM-backed probes
- Prototype and feature visualization
  - Activation maximization (regularized)
  - Feature inversion and deep dream-like visualizations
  - Prototype learning explanations (prototypical networks; case-based reasoning)
- Transformer-focused
  - Attention rollout, attention flow, head importance measures
  - Token-level saliency with layer/head aggregation strategies
  - LRP for Transformers; attribution alignment with attention maps

### API Notes
- All explainers follow `Explainer.__call__(inputs, target=...) -> attributions`
- Output shapes must align (or be broadcastable) to `inputs`
- Explainers may declare `supports="vision"|"nlp"|"tabular"|...` for routing in benchmarks



