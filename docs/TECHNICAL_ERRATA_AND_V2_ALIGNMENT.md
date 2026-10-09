# Technical Errata & Evidence Graph v2.0 Alignment Specification

This normative errata document reconciles the contracts, schemas, node identifiers, Three.js `r185` (`0.185.0`) APIs, determinism quantization rules, and combat/RPG mathematical tables across *Three.js Evidence Graph: Operational Manual v2.0* (64 pages) and *The Hollow Meridian: Full Multi-Agent Production Prompt v1.0* (81 pages).

---

## 1. Canonical 15-Node Topology Crosswalk (`N00` to `N14`)

To eliminate naming drift between the 16-box diagram on page 11 of *Evidence Graph v2.0* (which splits node `06` into parallel branches `06A` and `06B`), the `N00` to `N14` prose/schema identifiers on pages 12-17, and the 15-stage execution topology on page 14 of *The Hollow Meridian v1.0*, all schemas and task packets use the canonical `N00` to `N14` identifiers below:

| Canonical Schema ID | *Evidence Graph v2.0* Diagram Label (p. 11) | *The Hollow Meridian v1.0* Topology Stage (p. 14) | Primary Owner Agent |
| :--- | :--- | :--- | :--- |
| `N00_BRIEF` | `01 BRIEF_COMPILE` | `BRIEF + CONSTITUTION` | `orchestrator` |
| `N01_CONTRACTS` | `02 CONSTITUTION_AUDIT` | `PRODUCT + ART FREEZE` | `orchestrator` |
| `N02_SCAFFOLD` | `03 ARCHITECTURE_DECISION` | `RENDERER PROOF` | `orchestrator` |
| `N03_ASSET_COMPILER` | `04 ART+GAMEPLAY_BIBLE_FREEZE` | `PLAN + FOUNDATION` | `procedural_art_vfx` |
| `N04_WORLD_GRAPH` | `05 MILESTONE_PLAN` | `FIXED SIM + QA` | `world_quest` |
| `N05_RENDER_PIPELINE` | `06B PROCEDURAL + RENDER + AUDIO` (Render/Art) | `PARALLEL WORKERS` (World/Render) | `procedural_art_vfx` |
| `N06A_GAMEPLAY_COMBAT` | `06A GAMEPLAY + CAMERA WORKERS` | `PARALLEL WORKERS` (Combat/Enemies/Boss) | `combat_gameplay` |
| `N06B_AUDIO_SYNTH` | `06B PROCEDURAL + RENDER + AUDIO` (Audio/FX) | `PARALLEL WORKERS` (Audio/FX) | `procedural_audio` |
| `N07_UI_HUD_A11Y` | `07 INTEGRATION` | `INTEGRATION` | `ui_hud_accessibility` |
| `N08_TELEMETRY_HARNESS` | `08 STATIC_VERIFICATION` | `STATIC + REPLAY` | `qa_perf_playwright` |
| `N09_REPLAY_RUNNER` | `09 DETERMINISTIC_REPLAY` | `CAPTURE` | `qa_perf_playwright` |
| `N10_PERF_GATE` | `10 EVIDENCE_CAPTURE` | `READ-ONLY CRITICS` | `qa_perf_playwright` |
| `N11_VISUAL_AUDIO_CRITIC` | `11 INDEPENDENT_CRITICISM` | `EVIDENCE REDUCER` | `independent_critic` |
| `N12_PROVENANCE_AUDIT` | `12 EVIDENCE_REDUCTION` | `ACCEPT / REPAIR / ROLLBACK` | `independent_critic` |
| `N13_REPAIR_ROUTER` | `13 DECIDE` / `14 CROSS-BROWSER_RELEASE_AUDIT` | `BROWSER + PROVENANCE AUDIT` / `TWO CLEAN CYCLES` | `orchestrator` |
| `N14_RELEASE_CANDIDATE` | `15 RELEASE_CANDIDATE` | `RELEASE CANDIDATE` | `orchestrator` |

---

## 2. Schema Unification & Path/ID Regex Fixes

