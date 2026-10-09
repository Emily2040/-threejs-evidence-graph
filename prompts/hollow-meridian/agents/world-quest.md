# Specialist Agent Card: `world_quest`

- **Canonical Node**: `N04_WORLD_GRAPH` (`05 MILESTONE_PLAN` / `FIXED SIM + QA`)
- **Allowed Paths**: `src/world/`, `src/quest/`, `src/save/`, `tests/world/`
- **Forbidden Paths**: `src/combat/`, `src/render/`, `src/audio/`, `schemas/`
- **Core Responsibilities**:
  1. Build the authored five-space route (`Ash Court`, `Orrery Bridge`, `Archive Nave`, `Bell Foundry`, `Meridian Chamber`) and the ten-beat progression state machine (`recover_orientation`: `NOT_STARTED` -> `ACCEPTED` -> `NORTH_SEAL_ACQUIRED` -> `DEPTH_SEAL_ACQUIRED` -> `BOTH_SEALS_ACQUIRED` -> `CHAMBER_OPEN` -> `BOSS_DEFEATED` -> `CHOICE_BIND` / `CHOICE_RELEASE` -> `COMPLETE`).
  2. Implement the deterministic 3-ring `Meridian Alignment` spatial puzzle in `Archive Nave`, `Mnemonic Keeper` dialogue contract, and versioned local save schema (`Ash Salve`, `Chime Resin`, `North Seal`, `Depth Seal`, `Meridian Shard`, and chosen relic `Brass Vow`, `Ash Thread`, or `Vacant Name`).
