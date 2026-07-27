# Publication Status

Last reviewed: 27 July 2026

## What this release is

This repository is a document publication containing:

- *Three.js Evidence Graph v2.0*, a general operational framework;
- *The Hollow Meridian RPG Full Prompt v1.0*, a game-specific product contract and orchestration prompt;
- multilingual repository guides in English, Simplified Chinese, Japanese, and Korean;
- expanded *The Hollow Meridian* companion guides in the same four languages;
- cover and concept artwork, prompt provenance, citation metadata, version history, contribution guidance, and checksums.

All seven published JPEG assets and both PDF files are recorded in
[`SHA256SUMS.txt`](../SHA256SUMS.txt). The release manifest records artwork
dimensions and hashes in addition to publication metadata.

## Authorship and license

The two PDFs use **Emily Paradox** as their publication byline. The canonical
creator and rights holder for the repository is **Iamemily2050
(@iamemily2050)**. Official profiles and the contact address are recorded in
[AUTHORS.md](../AUTHORS.md).

Unless a file states otherwise, the repository documentation, PDFs, and
original concept artwork are released under the [MIT License](../LICENSE).
Copies or substantial portions must retain the copyright and permission
notices. Citation is requested for academic, editorial, and technical
discussion, but it is not an additional license condition.

## What this release is not

This release does not include:

- a playable game;
- a complete Three.js reference implementation;
- a production orchestrator;
- a benchmark;
- measured performance results;
- a completed evidence manifest;
- calibrated critic fixtures;
- a provenance scanner;
- an accepted `run-0001`;
- proof of cross-browser or cross-device determinism;
- proof of accessibility conformance;
- proof that an AAA-grade target has been achieved.

## Evidence interpretation

The Evidence Graph cover chart is explicitly illustrative. It is not run data.

Performance budgets in both PDFs are acceptance targets until a specific device, operating system, browser, renderer, quality profile, and commit have been measured.

Simulation and controlled data may qualify for bit-exact comparison under pinned conditions. GPU-rasterized evidence and cross-profile comparisons require declared tolerances.

## Relationship between the publications

*Three.js Evidence Graph v2.0* is the more recent general methodology. *The Hollow Meridian v1.0* shares its core control model but does not yet encode every v2 safeguard.

The RPG publication should be described as core-aligned or from the same evidence-graph lineage. It should not be described as a completed v2 reference implementation or as v2-conformance certified.

## Technical currency

The publications use Three.js r185 as their pinned baseline. Future Three.js releases may change APIs, renderer behavior, TSL capabilities, browser compatibility, and performance characteristics. A working implementation should pin exact dependency versions and re-run the renderer and compatibility gates before making current claims.

## Accessibility

The designed PDFs are untagged. The multilingual Markdown repository guides and expanded game guides provide a more accessible entry point, but they are explanatory companions rather than full text-equivalent editions of all 145 PDF pages.

## Artwork interpretation

The README and game-guide hero images are original concept artwork. They communicate the control model, authored route, material language, and intended boss readability. They are not gameplay screenshots, renderer captures, performance evidence, or proof that a playable build exists.

## Security review

The release files were checked for exposed credentials, unsafe URL schemes,
unexpected executable file modes, PDF active content and attachments, and
JPEG metadata or appended payloads. No credential or executable-content issue
was found. This structural review does not constitute steganalysis and cannot
guarantee the future safety of externally linked websites.

## Future evidence threshold

An empirical release should include, at minimum:

1. a runnable repository at one accepted commit;
2. declared authority documents and quality gates;
3. validated task, defect, and run schemas;
4. deterministic replay evidence under declared conditions;
5. declared-tolerance raster comparisons;
6. frame-time distributions on named devices;
7. provenance, bundle, and network audits;
8. critic calibration records;
9. a complete cost ledger;
10. one successful repair and one verified rollback;
11. two clean regression cycles;
12. an evidence index that binds every claim to an artifact.
