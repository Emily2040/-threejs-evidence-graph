# Translation Policy

## Normative language

English is the normative language for this repository and its two PDF publications.

The Simplified Chinese, Japanese, and Korean README files translate the explanatory publication guide. Each language also has an expanded *The Hollow Meridian* companion guide that explains the world premise, authored route, player loop, combat, puzzle, relic, save, boss, procedural-media, accessibility, and evidence contracts.

These localized guides do not replace the English PDFs and are not full translations of all 145 PDF pages.

## Localized surfaces

| Surface | English | Simplified Chinese | Japanese | Korean |
|---|---:|---:|---:|---:|
| Repository publication guide | Yes | Yes | Yes | Yes |
| Expanded Hollow Meridian game guide | Yes | Yes | Yes | Yes |
| Technical glossary | Yes | Yes | Yes | Yes |
| Evidence Graph PDF | Yes | No | No | No |
| Hollow Meridian PDF | Yes | No | No | No |

The localized Markdown files are editorial translations marked `unreviewed` until an independent native-language technical review is recorded. That status describes review coverage, not completeness of the translated sections.

## Content that remains in English

The following items remain unchanged in every language:

- publication titles;
- game proper nouns;
- filenames and paths;
- commands and code;
- schema keys and enum values;
- graph-node identifiers;
- gate and defect identifiers;
- API and product names;
- URLs and citation metadata.

Localized explanations may follow a canonical term when needed.

For game-specific explanations, introduce a canonical term once and then use the most natural local expression consistently. Do not translate away filenames, identifiers, diagnostic commands, or values that readers must locate in the English PDF or a future repository.

## Translation priorities

Translations should preserve:

1. the difference between a specification and a completed implementation;
2. the difference between target budgets and measured results;
3. the difference between bit-exact evidence and tolerance-based evidence;
4. the authority separation between builders, critics, auditors, and the human director;
5. the compatibility gap between Evidence Graph v2.0 and Hollow Meridian v1.0;
6. the precise scope of the no-downloaded-assets rule;
7. all limitations and non-goals.

Expanded game-guide translations should also preserve:

8. the ten-beat authored route and its order;
9. the difference between procedural construction and authored dramatic structure;
10. the combat lessons assigned to each enemy;
11. the two-phase boss transition and its fairness constraints;
12. the difference between a meaningful relic choice and feature-volume progression;
13. the save-state boundary between persistent decisions and transient presentation;
14. the distinction between concept artwork and captured gameplay evidence.

## Language review checklist

Reviewers should check:

1. natural terminology for professional game-development readers;
2. consistent treatment of canonical English proper nouns;
3. preserved quantities, timings, version numbers, and exclusions;
4. explicit non-implementation and non-benchmark caveats;
5. image captions that identify concept artwork without presenting it as a screenshot;
6. links between the four language editions;
7. parity of headings, tables, warnings, and practical-use steps;
8. no accidental broadening of scope or quality claims.

## Resolving discrepancies

If a translation conflicts with the English edition:

1. treat the English edition as authoritative;
2. identify the affected heading and sentence;
3. propose a corrected translation without changing canonical identifiers;
4. record terminology changes consistently across the full language edition.

Use the [multilingual technical glossary](GLOSSARY.md) when reviewing terminology.
