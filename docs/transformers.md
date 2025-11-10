## Transformer Interpretability

Planned modules
- Attention analysis: rollout, flow, head importance, entropy, redundancy
- Token-level saliency: gradient-based, LRP variants, attribution aggregation across layers/heads
- Alignment studies: attribution vs. attention concordance
- Visualization: head grids, token HTML renderers, sequence heatmaps

APIs
- `explain(inputs, target=...)` returns per-token attributions
- Head/layer selectors to focus or aggregate specific components


