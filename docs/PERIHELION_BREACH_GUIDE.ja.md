<!-- source_version: 2026.07.5; translation_status: reviewed; language: ja -->

# 『ペリヘリオン・ブリーチ』（Perihelion Breach）：FPSアドベンチャー開発仕様・設計ガイド

| **MONOGRAPH EDITIONS** | [**English**](PERIHELION_BREACH_GUIDE.md) | [**简体中文**](PERIHELION_BREACH_GUIDE.zh-CN.md) | [**日本語**](PERIHELION_BREACH_GUIDE.ja.md) | [**한국어**](PERIHELION_BREACH_GUIDE.ko.md) |
| :--- | :---: | :---: | :---: | :---: |
| **VOLUME COLOPHON** | `第四巻 · 36頁 · ゲーム 03：一人称SFシューター・アドベンチャー『ペリヘリオン・ブリーチ』 · SEED 2142` | [Normative PDF](../publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf) | [Master Folio](../README.ja.md) | `Three.js r185 · Zero External Assets` |

| 第四巻モノグラフ表紙 (36頁) | 図版 IV-1：0.09 AU イカロス9号ヘリオスタット主トラス | 図版 IV-2：極低温冷却マニホールドと排熱リロード | 図版 IV-3：ヘリアーク・ウォーデン決戦 (1,000 Int.) |
| :---: | :---: | :---: | :---: |
| [![第四巻モノグラフ表紙 (36頁)](../assets/perihelion-breach-cover.jpg)](../publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf) | ![図版 IV-1：0.09 AU イカロス9号ヘリオスタット主トラス](../assets/perihelion-breach-world-hero.jpg) | ![図版 IV-2：極低温冷却マニホールドと排熱リロード](../assets/perihelion-breach-arsenal-hero.jpg) | ![図版 IV-3：ヘリアーク・ウォーデン決戦 (1,000 Int.)](../assets/perihelion-breach-combat-hero.jpg) |

> **ガイドの位置づけ**
>
> 本書は『Perihelion Breach: FPS Adventure Full Multi-Agent Production Prompt v1.0』（[`publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf`](../publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf)、全36頁、`95,265` バイト、SHA-256 `75bdfff21c905122b4e1a0352e8c760c27e7c80cf8c3d5dcad63ea2263f89170`）の日本語ネイティブ技術解説書です。一人称視点SFシューター・アドベンチャー（FPS Adventure）バーティカルスライスにおける60 Hz弾道・グラップル機動フレーム表、アクティブ排熱リロード、Exo-Rigコア分岐、二段階ボス設計、および Evidence Graph v2.0 検証ゲートを規定します。本リポジトリは設計仕様書およびマルチエージェント用プロンプト群を提供するものであり、実行可能なゲームビルドそのものではありません。

---

## 1. 仕様書の概要とコア設計思想

『ペリヘリオン・ブリーチ』（*Perihelion Breach*）は、*Three.js Evidence Graph* スイートにおける**ファーストパーソン・シューター・アドベンチャー（FPS Adventure）**領域のフラッグシップ仕様書です。Three.js `r185`（`0.185.0`）環境において、**外部バイナリアセットのダウンロードを一切行わず**（`.glb`モデル、外部テクスチャ、フォント、録音済み音声ファイル不使用）、リポジトリ内のコードとシード値のみから**プレイ時間12〜15分**のハイスピードSFシューター・アドベンチャーを構築するための制作契約を定義しています。

**60 Hz固定ティックの精密な銃撃戦**と、**磁気グラップルおよび導管ルーティングによる立体的な空間踏破**を融合させています。

