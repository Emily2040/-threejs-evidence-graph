<!-- source_version: 2026.07.4; translation_status: reviewed; language: ko -->
# Three.js Evidence Graph: 운영 매뉴얼 v2.0 동반 가이드

[English](EVIDENCE_GRAPH_GUIDE.md) | [简体中文](EVIDENCE_GRAPH_GUIDE.zh-CN.md) | [日本語](EVIDENCE_GRAPH_GUIDE.ja.md) | [한국어](EVIDENCE_GRAPH_GUIDE.ko.md)

![제품 계약에서 작업 범위가 제한된 전문 에이전트 작업, 독립 증거 수집, 릴리스 게이트로 분기되는 제어 계층](../assets/evidence-graph-control-hero.jpg)

## 1. 목적 및 핵심 명제

*Three.js Evidence Graph: Operational Manual v2.0*([`publications/threejs-evidence-graph-operational-manual-v2.0-en.pdf`](../publications/threejs-evidence-graph-operational-manual-v2.0-en.pdf), 총 64페이지, `416,827`바이트, SHA-256 `d3830d411a61c52c92d6d9f4454d317a5e5bb7dbc3660824e7d24b7a959eb6cd`)은 외부 런타임 에셋을 다운로드하지 않고 범위가 명확한 소스 생성형 Three.js 브라우저 게임 버티컬 슬라이스(vertical slice)를 제작하기 위한 저장소 로컬 증거 그래프(Evidence Graph) 기반 멀티 에이전트 제작 시스템을 정의합니다.

단일 대화가 빌더, 비평가, 릴리스 승인 권한을 동시에 행사하는 대신, 증거 그래프(Evidence Graph)는 권한을 네 계층으로 분리합니다.

- **결정론적 제어 계층(`orchestrator`)**: 그래프 상태(`schemas/graph-state.d.ts`)를 관리하고, 범위가 제한된 작업 패킷(`schemas/task-packet.schema.json`)을 배포하며, 컴퓨팅 및 재시도 예산을 강제하고, 수정이 수렴하지 않을 경우 승인된 기준선(`accepted_baseline_commit`)으로 자동 롤백합니다.
- **작업 범위가 제한된 전문 에이전트 빌더(6개 역할)**: `combat_gameplay`, `world_quest`, `procedural_art_vfx`, `procedural_audio`, `ui_hud_accessibility`, `qa_perf_playwright`. 각 전문 에이전트는 허용된 `allowed_paths`에만 파일을 작성할 수 있으며 인계 전에 기계적 인수 명령(acceptance command)을 통과해야 합니다.
- **보정된 읽기 전용 비평가(`independent_critic`)**: 소스 코드 쓰기 권한 없이, 캡처된 시각 프레임, 오프라인 렌더링 오디오, 결정론적 리플레이 텔레메트리, 외부 에셋 제로 출처 추적 정보(provenance)를 제시 순서 반전 쌍으로 평가합니다.
- **두 가지 증거 체계(Evidence Regimes)**:
  - **체계 A(`A-PinnedBrowser`)**: 고정된 Chromium + GPU/SwiftShader 컨테이너 내부에서 60 Hz 정수 틱 시뮬레이션 상태(`state_hash`), 16비트 PCM 양자화 `OfflineAudioContext` 버퍼(`audio_hash`), `1e-5` 양자화 절차적 기하(`geometry_hash`)에 대해 비트 단위 SHA-256 일치를 검증합니다.
  - **체계 B(`B-CrossPlatform`)**: 이기종 하드웨어 및 브라우저(`webgpu` 기본 경로 및 `webgl2-fallback` 폴백 경로) 전반에서 불변 조건과 사전 선언 허용 오차(declared tolerance)를 검증합니다.

---

## 2. 64페이지 운영 매뉴얼의 8개 장 구조 및 부록

