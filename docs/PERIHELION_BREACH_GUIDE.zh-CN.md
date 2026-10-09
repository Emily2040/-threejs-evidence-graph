<!-- source_version: 2026.07.5; translation_status: reviewed; language: zh-CN -->

# 《近日点破袭》（Perihelion Breach）：第一人称科幻射击冒险研发与架构指南

[English](PERIHELION_BREACH_GUIDE.md) | [简体中文](PERIHELION_BREACH_GUIDE.zh-CN.md) | [日本語](PERIHELION_BREACH_GUIDE.ja.md) | [한국어](PERIHELION_BREACH_GUIDE.ko.md)

![Soren Kestrel 在《近日点破袭》的伊卡洛斯-9号太阳中继站定日镜桁架区高速机动](../assets/perihelion-breach-world-hero.jpg)

*本图为出版物概念设定渲染图，并非实机运行截图或交付验证证据。*

> **文档定位说明**
>
> 本文是《Perihelion Breach: FPS Adventure Full Multi-Agent Production Prompt v1.0》（[`publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf`](../publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf)，共 36 页，`95,265` 字节，SHA-256 `75bdfff21c905122b4e1a0352e8c760c27e7c80cf8c3d5dcad63ea2263f89170`）的简体中文原生技术指南。本文面向国内游戏工业与 WebGPU 引擎开发者，详述该第一人称科幻射击冒险（FPS Adventure）垂直切片的核心枪战循环、60 Hz 弹道与磁力抓钩运动学帧表、主动散热装填机制、外骨骼核心分支、双阶段 Boss 架构及 Evidence Graph v2.0 验收门禁。本仓库交付的是架构规格书与多智能体生产提示词套件，尚未包含可运行的 Three.js 成品代码。

---

## 1. 立项定位与核心设计哲学

《近日点破袭》（*Perihelion Breach*）是 *Three.js Evidence Graph* 研发套件中的**第一人称射击冒险（First-Person Shooter Adventure）**旗舰规格书。项目要求在 Three.js `r185`（`0.185.0`）环境下，以**零外部下载二进制资产**（不依赖外部 `.glb`、贴图、字体或预录音频文件）的纯代码编译方式，构建一段流程时长为 **12 至 15 分钟**的高速科幻 FPS 冒险垂直切片。

本作将 **60 Hz 高精度弹道枪战**与**三维空间抓钩摆荡及管线解谜**深度咬合：

- **单局流程时长**：12 至 15 分钟，无缝串联日冕轨道空间站的 5 大工程扇区。
- **主角设定**：**Soren Kestrel**（中继站先锋官，`The Relay Vanguard`），战术 AI **Vesper** 全程提供遥测导航；核心三维状态指标为 **`100 护盾（Shield）`**、**`100 装甲完整度（Hull Integrity）`** 与 **`0–100 核心热量（Core Heat）`**。
- **三把多功能复合武器**：`Kestrel-9 双线圈卡宾枪`（`coil_carbine`，副武器发射 `磁力抓钩锚点`）、`赫利俄斯散射磁轨炮`（`scatter_rail`）与 `弧翼破障榴弹发射器`（`breach_launcher`）。
- **主动散热装填（Thermal Vent Reload）与三维抓钩运动学**：在 `36 ticks` 换弹动作的第 `14..20 ticks` 黄金窗口内再次按下装填键，即可瞬间清空 `100% 核心热量` 并获得 `90 ticks` 电离超载增伤；上半身武器状态机与下半身 `滑铲推进`（`11.5 m/s`）及 `磁力抓钩牵引`（`18.0 m/s`）完全解耦。
- **外骨骼核心校准（Suit Rig Calibration）**：三选一互斥外骨骼改装核心（`后坐力陀螺仪`、`热能虹吸回路`、`抓钩超载驱动`），彻底改变控枪手感、热量经济与空中机动性。
- **三类合成体敌兵与双阶段主菜 Boss**：`伏特掠行虫`（`Volt Skitter`）、`神盾浮游机`（`Aegis Drone`）、`熔渣重装兵`（`Slag Enforcer`），以及镇守反应堆中枢的 **`日冕典狱长`（`The Heliarch Warden`，`1,000 装甲完整度`）**。
- **双结局轨道指令**：`DIRECTIVE_DIVERT`（偏转定日镜阵列以保全地球电网）或 `DIRECTIVE_VENT`（抛射反应堆核心以弹射船员救生舱）。