1. **JSON Schema Draft 2020-12 Upgrade**: All standalone schemas in [`schemas/`](../schemas/) (mirrored in [`orchestration/`](../orchestration/)) use `"$schema": "https://json-schema.org/draft/2020-12/schema"`.
2. **Evidence Path Pattern (`defect-record.schema.json`)**: Appendix B (p. 62) of *Evidence Graph v2.0* used `^run-[0-9]+/` while the repository tree (p. 17) placed evidence runs under `/evidence/run-0001/`. The normative schema accepts `"^(evidence/|examples/)?run-[0-9]{4,}/.+$"`.
3. **Defect ID Pattern (`defect-record.schema.json`)**: Appendix B (p. 62) restricted `issue_id` to `^[A-Z]{3}-[0-9]{3,}$`, which rejected *The Hollow Meridian*'s node-scoped IDs (`RPG-N06A-COMBAT-014`). The normative schema accepts `"^([A-Z]{3,6}-[0-9]{3,}|[A-Z]{3,6}-N[0-9]{2}[A-B]?-[A-Z0-9]{3,}-[0-9]{3,})$"`.
4. **Cross-Edition Contract Alignment**: `schemas/run-manifest.schema.json` enforces v2.0 mandatory fields (`determinism_regime`, `cost_ledger`, `human_signoff`, `provenance`, and `critic_verdicts`) for all runs, including *The Hollow Meridian*.
5. **Deterministic Browser QA Hooks**: *The Hollow Meridian* (p. 61) exposes `window.__rpgReady === true` and `window.__rpgQA` (`window.__rpgQA.getState()`, `window.__rpgQA.getMetrics()`, `window.__rpgQA.stepTicks(n)`, `window.__rpgQA.loadScenario(id, seed)`). Generic Evidence Graph harnesses may alias `window.__GAME_STATE__` to `window.__rpgQA.getState()`.

---

## 3. Integer 60 Hz Combat Frame Table & Input Disambiguation (*The Hollow Meridian* pp. 44-45)

*The Hollow Meridian* specifies a fixed `60 Hz` (`16.6667 ms` per tick) simulation clock, but pages 44-45 state combat windows in floating-point seconds that do not all divide evenly by `1/60 s`. In deterministic `Regime A`, all gameplay logic must use integer ticks (`1 tick = 1/60 s`):

| Player Action | Total Duration | Startup Ticks | Active / Hit Window Ticks | Recovery / Chain Ticks | Stamina Cost | Damage / Poise Damage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Light 1** (`light_1`) | `27 ticks` (`0.450 s`) | `0..9` (`10t`) | `10..14` (`5t`, `0.167-0.233 s`) | Recovery `15..26`; chain window `17..24` (`0.283-0.400 s`) | `10` | `16 HP` / `10 Poise` |
| **Light 2** (`light_2`) | `30 ticks` (`0.500 s`) | `0..10` (`11t`) | `11..17` (`7t`, `0.183-0.283 s`) | Recovery `18..29`; chain window `19..26` (`0.317-0.433 s`) | `11` | `18 HP` / `12 Poise` |
| **Light 3** (`light_3`) | `42 ticks` (`0.700 s`) | `0..14` (`15t`) | `15..23` (`9t`, `0.250-0.383 s`) | Recovery `24..41` (`18t`, directional follow-through) | `14` | `25 HP` / `24 Poise` |
| **Charged Heavy (Min Release)** (`charged_heavy_min`) | `49 ticks` (`0.817 s`, released at `27t` / `0.450 s`) | Charge `0..26` (`27t`) | `27..36` (`10t`) | Recovery `37..48` (`12t`) | `28` | `28 HP` / `30 Poise` |
| **Charged Heavy (Full Charge)** (`charged_heavy_full`) | `63 ticks` (`1.050 s`) | Charge `0..37` (`38t`) | `38..48` (`11t`, `0.633-0.800 s`) | Recovery `49..62` (`14t`, breaks Bell Sentinel guard) | `28` | `42 HP` / `45 Poise` |
| **Dodge** (`dodge`) | `31 ticks` (`0.517 s`, PDF `0.52 s`) | `0..6` (`7t`) | Invulnerable `7..18` (`12t`, `0.117-0.300 s`) | Recovery `19..30` (`12t`, no attack cancel before `19t`) | `22` | `0 HP` / `0 Poise` |
| **Parry** (`parry`) | `31 ticks` (`0.517 s`, PDF `0.52 s`) | `0..5` (`5t`, `0.083 s`, PDF `0.08 s`) | Deflect `6..12` (`7t`, `0.100-0.217 s`, PDF `0.10-0.22 s`) | Recovery `13..30` (`18t`); grants `+25 Resonance` on deflect | `12` | `0 HP` / `30 Poise` (interrupts eligible attacks) |
| **Guard** (`guard_hold`) | Continuous (`>= 13 ticks`) | Transitions from `parry` at tick `13` if input held | Continuous while held and Stamina > 0 | Guard break enters `45-tick` (`0.750 s`) stagger | `0.5 * incoming Poise` | Frontal mitigation `70%` |
| **Echo Brand** (`echo_brand`) | `360 ticks` (`6.000 s` mark duration) | `0..11` (`12t` cast) | Active mark `12..371` (`360t`) | Bonus `+20 Poise` stagger on parries against marked target | `50 Resonance` | Marks weak point (non-stacking) |

