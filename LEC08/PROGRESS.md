# Drill #8 애니메이션 뷰어 — 개발 진행 문서

- 과목: 2D 게임 프로그래밍
- 폴더: `LEC08/`
- 소스: `LEC08/animation_viewer.py`
- 라이브러리: pico2d
- 상태: 계획 수립 완료 / 구현 대기

---

## 1. 과제 요구사항 (채점 기준)

| 항목 | 요구 | 배점 | 상태 |
|---|---|---|---|
| 애니메이션 종류 | 4종 이상 (걷기, 뛰기, 점프, 공격 등) | 2 | ☐ |
| 정확한 재생 | 스프라이트 시트 기준 프레임 순서대로 재생 | 2 | ☐ |
| 확대 표시 | 캐릭터가 화면 절반 이상 차지 | 1 | ☐ |
| 무한 반복 | 전 애니메이션을 차례로 무한 반복 | 1 | ☐ |
| 보너스 A | 프레임마다 크기가 다른 스프라이트 시트 | +2 | ☐ |
| 보너스 B | 애니메이션별 프레임 수가 서로 다른 경우 | +2 | ☐ |
| 파일 위치 | `LEC08/animation_viewer.py` | 필수 | ☐ |
| 커밋 | 로그 20개 이상, 각각 의미 있게 | 필수 | ☐ |

### 재생 방식 상세
1. 화면 중앙에서 애니메이션 재생
2. 각 애니메이션 5회 반복
3. 1회 반복을 마치면 1초 정지
4. 모든 애니메이션을 순서대로 무한 반복

---

## 2. 파일 구성 계획

```
LEC08/
├── animation_viewer.py   # 메인 프로그램
├── sprites/              # 스프라이트 시트 원본
│   └── walk.png
├── tools/                # 시트 생성/점검 스크립트 (개발용)
│   └── make_sheet.py
└── PROGRESS.md           # 본 문서
```

---

## 3. 커밋 계획 (20개 이상)

한 커밋 = 동작 하나. 각 커밋은 실행 가능한 상태를 유지한다.

| # | 커밋 메시지 | 내용 |
|---|---|---|
| 1 | `LEC08: 폴더 및 진행 문서 구성` | 폴더 생성, 본 문서 추가 |
| 2 | `add LEC08 project metadata to gitignore` | 생성물 제외 규칙 |
| 3 | `open 800x600 canvas for animation viewer` | 캔버스 생성 |
| 4 | `load walk sprite sheet image` | 이미지 1장 로드 |
| 5 | `clip_draw helper to cut single frame` | 클리핑 드로우 헬퍼 |
| 6 | `play walk animation frames in order` | 걷기 프레임 순차 재생 |
| 7 | `add frame delay for walk animation` | 프레임 간 지연 |
| 8 | `draw character at canvas center` | 중앙 정렬 |
| 9 | `scale sprite sheet up to half of screen` | 확대 배율 적용 |
| 10 | `add run sprite sheet asset` | 뛰기 시트 추가 |
| 11 | `add jump sprite sheet asset` | 점프 시트 추가 |
| 12 | `add attack sprite sheet asset` | 공격 시트 추가 |
| 13 | `collect animation definitions into list` | 애니메이션 목록화 |
| 14 | `loop over animations in sequence` | 애니메이션 순차 재생 |
| 15 | `repeat each animation 5 times` | 5회 반복 제어 |
| 16 | `pause 1 second after each animation` | 전환 정지 |
| 17 | `restart sequence after last animation` | 무한 반복 |
| 18 | `show current animation name on screen` | 현재 애니메이션 라벨 |
| 19 | `support per-frame width and height` | 프레임별 크기 가변 (보너스 A) |
| 20 | `support different frame count per animation` | 애니메이션별 프레임 수 (보너스 B) |
| 21 | `load sprite sheets with transparency key` | 투명 배경 처리 |
| 22 | `update PROGRESS with bonus features done` | 문서 갱신 |
| 23 | `final review of animation viewer` | 최종 정리 |

