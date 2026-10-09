<!-- source_version: 2026.07.5; translation_status: reviewed; language: ja -->

# 『Three.js エビデンスグラフ＆ゼロアセット3大ジャンル垂直スライス公式設定資料集・建築解体新書』

![Three.js エビデンスグラフ＆ゼロアセット3大ジャンル垂直スライス制作仕様書集成](assets/svg/masthead-ja.svg)

| **公式設定資料集・言語版** | [**English (Original Folio)**](README.md) | [**简体中文 (典藏设定集版)**](README.zh-CN.md) | [**日本語 (公式設定資料集・解体新書版)**](README.ja.md) | [**한국어 (공식 아트북 & 마스터북판)**](README.ko.md) |
| :--- | :---: | :---: | :---: | :---: |
| **図録奥付 (COLOPHON)** | `Release 2026.07.5` | `全4巻 · 計217頁` | `Three.js r185 (0.185.0) WebGPU + TSL` | `外部バイナリアセットゼロ · MIT License` |

![3つのプロシージャル世界観を結ぶ建築三連画：『虚ろの子午線』『硝子の納骨堂』『ペリヘリオン・ブリーチ』](assets/readme-hero.jpg)

*図版 00：エビデンスグラフ制御基盤によって統御される3つのプロシージャル世界観の建築三連画。左：玄武岩の大聖堂、真鍮の子午環、そして「名もなき鐘」が聳えるダークファンタジー・アクションRPG『虚ろの子午線』（第二巻）。中央：1894年の嵐の孤島に建つフレネル灯台と骨硝子の地下納骨堂を舞台にした調査ミステリーホラー『硝子の納骨堂』（第三巻）。右：0.09 AUの太陽極近傍軌道を周回するヘリオスタット鏡群と灼熱のコロナを描くSF FPSアドベンチャー『ペリヘリオン・ブリーチ』（第四巻）。*

---

## 編纂序文・全四巻モノグラフ構成

単一コンテキストの対話型LLMによるゲーム生成は、同じコンテキスト窓がスコープを考案し、シェーダーを書き、フレーム判定を調整し、自らの出力を自己採点し始めた瞬間に破綻します。**Emily Paradox (`@iamemily2050`)** による**全4巻・計`217`頁の建築・ゲームシステム解体新書**は、自己完結型のチャットループを廃し、**Three.js `r185` (`0.185.0`)** 向けの決定論的マルチエージェント制作基盤を提示します。

本叢書におけるすべてのメッシュ、`TSL`（`Three.js Shading Language`）マテリアルノード、スケルタルリグ、音響インパルス応答、および60 Hzの戦闘・鑑識・弾道フレームテーブルは、**外部ダウンロードアセットゼロ**（`external_network_requests = 0`、`downloaded_assets_count = 0`）でソースコードから決定論的にコンパイルされます。

![全四巻コレクターズ・モノグラフ図録（計217頁）](assets/publication-set.jpg)

### 全四巻モノグラフ収録目録 (`publications/`)

