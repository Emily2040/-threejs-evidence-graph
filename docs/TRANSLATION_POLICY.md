# Native Multilingual Documentation & Translation Policy

## Normative Language & Native Four-Language Architecture

English is the normative language for the four PDF specifications (`217` pages total), JSON Schema Draft 2020-12 contracts (`schemas/`), TypeScript state interfaces, and copy-pasteable agent prompts (`prompts/`).

Alongside the English specifications, this repository provides **native-authored documentation suites in four languages** - **English (`en`)**, **Simplified Chinese (`zh-CN`)**, **Japanese (`ja`)**, and **Korean (`ko`)** - across the main repository READMEs (`README*.md`) and all four publication companion guides (`docs/*_GUIDE*.md`). Rather than mechanical sentence-by-sentence translation (`翻译腔` / `直訳調` / `번역투`), each language edition is written in authentic, domain-native game-engine and graphics-engineering prose while keeping every code identifier, schema key, tick window, and CLI command identical.

## Localized Surfaces (`2026.07.5`)

| Surface | English (`en`) | Simplified Chinese (`zh-CN`) | Japanese (`ja`) | Korean (`ko`) |
| :--- | :---: | :---: | :---: | :---: |
| **Repository Suite Overview (`README*.md`)** | [`README.md`](../README.md) | [`README.zh-CN.md`](../README.zh-CN.md) | [`README.ja.md`](../README.ja.md) | [`README.ko.md`](../README.ko.md) |
| **Custom Typographic SVG Masthead (`assets/svg/masthead-*.svg`)** | [`masthead-en.svg`](../assets/svg/masthead-en.svg) | [`masthead-zh-CN.svg`](../assets/svg/masthead-zh-CN.svg) | [`masthead-ja.svg`](../assets/svg/masthead-ja.svg) | [`masthead-ko.svg`](../assets/svg/masthead-ko.svg) |
| **Pub 01 Guide: Evidence Graph v2.0 (`docs/EVIDENCE_GRAPH_GUIDE*.md`)** | [EN](EVIDENCE_GRAPH_GUIDE.md) | [中文](EVIDENCE_GRAPH_GUIDE.zh-CN.md) | [日本語](EVIDENCE_GRAPH_GUIDE.ja.md) | [한국어](EVIDENCE_GRAPH_GUIDE.ko.md) |
| **Pub 02 Guide: The Hollow Meridian (`docs/THE_HOLLOW_MERIDIAN_GUIDE*.md`)** | [EN](THE_HOLLOW_MERIDIAN_GUIDE.md) | [中文](THE_HOLLOW_MERIDIAN_GUIDE.zh-CN.md) | [日本語](THE_HOLLOW_MERIDIAN_GUIDE.ja.md) | [한국어](THE_HOLLOW_MERIDIAN_GUIDE.ko.md) |
| **Pub 03 Guide: The Glass Ossuary (`docs/THE_GLASS_OSSUARY_GUIDE*.md`)** | [EN](THE_GLASS_OSSUARY_GUIDE.md) | [中文](THE_GLASS_OSSUARY_GUIDE.zh-CN.md) | [日本語](THE_GLASS_OSSUARY_GUIDE.ja.md) | [한국어](THE_GLASS_OSSUARY_GUIDE.ko.md) |
| **Pub 04 Guide: Perihelion Breach (`docs/PERIHELION_BREACH_GUIDE*.md`)** | [EN](PERIHELION_BREACH_GUIDE.md) | [中文](PERIHELION_BREACH_GUIDE.zh-CN.md) | [日本語](PERIHELION_BREACH_GUIDE.ja.md) | [한국어](PERIHELION_BREACH_GUIDE.ko.md) |
| **Multilingual Technical Glossary (`docs/GLOSSARY.md`)** | Yes | Yes | Yes | Yes |
| **Normative PDFs (`publications/*.pdf`, 217 pages total)** | Yes (4 PDFs) | Companion Guides | Companion Guides | Companion Guides |

All localized Markdown files carry a machine-checked provenance header (`<!-- source_version: 2026.07.5; translation_status: reviewed; language: ... -->`) verified by `python scripts/verify_release.py`.

## Content Retained in Canonical English Across All Editions

To guarantee zero ambiguity when developers or LLM agents cross-reference localized guides against the schemas and prompts, the following items remain in canonical English across all four languages:

- filenames, directory paths, and URLs;
- CLI commands (`npm run verify:all`, `python scripts/verify_release.py`, `sha256sum -c SHA256SUMS.txt`);
- JSON Schema property names and enum values (`A-PinnedBrowser`, `B-CrossPlatform`, `brass_vow`, `ash_thread`, `vacant_name`, `lens_sabotage`, `tidal_quarantine`, `acoustic_calling`, `recoil_gyro`, `thermal_siphon`, `grapple_overdrive`);
- 15-node graph identifiers (`N00_BRIEF` through `N14_RELEASE_CANDIDATE`);
- defect identifiers (`RPG-N06A-COMBAT-014`, `HOR-N06A-AUDIO-008`, `FPS-N06A-COMBAT-019`);
- browser QA globals (`window.__rpgQA`, `window.__horrorQA`, `window.__fpsQA`);
- canonical English game, zone, beat, and enemy identifiers on first reference.

## Quality & Native Readability Checklist

Every localized document is verified against eight criteria:

1. **Native domain register**: Uses authentic terminology expected by Chinese (`前摇/后摇/帧数表/削韧/受击硬直`), Japanese (`発生・持続・硬直フレーム/ジャストパリィ/強靭削り/逆位相消音`), and Korean (`선딜레이/후딜레이/무적 틱/강인도/역위상 상쇄`) game engineers.
2. **Script purity**: Zero Simplified Chinese characters (`遗`, `设`, etc.) leaking into Japanese `.ja.md` files.
3. **Numeric & hash parity**: Every frame count, tick window, HP/Poise value, draw-call budget, page count (`217` total: `64 + 81 + 36 + 36`), and SHA-256 prefix matches the English source.
4. **Epistemic honesty**: Preserves explicit statements that this repository ships specifications, schemas, prompts, and golden contract fixtures, not a finished runtime build or benchmark run.
5. **Concept-artwork labeling**: Captions clearly state that cover and hero plates are concept artwork, not runtime screenshots.
6. **Cross-language navigation**: Every README and companion guide links directly to all four language editions and all four publications.
7. **Glossary alignment**: Adheres to [`docs/GLOSSARY.md`](GLOSSARY.md).
8. **Automated verification**: Passes `python scripts/verify_release.py` with zero broken links or unreviewed headers.