- **想定プレイ時間**：12〜15分（太陽から`0.09 AU`の近日点軌道を周回する「イカロス9号」の5つの軌道セクター）。
- **主人公**：**Soren Kestrel**（リレー・ヴァンガード / `The Relay Vanguard`）。戦術AI **Vesper** のテレメトリ支援を受け、**`100 Shield（シールド）`**、**`100 Hull Integrity（装甲耐久度）`**、**`0–100 Core Heat（コア熱量）`** を管理。
- **3種の多機能ウェポン＆踏破ツール**：`Kestrel-9 ツインコイル・カービン`（`coil_carbine`、サブ射撃で `Magnetic Grapple Tether` を射出）、`ヘリオス・スキャッターレール`（`scatter_rail`）、`アークヴェイン・ブリーチランチャー`（`breach_launcher`）。
- **アクティブ排熱リロード（Thermal Vent Reload）＆グラップル運動学**：`36 ticks`のリロード中、`ticks 14..20`のウィンドウ内で再入力すると `Core Heat` を `100%` パージし、`90 ticks` のオーバーチャージ火力を獲得。上半身の銃器リロードタイマーと下半身の `Slide-Boost`（`11.5 m/s`）・`Magnetic Grapple`（`18.0 m/s`）は完全に分離（デカップリング）されています。
- **スーツリグ較正（Suit Rig Calibration）**：3つの排他的Exo-Rigコア（`リコイルジャイロ`、`サーマルサイフォン`、`グラップルオーバードライブ`）から1つを装着。
- **3種の機械兵（Synths）と二段階ボス**：`ボルト・スキッター`（`Volt Skitter`）、`イージス・ドローン`（`Aegis Drone`）、`スラグ・エンフォーサー`（`Slag Enforcer`）、および最深部ボス **`ヘリアーク・ウォーデン`（`The Heliarch Warden`、`1,000 Armor Integrity`）**。
- **2つの軌道ディレクティブ結末**：`DIRECTIVE_DIVERT`（ヘリオスタット鏡群を固定して地球側グリッドを防衛）または `DIRECTIVE_VENT`（炉心をパージして乗員脱出艇を射出）。

---

## 2. 世界観と手続き型マテリアル設計

舞台は太陽コロナの極限放射に晒される**イカロス9号（Icarus-9）太陽中継メガストラクチャー**。`5800K`の強烈なコロナ光、真空の鋭い影、そして青白いチェレンコフ冷却光が交錯します。外部セクターでは `240 ticks`（4秒）周期で太陽フレアが掃射され、ブラストシャッターが落とすハードシャドウの回廊をグラップルとスライディングで駆け抜けます。

| マテリアル系統 | カラーToken | Three.js `r185` TSL 手続き型シェーダー・ジオメトリ仕様 |
| :--- | :--- | :--- |
| **バキュームカーボン（Vacuum Carbon）** | `#090D14` | 異方性カーボン織り法線を持つ微小隕石防護マットパネル |
| **オービタルチタン（Orbital Titanium）** | `#1A2433` | ヘアライン加工された構造トラス、防爆シャッター、銃器レシーバー |
| **コロナアンバー（Corona Amber）** | `#F08A24` | カプトン金箔ヘリオスタット反射鏡および太陽フレア熱線予兆 |
| **チェレンコフシアン（Cherenkov Cyan）** | `#38C6D9` | 電離レールスラッグ軌跡、極低温冷却導管、アクティブ排熱アーク |
| **オーバーヒートプラズマレッド（Overheat Plasma Red）** | `#E54848` | コア過熱警報（`>= 85 Heat`）、敵の排熱弱点ベント、迫撃砲弾道 |

*パレットガードレール*：汎用AIパープル（`#7567F5`）および高彩度ネオンマゼンタは、手続き型シェーダー、戦術HUDレティクル、プラズマエフェクトを含め全面的に使用禁止です。

---

## 3. 10ビート軌道ミッション進行ルート（`restore_perihelion_attitude`）

| ビート | 軌道セクター | 戦術目標および空間アドベンチャーゲート |
| ---: | :--- | :--- |
| **01** | **アンビリカル・エアロック（`Umbilical Airlock`）** | 無重力ドッキングスパインへ接続。戦術AI `Vesper` を起動し、`Kestrel-9 ツインコイル・カービン` を装備 |
| **02** | **エアロックスパイン（`Airlock Spine`）** | 電磁クランプを破砕し、`Slide-Boost`（`24 ticks`）と `Thermal Vent Reload`（`ticks 14..20`）を較正 |
| **03** | **ヘリオスタット・トラス（`Heliostat Truss`）** | `240-tick` 周期の太陽フレアを避けつつ外部ミラー歩道を踏破。`Volt Skitter` 群を迎撃し `Magnetic Grapple` を解放 |
| **04** | **クライオ冷却マニホールド（`Cryo-Coolant Manifold`）** | `Aegis Drone` の狙撃をかわしながらグラップルスリングで垂直タービンシャフトを上昇し、`Arc-Vane Breach Launcher` を入手 |
| **05** | **導管フェーズルーティング（`Conduit Phase Routing`）** | `180 ticks` の減衰制限時間内に3つのプラズマアンカーを射ち込み、『冷却バイパスコア』（`Coolant Bypass Core`）を回収 |
| **06** | **バリスティック鋳造所（`Ballistic Foundry`）** | 多層るつぼアリーナで重装 `Slag Enforcer` を撃破し、`Helios Scatter-Rail` と『点火キーカード』を確保 |
| **07** | **スーツリグ較正ベンチ（`Suit Rig Calibration`）** | 3種のExo-Rigコア（`recoil_gyro` / `thermal_siphon` / `grapple_overdrive`）から1つを実装 |
| **08** | **コロナ防爆シャッター（`Corona Blast Shutter`）** | 太陽コロナに面した主タングステン隔壁を収納し、`Perihelion Core Chamber` へ突入 |
| **09** | **ペリヘリオン・コアチャンバー（`Perihelion Core Chamber`）** | 二段階ボス **`ヘリアーク・ウォーデン`（`The Heliarch Warden`、`1,000 Armor Integrity`）** を撃破 |
| **10** | **姿勢制御ブリッジ（`Attitude Control Bridge`）** | `DIRECTIVE_DIVERT` または `DIRECTIVE_VENT` を実行し、セーブデータとテレメトリログを確定 |

