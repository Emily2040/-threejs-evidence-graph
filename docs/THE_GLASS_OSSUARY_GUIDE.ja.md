<!-- source_version: 2026.07.5; translation_status: reviewed; language: ja -->

# 『硝子の納骨堂』（The Glass Ossuary）：ミステリーホラー開発仕様・設計ガイド

| **MONOGRAPH EDITIONS** | [**English**](THE_GLASS_OSSUARY_GUIDE.md) | [**简体中文**](THE_GLASS_OSSUARY_GUIDE.zh-CN.md) | [**日本語**](THE_GLASS_OSSUARY_GUIDE.ja.md) | [**한국어**](THE_GLASS_OSSUARY_GUIDE.ko.md) |
| :--- | :---: | :---: | :---: | :---: |
| **VOLUME COLOPHON** | `第三巻 · 36頁 · ゲーム 02：一人称調査ミステリーホラー『硝子の納骨堂』 · SEED 1894` | [Normative PDF](../publications/the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf) | [Master Folio](../README.ja.md) | `Three.js r185 · Zero External Assets` |

| 第三巻モノグラフ表紙 (36頁) | 図版 III-1：サン＝ヴェーヌ岩礁と屈折回廊 | 図版 III-2：灯台守の剥離室と1894年鑑識作業台 | 図版 III-3：硝子の聖歌隊 2段階ボス戦 (600 Int.) |
| :---: | :---: | :---: | :---: |
| [![第三巻モノグラフ表紙 (36頁)](../assets/the-glass-ossuary-cover.jpg)](../publications/the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf) | ![図版 III-1：サン＝ヴェーヌ岩礁と屈折回廊](../assets/glass-ossuary-investigation-hero.jpg) | ![図版 III-2：灯台守の剥離室と1894年鑑識作業台](../assets/glass-ossuary-inquest-hero.jpg) | ![図版 III-3：硝子の聖歌隊 2段階ボス戦 (600 Int.)](../assets/glass-ossuary-apparition-hero.jpg) |

> **ガイドの位置づけ**
>
> 本書は『The Glass Ossuary: Mystery Horror Full Multi-Agent Production Prompt v1.0』（[`publications/the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf`](../publications/the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf)、全36頁、`98,649` バイト、SHA-256 `efead090be003782a122463ba17fe686caa1c30aeafcf66f11d294555c7aafda`）の日本語ネイティブ技術解説書です。一人称視点の調査型サイコロジカルホラー・バーティカルスライスにおけるゲームデザイン契約、60 Hz固定ティックの音響・光学鑑識ツール、6ノード推理ボード、二段階ボス戦、および Evidence Graph v2.0 検証ハーネスを規定します。本リポジトリは設計仕様書およびマルチエージェント用プロンプト群を提供するものであり、実行可能なゲームビルドそのものではありません。

---

## 1. 仕様書の概要とコア設計思想

『硝子の納骨堂』（*The Glass Ossuary*）は、*Three.js Evidence Graph* スイートにおける**ミステリーホラー（Mystery on Horror）**領域のフラッグシップ仕様書です。Three.js `r185`（`0.185.0`）上で、**外部バイナリアセットのダウンロードを一切行わず**（`.glb`モデル、外部テクスチャ、フォント、録音済み音声ファイル不使用）、リポジトリ内のTypeScriptコードとシード値のみから**プレイ時間12〜16分**の一人称調査ホラーを構築するための制作契約を定義しています。

安易なスクリプト演出によるジャンプスケアを排し、**物理的な鑑識器具の操作**と**決定論的な60 Hz音響・光学ステートマシン**によって恐怖と推理を駆動します。