| **第一巻 · 64頁** | **第二巻 · 81頁** | **第三巻 · 36頁** | **第四巻 · 36頁** |
| :---: | :---: | :---: | :---: |
| [![第一巻：Three.js エビデンスグラフ v2.0](assets/threejs-evidence-graph-cover.jpg)](publications/threejs-evidence-graph-operational-manual-v2.0-en.pdf) | [![第二巻：『虚ろの子午線』](assets/the-hollow-meridian-cover.jpg)](publications/the-hollow-meridian-rpg-full-prompt-v1.0-en.pdf) | [![第三巻：『硝子の納骨堂』](assets/the-glass-ossuary-cover.jpg)](publications/the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf) | [![第四巻：『ペリヘリオン・ブリーチ』](assets/perihelion-breach-cover.jpg)](publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf) |
| [**『運用マニュアル v2.0』**](publications/threejs-evidence-graph-operational-manual-v2.0-en.pdf)<br/>`制御基盤＆決定論的検証規約` | [**『虚ろの子午線』**](publications/the-hollow-meridian-rpg-full-prompt-v1.0-en.pdf)<br/>`Game 01 · 三人称アクションRPG` | [**『硝子の納骨堂』**](publications/the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf)<br/>`Game 02 · 一人称ミステリーホラー` | [**『ペリヘリオン・ブリーチ』**](publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf)<br/>`Game 03 · 0.09 AU SF FPS` |
| `sha256: d3830d411a61c52c`<br/>`416,827 bytes` | `sha256: c4f8fe83995d526b`<br/>`357,144 bytes` | `sha256: efead090be003782`<br/>`98,649 bytes` | `sha256: 75bdfff21c905122`<br/>`95,265 bytes` |
| **ネイティブ解説書**：<br/>[EN](docs/EVIDENCE_GRAPH_GUIDE.md) · [中文](docs/EVIDENCE_GRAPH_GUIDE.zh-CN.md) · [日本語](docs/EVIDENCE_GRAPH_GUIDE.ja.md) · [한국어](docs/EVIDENCE_GRAPH_GUIDE.ko.md) | **ネイティブ解説書**：<br/>[EN](docs/THE_HOLLOW_MERIDIAN_GUIDE.md) · [中文](docs/THE_HOLLOW_MERIDIAN_GUIDE.zh-CN.md) · [日本語](docs/THE_HOLLOW_MERIDIAN_GUIDE.ja.md) · [한국어](docs/THE_HOLLOW_MERIDIAN_GUIDE.ko.md) | **ネイティブ解説書**：<br/>[EN](docs/THE_GLASS_OSSUARY_GUIDE.md) · [中文](docs/THE_GLASS_OSSUARY_GUIDE.zh-CN.md) · [日本語](docs/THE_GLASS_OSSUARY_GUIDE.ja.md) · [한국어](docs/THE_GLASS_OSSUARY_GUIDE.ko.md) | **ネイティブ解説書**：<br/>[EN](docs/PERIHELION_BREACH_GUIDE.md) · [中文](docs/PERIHELION_BREACH_GUIDE.zh-CN.md) · [日本語](docs/PERIHELION_BREACH_GUIDE.ja.md) · [한국어](docs/PERIHELION_BREACH_GUIDE.ko.md) |
| **スキーマ＆プロンプト**：<br/>[`prompts/evidence-graph/`](prompts/evidence-graph/) · [`schemas/`](schemas/) | **プロンプト＆基準実行**：<br/>[`prompts/hollow-meridian/`](prompts/hollow-meridian/) · [`run-0001`](examples/run-0001/) | **プロンプト＆基準実行**：<br/>[`prompts/glass-ossuary/`](prompts/glass-ossuary/) · [`run-0002`](examples/run-0002/) | **プロンプト＆基準実行**：<br/>[`prompts/perihelion-breach/`](prompts/perihelion-breach/) · [`run-0003`](examples/run-0003/) |

---

## 第一巻 · 決定論的制御プレーン（『Three.js エビデンスグラフ v2.0』 · 64頁）

| 図版 I-A：天文時計式検証機構＆光学制御アトリエ | 図版 I-B：ゼロアセット・プロシージャル幾何＆TSLコンパイル工房 |
| :---: | :---: |
| ![決定論的検証アトリエ](assets/evidence-graph-control-hero.jpg) | ![プロシージャル幾何＆TSLシェーダー工房](assets/evidence-graph-atelier-hero.jpg) |

![建築青写真図版 I：15ノード決定論的エビデンスグラフと3ジャンル垂直スライス実装構造](assets/svg/architecture-pipeline-ja.svg)

第一巻は、全3タイトルに共通する4つの構造的不変条件を定義します。

