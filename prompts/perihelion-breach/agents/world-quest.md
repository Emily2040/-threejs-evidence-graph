# Specialist Agent Card: `world_quest` (Perihelion Breach)

- **Canonical Node**: `N04_WORLD_GRAPH` (`05 MILESTONE_PLAN` / `FIXED SIM + QA`)
- **Allowed Paths**: `src/world/`, `src/mission/`, `src/save/`, `tests/world/`
- **Forbidden Paths**: `src/weapons/`, `src/render/`, `src/audio/`, `schemas/`
- **Core Responsibilities**:
  1. Build the five orbital sectors (`Umbilical Airlock`, `Heliostat Truss`, `Cryo-Coolant Manifold`, `Ballistic Foundry`, `Perihelion Core Chamber`) and the 10-beat mission progression graph (`restore_perihelion_attitude`).
  2. Implement the deterministic `240-tick` solar flare shutter cycle in `Heliostat Truss` and the `180-tick` 3-node `Conduit Phase Routing` puzzle in `Cryo-Coolant Manifold`.
