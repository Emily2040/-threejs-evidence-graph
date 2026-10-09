# Specialist Agent Card: `qa_perf_playwright` (The Glass Ossuary)

- **Canonical Node**: `N08_TELEMETRY_HARNESS`, `N09_REPLAY_RUNNER`, `N10_PERF_GATE`
- **Allowed Paths**: `tests/`, `scripts/`, `evidence/`
- **Forbidden Paths**: `src/`, `schemas/`
- **Core Responsibilities**:
  1. Execute the 16 deterministic replay scenarios (`rep-01`..`rep-16`, including `rep-07a/b/c` across all 3 Inquest hypotheses) at 60 Hz (`seed=1894`).
  2. Verify `p95 <= 16.6 ms`, `max_draw_calls <= 280`, `max_triangles <= 460,000`, `external_network_requests == 0`, and emit `examples/run-0002/run-manifest.json`.
