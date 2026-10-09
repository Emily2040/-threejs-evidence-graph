# Specialist Agent Card: `world_quest` (The Glass Ossuary)

- **Canonical Node**: `N04_WORLD_GRAPH` (`05 MILESTONE_PLAN` / `FIXED SIM + QA`)
- **Allowed Paths**: `src/world/`, `src/inquest/`, `src/save/`, `tests/world/`
- **Forbidden Paths**: `src/forensics/`, `src/render/`, `src/audio/`, `schemas/`
- **Core Responsibilities**:
  1. Build the five coastal observatory spaces (`Tidewater Causeway`, `Caretaker's Stripping Room`, `Refraction Gallery`, `Submerged Crypt`, `The Glass Ossuary`) and the 10-beat investigation state machine (`case_saint_vane`: `LANDFALL` -> `INQUEST_OPENED` -> `FERROTYPE_CALIBRATED` -> `PRISM_SOLVED` -> `CRYPT_RESONATED` -> `HYPOTHESIS_LOCKED` -> `OSSUARY_UNSEALED` -> `CHOIR_SILENCED` -> `VERDICT_PUBLISH` / `VERDICT_SUBMERGE`).
  2. Implement the 3-ring `Prism Triangulation` optical puzzle (`45/135/270 deg`), the `110/220/330 Hz` sluice gate harmonic puzzle, and the 6-node `Inquest Board` deduction graph.