- **想定プレイ時間**：12〜16分（シームレスに接続された5つの沿岸観測所エリア）。
- **主人公**：**Clara Vane**（音響記録保管官 / `The Acoustic Archivist`）。生存リソースは **`100 Composure（平静度）`**、**`100 Lantern Oil（ランタン油量）`**、**`0–100 Exposure（精神汚染度）`** の3軸。
- **3種のダイエジェティック鑑識器具**：`二焦点真鍮ルーペ`（`brass_loupe`）、`蝋管蓄音機`（`wax_phonograph`）、`銀塩フェロタイプ乾板カメラ`（`ferrotype_plate`）。
- **6ノード推理ボード（Inquest Board）**：集めた6つの物証を結線し、3つの排他的仮説（`レンズ破壊工作`、`潮汐隔離封鎖`、`音響招魂共鳴`）から1つを確定。選択した仮説が怪異の索敵挙動とボス戦の弱点露出フレームを直接変化させます。
- **3種の怪異（Apparitions）と二段階ボス**：`泥濘の聴取者`（`Mire Listener`）、`硝子隔壁の監視者`（`Glass Septum Watcher`）、`溺死聖歌隊員`（`Drowned Chorister`）、および深部ボス **`硝子の中の聖歌隊`（`The Choir in the Glass`、`600 Resonance Integrity`）**。
- **2つの結末（Verdict）**：`VERDICT_PUBLISH`（サン＝ヴァーヌ音響海難記録の公表）または `VERDICT_SUBMERGE`（納骨堂の完全水没による共鳴封鎖）。

---

## 2. 世界観と手続き型マテリアル設計

舞台は1894年秋の暴風雨に晒される**サン＝ヴァーヌ沿岸観測所（Saint-Vane Coastal Observatory）**。上層のフレネルレンズ灯台と、海難死者の声を閉じ込めるために骨灰と鉛ガラスで鋳造された地下の「骨硝子（ボーン・ガラス）」納骨堂が一体化した建築空間です。

| マテリアル系統 | カラーToken | Three.js `r185` TSL 手続き型シェーダー・ジオメトリ仕様 |
| :--- | :--- | :--- |
| **深淵タイドスレート（Abyssal Tide Slate）** | `#070B10` | 潮位ハイトマップと濡れた塩結晶のスペキュラを持つ柱状玄武岩 |
| **塩霜玄武岩（Salt-Frosted Basalt）** | `#16202A` | Voronoi結晶ノイズによる法線摂動を伴う構造リブ |
| **獣脂アンバー（Tallow Amber）** | `#C89B54` | 2100Kの防風ランタン光錐。シャッター開閉と油量減衰カーブに連動 |
| **ハロゲン化銀シアン（Silver-Halide Cyan）** | `#4FA89B` | 骨硝子の屈折分散（`ior: 1.54`）およびフェロタイプUV閃光のネガ反転ハイライト |
| **動脈ラスト（Arterial Rust）** | `#B8423A` | 水門鎖、封蝋、および高Exposure時の危険警告ビネット |

*パレットガードレール*：汎用AIパープル（`#7567F5`）および高彩度ネオンマゼンタは、手続き型シェーダー、UIオーバーレイ、骨硝子の屈折コースティクスを含め全面的に使用禁止です。

---

## 3. 10ビート調査進行ルート（`case_saint_vane`）

| ビート | 空間エリア | 鑑識目標およびメカニカルゲート |
| ---: | :--- | :--- |
| **01** | **潮汐堤道（`Tidewater Causeway`）** | 暴風雨の桟橋に着岸。ハイドロフォン足音計測、`Lantern Shutter`（`6 ticks`開閉）、ランタン油消費を較正 |
| **02** | **管理人剥離室（`Caretaker's Stripping Room`）** | 安全ハブ。6ノード推理ボード（`Inquest Board`）を確認し、管理人Moreauの蝋管（`case_saint_vane`）を再生 |
| **03** | **前室較正エリア（`Vestibule Threshold`）** | `銀塩フェロタイプ乾板カメラ`（`19..24 ticks` UV閃光判定、半径`6.5 m`以内に`150 ticks`スタン）のチュートリアル |
| **04** | **屈折回廊（`Refraction Gallery`）** | ランタンのシャッター制御で `Glass Septum Watcher` の視線錐を回避し、`二焦点真鍮ルーペ`（`75 ticks`）で微細刻印を解析 |
| **05** | **プリズム三角測量（`Prism Triangulation`）** | 3連フレネルレンズ環（`45 deg` / `135 deg` / `270 deg`）の角度を合わせ、『潮汐台帳の断片』（`Tide Ledger Fragment`）を回収 |
| **06** | **水没地下聖堂（`Submerged Crypt`）** | 膝丈の浸水路で `Mire Listener` と `Drowned Chorister` に対処しつつ、`110/220/330 Hz`の水門共振器を蓄音機で同調し『水中聴音蝋管』を回収 |
| **07** | **推理ボード結論（`Inquest Board Deduction`）** | 6つの証拠品を結び、3つの仮説（`lens_sabotage` / `tidal_quarantine` / `acoustic_calling`）から1つをロック |
| **08** | **納骨堂解封（`Ossuary Unsealing`）** | 『サン＝ヴァーヌ主封印』で音響隔壁を開放し、最深部の骨硝子大聖堂へ降下 |
| **09** | **硝子の納骨堂（`The Glass Ossuary`）** | 二段階ボス **`硝子の中の聖歌隊`（`The Choir in the Glass`、`600 Resonance Integrity`）** との対決 |
| **10** | **記録電信室（`Archive Telegraph`）** | `VERDICT_PUBLISH` または `VERDICT_SUBMERGE` を選択し、バージョン管理されたセーブデータへ永続化 |

