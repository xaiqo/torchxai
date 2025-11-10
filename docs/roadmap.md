## Roadmap

Near-term (foundations)
- Solidify base APIs for explainers and metrics
- Implement first-party explainers (IG, DeepLift, GradCAM)
- Add core metrics (faithfulness, infidelity, stability, sparsity)
- Improve visualization for images and tokens
- Basic benchmarking reports

Mid-term (scalability)
- Transformer interpretability module
- Explanation drift tracking and reports
- Plugin and registry ecosystem
- Distributed/batch explainability

Long-term
- CI/CD integration templates
- Community-driven explainer zoo and benchmarks

### Detailed Milestones (proposal)
- M0: API freeze for base `Explainer`/`Metric`; add 3 reference explainers and 3 metrics
- M1: Vision/NLP visualization modules and first benchmarking report format
- M2: Transformer attention analysis, token attributions, and head importance metrics
- M3: Robustness/faithfulness metric suite; insertion/deletion and ROAR pipelines
- M4: Distributed attribution runners with resumable experiments
- M5: Plugin entry points and security/provenance checks; community tutorials



