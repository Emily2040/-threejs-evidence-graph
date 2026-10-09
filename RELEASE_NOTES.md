# v2026.07.5 - Four-Publication Multi-Genre Suite & Native Four-Language Redesign

All four publications are verified. Every contract is checked. This release expands the repository into a **four-volume, `217`-page engineering specification and multi-agent production suite** under the publication byline **Emily Paradox** (creator and copyright holder **Iamemily2050 / `@iamemily2050`**):

1. **Three.js Evidence Graph: Operational Manual v2.0** (`64` pages) - Multi-agent control plane and dual determinism architecture
2. **Game 01 - The Hollow Meridian: RPG Full Multi-Agent Production Prompt v1.0** (`81` pages) - Third-person dark-fantasy action RPG vertical slice
3. **Game 02 - The Glass Ossuary: Mystery Horror Full Multi-Agent Production Prompt v1.0** (`36` pages) - First-person investigative psychological horror vertical slice (*Mystery on Horror*)
4. **Game 03 - Perihelion Breach: FPS Adventure Full Multi-Agent Production Prompt v1.0** (`36` pages) - First-person kinetic sci-fi shooter adventure vertical slice (*The First-Person Shooter Adventure*)

## Key Highlights of Release `2026.07.5`

- **Two New 36-Page Normative PDF Specifications (`publications/`)**:
  - `the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf` (`36` pages, `98,649` bytes): Specifies acoustic archivist **Clara Vane**'s investigation of Saint-Vane Tidal Island (1894), 60 Hz integer forensic instrument frame tables (`Lantern Shutter`, `Split-Diopter Brass Loupe`, `Wax-Cylinder Phonograph`, `Silver-Salt Ferrotype Plate`), a 6-node `Inquest Board` with three hypotheses (`lens_sabotage`, `tidal_quarantine`, `acoustic_calling`), three apparition archetypes (`Mire Listener`, `Glass Septum Watcher`, `Drowned Chorister`), and a two-phase boss encounter against **The Choir in the Glass**.
  - `perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf` (`36` pages, `95,265` bytes): Specifies vanguard specialist **Soren Kestrel**'s assault aboard the **Icarus-9 Orbital Solar Relay** at `0.09 AU`, 60 Hz ballistic/heat/traversal frame tables (`Kestrel-9 Twin-Coil Carbine`, `Helios Scatter-Rail`, `Arc-Vane Breach Launcher`, `Thermal Vent Reload` at `ticks 14..20`, `Magnetic Grapple` at `18.0 m/s`, `Slide-Boost` at `11.5 m/s`), three Exo-Rig core branches (`recoil_gyro`, `thermal_siphon`, `grapple_overdrive`), and a two-phase aerial arena boss encounter against **The Heliarch Warden**.
- **Native Four-Language Repository Redesign (`en`, `zh-CN`, `ja`, `ko`)**:
  - Re-authored `README.md`, `README.zh-CN.md`, `README.ja.md`, and `README.ko.md` alongside 16 native companion guides (`docs/EVIDENCE_GRAPH_GUIDE.*`, `docs/THE_HOLLOW_MERIDIAN_GUIDE.*`, `docs/THE_GLASS_OSSUARY_GUIDE.*`, `docs/PERIHELION_BREACH_GUIDE.*`) in idiomatic English, Simplified Chinese, Japanese, and Korean.
  - Added 21 custom native-localized SVG mastheads, architectural pipeline diagrams, and 60 Hz frame-window & palette telemetry cards (`assets/svg/*.svg`) alongside 6 new zero-EXIF concept/cover JPEGs (13 JPEGs total in `assets/*.jpg`).
- **Unified Schemas, 25 Agent Prompts & 3 Golden Reference Runs (`examples/run-0001..0003`)**:
  - Extended `schemas/*.schema.json` and `schemas/graph-state.d.ts` (mirrored in `orchestration/`) for all 9 branching modifiers across the three games.
  - Added 16 new copy-pasteable orchestrator and specialist agent prompts in `prompts/glass-ossuary/` and `prompts/perihelion-breach/` and validated golden fixtures in `examples/run-0002/` (`seed=1894`) and `examples/run-0003/` (`seed=2142`).

## Verification & Integrity

Run the automated verifier from the repository root:

```bash
sha256sum -c SHA256SUMS.txt
python scripts/verify_release.py
```

## Scope & License

This release ships specifications, JSON Schemas, prompts, and golden contract fixtures under the [MIT License](LICENSE). It does not claim to ship a playable runtime build or empirical GPU benchmark measurements.
