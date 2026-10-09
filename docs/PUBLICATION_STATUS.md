# Publication Status

Last reviewed: 28 July 2026 (Release `2026.07.5`)

## What This Release Is

This repository publishes a four-volume, `217`-page engineering specification, multi-agent prompt suite, and JSON Schema contract package for deterministic, zero-downloaded-asset Three.js `r185` (`0.185.0`) browser games:

1. **Three.js Evidence Graph: Operational Manual v2.0** (`64` pages) - general multi-agent control plane and dual determinism methodology;
2. **Game 01 - The Hollow Meridian: RPG Full Multi-Agent Production Prompt v1.0** (`81` pages) - third-person dark-fantasy action RPG vertical slice specification;
3. **Game 02 - The Glass Ossuary: Mystery Horror Full Multi-Agent Production Prompt v1.0** (`36` pages) - first-person investigative psychological horror vertical slice specification;
4. **Game 03 - Perihelion Breach: FPS Adventure Full Multi-Agent Production Prompt v1.0** (`36` pages) - first-person kinetic sci-fi shooter adventure vertical slice specification;
5. **Standalone JSON Schema Draft 2020-12 Contracts & Golden Fixtures**: `schemas/*.schema.json`, `schemas/graph-state.d.ts`, 25 copy-pasteable prompts in `prompts/`, and three validated golden reference runs (`examples/run-0001/`, `examples/run-0002/`, `examples/run-0003/`);
6. **Native Four-Language Documentation Suite (`en`, `zh-CN`, `ja`, `ko`)**: 4 repository READMEs (`README*.md`) and 16 native companion guides (`docs/*_GUIDE*.md`), backed by 13 zero-EXIF concept/cover JPEGs and 21 bespoke native-localized typographic, architectural, and 60 Hz telemetry SVGs.

| # | Publication Title | File Path | Edition | Pages | Size (Bytes) | SHA-256 Digest |
| :-: | :--- | :--- | :---: | ---: | ---: | :--- |
| **01** | **Three.js Evidence Graph: Operational Manual** | [`publications/threejs-evidence-graph-operational-manual-v2.0-en.pdf`](../publications/threejs-evidence-graph-operational-manual-v2.0-en.pdf) | `v2.0` | `64` | `416,827` | `d3830d411a61c52c92d6d9f4454d317a5e5bb7dbc3660824e7d24b7a959eb6cd` |
| **02** | **The Hollow Meridian: Action RPG Full Prompt** | [`publications/the-hollow-meridian-rpg-full-prompt-v1.0-en.pdf`](../publications/the-hollow-meridian-rpg-full-prompt-v1.0-en.pdf) | `v1.0` | `81` | `357,144` | `c4f8fe83995d526b99cefddd3d267bf6a3ed42c945b9df0b579193533bfa2b16` |
| **03** | **The Glass Ossuary: Mystery Horror Full Prompt** | [`publications/the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf`](../publications/the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf) | `v1.0` | `36` | `98,649` | `efead090be003782a122463ba17fe686caa1c30aeafcf66f11d294555c7aafda` |
| **04** | **Perihelion Breach: FPS Adventure Full Prompt** | [`publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf`](../publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf) | `v1.0` | `36` | `95,265` | `75bdfff21c905122b4e1a0352e8c760c27e7c80cf8c3d5dcad63ea2263f89170` |

## Authorship and License

All four PDFs use **Emily Paradox** as their publication byline. The canonical creator and rights holder for the repository is **Iamemily2050 (`@iamemily2050`)**. Official profiles and contact details are recorded in [`AUTHORS.md`](../AUTHORS.md).

Unless a file states otherwise, the repository documentation, schemas, prompts, PDFs, SVGs, and original concept artwork are released under the [MIT License](../LICENSE).

## What This Release Is Not

This release ships validated golden contract fixtures in `examples/run-0001/` through `examples/run-0003/`, but it does **not** include:

- a playable Three.js game runtime;
- empirical GPU frame-time measurements from a live build;
- a live Playwright browser capture run; or
- formal WCAG accessibility certification for an implemented UI.

## Accessibility & Security Verification

All four PDFs include root `/Lang (en-US)` and `/MarkInfo << /Marked true >>` catalog declarations and clickable `/Subtype /Link` `/URI` reference annotations on their closing bibliography pages (page 64 of *Evidence Graph v2.0*, page 36 of *The Glass Ossuary v1.0*, and page 36 of *Perihelion Breach v1.0*). All 13 JPEG assets in `assets/*.jpg` contain `0` EXIF bytes. Run `python scripts/verify_release.py` and `sha256sum -c SHA256SUMS.txt` from the repository root to verify every file.
