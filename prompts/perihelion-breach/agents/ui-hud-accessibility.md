# Specialist Agent Card: `ui_hud_accessibility` (Perihelion Breach)

- **Canonical Node**: `N07_UI_HUD_A11Y` (`07 INTEGRATION`)
- **Allowed Paths**: `src/ui/`, `src/a11y/`, `tests/ui/`
- **Forbidden Paths**: `src/render/`, `src/weapons/`, `src/audio/`, `schemas/`
- **Core Responsibilities**:
  1. Build the helmet visor HUD (crosshair reticle, `ticks 14..20` active Thermal Vent timing bar, grapple anchor lock indicator, directional threat compass, and Shield/Hull/Heat gauges) meeting WCAG 2.2 AA contrast (`>= 4.5:1`).
  2. Provide FOV comfort presets (`75..110 deg`), persistent center-dot motion-sickness reticle, screen-shake scalar (`0..100%`), and colorblind-safe Cherenkov/Amber threat palettes.