1. **15ノード有向巡回制御プレーン（`N00_BRIEF` .. `N14_RELEASE_CANDIDATE`）**：[`schemas/graph-state.d.ts`](schemas/graph-state.d.ts) によって厳格に統御されます。スキーマ検証済みの [`TaskPacket`](schemas/task-packet.schema.json) と合格済みの検証コマンド出力が揃わない限り、オーケストレーターは次のノードへ遷移できません。不適合時は有界ロールバック（`N13_REPAIR_ROUTER -> N05..N08`、ノード単位最大`3`回・全体最大`8`回）が発動します。
2. **ファイル所有権が分離された7つの専門エージェント**：各タイトルは7枚の専門ロールカード（`combat_gameplay`、`world_quest`、`procedural_art_vfx`、`procedural_audio`、`ui_hud_accessibility`、`qa_perf_playwright`、および読取専用の `independent_critic`）に分割され、`allowed_paths` 外の編集や検証基準の緩和は禁止されます。
3. **二系統の決定論レジーム（`A-PinnedBrowser` ＆ `B-CrossPlatform`）**：
   - **レジーム A（`A-PinnedBrowser`）**：固定Chromium＋GPU/SwiftShader環境におけるビット完全SHA-256検証（60 Hz整数シミュレーション `state_hash`、16-bit PCM量子化 `OfflineAudioContext` 音声 `audio_hash`、`1e-5` 量子化頂点バッファ `geometry_hash`）。
   - **レジーム B（`B-CrossPlatform`）**：`THREE.WebGPURenderer` と `{ forceWebGL: true }` フォールバック環境における知覚・不変条件ゲート（`P50 <= 8.3 ms`、`P95 <= 16.6 ms`、`P99 <= 22.0 ms`、ラウドネス `-16 LUFS +- 1.0 LU`、トゥルーピーク `<= -1.0 dBTP`）。
4. **アンチスロップ＆ゼロアセット来歴監査ゲート（`provenance_critic`）**：外部 `.glb/.gltf/.fbx/.obj/.png/.jpg/.wav/.mp3/.ogg` の取得を全面禁止し、汎用AIネオンパープル（`#7567F5`）の使用を遮断します。

---

## 第二巻 · ゲーム 01：『虚ろの子午線』 *The Hollow Meridian*（三人称ダークファンタジー・アクションRPG · 81頁）

| 図版 II-1：沈めるアストロラーベ参道と天体儀橋 | 図版 II-2：鋳鐘場と三聖遺物の祭壇 | 図版 II-3：子午線の間と「名もなき鐘」決戦 |
| :---: | :---: | :---: |
| ![『虚ろの子午線』ワールドルート概念図](assets/hollow-meridian-world-hero.jpg) | ![『虚ろの子午線』鋳鐘場と三聖遺物の祭壇](assets/hollow-meridian-sanctum-hero.jpg) | ![『虚ろの子午線』名もなき鐘ボス戦概念図](assets/hollow-meridian-boss-hero.jpg) |

![天文時計・近接戦闘青写真図版 II-A：『虚ろの子午線』60 Hz 近接判定フレーム表、鉱物パレット＆ボスゲート](assets/svg/game-01-telemetry-ja.svg)

失われた都市の「真名」を保存するために築かれた玄武岩と真鍮の巨大天文台を舞台に、プレイヤーは**測量師（`The Cartographer` / `Sable Veren`）**として10〜14分の垂直スライスを踏破します。5つの接続空間（`Ash Court` -> `Orrery Bridge` -> `Archive Nave` -> `Bell Foundry` -> `Meridian Chamber`）を巡り、3連リングの `Meridian Alignment` パズルを解き、ビルドを定義する3つの聖遺物から1つを選び、2段階ボス**名もなき鐘（The Bell Without a Name、850 HP、55% / 467 HPで第2段階音響分裂）**に挑みます。

