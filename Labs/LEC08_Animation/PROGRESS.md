# Drill #8 애니메이션 뷰어 — 개발 진행 문서

- 과목: 2D 게임 프로그래밍
- 폴더: `LEC08/`
- 소스: `LEC08/animation_viewer.py`
- 라이브러리: pico2d
- 상태: **구현 완료** (요구사항 전부 충족, 보너스 2개 포함)

---

## 1. 실행 방법

```
cd LEC08
python animation_viewer.py
```

ESC 키로 종료.

---

## 2. 과제 요구사항 대비

| 항목 | 요구 | 상태 | 구현 |
|---|---|---|---|
| 애니메이션 종류 | 4종 이상 | ✅ **5종** | idle, walk, run, jump, attack |
| 정확한 재생 | 프레임 순서대로 | ✅ | `clip_draw`로 시트 프레임 순차 재생 |
| 확대 표시 | 화면 절반 이상 | ✅ | `SCALE = 5` → 320px (화면 세로 53%) |
| 무한 반복 | 전 애니메이션 무한 반복 | ✅ | 마지막 후 `anim_index` 가 첫 번째로 |
| 5회 반복 + 1초 정지 | 각 애니메이션마다 | ✅ | `REPEAT = 5`, `PAUSE = 1.0` |
| 파일 위치 | `LEC08/animation_viewer.py` | ✅ | |
| 커밋 20개 이상 | 필수 | ✅ | 20개 (Drill #8 기준) |
| 보너스 A | 프레임마다 크기가 다른 시트 | ✅ | jump(높이 변화), attack(폭 변화) |
| 보너스 B | 애니메이션별 프레임 수 상이 | ✅ | 4 / 8 / 6 / 6 / 10 |

### 제출 시 Mention 할 내용 (보너스)

**보너스 A — 프레임 크기가 프레임마다 다른 스프라이트 시트**

애니메이션을 단일 프레임 크기가 아니라 **프레임 사각형 리스트**로 저장했습니다.
`(left, bottom, width, height)` 형태이므로 프레임마다 크기가 달라도 동일하게 재생됩니다.

- `jump` — 프레임 높이가 5종으로 변함 (64 / 68 / 72 / 74 / 78). 캐릭터가 도약하며 상승
- `attack` — 프레임 폭이 9종으로 변함 (82 / 83 / 85 / 87 / 89 / 94 / 100 / 103 / 107). 검의 길이에 따라 시트 프레임 폭이 달라짐

`draw_frame()`에서 `draw_h - DRAW_H` 만큼 y를 보정해, 프레임 높이가 달라도 캐릭터의 바닥 위치가 흔들리지 않고 화면 중앙에 정렬됩니다.

**보너스 B — 애니메이션별 프레임 수가 서로 다른 경우**

프레임 수를 하드코딩하지 않고 `len(frames)`로 계산하므로 애니메이션마다 다른 프레임 수를 지원합니다.

| 애니메이션 | 프레임 수 | 프레임 크기 |
|---|---|---|
| idle | 4 | 64×64 |
| walk | 8 | 64×64 |
| run | 6 | 64×64 |
| jump | 6 | 64×64 ~ 64×78 (높이 가변) |
| attack | 10 | 82×64 ~ 107×64 (폭 가변) |

---

## 3. 파일 구성

```
LEC08/
├── animation_viewer.py   # 메인 프로그램
├── PROGRESS.md           # 본 문서
├── fonts/
│   └── consola.ttf       # 라벨 표시용 폰트
├── sprites/
│   ├── idle.png          (256×64,  4프레임)
│   ├── walk.png          (512×64,  8프레임)
│   ├── run.png           (384×64,  6프레임)
│   ├── jump.png          (384×78,  6프레임, 높이 가변)
│   └── attack.png        (919×64, 10프레임, 폭 가변)
└── tools/
    └── make_sheet.py     # 스프라이트 시트 생성 스크립트
```

### 스프라이트 시트 생성

```
cd LEC08
python tools/make_sheet.py all
```

개별 생성: `walk` / `run` / `jump` / `attack` / `idle`

PIL로 캐릭터(머리·몸통·팔·다리·검)를 프레임마다 다른 포즈로 렌더링해
가로로 이어 붙인 시트를 만듭니다. `draw_character()`가 관절 좌표를
`{'leg_a': (x, lift), ...}` 형태의 pose 딕셔너리로 받아 포즈를 정의합니다.

---

## 4. 커밋 기록 (Drill #8, 20개 이상)

| # | 커밋 메시지 (한국어) | 원문 (English) |
|---|---|---|
| 1 | LEC08 애니메이션 뷰어 진행 문서 추가 | add LEC08 animation viewer progress document |
| 2 | 스프라이트 시트 도구 및 걷기 애니메이션 추가 | add sprite sheet tool and walk animation |
| 3 | 달리기 애니메이션 스프라이트 시트 추가 | add run animation sprite sheet |
| 4 | 프레임 높이가 가변적인 점프 애니메이션 추가 | add jump animation with varying frame heights |
| 5 | 검 휘두르기 공격 애니메이션 추가 | add attack animation with sword swing |
| 6 | 대기 애니메이션 및 일괄 시트 생성 모드 추가 | add idle animation and batch sheet build mode |
| 7 | 애니메이션 뷰어용 캔버스 생성 | open canvas for animation viewer |
| 8 | 걷기 스프라이트 시트 로드 | load walk sprite sheet |
| 9 | clip_draw 헬퍼 함수 추가 및 걷기 프레임 재생 | add clip_draw helper and play walk frames |
| 10 | 걷기 애니메이션에 프레임 지연 시간 추가 | add frame delay to walk animation |
| 11 | 캐릭터를 화면 절반 이상 크기로 확대 | scale character up to fill over half of screen |
| 12 | 화면에 애니메이션 이름 및 프레임 번호 표시 | show animation name and frame index on screen |
| 13 | 달리기, 점프, 공격, 대기 스프라이트 시트 로드 | load run jump attack and idle sprite sheets |
| 14 | 애니메이션을 프레임 사각형 테이블 구조로 정리 | collect animations into table with frame rectangles |
| 15 | 애니메이션 순차 재생 및 첫 동작 복귀 루프 구현 | play animations in sequence and loop back to first |
| 16 | 동작별 5회 반복 및 1초 일시정지 추가 | repeat each animation 5 times with 1 second pause |
| 17 | 전체 진행률 표시줄 및 ESC 키 종료 기능 추가 | add sequence progress bar and escape key exit |
| 18 | 공격 및 점프 시트의 프레임별 가변 크기 지원 | support per frame size for attack and jump sheets |
| 19 | 보너스 과제(가변 프레임 크기 및 프레임 수) 문서화 | document bonus frame size and frame count support |
| 20 | 폰트 파일 번들링 및 load_font 절대 경로 적용 | bundle font file and use absolute path for load_font |
| 21 | 캔버스 위치 및 진행률 표시줄 레이아웃 상수 추출 | extract layout constants for canvas position and progress bar |
| 22 | 보너스 기능 세부 사항으로 진행 문서 업데이트 | update progress document with bonus feature details |
| 23 | refactor: LEC08 작업 내용을 Labs/LEC08_Animation으로 이전 및 정리 | refactor: move LEC08 into Labs/LEC08_Animation |

---

## 5. 구현 흐름

### Phase 0 — 준비
- [x] LEC08 폴더 및 진행 문서
- [x] 스프라이트 시트 생성 도구 (`tools/make_sheet.py`)
- [x] 5종 시트 생성

### Phase 1 — 단일 애니메이션
- [x] 캔버스 + 시트 로드
- [x] `clip_draw(left, bottom, w, h, x, y, w, h)` 헬퍼
- [x] 걷기 프레임 인덱스 증가
- [x] `delay()` 로 프레임 속도 조절
- [x] 중앙 좌표에 그리기
- [x] 5배 확대 (화면 세로 53%)

### Phase 2 — 다중 애니메이션
- [x] 애니메이션 정의를 테이블로 구조화
- [x] 순차 재생 + 첫 번째로 복귀
- [x] 5회 반복 카운터
- [x] 전환 시 1초 정지
- [x] 현재 애니메이션/프레임/반복 횟수 라벨
- [x] 전체 진행 표시줄
- [x] ESC 종료

### Phase 3 — 보너스
- [x] 프레임 사각형 리스트 구조 (jump 높이 가변, attack 폭 가변)
- [x] `len(frames)` 로 애니메이션별 프레임 수 대응
- [x] 프레임 높이 차이 중앙 정렬 보정

### Phase 4 — 마무리
- [x] 폰트 번들링 및 절대 경로 로드
- [x] 상수 추출 (`CENTER_X/Y`, `BAR_W/Y`)
- [x] 커밋 20개 이상
- [x] 12초 연속 실행 크래시 없음 검증
- [x] 헤드리스 시뮬레이션으로 순서 검증 (5회 반복 → 1초 정지 → 다음 → 무한)

---

## 6. pico2d API 메모

```python
img.clip_draw(left, bottom, width, height, x, y, w, h)
#        └── 시트 내 좌표 (왼쪽 아래 기준) ──┘  └화면좌표┘ └확대┘
```

- 시트 좌표의 `bottom`은 **왼쪽 아래 기준** (pico2d가 `self.h - bottom - height`로 변환)
- `load_font`는 SDL이 경로를 해석하므로 `os.path.abspath()` 필요
- 더미 비디오 드라이버(`SDL_VIDEODRIVER=dummy`)에서는 `load_image`가 실패하므로 로직 검증 시 스텁 처리

---

## 7. 커밋 규칙

- 한 커밋에 서로 unrelated한 변경 금지
- 커밋 메시지는 영어, 명령형, 50자 이내
- 실행 불가능한 상태로 커밋하지 않음
- 커밋 전 `git status`로 의도한 파일만 stage
