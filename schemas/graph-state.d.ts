/**
 * Normative Evidence Graph v2.0 TypeScript State & Cross-Publication Node Mapping
 * Reconciles Three.js Evidence Graph Operational Manual v2.0 (pp. 11-12)
 * and The Hollow Meridian Full Production Prompt v1.0 (p. 14 & p. 79).
 */

export type CanonicalNodeId =
  | "N00_BRIEF"                    // EG p.11: 01 BRIEF_COMPILE               | HM p.14: BRIEF + CONSTITUTION
  | "N01_CONTRACTS"                // EG p.11: 02 CONSTITUTION_AUDIT          | HM p.14: PRODUCT + ART FREEZE
  | "N02_SCAFFOLD"                 // EG p.11: 03 ARCHITECTURE_DECISION       | HM p.14: RENDERER PROOF
  | "N03_ASSET_COMPILER"           // EG p.11: 04 ART+GAMEPLAY_BIBLE_FREEZE   | HM p.14: PLAN + FOUNDATION
  | "N04_WORLD_GRAPH"              // EG p.11: 05 MILESTONE_PLAN              | HM p.14: FIXED SIM + QA
  | "N05_RENDER_PIPELINE"          // EG p.11: 06B PROCEDURAL + RENDER + AUDIO| HM p.14: PARALLEL WORKERS (Render/Art)
  | "N06A_GAMEPLAY_COMBAT"         // EG p.11: 06A GAMEPLAY + CAMERA WORKERS  | HM p.14: PARALLEL WORKERS (Combat/AI)
  | "N06B_AUDIO_SYNTH"             // EG p.11: 06B PROCEDURAL + RENDER + AUDIO| HM p.14: PARALLEL WORKERS (Audio/FX)
  | "N07_UI_HUD_A11Y"              // EG p.11: 07 INTEGRATION                 | HM p.14: INTEGRATION
  | "N08_TELEMETRY_HARNESS"        // EG p.11: 08 STATIC_VERIFICATION         | HM p.14: STATIC + REPLAY
  | "N09_REPLAY_RUNNER"            // EG p.11: 09 DETERMINISTIC_REPLAY        | HM p.14: CAPTURE
  | "N10_PERF_GATE"                // EG p.11: 10 EVIDENCE_CAPTURE            | HM p.14: READ-ONLY CRITICS
  | "N11_VISUAL_AUDIO_CRITIC"      // EG p.11: 11 INDEPENDENT_CRITICISM       | HM p.14: EVIDENCE REDUCER
  | "N12_PROVENANCE_AUDIT"         // EG p.11: 12 EVIDENCE_REDUCTION          | HM p.14: ACCEPT / REPAIR / ROLLBACK
  | "N13_REPAIR_ROUTER"            // EG p.11: 13 DECIDE / 14 CROSS-BROWSER   | HM p.14: BROWSER + PROVENANCE AUDIT / TWO CLEAN CYCLES
  | "N14_RELEASE_CANDIDATE";       // EG p.11: 15 RELEASE_CANDIDATE           | HM p.14: RELEASE CANDIDATE

export type DeterminismRegime = "A-PinnedBrowser" | "B-CrossPlatform";

export type RelicId = "none" | "brass_vow" | "ash_thread" | "vacant_name";

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