| 60 Hz 近接アクション (`seed=1337`) | 発生 (Startup) | 持続 / パリィ / 無敵窓 | 硬直 (Recovery) | 合計フレーム | スタミナ / 共鳴コストとメカニクス効果 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Light Attack 1 / 2 / 3` | `10 / 11 / 15t` | `5 / 7 / 9 ticks` | `12 / 12 / 18t` | `27 / 30 / 42t` | `10 / 11 / 14 Stamina`消費；`16 / 18 / 25 HP`ダメージ |
| `Charged Heavy`（溜め強攻撃） | `27..38 ticks` | `10..11 ticks` | `12..14 ticks` | `49..63 ticks` | `28 Stamina`消費；`28..42 HP`ダメージ＋強靭削り |
| `Dodge Roll`（回避ロール） | `7 ticks` | `Ticks 7..18`（`12t`無敵） | `12 ticks` | `31 ticks` | `22 Stamina`消費（`ash_thread`時`18`）；完全無敵窓 |
| `Parry Deflect`（パリィ弾き） | `5 ticks` (`0..4`) | `Ticks 6..12`（`7t`弾き） | `18 ticks` | `31 ticks` | `12 Stamina`消費；`tick >= 13`長押しで `Guard` へ移行 |
| `Echo Brand`（残響の刻印） | `12 ticks` | `360 ticks` 脆弱化刻印 | `0 ticks` | `12 ticks` | `50 Resonance`消費（`vacant_name`時`60`・`540 ticks`持続）；被ダメージ`+25%` |

- **規範英語版PDF（`81`頁）**：[`publications/the-hollow-meridian-rpg-full-prompt-v1.0-en.pdf`](publications/the-hollow-meridian-rpg-full-prompt-v1.0-en.pdf)
- **4言語ネイティブ解説書**：[日本語](docs/THE_HOLLOW_MERIDIAN_GUIDE.ja.md) · [English](docs/THE_HOLLOW_MERIDIAN_GUIDE.md) · [简体中文](docs/THE_HOLLOW_MERIDIAN_GUIDE.zh-CN.md) · [한국어](docs/THE_HOLLOW_MERIDIAN_GUIDE.ko.md)
- **エージェントカード＆基準実行**：[`prompts/hollow-meridian/`](prompts/hollow-meridian/)（`orchestrator.md`＋専門カード7枚） · [`examples/run-0001/`](examples/run-0001/)

---

## 第三巻 · ゲーム 02：『硝子の納骨堂』 *The Glass Ossuary*（一人称調査ミステリーホラー · 36頁）

| 図版 III-1：サン＝ヴェーヌ岩礁と屈折回廊 | 図版 III-2：灯台守の剥離室と1894年鑑識作業台 | 図版 III-3：骨硝子の地下納骨堂と「硝子の聖歌隊」 |
| :---: | :---: | :---: |
| ![『硝子の納骨堂』科学調査概念図](assets/glass-ossuary-investigation-hero.jpg) | ![『硝子の納骨堂』灯台守の剥離室と鑑識作業台](assets/glass-ossuary-inquest-hero.jpg) | ![『硝子の納骨堂』硝子の聖歌隊ボス戦概念図](assets/glass-ossuary-apparition-hero.jpg) |

![1894年 光学・音響鑑識青写真図版 III-A：『硝子の納骨堂』60 Hz 調査機器タイミング、湿板パレット＆審問推理ボード](assets/svg/game-02-telemetry-ja.svg)

1894年10月、嵐に閉ざされた潮汐島**サン＝ヴェーヌ岩礁（Saint-Vane Reef）**。音響記録官 **Clara Vane** は、地下の骨硝子納骨堂と融合した古い沿岸灯台へ足を踏み入れます。銃器による戦闘や安易なジャンプスケアを排し、19世紀の3つの物理鑑識機器（`Split-Diopter Brass Loupe` 複焦点真鍮ルーペ、`Wax-Cylinder Phonograph` 蝋管蓄音機、`Silver-Salt Ferrotype Plate` 銀塩湿板フラッシュ）と6ノードの `Inquest Board`（審問推理盤）、そして光と音のステルス規律のみを頼りに、**硝子の聖歌隊（The Choir in the Glass、600 共鳴完全性、300で第2段階分裂）**の真相を暴きます。

| 60 Hz 鑑識・ステルス動作 (`seed=1894`) | 発生 (Startup) | 有効ウィンドウ (Active) | 硬直 / 冷却 | 合計フレーム | リソース消費と光学・音響鑑識メカニクス |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Lantern Shutter`（ランタン遮光） | `6 ticks` | トグル維持（`tick 7..`） | `6 ticks` | `12 ticks` | `0 Oil`；光円錐を即座に遮断し、`Glass Septum Watcher` の視線ロックを切る |
| `Brass Loupe Focus`（ルーペ焦点） | `9 ticks` | 長押し（`ticks 10..69`） | `6 ticks` | `75 ticks` | `0 Oil`；フレネル環角度（`45/135/270 deg`）と骨硝子の微細亀裂を解読 |
| `Phonograph Cancel`（逆位相再生） | `24 ticks` | `Ticks 25..114`（`90t`） | `36 ticks` | `150 ticks` | 逆位相音波で室内共鳴を打ち消し、`Mire Listener` から足音を隠蔽 |
| `Ferrotype UV Flash`（湿板UV閃光） | `18 ticks` | `Ticks 19..24`（`6t`） | `66 ticks` | `90 ticks` | `6.5 m`内の怪異を`102 ticks`（`lens_sabotage`時`132 ticks`）スタン |
| `Crouch Sidestep`（しゃがみ歩調） | `5 ticks` | `Ticks 6..16`（`11t`） | `12 ticks` | `28 ticks` | 濡れた石床の足音ピークを `<= -38 dBFS` 以下に抑制 |
| `Smelling Salts`（気付け塩） | `15 ticks` | `Ticks 16..45`（`30t`） | `10 ticks` | `55 ticks` | `Composure +40` 回復、および `Exposure -25` 浄化 |