### Charge Interpolation & Parry/Guard Disambiguation Rules
- **Charged Heavy Interpolation (`t_release` in `[27, 63]`)**: Releasing the heavy input at integer tick `t_release` (`27 <= t_release <= 63`) interpolates damage and poise damage linearly: `alpha = (t_release - 27) / 36`, `damage = Math.round(28 + 14 * alpha)`, `poise_damage = Math.round(30 + 15 * alpha)`.
- **Parry vs. Guard Input Disambiguation**: Because `Parry` and `Guard` share the defensive input (`Right Mouse Button` / `Left Bumper` / `Key F`), pressing the defensive input immediately enters `Parry` at tick `0` (`5` startup ticks `0..4`, `7` active deflect ticks `6..12`). If an incoming eligible attack intersects ticks `6..12`, a `Parry` deflect triggers. If no deflect triggers and the defensive input remains held at tick `13`, the state machine transitions seamlessly into continuous `Guard` without incurring a second startup penalty.

---

## 4. Complete RPG Numeric Balance, Enemy & Boss Contracts (*The Hollow Meridian* pp. 44-50)

### 4.1 Player Resources, Consumables & Non-Level Progression Contract
Per page 50 (`PROGRESSION CONTRACT`), progression in *The Hollow Meridian* is a single meaningful relic choice at the Shrine, **never** an XP or level-grinding system:
- **Base Player Resources (Fixed)**: `100 Health`, `100 Stamina` (regenerates at `28 Stamina / s` = `0.4667 Stamina / tick` after a `36-tick` / `0.60 s` non-spending delay), `0 to 100 Resonance` (`+10 Resonance` per melee hit, `+25 Resonance` per successful Parry deflect; `Echo Brand` spends `50 Resonance`).
- **Consumables (Page 49)**:
  - **Ash Salve**: Restores `40 Health` over `18 ticks` (`0.30 s`), maximum carried `3` (replenished at resting checkpoints).
  - **Chime Resin**: Increases Stamina regeneration by `+50%` (`42 Stamina / s`) for `720 ticks` (`12.0 s`), maximum carried `2`.

### 4.2 Three Shrine Relics (`Brass Vow`, `Ash Thread`, `Vacant Name` - Page 49)
At Beat 07 (`Shrine Choice`), the player spends the authored `Meridian Shard` to lock in one of three mutually exclusive relics:
1. **`Brass Vow` (`brass_vow`)**: Widens the `Parry` active deflect window by `+2 ticks` (ticks `5..13`) and increases Parry poise damage from `30` to `45`, but increases continuous `Guard` stamina drain by `+15%`.
2. **`Ash Thread` (`ash_thread`)**: Extends `Dodge` invulnerability by `+2 ticks` (ticks `6..19`) and reduces `Dodge` stamina cost from `22` to `18`, but reduces continuous `Guard` frontal damage mitigation from `70%` to `55%`.
3. **`Vacant Name` (`vacant_name`)**: Extends `Echo Brand` mark duration from `360 ticks` (`6.0 s`) to `540 ticks` (`9.0 s`) and causes `Charged Heavy` hits against a marked target to trigger a `24 HP` / `18 Poise` Resonance detonation, while increasing `Echo Brand` cost from `50` to `60 Resonance`.

### 4.3 Canonical Enemy Archetypes & Two-Phase Boss (Pages 45-48)