> 현재 저장소 커밋 7개. Drill #8 에서 최소 13개 이상 추가해 20개 이상을 확보한다.

---

## 4. 구현 순서 (Phase)

### Phase 0 — 준비
- [x] LEC08 폴더 생성
- [x] 진행 문서 작성
- [ ] .gitignore에 생성물(임시 이미지) 추가

### Phase 1 — 스프라이트 시트 확보
- [ ] 제작 방법 결정 (PIL 직접 생성 / 무료 이미지 검색)
- [ ] 4종 시트 확보 (걷기 / 뛰기 / 점프 / 공격)
- [ ] 프레임 수·프레임 크기 표 작성
- [ ] `tools/make_sheet.py` 로 시트 생성 또는 검색 결과 저장
- [ ] 투명 배경(PNG) 확인

| 애니메이션 | 프레임 수 | 프레임 크기 | 확대 배율 |
|---|---|---|---|
| 걷기 (walk) | 8 | 64×64 | 4.0 |
| 뛰기 (run) | 8 | 64×64 | 4.0 |
| 점프 (jump) | 6 | 64×64 | 4.0 |
| 공격 (attack) | 10 | 64×64 | 4.0 |

> 64×64 × 4 = 256px → 800×600 화면에서 세로 42%, 가로 32%. "화면 절반 이상" 충족 여부는 실행 화면으로 확인 후 배율 조정.

### Phase 2 — 단일 애니메이션 재생
- [ ] 캔버스 + 시트 로드
- [ ] `clip_draw(left, top, w, h, x, y, w, h)` 헬퍼
- [ ] 걷기 프레임 인덱스 증가
- [ ] `delay()` 로 프레임 속도 조절
- [ ] 중앙 좌표 계산

### Phase 3 — 확대
- [ ] 확대 배율 상수 적용
- [ ] 프레임 사각형(바닥 정렬) 유지 확인

### Phase 4 — 다중 애니메이션 + 무한 반복
- [ ] 애니메이션 정의 리스트
- [ ] 5회 반복 카운터
- [ ] 전환 시 1초 정지
- [ ] 마지막 애니메이션 후 처음부터

### Phase 5 — 보너스
- [ ] 프레임마다 크기가 다른 시트 지원
- [ ] 애니메이션별 프레임 수 상이 처리
- [ ] 라벨 표시

### Phase 6 — 마무리
- [ ] 실행 확인 및 FPS 점검
- [ ] 커밋 20개 이상 달성
- [ ] 문서 최종 갱신

---

## 5. 핵심 API 메모 (pico2d)

```python
open_canvas(800, 600)
img = load_image('sprites/walk.png')

# 시트에서 한 프레임만 잘라서 그리기
img.clip_draw(left, top, w, h, x, y, dw, dh)   # dw, dh = 확대된 크기

clear_canvas()
update_canvas()
delay(0.1)          # 1초 정지
delay(0.08)         # 프레임 간 지연

# 프레임 좌표 계산
left = index * FRAME_W
top  = 0
```

주의: `Image.clip_draw(left, top, width, height, x, y, w, h)` — 앞 4개는 원본 시트 내 좌표, 뒤 3개는 화면 좌표와 크기.

---

## 6. 결정 필요 사항

- [ ] 스프라이트 시트를 직접(PIL) 생성할지, 무료 이미지 검색 결과로 쓸지
- [ ] 보너스 A(프레임별 크기 가변)를 실제 시트로 구현할지
- [ ] 애니메이션 라벨 텍스트를 화면에 표시할지 (pico2d `load_font` 필요)

---

## 7. 커밋 규칙

- 한 커밋에 서로 unrelated한 변경 금지
- 커밋 메시지는 영어, 명령형, 50자 이내
- 실행 불가능한 상태로 커밋하지 않음
- 커밋 전 `git status`로 의도한 파일만 stage
