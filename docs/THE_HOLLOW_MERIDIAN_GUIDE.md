# The Hollow Meridian: Explanatory Game Guide

[English](THE_HOLLOW_MERIDIAN_GUIDE.md) | [简体中文](THE_HOLLOW_MERIDIAN_GUIDE.zh-CN.md) | [日本語](THE_HOLLOW_MERIDIAN_GUIDE.ja.md) | [한국어](THE_HOLLOW_MERIDIAN_GUIDE.ko.md)

![The authored route through the ruined observatory of The Hollow Meridian](../assets/hollow-meridian-world-hero.jpg)

*Concept artwork for the publication. Not a gameplay capture or implementation evidence.*

> **Guide status**
>
> This is a reader-oriented companion to *The Hollow Meridian RPG Full Prompt v1.0*. It explains the intended game, production system, and limitations. It is not a playable build, a translation of the complete 81-page PDF, or evidence that the target experience has been implemented.

## What the publication is

*The Hollow Meridian* is both a compact game design contract and a multi-agent production prompt. It specifies one third-person dark-fantasy action RPG vertical slice for desktop browsers using Three.js. The visible and audible game content must be generated from repository-controlled code, explicit parameters, and named seeds. Downloaded final models, textures, images, fonts, animation clips, prerecorded audio, and asset packs are outside the contract.

The publication fixes the product before implementation begins:

- a first playthrough of approximately 10 to 14 minutes;
- one safe hub and one authored route through five principal spaces;
- one quest, one spatial puzzle, and three enemy archetypes;
- one meaningful choice between three relics;
- one two-phase boss and two ending outcomes;
- one local save slot with checkpoint, death, recovery, victory, and return-to-hub behavior.

The goal is depth within a narrow route. Open-world expansion, crafting, shops, random loot, companions, multiplayer, mounts, character creation, and additional bosses are deliberately deferred.

## World and player fantasy

The setting is a ruined observatory that once preserved the true names of vanished cities. Architecture functions as both worldbuilding and navigation. Radial ribs, concentric rings, meridian rails, archive cells, index arms, bell frames, ceramic masks, and ash channels establish the visual grammar.

The player controls the **Cartographer**, a faceless adult warden wearing layered bone-ceramic and tarnished-brass armor. The Cartographer carries a segmented poleblade and an Echo Lantern. The fantasy is not unrestricted power. It is controlled orientation: reading space, learning timing, recovering names, and deciding whether the observatory should bind or release what it has stored.

The main material families have distinct roles:

| Material | Intended visual behavior |
|---|---|
| Dark basalt | Broad roughness, strong mass, pale dust on upward faces |
| Tarnished brass | Structural rhythm, localized verdigris, polished contact points |
| Bone ceramic | Masks and armor, seeded cracking, warm exposed edges |
| Ember glass | Bounded transparency around a separate emissive core |
| Name-light | Generated line glyphs and pale cyan-white guidance, not a downloaded font |

Stable name-light is pale cyan-white. Unstable bell energy is amber-white. Deep red is reserved for damage and critical warnings. Saturated purple is not the default magic language.

## The ten-beat player journey

The route is authored even when its geometry and materials are procedurally constructed.

| Beat | Space and purpose | Player-facing result |
|---:|---|---|
| 1 | **Ash Court arrival** | Learn movement, camera, interaction, the Mnemonic Keeper, and the resting checkpoint |
| 2 | **Quest acceptance** | Learn that two orientation seals are required and open the route |
| 3 | **Orrery Bridge tutorial** | Meet the Ashbound Skirmisher and learn lock-on, dodge, guard, parry, and the first consumable |
| 4 | **Archive Nave** | Read a vertical reveal, manage Lantern Wraith pressure, and find optional lore |
| 5 | **Meridian alignment** | Solve a deterministic three-ring spatial puzzle and obtain the North Seal |
| 6 | **Bell Foundry** | Break the Bell Sentinel's guard and obtain the Depth Seal |
| 7 | **Shrine choice** | Select one of three relics that changes the combat model |
| 8 | **Chamber opening** | Trigger a short, skippable generated sequence and reveal the boss |
| 9 | **Unnamed Bell** | Complete a two-phase encounter with readable hazards and different spatial rules |
| 10 | **Bind or release** | Choose one of two outcomes, save the consequence, and return to the hub |