- **規範英語版PDF（`36`頁）**：[`publications/the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf`](publications/the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf)
- **4言語ネイティブ解説書**：[日本語](docs/THE_GLASS_OSSUARY_GUIDE.ja.md) · [English](docs/THE_GLASS_OSSUARY_GUIDE.md) · [简体中文](docs/THE_GLASS_OSSUARY_GUIDE.zh-CN.md) · [한국어](docs/THE_GLASS_OSSUARY_GUIDE.ko.md)
- **エージェントカード＆基準実行**：[`prompts/glass-ossuary/`](prompts/glass-ossuary/)（`orchestrator.md`＋専門カード7枚） · [`examples/run-0002/`](examples/run-0002/)

---

## 第四巻 · ゲーム 03：『ペリヘリオン・ブリーチ』 *Perihelion Breach*（一人称SFシューター・アドベンチャー · 36頁）

| 図版 IV-1：0.09 AU イカロス9号ヘリオスタット主トラス | 図版 IV-2：極低温冷却マニホールドと排熱リロード銃撃戦 | 図版 IV-3：近日点コアチェンバーと「ヘリアーク・ウォーデン」決戦 |
| :---: | :---: | :---: |
| ![『ペリヘリオン・ブリーチ』軌道ステージ概念図](assets/perihelion-breach-world-hero.jpg) | ![『ペリヘリオン・ブリーチ』極低温冷却マニホールドと排熱リロード](assets/perihelion-breach-arsenal-hero.jpg) | ![『ペリヘリオン・ブリーチ』ヘリアーク・ウォーデン戦闘概念図](assets/perihelion-breach-combat-hero.jpg) |

![0.09 AU 軌道弾道・熱力学青写真図版 IV-A：『ペリヘリオン・ブリーチ』60 Hz グラップル、排熱リロード＆太陽フレア周期](assets/svg/game-03-telemetry-ja.svg)

