# Multilingual Technical Glossary

English terms remain canonical. English is normative for identifiers, schema keys, CLI commands, and file paths. Explanatory prose across `README*.md` and `docs/*_GUIDE*.md` uses natural, idiomatic terminology in English (`en`), Simplified Chinese (`zh-CN`), Japanese (`ja`), and Korean (`ko`).

## Core Control Plane & Three.js r185 Architecture Terms

| English (`en`) | 简体中文 (`zh-CN`) | 日本語 (`ja`) | 한국어 (`ko`) |
| :--- | :--- | :--- | :--- |
| Evidence Graph | 证据图谱 | エビデンスグラフ | 에비던스 그래프 / 증거 그래프 |
| vertical slice | 垂直切片 | バーティカルスライス | 버티컬 슬라이스 |
| product contract | 产品契约 | プロダクト契約 | 제품 계약 |
| control plane | 控制平面 | 制御プレーン / コントロールプレーン | 제어 평면 / 제어 계층 |
| bounded specialist | 权限受限的专家智能体 | 権限分離された専門サブエージェント | 작업 범위가 격리된 전담 서브에이전트 |
| task packet (`TaskPacket`) | 任务包 (`TaskPacket`) | タスクパケット (`TaskPacket`) | 작업 패킷 (`TaskPacket`) |
| defect record (`DefectRecord`) | 缺陷记录 (`DefectRecord`) | 欠陥記録 (`DefectRecord`) | 결함 기록 (`DefectRecord`) |
| run manifest (`RunManifest`) | 运行清单 (`RunManifest`) | 実行マニフェスト (`RunManifest`) | 실행 매니페스트 (`RunManifest`) |
| graph state (`GraphState`) | 图状态 (`GraphState`) | グラフ状態 (`GraphState`) | 그래프 상태 (`GraphState`) |
| determinism regime (`A-PinnedBrowser` / `B-CrossPlatform`) | 确定性验证体制 (`A-PinnedBrowser` / `B-CrossPlatform`) | 決定論レジーム (`A-PinnedBrowser` / `B-CrossPlatform`) | 결정론 레짐 (`A-PinnedBrowser` / `B-CrossPlatform`) |
| state hash (`state_hash`) | 状态哈希 (`state_hash`) | 状態ハッシュ (`state_hash`) | 상태 해시 (`state_hash`) |
| audio hash (`audio_hash`) | 音频哈希 (`audio_hash`) | 音声ハッシュ (`audio_hash`) | 오디오 해시 (`audio_hash`) |
| geometry hash (`geometry_hash`) | 几何顶点哈希 (`geometry_hash`) | ジオメトリハッシュ (`geometry_hash`) | 지오메트리 해시 (`geometry_hash`) |
| Three.js Shading Language (TSL) | Three.js 着色器语言 (TSL) | Three.js シェーディング言語 (TSL) | Three.js 셰이딩 언어 (TSL) |
| WebGPURenderer | WebGPU 渲染器 (`WebGPURenderer`) | WebGPU レンダラー (`WebGPURenderer`) | WebGPU 렌더러 (`WebGPURenderer`) |
| PostProcessing | 节点后处理管线 (`THREE.PostProcessing`) | ノード後処理パイプライン (`THREE.PostProcessing`) | 노드 후처리 파이프라인 (`THREE.PostProcessing`) |
| compileAsync | 异步着色器预编译 (`compileAsync`) | 非同期シェーダー事前コンパイル (`compileAsync`) | 비동기 셰이더 사전 컴파일 (`compileAsync`) |
| InstancedMesh / BatchedMesh | 实例化网格 / 批处理网格 | インスタンス化メッシュ / バッチメッシュ | 인스턴스 메시 / 배치 메시 |
| OfflineAudioContext | 离线音频上下文 (`OfflineAudioContext`) | オフライン音声コンテキスト (`OfflineAudioContext`) | 오프라인 오디오 컨텍스트 (`OfflineAudioContext`) |
| integrated loudness (LUFS) / true peak (dBTP) | 综合响度 (LUFS) / 真峰值 (dBTP) | 統合ラウドネス (LUFS) / トゥルーピーク (dBTP) | 통합 라우드니스 (LUFS) / 트루 피크 (dBTP) |
| fixed-tick simulation (60 Hz) | 60 Hz 固定步进模拟 | 60 Hz 固定ティックシミュレーション | 60 Hz 고정 틱 시뮬레이션 |