---

## 4. 60 Hz 決定論的鑑識器具・ステルスフレーム表

すべてのアクションは60 Hz整数ティック（`1 tick = 16.6667 ms`）で処理されます。光学的可視状態（`LANTERN_OPEN` / `LANTERN_SHUTTERED`）と音響逆位相マスキング（`PHONOGRAPH_CANCEL_ACTIVE`）は直交するビットマスクチャネルとして実装され、ランタンのシャッター開閉が蓄音機の消音フィールドを上書きしてしまう不具合を構造的に防ぎます。

<div align="center">
  <img src="../assets/svg/game-02-telemetry-ja.svg" width="100%" alt="『硝子の納骨堂』60 Hz 鑑識器具フレームタイムライン・カラーパレット・音響閾値" />
</div>

| アクション | 発生（Startup） | 持続（Active Window） | 硬直（Recovery） | 合計フレーム | リソース消費・メカニカル効果 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **ランタンシャッター（`Lantern Shutter`）** | `6 ticks` | トグル（`7..`） | `6 ticks` | `12 ticks` | `油消費 0`。光錐を遮断し、光学視線ヘイトを即座に切る |
| **真鍮ルーペ焦点（`Brass Loupe Focus`）** | `9 ticks` | ホールド（`10..69`） | `6 ticks` | `75 ticks` | `油消費 0`。プリズム刻印および骨硝子の微細亀裂を解読 |
| **蓄音機逆位相消音（`Phonograph Cancel`）** | `24 ticks` | `Ticks 25..114` | `36 ticks` | `150 ticks` | 室内の不協和共鳴を相殺し、`Mire Listener` から足音デシベルを隠蔽 |
| **フェロタイプ閃光（`Ferrotype Flash`）** | `18 ticks` | `Ticks 19..24` | `66 ticks` | `90 ticks` | 隠し継ぎ目を露光。半径`6.5 m`以内の怪異を`150 ticks`スタン |
| **しゃがみサイドステップ（`Crouch Sidestep`）** | `5 ticks` | `Ticks 6..16` | `12 ticks` | `28 ticks` | 水場や鉄格子上での足音ノイズを `<= -38 dBFS` に抑制 |
| **樟脳嗅ぎ塩（`Smelling Salts`）** | `15 ticks` | `Ticks 16..45` | `10 ticks` | `55 ticks` | `Composure +40` 回復、`Exposure -25` 浄化 |

---

## 5. 怪異生態と二段階ボス：硝子の中の聖歌隊（The Choir in the Glass）

### 3種の怪異アーキタイプ
1. **泥濘の聴取者（`Mire Listener`）**：視覚を持たない水陸両生の音響捕食者。水しぶきや足音、無防備な蓄音機のゼンマイ音が `-28 dBFS` を超えた地点へ高速突進します。
2. **硝子隔壁の監視者（`Glass Septum Watcher`）**：回転するフレネルガラス隔壁の内部に封じられた屈折シルエット。開放されたランタン光錐または直視界に入った時のみ接近し、シャッターを閉じると静止します。
3. **溺死聖歌隊員（`Drowned Chorister`）**：半径`4.5 m`の低周波ハミング領域を纏う亡霊。`Wax-Cylinder Phonograph` の逆位相再生で中和しない限り、持続的に `Composure` を削り `Exposure` を蓄積させます。

