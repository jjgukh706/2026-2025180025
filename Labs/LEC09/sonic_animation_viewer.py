"""
[LEC09] 소닉 애니메이션 뷰어 (Sonic Animation Viewer)
- 10종 동작, 총 76프레임 순차 재생
- 각 동작 5회 반복 후 1초 일시정지
- 10종 전체 무한 순환
- 원본 스프라이트 4배 확대 렌더링
- pico2d 라이브러리 기반 구현
"""

import os
from pico2d import *

# 작업 디렉터리를 스크립트 위치로 변경
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 캔버스 및 레이아웃 설정
CANVAS_W = 800
CANVAS_H = 600
CENTER_X = CANVAS_W // 2
CENTER_Y = CANVAS_H // 2
SCALE = 4
BASE_H = 39 * SCALE

REPEAT_LIMIT = 5
PAUSE_DURATION = 1.0

BAR_W = 600
BAR_H = 12
BAR_Y = 40

# --- 10종 애니메이션 동작 데이터 (총 76프레임) ---
# 형식: (left, bottom, width, height) - pico2d 기준점
WALK_FRAMES = [
    (1, 447, 29, 39), (31, 447, 26, 39), (58, 447, 58, 39), (118, 447, 30, 39),
    (150, 447, 30, 39), (182, 447, 87, 39), (270, 447, 24, 39), (302, 447, 29, 39)
]
RUN_FRAMES = [
    (8, 407, 26, 39), (37, 407, 27, 39), (65, 407, 31, 39), (97, 407, 37, 39),
    (135, 407, 32, 39), (170, 407, 32, 39), (206, 407, 26, 39), (238, 407, 24, 39),
    (263, 407, 30, 39), (295, 407, 36, 39), (334, 407, 32, 39), (370, 407, 29, 39)
]
DASH_FRAMES = [
    (1, 361, 33, 43), (39, 361, 35, 43), (89, 361, 35, 43),
    (130, 361, 34, 43), (181, 361, 34, 43), (228, 361, 33, 43)
]
ROLL_FRAMES = [
    (1, 325, 29, 33), (35, 325, 29, 33), (67, 325, 30, 33), (98, 325, 31, 33),
    (131, 325, 29, 33), (162, 325, 29, 33), (193, 325, 30, 33), (230, 325, 31, 33),
    (268, 325, 30, 33)
]
SKID_FRAMES = [
    (1, 292, 30, 27), (36, 292, 29, 27), (70, 292, 29, 27),
    (105, 292, 29, 27), (139, 292, 29, 27), (174, 292, 29, 27)
]
PUSH_FRAMES = [
    (1, 251, 29, 36), (36, 251, 30, 36), (74, 251, 31, 36),
    (111, 251, 31, 36), (149, 251, 30, 36), (186, 251, 31, 36)
]
SPRING_FRAMES = [
    (1, 207, 29, 35), (36, 207, 30, 35), (72, 207, 39, 35),
    (123, 207, 39, 35), (172, 207, 39, 35), (218, 207, 38, 35)
]
SPIN_FRAMES = [
    (1, 154, 24, 45), (31, 154, 29, 45), (65, 154, 20, 45), (90, 154, 25, 45),
    (119, 154, 25, 45), (149, 154, 20, 45), (184, 154, 40, 45), (232, 154, 39, 45)
]
FALL_FRAMES = [
    (1, 108, 27, 40), (31, 108, 31, 40), (64, 108, 31, 40), (99, 108, 33, 40),
    (136, 108, 32, 40), (176, 108, 33, 40), (217, 108, 33, 40), (254, 108, 33, 40)
]
POSE_FRAMES = [
    (6, 56, 34, 43), (49, 56, 34, 43), (96, 56, 23, 43), (125, 56, 23, 43),
    (10, 0, 60, 53), (71, 0, 34, 53), (107, 0, 19, 53)
]

ACTIONS = [
    ('Walk (걷기)', WALK_FRAMES, 0.10),
    ('Run (달리기)', RUN_FRAMES, 0.07),
    ('Sprint (대시)', DASH_FRAMES, 0.05),
    ('Roll (점프/구르기)', ROLL_FRAMES, 0.07),
    ('Skid (제동)', SKID_FRAMES, 0.08),
    ('Push (밀기)', PUSH_FRAMES, 0.10),
    ('Spring (스프링 도약)', SPRING_FRAMES, 0.08),
    ('Spin Charge (회전 진입)', SPIN_FRAMES, 0.05),
    ('Fall/Hurt (낙하/피격)', FALL_FRAMES, 0.08),
    ('Pose (승리 포즈)', POSE_FRAMES, 0.12),
]


def draw_frame(sheet, frame, x, y):
    """프레임 사각형을 4배 확대하여 지면 접지면에 맞추어 렌더링"""
    left, bottom, w, h = frame
    draw_w = w * SCALE
    draw_h = h * SCALE
    y_offset = (draw_h - BASE_H) / 2
    sheet.clip_draw(left, bottom, w, h, x, y + y_offset, draw_w, draw_h)


def main():
    open_canvas(CANVAS_W, CANVAS_H)
    sheet = load_image('sonic-sprite.png')

    font_path = os.path.abspath('../LEC08_Animation/fonts/consola.ttf')
    font = load_font(font_path, 22) if os.path.exists(font_path) else None

    action_index = 0
    frame_index = 0
    repeat_count = 0
    pausing = False
    running = True

    while running:
        name, frames, interval = ACTIONS[action_index]

        clear_canvas()
        draw_frame(sheet, frames[frame_index], CENTER_X, CENTER_Y)

        # 상태 텍스트 출력
        if font:
            status_text = f"Action: {name} | Frame: {frame_index + 1}/{len(frames)} | Cycle: {repeat_count + 1}/{REPEAT_LIMIT}"
            if pausing:
                status_text += " [PAUSED 1.0s]"
            font.draw(CENTER_X - 250, CANVAS_H - 50, status_text, (255, 255, 255))

        # 전체 진행 표시줄
        total_actions = len(ACTIONS)
        progress = (action_index + (repeat_count + (frame_index + 1) / len(frames)) / REPEAT_LIMIT) / total_actions
        draw_rectangle(CENTER_X - BAR_W // 2, BAR_Y, CENTER_X + BAR_W // 2, BAR_Y + BAR_H, 60, 60, 60)
        draw_rectangle(CENTER_X - BAR_W // 2, BAR_Y, CENTER_X - BAR_W // 2 + int(BAR_W * progress), BAR_Y + BAR_H, 0, 200, 120)

        update_canvas()

        for event in get_events():
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                running = False

        if pausing:
            delay(PAUSE_DURATION)
            pausing = False
            action_index = (action_index + 1) % len(ACTIONS)
            print(f"[Action Switch] Now playing: {ACTIONS[action_index][0]}")
            frame_index = 0
            repeat_count = 0
        else:
            delay(interval)
            frame_index += 1
            if frame_index >= len(frames):
                frame_index = 0
                repeat_count += 1
                if repeat_count >= REPEAT_LIMIT:
                    pausing = True
                    frame_index = len(frames) - 1

    close_canvas()


if __name__ == '__main__':
    main()
