# Specialist Agent Card: `combat_gameplay` (The Glass Ossuary)

- **Canonical Node**: `N06A_GAMEPLAY_COMBAT` (`06A GAMEPLAY + CAMERA WORKERS`)
- **Allowed Paths**: `src/forensics/`, `src/apparitions/`, `src/camera/`, `tests/replay/`
- **Forbidden Paths**: `src/render/`, `src/audio/`, `src/ui/`, `schemas/`, `orchestration/`
- **Core Responsibilities**:
  1. Implement the fixed 60 Hz investigative state machine for `Clara Vane` (`100 Composure`, `100 Lantern Oil`, `0-100 Exposure`), including `Lantern Shutter` (`6 ticks` toggle), `Split-Diopter Brass Loupe` (`75 ticks` focus), `Wax-Cylinder Phonograph` (`ticks 25..114` phase cancellation), `Silver-Salt Ferrotype Plate` (`ticks 19..24` active UV flash, `150 ticks` stun within `6.5 m`), and `Crouch Sidestep` (`28 ticks`, `<= -38 dBFS`).
  2. Implement the three apparition archetypes (`Mire Listener`, `Glass Septum Watcher`, `Drowned Chorister`) governed by deterministic acoustic decibel radii and optical sight-cones, plus the two-phase encounter **The Choir in the Glass** (`600 Resonance Integrity`).
  3. Apply the three Inquest Board deduction modifiers (`Lens Sabotage` / `lens_sabotage`, `Tidal Quarantine` / `tidal_quarantine`, `Acoustic Calling` / `acoustic_calling`) as pure state modifiers.
