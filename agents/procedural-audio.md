# Specialist Agent Card: `procedural_audio`

- **Canonical Node**: `N06B_AUDIO_SYNTH` (`06B PROCEDURAL + RENDER + AUDIO`)
- **Allowed Paths**: `src/audio/`, `tests/audio/`
- **Forbidden Paths**: `src/combat/`, `src/render/`, `src/ui/`, `schemas/`
- **Core Responsibilities**:
  1. Synthesize all combat cues, ambient room drones, `Mnemonic Keeper` voice tones, and boss phase stems in code via Web Audio API (`AudioContext` / `OfflineAudioContext`) with zero downloaded audio files.
  2. Enforce `-16 LUFS +/- 2` integrated loudness and `-1.0 dBTP` true-peak ceiling.
  3. Quantize `OfflineAudioContext` renders to signed 16-bit PCM with a 2-LSB deadband (`Math.round(s * 8191)`) before computing `audio_hash` in `Regime A`.
