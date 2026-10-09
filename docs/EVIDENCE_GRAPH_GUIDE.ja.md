<!-- source_version: 2026.07.4; translation_status: reviewed; language: ja -->
# Three.js Evidence Graph：運用マニュアル v2.0 コンパニオンガイド

[English](EVIDENCE_GRAPH_GUIDE.md) | [简体中文](EVIDENCE_GRAPH_GUIDE.zh-CN.md) | [日本語](EVIDENCE_GRAPH_GUIDE.ja.md) | [한국어](EVIDENCE_GRAPH_GUIDE.ko.md)

![プロダクト契約から範囲を限定した専門作業、エビデンス取得、リリース判定へ分岐するコントロールプレーン](../assets/evidence-graph-control-hero.jpg)

## 1. 目的と中核テーゼ

*Three.js Evidence Graph: Operational Manual v2.0*（[`publications/threejs-evidence-graph-operational-manual-v2.0-en.pdf`](../publications/threejs-evidence-graph-operational-manual-v2.0-en.pdf)、全64ページ、`416,827` バイト、SHA-256 `d3830d411a61c52c92d6d9f4454d317a5e5bb7dbc3660824e7d24b7a959eb6cd`）は、外部の実行時アセットをダウンロードせずに、範囲を限定したソース生成型の Three.js ブラウザゲーム・バーティカルスライス（vertical slice）を構築するための、リポジトリ内完結型・エビデンスグラフ（Evidence Graph）駆動マルチエージェント制作システムを定義しています。

1つの会話に構築、評価、リリース承認の権限を集中させるのではなく、エビデンスグラフ（Evidence Graph）は以下の4層に権限を分離します。

- **決定論的コントロールプレーン（`orchestrator`）**：グラフ状態（`schemas/graph-state.d.ts`）を管理し、作業範囲を限定したタスクパケット（`schemas/task-packet.schema.json`）を配布し、計算資源と再試行の予算を強制し、修復が収束しない場合は受け入れ済みベースライン（`accepted_baseline_commit`）へ自動ロールバックします。
- **作業範囲を限定したスペシャリスト構築者（6役割）**：`combat_gameplay`、`world_quest`、`procedural_art_vfx`、`procedural_audio`、`ui_hud_accessibility`、`qa_perf_playwright`。各スペシャリストは許可された `allowed_paths` のみに書き込み、引き渡し前に機械的な受け入れ判定コマンド（acceptance command）に合格する必要があります。
- **校正された読み取り専用評価者（`independent_critic`）**：ソースコードへの書き込み権限を持たず、取得済みの映像フレーム、オフライン音声レンダリング、決定論的リプレイのテレメトリ、および外部アセットゼロの生成由来の追跡情報（provenance）を提示順反転ペアで評価します。
- **2つのエビデンス制度（Evidence Regimes）**：
  - **制度 A（`A-PinnedBrowser`）**：固定された Chromium + GPU/SwiftShader コンテナ内で、60 Hz 整数ティックのシミュレーション状態（`state_hash`）、16ビット PCM 量子化済み `OfflineAudioContext` バッファ（`audio_hash`）、および `1e-5` 量子化済みプロシージャルジオメトリ（`geometry_hash`）のビット単位 SHA-256 一致を検証します。
  - **制度 B（`B-CrossPlatform`）**：異なるハードウェアやブラウザ環境（`webgpu` 主経路および `webgl2-fallback`）にわたり、不変条件と宣言済み許容範囲（declared tolerance）を検証します。

---

## 2. 64ページ運用マニュアルの8章構成と付録

| 章 | ページ | 対象範囲と規範的成果物 |
| :--- | :--- | :--- |
| **Delta v1 -> v2 欠陥台帳** | p. 04 | プロンプトのみに依存した v1 ワークフローの10個の構造的欠陥（`DOC-001` から `DOC-010`）と、それに対応する v2.0 の制御機構を対照します。 |
| **00. 診断（Diagnosis）** | pp. 05-09 | 単一会話による大規模 3D ゲーム生成が破綻する理由（文脈ドリフト、シェーダーコンパイル停止、証拠なき自己肯定、未校正の視覚評価）を分析します。 |
| **01. コントロールプレーン（Control plane）** | pp. 10-17 | 15ノードの有向巡回エビデンスグラフ（`N00_BRIEF` から `N14_RELEASE_CANDIDATE`）、権限階層、書き込み所有権の分離、リポジトリ構成を定義します。 |
| **02. Three.js アーキテクチャ（Three.js architecture）** | pp. 18-29 | Three.js `r185`（`0.185.0`）、`THREE.WebGPURenderer` と `{ forceWebGL: true }` フォールバック、TSL ノードマテリアル、`compileAsync` + `postProcessing.renderAsync()` 事前コンパイル、およびフレーム時間予算（`P50 <= 8.3 ms`、`P95 <= 16.6 ms`、`P99 <= 22.0 ms`）を規定します。 |
| **03. アセットフリー制作（Asset-free production）** | pp. 30-36 | プロシージャル生成をコンパイルとして扱い、シード固定 PRNG、プロシージャル生成文法（procedural grammar）、TSL マテリアル、Web Audio オフライン合成（`-16 LUFS +/- 2`、`-1.0 dBTP`）を定義します。 |
| **04. エビデンスと収束（Evidence + convergence）** | pp. 37-45 | Playwright テレメトリ取得（`window.__rpgReady`、`window.__rpgQA`）、制度 A/B の決定論ゲート、評価者の校正（critic calibration）、および `DefectRecord` 根本原因修復ループ（最大3回、超過時はロールバック）を規定します。 |
| **05. 運用と計算資源経済（Operations）** | pp. 46-48 | モデル階層のルーティング、実行単位のコスト台帳（`cost_ledger`）、サプライチェーン来歴監査、および指名された人間のディレクター（`human_signoff`）の権限を定義します。 |
| **06. プロンプト言語（Prompt language）** | pp. 49-52 | 4部構成のオーケストレーター・プロンプトとスペシャリスト委任テンプレートを提供します（[`prompts/evidence-graph/orchestrator.md`](../prompts/evidence-graph/orchestrator.md) に収録）。 |
| **07. 実装プログラム（Implementation program）** | pp. 53-57 | `N00_BRIEF` から `N14_RELEASE_CANDIDATE` までの段階的実装手順と v1 から v2 への移行チェックリストを示します。 |
| **付録 A-B および一次資料（Appendices A-B & Primary Sources）** | pp. 58-64 | 規範的 JSON Schema（[`schemas/`](../schemas/) にて Draft 2020-12 に更新済み）およびクリック可能な URI リンク注釈付き一次技術文献23件を収録しています。 |

