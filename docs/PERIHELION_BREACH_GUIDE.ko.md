<!-- source_version: 2026.07.5; translation_status: reviewed; language: ko -->

# 《근일점 돌파》(Perihelion Breach): FPS 어드벤처 개발 규격 및 아키텍처 가이드

| **MONOGRAPH EDITIONS** | [**English**](PERIHELION_BREACH_GUIDE.md) | [**简体中文**](PERIHELION_BREACH_GUIDE.zh-CN.md) | [**日本語**](PERIHELION_BREACH_GUIDE.ja.md) | [**한국어**](PERIHELION_BREACH_GUIDE.ko.md) |
| :--- | :---: | :---: | :---: | :---: |
| **VOLUME COLOPHON** | `제4권 · 36페이지 · 게임 03: 1인칭 SF 슈터 어드벤처 《근일점 돌파》 · SEED 2142` | [Normative PDF](../publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf) | [Master Folio](../README.ko.md) | `Three.js r185 · Zero External Assets` |

| 제4권 모노그래프 표지 (36P) | 도판 IV-1: 0.09 AU 이카루스-9 헬리오스탯 트러스 | 도판 IV-2: 극저온 냉각 매니폴드 & 능동 방열 재장전 | 도판 IV-3: 헬리아크 워든 공중 보스전 (1,000 무결성) |
| :---: | :---: | :---: | :---: |
| [![제4권 모노그래프 표지 (36P)](../assets/perihelion-breach-cover.jpg)](../publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf) | ![도판 IV-1: 0.09 AU 이카루스-9 헬리오스탯 트러스](../assets/perihelion-breach-world-hero.jpg) | ![도판 IV-2: 극저온 냉각 매니폴드 & 능동 방열 재장전](../assets/perihelion-breach-arsenal-hero.jpg) | ![도판 IV-3: 헬리아크 워든 공중 보스전 (1,000 무결성)](../assets/perihelion-breach-combat-hero.jpg) |

> **문서 위상 안내**
>
> 본 문서는 《Perihelion Breach: FPS Adventure Full Multi-Agent Production Prompt v1.0》([`publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf`](../publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf), 총 36쪽, `95,265` 바이트, SHA-256 `75bdfff21c905122b4e1a0352e8c760c27e7c80cf8c3d5dcad63ea2263f89170`)의 한국어 네이티브 기술 가이드입니다. 1인칭 SF 슈팅 어드벤처(FPS Adventure) 버티컬 슬라이스의 60 Hz 탄도학 및 자기 그래플 기동 프레임 테이블, 액티브 방열 재장전(Thermal Vent Reload), 엑소 리그 코어 분기, 2페이즈 보스 설계 및 Evidence Graph v2.0 검증 게이트를 다룹니다. 본 저장소는 아키텍처 규격서와 멀티 에이전트 프롬프트 패키지를 제공하며, 실행 가능한 런타임 게임 빌드는 아직 포함하지 않습니다.

---

## 1. 규격서 개요 및 핵심 설계 철학

《근일점 돌파》(*Perihelion Breach*)는 *Three.js Evidence Graph* 스위트의 **1인칭 슈팅 어드벤처(First-Person Shooter Adventure)** 플래그십 규격서입니다. Three.js `r185`(`0.185.0`) 환경에서 **외부 바이너리 에셋 다운로드 없이**(외부 `.glb`, 텍스처, 폰트, 사전 녹음 오디오 파일 무사용) 오직 저장소 내 소스 코드와 시드(Seed)만으로 **플레이 타임 12~15분** 분량의 하이퍼 SF FPS 어드벤처 버티컬 슬라이스를 구축하는 엔지니어링 계약을 정의합니다.

**60 Hz 고정 틱 기반의 정교한 사격 교전**과 **자기 그래플 슬링샷 및 도관 퍼즐을 결합한 입체적 공간 돌파**가 핵심입니다.