## Three Flagship Games - Titles, Protagonists & Genre Mechanics

| Canonical English Term | 简体中文 (`zh-CN`) | 日本語 (`ja`) | 한국어 (`ko`) |
| :--- | :--- | :--- | :--- |
| *The Hollow Meridian* (Game 01 · Action RPG) | 《虚空子午线》 | 『虚ろの子午線』 | 《공허의 자오선》 |
| `The Cartographer` (`Sable Veren`) | 制图师 (`The Cartographer`) | 測量師 (`The Cartographer`) | 측량사 (`The Cartographer`) |
| `The Bell Without a Name` | 无名之钟 (`The Bell Without a Name`) | 名もなき鐘 (`The Bell Without a Name`) | 이름 없는 종 (`The Bell Without a Name`) |
| `Parry` / `Guard` / `Poise` / `Resonance` | 弹反 / 格挡 / 韧性值 / 共鸣值 | パリィ / ガード / 強靭度(体勢値) / 共鳴 | 패링 / 가드 / 강인도 / 공명 |
| Shrine Relic (`brass_vow`, `ash_thread`, `vacant_name`) | 祭坛遗物 (`黄铜誓约` / `灰烬织线` / `空缺真名`) | 聖堂の遺物 (`真鍮の誓約` / `灰の糸` / `空白の真名`) | 제단 유물 (`황동의 서약` / `잿빛 실타래` / `공백의 진명`) |
| *The Glass Ossuary* (Game 02 · Mystery Horror) | 《琉璃骸骨堂》 | 『硝子の納骨堂』 | 《유리 납골당》 |
| `Clara Vane` (`The Acoustic Archivist`) | 声学档案调查员 `Clara Vane` | 音響記録保管官 `Clara Vane` | 음향 기록 보관관 `Clara Vane` |
| `The Choir in the Glass` | 玻璃圣咏团 (`The Choir in the Glass`) | 硝子の中の聖歌隊 (`The Choir in the Glass`) | 유리 속의 성가대 (`The Choir in the Glass`) |
| `Composure` / `Lantern Oil` / `Exposure` | 定力 / 提灯鲸油 / 精神侵蚀度 | 平常心 (`Composure`) / ランタン鯨油 / 精神侵蝕度 (`Exposure`) | 침착성 (`Composure`) / 랜턴 오일 / 정신 침식도 (`Exposure`) |
| `Split-Diopter Brass Loupe` | 双焦黄铜放大镜 | 二焦点真鍮ルーペ | 이중 초점 황동 루페 |
| `Wax-Cylinder Phonograph` | 蜡筒留声机（反相消音） | 蝋管蓄音機（逆位相消音） | 밀랍 실린더 축음기 (역위상 상쇄) |
| `Silver-Salt Ferrotype Plate` | 银盐铁版照相机（紫外闪光） | 銀塩フェロタイプ乾板カメラ | 은염 페로타입 건판 카메라 |
| `Inquest Board` (`lens_sabotage`, `tidal_quarantine`, `acoustic_calling`) | 六节点推理板 (`透镜破坏案` / `潮汐封锁案` / `声学召魂案`) | 6ノード推理ボード (`レンズ工作説` / `潮汐隔離説` / `音響招魂説`) | 6노드 추리 보드 (`렌즈 사보타주 가설` / `조수 격리 가설` / `음향 강령 가설`) |
| *Perihelion Breach* (Game 03 · FPS Adventure) | 《近日点破袭》 | 『ペリヘリオン・ブリーチ』 | 《근일점 돌파》 |
| `Soren Kestrel` & `Station AI Vesper` | 先锋官 `Soren Kestrel` 与战术 AI `Vesper` | 先遣隊員 `Soren Kestrel` ＆ 戦術AI `Vesper` | 선봉대원 `Soren Kestrel` & 전술 AI `Vesper` |
| `The Heliarch Warden` | 日冕典狱长 (`The Heliarch Warden`) | ヘリアーク・ウォーデン (`The Heliarch Warden`) | 헬리아크 워든 (`The Heliarch Warden`) |
| `Shield` / `Hull Integrity` / `Core Heat` | 能量护盾 / 装甲完整度 / 核心热量 | シールド / 装甲耐久値 / コア熱量 | 에너지 실드 / 장갑 무결성 / 코어 열량 |
| `Thermal Vent Reload` (`ticks 14..20`) | 主动散热装填 (`ticks 14..20`) | サーマルベント・リロード (`ticks 14..20`) | 액티브 방열 재장전 (`ticks 14..20`) |
| `Magnetic Grapple` / `Slide-Boost` | 磁力抓钩摆荡 / 滑铲推进 | マグネティック・グラップル / スライドブースト | 자기 그래플 슬링샷 / 슬라이드 부스트 |
| Exo-Rig Core (`recoil_gyro`, `thermal_siphon`, `grapple_overdrive`) | 外骨骼核心 (`陀螺仪制退核心` / `热能虹吸核心` / `抓钩超载核心`) | Exo-Rigコア (`反動制御ジャイロ` / `熱エネルギーサイフォン` / `グラップル・オーバードライブ`) | 엑소 리그 코어 (`반동 제어 자이로` / `열에너지 사이펀` / `그래플 오버드라이브`) |