---

## 2. 世界观舞台与程序化材质规范

故事发生于距离太阳仅 `0.09 AU` 近日点轨道的**伊卡洛斯-9号（Icarus-9）巨型太阳中继站**。`5800K` 的炽烈日冕强光、深邃的真空硬阴影与蓝青色的切伦科夫冷却剂辉光形成强烈视觉对比。外层空间区域每 `240 ticks`（4 秒）触发一次日冕耀斑扫射，玩家必须利用防爆百叶窗投下的硬阴影走廊进行高速掩体机动。

| 材质家族 | 色值 Token | Three.js `r185` TSL 程序化着色与几何生成规范 |
| :--- | :--- | :--- |
| **真空碳纤维（Vacuum Carbon）** | `#090D14` | 防微陨石哑光碳纤维护板，带各向异性编织法线纹理 |
| **轨道钛合金（Orbital Titanium）** | `#1A2433` | 拉丝结构桁架、防爆百叶闸门与第一人称武器机匣 |
| **日冕琥珀金（Corona Amber）** | `#F08A24` | 聚酰亚胺金箔定日镜阵列与日冕耀斑高温危险预警区 |
| **切伦科夫青（Cherenkov Cyan）** | `#38C6D9` | 电离磁轨弹道尾迹、低温冷却剂管道与主动散热电弧 |
| **过热等离子红（Overheat Plasma Red）** | `#E54848` | 核心过热警报（`>= 85 Heat`）、敌方散热弱点核心与迫击炮弹道弧 |

---

## 3. 十拍轨道作战推进路线（`restore_perihelion_attitude`）

| 节拍 | 空间站扇区 | 战术作战目标与空间解谜门禁 |
| ---: | :--- | :--- |
| **01** | **脐带气闸舱（`Umbilical Airlock`）** | 零重力对接脊柱舱；初始化战术 AI `Vesper` 遥测界面，装备 `Kestrel-9 双线圈卡宾枪` |
| **02** | **气闸主脊（`Airlock Spine`）** | 击碎磁力脐带锁；校准 `滑铲推进`（`24 ticks`）与 `主动散热装填`（`ticks 14..20` 判定窗口） |
| **03** | **定日镜桁架区（`Heliostat Truss`）** | 在 `240-tick` 日冕耀斑周期掩护下穿越外部反射镜步道，迎击 `伏特掠行虫` 群并解锁 `磁力抓钩` |
| **04** | **低温冷却歧管（`Cryo-Coolant Manifold`）** | 利用磁力抓钩在垂直涡轮井道内高速摆荡攀升，突破 `神盾浮游机` 狙击封锁，夺取 `弧翼破障榴弹发射器` |
| **05** | **相位管线接通（`Conduit Phase Routing`）** | 在 `180 ticks` 电容衰减窗口内连续发射 3 枚抛物线等离子锚点接通冷却回路，取出 `冷却旁路核心` |
| **06** | **弹道铸造厂（`Ballistic Foundry`）** | 多层立体熔炉竞技场攻坚战，击败重装 `熔渣重装兵`，取得 `赫利俄斯散射磁轨炮` 与 `点火密钥卡` |
| **07** | **外骨骼校准台（`Suit Rig Calibration`）** | 在工程台安装唯一外骨骼核心：`后坐力陀螺仪`（`recoil_gyro`）、`热能虹吸回路`（`thermal_siphon`）或 `抓钩超载驱动`（`grapple_overdrive`） |
| **08** | **日冕防爆闸（`Corona Blast Shutter`）** | 收回直面太阳日冕的巨型钨合金防护闸门，突入 `近日点核心舱` |
| **09** | **近日点核心舱（`Perihelion Core Chamber`）** | 迎战双阶段高速轨道 Boss **`日冕典狱长`（`The Heliarch Warden`，`1,000 装甲完整度`）** |
| **10** | **姿态控制舰桥（`Attitude Control Bridge`）** | 执行 `DIRECTIVE_DIVERT` 或 `DIRECTIVE_VENT` 最终指令，写入版本化存档并封存任务遥测日志 |

