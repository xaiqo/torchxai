## Benchmarking

Purpose
- Systematically compare explainers and report metrics
- Track compute time and resource usage
- Enable repeatable experiments across datasets/models

Scaffold
- `BenchmarkRunner` accepts a model, explainer class, and metric instances, and returns aggregated scores and runtime.

Planned
- JSON/Markdown/HTML reporting
- Multi-model, multi-dataset runners and result persistence
- Version-controlled comparisons and drift analysis hooks

### Benchmark Design (planned)
- Experiment spec
  - Declarative YAML/JSON for model/explainer/metric/dataset grids
  - Reproducibility: random seeds, deterministic flags, environment capture
- Execution
  - Batched and distributed runs (DDP/FSDP where applicable)
  - Checkpointing and resume-on-failure
  - Mixed-precision controls and memory profiling
- Reporting
  - Structured outputs: JSONL per-run, aggregated JSON, Markdown summaries, HTML dashboards
  - Slices and cohorts (by class, difficulty, domain shift)
  - Cross-version comparisons for regression and drift analysis
- Datasets
  - Pluggable dataset adapters for vision (ImageNet-like), NLP (GLUE-like), tabular (UCI-like)
  - Synthetic datasets for unit/prop-test style evaluation