太陽からわずか `0.09 AU` の極近傍軌道を周回する**イカロス9号軌道太陽中継ステーション（Icarus-9 Orbital Solar Relay）**。防衛グリッドの暴走によりヘリオスタット鏡群が熱暴走カスケードに陥った施設へ、先遣隊スペシャリスト **Soren Kestrel** が突入します。`18.0 m/s` の `Magnetic Grapple` スリングショット、`11.5 m/s` の `Slide-Boost`、`ticks 14..20` のアクティブ `Thermal Vent Reload`（排熱リロード）、および `240 ticks`（`4.0 s`）周期の太陽フレア遮蔽回廊を駆使し、立体アリーナで**ヘリアーク・ウォーデン（The Heliarch Warden、1,000 装甲完全性、500で第2段階移行）**を撃破します。

| 60 Hz 弾道・機動アクション (`seed=2142`) | 発生 (Startup) | 有効窓 (Active) | 硬直 / 回復 | 合計フレーム | 熱量 / 速度とメカニクス効果 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Carbine 3-Burst`（3点バースト） | `2 ticks` | `Ticks 3..11`（3発） | `10 ticks` | `21 ticks` | `+12 Heat`；`3 x 14 dmg` ヒットスキャン（弱点倍率 `1.5x`） |
| `Scatter Uncharged`（非チャージ散弾） | `3 ticks` | `Tick 4`（`5x12`拡散） | `15 ticks` | `18 ticks` | `+18 Heat`；近距離`60 dmg`、エネルギーシールドを一撃剥離 |
| `Scatter ADS Rail Slug`（ADS徹甲弾） | `30..54t` | `Tick 31..55` | `18 ticks` | `48..72 ticks` | `+28 Heat`；`55..85 dmg` 貫通レールスラッグ（弱点倍率 `1.75x`） |
| `Breach Anchor`（ブリーチアンカー） | `6 ticks` | テザー弾頭 | `24 ticks` | `30 ticks` | `+30 Heat`；`60 AoE dmg` 装甲破砕または導管位相リンク接続 |
| `Thermal Vent Reload`（排熱リロード） | `13 ticks` | `Ticks 14..20`（`7t`） | `16 ticks` | `36 ticks` | `14..20t`入力成功で `Heat 100%` 即時パージ＋`90t` オーバーチャージ |
| `Slide-Boost`（スライドブースト） | `3 ticks` | `Ticks 4..18`（`15t`） | `6 ticks` | `24 ticks` | `11.5 m/s` 高速スライディング；`ticks 8..18` ジャンプキャンセル可 |
| `Magnetic Grapple`（磁気グラップル） | `6 ticks` | `18..42 ticks` 牽引 | `12 ticks` | `36..60 ticks` | `18.0 m/s` 高速牽引；接線ベクトル維持によるスリングショット跳躍 |

- **規範英語版PDF（`36`頁）**：[`publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf`](publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf)
- **4言語ネイティブ解説書**：[日本語](docs/PERIHELION_BREACH_GUIDE.ja.md) · [English](docs/PERIHELION_BREACH_GUIDE.md) · [简体中文](docs/PERIHELION_BREACH_GUIDE.zh-CN.md) · [한국어](docs/PERIHELION_BREACH_GUIDE.ko.md)
- **エージェントカード＆基準実行**：[`prompts/perihelion-breach/`](prompts/perihelion-breach/)（`orchestrator.md`＋専門カード7枚） · [`examples/run-0003/`](examples/run-0003/)

---

## 3大フラッグシップタイトル横断比較マトリクス

| 設計・技術次元 | 第二巻：『虚ろの子午線』 | 第三巻：『硝子の納骨堂』 | 第四巻：『ペリヘリオン・ブリーチ』 |
| :--- | :--- | :--- | :--- |
| **ジャンル＆カメラ** | 三人称ダークファンタジー・アクションRPG | 一人称調査ミステリーホラー | 一人称SFシューター・アドベンチャー |
| **想定プレイ時間** | 10〜14分（`81`頁PDF） | 12〜16分（`36`頁PDF） | 12〜15分（`36`頁PDF） |
| **主人公** | `Sable Veren`（測量師） | `Clara Vane`（音響記録官） | `Soren Kestrel`（軌道先遣隊） |
| **主要リソース** | `100 Health` · `100 Stamina` · `0-100 Resonance` | `100 Composure` · `100 Lantern Oil` · `0-100 Exposure` | `100 Shield` · `100 Hull Integrity` · `0-100 Core Heat` |
| **60 Hz 固有メカニクス** | `Parry Deflect`（`6..12t`）と長押し `Guard`（`>=13t`） | `Lantern Shutter`（`6t`）＋逆位相蓄音機＋湿板UV閃光（`19..24t`） | `Thermal Vent Reload`（`14..20t`）＋`18 m/s` グラップル＋スライド |
| **5つの接続空間** | `Ash Court` -> `Orrery Bridge` -> `Archive Nave` -> `Bell Foundry` -> `Meridian Chamber` | `Tidewater Causeway` -> `Caretaker's Stripping Room` -> `Refraction Gallery` -> `Submerged Crypt` -> `The Glass Ossuary` | `Umbilical Airlock` -> `Heliostat Truss` -> `Cryo-Coolant Manifold` -> `Ballistic Foundry` -> `Perihelion Core Chamber` |
| **ビート05 空間パズル** | `Meridian Alignment`（3連真鍮リング -> `North Seal`） | `Prism Triangulation`（`45/135/270度`）＋`110/220/330 Hz` 水門 | `Conduit Phase Routing`（`180t`減衰窓内に3導管接続 -> `Coolant Bypass`） |
| **3種の敵アーキタイプ** | `Ashbound Skirmisher`、`Lantern Wraith`、`Bell Sentinel` | `Mire Listener`、`Glass Septum Watcher`、`Drowned Chorister` | `Volt Skitter`、`Aegis Drone`、`Slag Enforcer` |
| **ビート07 ビルド選択** | **3聖遺物**：`brass_vow` · `ash_thread` · `vacant_name` | **3仮説**：`lens_sabotage` · `tidal_quarantine` · `acoustic_calling` | **3外骨格コア**：`recoil_gyro` · `thermal_siphon` · `grapple_overdrive` |
| **ビート09 2段階ボス** | **名もなき鐘**（`850 HP`、`467 HP`で第2段階） | **硝子の聖歌隊**（`600 Integrity`、`300`で第2段階） | **ヘリアーク・ウォーデン**（`1,000 Integrity`、`500`で第2段階） |
| **ビート10 マルチエンディング** | `CHOICE_BIND` または `CHOICE_RELEASE` | `VERDICT_PUBLISH` または `VERDICT_SUBMERGE` | `DIRECTIVE_DIVERT` または `DIRECTIVE_VENT` |
| **描画予算** | `<= 300` draw calls · `<= 500,000` tris | `<= 280` draw calls · `<= 460,000` tris | `<= 300` draw calls · `<= 500,000` tris |
| **ゴールデン実行記録** | [`examples/run-0001/`](examples/run-0001/) (`seed=1337`) | [`examples/run-0002/`](examples/run-0002/) (`seed=1894`) | [`examples/run-0003/`](examples/run-0003/) (`seed=2142`) |

