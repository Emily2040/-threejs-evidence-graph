# Specialist Agent Card: `procedural_art_vfx`

- **Canonical Nodes**: `N03_ASSET_COMPILER`, `N05_RENDER_PIPELINE`
- **Allowed Paths**: `src/render/`, `src/procedural/`, `src/materials/`, `src/vfx/`
- **Forbidden Paths**: `src/combat/`, `src/audio/`, `src/ui/`, `schemas/`
- **Core Responsibilities**:
  1. Generate all world architecture, hierarchical character/enemy/boss rigs, and VFX procedurally in Three.js `r185` (`0.185.0`) with zero downloaded textures, models, or fonts.
  2. Enforce the five-color palette (`#0B1018` abyssal slate, `#1C2636` weathered stone, `#D5A54B` tarnished brass, `#63C7C2` sea-glass cyan Name-light, `#D8564A` crimson hazard; forbid `#7567F5` neon purple).
  3. Configure `THREE.WebGPURenderer` (with `{ forceWebGL: true }` fallback), TSL `NodeMaterial` shaders, `InstancedMesh`/`BatchedMesh` pooling (`<= 300` draw calls, `<= 500,000` triangles), and prewarm via `await renderer.compileAsync(scene, camera)` plus `await postProcessing.renderAsync()`.
