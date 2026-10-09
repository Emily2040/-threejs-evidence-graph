# Specialist Agent Card: `ui_hud_accessibility`

- **Canonical Node**: `N07_UI_HUD_A11Y` (`07 INTEGRATION`)
- **Allowed Paths**: `src/ui/`, `src/input/`, `tests/ui/`
- **Forbidden Paths**: `src/combat/`, `src/render/`, `src/audio/`, `schemas/`
- **Core Responsibilities**:
  1. Build the diegetic HUD (Health, Stamina, Resonance, active Consumables `Ash Salve` / `Chime Resin`, active Relic `Brass Vow` / `Ash Thread` / `Vacant Name`, and boss health/poise bar for **The Bell Without a Name**).
  2. Provide full keyboard/gamepad remapping, high-contrast UI mode, reduced camera-motion mode, scalable subtitles, and visual equivalents for audio telegraphs.
