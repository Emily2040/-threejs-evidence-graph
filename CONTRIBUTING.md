# Contributing

Thank you for helping improve this publication.

## Good contribution types

- Factual corrections with an exact PDF title and page number
- Broken or outdated source links
- Translation corrections with the source English sentence
- Accessibility improvements to the repository documentation
- Reproducible implementation reports with environment and commit details
- Machine-readable schemas, validators, and evidence tooling that preserve the published authority model

## Before opening a pull request

1. Keep the scope narrow.
2. Explain the observed defect.
3. Cite the affected file, heading, page, or line.
4. Describe why the proposed change is more accurate.
5. Preserve publication titles, game proper nouns, schema keys, commands, paths, and code identifiers.
6. Do not convert target values into claims of measured performance.
7. Do not describe *The Hollow Meridian v1.0* as fully compliant with Evidence Graph v2.0.

## Translation corrections

Include:

- language;
- current translated sentence;
- normative English sentence;
- proposed translation;
- reason for the change;
- any related terminology that must be updated for consistency.

## Implementation reports

An implementation report should identify:

- repository and commit;
- Three.js version;
- operating system, browser, GPU, and driver;
- renderer and quality profile;
- target device class;
- deterministic replay conditions;
- performance distribution;
- evidence paths;
- known limitations;
- failed gates;
- model-call cost ledger when agents were used.

Screenshots without a manifest are useful illustrations, but they are not sufficient evidence for a release claim.

## Publication integrity

Do not replace the PDFs silently. Any PDF revision must:

- increment its document version;
- add a changelog entry;
- update `CITATION.cff`;
- update `SHA256SUMS.txt`;
- describe the changed claims;
- preserve the previous release through GitHub Releases.
