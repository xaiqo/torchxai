## Visualization

Goals
- Provide normalized saliency/heatmaps for vision models
- Token-level attribution renderers for NLP
- Feature importance summaries for tabular data

Utilities (early scaffold)
- `normalize_to_01`: scales tensor per-sample to [0, 1]

Planned
- Matplotlib helpers for images
- Overlay heatmaps on input images
- HTML rendering for token attributions

### Advanced Visualization Modules
- Vision
  - Multi-method overlays (e.g., IG vs. Grad-CAM comparisons)
  - Insertion/deletion animation playback for faithfulness
  - Region-of-interest zooms; bounding box overlays; segmentation mask alignment
- NLP
  - Token-level color maps with hover tooltips and attribution values
  - Layer/head attention grids with selection filters
  - Phrase-level aggregation and span visualizations
- Tabular
  - Global feature importance bars and SHAP-like beeswarm plots
  - Partial dependence plots with attribution overlays
- Reporting
  - HTML export of experiment runs (interactive), static PNG/SVG snapshots
  - Side-by-side model/version comparisons for drift analysis