### 二段階ボス：硝子の中の聖歌隊（`The Choir in the Glass`、`600 Resonance Integrity`）
- **造形構造**：全高約`5.2 m`の骨硝子パイプオルガンと潮汐ベルジャーの複合体。7体の聖歌隊シルエットがハロゲン化銀の心臓部を取り囲んでいます。
- **第1フェーズ（`600 -> 301 Integrity`）**：`Refractive Blind`（プリズム掃射。ランタン遮光と柱への退避が必須）、`Tidal Undertow`（足元の引き波）、`Shatter Harmonic`（床面ガラス棘の予兆攻撃）、`Hollow Hymn`（大合唱衝撃波）を使用。`Hollow Hymn` に合わせて蓄音機の逆位相（`ticks 25..114`）を重ねると、中央共鳴核が `150 ticks` 露出します。
- **第2フェーズ（`300 -> 0 Integrity`）**：外殻ベルジャーが割れ、3枚の回転フレネルミラーが周囲を周回。`Prism Split`、`Glass Lung Vacuum`、`Echoing Verdict`、`Final Exposure` が追加されます。逆位相消音で音響障壁を剥がした直後に `6.5 m` 以内へ踏み込み、`Silver-Salt Ferrotype Plate` のUV閃光（`ticks 19..24`）を叩き込むことで3つの共鳴封印を破砕します。

---

## 6. 6ノード推理ボードと3つの仮説ブランチ

ビート07（`Inquest Board Deduction`）で6つの物証を結線すると、`GraphState.active_relic` に格納される3つの仮説から1つを選択・確定できます。

- **`レンズ破壊工作`（`lens_sabotage`）**：灯台のフレネルレンズが蒸気船メリディアン号を座礁させるため意図的に狂わされていたと立証。`Brass Loupe` の解析距離が `+35%` 拡大し、`Ferrotype Flash` のスタン持続が `+30 ticks` 延長されます。
- **`潮汐隔離封鎖`（`tidal_quarantine`）**：管理人Moreauが音響汚染の拡散を防ぐため自ら地下聖堂を水没させたと立証。浸水エリアでの `Exposure` 蓄積が `-30%` 軽減され、ランタン油の消費効率が `+25%` 向上します。
- **`音響招魂共鳴`（`acoustic_calling`）**：骨硝子リブが溺死者の周波数を受信・増幅する音響変換器として設計されたと立証。`Wax-Cylinder Phonograph` の逆位相持続ウィンドウが `+24 ticks` 拡張され、ボスに対する共鳴破壊ダメージが `+20%` 増加します。

---

## 7. スタンドアロンプロンプト・JSON Schema・ゴールデンフィクスチャ

- **マスターオーケストレータープロンプト**：[`prompts/glass-ossuary/orchestrator.md`](../prompts/glass-ossuary/orchestrator.md)（[`orchestration/prompts/glass-ossuary-orchestrator.md`](../orchestration/prompts/glass-ossuary-orchestrator.md) にミラー配置）
- **7枚の専門サブエージェントカード**：[`prompts/glass-ossuary/agents/`](../prompts/glass-ossuary/agents/)
- **ゴールデン検証フィクスチャ（`run-0002`）**：[`examples/run-0002/task-packet.json`](../examples/run-0002/task-packet.json)、[`examples/run-0002/defect-record.json`](../examples/run-0002/defect-record.json)、[`examples/run-0002/run-manifest.json`](../examples/run-0002/run-manifest.json)
- **シリーズ全4巻コンパニオンガイド**：
  - [`docs/EVIDENCE_GRAPH_GUIDE.ja.md`](EVIDENCE_GRAPH_GUIDE.ja.md)（『Three.js Evidence Graph v2.0 運用マニュアル』、全64頁）
  - [`docs/THE_HOLLOW_MERIDIAN_GUIDE.ja.md`](THE_HOLLOW_MERIDIAN_GUIDE.ja.md)（『虚ろの子午線 v1.0』、全81頁）
  - [`docs/PERIHELION_BREACH_GUIDE.ja.md`](PERIHELION_BREACH_GUIDE.ja.md)（『ペリヘリオン・ブリーチ v1.0』、全36頁）