- **목표 플레이 시간**: 12~15분 (태양으로부터 `0.09 AU` 근일점 궤도를 도는 ‘이카로스-9’ 스테이션의 5개 궤도 섹터).
- **주인공**: **Soren Kestrel** (릴레이 선봉대원 / `The Relay Vanguard`). 전술 AI **Vesper**의 텔레메트리 지원을 받으며 **`100 실드(Shield)`**, **`100 장갑 무결성(Hull Integrity)`**, **`0–100 코어 열량(Core Heat)`**을 관리합니다.
- **3종의 복합 화기 및 기동 장비**: `Kestrel-9 트윈코일 카빈`(`coil_carbine`, 보조 사격으로 `자기 그래플 테더` 발사), `헬리오스 스캐터-레일`(`scatter_rail`), `아크-베인 브리치 런처`(`breach_launcher`).
- **액티브 방열 재장전(Thermal Vent Reload) 및 그래플 운동학**: `36 ticks` 재장전 동작 중 `ticks 14..20` 구간에 재입력하면 `코어 열량`을 `100%` 배출하고 `90 ticks` 동안 이온 과충전 화력 버프를 획득합니다. 상체 무기 재장전 타이머는 하체 `슬라이드 부스트`(`11.5 m/s`) 및 `자기 그래플`(`18.0 m/s`) 상태와 완전히 분리되어 공중 기동 중에도 끊김 없이 작동합니다.
- **수트 리그 보정(Suit Rig Calibration)**: 3가지 상호 배타적 엑소 리그 코어(`반동 자이로`, `열 사이펀`, `그래플 오버드라이브`) 중 하나를 장착해 반동 제어, 열량 경제, 공중 모멘텀을 재정의합니다.
- **3종의 신스(Synth) 적군 및 2페이즈 보스**: `볼트 스키터`(`Volt Skitter`), `이지스 드론`(`Aegis Drone`), `슬래그 인포서`(`Slag Enforcer`), 그리고 코어 챔버 보스 **`헬리아크 워든`(`The Heliarch Warden`, `1,000 장갑 무결성`)**.
- **2가지 궤도 디렉티브 엔딩**: `DIRECTIVE_DIVERT`(헬리오스탯 미러 어레이를 고정해 지구 방향 전력망 수호) 또는 `DIRECTIVE_VENT`(반응로 코어를 사출해 승무원 구명정 발사).

---

## 2. 세계관 배경 및 절차적 머티리얼 문법

배경은 태양 코로나의 극한 복사에 노출된 **이카로스-9(Icarus-9) 궤도 태양 중계 메가스트럭처**입니다. `5800K`의 눈부신 코로나 백색광, 진공의 날카로운 그림자, 청록색 체렌코프 냉각수 플룸이 강렬한 대비를 이룹니다. 외부 섹터에서는 `240 ticks`(4초) 주기로 태양 플레어가 휩쓸고 지나가며, 플레이어는 방폭 셔터가 드리우는 하드 섀도우 회랑을 따라 그래플과 슬라이딩으로 기동해야 합니다.

| 머티리얼 패밀리 | 컬러 토큰 | Three.js `r185` TSL 절차적 셰이더 및 지오메트리 규격 |
| :--- | :--- | :--- |
| **진공 카본 (Vacuum Carbon)** | `#090D14` | 이방성 카본 직조 법선을 지닌 미세운석 차폐 매트 패널 |
| **오비탈 티타늄 (Orbital Titanium)** | `#1A2433` | 브러시드 가공 구조 트러스, 방폭 셔터 및 1인칭 총기 리시버 |
| **코로나 앰버 (Corona Amber)** | `#F08A24` | 캡톤 금박 헬리오스탯 반사경 및 태양 플레어 열선 예고 영역 |
| **체렌코프 시안 (Cherenkov Cyan)** | `#38C6D9` | 이온화 레일 슬러그 궤적, 극저온 냉각수 도관 및 액티브 방열 아크 |
| **오버히트 플라즈마 레드 (Overheat Plasma Red)** | `#E54848` | 코어 과열 경보(`>= 85 Heat`), 적군 방열 약점 벤트 및 박격포 탄도 |

*팔레트 가드레일(Palette Guardrail)*: 흔한 AI 템플릿 보라색(`#7567F5`) 및 고채도 네온 마젠타는 모든 절차적 셰이더, 전술 HUD 조준선, 플라즈마 이펙트에서 엄격히 금지됩니다.

---

## 3. 10비트 궤도 미션 진행 루트 (`restore_perihelion_attitude`)