## Proper Nouns & Canonical Identifiers Retained in English

Code identifiers, beat IDs, zone IDs, enemy IDs, schema keys, and CLI commands remain in English across all four language editions (with native localized titles or explanations provided alongside):

- **Core**: `Three.js`, `WebGPU`, `WebGL 2`, `TSL`, `Three.js Evidence Graph`
- **Game 01 (*The Hollow Meridian*)**: `The Hollow Meridian`, `The Cartographer`, `The Bell Without a Name`, `Mnemonic Keeper`, `Ash Court`, `Orrery Bridge`, `Archive Nave`, `Bell Foundry`, `Meridian Chamber`, `North Seal`, `Depth Seal`, `Echo Lantern`, `Echo Brand`, `Ashbound Skirmisher`, `Lantern Wraith`, `Bell Sentinel`, `brass_vow`, `ash_thread`, `vacant_name`
- **Game 02 (*The Glass Ossuary*)**: `The Glass Ossuary`, `Clara Vane`, `Caretaker Moreau`, `The Choir in the Glass`, `Tidewater Causeway`, `Caretaker's Stripping Room`, `Refraction Gallery`, `Submerged Crypt`, `Split-Diopter Brass Loupe`, `Wax-Cylinder Phonograph`, `Silver-Salt Ferrotype Plate`, `Mire Listener`, `Glass Septum Watcher`, `Drowned Chorister`, `lens_sabotage`, `tidal_quarantine`, `acoustic_calling`
- **Game 03 (*Perihelion Breach*)**: `Perihelion Breach`, `Soren Kestrel`, `Station AI Vesper`, `Icarus-9`, `The Heliarch Warden`, `Umbilical Airlock`, `Heliostat Truss`, `Cryo-Coolant Manifold`, `Ballistic Foundry`, `Perihelion Core Chamber`, `Kestrel-9 Twin-Coil Carbine`, `Helios Scatter-Rail`, `Arc-Vane Breach Launcher`, `Volt Skitter`, `Aegis Drone`, `Slag Enforcer`, `recoil_gyro`, `thermal_siphon`, `grapple_overdrive`
