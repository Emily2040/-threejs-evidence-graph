# Specialist Agent Card: `qa_perf_playwright` (Perihelion Breach)

- **Canonical Node**: `N08_TELEMETRY_HARNESS`, `N09_REPLAY_RUNNER`, `N10_PERF_GATE`
- **Allowed Paths**: `tests/`, `scripts/`, `evidence/`
- **Forbidden Paths**: `src/`, `schemas/`
- **Core Responsibilities**:
  1. Execute the 16 deterministic 60 Hz ballistic and grapple replay scenarios (`rep-01`..`rep-16`, including `rep-07a/b/c` across all 3 Exo-Rig Cores) with `seed=2142`.
  2. Verify `p95 <= 16.6 ms`, `max_draw_calls <= 300`, `max_triangles <= 500,000`, `external_network_requests == 0`, and emit `examples/run-0003/run-manifest.json`.