---

## 4. 60 Hz 決定論的ウェポン・排熱・グラップルフレーム表

すべての射撃レート、チャージ時間、アクティブリロード判定、移動インパルスは60 Hz整数ティック（`1 tick = 16.6667 ms`）で動作します。上半身のリロード進行カウンタは下半身のグラップル離脱やスライディング遷移から独立しており、空中機動中の排熱リロードが不発にならない設計です（`FPS-N06A-COMBAT-019`）。

<div align="center">
  <img src="../assets/svg/game-03-telemetry-ja.svg" width="100%" alt="『ペリヘリオン・ブリーチ』60 Hz 銃器・排熱リロード・グラップルフレームタイムライン・カラーパレット" />
</div>

| アクション | 発生（Startup） | 持続・受付（Active） | 硬直（Recovery） | 合計フレーム | 熱量・ダメージ・メカニカル効果 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **カービン3点バースト（`Carbine 3-Burst`）** | `2 ticks` | `Ticks 3..11`（3発） | `10 ticks` | `21 ticks` | `+12 Heat`、`3 x 14 dmg` ヒットスキャン（弱点倍率 `1.5x`） |
| **スキャッター腰だめ（`Scatter Uncharged`）** | `3 ticks` | `Tick 4`（`5x12`拡散） | `15 ticks` | `18 ticks` | `+18 Heat`、`60 dmg` 近距離拡散フレシェット。シールド剥離に有効 |
| **スキャッターADSレール弾（`Scatter ADS Slug`）** | `30..54 ticks` | `Tick 31..55` | `18 ticks` | `48..72 ticks` | `+28 Heat`、`55..85 dmg` 貫通電磁スラッグ（弱点倍率 `1.75x`） |
| **ブリーチアンカー射出（`Breach Anchor`）** | `6 ticks` | 放物線弾道飛行 | `24 ticks` | `30 ticks` | `+30 Heat`、`60 AoE dmg` 重装甲破砕・パズル導管リンク |
| **アクティブ排熱リロード（`Thermal Vent Reload`）** | `13 ticks` | `Ticks 14..20` | `16 ticks` | `36 ticks` | `14..20t` の入力成功で `100% Heat` 消去＋`90t` オーバーチャージ |
| **スライドブースト（`Slide-Boost`）** | `3 ticks` | `Ticks 4..18` | `6 ticks` | `24 ticks` | `11.5 m/s` 低姿勢スライディング。`ticks 8..18` でジャンプキャンセル可 |
| **磁気グラップル（`Magnetic Grapple`）** | `6 ticks` | `18..42 ticks` 牽引 | `12 ticks` | `36..60 ticks` | `18.0 m/s` アンカー牽引。離脱時に接線スリング運動量を保持 |

---

## 5. エネミー編成と二段階ボス：ヘリアーク・ウォーデン（The Heliarch Warden）

