## Plugin and Registry System

Goals
- Allow third-party explainers/metrics via entry points
- Versioned discovery with provenance and safety checks

Design
- `torchxai.registry` for in-process registration
- Optional `torchxai-plugins-*` packages expose entry points (e.g., `torchxai.explainers`, `torchxai.metrics`)
- Namespacing and collision handling

Security
- Allowlist/denylist, semantic version ranges, signed releases (future)


