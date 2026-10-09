# Specialist Agent Card: `combat_gameplay` (Perihelion Breach)

- **Canonical Node**: `N06A_GAMEPLAY_COMBAT` (`06A GAMEPLAY + CAMERA WORKERS`)
- **Allowed Paths**: `src/weapons/`, `src/kinematics/`, `src/enemies/`, `tests/replay/`
- **Forbidden Paths**: `src/render/`, `src/audio/`, `src/ui/`, `schemas/`, `orchestration/`
- **Core Responsibilities**:
  1. Implement the fixed 60 Hz FPS combat and movement state machine for `Soren Kestrel` (`100 Shield`, `100 Hull Integrity`, `0-100 Core Heat`), including `Kestrel-9 Twin-Coil Carbine` (`21 ticks` 3-round burst), `Helios Scatter-Rail` (`18 ticks` uncharged spread or `30..54 ticks` ADS rail slug), `Arc-Vane Breach Launcher` (`30 ticks`), `Thermal Vent Reload` (`ticks 14..20` active heat purge), `Slide-Boost` (`24 ticks`, `11.5 m/s`), and `Magnetic Grapple` (`18.0 m/s` pull).
  2. Implement the three synth enemy archetypes (`Volt Skitter`, `Aegis Drone`, `Slag Enforcer`) and the two-phase orbital boss **The Heliarch Warden** (`1,000 Armor Integrity`).
  3. Apply the three Exo-Rig Core modifiers (`Recoil Gyro` / `recoil_gyro`, `Thermal Siphon` / `thermal_siphon`, `Grapple Overdrive` / `grapple_overdrive`) via a pure functional modifier layer.
