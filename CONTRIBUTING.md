# Contributing

Thank you for helping improve this publication.

## Contribution license

Unless explicitly agreed otherwise in writing, contributions submitted to this
repository are provided under the same [MIT License](LICENSE) that covers the
repository. Contributors must have the right to submit their work and must not
include third-party material that is incompatible with that license.

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

For a native-language technical review, also confirm:

- every English heading and warning has a localized counterpart;
- route order, quantities, timings, exclusions, and version relationships are unchanged;
- concept artwork is not described as captured gameplay;
- the guide does not imply that the English PDF has been fully translated;
- generic prose reads naturally in the target language;
- canonical proper nouns, filenames, commands, schemas, identifiers, and paths remain traceable;
- terminology agrees with `docs/GLOSSARY.md`.

After a complete review, propose the exact translation-status change and identify the reviewer, language, files, review date, and source version. Do not remove the `unreviewed` marker without a recorded independent review.

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

Do not replace published binary files silently. Any PDF or JPEG revision must
update `SHA256SUMS.txt`, the release manifest, and the changelog. A PDF
revision must also:

- increment its document version;
- add a changelog entry;
- update `CITATION.cff`;
- describe the changed claims;
- preserve the previous release through GitHub Releases.
