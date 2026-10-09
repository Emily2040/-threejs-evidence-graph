# Artwork & Vector Typography Provenance (`2026.07.5`)

All visual assets in `assets/` and `assets/svg/` are explanatory publication plates, concept artwork, and vector architectural diagrams created specifically for this repository. None of these files are presented as captures from a finished runtime build or empirical GPU benchmark evidence.

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

## 2. Custom Typographic & Architectural SVGs (`assets/svg/*.svg`, 5 Files)

Because GitHub strips custom CSS and `@font-face` rules from Markdown, the repository uses resolution-independent SVG banners in `assets/svg/` with curated system and CJK font stacks (`Inter`/`Segoe UI`, `JetBrains Mono`, `PingFang SC`/`Microsoft YaHei`, `Hiragino Sans`/`Yu Gothic UI`, `Pretendard`/`Malgun Gothic`):

- `assets/svg/masthead-en.svg`: Native English suite masthead (`1260x356`)
- `assets/svg/masthead-zh-CN.svg`: Native Simplified Chinese suite masthead (`1260x356`)
- `assets/svg/masthead-ja.svg`: Native Japanese suite masthead (`1260x356`)
- `assets/svg/masthead-ko.svg`: Native Korean suite masthead (`1260x356`)
- `assets/svg/architecture-pipeline.svg`: 15-node Evidence Graph (`N00`..`N14`) and 3-genre instantiation diagram (`1260x340`)