---

## 3. 正準15ノード制作グラフ（`N00` から `N14`）

1. `N00_BRIEF`（`01 BRIEF_COMPILE`）：プロダクト要件、除外範囲、スライス目標時間の確定。
2. `N01_CONTRACTS`（`02 CONSTITUTION_AUDIT`）：JSON Schema（`task-packet`、`defect-record`、`run-manifest`）およびシード不変条件の凍結。
3. `N02_SCAFFOLD`（`03 ARCHITECTURE_DECISION`）：決定論的 60 Hz クロック、PRNG、および Three.js `r185` `WebGPURenderer` 起動基盤の構築。
4. `N03_ASSET_COMPILER`（`04 ART+GAMEPLAY_BIBLE_FREEZE`）：プロシージャル生成文法、パレット規則、TSL マテリアル契約の凍結。
5. `N04_WORLD_GRAPH`（`05 MILESTONE_PLAN`）：設計済みルート、衝突判定ボリューム、チェックポイント状態グラフの構築。
6. `N05_RENDER_PIPELINE`（`06B PROCEDURAL + RENDER + AUDIO` - 描画）：ライティング、`PMREMGenerator`、`InstancedMesh`/`BatchedMesh`、`THREE.PostProcessing` の構成。
7. `N06A_GAMEPLAY_COMBAT`（`06A GAMEPLAY + CAMERA WORKERS`）：整数ティック戦闘ステートマシン、敵、ボス段階移行、カメラ衝突処理の実装。
8. `N06B_AUDIO_SYNTH`（`06B PROCEDURAL + RENDER + AUDIO` - 音声）：プロシージャル Web Audio 合成および `OfflineAudioContext` ラウドネス/PCM ハッシュ検証の実装。
9. `N07_UI_HUD_A11Y`（`07 INTEGRATION`）：HUD、キー再割り当て、高コントラスト/視差効果低減モード、セーブスキーマの統合。
10. `N08_TELEMETRY_HARNESS`（`08 STATIC_VERIFICATION`）：静的検証の実行と `window.__rpgReady` / `window.__rpgQA` フックの配線。
11. `N09_REPLAY_RUNNER`（`09 DETERMINISTIC_REPLAY`）：決定論的リプレイの実行と `state_hash`、`audio_hash`、`geometry_hash` の記録。
12. `N10_PERF_GATE`（`10 EVIDENCE_CAPTURE`）：1920x1080 フレーム時間分布、ドローコール、ポリゴン数、GPU メモリの計測。
13. `N11_VISUAL_AUDIO_CRITIC`（`11 INDEPENDENT_CRITICISM`）：校正された読み取り専用評価者による視覚・音声・ゲームプレイ評価。
14. `N12_PROVENANCE_AUDIT`（`12 EVIDENCE_REDUCTION`）：実行時の外部ネットワーク要求ゼロおよびダウンロード済みメディアゼロの監査。
15. `N13_REPAIR_ROUTER`（`13 DECIDE` / `14 CROSS-BROWSER_RELEASE_AUDIT`）：`P0`-`P2` の `DefectRecord` を単一の書き込み所有者へルーティング（最大3回）、収束しない場合は `accepted_baseline_commit` へロールバック。
16. `N14_RELEASE_CANDIDATE`（`15 RELEASE_CANDIDATE`）：`cost_ledger` と `human_signoff` を含む検証済み `run-manifest.json` の出力。

---

## 4. スタンドアロン契約・プロンプト・検証フィクスチャ

- **規範的 JSON Schema（Draft 2020-12）および型定義**：[`schemas/task-packet.schema.json`](../schemas/task-packet.schema.json)、[`schemas/defect-record.schema.json`](../schemas/defect-record.schema.json)、[`schemas/run-manifest.schema.json`](../schemas/run-manifest.schema.json)、[`schemas/graph-state.d.ts`](../schemas/graph-state.d.ts)
- **コピー＆ペースト可能なオーケストレーター・プロンプト**：[`prompts/evidence-graph/orchestrator.md`](../prompts/evidence-graph/orchestrator.md)
- **ゴールデン検証フィクスチャ**：[`examples/run-0001/`](../examples/run-0001/)
- **技術正誤表および v2.0 整合仕様**：[`docs/TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md`](TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md)