---

## 4. 60 Hz 确定性武器、主动散热与抓钩运动学帧数表

所有枪械射速、充能斜率、主动散热窗口及位移冲量均严格运行于 60 Hz 整数帧（`1 tick = 16.6667 ms`）。上半身换弹计时器与下半身抓钩脱钩/滑铲状态机完全解耦（修复缺陷 `FPS-N06A-COMBAT-019`）。

| 动作名称 | 前摇（Startup） | 判定/蓄力窗口（Active） | 后摇（Recovery） | 总帧数 | 热量消耗、伤害与机制效果 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **卡宾枪三连发（`Carbine 3-Burst`）** | `2 ticks` | `Ticks 3..11`（3 发） | `10 ticks` | `21 ticks` | `+12 Heat`；`3 x 14` 即时命中伤害（弱点倍率 `1.5x`） |
| **散射磁轨腰射（`Scatter Uncharged`）** | `3 ticks` | `Tick 4`（`5x12` 散射） | `15 ticks` | `18 ticks` | `+18 Heat`；`60` 近距箭霰伤害，高效击穿能量护盾 |
| **磁轨开镜蓄力弹（`Scatter ADS Slug`）** | `30..54 ticks` | `Tick 31..55` | `18 ticks` | `48..72 ticks` | `+28 Heat`；`55..85` 穿透电磁弹头（弱点倍率 `1.75x`） |
| **破障等离子锚（`Breach Anchor`）** | `6 ticks` | 抛物线飞行 | `24 ticks` | `30 ticks` | `+30 Heat`；`60 AoE` 破甲爆炸，或接通解谜导电节点 |
| **主动散热装填（`Thermal Vent Reload`）** | `13 ticks` | `Ticks 14..20` | `16 ticks` | `36 ticks` | 在 `14..20t` 按下装填清空 `100% 热量` 并获 `90t` 超载增伤 |
| **滑铲推进（`Slide-Boost`）** | `3 ticks` | `Ticks 4..18` | `6 ticks` | `24 ticks` | `11.5 m/s` 低姿滑铲；支持在 `ticks 8..18` 跳跃取消保速 |
| **磁力抓钩牵引（`Magnetic Grapple`）** | `6 ticks` | `18..42 ticks` 牵引 | `12 ticks` | `36..60 ticks` | `18.0 m/s` 高速拉向锚点；脱钩时完整保留切向摆荡动量 |

---

## 5. 合成体敌兵阵容与双阶段 Boss：日冕典狱长（The Heliarch Warden）

![Soren Kestrel 在近日点核心舱内使用磁力抓钩与磁轨炮迎战“日冕典狱长”](../assets/perihelion-breach-combat-hero.jpg)

*本图为出版物概念设定渲染图，并非实机运行截图或交付验证证据。*

### 三类合成体敌兵原型
1. **伏特掠行虫（`Volt Skitter`）**：高速四足维修合成体（`90 Hull`，移速 `6.8 m/s`），可沿墙壁与桁架横梁攀爬突袭，迫使玩家保持高速位移。
2. **神盾浮游机（`Aegis Drone`）**：悬浮定向护盾哨戒机（`140 Hull + 80 Shield`），正面展开能量屏障并在高空步道精准狙击；需利用抓钩绕后或用散射磁轨炮过载其护盾。
3. **熔渣重装兵（`Slag Enforcer`）**：重装甲铸造机兵（`320 Hull`），发射高抛熔渣迫击炮；每次齐射后其背部 `冷却脊柱（Coolant Spine）` 会暴露 `90 ticks`（承受 `1.75x` 弱点伤害）。

