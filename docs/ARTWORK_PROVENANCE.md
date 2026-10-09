# Artwork & Vector Typography Provenance (`2026.07.5`)

Every visual file is a specification artifact. None are runtime captures. All visual assets in `assets/` and `assets/svg/` are explanatory publication plates, concept artwork, and vector architectural diagrams created specifically for this repository, not empirical GPU benchmark evidence.

## 1. Zero-EXIF Concept & Cover JPEG Assets (`assets/*.jpg`, 13 Files)

Every JPEG asset is stripped of EXIF/metadata payloads (`0` EXIF bytes verified by `python scripts/verify_release.py`) and checksummed in [`SHA256SUMS.txt`](../SHA256SUMS.txt):

| Asset Path | Dimensions | Role & Associated Publication |
| :--- | :---: | :--- |
| `assets/readme-hero.jpg` | `2172x724` | Repository panoramic visual-system banner |
| `assets/evidence-graph-control-hero.jpg` | `2172x724` | *Three.js Evidence Graph v2.0* control-plane section hero |
| `assets/hollow-meridian-world-hero.jpg` | `2172x724` | *The Hollow Meridian* (Game 01) world route concept plate |
| `assets/hollow-meridian-boss-hero.jpg` | `2172x724` | *The Hollow Meridian* (Game 01) *The Bell Without a Name* boss plate |
| `assets/glass-ossuary-investigation-hero.jpg` | `1600x893` | *The Glass Ossuary* (Game 02) *Refraction Gallery* forensic investigation plate |
| `assets/glass-ossuary-apparition-hero.jpg` | `1600x893` | *The Glass Ossuary* (Game 02) *The Choir in the Glass* boss encounter plate |
| `assets/perihelion-breach-world-hero.jpg` | `1600x893` | *Perihelion Breach* (Game 03) *Icarus-9 Heliostat Truss* traversal plate |
| `assets/perihelion-breach-combat-hero.jpg` | `1600x893` | *Perihelion Breach* (Game 03) *The Heliarch Warden* aerial boss combat plate |
| `assets/publication-set.jpg` | `1600x993` | Four-publication composite cover plate (`217` pages total) |
| `assets/threejs-evidence-graph-cover.jpg` | `1191x1684` | Page-1 cover plate of *Three.js Evidence Graph v2.0* (`64` pages) |
| `assets/the-hollow-meridian-cover.jpg` | `1191x1684` | Page-1 cover plate of *The Hollow Meridian v1.0* (`81` pages) |
| `assets/the-glass-ossuary-cover.jpg` | `1400x1812` | Page-1 cover plate of *The Glass Ossuary v1.0* (`36` pages) |
| `assets/perihelion-breach-cover.jpg` | `1400x1812` | Page-1 cover plate of *Perihelion Breach v1.0* (`36` pages) |

## 2. Custom Typographic, Architectural & 60 Hz Telemetry SVGs (`assets/svg/*.svg`, 21 Files)

Because GitHub strips custom CSS and `@font-face` rules from Markdown, the repository uses resolution-independent SVG diagrams in `assets/svg/` with curated system and CJK font stacks (`Inter`/`Segoe UI`, `JetBrains Mono`, `PingFang SC`/`Microsoft YaHei`, `Hiragino Sans`/`Yu Gothic UI`, `Pretendard`/`Malgun Gothic`) so every diagram is natively authored in English (`en`), Simplified Chinese (`zh-CN`), Japanese (`ja`), and Korean (`ko`):

- **Suite Mastheads (4 files, `1260x356`)**:
  - `assets/svg/masthead-en.svg`: Native English suite masthead
  - `assets/svg/masthead-zh-CN.svg`: Native Simplified Chinese suite masthead
  - `assets/svg/masthead-ja.svg`: Native Japanese suite masthead
  - `assets/svg/masthead-ko.svg`: Native Korean suite masthead
- **15-Node Evidence Graph & Three-Genre Instantiation Architecture Diagrams (5 files, `1260x348`)**:
  - `assets/svg/architecture-pipeline.svg`: Canonical English 15-node (`N00`..`N14`) architecture pipeline diagram
  - `assets/svg/architecture-pipeline-en.svg`: Native English 15-node (`N00`..`N14`) architecture pipeline diagram
  - `assets/svg/architecture-pipeline-zh-CN.svg`: Native Simplified Chinese 15-node (`N00`..`N14`) architecture pipeline diagram
  - `assets/svg/architecture-pipeline-ja.svg`: Native Japanese 15-node (`N00`..`N14`) architecture pipeline diagram
  - `assets/svg/architecture-pipeline-ko.svg`: Native Korean 15-node (`N00`..`N14`) architecture pipeline diagram
- **Game 01 (*The Hollow Meridian*) 60 Hz Combat Frame & Palette Telemetry Cards (4 files, `1260x320`)**:
  - `assets/svg/game-01-telemetry-en.svg`, `assets/svg/game-01-telemetry-zh-CN.svg`, `assets/svg/game-01-telemetry-ja.svg`, `assets/svg/game-01-telemetry-ko.svg`
- **Game 02 (*The Glass Ossuary*) 60 Hz Forensic Instrument & Acoustic Telemetry Cards (4 files, `1260x320`)**:
  - `assets/svg/game-02-telemetry-en.svg`, `assets/svg/game-02-telemetry-zh-CN.svg`, `assets/svg/game-02-telemetry-ja.svg`, `assets/svg/game-02-telemetry-ko.svg`
- **Game 03 (*Perihelion Breach*) 60 Hz Ballistics, Thermal Vent & Grapple Telemetry Cards (4 files, `1260x320`)**:
  - `assets/svg/game-03-telemetry-en.svg`, `assets/svg/game-03-telemetry-zh-CN.svg`, `assets/svg/game-03-telemetry-ja.svg`, `assets/svg/game-03-telemetry-ko.svg`