### 3種の機械兵（Synth）アーキタイプ
1. **ボルト・スキッター（`Volt Skitter`）**：壁面やトラス梁を疾走する四脚保守シンス（`90 Hull`、移動速度`6.8 m/s`）。遮蔽物に隠れたプレイヤーを炙り出します。
2. **イージス・ドローン（`Aegis Drone`）**：前方指向性エネルギーシールドを展開する浮遊狙撃機（`140 Hull + 80 Shield`）。グラップルで側背面へ回り込むか、`Scatter-Rail` の拡散射撃でシールドを過負荷させて撃破します。
3. **スラグ・エンフォーサー（`Slag Enforcer`）**：溶融スラグ迫撃砲を撃ち出す重装フレーム（`320 Hull`）。砲撃直後の `90 ticks` 間、背面の『冷却スパイン（`Coolant Spine`）』弱点（`1.75x`）が露出します。

### 二段階ボス：ヘリアーク・ウォーデン（`The Heliarch Warden`、`1,000 Armor Integrity`）
- **造形構造**：回転する反応炉ジンバルの中央に吊り下げられた全高`6.0 m`のジャイロスコープ太陽核オートマトン。4枚の可動ヘリオスタット翼と磁気グラップルリングを備えています。
- **第1フェーズ（`1,000 -> 501 Integrity`）**：`Solar Sweep Beam`（水平コロナレーザー。`Slide-Boost` でのくぐり抜け、またはグラップル跳躍で回避）、`Grapple Pylon Drop`（磁気アンカー投下）、`Cluster Mortar`、`Radiant Pulse`（直後に背面 `Core Vent` 弱点が `150 ticks` 露出）を実行。
- **第2フェーズ（`500 -> 0 Integrity`）**：床面シャッターが開放され直下の太陽プラズマが露出。逆回転する3連キャットウォークリング間をグラップルで飛び移りながら戦う空中機動フェーズへ移行します。`Coronal Ejection`、`Rotating Mirror Ring`、`Rail Volley`、`Perihelion Collapse`（直後に中央 `Core Vent` が `150 ticks` 露出）が追加されます。

---

## 6. スーツリグ較正：3つのExo-Rigコア分岐

ビート07（`Suit Rig Calibration`）のエンジニアリングベンチにて、`GraphState.active_relic` に記録される3つのExo-Rigコアから1つを装着します。

- **`リコイルジャイロ`（`recoil_gyro`）**：銃器の反動キックを `-45%` 抑制し、`Scatter-Rail` 腰だめ拡散角を `-25%` 縮小、さらに弱点ヒット倍率を `1.5x` から `1.85x` へ引き上げます。
- **`サーマルサイフォン`（`thermal_siphon`）**：`Thermal Vent Reload` の成功受付ウィンドウを `ticks 14..20`（7フレーム）から `ticks 12..23`（12フレーム）へ拡張し、排出した熱量を `+25 Shield` のオーバーシールドへ変換します。
- **`グラップルオーバードライブ`（`grapple_overdrive`）**：`Magnetic Grapple` の牽引速度を `18.0 m/s` から `22.5 m/s` へ加速し、クールダウンを `-35%` 短縮、グラップルキック着弾時にEMP衝撃波を発生させます。

---

## 7. スタンドアロンプロンプト・JSON Schema・ゴールデンフィクスチャ

- **マスターオーケストレータープロンプト**：[`prompts/perihelion-breach/orchestrator.md`](../prompts/perihelion-breach/orchestrator.md)（[`orchestration/prompts/perihelion-breach-orchestrator.md`](../orchestration/prompts/perihelion-breach-orchestrator.md) にミラー配置）
- **7枚の専門サブエージェントカード**：[`prompts/perihelion-breach/agents/`](../prompts/perihelion-breach/agents/)
- **ゴールデン検証フィクスチャ（`run-0003`）**：[`examples/run-0003/task-packet.json`](../examples/run-0003/task-packet.json)、[`examples/run-0003/defect-record.json`](../examples/run-0003/defect-record.json)、[`examples/run-0003/run-manifest.json`](../examples/run-0003/run-manifest.json)
- **シリーズ全4巻コンパニオンガイド**：
  - [`docs/EVIDENCE_GRAPH_GUIDE.ja.md`](EVIDENCE_GRAPH_GUIDE.ja.md)（『Three.js Evidence Graph v2.0 運用マニュアル』、全64頁）
  - [`docs/THE_HOLLOW_MERIDIAN_GUIDE.ja.md`](THE_HOLLOW_MERIDIAN_GUIDE.ja.md)（『虚ろの子午線 v1.0』、全81頁）
  - [`docs/THE_GLASS_OSSUARY_GUIDE.ja.md`](THE_GLASS_OSSUARY_GUIDE.ja.md)（『硝子の納骨堂 v1.0』、全36頁）