| 비트 | 궤도 섹터 | 전술 교전 목표 및 공간 어드벤처 게이트 |
| ---: | :--- | :--- |
| **01** | **엄빌리컬 에어록 (`Umbilical Airlock`)** | 무중력 도킹 스파인 진입; 전술 AI `Vesper` 초기화 및 `Kestrel-9 트윈코일 카빈` 장비 |
| **02** | **에어록 스파인 (`Airlock Spine`)** | 자기 엄빌리컬 클램프 파쇄; `슬라이드 부스트`(`24 ticks`) 및 `액티브 방열 재장전`(`ticks 14..20`) 보정 |
| **03** | **헬리오스탯 트러스 (`Heliostat Truss`)** | `240-tick` 주기 태양 플레어를 피하며 외부 미러 캣워크 돌파; `Volt Skitter` 무리 교전 및 `자기 그래플` 해금 |
| **04** | **극저온 냉각 매니폴드 (`Cryo-Coolant Manifold`)** | `Aegis Drone` 저격을 뚫고 그래플 슬링샷으로 수직 터빈 샤프트 상승, `아크-베인 브리치 런처` 확보 |
| **05** | **도관 위상 라우팅 (`Conduit Phase Routing`)** | `180 ticks` 축전기 감쇠 시간 내에 3개의 포물선 플라즈마 앵커를 연결해 《냉각 바이패스 코어》(`Coolant Bypass Core`) 추출 |
| **06** | **발리스틱 주조소 (`Ballistic Foundry`)** | 다층 도가니 아레나에서 중장갑 `Slag Enforcer`를 제압하고 `헬리오스 스캐터-레일`과 《점화 키카드》 확보 |
| **07** | **수트 리그 보정 벤치 (`Suit Rig Calibration`)** | 엔지니어링 벤치에서 3대 엑소 리그 코어(`recoil_gyro`, `thermal_siphon`, `grapple_overdrive`) 중 하나를 장착 |
| **08** | **코로나 방폭 셔터 (`Corona Blast Shutter`)** | 태양 코로나를 마주 보는 주 텅스텐 차폐벽을 개방하고 `근일점 코어 챔버`로 진입 |
| **09** | **근일점 코어 챔버 (`Perihelion Core Chamber`)** | 2페이즈 고속 기동 보스 **`헬리아크 워든`(`The Heliarch Warden`, `1,000 장갑 무결성`)** 격파 |
| **10** | **자세 제어 브리지 (`Attitude Control Bridge`)** | `DIRECTIVE_DIVERT` 또는 `DIRECTIVE_VENT` 최종 지령을 실행하고 버전 관리된 세이브 및 텔레메트리 로그 확정 |

---

## 4. 60 Hz 결정론적 화기, 액티브 방열 및 그래플 프레임 테이블

모든 화기 연사 템포, 충전 램프, 액티브 재장전 판정 및 기동 임펄스는 60 Hz 정수 틱(`1 tick = 16.6667 ms`)으로 작동합니다. 상체 화기 재장전 카운터는 하체 그래플 이탈 및 슬라이드 부스트 전이와 완전히 분리되어 공중 기동 중에도 방열 재장전이 캔슬되지 않습니다(`FPS-N06A-COMBAT-019`).

<div align="center">
  <img src="../assets/svg/game-03-telemetry-ko.svg" width="100%" alt="《근일점 돌파》 60 Hz 화기, 방열 재장전 및 그래플 기동 프레임 타임라인 다이어그램" />
</div>

| 액션명 | 선딜레이 (Startup) | 판정/충전 구간 (Active) | 후딜레이 (Recovery) | 총 틱 | 열량, 피해량 및 메커니컬 효과 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **카빈 3점사 (`Carbine 3-Burst`)** | `2 ticks` | `Ticks 3..11` (3발) | `10 ticks` | `21 ticks` | `+12 Heat`; `3 x 14 dmg` 히트스캔 (약점 배율 `1.5x`) |
| **스캐터 비조준 산탄 (`Scatter Uncharged`)** | `3 ticks` | `Tick 4` (`5x12` 산탄) | `15 ticks` | `18 ticks` | `+18 Heat`; `60 dmg` 근거리 플레셋 산탄, 에너지 실드 파쇄 특화 |
| **스캐터 조준 레일탄 (`Scatter ADS Slug`)** | `30..54 ticks` | `Tick 31..55` | `18 ticks` | `48..72 ticks` | `+28 Heat`; `55..85 dmg` 관통 전자기 슬러그 (약점 배율 `1.75x`) |
| **브리치 앵커 발사 (`Breach Anchor`)** | `6 ticks` | 포물선 투사체 비행 | `24 ticks` | `30 ticks` | `+30 Heat`; `60 AoE dmg` 중장갑 파쇄 또는 퍼즐 도관 연결 |
| **액티브 방열 재장전 (`Thermal Vent Reload`)** | `13 ticks` | `Ticks 14..20` | `16 ticks` | `36 ticks` | `14..20t` 입력 성공 시 `100% Heat` 제거 및 `90t` 과충전 버프 |
| **슬라이드 부스트 (`Slide-Boost`)** | `3 ticks` | `Ticks 4..18` | `6 ticks` | `24 ticks` | `11.5 m/s` 저자세 슬라이딩; `ticks 8..18` 점프 캔슬 가속 유지 |
| **자기 그래플 (`Magnetic Grapple`)** | `6 ticks` | `18..42 ticks` 견인 | `12 ticks` | `36..60 ticks` | `18.0 m/s` 앵커 견인; 이탈 시 접선 슬링샷 모멘텀 보존 |

---

## 5. 신스(Synth) 적군 로스터 및 2페이즈 보스: 헬리아크 워든 (The Heliarch Warden)

