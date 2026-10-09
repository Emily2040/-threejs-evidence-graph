# v2026.07.4 - Contract Schemas, PDF Repairs, and Multilingual Parity

This release publishes two complementary works under the publication byline Emily Paradox:

- *Three.js Evidence Graph: Operational Manual v2.0*
- *The Hollow Meridian RPG Full Prompt v1.0*

The canonical creator and rights-holder identity is Iamemily2050
(@iamemily2050). Official profiles and the contact address are recorded in
`AUTHORS.md` and `release-manifest.json`.

## What the release contributes

*Three.js Evidence Graph* defines a repository-local production model in which deterministic code controls state, scheduling, budgets, gates, rollback, and release. Bounded specialist agents implement work. Independent capture, mechanical checks, calibrated critics, and provenance audits determine whether a change is accepted.

*The Hollow Meridian* turns the same core lineage into a game-specific production contract for an intended 10 to 14 minute third-person action RPG vertical slice. It fixes the route, combat scope, enemies, boss, RPG decisions, procedural-media policy, agent roles, QA interfaces, repair process, and release gates.

Release `2026.07.4` adds the standalone machine-readable JSON Schema Draft 2020-12 contracts (`schemas/*.schema.json`), TypeScript state contract (`schemas/graph-state.d.ts`), copy-pasteable orchestrator and specialist prompts (`prompts/`), validated golden reference fixtures (`examples/run-0001/`), technical errata (`docs/TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md`), four-language companion guides for *Three.js Evidence Graph v2.0* (`docs/EVIDENCE_GRAPH_GUIDE.*.md`), direct PDF stream and vector typography repairs, regenerated cover artwork, and automated verification (`scripts/verify_release.py`).

## Included

- 64-page Evidence Graph English PDF (with repaired `--` `/ToUnicode` mapping, repaired page-1 P95 label placement, and 23 clickable `/URI` reference annotations on page 64)
- 81-page Hollow Meridian English PDF (with repaired page-1 top-right version bar clearance, palette-aligned brass/cyan rings on pages 1 and 9, unclipped page-9 `MERIDIAN CHAMBER` label, higher-contrast section divider numerals/rings, and unified page-81 closing card)
- Standalone JSON Schemas (`schemas/task-packet.schema.json`, `schemas/defect-record.schema.json`, `schemas/run-manifest.schema.json`) and `schemas/graph-state.d.ts` (mirrored in `orchestration/`)
- Standalone copy-pasteable prompts (`prompts/evidence-graph/orchestrator.md`, `prompts/hollow-meridian/orchestrator.md`, and `prompts/hollow-meridian/agents/*.md`, mirrored in `orchestration/prompts/` and `agents/`)
- Golden reference fixtures (`examples/run-0001/task-packet.json`, `defect-record.json`, `run-manifest.json`)
- Technical errata and cross-edition v2.0 alignment guide (`docs/TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md`)
- English, Simplified Chinese, Japanese, and Korean repository guides (`README*.md`)
- English, Simplified Chinese, Japanese, and Korean *Three.js Evidence Graph v2.0* companion guides (`docs/EVIDENCE_GRAPH_GUIDE*.md`)
- English, Simplified Chinese, Japanese, and Korean *The Hollow Meridian* companion guides (`docs/THE_HOLLOW_MERIDIAN_GUIDE*.md`)
- Expanded multilingual technical glossary (`docs/GLOSSARY.md`)
- Publication-status and translation-policy documents (`docs/PUBLICATION_STATUS.md`, `docs/TRANSLATION_POLICY.md`)
- Normalized PDF metadata, `/Lang (en-US)`, and `/MarkInfo` declarations
- Citation metadata (`CITATION.cff` and `CITATIONS.md`)
- SHA-256 integrity checksums (`SHA256SUMS.txt` with enforced LF line endings covering 39 release artifacts)
- Machine-readable release manifest (`release-manifest.json`), changelog (`CHANGELOG.md`), and verification suite (`scripts/verify_release.py` and `.github/workflows/verify-release.yml`)
- Regenerated cover and concept artwork (`assets/*.jpg`) with zero EXIF bytes

## Evidence status

This is a documentation, specification, and contract-schema release.

It includes validated golden contract fixtures in `examples/run-0001/`, but it does not include:

- a playable game;
- a completed Three.js runtime implementation;
- empirical benchmark results or measured GPU performance data;
- a live browser capture run;
- empirical proof of an AAA-grade runtime result.

Figure 0 in the Evidence Graph manual is an illustrative target profile, not run data.

## Version relationship

*The Hollow Meridian v1.0* is core-aligned with the Evidence Graph lineage. It is not certified as a completed runtime implementation of Evidence Graph v2.0.

In release `2026.07.4`, [`docs/TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md`](docs/TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md) and [`schemas/`](schemas/) reconcile the schema contracts between both editions for:

- two explicit evidence regimes (`A-PinnedBrowser` and `B-CrossPlatform`);
- mandatory `cost_ledger` and `human_signoff` blocks in `run-manifest.schema.json`;
- integer 60 Hz tick combat framing, button-down Parry/Guard disambiguation, and Phase 2 `Split Meridian Rings` weak-point timing;
- 16-bit PCM quantization for `OfflineAudioContext` hashing and `1e-5` vertex quantization for procedural geometry in Regime A;
- Three.js `r185` (`0.185.0`) `THREE.WebGPURenderer` with `{ forceWebGL: true }` fallback and `postProcessing.renderAsync()` pre-warming.

## Translation scope

The four README guides, four *Three.js Evidence Graph v2.0* companion guides, and four *The Hollow Meridian* companion guides explain the repository publication, control graph, and RPG specification in English, Simplified Chinese, Japanese, and Korean.

The 145 designed PDF pages (`64 + 81` pages) remain the normative English editions. All localized Markdown guides carry `translation_status: reviewed` and are verified by `python scripts/verify_release.py`.

## Artwork status

The hero images are original concept artwork generated for this repository, and the cover composites are rendered directly from the repaired page-1 PDF plates. They are explicitly presented as explanatory publication images, not gameplay screenshots, renderer captures, benchmark evidence, or proof of implementation.

## Technical baseline

The publications were authored against Three.js `r185` (`0.185.0`). This is a pinned document baseline, not a promise that future implementations can ignore later API, renderer, browser, or device changes.

## Integrity

Use `sha256sum -c SHA256SUMS.txt` and `python scripts/verify_release.py` from the repository root to verify all 39 checksummed files, JSON schemas, golden fixtures, PDFs, JPEGs, and Markdown links. Never replace a publication or artwork asset silently inside this release. Corrections require updated checksums, a changelog entry, and a new repository release.

The release files were reviewed for exposed credentials, unsafe URL schemes,
unexpected executable file modes, PDF active content and attachments, and
JPEG metadata or appended payloads. No credential or executable-content issue
was found. This is a structural release audit, not a claim that future external
links or deliberately concealed pixel data can never present risk.

## License

This repository is released under the MIT License.

Copyright (c) 2026 Iamemily2050 (@iamemily2050).

Unless a file states otherwise, the license covers the repository
documentation, schemas, prompts, PDFs, and original concept artwork. Copies or
substantial portions must retain the copyright and permission notices. Citation
is requested for academic, editorial, and technical discussion, but it is not an
additional license condition.
