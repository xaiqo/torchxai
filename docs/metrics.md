## Metrics

Interface
- Base class: `torchxai.metrics.base.Metric`
- Method: `evaluate(model, inputs, attributions) -> Dict[str, float]`

Planned metrics
- Faithfulness: correlation of relevance with output changes
- Infidelity: sensitivity to perturbations
- Stability: robustness to small input variations
- Comprehensibility: sparsity, concentration
- Local Lipschitzness and Robustness Index (see tasks/)

Example metric
```python
from typing import Dict
import torch
from torchxai.metrics.base import Metric
from torchxai.registry import registry

@registry.register_metric("ZeroMetric")
class ZeroMetric(Metric):
    def evaluate(self, model, inputs: torch.Tensor, attributions: torch.Tensor, **_) -> Dict[str, float]:
        return {"dummy": 0.0}
```

### Detailed Metric Suite (roadmap)
- Faithfulness family
  - Insertion/Deletion curves with AUC; AOPC (Area Over Perturbation Curve)
  - ROAR (RemOve And Retrain) / KAR (Keep And Retrain) for dataset-level validation
  - Output sensitivity wrt masked top-k attributions
- Infidelity and sensitivity
  - Infidelity under random noise and structured perturbations
  - Sensitivity-n (response to perturbing n features)
  - Local Lipschitzness around inputs (bounded neighborhoods)
- Robustness and stability
  - Noise robustness (Gaussian, blur, JPEG), SSIM/PSNR deltas on maps
  - Explanation repeatability across seeds/augmentations
- Localization and pointing
  - Pointing game accuracy; IoU overlap with ground-truth masks
  - Center-of-mass alignment metrics
- Ranking/utility
  - NDCG on feature rankings, Kendall tau/Spearman on attribution order
  - Monotonicity w.r.t. feature removal/retention
- Human-centered interpretability
  - Sparsity/compactness (L0/L1 proxies, Gini)
  - Completeness checks (sum of attributions vs. output deltas)
  - Calibration of attribution scores