| 장 | 페이지 | 핵심 범위 및 규범 산출물 |
| :--- | :--- | :--- |
| **Delta v1 -> v2 결함 원장** | p. 04 | 프롬프트에만 의존하던 v1 워크플로의 10가지 구조적 결함(`DOC-001`부터 `DOC-010`)과 이에 대응하는 v2.0 아키텍처 통제 장치를 매핑합니다. |
| **00. 진단(Diagnosis)** | pp. 05-09 | 단일 대화 기반 대규모 3D 게임 생성이 실패하는 원인(컨텍스트 드리프트, 셰이더 컴파일 지연, 증거 없는 자체 합격 선언, 보정되지 않은 시각 평가)을 분석합니다. |
| **01. 제어 계층(Control plane)** | pp. 10-17 | 15개 노드 유향 순환 증거 그래프(`N00_BRIEF`부터 `N14_RELEASE_CANDIDATE`), 권한 계층, 파일 쓰기 격리, 저장소 디렉터리 구조를 정의합니다. |
| **02. Three.js 아키텍처(Three.js architecture)** | pp. 18-29 | Three.js `r185`(`0.185.0`), `THREE.WebGPURenderer`와 `{ forceWebGL: true }` 폴백, TSL 노드 머티리얼, `compileAsync` + `postProcessing.renderAsync()` 사전 컴파일, 프레임 시간 예산(`P50 <= 8.3 ms`, `P95 <= 16.6 ms`, `P99 <= 22.0 ms`)을 규정합니다. |
| **03. 무에셋 절차적 제작(Asset-free production)** | pp. 30-36 | 절차적 생성을 컴파일로 다루며 시드 고정 PRNG, 절차적 생성 문법(procedural grammar), TSL 표면 머티리얼, Web Audio 오프라인 합성(`-16 LUFS +/- 2`, `-1.0 dBTP`)을 정의합니다. |
| **04. 증거와 수렴(Evidence + convergence)** | pp. 37-45 | Playwright 텔레메트리 캡처(`window.__rpgReady`, `window.__rpgQA`), 체계 A/B 결정론 게이트, 평가자 보정(critic calibration), `DefectRecord` 근본 원인 수정 루프(최대 3회 재시도 후 롤백)를 규정합니다. |
| **05. 운영 및 컴퓨팅 경제성(Operations)** | pp. 46-48 | 모델 등급 라우팅, 실행 단위 비용 원장(`cost_ledger`), 공급망 출처 감사, 지정된 인간 디렉터(`human_signoff`) 승인 권한을 정의합니다. |
| **06. 프롬프트 언어(Prompt language)** | pp. 49-52 | 4부 구성의 오케스트레이터 시스템 프롬프트와 전문 에이전트 위임 템플릿을 제공합니다([`prompts/evidence-graph/orchestrator.md`](../prompts/evidence-graph/orchestrator.md)에 수록). |
| **07. 구현 프로그램(Implementation program)** | pp. 53-57 | `N00_BRIEF`부터 `N14_RELEASE_CANDIDATE`까지의 단계별 실행 절차와 v1-to-v2 마이그레이션 체크리스트를 제시합니다. |
| **부록 A-B 및 1차 참고문헌(Appendices A-B & Primary Sources)** | pp. 58-64 | 규범적 JSON Schema([`schemas/`](../schemas/)에서 Draft 2020-12로 업그레이드됨)와 클릭 가능한 URI 링크 주석이 포함된 23개 1차 기술 참고문헌을 수록합니다. |

---

## 3. 표준 15개 노드 제작 그래프(`N00`부터 `N14`)

