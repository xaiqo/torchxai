## Evaluation Protocols

Objectives
- Provide standardized, repeatable evaluation for explainers across domains

Protocols
- Faithfulness: insertion/deletion with fixed step sizes and seeds
- ROAR/KAR: data masking and retrain loops with consistent hyperparameters
- Sensitivity/Infidelity: perturbation distributions and sampling budgets
- Localization: mask IoU and pointing game with dataset-specific preprocessing

Reporting
- JSON schema for per-run/per-method metrics
- Aggregation: means, confidence intervals, and cohort stratification


