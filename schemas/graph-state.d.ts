/**
 * Normative Evidence Graph v2.0 TypeScript State & Cross-Publication Node Mapping
 * Shared across Three.js Evidence Graph Operational Manual v2.0 (64 pp),
 * The Hollow Meridian v1.0 (81 pp), The Glass Ossuary v1.0 (36 pp),
 * and Perihelion Breach v1.0 (36 pp).
 */

export type CanonicalNodeId =
  | "N00_BRIEF"                    // EG p.11: 01 BRIEF_COMPILE               | Slice: BRIEF + CONSTITUTION
  | "N01_CONTRACTS"                // EG p.11: 02 CONSTITUTION_AUDIT          | Slice: PRODUCT + ART FREEZE
  | "N02_SCAFFOLD"                 // EG p.11: 03 ARCHITECTURE_DECISION       | Slice: RENDERER PROOF
  | "N03_ASSET_COMPILER"           // EG p.11: 04 ART+GAMEPLAY_BIBLE_FREEZE   | Slice: PLAN + FOUNDATION
  | "N04_WORLD_GRAPH"              // EG p.11: 05 MILESTONE_PLAN              | Slice: FIXED SIM + QA
  | "N05_RENDER_PIPELINE"          // EG p.11: 06B PROCEDURAL + RENDER + AUDIO| Slice: PARALLEL WORKERS (Render/Art)
  | "N06A_GAMEPLAY_COMBAT"         // EG p.11: 06A GAMEPLAY + CAMERA WORKERS  | Slice: PARALLEL WORKERS (Combat/Forensics/Ballistics)
  | "N06B_AUDIO_SYNTH"             // EG p.11: 06B PROCEDURAL + RENDER + AUDIO| Slice: PARALLEL WORKERS (Audio/FX)
  | "N07_UI_HUD_A11Y"              // EG p.11: 07 INTEGRATION                 | Slice: INTEGRATION
  | "N08_TELEMETRY_HARNESS"        // EG p.11: 08 STATIC_VERIFICATION         | Slice: STATIC + REPLAY
  | "N09_REPLAY_RUNNER"            // EG p.11: 09 DETERMINISTIC_REPLAY        | Slice: CAPTURE
  | "N10_PERF_GATE"                // EG p.11: 10 EVIDENCE_CAPTURE            | Slice: READ-ONLY CRITICS
  | "N11_VISUAL_AUDIO_CRITIC"      // EG p.11: 11 INDEPENDENT_CRITICISM       | Slice: EVIDENCE REDUCER
  | "N12_PROVENANCE_AUDIT"         // EG p.11: 12 EVIDENCE_REDUCTION          | Slice: ACCEPT / REPAIR / ROLLBACK
  | "N13_REPAIR_ROUTER"            // EG p.11: 13 DECIDE / 14 CROSS-BROWSER   | Slice: BROWSER + PROVENANCE AUDIT / TWO CLEAN CYCLES
  | "N14_RELEASE_CANDIDATE";       // EG p.11: 15 RELEASE_CANDIDATE           | Slice: RELEASE CANDIDATE

export type DeterminismRegime = "A-PinnedBrowser" | "B-CrossPlatform";

export type HollowMeridianRelicId = "brass_vow" | "ash_thread" | "vacant_name";
export type GlassOssuaryHypothesisId = "lens_sabotage" | "tidal_quarantine" | "acoustic_calling";
export type PerihelionBreachRigCoreId = "recoil_gyro" | "thermal_siphon" | "grapple_overdrive";

export type RelicId =
  | "none"
  | HollowMeridianRelicId
  | GlassOssuaryHypothesisId
  | PerihelionBreachRigCoreId;

export interface NodeExecutionRecord {
  node: CanonicalNodeId;
  status: "pending" | "running" | "passed" | "failed" | "repaired" | "rolled_back";
  packet_id: string;
  started_at?: string;
  completed_at?: string;
  attempt: number;
  artifacts: string[];
  open_defects: string[];
}

export interface GraphState {
  run_id: string;
  git_commit: string;
  accepted_baseline_commit: string;
  three_version: "0.185.0";
  determinism_regime: DeterminismRegime;
  current_node: CanonicalNodeId;
  active_relic: RelicId;
  repair_iteration: number;
  max_repair_iterations: number;
  nodes: Record<CanonicalNodeId, NodeExecutionRecord>;
  cost_ledger: {
    total_tokens: number;
    wall_clock_seconds: number;
    subagent_invocations: number;
    repair_cycles: number;
  };
  human_signoff: {
    authority: string;
    status: "approved" | "pending" | "rejected";
    signed_at?: string;
  };
}
