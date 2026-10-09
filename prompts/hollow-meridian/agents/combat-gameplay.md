# Specialist Agent Card: `combat_gameplay`

- **Canonical Node**: `N06A_GAMEPLAY_COMBAT` (`06A GAMEPLAY + CAMERA WORKERS`)
- **Allowed Paths**: `src/combat/`, `src/entities/`, `src/camera/`, `tests/replay/`
- **Forbidden Paths**: `src/render/`, `src/audio/`, `src/ui/`, `schemas/`, `orchestration/`
- **Core Responsibilities**:
  1. Implement the fixed 60 Hz integer-tick combat state machine for `The Cartographer` (`100 Health`, `100 Stamina`, `0-100 Resonance`, `Light 1/2/3`, `Charged Heavy` `27..63 ticks`, `Dodge` `31 ticks` with i-frames `7..18`, `Parry` button-down deflect `6..12` transitioning to `Guard` at tick `13`, and `Echo Brand` `50 Resonance`).
  2. Implement the three canonical enemy archetypes (`Ashbound Skirmisher`, `Bell Sentinel`, `Lantern Wraith`), the deterministic Encounter Director (max 3 active enemies, max 2 melee slots), and the two-phase boss **The Bell Without a Name** (`Meridian Sweep`, `Tolling Stomp`, `Chain Thrust`, `Bell Pulse`; Phase 2 at 55% HP: `Split Meridian`, `Orbiting Core Shot`, `Broken Toll`, `Grasp of Direction`).
  3. Apply the three Shrine relic modifiers (`Brass Vow` / `brass_vow`, `Ash Thread` / `ash_thread`, `Vacant Name` / `vacant_name`) through a pure modifier layer without XP or level grinding.
