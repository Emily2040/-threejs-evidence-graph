# Publication Status

Last reviewed: 27 July 2026 (Release `2026.07.4`)

## What this release is

This repository is a document and contract-schema publication containing:

- *Three.js Evidence Graph v2.0*, a 64-page general operational framework;
- *The Hollow Meridian RPG Full Prompt v1.0*, an 81-page game-specific product contract and orchestration prompt;
- standalone Draft 2020-12 JSON Schemas (`schemas/*.schema.json`), TypeScript state definitions (`schemas/graph-state.d.ts`), copy-pasteable prompts (`prompts/`), golden reference fixtures (`examples/run-0001/`), and technical errata (`docs/TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md`);
- multilingual repository guides (`README*.md`), *Three.js Evidence Graph v2.0* companion guides (`docs/EVIDENCE_GRAPH_GUIDE*.md`), and expanded *The Hollow Meridian* companion guides (`docs/THE_HOLLOW_MERIDIAN_GUIDE*.md`) in English, Simplified Chinese, Japanese, and Korean;
- cover and concept artwork, prompt provenance, citation metadata, version history, contribution guidance, automated verification (`scripts/verify_release.py`), and checksums (`SHA256SUMS.txt`).

| Title | File Path | Edition | Pages | Size (Bytes) | SHA-256 Digest |
|---|---|---|---:|---:|---|
| **Three.js Evidence Graph: Operational Manual** | [`publications/threejs-evidence-graph-operational-manual-v2.0-en.pdf`](../publications/threejs-evidence-graph-operational-manual-v2.0-en.pdf) | `v2.0` | `64` | `416,827` | `d3830d411a61c52c92d6d9f4454d317a5e5bb7dbc3660824e7d24b7a959eb6cd` |
| **The Hollow Meridian: Full Multi-Agent Production Prompt** | [`publications/the-hollow-meridian-rpg-full-prompt-v1.0-en.pdf`](../publications/the-hollow-meridian-rpg-full-prompt-v1.0-en.pdf) | `v1.0` | `81` | `357,144` | `c4f8fe83995d526b99cefddd3d267bf6a3ed42c945b9df0b579193533bfa2b16` |

All seven published JPEG assets, both PDF files, standalone schemas, golden fixtures, prompts, and documentation files are recorded in [`SHA256SUMS.txt`](../SHA256SUMS.txt). The release manifest ([`release-manifest.json`](../release-manifest.json)) records artwork dimensions and hashes in addition to publication and schema metadata.

## Authorship and license

The two PDFs use **Emily Paradox** as their publication byline. The canonical
creator and rights holder for the repository is **Iamemily2050
(@iamemily2050)**. Official profiles and the contact address are recorded in
[AUTHORS.md](../AUTHORS.md).

Unless a file states otherwise, the repository documentation, schemas, prompts,
PDFs, and original concept artwork are released under the [MIT License](../LICENSE).
Copies or substantial portions must retain the copyright and permission
notices. Citation is requested for academic, editorial, and technical
discussion, but it is not an additional license condition.

## What this release is not

This release includes standalone JSON Schemas, prompts, and schema-validated golden reference fixtures in `examples/run-0001/`, but it does not include:

- a playable game;
- a complete Three.js runtime implementation;
- a live production orchestrator binary;
- empirical benchmark or GPU frame-time measurements from a playable build;
- a live Playwright capture run;
- proof of cross-browser or cross-device runtime determinism;
- proof of formal WCAG accessibility conformance;
- proof that an AAA-grade runtime target has been achieved.

## Evidence interpretation

The Evidence Graph cover chart is explicitly illustrative. It is not run data.

Performance budgets in both PDFs are acceptance targets until a specific device, operating system, browser, renderer, quality profile, and commit have been measured.

Simulation and controlled data may qualify for bit-exact comparison under pinned conditions (`Regime A`, using integer 60 Hz ticks, 16-bit PCM audio quantization, and `1e-5` geometry vertex quantization as specified in [`docs/TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md`](TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md)). GPU-rasterized evidence and cross-profile comparisons require declared tolerances (`Regime B`).

## Relationship between the publications

*Three.js Evidence Graph v2.0* is the general methodology. *The Hollow Meridian v1.0* shares its core control model and was authored prior to several v2 safeguards.

In release `2026.07.4`, [`docs/TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md`](TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md) and [`schemas/`](../schemas/) provide the unified v2.0 contract layer bridging both publications without altering their historical scope distinction.

## Technical currency

The publications use Three.js `r185` (`0.185.0`) as their pinned baseline. Future Three.js releases may change APIs, renderer behavior, TSL capabilities, browser compatibility, and performance characteristics. A working implementation should pin exact dependency versions and re-run the renderer and compatibility gates before making current claims.

## Accessibility

Both PDFs include root `/Lang (en-US)` and `/MarkInfo << /Marked true >>` catalog declarations, and the standalone Markdown files (`README*.md`, `docs/EVIDENCE_GRAPH_GUIDE*.md`, `docs/THE_HOLLOW_MERIDIAN_GUIDE*.md`, `docs/TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md`, `prompts/**/*.md`, and `schemas/*.schema.json`) provide accessible, copy-pasteable text equivalents for the schemas, prompts, and guides.

## Artwork interpretation

The README and game-guide hero images are original concept artwork. They communicate the control model, authored route, material language, and intended boss readability. They are not gameplay screenshots, renderer captures, performance evidence, or proof that a playable build exists.

## Security review

The release files were checked for exposed credentials, unsafe URL schemes,
unexpected executable file modes, PDF active content and attachments, and
JPEG metadata or appended payloads (`0` EXIF bytes across all seven JPEGs). No
credential or executable-content issue was found. This structural review does
not constitute steganalysis and cannot guarantee the future safety of
externally linked websites.

## Future evidence threshold

An empirical runtime release should include, at minimum:

1. a runnable repository at one accepted commit;
2. declared authority documents and quality gates;
3. validated task, defect, and run schemas (shipped in `schemas/`);
4. deterministic replay evidence under declared conditions;
5. declared-tolerance raster comparisons;
6. frame-time distributions on named devices;
7. provenance, bundle, and network audits;
8. critic calibration records;
9. a complete cost ledger;
10. one successful runtime repair and one verified rollback;
11. two clean regression cycles;
12. an evidence index that binds every claim to an artifact.