Procedural systems may build architecture, materials, signs, particles, and bounded variation. They may not decide the dramatic route, encounter order, focal hierarchy, reveal timing, or narrative purpose of a space.

## Moment-to-moment play

The core loop is:

1. orient through architecture and light;
2. read an encounter or interaction;
3. commit to movement, defense, or attack;
4. spend or recover stamina;
5. earn Resonance through effective play;
6. use Echo Brand or a relic-modified option;
7. collect a seal, resolve a puzzle, or advance quest state;
8. reach a checkpoint and preserve the meaningful state;
9. revisit the route under changed combat or narrative conditions.

The specification rejects click-to-damage combat, decorative inventory statistics, quests that do not alter world state, bosses that are enlarged standard enemies, and procedural randomness without a grammar.

## Combat model

The Cartographer has a limited, readable action set:

- camera-relative movement and combat strafing;
- a light attack chain;
- a charged heavy attack;
- dodge with committed timing;
- guard and selected parry windows;
- stamina as the primary action constraint;
- Resonance earned through parries, damage, and defined relic effects;
- Echo Brand as a targeted Resonance-spending action.

Combat values belong in centralized typed data and require tests. Hitboxes and hurtboxes must remain visibly aligned with procedural rig joints and weapon segments. Input buffering is allowed, but impossible cancellation is not. Camera collision, lock-on, narrow spaces, multiple enemies, and boss framing each require diagnostic evidence.

### Enemy lessons

Each enemy teaches a different rule:

- **Ashbound Skirmisher:** basic spacing, readable melee timing, dodge, and parry.
- **Lantern Wraith:** ranged pressure, charge recognition, lateral movement, and controlled target selection.
- **Bell Sentinel:** guard pressure, heavy attacks, poise, and preparation for the boss.

The encounter director controls attack opportunities so that multiple enemies do not create unreadable simultaneous pressure.

## The Bell Without a Name

![The Bell Without a Name entering its second phase inside the Meridian Chamber](../assets/hollow-meridian-boss-hero.jpg)

*Concept artwork for the publication. Not a gameplay capture or implementation evidence.*

The boss is a separate system, not a larger Bell Sentinel. Its approximately 4.5-meter construction combines an asymmetric ring frame, a suspended dark bell core, three articulated striking arms, trailing index chains, and a blank ceramic face plate that cracks between phases.

Phase one teaches four readable attacks: a broad meridian sweep, a vertical tolling strike followed by an expanding floor ring, a narrow chain thrust, and a charged resonance pulse. Selected attacks can be parried, and disciplined heavy attacks or parries can break poise.

At 55 percent health, attack selection pauses for a protected transition. The face plate cracks, the bell core detaches into a hovering orbit, cold name-light shifts toward unstable amber-white, and a rotating meridian hazard introduces visible safe sectors. Phase two changes space and cadence without discarding the combat rules the player has learned.

The boss contract forbids unavoidable recorded damage, unreadable attack combinations, hidden hazard sectors, and a final phase that removes every recovery opportunity.

## RPG state, relics, and consequences

RPG depth comes from a small number of state changes that affect play:

- quest acceptance opens the route;
- each recovered seal changes progression state;
- one of three relics modifies a real combat decision;
- consumables have bounded roles;
- checkpoint and death recovery preserve declared state;
- the final bind-or-release decision changes the visual and textual outcome;
- completion state persists when the player returns to the hub.

Progression is one meaningful relic decision, not a level grind. The save schema is versioned and stores quest state, seals, the selected relic, consumables, checkpoint identity, completion, ending choice, settings, and remapped controls. Temporary particles, enemy animation phases, and incidental combat state are not persisted unless checkpoint design requires them.

## Source-generated art, animation, and audio

The no-downloaded-assets rule applies to final visible and audible media. It does not prohibit audited development dependencies, browser APIs, build tools, test tools, or profilers.

