# Specialist Agent Card: `procedural_art_vfx` (Perihelion Breach)

- **Canonical Node**: `N05_RENDER_PIPELINE` (`06B PROCEDURAL + RENDER + AUDIO`)
- **Allowed Paths**: `src/render/`, `src/materials/`, `src/vfx/`, `tests/render/`
- **Forbidden Paths**: `src/weapons/`, `src/audio/`, `src/ui/`, `schemas/`
- **Core Responsibilities**:
  1. Generate all orbital titanium trusses, gold-foil heliostat mirrors, first-person weapon viewmodels, and synth silhouettes from deterministic TypeScript geometry builders (`<= 300` draw calls, `<= 500,000` triangles).
  2. Author TSL (`Three.js Shading Language`) shaders for Cherenkov cyan rail-trails, corona amber heat-shimmer, cryo-frost condensation, and active thermal-vent plasma discharge (`#090D14`, `#1A2433`, `#F08A24`, `#38C6D9`, `#E54848`).