| Entity | Canonical ID | Health | Poise Threshold | Stagger Window | Signature Attacks & Damage (`HP` / `Poise`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Ashbound Skirmisher** | `ashbound_skirmisher` | `95` | `30` | `75 ticks` (`1.25 s`) | `Quick Slash` (`14 HP` / `12 Poise`, parryable), `Delayed Lunge` (`22 HP` / `20 Poise`, parryable, no rotation after commitment) |
| **Bell Sentinel** | `bell_sentinel` | `180` | `65` (Shield Guard `45`) | `105 ticks` (`1.75 s`) | `Shield Pressure` (`16 HP` / `25 Poise`), `Horizontal Sweep` (`24 HP` / `28 Poise`, parryable), `Delayed Overhead` (`34 HP` / `40 Poise`, high telegraph) |
| **Lantern Wraith** | `lantern_wraith` | `110` | `25` | `90 ticks` (`1.50 s`) | `Fire Bolt` (`18 HP` / `14 Poise` ranged projectile), `Radial Flare` (`20 HP` / `22 Poise` close burst), visible departure/arrival cues |
| **The Bell Without a Name (Phase 1: 100%-55% HP)** | `the_bell_without_a_name` | `850` (Phase 2 at `467 HP`) | `120` | `150 ticks` (`2.50 s`) | `Meridian Sweep` (`26 HP` / `28 Poise`, parryable frames), `Tolling Stomp` (`28 HP` / `32 Poise` + expanding floor ring), `Chain Thrust` (`24 HP` / `24 Poise`, parryable), `Bell Pulse` (`32 HP` / `35 Poise` medium burst) |
| **The Bell Without a Name (Phase 2: 55%-0% HP)** | `the_bell_without_a_name` | `467 -> 0` | `140` | `180 ticks` (`3.00 s`) | `Split Meridian` (`30 HP` / `30 Poise`, two sequential floor arcs), `Orbiting Core Shot` (3 paced projectiles, `16 HP` each), `Broken Toll` (`36 HP` / `42 Poise` delayed overhead + marked falling fragments), `Grasp of Direction` (`22 HP` pull field with visible boundary) |

- **Boss Weak-Point Exposure Rule (Page 48)**: On page 48, *The Hollow Meridian* states that the boss exposes a Resonance weak point after `Bell Pulse` or poise break, and in Phase 2 detaches the bell core during `Split Meridian` and `Broken Toll`. Normative trigger: after the recovery window of `Bell Pulse` (Phase 1) or `Broken Toll` (Phase 2), or immediately upon any poise break (`Poise <= 0`), the suspended bell core drops to player melee height and exposes its Resonance weak point (`1.5x` incoming HP damage) for `150 ticks` (`2.50 s`, extended to `180 ticks` / `3.00 s` on poise break).
- **Replay Scenario `rep-11` Three-Branch Shrine Protocol**: Because Beat 07 (`Shrine Choice`) has three mutually exclusive relics (`Brass Vow`, `Ash Thread`, `Vacant Name`), scenario `rep-11` executes as three sub-scenarios (`rep-11a-shrine-brass-vow`, `rep-11b-shrine-ash-thread`, `rep-11c-shrine-vacant-name`), each recording its own deterministic `state_hash` in `run-manifest.json`.

---

## 5. Determinism Regime A Quantization & Three.js `r185` (`0.185.0`) Alignment

1. **Web Audio `OfflineAudioContext` Quantization (`Regime A`)**: Native browser C++ implementations of `BiquadFilterNode`, `DynamicsCompressorNode`, and `PannerNode` produce 1-2 ULP `Float32` differences across CPU SIMD paths. To compute a deterministic `audio_hash` in `Regime A`, render through `OfflineAudioContext(2, sampleRate * durationSec, 48000)`, clamp each channel sample `s` to `[-1.0, 1.0]`, quantize to signed 16-bit PCM with a 2-LSB deadband (`Math.round(s * 8191)`), and hash the resulting `Int16Array` byte buffer with SHA-256.
2. **Procedural Geometry Attribute Quantization (`Regime A`)**: Before computing `geometry_hash` over procedural `BufferGeometry` attributes (`position`, `normal`, `uv`), quantize every floating-point component via `Math.round(val * 1e5) / 1e5` (converting `-0.0` to `0.0`) so transcendental approximations (`Math.sin`, `Math.cos`, `Math.hypot`) do not cause false hash mismatches.
3. **Three.js `r185` (`0.185.0`) Unified `WebGPURenderer` & Post-Processing Warmup**:
   - Import `WebGPURenderer`, `PostProcessing`, and `MeshStandardNodeMaterial` from `three/webgpu` and TSL nodes (`Fn`, `uniform`, `attribute`, `vec3`, `vec4`, `color`, `pass`, `mrt`, `output`, `emissive`) from `three/tsl`.
   - For the WebGL 2 fallback path, instantiate `new THREE.WebGPURenderer({ forceWebGL: true, antialias: true })` so the same TSL `NodeMaterial` and `THREE.PostProcessing` graph runs across both backends without maintaining a separate GLSL `ShaderMaterial` + legacy `EffectComposer` tree.
   - During the loading screen (before `N10_PERF_GATE` frame-time capture begins), execute both `await renderer.compileAsync(scene, camera)` and one offscreen `await postProcessing.renderAsync()` pass so all full-screen post-processing pipelines are compiled before frame 0.