1. `N00_BRIEF`(`01 BRIEF_COMPILE`): 제품 브리프, 범위 제외 항목, 슬라이스 플레이 시간 목표 확정.
2. `N01_CONTRACTS`(`02 CONSTITUTION_AUDIT`): JSON Schema(`task-packet`, `defect-record`, `run-manifest`) 및 시드 불변 조건 동결.
3. `N02_SCAFFOLD`(`03 ARCHITECTURE_DECISION`): 결정론적 60 Hz 시뮬레이션 클록, PRNG, Three.js `r185` `WebGPURenderer` 부트 하네스 구축.
4. `N03_ASSET_COMPILER`(`04 ART+GAMEPLAY_BIBLE_FREEZE`): 절차적 생성 문법, 색상 팔레트 규칙, TSL 머티리얼 계약 동결.
5. `N04_WORLD_GRAPH`(`05 MILESTONE_PLAN`): 설계된 고정 경로, 충돌 볼륨, 체크포인트 상태 그래프 구축.
6. `N05_RENDER_PIPELINE`(`06B PROCEDURAL + RENDER + AUDIO` - 렌더): 조명, `PMREMGenerator`, `InstancedMesh`/`BatchedMesh`, `THREE.PostProcessing` 구성.
7. `N06A_GAMEPLAY_COMBAT`(`06A GAMEPLAY + CAMERA WORKERS`): 정수 틱 전투 상태 머신, 적 유형, 보스 페이즈 전환, 카메라 충돌 구현.
8. `N06B_AUDIO_SYNTH`(`06B PROCEDURAL + RENDER + AUDIO` - 오디오): 절차적 Web Audio 합성 및 `OfflineAudioContext` 라우드니스/PCM 해시 검증 구현.
9. `N07_UI_HUD_A11Y`(`07 INTEGRATION`): HUD, 조작 재매핑, 고대비/모션 감소 모드, 버전 관리 저장 스키마 통합.
10. `N08_TELEMETRY_HARNESS`(`08 STATIC_VERIFICATION`): 정적 검증 실행 및 `window.__rpgReady` / `window.__rpgQA` 진단 훅 연결.
11. `N09_REPLAY_RUNNER`(`09 DETERMINISTIC_REPLAY`): 시드 기반 결정론적 리플레이 실행 및 `state_hash`, `audio_hash`, `geometry_hash` 기록.
12. `N10_PERF_GATE`(`10 EVIDENCE_CAPTURE`): 1920x1080 프레임 시간 백분위수, 드로콜, 삼각형 수, GPU 메모리 텔레메트리 캡처.
13. `N11_VISUAL_AUDIO_CRITIC`(`11 INDEPENDENT_CRITICISM`): 보정된 읽기 전용 비평가의 시각, 오디오, 게임플레이 평가 실행.
14. `N12_PROVENANCE_AUDIT`(`12 EVIDENCE_REDUCTION`): 런타임 외부 네트워크 요청 0건 및 다운로드 에셋 0건 출처 감사.
15. `N13_REPAIR_ROUTER`(`13 DECIDE` / `14 CROSS-BROWSER_RELEASE_AUDIT`): `P0`-`P2` 등급 `DefectRecord`를 단일 쓰기 소유 에이전트로 라우팅(최대 3회 수정 주기)하거나 미수렴 시 `accepted_baseline_commit`으로 롤백.
16. `N14_RELEASE_CANDIDATE`(`15 RELEASE_CANDIDATE`): `cost_ledger`와 `human_signoff`가 포함된 검증된 `run-manifest.json` 산출.

---

## 4. 저장소 독립형 스키마, 프롬프트 및 골든 픽스처

- **규범적 JSON Schema(Draft 2020-12) 및 상태 인터페이스**: [`schemas/task-packet.schema.json`](../schemas/task-packet.schema.json), [`schemas/defect-record.schema.json`](../schemas/defect-record.schema.json), [`schemas/run-manifest.schema.json`](../schemas/run-manifest.schema.json), [`schemas/graph-state.d.ts`](../schemas/graph-state.d.ts)
- **복사 가능한 오케스트레이터 프롬프트**: [`prompts/evidence-graph/orchestrator.md`](../prompts/evidence-graph/orchestrator.md)
- **골든 검증 픽스처**: [`examples/run-0001/`](../examples/run-0001/)
- **기술 정오표 및 v2.0 정렬 명세**: [`docs/TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md`](TECHNICAL_ERRATA_AND_V2_ALIGNMENT.md)
