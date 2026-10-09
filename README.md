# Three.js Evidence Graph & Multi-Genre Zero-Asset Game Production Suite

<div align="center">

[![Native English](https://img.shields.io/badge/Edition-Native_English-D49B4B?style=for-the-badge)](README.md)
[![简体中文](https://img.shields.io/badge/语言-简体中文_(原生母语版)-45B29D?style=for-the-badge)](README.zh-CN.md)
[![日本語](https://img.shields.io/badge/言語-日本語_(ネイティブ版)-38C6D9?style=for-the-badge)](README.ja.md)
[![한국어](https://img.shields.io/badge/언어-한국어_(네이티브판)-C89B54?style=for-the-badge)](README.ko.md)

[![Release 2026.07.5](https://img.shields.io/badge/Release-2026.07.5-0F1722?style=flat-square&logo=github)](RELEASE_NOTES.md)
[![Three.js r185](https://img.shields.io/badge/Three.js-r185_(0.185.0)-45B29D?style=flat-square)](docs/TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md)
[![Publications 4 PDFs / 217 Pages](https://img.shields.io/badge/Publications-4_PDFs_·_217_Pages-D49B4B?style=flat-square)](docs/PUBLICATION_STATUS.md)
[![JSON Schema Draft 2020-12](https://img.shields.io/badge/Schemas-Draft_2020--12-38C6D9?style=flat-square)](schemas/)
[![License MIT](https://img.shields.io/badge/License-MIT-CBD5E1?style=flat-square)](LICENSE)

</div>

![Three.js Evidence Graph & Multi-Genre Game Production Suite Masthead](assets/svg/masthead-en.svg)

> **What This Repository Is**
>
> This repository publishes a **four-volume, `217`-page engineering specification and multi-agent prompt suite** authored by **Emily Paradox (`@iamemily2050`)** for building deterministic, source-generated Three.js `r185` (`0.185.0`) browser games with **zero downloaded runtime assets**. It pairs one general control-plane methodology (*Three.js Evidence Graph: Operational Manual v2.0*, `64` pages) with three complete genre vertical-slice production specifications:
> 1. **Game 01 - Third-Person Action RPG**: ***The Hollow Meridian*** (`81` pages)
> 2. **Game 02 - Mystery on Horror**: ***The Glass Ossuary*** (`36` pages)
> 3. **Game 03 - First-Person Shooter Adventure**: ***Perihelion Breach*** (`36` pages)
>
> Every publication is backed by standalone JSON Schema Draft 2020-12 contracts (`schemas/`), copy-pasteable orchestrator and specialist agent prompts (`prompts/`), validated golden reference runs (`examples/run-0001/` through `examples/run-0003/`), and native-authored companion guides in **English**, **Simplified Chinese (`简体中文`)**, **Japanese (`日本語`)**, and **Korean (`한국어`)**.

---

## Four-Publication Suite Overview (`217` Pages Total)

![The Four-Publication Suite: Three.js Evidence Graph v2.0, The Hollow Meridian, The Glass Ossuary, and Perihelion Breach](assets/publication-set.jpg)

*Composite plate of the four PDF publications in this repository. All covers and section heroes are publication plates and concept artwork rather than captures from a finished runtime build.*

| # | Publication & Genre | PDF Artifact (`publications/`) | Pages | Size (Bytes) | Native Companion Guides (`docs/`) | Prompts & Fixtures |
| :-: | :--- | :--- | ---: | ---: | :--- | :--- |
| **01** | **Three.js Evidence Graph v2.0**<br/>*Multi-Agent Control Plane & Determinism Manual* | [`threejs-evidence-graph-operational-manual-v2.0-en.pdf`](publications/threejs-evidence-graph-operational-manual-v2.0-en.pdf)<br/>`sha256[0..16]: d3830d411a61c52c` | `64` | `416,827` | [EN](docs/EVIDENCE_GRAPH_GUIDE.md) · [中文](docs/EVIDENCE_GRAPH_GUIDE.zh-CN.md) · [日本語](docs/EVIDENCE_GRAPH_GUIDE.ja.md) · [한국어](docs/EVIDENCE_GRAPH_GUIDE.ko.md) | [`prompts/evidence-graph/`](prompts/evidence-graph/)<br/>[`schemas/`](schemas/) |
| **02** | **The Hollow Meridian v1.0**<br/>*Game 01 · Third-Person Dark-Fantasy Action RPG* | [`the-hollow-meridian-rpg-full-prompt-v1.0-en.pdf`](publications/the-hollow-meridian-rpg-full-prompt-v1.0-en.pdf)<br/>`sha256[0..16]: c4f8fe83995d526b` | `81` | `357,144` | [EN](docs/THE_HOLLOW_MERIDIAN_GUIDE.md) · [中文](docs/THE_HOLLOW_MERIDIAN_GUIDE.zh-CN.md) · [日本語](docs/THE_HOLLOW_MERIDIAN_GUIDE.ja.md) · [한국어](docs/THE_HOLLOW_MERIDIAN_GUIDE.ko.md) | [`prompts/hollow-meridian/`](prompts/hollow-meridian/)<br/>[`examples/run-0001/`](examples/run-0001/) |
| **03** | **The Glass Ossuary v1.0**<br/>*Game 02 · First-Person Investigative Mystery Horror* | [`the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf`](publications/the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf)<br/>`sha256[0..16]: efead090be003782` | `36` | `98,649` | [EN](docs/THE_GLASS_OSSUARY_GUIDE.md) · [中文](docs/THE_GLASS_OSSUARY_GUIDE.zh-CN.md) · [日本語](docs/THE_GLASS_OSSUARY_GUIDE.ja.md) · [한국어](docs/THE_GLASS_OSSUARY_GUIDE.ko.md) | [`prompts/glass-ossuary/`](prompts/glass-ossuary/)<br/>[`examples/run-0002/`](examples/run-0002/) |
| **04** | **Perihelion Breach v1.0**<br/>*Game 03 · First-Person Sci-Fi Shooter Adventure* | [`perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf`](publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf)<br/>`sha256[0..16]: 75bdfff21c905122` | `36` | `95,265` | [EN](docs/PERIHELION_BREACH_GUIDE.md) · [中文](docs/PERIHELION_BREACH_GUIDE.zh-CN.md) · [日本語](docs/PERIHELION_BREACH_GUIDE.ja.md) · [한국어](docs/PERIHELION_BREACH_GUIDE.ko.md) | [`prompts/perihelion-breach/`](prompts/perihelion-breach/)<br/>[`examples/run-0003/`](examples/run-0003/) |

---

## Core Architecture: The 15-Node Evidence Graph (`N00` .. `N14`)

![15-Node Evidence Graph Topology and Three-Genre Game Instantiation](assets/svg/architecture-pipeline.svg)

Single-conversation LLM game generation routinely collapses when the same context window invents scope, writes shaders, edits combat math, and grades its own output. *Three.js Evidence Graph v2.0* replaces self-certified chat loops with four structural invariants:

1. **Deterministic Orchestrator (`orchestrator`)**: Advances a 15-node directed cyclic graph (`N00_BRIEF` through `N14_RELEASE_CANDIDATE`) governed by [`schemas/graph-state.d.ts`](schemas/graph-state.d.ts). No node advances without a schema-valid [`TaskPacket`](schemas/task-packet.schema.json) and passing acceptance commands.
2. **File-Ownership-Isolated Specialist Workers (7 Cards per Game)**: `combat_gameplay`, `world_quest`, `procedural_art_vfx`, `procedural_audio`, `ui_hud_accessibility`, `qa_perf_playwright`, and read-only `independent_critic`. Specialists cannot edit outside their `allowed_paths` or modify verification schemas.
3. **Dual Determinism Regimes (`A-PinnedBrowser` & `B-CrossPlatform`)**:
   - **Regime A (`A-PinnedBrowser`)**: Bit-exact SHA-256 verification inside a pinned Chromium + GPU/SwiftShader harness for 60 Hz integer simulation ticks (`state_hash`), 16-bit PCM quantized `OfflineAudioContext` renders (`audio_hash`), and `1e-5` quantized procedural vertex buffers (`geometry_hash`).
   - **Regime B (`B-CrossPlatform`)**: Bounded invariant and perceptual tolerance gates (`P50 <= 8.3 ms`, `P95 <= 16.6 ms`, `P99 <= 22.0 ms`, `-16 LUFS +- 1.0 LU`, `<= -1.0 dBTP`) across `THREE.WebGPURenderer` and `{ forceWebGL: true }` fallback.
4. **Zero Downloaded Runtime Assets (`provenance_critic`)**: Every mesh, TSL (`Three.js Shading Language`) surface shader, skeletal rig, UI glyph, and Web Audio stem is compiled deterministically from code. `external_network_requests` and `downloaded_assets_count` are locked to `0`.

---

## Side-by-Side Comparison of the Three Flagship Games

| Dimension | Game 01: *The Hollow Meridian* | Game 02: *The Glass Ossuary* | Game 03: *Perihelion Breach* |
| :--- | :--- | :--- | :--- |
| **Genre & Camera** | Third-Person Dark-Fantasy Action RPG | First-Person Investigative Mystery Horror | First-Person Sci-Fi Shooter Adventure |
| **Target Playtime** | 10 to 14 minutes | 12 to 16 minutes | 12 to 15 minutes |
| **Protagonist** | `The Cartographer` (`Sable Veren`) | `Clara Vane` (`The Acoustic Archivist`) | `Soren Kestrel` (`The Relay Vanguard`) |
| **Core Resources** | `100 Health` · `100 Stamina` · `0-100 Resonance` | `100 Composure` · `100 Lantern Oil` · `0-100 Exposure` | `100 Shield` · `100 Hull Integrity` · `0-100 Core Heat` |
| **Signature 60 Hz Mechanic** | Button-down `Parry` deflect (`ticks 6..12`) vs. held `Guard` (`tick >= 13`) | Orthogonal optical `Lantern Shutter` (`6t`) + `Phonograph Cancel` (`ticks 25..114`) + `Ferrotype Flash` (`ticks 19..24`) | `Thermal Vent Reload` (`ticks 14..20` purges `100% Heat`) + `Magnetic Grapple` (`18.0 m/s`) + `Slide-Boost` (`11.5 m/s`) |
| **Five Authored Spaces** | `Ash Court` -> `Orrery Bridge` -> `Archive Nave` -> `Bell Foundry` -> `Meridian Chamber` | `Tidewater Causeway` -> `Caretaker's Stripping Room` -> `Refraction Gallery` -> `Submerged Crypt` -> `The Glass Ossuary` | `Umbilical Airlock` -> `Heliostat Truss` -> `Cryo-Coolant Manifold` -> `Ballistic Foundry` -> `Perihelion Core Chamber` |
| **Spatial Puzzle (Beat 05)** | `Meridian Alignment` (3 concentric brass rings -> `North Seal`) | `Prism Triangulation` (`45/135/270 deg` Fresnel rings -> `Tide Ledger Fragment`) + `110/220/330 Hz` sluices | `Conduit Phase Routing` (3 plasma anchors within `180-tick` decay window -> `Coolant Bypass Core`) |
| **Three Enemy Archetypes** | `Ashbound Skirmisher`, `Lantern Wraith`, `Bell Sentinel` | `Mire Listener` (acoustic), `Glass Septum Watcher` (optical), `Drowned Chorister` (aura) | `Volt Skitter` (wall-runner), `Aegis Drone` (shield sniper), `Slag Enforcer` (mortar heavy) |
| **Build-Defining Choice (Beat 07)** | **Shrine Relic**: `brass_vow` · `ash_thread` · `vacant_name` | **Inquest Hypothesis**: `lens_sabotage` · `tidal_quarantine` · `acoustic_calling` | **Exo-Rig Core**: `recoil_gyro` · `thermal_siphon` · `grapple_overdrive` |
| **Two-Phase Boss (Beat 09)** | **The Bell Without a Name** (`850 HP`, Phase 2 at `55%` / `467 HP`) | **The Choir in the Glass** (`600 Resonance Integrity`, Phase 2 at `300 Integrity`) | **The Heliarch Warden** (`1,000 Armor Integrity`, Phase 2 at `500 Integrity`) |
| **Dual Endings (Beat 10)** | `CHOICE_BIND` or `CHOICE_RELEASE` | `VERDICT_PUBLISH` or `VERDICT_SUBMERGE` | `DIRECTIVE_DIVERT` or `DIRECTIVE_VENT` |
| **Performance Budget** | `<= 300` draw calls · `<= 500,000` tris | `<= 280` draw calls · `<= 460,000` tris | `<= 300` draw calls · `<= 500,000` tris |
| **Golden Fixture** | [`examples/run-0001/`](examples/run-0001/) (`seed=1337`) | [`examples/run-0002/`](examples/run-0002/) (`seed=1894`) | [`examples/run-0003/`](examples/run-0003/) (`seed=2142`) |

---

## Deep Dive into Each Flagship Game

### 1. Game 01 - *The Hollow Meridian* (Third-Person Dark-Fantasy Action RPG · 81 Pages)

| World & Exploration Concept Plate | Two-Phase Boss Concept Plate |
| :---: | :---: |
| ![The Hollow Meridian World Route](assets/hollow-meridian-world-hero.jpg) | ![The Bell Without a Name Boss Encounter](assets/hollow-meridian-boss-hero.jpg) |

*The Hollow Meridian* sets the player inside a ruined brass-and-basalt observatory that once preserved the true names of vanished cities. Playing as **The Cartographer**, you navigate five interconnected spaces, master committed 60 Hz melee parries and stamina discipline, solve the three-ring `Meridian Alignment` puzzle, choose one of three build-defining Shrine relics, and confront **The Bell Without a Name**.

<details>
<summary><strong>Inspect The Hollow Meridian 10-Beat Route, 60 Hz Combat Frame Table & Relic Branches</strong></summary>

#### Authored 10-Beat Route (`recover_orientation`)
1. `01 Ash Court Arrival` (safe hub, `Mnemonic Keeper`, checkpoint) -> 2. `02 Quest Acceptance` (`North Seal` & `Depth Seal`) -> 3. `03 Orrery Bridge Tutorial` (`Ashbound Skirmisher`, `Ash Salve`) -> 4. `04 Archive Nave` (`Lantern Wraith` vertical pressure) -> 5. `05 Meridian Alignment` (3-ring puzzle -> `North Seal`) -> 6. `06 Bell Foundry` (`Bell Sentinel` guard-break -> `Depth Seal` & `Meridian Shard`) -> 7. `07 Shrine Choice` (`brass_vow`, `ash_thread`, or `vacant_name`) -> 8. `08 Chamber Opening` -> 9. `09 The Unnamed Bell` (`850 HP`, Phase 2 at `467 HP`) -> 10. `10 Bind or Release` (`CHOICE_BIND` / `CHOICE_RELEASE`).

#### 60 Hz Integer Combat Timing Table (`docs/TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md`)
| Action | Startup | Active / I-Frames | Recovery | Total | Cost & Effect |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Light Attack 1 / 2 / 3` | `10 / 11 / 15t` | `5 / 7 / 9t` | `12 / 12 / 18t` | `27 / 30 / 42t` | `10 / 11 / 14 Stamina`; `16 / 18 / 25 HP` |
| `Charged Heavy` | `27..38t` | `10..11t` | `12..14t` | `49..63t` | `28 Stamina`; `28..42 HP` + high poise damage |
| `Dodge Roll` | `7t` | `Ticks 7..18` (`12t`) | `12t` | `31t` | `22 Stamina`; full i-frames during `ticks 7..18` |
| `Parry Deflect` | `5t` (`0..4`) | `Ticks 6..12` (`7t`) | `18t` | `31t` | `12 Stamina`; transitions to `Guard` at `tick 13` if held |
| `Echo Brand` | `12t` | `360t mark` | `0t` | `12t cast` | `50 Resonance`; `+25%` damage vulnerability & exposes boss weak point |

- **PDF Specification**: [`publications/the-hollow-meridian-rpg-full-prompt-v1.0-en.pdf`](publications/the-hollow-meridian-rpg-full-prompt-v1.0-en.pdf)
- **Native Guides**: [English](docs/THE_HOLLOW_MERIDIAN_GUIDE.md) · [简体中文](docs/THE_HOLLOW_MERIDIAN_GUIDE.zh-CN.md) · [日本語](docs/THE_HOLLOW_MERIDIAN_GUIDE.ja.md) · [한국어](docs/THE_HOLLOW_MERIDIAN_GUIDE.ko.md)
- **Prompts & Fixtures**: [`prompts/hollow-meridian/`](prompts/hollow-meridian/) · [`examples/run-0001/`](examples/run-0001/)

</details>

---

### 2. Game 02 - *The Glass Ossuary* (First-Person Investigative Mystery Horror · 36 Pages)

| Forensic Investigation Concept Plate | Apparition & Ossuary Boss Concept Plate |
| :---: | :---: |
| ![The Glass Ossuary Forensic Investigation](assets/glass-ossuary-investigation-hero.jpg) | ![The Choir in the Glass Apparition Encounter](assets/glass-ossuary-apparition-hero.jpg) |

*The Glass Ossuary* places acoustic archivist **Clara Vane** on a storm-lashed tidal island in 1894 where a coastal lighthouse has been fused with a subterranean bone-glass ossuary. Instead of combat weapons or scripted jump scares, survival and revelation depend on three physical 19th-century forensic instruments (`Split-Diopter Brass Loupe`, `Wax-Cylinder Phonograph`, and `Silver-Salt Ferrotype Plate`), a 6-node `Inquest Board`, and strict light/sound discipline against **The Choir in the Glass**.

<details>
<summary><strong>Inspect The Glass Ossuary 10-Beat Route, 60 Hz Instrument Frame Table & Inquest Hypotheses</strong></summary>

#### Authored 10-Beat Investigative Route (`case_saint_vane`)
1. `01 Causeway Landfall` (`Tidewater Causeway`, hydrophone footsteps, `Lantern Shutter`) -> 2. `02 The Sealed Inquest` (`Caretaker's Stripping Room`, 6-node `Inquest Board`, `Caretaker Moreau` cylinder) -> 3. `03 Ferrotype Calibration` (`Silver-Salt Ferrotype Plate` UV flash stun) -> 4. `04 Refraction Gallery` (`Glass Septum Watcher` optical evasion & `Brass Loupe`) -> 5. `05 Prism Triangulation` (`45/135/270 deg` Fresnel rings -> `Tide Ledger Fragment`) -> 6. `06 Submerged Crypt` (`Mire Listener` & `Drowned Chorister`, `110/220/330 Hz` sluices -> `Hydrophone Cylinder`) -> 7. `07 Inquest Board Deduction` (`lens_sabotage`, `tidal_quarantine`, or `acoustic_calling`) -> 8. `08 Ossuary Unsealing` -> 9. `09 The Choir in the Glass` (`600 Resonance Integrity`, Phase 2 at `300 Integrity`) -> 10. `10 Publish or Submerge` (`VERDICT_PUBLISH` / `VERDICT_SUBMERGE`).

#### 60 Hz Integer Forensic Instrument Timing Table
| Action | Startup | Active Window | Recovery | Total | Cost & Mechanical Effect |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Lantern Shutter` | `6 ticks` | Toggle (`7..`) | `6 ticks` | `12 ticks` | `0 Oil`; cuts light cone and optical sight-cone aggro |
| `Brass Loupe Focus` | `9 ticks` | Hold (`10..69`) | `6 ticks` | `75 ticks` | `0 Oil`; decodes prism markings and bone-glass glyphs |
| `Phonograph Cancel` | `24 ticks` | `Ticks 25..114` | `36 ticks` | `150 ticks` | Cancels room harmonic; masks footsteps from `Mire Listener` |
| `Ferrotype Flash` | `18 ticks` | `Ticks 19..24` | `66 ticks` | `90 ticks` | Stuns apparitions `150 ticks` within `6.5 m`; exposes seams |
| `Crouch Sidestep` | `5 ticks` | `Ticks 6..16` | `12 ticks` | `28 ticks` | Keeps footstep noise `<= -38 dBFS` across wet stone |
| `Smelling Salts` | `15 ticks` | `Ticks 16..45` | `10 ticks` | `55 ticks` | Restores `+40 Composure` and purges `-25 Exposure` |

- **PDF Specification**: [`publications/the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf`](publications/the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf)
- **Native Guides**: [English](docs/THE_GLASS_OSSUARY_GUIDE.md) · [简体中文](docs/THE_GLASS_OSSUARY_GUIDE.zh-CN.md) · [日本語](docs/THE_GLASS_OSSUARY_GUIDE.ja.md) · [한국어](docs/THE_GLASS_OSSUARY_GUIDE.ko.md)
- **Prompts & Fixtures**: [`prompts/glass-ossuary/`](prompts/glass-ossuary/) · [`examples/run-0002/`](examples/run-0002/)

</details>

---

### 3. Game 03 - *Perihelion Breach* (First-Person Sci-Fi Shooter Adventure · 36 Pages)

| Orbital Solar-Relay Traversal Concept Plate | High-Velocity Boss Combat Concept Plate |
| :---: | :---: |
| ![Perihelion Breach World Route](assets/perihelion-breach-world-hero.jpg) | ![The Heliarch Warden Boss Combat](assets/perihelion-breach-combat-hero.jpg) |

*Perihelion Breach* drops vanguard specialist **Soren Kestrel** aboard the sun-grazing **Icarus-9 Orbital Solar Relay** at `0.09 AU` after its autonomous defense grid locks the heliostat mirrors into a thermal runaway cascade. Built for high-velocity 60 Hz gunplay and three-dimensional traversal, it combines electromagnetic coilguns and piercing rail-slugs with active `Thermal Vent Reload` timings (`ticks 14..20`), `Magnetic Grapple` slingshots (`18.0 m/s`), `240-tick` solar flare shadow corridors, and a two-phase aerial arena battle against **The Heliarch Warden**.

<details>
<summary><strong>Inspect Perihelion Breach 10-Beat Route, 60 Hz Ballistics/Grapple Frame Table & Exo-Rig Cores</strong></summary>

#### Authored 10-Beat Orbital Route (`restore_perihelion_attitude`)
1. `01 Airlock Breach` (`Umbilical Airlock`, `Station AI Vesper`, `Kestrel-9 Twin-Coil Carbine`) -> 2. `02 Lockdown Override` (`Slide-Boost` & `Thermal Vent Reload` calibration) -> 3. `03 Heliostat Skirmish` (`240-tick` solar flare cycle, `Volt Skitter` packs, `Magnetic Grapple` unlock) -> 4. `04 Cryo-Coolant Ascent` (vertical grapple shaft against `Aegis Drone`, `Arc-Vane Breach Launcher`) -> 5. `05 Conduit Phase Routing` (3 plasma anchors within `180 ticks` -> `Coolant Bypass Core`) -> 6. `06 Ballistic Foundry Siege` (`Slag Enforcer` arena -> `Helios Scatter-Rail` & `Ignition Keycard`) -> 7. `07 Suit Rig Calibration` (`recoil_gyro`, `thermal_siphon`, or `grapple_overdrive`) -> 8. `08 Shutter Retraction` -> 9. `09 The Heliarch Warden` (`1,000 Armor Integrity`, Phase 2 at `500 Integrity`) -> 10. `10 Divert or Vent` (`DIRECTIVE_DIVERT` / `DIRECTIVE_VENT`).

#### 60 Hz Integer Weapon, Thermal Vent & Grapple Timing Table
| Action | Startup | Active / Window | Recovery | Total | Heat / Damage / Mechanical Effect |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Carbine 3-Burst` | `2 ticks` | `Ticks 3..11` (3x) | `10 ticks` | `21 ticks` | `+12 Heat`; `3 x 14 dmg` hitscan (`1.5x` weak-point multiplier) |
| `Scatter Uncharged` | `3 ticks` | `Tick 4` (`5x12`) | `15 ticks` | `18 ticks` | `+18 Heat`; `60 dmg` close spread; strips energy shields |
| `Scatter ADS Slug` | `30..54 ticks` | `Tick 31..55` | `18 ticks` | `48..72 ticks` | `+28 Heat`; `55..85 dmg` piercing rail slug (`1.75x` weak point) |
| `Breach Anchor` | `6 ticks` | Projectile | `24 ticks` | `30 ticks` | `+30 Heat`; `60 AoE dmg` armor crack or conduit link |
| `Thermal Vent Reload` | `13 ticks` | `Ticks 14..20` | `16 ticks` | `36 ticks` | Active input in `14..20t` clears `100% Heat` + `90t` overcharge |
| `Slide-Boost` | `3 ticks` | `Ticks 4..18` | `6 ticks` | `24 ticks` | `11.5 m/s` slide; jump-cancel window at `ticks 8..18` |
| `Magnetic Grapple` | `6 ticks` | `18..42 ticks` pull | `12 ticks` | `36..60 ticks` | `18.0 m/s` pull to anchor; preserves tangential slingshot velocity |

- **PDF Specification**: [`publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf`](publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf)
- **Native Guides**: [English](docs/PERIHELION_BREACH_GUIDE.md) · [简体中文](docs/PERIHELION_BREACH_GUIDE.zh-CN.md) · [日本語](docs/PERIHELION_BREACH_GUIDE.ja.md) · [한국어](docs/PERIHELION_BREACH_GUIDE.ko.md)
- **Prompts & Fixtures**: [`prompts/perihelion-breach/`](prompts/perihelion-breach/) · [`examples/run-0003/`](examples/run-0003/)

</details>

---

## Native Four-Language Documentation Matrix

Every README and companion guide in this repository is written natively for professional game developers and graphics engineers in **English**, **Simplified Chinese (`简体中文`)**, **Japanese (`日本語`)**, and **Korean (`한국어`)**, while keeping canonical code identifiers, CLI commands, and schema keys intact for unambiguous cross-referencing:

| Document Surface | Native English (`en`) | Native Simplified Chinese (`zh-CN`) | Native Japanese (`ja`) | Native Korean (`ko`) |
| :--- | :--- | :--- | :--- | :--- |
| **Repository Overview & Suite Guide** | [`README.md`](README.md) | [`README.zh-CN.md`](README.zh-CN.md) | [`README.ja.md`](README.ja.md) | [`README.ko.md`](README.ko.md) |
| **Pub 01: Evidence Graph v2.0 Manual (64 pp)** | [`EVIDENCE_GRAPH_GUIDE.md`](docs/EVIDENCE_GRAPH_GUIDE.md) | [`EVIDENCE_GRAPH_GUIDE.zh-CN.md`](docs/EVIDENCE_GRAPH_GUIDE.zh-CN.md) | [`EVIDENCE_GRAPH_GUIDE.ja.md`](docs/EVIDENCE_GRAPH_GUIDE.ja.md) | [`EVIDENCE_GRAPH_GUIDE.ko.md`](docs/EVIDENCE_GRAPH_GUIDE.ko.md) |
| **Pub 02: The Hollow Meridian - Action RPG (81 pp)** | [`THE_HOLLOW_MERIDIAN_GUIDE.md`](docs/THE_HOLLOW_MERIDIAN_GUIDE.md) | [`THE_HOLLOW_MERIDIAN_GUIDE.zh-CN.md`](docs/THE_HOLLOW_MERIDIAN_GUIDE.zh-CN.md) | [`THE_HOLLOW_MERIDIAN_GUIDE.ja.md`](docs/THE_HOLLOW_MERIDIAN_GUIDE.ja.md) | [`THE_HOLLOW_MERIDIAN_GUIDE.ko.md`](docs/THE_HOLLOW_MERIDIAN_GUIDE.ko.md) |
| **Pub 03: The Glass Ossuary - Mystery Horror (36 pp)** | [`THE_GLASS_OSSUARY_GUIDE.md`](docs/THE_GLASS_OSSUARY_GUIDE.md) | [`THE_GLASS_OSSUARY_GUIDE.zh-CN.md`](docs/THE_GLASS_OSSUARY_GUIDE.zh-CN.md) | [`THE_GLASS_OSSUARY_GUIDE.ja.md`](docs/THE_GLASS_OSSUARY_GUIDE.ja.md) | [`THE_GLASS_OSSUARY_GUIDE.ko.md`](docs/THE_GLASS_OSSUARY_GUIDE.ko.md) |
| **Pub 04: Perihelion Breach - FPS Adventure (36 pp)** | [`PERIHELION_BREACH_GUIDE.md`](docs/PERIHELION_BREACH_GUIDE.md) | [`PERIHELION_BREACH_GUIDE.zh-CN.md`](docs/PERIHELION_BREACH_GUIDE.zh-CN.md) | [`PERIHELION_BREACH_GUIDE.ja.md`](docs/PERIHELION_BREACH_GUIDE.ja.md) | [`PERIHELION_BREACH_GUIDE.ko.md`](docs/PERIHELION_BREACH_GUIDE.ko.md) |
| **Multilingual Terminology & Policy** | [`docs/GLOSSARY.md`](docs/GLOSSARY.md) · [`docs/TRANSLATION_POLICY.md`](docs/TRANSLATION_POLICY.md) | [`docs/GLOSSARY.md`](docs/GLOSSARY.md) | [`docs/GLOSSARY.md`](docs/GLOSSARY.md) | [`docs/GLOSSARY.md`](docs/GLOSSARY.md) |

---

## Repository Architecture & File Map

```text
threejs-evidence-graph/
├── publications/                                                     # 4 Normative English PDFs (217 pages total)
│   ├── threejs-evidence-graph-operational-manual-v2.0-en.pdf         # 64 pages · Control Plane & Determinism Manual
│   ├── the-hollow-meridian-rpg-full-prompt-v1.0-en.pdf               # 81 pages · Game 01: Third-Person Action RPG
│   ├── the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf      # 36 pages · Game 02: First-Person Mystery Horror
│   └── perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf       # 36 pages · Game 03: First-Person Shooter Adventure
├── schemas/                                                          # Normative Draft 2020-12 JSON Schemas & TypeScript State
│   ├── task-packet.schema.json
│   ├── defect-record.schema.json
│   ├── run-manifest.schema.json
│   └── graph-state.d.ts
├── orchestration/                                                    # Drop-in mirror for agent runtime working directories
│   ├── *.schema.json & graph-state.d.ts
│   └── prompts/{orchestrator,hollow-meridian-orchestrator,glass-ossuary-orchestrator,perihelion-breach-orchestrator}.md
├── prompts/                                                          # Copy-pasteable Orchestrator + 21 Specialist Agent Cards
│   ├── evidence-graph/orchestrator.md
│   ├── hollow-meridian/{orchestrator.md, agents/*.md}              # 7 specialist cards for Game 01
│   ├── glass-ossuary/{orchestrator.md, agents/*.md}                # 7 specialist cards for Game 02
│   └── perihelion-breach/{orchestrator.md, agents/*.md}            # 7 specialist cards for Game 03
├── examples/                                                         # Schema-validated Golden Reference Fixtures
│   ├── run-0001/{task-packet,defect-record,run-manifest}.json      # Game 01 fixtures (3 Shrine Relic branches)
│   ├── run-0002/{task-packet,defect-record,run-manifest}.json      # Game 02 fixtures (3 Inquest Hypothesis branches)
│   └── run-0003/{task-packet,defect-record,run-manifest}.json      # Game 03 fixtures (3 Exo-Rig Core branches)
├── docs/                                                             # 16 Native Companion Guides + Errata + Governance
│   ├── EVIDENCE_GRAPH_GUIDE.{md,zh-CN.md,ja.md,ko.md}
│   ├── THE_HOLLOW_MERIDIAN_GUIDE.{md,zh-CN.md,ja.md,ko.md}
│   ├── THE_GLASS_OSSUARY_GUIDE.{md,zh-CN.md,ja.md,ko.md}
│   ├── PERIHELION_BREACH_GUIDE.{md,zh-CN.md,ja.md,ko.md}
│   ├── TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md
│   ├── GLOSSARY.md, TRANSLATION_POLICY.md, PUBLICATION_STATUS.md
│   └── ARTWORK_PROVENANCE.md
├── assets/                                                           # 13 Zero-EXIF JPEGs + 5 Custom Typographic SVGs
│   ├── svg/{masthead-en,masthead-zh-CN,masthead-ja,masthead-ko,architecture-pipeline}.svg
│   └── *.jpg
├── scripts/verify_release.py                                         # Automated SHA-256, Schema, PDF, EXIF & Link Verifier
├── SHA256SUMS.txt                                                    # Bit-exact SHA-256 checksums (LF line endings)
└── release-manifest.json                                             # Machine-readable suite & asset inventory
```

---

## Quick Verification & Usage

Run the automated release and contract verifier from the repository root to validate every SHA-256 digest, JSON Schema Draft 2020-12 contract, golden fixture (`run-0001` through `run-0003`), PDF catalog `/Lang` and `/URI` annotation, zero-EXIF JPEG asset, and localized Markdown link:

```bash
sha256sum -c SHA256SUMS.txt
python scripts/verify_release.py
```

---

## Scope, Epistemic Honesty & Non-Claims

This repository publishes **architecture specifications, production prompts, JSON Schemas, and golden contract fixtures**. It intentionally does **not** claim to ship:

- a compiled or playable Three.js game runtime;
- measured GPU frame-time benchmarks from a live build;
- a live Playwright browser capture package; or
- certified WCAG conformance for an implemented UI.

All frame-time percentiles (`P50 <= 8.3 ms`, `P95 <= 16.6 ms`, `P99 <= 22.0 ms`), draw-call ceilings, and loudness targets (`-16 LUFS +- 1.0 LU`, `<= -1.0 dBTP`) are **normative acceptance gates** that an implementation must pass before `N14_RELEASE_CANDIDATE` sign-off.

---

## Authorship, Citation & License

- **Publication Byline**: Emily Paradox
- **Creator & Copyright Holder**: **Iamemily2050 (`@iamemily2050`)**
- **GitHub**: [Emily2040](https://github.com/Emily2040) · **Website**: [iamemily2050.com](https://iamemily2050.com) · **X**: [`@iamemily2050`](https://x.com/iamemily2050) · **Instagram**: [`@iamemily2050`](https://instagram.com/iamemily2050)
- **Citation Metadata**: [`CITATION.cff`](CITATION.cff) and [`CITATIONS.md`](CITATIONS.md)
- **License**: Released under the [MIT License](LICENSE). See [`AUTHORS.md`](AUTHORS.md) for the complete attribution record.
