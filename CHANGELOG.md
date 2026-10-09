# Changelog

Every release is verified.

All notable changes to the publication bundle are documented here.

## [2026.07.5] - 2026-07-28

### Added

- **Game 02 Flagship Publication (*Mystery on Horror*)**: Added `publications/the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf` (`36` pages, A4 vector PDF with `/Lang (en-US)`, `/MarkInfo << /Marked true >>`, and 20 clickable `/URI` reference links on page 36), specifying a 12-to-16-minute first-person investigative psychological horror vertical slice (*The Glass Ossuary* / 《琉璃骸骨堂》 / 『硝子の納骨堂』 / 《유리 납골당》) in Three.js `r185` (`0.185.0`) with zero downloaded assets
- **Game 03 Flagship Publication (*First-Person Shooter Adventure*)**: Added `publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf` (`36` pages, A4 vector PDF with `/Lang (en-US)`, `/MarkInfo << /Marked true >>`, and 20 clickable `/URI` reference links on page 36), specifying a 12-to-15-minute first-person kinetic sci-fi shooter adventure vertical slice (*Perihelion Breach* / 《近日点破袭》 / 『ペリヘリオン・ブリーチ』 / 《근일점 돌파》) in Three.js `r185` (`0.185.0`) with zero downloaded assets
- **Native Four-Language Companion Guides for All Four Publications (`16` Guides in `docs/`)**: Added native English, Simplified Chinese (`zh-CN`), Japanese (`ja`), and Korean (`ko`) companion guides for *The Glass Ossuary* (`docs/THE_GLASS_OSSUARY_GUIDE.{md,zh-CN.md,ja.md,ko.md}`) and *Perihelion Breach* (`docs/PERIHELION_BREACH_GUIDE.{md,zh-CN.md,ja.md,ko.md}`), and updated `docs/EVIDENCE_GRAPH_GUIDE.*` and `docs/THE_HOLLOW_MERIDIAN_GUIDE.*` with full four-publication cross-links
- **Complete Collector's Monograph Redesign & 21-SVG Archival Blueprint Suite**: Rebuilt `README.md`, `README.zh-CN.md`, `README.ja.md`, and `README.ko.md` and all 16 companion guides in `docs/` as native Collector's Monographs (`en`, `zh-CN`, `ja`, `ko`) with zero `img.shields.io` badge clutter, paired with 21 warm archival vellum & copperplate engineering blueprint SVGs in `assets/svg/` (`masthead-{en,zh-CN,ja,ko}.svg`, `architecture-pipeline{,-en,-zh-CN,-ja,-ko}.svg`, and `game-01..03-telemetry-{en,zh-CN,ja,ko}.svg`)
- **17 Zero-EXIF Collector's Monograph Covers, Concept Plates, Prompts & Golden Reference Runs (`run-0002` & `run-0003`)**:
  - Added and redesigned 17 zero-EXIF JPEG plates (`assets/readme-hero.jpg`, `assets/publication-set.jpg`, 4 bespoke Collector's Monograph covers `assets/*-cover.jpg`, and 11 fine-art concept plates including `evidence-graph-control-hero.jpg`, `evidence-graph-atelier-hero.jpg`, `hollow-meridian-world-hero.jpg`, `hollow-meridian-boss-hero.jpg`, `hollow-meridian-sanctum-hero.jpg`, `glass-ossuary-investigation-hero.jpg`, `glass-ossuary-apparition-hero.jpg`, `glass-ossuary-inquest-hero.jpg`, `perihelion-breach-world-hero.jpg`, `perihelion-breach-combat-hero.jpg`, and `perihelion-breach-arsenal-hero.jpg`)
  - Added 16 standalone copy-pasteable orchestrator and specialist agent prompt files in `prompts/glass-ossuary/` and `prompts/perihelion-breach/` (mirrored in `orchestration/prompts/`)
  - Added schema-validated golden reference fixtures in `examples/run-0002/` (*The Glass Ossuary*, `seed=1894`) and `examples/run-0003/` (*Perihelion Breach*, `seed=2142`)
  - Added `docs/ARTWORK_PROVENANCE.md` and Section 6 of `docs/TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md`

## [2026.07.4] - 2026-07-27

### Added

- Standalone Draft 2020-12 JSON Schemas (`schemas/task-packet.schema.json`, `schemas/defect-record.schema.json`, `schemas/run-manifest.schema.json`) and TypeScript state definitions (`schemas/graph-state.d.ts`), mirrored in `orchestration/`
- Standalone copy-pasteable prompts (`prompts/evidence-graph/orchestrator.md`, `prompts/hollow-meridian/orchestrator.md`, and seven specialist agent prompt cards in `prompts/hollow-meridian/agents/*.md`, mirrored in `orchestration/prompts/` and `agents/`)
- Validated golden reference fixtures in `examples/run-0001/` (`task-packet.json`, `defect-record.json`, `run-manifest.json`)
- Technical errata and cross-edition alignment specification (`docs/TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md`)
- Four-language companion guides for the primary manual (`docs/EVIDENCE_GRAPH_GUIDE.md`, `.zh-CN.md`, `.ja.md`, `.ko.md`)
- Automated release and contract verification script (`scripts/verify_release.py`) and GitHub Actions workflow (`.github/workflows/verify-release.yml`)

### Fixed

- Fixed JetBrains Mono `/ToUnicode` ligature mapping (`<048f> <002d>`) in `publications/threejs-evidence-graph-operational-manual-v2.0-en.pdf` so `--` in CLI commands (`npm run test:perf -- hero-prewarm`) extracts cleanly instead of `/-`
- Shifted the `P95 BUDGET 16.6 MS` label on page 1 of `threejs-evidence-graph-operational-manual-v2.0-en.pdf` above the dashed budget line so it no longer collides with the blue P95 curve
- Updated References `[9]` and `[10]` on page 64 of `threejs-evidence-graph-operational-manual-v2.0-en.pdf` to live Three.js `r185` WebGPU/TSL URLs and added 23 clickable `/Subtype /Link` `/URI` annotations across page 64
- Shifted the top-right vertical accent bars on page 1 of `publications/the-hollow-meridian-rpg-full-prompt-v1.0-en.pdf` clear of `VERSION 1.0 / JULY 2026`, softened the red curve crossing the subtitle, and recolored the off-palette `#7567F5` inner ring to tarnished brass (`#D5A54B`)
- Fixed right-edge clipping of `MERIDIAN CHAMBER` on page 9, brightened dark-on-dark section divider numerals and radar rings on pages 2, 7, 25, 43, and 63, unified the closing page 81 background card, and added `/Lang (en-US)` and `/MarkInfo << /Marked true >>` to both PDF catalogs
- Regenerated `assets/threejs-evidence-graph-cover.jpg`, `assets/the-hollow-meridian-cover.jpg`, and `assets/publication-set.jpg` from the repaired page-1 renders, cleaned the worker border strips in `assets/evidence-graph-control-hero.jpg`, and verified zero EXIF bytes across all seven JPEG assets
- Enforced LF (`eol=lf`) on `SHA256SUMS.txt` in `.gitattributes` for cross-platform `sha256sum -c` compatibility
- Standardized the canonical repository URL (`https://github.com/Emily2040/-threejs-evidence-graph`) across `CITATION.cff`, `CITATIONS.md`, and `release-manifest.json`, set `type: software` in `CITATION.cff`, and normalized BibTeX fields in `CITATIONS.md`
- Corrected localized page-count references to `145` (`64 + 81` pages), fixed the unlocalized character `遺物` in `README.ja.md`, added canonical English beat names to `docs/THE_HOLLOW_MERIDIAN_GUIDE.zh-CN.md`, synchronized the three-paragraph gameplay summary in `README.md`, and promoted localized guides to `translation_status: reviewed`

## [2026.07.3] - 2026-07-27

### Added

- SHA-256 integrity coverage for all seven JPEG assets and both PDF publications
- Complete artwork dimensions and hashes in the machine-readable release manifest
- Structural security review of repository history, links, PDFs, and JPEG assets

### Changed

- Prepared the canonical repository name as `threejs-evidence-graph`
- Updated citation and release metadata to the canonical repository URL
- Expanded multilingual integrity instructions with a reproducible verification command

### Security

- Found no exposed tokens, private keys, credentials, unsafe URL schemes, executable repository files, PDF active content, PDF attachments, JPEG metadata, or appended JPEG payloads

## [2026.07.2] - 2026-07-27

### Added

- MIT License aligned with the canonical Seedance V2 repository
- Author and rights-holder record with official GitHub, website, X, Instagram, and contact links
- Machine-readable creator, profile, copyright, license, and scope metadata

### Changed

- Updated all four README editions with the license terms and canonical creator identity
- Corrected repository URLs in citation and release metadata to the live GitHub repository
- Updated publication-status and release documents for the licensed release

### Status

- Documentation, identity, and licensing patch
- Publication byline remains Emily Paradox
- Creator and copyright holder is Iamemily2050 (@iamemily2050)
- Repository contents are released under the MIT License unless a file states otherwise

## [2026.07.1] - 2026-07-27

### Added

- Expanded *The Hollow Meridian* explanatory game guide
- Full companion-guide editions in Simplified Chinese, Japanese, and Korean
- Detailed route, play-loop, combat, boss, relic, save, procedural-media, accessibility, and evidence explanations
- Three coordinated ImageGen section heroes for the control plane, authored game route, and boss transition
- Prompt and provenance record for the new artwork
- Expanded multilingual game-development glossary
- Language-review checklist and localized-surface matrix

### Changed

- Expanded all four README editions with clearer game explanations and companion-guide links
- Updated the repository map, publication status, translation policy, release notes, and manifest

### Status

- Documentation and concept-art update
- English remains normative for both PDFs
- Localized guides remain marked unreviewed until independent native-language technical review
- No playable implementation or benchmark included

## [2026.07.0] - 2026-07-27

### Added

- *Three.js Evidence Graph v2.0* PDF
- *The Hollow Meridian RPG Full Prompt v1.0* PDF
- English publication guide
- Simplified Chinese, Japanese, and Korean publication guides
- Publication-status and translation-policy documents
- Multilingual technical glossary
- Citation metadata
- PDF integrity checksums
- Contribution guidance
- Repository cover assets
- ImageGen-created multilingual README hero banner

### Status

- Documentation and specification release
- No playable implementation or benchmark included
- No reuse license selected
