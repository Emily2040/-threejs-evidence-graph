<!-- source_version: 2026.07.5; translation_status: reviewed; language: zh-CN -->

# Three.js Evidence Graph：操作手册 v2.0 配套导读指南

[English](EVIDENCE_GRAPH_GUIDE.md) | [简体中文](EVIDENCE_GRAPH_GUIDE.zh-CN.md) | [日本語](EVIDENCE_GRAPH_GUIDE.ja.md) | [한국어](EVIDENCE_GRAPH_GUIDE.ko.md)

![从产品契约分支到有边界专家工作、独立证据捕获与发布关卡的控制平面](../assets/evidence-graph-control-hero.jpg)

## 1. 编写目的与核心命题

*Three.js Evidence Graph: Operational Manual v2.0*（[`publications/threejs-evidence-graph-operational-manual-v2.0-en.pdf`](../publications/threejs-evidence-graph-operational-manual-v2.0-en.pdf)，共 64 页，`416,827` 字节，SHA-256 `d3830d411a61c52c92d6d9f4454d317a5e5bb7dbc3660824e7d24b7a959eb6cd`）定义了一套位于仓库内部、由证据图（Evidence Graph）驱动的多智能体生产系统，用于在不下载任何外部运行时资产的前提下构建范围明确的 Three.js 浏览器游戏垂直切片（vertical slice）。

证据图（Evidence Graph）拒绝让单一对话同时充当构建者、评审者与发布审批方，而是将权限分离为四个层级：

- **确定性控制平面（`orchestrator`）**：管理图状态（`schemas/graph-state.d.ts`），分发边界明确的任务包（`schemas/task-packet.schema.json`），执行算力与重试预算，并在修复未收敛时自动回滚至已接受基线（`accepted_baseline_commit`）。
- **边界明确的专家构建者（6 类角色）**：`combat_gameplay`、`world_quest`、`procedural_art_vfx`、`procedural_audio`、`ui_hud_accessibility` 与 `qa_perf_playwright`。每位专家仅能写入其 `allowed_paths`，且在移交前必须通过机械验收命令。
- **经过校准的只读评审者（`independent_critic`）**：以无源码写入权限的只读身份，对捕获画面、离线渲染音频、确定性回放遥测及零外部资产来源可追溯性（provenance）进行正反双序盲审。
- **双重证据制度（Evidence Regimes）**：
  - **制度 A（`A-PinnedBrowser`）**：在固定 Chromium 与 GPU/SwiftShader 容器内，对 60 Hz 整数 tick 模拟状态（`state_hash`）、16 位 PCM 量化的 `OfflineAudioContext` 缓冲区（`audio_hash`）与 `1e-5` 量化的程序化几何体（`geometry_hash`）执行逐比特 SHA-256 校验。
  - **制度 B（`B-CrossPlatform`）**：在跨硬件与跨浏览器环境（`webgpu` 主路径与 `webgl2-fallback` 回退路径）下执行不变量与预先声明的容差校验。

---

## 2. 64 页操作手册的八节结构与附录

| 章节 | 页码 | 核心范围与规范交付物 |
| :--- | :--- | :--- |
| **Delta v1 -> v2 缺陷账本** | 第 04 页 | 列出纯提示词 v1 工作流的 10 项结构性缺陷（`DOC-001` 至 `DOC-010`）及其对应的 v2.0 架构控制措施。 |
| **00. 诊断（Diagnosis）** | 第 05-09 页 | 剖析单次对话生成大型 3D 游戏的常见失效模式（上下文漂移、着色器编译卡顿、无证据自评通过及未校准的视觉评审）。 |
| **01. 控制平面（Control plane）** | 第 10-17 页 | 定义 15 节点有向循环证据图（`N00_BRIEF` 至 `N14_RELEASE_CANDIDATE`）、权限层级、文件写入隔离与仓库目录结构。 |
| **02. Three.js 架构（Three.js architecture）** | 第 18-29 页 | 锁定 Three.js `r185`（`0.185.0`）、原生 `THREE.WebGPURenderer` 与 `{ forceWebGL: true }` 回退、TSL 节点材质、`compileAsync` + `postProcessing.renderAsync()` 预热及帧时间预算（`P50 <= 8.3 ms`、`P95 <= 16.6 ms`、`P99 <= 22.0 ms`）。 |
| **03. 零外部资产生产（Asset-free production）** | 第 30-36 页 | 将程序化生成视为编译：受控种子 PRNG、程序化生成语法（procedural grammar）、TSL 材质与 Web Audio 离线合成（`-16 LUFS +/- 2`、`-1.0 dBTP`）。 |
| **04. 证据与收敛（Evidence + convergence）** | 第 37-45 页 | 规定 Playwright 遥测捕获（`window.__rpgReady`、`window.__rpgQA`）、制度 A/B 确定性关卡、评审者校准（critic calibration）与 `DefectRecord` 根因修复循环（最多 3 次重试后自动回滚）。 |
| **05. 运维与算力经济（Operations）** | 第 46-48 页 | 定义模型分级路由、运行级成本账本（`cost_ledger`）、供应链来源可追溯性审计与具名人类主管（`human_signoff`）签核。 |
| **06. 提示词语言（Prompt language）** | 第 49-52 页 | 提供四部分编排器系统提示词与专家委派模板（独立文件位于 [`prompts/evidence-graph/orchestrator.md`](../prompts/evidence-graph/orchestrator.md)）。 |
| **07. 实施计划（Implementation program）** | 第 53-57 页 | 给出从 `N00_BRIEF` 到 `N14_RELEASE_CANDIDATE` 的逐步实施路线与 v1 至 v2 迁移检查清单。 |
| **附录 A-B 与原始文献（Appendices A-B & Primary Sources）** | 第 58-64 页 | 规范性 JSON Schema（在 [`schemas/`](../schemas/) 中已升级为 Draft 2020-12）以及带 23 个可点击 URI 链接注释的一手技术文献。 |