### 双阶段 Boss：日冕典狱长（`The Heliarch Warden`，`1,000 装甲完整度`）
- **结构设计**：悬浮于旋转反应堆万向节中央的 `6.0 m` 陀螺仪日冕自律机甲，外围环绕四片可展开的定日镜翼板与磁力抓钩锚定环。
- **第一阶段（`1,000 -> 501 完整度`）**：施展 `日冕横扫光束`（`Solar Sweep Beam`，需低姿滑铲穿过下缘或抓钩腾空规避）、`抓钩塔空投`（`Grapple Pylon Drop`）、`集束熔渣迫击炮`（`Cluster Mortar`）与 `辐射脉冲`（`Radiant Pulse`，释放后背部 `核心散热口 Core Vent` 暴露 `150 ticks`）。
- **第二阶段（`500 -> 0 完整度`）**：反应堆底部防护甲板收缩，下方直接暴露炽热日冕等离子流，迫使玩家在三层反向旋转的悬空步道环之间依靠磁力抓钩摆荡作战。新增 `日冕物质抛射`（`Coronal Ejection`）、`旋转镜环折射`（`Rotating Mirror Ring`）、`磁轨齐射`（`Rail Volley`）与 `近日点坍缩`（`Perihelion Collapse`，完美规避后核心散热口暴露 `150 ticks`）。

---

## 6. 外骨骼核心校准：三大改装分支

在第 07 拍（`Suit Rig Calibration`）中，玩家可在工程校准台安装三枚互斥外骨骼核心之一（记录于 `GraphState.active_relic`）：

- **`后坐力陀螺仪`（`recoil_gyro`）**：将第一人称武器视角上跳降低 `-45%`，散射磁轨炮腰射散布收窄 `-25%`，并将精准弱点伤害倍率从 `1.5x` 提升至 `1.85x`。
- **`热能虹吸回路`（`thermal_siphon`）**：将 `主动散热装填` 的黄金判定窗口从 `ticks 14..20`（7 帧）拓宽至 `ticks 12..23`（12 帧），并将排出的核心热量转化为 `+25 临时超载护盾`。
- **`抓钩超载驱动`（`grapple_overdrive`）**：将 `磁力抓钩` 牵引速度从 `18.0 m/s` 提升至 `22.5 m/s`，冷却时间缩短 `-35%`，并在抓钩飞踢命中时释放脉冲电磁震波。

---

## 7. 独立提示词、Schema 契约与黄金验证样本

- **主控编排器提示词（Orchestrator Prompt）**：[`prompts/perihelion-breach/orchestrator.md`](../prompts/perihelion-breach/orchestrator.md)（同步镜像于 [`orchestration/prompts/perihelion-breach-orchestrator.md`](../orchestration/prompts/perihelion-breach-orchestrator.md)）
- **7 张专家智能体卡（Specialist Agent Cards）**：[`prompts/perihelion-breach/agents/`](../prompts/perihelion-breach/agents/)
- **黄金参考样本（`run-0003`）**：[`examples/run-0003/task-packet.json`](../examples/run-0003/task-packet.json)、[`examples/run-0003/defect-record.json`](../examples/run-0003/defect-record.json)、[`examples/run-0003/run-manifest.json`](../examples/run-0003/run-manifest.json)
- **同系列四卷配套指南**：
  - [`docs/EVIDENCE_GRAPH_GUIDE.zh-CN.md`](EVIDENCE_GRAPH_GUIDE.zh-CN.md)（《Three.js Evidence Graph v2.0 操作手册》，64 页）
  - [`docs/THE_HOLLOW_MERIDIAN_GUIDE.zh-CN.md`](THE_HOLLOW_MERIDIAN_GUIDE.zh-CN.md)（《虚空子午线 v1.0》，81 页）
  - [`docs/THE_GLASS_OSSUARY_GUIDE.zh-CN.md`](THE_GLASS_OSSUARY_GUIDE.zh-CN.md)（《琉璃骸骨堂 v1.0》，36 页）
