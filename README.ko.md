<!-- source_version: 2026.07.5; translation_status: reviewed; language: ko -->

# Three.js 에비던스 그래프 & 멀티 장르 무에셋 게임 프로덕션 스위트

<div align="center">

[![Native English](https://img.shields.io/badge/Edition-Native_English-D49B4B?style=for-the-badge)](README.md)
[![简体中文](https://img.shields.io/badge/语言-简体中文_(原生母语版)-45B29D?style=for-the-badge)](README.zh-CN.md)
[![日本語](https://img.shields.io/badge/言語-日本語_(ネイティブ版)-38C6D9?style=for-the-badge)](README.ja.md)
[![한국어](https://img.shields.io/badge/언어-한국어_(네이티브판)-C89B54?style=for-the-badge)](README.ko.md)

[![Release 2026.07.5](https://img.shields.io/badge/릴리스-2026.07.5-0F1722?style=flat-square&logo=github)](RELEASE_NOTES.md)
[![Three.js r185](https://img.shields.io/badge/Three.js-r185_(0.185.0)-45B29D?style=flat-square)](docs/TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md)
[![Publications 4 PDFs / 217 Pages](https://img.shields.io/badge/출판물-총4권_·_217쪽-D49B4B?style=flat-square)](docs/PUBLICATION_STATUS.md)
[![JSON Schema Draft 2020-12](https://img.shields.io/badge/스키마-Draft_2020--12-38C6D9?style=flat-square)](schemas/)
[![License MIT](https://img.shields.io/badge/라이선스-MIT-CBD5E1?style=flat-square)](LICENSE)

</div>

![Three.js 에비던스 그래프 & 멀티 장르 프로덕션 스위트 마스트헤드](assets/svg/masthead-ko.svg)

> **저장소 핵심 개요**
>
> 본 저장소는 **Emily Paradox(`@iamemily2050`)**가 집필한 Three.js `r185`(`0.185.0`) 기반 **총 4권, `217`쪽 분량의 엔지니어링 규격서 및 멀티 에이전트 제작 프롬프트 스위트**입니다. 외부 3D 모델(`.glb`), 텍스처, 폰트, 사전 녹음 오디오 파일을 일절 다운로드하지 않고, 오직 저장소 내 소스 코드와 시드(Seed)만으로 결정론적 브라우저 게임 버티컬 슬라이스를 제작하기 위한 범용 제어 평면 매뉴얼(《Three.js Evidence Graph: Operational Manual v2.0》, `64`쪽)과 3종의 장르별 플래그십 제작 규격서를 제공합니다.
> 1. **Game 01 — 3인칭 다크 판타지 액션 RPG**: **《공허의 자오선》(*The Hollow Meridian*, 81쪽)**
> 2. **Game 02 — 1인칭 음향 포렌식 미스터리 호러**: **《유리 납골당》(*The Glass Ossuary*, 36쪽)**
> 3. **Game 03 — 1인칭 하이퍼 SF 슈팅 어드벤처**: **《근일점 돌파》(*Perihelion Breach*, 36쪽)**
>
> 모든 출판물에는 독립 실행형 JSON Schema Draft 2020-12 계약 파일(`schemas/`), 즉시 복사해 사용할 수 있는 마스터 오케스트레이터 및 21종의 전문 에이전트 카드(`prompts/`), 스키마 검증을 통과한 골든 레퍼런스 픽스처(`examples/run-0001/` ~ `examples/run-0003/`), 그리고 번역투가 아닌 **영어, 중국어 간체, 일본어, 한국어** 현업 게임 개발 용어로 집필된 네이티브 동반 가이드가 포함되어 있습니다.

---

## 4권 출판물 스위트 총람 (총 `217`쪽)

![4권 출판물 세트: Three.js Evidence Graph v2.0, 《공허의 자오선》, 《유리 납골당》, 《근일점 돌파》](assets/publication-set.jpg)

*본 이미지는 저장소에 수록된 4권의 PDF 출판물 합본 플레이트입니다. 모든 표지와 섹션 히어로 이미지는 출판물용 컨셉 아트워크이며, 실제 게임플레이 스크린샷이나 런타임 벤치마크 증거가 아닙니다.*

| 권호 | 출판물 제목 및 장르 | PDF 아티팩트 (`publications/`) | 쪽수 | 파일 크기 | 4개국어 네이티브 가이드 (`docs/`) | 프롬프트 및 골든 픽스처 |
| :-: | :--- | :--- | ---: | ---: | :--- | :--- |
| **01** | **Three.js Evidence Graph v2.0**<br/>*멀티 에이전트 제어 평면 및 결정론 운영 매뉴얼* | [`threejs-evidence-graph-operational-manual-v2.0-en.pdf`](publications/threejs-evidence-graph-operational-manual-v2.0-en.pdf)<br/>`sha256[0..16]: d3830d411a61c52c` | `64`쪽 | `416,827` B | [EN](docs/EVIDENCE_GRAPH_GUIDE.md) · [中文](docs/EVIDENCE_GRAPH_GUIDE.zh-CN.md) · [日本語](docs/EVIDENCE_GRAPH_GUIDE.ja.md) · [한국어](docs/EVIDENCE_GRAPH_GUIDE.ko.md) | [`prompts/evidence-graph/`](prompts/evidence-graph/)<br/>[`schemas/`](schemas/) |
| **02** | **《공허의 자오선》 The Hollow Meridian v1.0**<br/>*Game 01 · 3인칭 다크 판타지 액션 RPG* | [`the-hollow-meridian-rpg-full-prompt-v1.0-en.pdf`](publications/the-hollow-meridian-rpg-full-prompt-v1.0-en.pdf)<br/>`sha256[0..16]: c4f8fe83995d526b` | `81`쪽 | `357,144` B | [EN](docs/THE_HOLLOW_MERIDIAN_GUIDE.md) · [中文](docs/THE_HOLLOW_MERIDIAN_GUIDE.zh-CN.md) · [日本語](docs/THE_HOLLOW_MERIDIAN_GUIDE.ja.md) · [한국어](docs/THE_HOLLOW_MERIDIAN_GUIDE.ko.md) | [`prompts/hollow-meridian/`](prompts/hollow-meridian/)<br/>[`examples/run-0001/`](examples/run-0001/) |
| **03** | **《유리 납골당》 The Glass Ossuary v1.0**<br/>*Game 02 · 1인칭 조사형 미스터리 호러* | [`the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf`](publications/the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf)<br/>`sha256[0..16]: efead090be003782` | `36`쪽 | `98,649` B | [EN](docs/THE_GLASS_OSSUARY_GUIDE.md) · [中文](docs/THE_GLASS_OSSUARY_GUIDE.zh-CN.md) · [日本語](docs/THE_GLASS_OSSUARY_GUIDE.ja.md) · [한국어](docs/THE_GLASS_OSSUARY_GUIDE.ko.md) | [`prompts/glass-ossuary/`](prompts/glass-ossuary/)<br/>[`examples/run-0002/`](examples/run-0002/) |
| **04** | **《근일점 돌파》 Perihelion Breach v1.0**<br/>*Game 03 · 1인칭 SF 슈팅 어드벤처* | [`perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf`](publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf)<br/>`sha256[0..16]: 75bdfff21c905122` | `36`쪽 | `95,265` B | [EN](docs/PERIHELION_BREACH_GUIDE.md) · [中文](docs/PERIHELION_BREACH_GUIDE.zh-CN.md) · [日本語](docs/PERIHELION_BREACH_GUIDE.ja.md) · [한국어](docs/PERIHELION_BREACH_GUIDE.ko.md) | [`prompts/perihelion-breach/`](prompts/perihelion-breach/)<br/>[`examples/run-0003/`](examples/run-0003/) |

---

## 코어 아키텍처: 15노드 에비던스 그래프 (`N00` .. `N14`)

![15노드 에비던스 그래프 토폴로지 및 3대 장르 게임 인스턴스화 다이어그램](assets/svg/architecture-pipeline.svg)

단일 LLM 대화창에서 기획, 셰이더 작성, 전투 수치 조정, 자체 검수를 동시에 수행하면 컨텍스트 드리프트와 셰이더 스파이크, 근거 없는 자기 승인 문제가 발생합니다. **Three.js Evidence Graph v2.0**은 권한과 검증을 다음 4계층으로 분리하여 이를 원천 차단합니다.

1. **결정론적 마스터 오케스트레이터 (`orchestrator`)**: [`schemas/graph-state.d.ts`](schemas/graph-state.d.ts)를 기반으로 `N00_BRIEF`부터 `N14_RELEASE_CANDIDATE`까지 15노드 DAG 상태 전이를 제어합니다. [`task-packet.schema.json`](schemas/task-packet.schema.json) 규격을 통과한 작업 패킷과 인수 테스트 통과 없이는 다음 노드로 진행할 수 없습니다.
2. **파일 쓰기 권한이 격리된 전담 서브에이전트 (게임당 7종 카드)**: `combat_gameplay`, `world_quest`, `procedural_art_vfx`, `procedural_audio`, `ui_hud_accessibility`, `qa_perf_playwright` 및 읽기 전용 `independent_critic`으로 구성됩니다. 각 작업 에이전트는 허용된 `allowed_paths` 외부의 파일을 수정할 수 없습니다.
3. **이중 결정론 레짐 (`A-PinnedBrowser` & `B-CrossPlatform`)**:
   - **레짐 A (`A-PinnedBrowser`, 고정 컨테이너 비트 일치)**: 고정 버전 Chromium 컨테이너에서 60 Hz 정수 틱 상태 해시(`state_hash`), 16-bit PCM 양자화된 `OfflineAudioContext` 오디오 해시(`audio_hash`), `1e-5` 양자화된 절차적 지오메트리 해시(`geometry_hash`)의 SHA-256 일치를 검증합니다.
   - **레짐 B (`B-CrossPlatform`, 크로스 플랫폼 허용 오차)**: `THREE.WebGPURenderer` 주 경로 및 `{ forceWebGL: true }` 폴백 경로에서 프레임 시간 백분위수(`P50 <= 8.3 ms`, `P95 <= 16.6 ms`, `P99 <= 22.0 ms`)와 EBU R128 라우드니스(`-16 LUFS +- 1.0 LU`, 트루 피크 `<= -1.0 dBTP`)를 검증합니다.
4. **외부 바이너리 에셋 제로 원칙 (`provenance_critic`)**: 모든 3D 메시, TSL(`Three.js Shading Language`) 셰이더, 스켈레탈 리그, UI 글리프, Web Audio 사운드는 코드에서 실시간 컴파일되며, `external_network_requests`와 `downloaded_assets_count`는 `0`으로 강제됩니다.

---

## 3대 플래그십 게임 장르별 비교 매트릭스

| 비교 항목 | Game 01: 《공허의 자오선》 (*The Hollow Meridian*) | Game 02: 《유리 납골당》 (*The Glass Ossuary*) | Game 03: 《근일점 돌파》 (*Perihelion Breach*) |
| :--- | :--- | :--- | :--- |
| **장르 및 카메라 시점** | 3인칭 다크 판타지 액션 RPG | 1인칭 조사형 미스터리 호러 (Mystery on Horror) | 1인칭 하이퍼 SF 슈팅 어드벤처 (FPS Adventure) |
| **목표 플레이 시간** | 10~14분 | 12~16분 | 12~15분 |
| **주인공** | `The Cartographer` (측량사 `Sable Veren`) | `Clara Vane` (음향 기록 보관관 `The Acoustic Archivist`) | `Soren Kestrel` (릴레이 선봉대원 + 전술 AI `Vesper`) |
| **핵심 생존 자원** | `100 체력` · `100 스태미나` · `0–100 공명` | `100 침착성` · `100 랜턴 오일` · `0–100 정신 침식도` | `100 실드` · `100 장갑 무결성` · `0–100 코어 열량` |
| **60 Hz 핵심 메커니즘** | 버튼 다운 즉시 `패링`(`ticks 6..12`)과 홀드 `가드`(`tick >= 13`) 우선순위 분리 | 직교 비트마스크 `랜턴 셔터`(`6t`) + `축음기 위상 상쇄`(`25..114t`) + `페로타입 플래시`(`19..24t`) | `액티브 방열 재장전`(`14..20t` 열량 100% 배출 및 과충전) + `자기 그래플`(`18.0 m/s`) + `슬라이드 부스트`(`11.5 m/s`) |
| **5개 연결 공간 루트** | `Ash Court` -> `Orrery Bridge` -> `Archive Nave` -> `Bell Foundry` -> `Meridian Chamber` | `Tidewater Causeway` -> `Caretaker's Stripping Room` -> `Refraction Gallery` -> `Submerged Crypt` -> `The Glass Ossuary` | `Umbilical Airlock` -> `Heliostat Truss` -> `Cryo-Coolant Manifold` -> `Ballistic Foundry` -> `Perihelion Core Chamber` |
| **비트 05 공간 퍼즐** | `Meridian Alignment` (3중 황동 링 정렬 -> `North Seal`) | `Prism Triangulation` (`45/135/270 deg` 프레넬 링 -> 《조수 원장 단편》) + `110/220/330 Hz` 수문 동조 | `Conduit Phase Routing` (`180 ticks` 감쇠 시간 내 3개 플라즈마 앵커 연결 -> 《냉각 바이패스 코어》) |
| **3종 적/괴이 아키타입** | `Ashbound Skirmisher`, `Lantern Wraith`, `Bell Sentinel` | `Mire Listener`(음향 추적), `Glass Septum Watcher`(시선 굴절), `Drowned Chorister`(저주파 오라) | `Volt Skitter`(벽면 질주), `Aegis Drone`(실드 저격), `Slag Enforcer`(용융 박격포) |
| **비트 07 빌드 분기** | **제단 유물**: `brass_vow` · `ash_thread` · `vacant_name` | **추리 보드 가설**: `lens_sabotage` · `tidal_quarantine` · `acoustic_calling` | **엑소 리그 코어**: `recoil_gyro` · `thermal_siphon` · `grapple_overdrive` |
| **비트 09 2페이즈 보스** | **이름 없는 종** (`The Bell Without a Name`, `850 HP`, `55%`에서 2페이즈) | **유리 속의 성가대** (`The Choir in the Glass`, `600 무결성`, `300`에서 2페이즈) | **헬리아크 워든** (`The Heliarch Warden`, `1,000 무결성`, `500`에서 2페이즈) |
| **비트 10 멀티 엔딩** | `CHOICE_BIND`(구속) 또는 `CHOICE_RELEASE`(해방) | `VERDICT_PUBLISH`(공개) 또는 `VERDICT_SUBMERGE`(영구 수몰) | `DIRECTIVE_DIVERT`(전력망 수호) 또는 `DIRECTIVE_VENT`(코어 사출) |
| **렌더링 예산 상한** | `<= 300` Draw Calls · `<= 500,000` Tris | `<= 280` Draw Calls · `<= 460,000` Tris | `<= 300` Draw Calls · `<= 500,000` Tris |
| **골든 픽스처** | [`examples/run-0001/`](examples/run-0001/) (`seed=1337`) | [`examples/run-0002/`](examples/run-0002/) (`seed=1894`) | [`examples/run-0003/`](examples/run-0003/) (`seed=2142`) |

---

## 플래그십 3작품 상세 안내

### 1. Game 01 — 《공허의 자오선》 (*The Hollow Meridian* · 3인칭 액션 RPG · 81쪽)

| 폐허 관측소 월드 루트 컨셉 플레이트 | 2페이즈 보스 '이름 없는 종' 컨셉 플레이트 |
| :---: | :---: |
| ![공허의 자오선 월드 루트](assets/hollow-meridian-world-hero.jpg) | ![이름 없는 종 보스전](assets/hollow-meridian-boss-hero.jpg) |

사라진 도시들의 진짜 이름을 보존하던 황동과 현무암 폐허 관측소를 배경으로, 플레이어는 **The Cartographer(측량사)**가 되어 5개의 공간을 돌파합니다. 60 Hz 정수 틱 기반의 7틱 패링 판정, 스태미나 운영, 3중 링 자오선 정렬 퍼즐, 제단 유물 선택을 거쳐 2페이즈 보스 **The Bell Without a Name(이름 없는 종)**과 맞섭니다.

<details>
<summary><strong>《공허의 자오선》 10비트 진행 루트 · 60 Hz 전투 프레임 테이블 · 제단 유물 분기 펼치기</strong></summary>

| 액션 | 선딜레이 | 활성 / 무적 틱 | 후딜레이 | 총 틱 | 소모 자원 및 전투 효과 |
| :--- | :--- | :--- | :--- | :--- | :--- |
- **수작업 10비트 진행 루트 (`recover_orientation`)**: `01 Ash Court Arrival`(안전 허브 · `Mnemonic Keeper`) -> `02 Quest Acceptance`(방위 인장 2종 퀘스트) -> `03 Orrery Bridge Tutorial`(`Ashbound Skirmisher` 교전) -> `04 Archive Nave`(`Lantern Wraith` 원거리 압박) -> `05 Meridian Alignment`(3중 고리 퍼즐 -> `North Seal`) -> `06 Bell Foundry`(`Bell Sentinel` 가드 브레이크 -> `Depth Seal`) -> `07 Shrine Choice`(유물 3종 중 택1: `brass_vow` / `ash_thread` / `vacant_name`) -> `08 Chamber Opening` -> `09 The Unnamed Bell`(`850 HP` 2페이즈 보스전) -> `10 Bind or Release`(`CHOICE_BIND` / `CHOICE_RELEASE`).

| 액션 | 선딜레이 | 활성 / 무적 틱 | 후딜레이 | 총 틱 | 소모 자원 및 전투 효과 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Light Attack 1 / 2 / 3` | `10 / 11 / 15t` | `5 / 7 / 9t` | `12 / 12 / 18t` | `27 / 30 / 42t` | `10 / 11 / 14 Stamina`; `16 / 18 / 25 HP` |
| `Charged Heavy` | `27..38t` | `10..11t` | `12..14t` | `49..63t` | `28 Stamina`; `28..42 HP` + 강인도 감쇄 |
| `Dodge Roll` | `7t` | `Ticks 7..18` (`12t`) | `12t` | `31t` | `22 Stamina`; `ticks 7..18` 완전 무적 |
| `Parry Deflect` | `5t` (`0..4`) | `Ticks 6..12` (`7t`) | `18t` | `31t` | `12 Stamina`; 홀드 시 `tick 13`부터 `Guard` 전환 |
| `Echo Brand` | `12t` | `360t 표식` | `0t` | `12t 시전` | `50 Resonance`; 받는 피해 `+25%` + 보스 약점 노출 |

- **PDF 규격서**: [`publications/the-hollow-meridian-rpg-full-prompt-v1.0-en.pdf`](publications/the-hollow-meridian-rpg-full-prompt-v1.0-en.pdf)
- **한국어 상세 가이드**: [`docs/THE_HOLLOW_MERIDIAN_GUIDE.ko.md`](docs/THE_HOLLOW_MERIDIAN_GUIDE.ko.md)
- **프롬프트 및 골든 픽스처**: [`prompts/hollow-meridian/`](prompts/hollow-meridian/) · [`examples/run-0001/`](examples/run-0001/)

</details>

---

### 2. Game 02 — 《유리 납골당》 (*The Glass Ossuary* · 1인칭 미스터리 호러 · 36쪽)

| 굴절 회랑 포렌식 조사 컨셉 플레이트 | 2페이즈 보스 '유리 속의 성가대' 컨셉 플레이트 |
| :---: | :---: |
| ![유리 납골당 포렌식 조사](assets/glass-ossuary-investigation-hero.jpg) | ![유리 속의 성가대 보스전](assets/glass-ossuary-apparition-hero.jpg) |

1894년 가을 폭풍우가 몰아치는 밤, 음향 기록 보관관 **Clara Vane**은 프레넬 등대와 지하 골유리(Bone-Glass) 납골당이 결합된 생반 해안 관측소에 상륙합니다. 총기나 작위적인 점프 스케어 대신 `이중 초점 황동 루페`, `밀랍 실린더 축음기`, `은염 페로타입 건판 카메라` 등 3종의 물리 포렌식 장비와 `6노드 추리 보드`를 활용해 난파 사건의 진실을 추리하고 최심부에서 **The Choir in the Glass(유리 속의 성가대)**와 대면합니다.

<details>
<summary><strong>《유리 납골당》 10비트 조사 루트 · 60 Hz 포렌식 장비 프레임 테이블 · 추리 가설 분기 펼치기</strong></summary>

- **10비트 포렌식 조사 루트 (`case_saint_vane`)**: `01 Causeway Landfall`(`Tidewater Causeway` 상륙 · `Lantern Shutter`) -> `02 The Sealed Inquest`(`Caretaker's Stripping Room` · 6노드 추리 보드 · Moreau 실린더) -> `03 Ferrotype Calibration`(`Ferrotype Plate` 자외선 플래시 교정) -> `04 Refraction Gallery`(`Glass Septum Watcher` 시야 회피 · `Brass Loupe`) -> `05 Prism Triangulation`(`45/135/270 deg` 프레넬 링 -> 《조수 원장 단편》) -> `06 Submerged Crypt`(`Mire Listener` 음향 잠입 · `110/220/330 Hz` 수문 -> 《수중 청음 실린더》) -> `07 Inquest Board Deduction`(3대 가설 분기: `lens_sabotage` / `tidal_quarantine` / `acoustic_calling`) -> `08 Ossuary Unsealing` -> `09 The Choir in the Glass`(`600 Integrity` 2페이즈 보스전) -> `10 Publish or Submerge`(`VERDICT_PUBLISH` / `VERDICT_SUBMERGE`).

| 장비 및 액션 | 선딜레이 | 유효 윈도우 | 후딜레이 | 총 틱 | 소모 자원 및 조사 효과 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Lantern Shutter` | `6 ticks` | 토글 유지 (`7..`) | `6 ticks` | `12 ticks` | `0 Oil`; 광원 원뿔을 차단해 광학 시야 어그로 해제 |
| `Brass Loupe Focus` | `9 ticks` | 홀드 (`10..69`) | `6 ticks` | `75 ticks` | `0 Oil`; 미세 프리즘 눈금 및 골유리 각인 해독 |
| `Phonograph Cancel` | `24 ticks` | `Ticks 25..114` | `36 ticks` | `150 ticks` | 실내 공명 주파수 역위상 상쇄; `Mire Listener`에게 발소리 은폐 |
| `Ferrotype Flash` | `18 ticks` | `Ticks 19..24` | `66 ticks` | `90 ticks` | `6.5 m` 내 괴이 `150 ticks` 경직 + 골유리 균열 노출 |
| `Crouch Sidestep` | `5 ticks` | `Ticks 6..16` | `12 ticks` | `28 ticks` | 젖은 석재 바닥 발소리를 `<= -38 dBFS` 이하로 억제 |
| `Smelling Salts` | `15 ticks` | `Ticks 16..45` | `10 ticks` | `55 ticks` | `Composure +40` 회복 및 `Exposure -25` 정화 |

- **PDF 규격서**: [`publications/the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf`](publications/the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf)
- **한국어 상세 가이드**: [`docs/THE_GLASS_OSSUARY_GUIDE.ko.md`](docs/THE_GLASS_OSSUARY_GUIDE.ko.md)
- **프롬프트 및 골든 픽스처**: [`prompts/glass-ossuary/`](prompts/glass-ossuary/) · [`examples/run-0002/`](examples/run-0002/)

</details>

---

### 3. Game 03 — 《근일점 돌파》 (*Perihelion Breach* · 1인칭 SF 슈팅 어드벤처 · 36쪽)

| 이카로스-9 궤도 태양 중계소 컨셉 플레이트 | 2페이즈 보스 '헬리아크 워든' 교전 컨셉 플레이트 |
| :---: | :---: |
| ![근일점 돌파 궤도 스테이션](assets/perihelion-breach-world-hero.jpg) | ![헬리아크 워든 보스전](assets/perihelion-breach-combat-hero.jpg) |

태양으로부터 불과 `0.09 AU` 떨어진 근일점 궤도를 도는 **이카로스-9(Icarus-9) 태양 중계 스테이션**에서 선봉대원 **Soren Kestrel**이 전술 AI **Vesper**와 함께 열폭주에 빠진 방어 그리드를 돌파합니다. `Kestrel-9 트윈코일 카빈`, 관통 전자기 슬러그를 발사하는 `헬리오스 스캐터-레일`, `ticks 14..20` 구간에 열량을 100% 배출하는 `액티브 방열 재장전`, `18.0 m/s` `자기 그래플` 슬링샷 기동을 결합해 2페이즈 보스 **The Heliarch Warden(헬리아크 워든)**을 격파합니다.

<details>
<summary><strong>《근일점 돌파》 10비트 작전 루트 · 60 Hz 화기/그래플 프레임 테이블 · 엑소 리그 분기 펼치기</strong></summary>

- **10비트 궤도 작전 루트 (`restore_perihelion_attitude`)**: `01 Airlock Breach`(`Umbilical Airlock` · 전술 AI `Vesper` · `Kestrel-9 Carbine`) -> `02 Lockdown Override`(`Slide-Boost` & `Thermal Vent Reload` 교정) -> `03 Heliostat Skirmish`(`240-tick` 태양 플레어 주기 · `Volt Skitter` 요격 · `Magnetic Grapple` 해금) -> `04 Cryo-Coolant Ascent`(`Aegis Drone` 수직 터빈 돌파 · `Breach Launcher` 획득) -> `05 Conduit Phase Routing`(`180 ticks` 내 플라즈마 앵커 3개 연결 -> 《냉각 바이패스 코어》) -> `06 Ballistic Foundry Siege`(`Slag Enforcer` 격파 -> `Helios Scatter-Rail`) -> `07 Suit Rig Calibration`(엑소 리그 코어 3종 중 택1: `recoil_gyro` / `thermal_siphon` / `grapple_overdrive`) -> `08 Shutter Retraction` -> `09 The Heliarch Warden`(`1,000 Integrity` 2페이즈 보스전) -> `10 Divert or Vent`(`DIRECTIVE_DIVERT` / `DIRECTIVE_VENT`).

| 화기 및 기동 | 선딜레이 | 활성 / 입력 구간 | 후딜레이 | 총 틱 | 열량 · 대미지 · 전술 기동 효과 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Carbine 3-Burst` | `2 ticks` | `Ticks 3..11` (3발) | `10 ticks` | `21 ticks` | `+12 Heat`; `3 x 14 dmg` 히트스캔 (약점 `1.5x`) |
| `Scatter Uncharged` | `3 ticks` | `Tick 4` (`5x12`) | `15 ticks` | `18 ticks` | `+18 Heat`; 근거리 `60 dmg` 산탄 · 에너지 실드 파쇄 |
| `Scatter ADS Slug` | `30..54 ticks` | `Tick 31..55` | `18 ticks` | `48..72 ticks` | `+28 Heat`; `55..85 dmg` 관통 레일 슬러그 (약점 `1.75x`) |
| `Breach Anchor` | `6 ticks` | 투사체 발사 | `24 ticks` | `30 ticks` | `+30 Heat`; `60 AoE dmg` 장갑 균열 또는 도관 앵커 연결 |
| `Thermal Vent Reload` | `13 ticks` | `Ticks 14..20` | `16 ticks` | `36 ticks` | `14..20t` 입력 성공 시 `Heat 100%` 배출 + `90t` 오버차지 |
| `Slide-Boost` | `3 ticks` | `Ticks 4..18` | `6 ticks` | `24 ticks` | `11.5 m/s` 고속 슬라이딩 (`ticks 8..18` 점프 캔슬 가능) |
| `Magnetic Grapple` | `6 ticks` | `18..42 ticks` 견인 | `12 ticks` | `36..60 ticks` | `18.0 m/s` 앵커 견인 · 이탈 시 접선 슬링샷 속도 보존 |

- **PDF 규격서**: [`publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf`](publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf)
- **한국어 상세 가이드**: [`docs/PERIHELION_BREACH_GUIDE.ko.md`](docs/PERIHELION_BREACH_GUIDE.ko.md)
- **프롬프트 및 골든 픽스처**: [`prompts/perihelion-breach/`](prompts/perihelion-breach/) · [`examples/run-0003/`](examples/run-0003/)

</details>

---

## 4개국어 네이티브 기술 문서 매트릭스

본 저장소의 모든 README와 4권의 동반 가이드는 기계적인 번역투를 배제하고 **영어, 중국어 간체, 일본어, 한국어** 각 언어권의 현업 게임 엔진·그래픽스 엔지니어링 용어에 맞춰 네이티브로 집필되었습니다(코드 식별자, CLI 명령어, 스키마 키는 추적성을 위해 영문 원형을 유지합니다).

| 문서 구분 | 영문판 (`en`) | 중국어 간체 네이티브판 (`zh-CN`) | 일본어 네이티브판 (`ja`) | 한국어 네이티브판 (`ko`) |
| :--- | :--- | :--- | :--- | :--- |
| **저장소 총람 및 스위트 가이드** | [`README.md`](README.md) | [`README.zh-CN.md`](README.zh-CN.md) | [`README.ja.md`](README.ja.md) | [`README.ko.md`](README.ko.md) |
| **제1권: Evidence Graph v2.0 매뉴얼 (64쪽)** | [`EVIDENCE_GRAPH_GUIDE.md`](docs/EVIDENCE_GRAPH_GUIDE.md) | [`EVIDENCE_GRAPH_GUIDE.zh-CN.md`](docs/EVIDENCE_GRAPH_GUIDE.zh-CN.md) | [`EVIDENCE_GRAPH_GUIDE.ja.md`](docs/EVIDENCE_GRAPH_GUIDE.ja.md) | [`EVIDENCE_GRAPH_GUIDE.ko.md`](docs/EVIDENCE_GRAPH_GUIDE.ko.md) |
| **제2권: 《공허의 자오선》 액션 RPG (81쪽)** | [`THE_HOLLOW_MERIDIAN_GUIDE.md`](docs/THE_HOLLOW_MERIDIAN_GUIDE.md) | [`THE_HOLLOW_MERIDIAN_GUIDE.zh-CN.md`](docs/THE_HOLLOW_MERIDIAN_GUIDE.zh-CN.md) | [`THE_HOLLOW_MERIDIAN_GUIDE.ja.md`](docs/THE_HOLLOW_MERIDIAN_GUIDE.ja.md) | [`THE_HOLLOW_MERIDIAN_GUIDE.ko.md`](docs/THE_HOLLOW_MERIDIAN_GUIDE.ko.md) |
| **제3권: 《유리 납골당》 미스터리 호러 (36쪽)** | [`THE_GLASS_OSSUARY_GUIDE.md`](docs/THE_GLASS_OSSUARY_GUIDE.md) | [`THE_GLASS_OSSUARY_GUIDE.zh-CN.md`](docs/THE_GLASS_OSSUARY_GUIDE.zh-CN.md) | [`THE_GLASS_OSSUARY_GUIDE.ja.md`](docs/THE_GLASS_OSSUARY_GUIDE.ja.md) | [`THE_GLASS_OSSUARY_GUIDE.ko.md`](docs/THE_GLASS_OSSUARY_GUIDE.ko.md) |
| **제4권: 《근일점 돌파》 FPS 어드벤처 (36쪽)** | [`PERIHELION_BREACH_GUIDE.md`](docs/PERIHELION_BREACH_GUIDE.md) | [`PERIHELION_BREACH_GUIDE.zh-CN.md`](docs/PERIHELION_BREACH_GUIDE.zh-CN.md) | [`PERIHELION_BREACH_GUIDE.ja.md`](docs/PERIHELION_BREACH_GUIDE.ja.md) | [`PERIHELION_BREACH_GUIDE.ko.md`](docs/PERIHELION_BREACH_GUIDE.ko.md) |
| **다국어 용어집 및 번역 정책** | [`docs/GLOSSARY.md`](docs/GLOSSARY.md) · [`docs/TRANSLATION_POLICY.md`](docs/TRANSLATION_POLICY.md) | [`docs/GLOSSARY.md`](docs/GLOSSARY.md) | [`docs/GLOSSARY.md`](docs/GLOSSARY.md) | [`docs/GLOSSARY.md`](docs/GLOSSARY.md) |

---

## 저장소 디렉터리 구조 및 아키텍처 맵

```text
threejs-evidence-graph/
├── publications/                                                     # 규범적 영문 PDF 출판물 4권 (총 217쪽)
│   ├── threejs-evidence-graph-operational-manual-v2.0-en.pdf         # 64쪽 · 제어 평면 및 결정론 운영 매뉴얼
│   ├── the-hollow-meridian-rpg-full-prompt-v1.0-en.pdf               # 81쪽 · Game 01: 《공허의 자오선》 액션 RPG
│   ├── the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf      # 36쪽 · Game 02: 《유리 납골당》 미스터리 호러
│   └── perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf       # 36쪽 · Game 03: 《근일점 돌파》 SF 슈팅 어드벤처
├── schemas/                                                          # Draft 2020-12 JSON Schema 계약 및 TypeScript 상태 정의
├── orchestration/                                                    # 에이전트 런타임 작업 디렉터리용 드롭인 미러
├── prompts/                                                          # 마스터 오케스트레이터 4종 + 전담 서브에이전트 카드 21종
├── examples/                                                         # 스키마 검증을 통과한 골든 픽스처 (run-0001..0003)
├── docs/                                                             # 4개국어 네이티브 가이드 16종 + 정오표 + 거버넌스 문서
├── assets/                                                           # EXIF 제로 JPEG 13종 + 커스텀 타이포그래피 SVG 5종
├── scripts/verify_release.py                                         # 자동 SHA-256, 스키마, PDF, EXIF, 링크 검증 스크립트
├── SHA256SUMS.txt                                                    # 전체 릴리스 아티팩트 SHA-256 체크섬 (LF 줄바꿈)
└── release-manifest.json                                             # 기계 판독용 릴리스 매니페스트
```

---

## 무결성 검증 명령어

저장소 루트에서 아래 명령어를 실행하면 전체 파일의 SHA-256 해시, JSON Schema Draft 2020-12 계약, 3종의 골든 픽스처(`run-0001` ~ `run-0003`), 4권의 PDF 접근성 태그 및 클릭 가능한 URI 링크, 13장의 EXIF 제로 JPEG 에셋, 모든 다국어 Markdown 링크를 한 번에 검증할 수 있습니다.

```bash
sha256sum -c SHA256SUMS.txt
python scripts/verify_release.py
```

---

## 범위 및 비주장 사항 (Epistemic Honesty)

본 저장소는 **아키텍처 규격서, 멀티 에이전트 제작 프롬프트, JSON Schema 계약 및 골든 레퍼런스 픽스처**를 배포하며, 다음 항목은 **포함하지 않습니다**:

- 플레이 가능한 Three.js 런타임 게임 빌드;
- 실제 빌드에서 측정된 GPU 프레임 시간 벤치마크 데이터;
- 라이브 Playwright 브라우저 캡처 패키지;
- 구현된 UI에 대한 공식 WCAG 접근성 인증.

문서에 명시된 프레임 시간 백분위수(`P50 <= 8.3 ms`, `P95 <= 16.6 ms`, `P99 <= 22.0 ms`), Draw Call 상한, 오디오 라우드니스 목표(`-16 LUFS +- 1.0 LU`, `<= -1.0 dBTP`)는 모두 `N14_RELEASE_CANDIDATE` 승인 전에 구현체가 통과해야 하는 **규범적 인수 게이트(Normative Acceptance Gates)**입니다.

---

## 저자, 인용 및 라이선스

- **출판물 표기명**: Emily Paradox
- **창작자 및 저작권자**: **Iamemily2050 (`@iamemily2050`)**
- **GitHub**: [Emily2040](https://github.com/Emily2040) · **웹사이트**: [iamemily2050.com](https://iamemily2050.com) · **X**: [`@iamemily2050`](https://x.com/iamemily2050) · **Instagram**: [`@iamemily2050`](https://instagram.com/iamemily2050)
- **인용 메타데이터**: [`CITATION.cff`](CITATION.cff) 및 [`CITATIONS.md`](CITATIONS.md)
- **라이선스**: 별도 명시가 없는 한 [MIT 라이선스](LICENSE)에 따라 배포됩니다. 전체 귀속 기록은 [`AUTHORS.md`](AUTHORS.md)를 참조하십시오.
