<!-- source_version: 2026.07.5; translation_status: reviewed; language: ko -->

# 《유리 납골당》(The Glass Ossuary): 미스터리 호러 개발 규격 및 아키텍처 가이드

<div align="center">

[![English](https://img.shields.io/badge/Language-English-4FA89B?style=for-the-badge)](THE_GLASS_OSSUARY_GUIDE.md)
[![Simplified Chinese](https://img.shields.io/badge/语言-简体中文-C89B54?style=for-the-badge)](THE_GLASS_OSSUARY_GUIDE.zh-CN.md)
[![Japanese](https://img.shields.io/badge/言語-日本語-B8423A?style=for-the-badge)](THE_GLASS_OSSUARY_GUIDE.ja.md)
[![Korean](https://img.shields.io/badge/언어-한국어-4FA89B?style=for-the-badge)](THE_GLASS_OSSUARY_GUIDE.ko.md)

[![마스터 스위트로 돌아가기](https://img.shields.io/badge/←_마스터_스위트-README.ko-16202A?style=flat-square&borderColor=4FA89B)](../README.ko.md)
[![장르](https://img.shields.io/badge/장르-1인칭_조사형_미스터리_호러-4FA89B?style=flat-square)](../publications/the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf)
[![분량](https://img.shields.io/badge/출판물-36쪽_PDF-C89B54?style=flat-square)](../publications/the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf)
[![골든 픽스처](https://img.shields.io/badge/골든_픽스처-examples%2Frun--0002-3DBE8B?style=flat-square)](../examples/run-0002/run-manifest.json)

| 출판물 표지 (36쪽) | 현장 조사 컨셉 (`Refraction Gallery`) | 보스전 컨셉 (`The Choir in the Glass`) |
| :---: | :---: | :---: |
| <a href="../publications/the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf"><img src="../assets/the-glass-ossuary-cover.jpg" width="210" alt="《유리 납골당》 v1.0 표지" /></a> | <img src="../assets/glass-ossuary-investigation-hero.jpg" width="340" alt="《유리 납골당》의 굴절 회랑에서 포렌식 조사를 수행하는 Clara Vane" /> | <img src="../assets/glass-ossuary-apparition-hero.jpg" width="340" alt="《유리 납골당》 최심부 대성당에서 현현하는 2페이즈 보스 유리 속의 성가대" /> |

*본 이미지들은 출판물용 컨셉 아트워크이며, 실제 게임플레이 캡처나 구현 완료 증거가 아닙니다.*

</div>

> **문서 위상 안내**
>
> 본 문서는 《The Glass Ossuary: Mystery Horror Full Multi-Agent Production Prompt v1.0》([`publications/the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf`](../publications/the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf), 총 36쪽, `98,649` 바이트, SHA-256 `efead090be003782a122463ba17fe686caa1c30aeafcf66f11d294555c7aafda`)의 한국어 네이티브 기술 가이드입니다. 1인칭 조사형 심리 호러 버티컬 슬라이스의 핵심 게임플레이 루프, 60 Hz 고정 틱 음향·광학 포렌식 장비 프레임 테이블, 6노드 추리 보드 분기, 2페이즈 보스 설계 및 Evidence Graph v2.0 검증 하네스를 다룹니다. 본 저장소는 아키텍처 규격서와 멀티 에이전트 프롬프트 패키지를 제공하며, 실행 가능한 런타임 게임 빌드는 아직 포함하지 않습니다.

---

## 1. 규격서 개요 및 핵심 설계 철학

《유리 납골당》(*The Glass Ossuary*)은 *Three.js Evidence Graph* 스위트의 **미스터리 호러(Mystery on Horror)** 플래그십 규격서입니다. Three.js `r185`(`0.185.0`) 환경에서 **외부 바이너리 에셋 다운로드 없이**(외부 `.glb`, 텍스처, 폰트, 사전 녹음 오디오 파일 무사용) 오직 저장소 내 소스 코드와 시드(Seed)만으로 **플레이 타임 12~16분** 분량의 1인칭 조사 호러 버티컬 슬라이스를 구축하는 엔지니어링 계약을 정의합니다.

단순한 스크립트형 점프 스케어(Jump Scare)를 배제하고, **물리적 포렌식 장비 조작**과 **결정론적 60 Hz 음향·광학 상태 머신**을 통해 공포와 추리의 긴장감을 조성합니다.

- **목표 플레이 시간**: 12~16분 (단일 씬 그래프로 연결된 5개 해안 관측소 공간).
- **주인공**: **Clara Vane** (음향 기록 보관관 / `The Acoustic Archivist`). 핵심 생존 지표는 **`100 침착성(Composure)`**, **`100 랜턴 오일(Lantern Oil)`**, **`0–100 정신 침식도(Exposure)`**.
- **3종의 다이어제틱 포렌식 장비**: `이중 초점 황동 루페`(`brass_loupe`), `밀랍 실린더 축음기`(`wax_phonograph`), `은염 페로타입 건판 카메라`(`ferrotype_plate`).
- **6노드 추리 보드(Inquest Board)**: 수집한 6개의 단서를 연결해 3가지 상호 배타적 가설(`렌즈 사보타주`, `조수 격리 봉쇄`, `음향 강령 공명`) 중 하나를 확정하며, 선택한 가설이 괴이의 어그로 규칙과 보스전 약점 노출 시간을 직접 변경합니다.
- **3종의 괴이(Apparitions) 및 2페이즈 보스**: `진창의 경청자`(`Mire Listener`), `유리 격막의 감시자`(`Glass Septum Watcher`), `익사한 성가대원`(`Drowned Chorister`), 그리고 최종 보스 **`유리 속의 성가대`(`The Choir in the Glass`, `600 공명 무결성`)**.
- **2가지 최종 평결 엔딩**: `VERDICT_PUBLISH`(생반 음향 난파 원장 공개) 또는 `VERDICT_SUBMERGE`(수문 개방으로 납골당 영구 수몰).

---

## 2. 세계관 배경 및 절차적 머티리얼 문법

배경은 1894년 가을 폭풍우가 몰아치는 **생반 해안 관측소(Saint-Vane Coastal Observatory)**입니다. 상층부의 프레넬 등대 렌즈 어레이와 지하 조수 납골당이 결합된 구조로, 아치형 내벽은 난파선 사망자들의 마지막 목소리를 가두기 위해 골회와 납유리를 합금한 ‘골유리(Bone-Glass)’ 공명 리브로 마감되어 있습니다.

| 머티리얼 패밀리 | 컬러 토큰 | Three.js `r185` TSL 절차적 셰이더 및 지오메트리 규격 |
| :--- | :--- | :--- |
| **심연 조수 슬레이트 (Abyssal Tide Slate)** | `#070B10` | 조수 높이 맵과 젖은 소금 결정 스페큘러를 지닌 주상절리 현무암 |
| **소금 서리 현무암 (Salt-Frosted Basalt)** | `#16202A` | 보로노이(Voronoi) 소금 결정 노이즈 법선 섭동을 적용한 구조 리브 |
| **우지 앰버 (Tallow Amber)** | `#C89B54` | 2100K 방풍 랜턴 조명 콘. 셔터 개폐 및 오일 소모 곡선과 연동 |
| **은염 시안 (Silver-Halide Cyan)** | `#4FA89B` | 골유리 굴절 분산(`ior: 1.54`) 및 페로타입 UV 플래시 네거티브 반전 하이라이트 |
| **동맥 러스트 (Arterial Rust)** | `#B8423A` | 수문 쇠사슬, 밀랍 인장 및 고침식도(Exposure) 경고 비네트 |

*팔레트 가드레일(Palette Guardrail)*: 흔한 AI 템플릿 보라색(`#7567F5`) 및 고채도 네온 마젠타는 모든 절차적 셰이더, UI 오버레이, 골유리 굴절 커스틱스에서 엄격히 금지됩니다.

---

## 3. 10비트 조사 진행 루트 (`case_saint_vane`)

| 비트 | 공간 구역 | 포렌식 목표 및 핵심 메커니컬 게이트 |
| ---: | :--- | :--- |
| **01** | **조수 제방길 (`Tidewater Causeway`)** | 폭풍 속 상륙; 수중 청음기 발소리, `Lantern Shutter`(`6 ticks` 토글) 및 오일 소모율 보정 |
| **02** | **관리인의 박리실 (`Caretaker's Stripping Room`)** | 안전 허브; 6노드 `Inquest Board`(추리 보드) 확인 및 관리인 Moreau의 밀랍 실린더(`case_saint_vane`) 재생 |
| **03** | **전실 보정 구역 (`Vestibule Threshold`)** | `은염 페로타입 건판 카메라`(`19..24 ticks` UV 플래시 판정, `6.5 m` 내 `150 ticks` 기절) 튜토리얼 |
| **04** | **굴절 회랑 (`Refraction Gallery`)** | 랜턴 셔터 제어로 `Glass Septum Watcher`의 시야 콘을 회피하며 `이중 초점 황동 루페`(`75 ticks`)로 미세 균열 해독 |
| **05** | **프리즘 삼각측량 (`Prism Triangulation`)** | 3중 동심 프레넬 렌즈 링(`45 deg`, `135 deg`, `270 deg`)을 정렬해 숨겨진 《조수 원장 단편》(`Tide Ledger Fragment`) 획득 |
| **06** | **수몰된 지하 묘실 (`Submerged Crypt`)** | 무릎 깊이의 침수 구간에서 `Mire Listener`와 `Drowned Chorister`를 피해 `110/220/330 Hz` 수문 공명기를 축음기로 동조, 《수중 청음 실린더》 회수 |
| **07** | **추리 보드 평결 (`Inquest Board Deduction`)** | 6개 단서를 모두 연결하고 3대 가설(`lens_sabotage`, `tidal_quarantine`, `acoustic_calling`) 중 하나를 확정 |
| **08** | **납골당 봉인 해제 (`Ossuary Unsealing`)** | 《생반 마스터 인장》으로 음향 격벽을 개방하고 최심부 골유리 대성당으로 하강 |
| **09** | **유리 납골당 (`The Glass Ossuary`)** | 2페이즈 보스 **`유리 속의 성가대`(`The Choir in the Glass`, `600 공명 무결성`)** 조우전 |
| **10** | **기록 전신실 (`Archive Telegraph`)** | `VERDICT_PUBLISH` 또는 `VERDICT_SUBMERGE`를 선택하고 버전 관리된 로컬 세이브에 영구 기록 |

---

## 4. 60 Hz 결정론적 포렌식 장비 및 잠입 프레임 테이블

모든 액션은 60 Hz 정수 틱(`1 tick = 16.6667 ms`) 단위로 구동됩니다. 광학 가시성 상태(`LANTERN_OPEN` / `LANTERN_SHUTTERED`)와 음향 역위상 마스킹(`PHONOGRAPH_CANCEL_ACTIVE`)은 직교 비트마스크 채널로 분리되어, 랜턴 셔터를 여닫아도 활성화된 축음기 위상 상쇄 효과가 절대 덮어써지지 않습니다.

<div align="center">
  <img src="../assets/svg/game-02-telemetry-ko.svg" width="100%" alt="《유리 납골당》 60 Hz 포렌식 장비 프레임 타임라인, 컬러 팔레트 및 음향 임계값 다이어그램" />
</div>

| 액션명 | 선딜레이 (Startup) | 판정 구간 (Active Window) | 후딜레이 (Recovery) | 총 틱 | 자원 소모 및 메커니컬 효과 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **랜턴 셔터 (`Lantern Shutter`)** | `6 ticks` | 토글 (`7..`) | `6 ticks` | `12 ticks` | `오일 0`; 조명 콘을 즉시 차단하고 광학 시야 어그로 해제 |
| **황동 루페 초점 (`Brass Loupe Focus`)** | `9 ticks` | 홀드 (`10..69`) | `6 ticks` | `75 ticks` | `오일 0`; 프리즘 눈금 및 골유리 미세 각인 해독 |
| **축음기 위상 상쇄 (`Phonograph Cancel`)** | `24 ticks` | `Ticks 25..114` | `36 ticks` | `150 ticks` | 실내 공명파 상쇄; `Mire Listener`로부터 발소리 데시벨 은폐 |
| **페로타입 플래시 (`Ferrotype Flash`)** | `18 ticks` | `Ticks 19..24` | `66 ticks` | `90 ticks` | 숨겨진 골유리 이음매 감광; 반경 `6.5 m` 내 괴이 `150 ticks` 기절 |
| **앉아 옆걸음 (`Crouch Sidestep`)** | `5 ticks` | `Ticks 6..16` | `12 ticks` | `28 ticks` | 젖은 석판 및 철제 그레이팅 위 발소리를 `<= -38 dBFS`로 억제 |
| **장뇌 후각염 (`Smelling Salts`)** | `15 ticks` | `Ticks 16..45` | `10 ticks` | `55 ticks` | `침착성(Composure) +40` 회복 및 `정신 침식도(Exposure) -25` 정화 |

---

## 5. 괴이 생태계 및 2페이즈 보스: 유리 속의 성가대 (The Choir in the Glass)

### 3종 괴이 아키타입
1. **진창의 경청자 (`Mire Listener`)**: 시력이 없는 수륙양용 음향 포식자. 물장구, 달리기, 혹은 마스킹되지 않은 축음기 태엽 소리가 `-28 dBFS`를 초과하면 해당 좌표로 급습합니다.
2. **유리 격막의 감시자 (`Glass Septum Watcher`)**: 회전하는 프레넬 유리 격막 내부에 갇힌 굴절 실루엣. 열린 랜턴 조명 콘이나 직시야에 들어올 때만 접근하며, 랜턴 셔터를 닫으면 즉시 정지합니다.
3. **익사한 성가대원 (`Drowned Chorister`)**: 반경 `4.5 m`의 저주파 허밍 오라를 두른 채 배회하는 망령. 축음기 역위상 파형으로 중화하지 않으면 지속해서 `침착성`을 깎고 `침식도`를 누적시킵니다.

### 2페이즈 보스: 유리 속의 성가대 (`The Choir in the Glass`, `600 공명 무결성`)
- **조형 구조**: 높이 `5.2 m` 규모의 매달린 골유리 파이프 오르간과 조수 벨자(Bell-Jar) 결합체로, 7구의 융합된 성가대 실루엣이 은염 공명 심장을 감싸고 있습니다.
- **1페이즈 (`600 -> 301 무결성`)**: `Refractive Blind`(프리즘 빔 소사, 랜턴 차폐 및 기둥 엄폐 필수), `Tidal Undertow`(발밑 역류 견인), `Shatter Harmonic`(바닥 유리 가시 예고), `Hollow Hymn`(화음 충격파)을 구사합니다. `Hollow Hymn` 시전 중 축음기 위상 상쇄(`ticks 25..114`)를 맞추면 중앙 공명 코어가 `150 ticks` 동안 노출됩니다.
- **2페이즈 (`300 -> 0 무결성`)**: 외곽 벨자가 깨지며 3개의 회전 프레넬 미러 링으로 분리되고 `Prism Split`, `Glass Lung Vacuum`, `Echoing Verdict`, `Final Exposure` 패턴이 추가됩니다. 위상 상쇄로 음향 장막을 벗겨낸 뒤 `6.5 m` 이내로 파고들어 `은염 페로타입 건판 카메라`(`ticks 19..24`) 플래시를 적중시켜 3개의 공명 봉인을 파괴해야 합니다.

---

## 6. 6노드 추리 보드 및 3대 가설 분기

비트 07(`Inquest Board Deduction`)에서 6개 물리 단서를 연결하면 `GraphState.active_relic`에 기록되는 3가지 가설 중 하나를 확정할 수 있습니다.

- **`렌즈 사보타주` (`lens_sabotage`)**: 등대 프레넬 렌즈가 증기선 메리디언호의 좌초를 유도하기 위해 고의로 조작되었음을 입증합니다. `황동 루페` 조사 거리가 `+35%` 증가하고 `페로타입 플래시` 기절 시간이 `+30 ticks` 연장됩니다.
- **`조수 격리 봉쇄` (`tidal_quarantine`)**: 관리인 Moreau가 음향 전염을 막기 위해 스스로 지하 묘실을 수몰시켰음을 입증합니다. 수중 이동 시 `정신 침식도` 축적 속도가 `-30%` 감소하고 랜턴 오일 효율이 `+25%` 향상됩니다.
- **`음향 강령 공명` (`acoustic_calling`)**: 골유리 리브가 난파선 사망자들의 주파수를 증폭하는 음향 송수신기로 설계되었음을 입증합니다. `밀랍 실린더 축음기` 위상 상쇄 유효 구간이 `+24 ticks` 넓어지고 보스의 공명 무결성에 가하는 피해가 `+20%` 증가합니다.

---

## 7. 독립 프롬프트, JSON 스키마 및 골든 픽스처

- **마스터 오케스트레이터 프롬프트**: [`prompts/glass-ossuary/orchestrator.md`](../prompts/glass-ossuary/orchestrator.md) ([`orchestration/prompts/glass-ossuary-orchestrator.md`](../orchestration/prompts/glass-ossuary-orchestrator.md) 미러링)
- **7종 전문 에이전트 카드**: [`prompts/glass-ossuary/agents/`](../prompts/glass-ossuary/agents/)
- **골든 레퍼런스 픽스처 (`run-0002`)**: [`examples/run-0002/task-packet.json`](../examples/run-0002/task-packet.json), [`examples/run-0002/defect-record.json`](../examples/run-0002/defect-record.json), [`examples/run-0002/run-manifest.json`](../examples/run-0002/run-manifest.json)
- **시리즈 4권 동반 가이드**:
  - [`docs/EVIDENCE_GRAPH_GUIDE.ko.md`](EVIDENCE_GRAPH_GUIDE.ko.md) (《Three.js Evidence Graph v2.0 운영 매뉴얼》, 64쪽)
  - [`docs/THE_HOLLOW_MERIDIAN_GUIDE.ko.md`](THE_HOLLOW_MERIDIAN_GUIDE.ko.md) (《공허의 자오선 v1.0》, 81쪽)
  - [`docs/PERIHELION_BREACH_GUIDE.ko.md`](PERIHELION_BREACH_GUIDE.ko.md) (《근일점 돌파 v1.0》, 36쪽)
