## Architecture Overview

Package layout (src/torchxai)
- explainers: Base `Explainer` and concrete methods
- metrics: Quantitative evaluation of attributions
- visualization: Utilities for rendering/normalization
- benchmarking: Orchestrates explainer runs and metric collection
- registry: Lightweight plugin/registration decorator system
- utils: Types and small helpers

Key principles
- Torch-native: Autograd, modules, tensors, hooks
- Consistent APIs: `Explainer.__call__(inputs, target=...)` returning attributions
- Extensibility: Easy to add custom explainers and metrics via the registry
- Reproducibility: Deterministic evaluation options and versioned reports (planned)

Extending
1) Implement a new explainer by subclassing `Explainer` and overriding `explain`.
2) Implement a new metric by subclassing `Metric` and implementing `evaluate`.
3) Register with `registry.register_explainer("Name")` or `registry.register_metric("Name")`.

### System Modules (planned)
- Data adapters: unified interfaces for image, text, and tabular datasets
- Model adapters: convenience wrappers to extract features/activations from CNNs/Transformers/MLPs
- Attribution routers: map model/domain → compatible explainer sets
- Reporters: JSON/Markdown/HTML emitters with schema
- Plugin discovery: entry-point loaders with version constraints and provenance metadata
- Distributed orchestrator: launch and aggregate explainability jobs across devices/nodes