### 3종 신스 적군 아키타입
1. **볼트 스키터 (`Volt Skitter`)**: 벽면과 트러스 빔을 타고 고속 질주하는 4족 보행 유지보수 신스(`90 Hull`, 이동 속도 `6.8 m/s`). 엄폐한 플레이어를 밖으로 몰아냅니다.
2. **이지스 드론 (`Aegis Drone`)**: 전면 지향성 에너지 실드를 전개하는 부유 저격기(`140 Hull + 80 Shield`). 그래플로 측후방을 잡거나 `스캐터-레일` 산탄으로 실드를 과부하시켜 격파합니다.
3. **슬래그 인포서 (`Slag Enforcer`)**: 용융 슬래그 박격포를 발사하는 중장갑 프레임(`320 Hull`). 포격 직후 `90 ticks` 동안 등 뒤의 《냉각 척추(`Coolant Spine`)》 약점(`1.75x` 배율)이 노출됩니다.

### 2페이즈 보스: 헬리아크 워든 (`The Heliarch Warden`, `1,000 장갑 무결성`)
- **조형 구조**: 회전하는 반응로 짐벌 중앙에 현수된 높이 `6.0 m` 규모의 자이로스코프 태양 코어 오토마톤으로, 4개의 가동식 헬리오스탯 날개와 자기 그래플 링으로 무장하고 있습니다.
- **1페이즈 (`1,000 -> 501 무결성`)**: `Solar Sweep Beam`(수평 코로나 레이저, `슬라이드 부스트`로 하단 통과 또는 그래플 체공 회피), `Grapple Pylon Drop`(임시 자기 앵커 투하), `Cluster Mortar`, `Radiant Pulse`(시전 직후 등 쪽 `Core Vent` 약점이 `150 ticks` 노출)를 구사합니다.
- **2페이즈 (`500 -> 0 무결성`)**: 반응로 바닥 차폐판이 열리며 직하방의 태양 플라즈마가 드러나고, 역회전하는 3중 공중 캣워크 링 사이를 그래플로 오가며 싸우는 고기동 페이즈로 전환됩니다. `Coronal Ejection`, `Rotating Mirror Ring`, `Rail Volley`, `Perihelion Collapse`(직후 중앙 `Core Vent` 약점이 `150 ticks` 동안 노출) 패턴이 추가됩니다.

---

## 6. 수트 리그 보정: 3대 엑소 리그 코어 분기

비트 07(`Suit Rig Calibration`) 엔지니어링 벤치에서 `GraphState.active_relic`에 저장되는 3가지 엑소 리그 코어 중 하나를 장착합니다.

- **`반동 자이로` (`recoil_gyro`)**: 총기 뷰모델 반동 킥을 `-45%` 억제하고, 비조준 `스캐터-레일` 탄착군을 `-25%` 좁히며, 정밀 약점 타격 배율을 `1.5x`에서 `1.85x`로 강화합니다.
- **`열 사이펀` (`thermal_siphon`)**: `액티브 방열 재장전` 성공 판정 구간을 `ticks 14..20`(7틱)에서 `ticks 12..23`(12틱)으로 넓히고, 배출된 코어 열량을 `+25 실드` 오버실드로 전환합니다.
- **`그래플 오버드라이브` (`grapple_overdrive`)**: `자기 그래플` 견인 속도를 `18.0 m/s`에서 `22.5 m/s`로 가속하고 쿨다운을 `-35%` 단축하며, 그래플 킥 타격 시 EMP 충격파를 방출합니다.

---

## 7. 독립 프롬프트, JSON 스키마 및 골든 픽스처

- **마스터 오케스트레이터 프롬프트**: [`prompts/perihelion-breach/orchestrator.md`](../prompts/perihelion-breach/orchestrator.md) ([`orchestration/prompts/perihelion-breach-orchestrator.md`](../orchestration/prompts/perihelion-breach-orchestrator.md) 미러링)
- **7종 전문 에이전트 카드**: [`prompts/perihelion-breach/agents/`](../prompts/perihelion-breach/agents/)
- **골든 레퍼런스 픽스처 (`run-0003`)**: [`examples/run-0003/task-packet.json`](../examples/run-0003/task-packet.json), [`examples/run-0003/defect-record.json`](../examples/run-0003/defect-record.json), [`examples/run-0003/run-manifest.json`](../examples/run-0003/run-manifest.json)
- **시리즈 4권 동반 가이드**:
  - [`docs/EVIDENCE_GRAPH_GUIDE.ko.md`](EVIDENCE_GRAPH_GUIDE.ko.md) (《Three.js Evidence Graph v2.0 운영 매뉴얼》, 64쪽)
  - [`docs/THE_HOLLOW_MERIDIAN_GUIDE.ko.md`](THE_HOLLOW_MERIDIAN_GUIDE.ko.md) (《공허의 자오선 v1.0》, 81쪽)
  - [`docs/THE_GLASS_OSSUARY_GUIDE.ko.md`](THE_GLASS_OSSUARY_GUIDE.ko.md) (《유리 납골당 v1.0》, 36쪽)
