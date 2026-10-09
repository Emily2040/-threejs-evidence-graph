# Specialist Agent Card: `qa_perf_playwright`

- **Canonical Nodes**: `N08_TELEMETRY_HARNESS`, `N09_REPLAY_RUNNER`, `N10_PERF_GATE`
- **Allowed Paths**: `src/telemetry/`, `tests/playwright/`, `scripts/`
- **Forbidden Paths**: `src/combat/`, `src/render/`, `src/audio/`, `schemas/`
- **Core Responsibilities**:
  1. Expose deterministic browser inspection hooks `window.__rpgReady === true` and `window.__rpgQA` (`getState()`, `getMetrics()`, `stepTicks(n)`, `loadScenario(id, seed)`).
  2. Run the 16 deterministic replay scenarios (`rep-01` through `rep-16`, including `rep-11a-shrine-brass-vow`, `rep-11b-shrine-ash-thread`, and `rep-11c-shrine-vacant-name`) and verify `P50 <= 8.3 ms`, `P95 <= 16.6 ms`, `P99 <= 22.0 ms`.
