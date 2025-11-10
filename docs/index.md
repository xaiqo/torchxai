## torchxai Documentation

torchxai is a modular, extensible XAI toolkit for PyTorch. It provides:
- A unified interface for multiple attribution methods
- Quantitative metrics for reliability
- Visualization utilities
- Benchmarking workflows
- Registry/plugins for community extensions

Start here:
- Getting Started: getting_started.md
- Architecture: architecture.md
- Explainers: explainers.md
- Metrics: metrics.md
- Visualization: visualization.md
- Benchmarking: benchmarking.md
- Roadmap: roadmap.md

Background/context:
- Project brief: project.md

### Key Feature Areas (planned and in-progress)
- Explainers
  - Gradient-based: Integrated Gradients (variants), DeepLift, Input×Gradient, Grad-CAM/++, Guided Backprop, DeconvNet, Layer-wise Relevance Propagation (LRP)
  - Perturbation-based: Occlusion, RISE, LIME, KernelSHAP, Feature Ablation
  - Concept-based and causal: TCAV/TCAV+, ACE (automated concept extraction), Counterfactuals (DiCE-style), Causal feature attribution
  - Transformer-specific: Attention rollout/flow, head attribution, token-level saliency aggregation, LRP for Transformers
  - Prototype and feature visualization: Activation maximization, feature inversion, prototypical explanations
- Metrics
  - Faithfulness (insertion/deletion curves, AOPC), ROAR (RemOve And Retrain), Sensitivity-n/Infidelity, Completeness checks
  - Robustness and stability: local Lipschitzness, noise robustness, SSIM/PSNR deltas on explanations
  - Localization/pointing: pointing game, IoU/Mask-overlap for vision
  - Ranking/utility: NDCG, Kendall tau for attribution orderings
  - Human-centered: sparsity/compactness, monotonicity, calibration/consistency
- Visualization
  - Image overlays, multi-panel saliency comparisons, attention head grids, token-level HTML renderers
  - Tabular importance dashboards and SHAP-like summary plots
- Benchmarking
  - Multi-dataset, multi-model sweeps with JSON/Markdown/HTML reports
  - Reproducibility controls, seeds, and environment captures
  - Distributed/batch attribution for scale
- Ops/Plugins
  - Entry-point based discovery, versioned registry, safety checks for dynamic loading
  - CI/CD templates, docs deploy, and release automation


