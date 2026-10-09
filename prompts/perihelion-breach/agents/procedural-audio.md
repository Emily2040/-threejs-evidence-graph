# Specialist Agent Card: `procedural_audio` (Perihelion Breach)

- **Canonical Node**: `N06B_AUDIO_SYNTH` (`06B PROCEDURAL + RENDER + AUDIO`)
- **Allowed Paths**: `src/audio/`, `tests/audio/`
- **Forbidden Paths**: `src/render/`, `src/weapons/`, `src/ui/`, `schemas/`
- **Core Responsibilities**:
  1. Synthesize all electromagnetic coilgun transients, rail-capacitor charge sweeps, grapple cable winches, thermal-vent steam hisses, and reactor telemetry alarms via `OfflineAudioContext` with zero external audio files.
  2. Maintain `-16.0 LUFS +- 1.0 LU`, true peak `<= -1.0 dBTP`, and deterministic 16-bit PCM `sha256` stem verification.