---

## 4言語ネイティブドキュメント体系

| ドキュメント種別 | ネイティブ英語版 (`en`) | ネイティブ簡体字中国語版 (`zh-CN`) | ネイティブ日本語版 (`ja`) | ネイティブ韓国語版 (`ko`) |
| :--- | :--- | :--- | :--- | :--- |
| **総合案内・モノグラフ総覧** | [`README.md`](README.md) | [`README.zh-CN.md`](README.zh-CN.md) | [`README.ja.md`](README.ja.md) | [`README.ko.md`](README.ko.md) |
| **第一巻：エビデンスグラフ v2.0 (64頁)** | [`EVIDENCE_GRAPH_GUIDE.md`](docs/EVIDENCE_GRAPH_GUIDE.md) | [`EVIDENCE_GRAPH_GUIDE.zh-CN.md`](docs/EVIDENCE_GRAPH_GUIDE.zh-CN.md) | [`EVIDENCE_GRAPH_GUIDE.ja.md`](docs/EVIDENCE_GRAPH_GUIDE.ja.md) | [`EVIDENCE_GRAPH_GUIDE.ko.md`](docs/EVIDENCE_GRAPH_GUIDE.ko.md) |
| **第二巻：『虚ろの子午線』RPG (81頁)** | [`THE_HOLLOW_MERIDIAN_GUIDE.md`](docs/THE_HOLLOW_MERIDIAN_GUIDE.md) | [`THE_HOLLOW_MERIDIAN_GUIDE.zh-CN.md`](docs/THE_HOLLOW_MERIDIAN_GUIDE.zh-CN.md) | [`THE_HOLLOW_MERIDIAN_GUIDE.ja.md`](docs/THE_HOLLOW_MERIDIAN_GUIDE.ja.md) | [`THE_HOLLOW_MERIDIAN_GUIDE.ko.md`](docs/THE_HOLLOW_MERIDIAN_GUIDE.ko.md) |
| **第三巻：『硝子の納骨堂』ホラー (36頁)** | [`THE_GLASS_OSSUARY_GUIDE.md`](docs/THE_GLASS_OSSUARY_GUIDE.md) | [`THE_GLASS_OSSUARY_GUIDE.zh-CN.md`](docs/THE_GLASS_OSSUARY_GUIDE.zh-CN.md) | [`THE_GLASS_OSSUARY_GUIDE.ja.md`](docs/THE_GLASS_OSSUARY_GUIDE.ja.md) | [`THE_GLASS_OSSUARY_GUIDE.ko.md`](docs/THE_GLASS_OSSUARY_GUIDE.ko.md) |
| **第四巻：『ペリヘリオン・ブリーチ』FPS (36頁)** | [`PERIHELION_BREACH_GUIDE.md`](docs/PERIHELION_BREACH_GUIDE.md) | [`PERIHELION_BREACH_GUIDE.zh-CN.md`](docs/PERIHELION_BREACH_GUIDE.zh-CN.md) | [`PERIHELION_BREACH_GUIDE.ja.md`](docs/PERIHELION_BREACH_GUIDE.ja.md) | [`PERIHELION_BREACH_GUIDE.ko.md`](docs/PERIHELION_BREACH_GUIDE.ko.md) |
| **用語集＆翻訳ポリシー** | [`GLOSSARY.md`](docs/GLOSSARY.md) · [`TRANSLATION_POLICY.md`](docs/TRANSLATION_POLICY.md) | [`GLOSSARY.md`](docs/GLOSSARY.md) | [`GLOSSARY.md`](docs/GLOSSARY.md) | [`GLOSSARY.md`](docs/GLOSSARY.md) |

---

## リリース検証コマンド＆書誌情報

```bash
# 1. SHA256SUMS.txt の全チェックサムを検証
sha256sum -c SHA256SUMS.txt

# 2. 自動検証スイートを実行（4冊計217頁のPDF、9つのゴールデンフィクスチャ、17枚のゼロEXIF画像、21枚の青写真SVG、4言語リンクを検証）
python scripts/verify_release.py
```

- **技術正誤表＆v2.0整合仕様**：[`docs/TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md`](docs/TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md)
- **公開ステータス＆認識論的境界**：[`docs/PUBLICATION_STATUS.md`](docs/PUBLICATION_STATUS.md)
- **アートワーク来歴＆ゼロEXIF規約**：[`docs/ARTWORK_PROVENANCE.md`](docs/ARTWORK_PROVENANCE.md)
- **学術引用メタデータ**：[`CITATION.cff`](CITATION.cff) · [`CITATIONS.md`](CITATIONS.md)
- **ライセンス**：[MIT License](LICENSE) · Copyright (c) 2026 Emily Paradox (`@iamemily2050`)
