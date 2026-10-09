# Specialist Agent Card: `procedural_audio` (The Glass Ossuary)

- **Canonical Node**: `N06B_AUDIO_SYNTH` (`06B PROCEDURAL + RENDER + AUDIO`)
- **Allowed Paths**: `src/audio/`, `tests/audio/`
- **Forbidden Paths**: `src/render/`, `src/forensics/`, `src/ui/`, `schemas/`
- **Core Responsibilities**:
  1. Synthesize all hydrophone sub-bass drones, wax-cylinder formant vocalizations, glass harmonic chimes, and footsteps via deterministic `OfflineAudioContext` graphs with zero external `.wav`/`.mp3`/`.ogg` files.
  2. Enforce EBU R128 loudness (`-16.0 LUFS +- 1.0 LU`, true peak `<= -1.0 dBTP`) and 16-bit PCM quantized `sha256` stem verification under Regime A.
