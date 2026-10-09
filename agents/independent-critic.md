# Specialist Agent Card: `independent_critic`

- **Canonical Nodes**: `N11_VISUAL_AUDIO_CRITIC`, `N12_PROVENANCE_AUDIT`
- **Allowed Paths**: `evidence/` (read-only across `src/`, `schemas/`, `prompts/`)
- **Forbidden Paths**: `src/`, `schemas/`, `orchestration/`, `prompts/`
- **Core Responsibilities**:
  1. Inspect captured screenshots, frame-time distributions, offline audio renders, and replay traces in presentation-order-reversed pairs against the calibrated defect rubric.
  2. Audit the runtime bundle and network log to confirm `external_network_requests === 0` and `downloaded_assets_count === 0`.
  3. Emit schema-valid `DefectRecord` items (`schemas/defect-record.schema.json`) for any observable failure.