---

## 3. 规范化 15 节点生产图（`N00` 至 `N14`）

1. `N00_BRIEF`（`01 BRIEF_COMPILE`）：编译产品简报、范围排除项与垂直切片时长目标。
2. `N01_CONTRACTS`（`02 CONSTITUTION_AUDIT`）：冻结 JSON Schema（`task-packet`、`defect-record`、`run-manifest`）与种子不变量。
3. `N02_SCAFFOLD`（`03 ARCHITECTURE_DECISION`）：建立确定性 60 Hz 时钟、PRNG 与 Three.js `r185` `WebGPURenderer` 启动框架。
4. `N03_ASSET_COMPILER`（`04 ART+GAMEPLAY_BIBLE_FREEZE`）：冻结程序化几何语法、色板规则与 TSL 材质契约。
5. `N04_WORLD_GRAPH`（`05 MILESTONE_PLAN`）：构建经编排的空间路线、碰撞体积与检查点状态图。
6. `N05_RENDER_PIPELINE`（`06B PROCEDURAL + RENDER + AUDIO` - 渲染）：配置光照、`PMREMGenerator`、`InstancedMesh`/`BatchedMesh` 与 `THREE.PostProcessing`。
7. `N06A_GAMEPLAY_COMBAT`（`06A GAMEPLAY + CAMERA WORKERS`）：实现整数 tick 战斗状态机、敌人、首领阶段与镜头碰撞。
8. `N06B_AUDIO_SYNTH`（`06B PROCEDURAL + RENDER + AUDIO` - 音频）：实现程序化 Web Audio 合成与 `OfflineAudioContext` 响度/PCM 哈希校验。
9. `N07_UI_HUD_A11Y`（`07 INTEGRATION`）：集成 HUD、键位重映射、高对比度/减弱动态模式与版本化存档 schema。
10. `N08_TELEMETRY_HARNESS`（`08 STATIC_VERIFICATION`）：执行静态校验并挂载 `window.__rpgReady` / `window.__rpgQA` 诊断钩子。
11. `N09_REPLAY_RUNNER`（`09 DETERMINISTIC_REPLAY`）：运行确定性回放并记录 `state_hash`、`audio_hash` 与 `geometry_hash`。
12. `N10_PERF_GATE`（`10 EVIDENCE_CAPTURE`）：捕获 1920x1080 帧时间分布、绘制调用、三角形数量与显存占用。
13. `N11_VISUAL_AUDIO_CRITIC`（`11 INDEPENDENT_CRITICISM`）：由经过校准的只读评审者对捕获产物执行视觉、音频与玩法评审。
14. `N12_PROVENANCE_AUDIT`（`12 EVIDENCE_REDUCTION`）：验证运行时零外部网络请求与零下载媒体资产。
15. `N13_REPAIR_ROUTER`（`13 DECIDE` / `14 CROSS-BROWSER_RELEASE_AUDIT`）：将 `P0`-`P2` 级 `DefectRecord` 路由至唯一写入负责人（最多 3 轮修复），超限则回滚至 `accepted_baseline_commit`。
16. `N14_RELEASE_CANDIDATE`（`15 RELEASE_CANDIDATE`）：输出包含 `cost_ledger` 与 `human_signoff` 的 `run-manifest.json`。

---

## 4. 仓库独立契约与验证资源

- **规范性 JSON Schema（Draft 2020-12）与状态接口**：[`schemas/task-packet.schema.json`](../schemas/task-packet.schema.json)、[`schemas/defect-record.schema.json`](../schemas/defect-record.schema.json)、[`schemas/run-manifest.schema.json`](../schemas/run-manifest.schema.json)、[`schemas/graph-state.d.ts`](../schemas/graph-state.d.ts)
- **可直接复制的编排器提示词**：[`prompts/evidence-graph/orchestrator.md`](../prompts/evidence-graph/orchestrator.md)
- **黄金参考运行样例**：[`examples/run-0001/`](../examples/run-0001/)
- **技术勘误与跨版本对齐规范**：[`docs/TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md`](TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md)
- **三款跨品类游戏垂直切片配套指南**：
  - [docs/THE_HOLLOW_MERIDIAN_GUIDE.zh-CN.md](THE_HOLLOW_MERIDIAN_GUIDE.zh-CN.md)（《虚空子午线 v1.0》动作 RPG，81 页，examples/run-0001/）
  - [docs/THE_GLASS_OSSUARY_GUIDE.zh-CN.md](THE_GLASS_OSSUARY_GUIDE.zh-CN.md)（《琉璃骸骨堂 v1.0》悬疑恐怖，36 页，examples/run-0002/）
  - [docs/PERIHELION_BREACH_GUIDE.zh-CN.md](PERIHELION_BREACH_GUIDE.zh-CN.md)（《近日点破袭 v1.0》科幻射击冒险，36 页，examples/run-0003/）