Procedural generation is treated as compilation. A generator needs:

- a bounded grammar and parameter ranges;
- named seeds and deterministic output where claimed;
- rejection tests for overlap, route obstruction, repetition, and invalid collision;
- level-of-detail, culling, batching, pooling, and cost controls;
- provenance records and diagnostic views.

Characters use procedural rigs, typed keyframes, deterministic pose curves, or generated animation clips. Procedural motion must support authored posing and combat timing rather than replace them with continuous wobble.

Audio is synthesized with Web Audio primitives and spatial nodes. The target palette includes bell partials, controlled noise, envelopes, filtered impacts, route ambience, combat feedback, puzzle resolution, boss-phase mix changes, and distinct ending states. Important audio information requires a visual equivalent.

## Interface, controls, and accessibility

The game contract includes keyboard, mouse, and gamepad support. Dialogue and menu input must not trigger combat actions. Pause stops authoritative simulation while allowing non-authoritative menu presentation to continue.

Accessibility targets include:

- remappable keyboard and gamepad controls;
- reduced-motion options for menus and ending effects;
- high-contrast interaction and route markers;
- readable telegraphs that do not depend on color alone;
- separate audio sliders;
- visual equivalents for important sound cues;
- stable camera behavior with reduced shake during precision combat.

These are engineering requirements in the specification. They are not evidence of formal WCAG conformance.

## How the production graph uses the game contract

The prompt distributes work across bounded roles for architecture, gameplay and combat, procedural world construction, AI and boss behavior, RPG and UI systems, audio and effects, integration, QA and performance, visual criticism, and provenance auditing.

Builders do not approve their own output. Deterministic code controls graph transitions. Read-only critics evaluate captured artifacts. A provenance auditor can block release. Every delegated task identifies permitted files, forbidden files, invariants, acceptance commands, required evidence, budgets, retry limits, and rollback conditions.

The evidence surface includes:

- fixed-tick simulation and replay capture;
- periodic and final state hashes;
- stable diagnostic URLs and camera states;
- screenshots and traces tied to one commit;
- combat, puzzle, boss, save, ending, accessibility, and provenance evidence;
- frame-time distributions and renderer statistics;
- clean-checkout reproduction and two clean regression cycles.

Visual output across GPUs and browsers is not assumed to be bit-identical. Controlled simulation state may use exact comparison. Rasterized evidence needs declared perceptual tolerances.

## How to use the publication

1. Read the deployment declaration, game contract, experience pillars, anti-slop contract, and authored route.
2. Review the authority graph and repository documents that must exist before delegation.
3. Read the systems section to understand the minimum combat, RPG, world, audio, interface, and accessibility contracts.
4. Adopt the schemas before dispatching specialist tasks.
5. Paste the full orchestrator prompt into a capable repository-local coding agent.
6. Store specialist cards under the repository's agent directory.
7. Implement validation, graph state, evidence capture, and rollback before increasing content.
8. Begin with a smaller proof slice if the full 10-to-14-minute route exceeds the available evidence or compute budget.
9. Do not announce completion until the release predicates pass against one identified commit.

## What still needs to be built

This publication describes the target and the control system. The repository does not yet include:

- a playable Three.js implementation;
- executable task, defect, graph, and release validators;
- the deterministic replay and capture harness;
- generated source assets and runtime code;
- measured performance results;
- an accepted `run-0001` evidence package;
- a documented repair and verified rollback;
- a release candidate that passes the declared gates.

The accurate claim is that *The Hollow Meridian* is an applied RPG specification from the Evidence Graph lineage. It is not a finished game or a proof that the proposed production method has already converged.

## Language and terminology

English remains normative for the PDF, commands, filenames, schemas, identifiers, and game proper nouns. The localized guides explain the game in Simplified Chinese, Japanese, and Korean while keeping canonical terms traceable.

If a localized guide differs from the English publication, use the English edition for technical interpretation and report the discrepancy. See the [Translation Policy](TRANSLATION_POLICY.md) and [Multilingual Technical Glossary](GLOSSARY.md).
