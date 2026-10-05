import os
from pico2d import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

CANVAS_W = 800
CANVAS_H = 600
CENTER_X = CANVAS_W // 2
CENTER_Y = CANVAS_H // 2
SCALE = 4
BASE_H = 39 * SCALE
REPEAT_LIMIT = 5
PAUSE_DURATION = 1.0

open_canvas(CANVAS_W, CANVAS_H)

sheet = load_image('sonic-sprite.png')

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
    ('Run (달리기)', RUN_FRAMES, 0.08),
    ('Sprint (대시)', DASH_FRAMES, 0.06),
    ('Roll (점프/구르기)', ROLL_FRAMES, 0.08),
    ('Skid (제동)', SKID_FRAMES, 0.08),
    ('Push (밀기)', PUSH_FRAMES, 0.10),
    ('Spring (스프링 도약)', SPRING_FRAMES, 0.08),
    ('Spin Charge (회전 진입)', SPIN_FRAMES, 0.05),
    ('Fall/Hurt (낙하/피격)', FALL_FRAMES, 0.08),
    ('Pose (승리 포즈)', POSE_FRAMES, 0.12),
]

def draw_frame(sheet, frame, x, y):
    left, bottom, w, h = frame
    draw_w = w * SCALE
    draw_h = h * SCALE
    y_offset = (draw_h - BASE_H) / 2
    sheet.clip_draw(left, bottom, w, h, x, y + y_offset, draw_w, draw_h)

action_index = 0
frame_index = 0
repeat_count = 0
pausing = False
running = True

while running:
    name, frames, interval = ACTIONS[action_index]

    clear_canvas()
    draw_frame(sheet, frames[frame_index], CENTER_X, CENTER_Y)
    update_canvas()

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    if pausing:
        delay(PAUSE_DURATION)
        pausing = False
        # 10종 동작 순차 재생 후 1번 동작으로 무한 순환
        action_index = (action_index + 1) % len(ACTIONS)
        print(f'[Action Switch] Now playing: {ACTIONS[action_index][0]}')
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
