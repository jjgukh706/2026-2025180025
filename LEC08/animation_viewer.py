import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


from pico2d import *


open_canvas(800, 600)

SCALE = 5
REPEAT = 5
PAUSE = 1.0

WALK_FRAMES = [(i * 64, 0, 64, 64) for i in range(8)]
RUN_FRAMES = [(i * 64, 0, 64, 64) for i in range(6)]
JUMP_FRAMES = [(0, 0, 64, 64), (64, 0, 64, 68), (128, 0, 64, 74),
               (192, 0, 64, 78), (256, 0, 64, 72), (320, 0, 64, 64)]
ATTACK_FRAMES = [(i * 64, 0, 64, 64) for i in range(10)]
IDLE_FRAMES = [(i * 64, 0, 64, 64) for i in range(4)]

ANIMATIONS = [
    ('idle', load_image('sprites/idle.png'), IDLE_FRAMES, 0.12),
    ('walk', load_image('sprites/walk.png'), WALK_FRAMES, 0.10),
    ('run', load_image('sprites/run.png'), RUN_FRAMES, 0.07),
    ('jump', load_image('sprites/jump.png'), JUMP_FRAMES, 0.10),
    ('attack', load_image('sprites/attack.png'), ATTACK_FRAMES, 0.06),
]

label = load_font('consola.ttf', 30)


def draw_frame(sheet, frame, x, y):
    left, bottom, w, h = frame
    sheet.clip_draw(left, bottom, w, h, x, y, w * SCALE, h * SCALE)


anim_index = 0
frame_index = 0
repeat_count = 0
pausing = False

while True:
    clear_canvas()
    name, sheet, frames, interval = ANIMATIONS[anim_index]

    if pausing:
        label.draw(400, 300, name, (255, 255, 0))
    else:
        draw_frame(sheet, frames[frame_index], 400, 300)
        label.draw(400, 560, '%s  frame %d / %d  (loop %d / %d)' %
                   (name, frame_index + 1, len(frames), repeat_count + 1, REPEAT),
                   (255, 255, 255))

    bar_w = 600
    draw_rectangle(400 - bar_w / 2, 40, 400 + bar_w / 2, 52, 80, 80, 80)
    progress = (anim_index + frame_index / len(frames)) / len(ANIMATIONS)
    draw_rectangle(400 - bar_w / 2, 40,
                   400 - bar_w / 2 + bar_w * progress, 52,
                   0, 200, 120)

    update_canvas()

    for event in get_events():
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            close_canvas()
            exit()

    if pausing:
        delay(PAUSE)
        pausing = False
        anim_index = (anim_index + 1) % len(ANIMATIONS)
        frame_index = 0
        repeat_count = 0
    else:
        delay(interval)
        frame_index += 1
        if frame_index >= len(frames):
            frame_index = 0
            repeat_count += 1
            if repeat_count >= REPEAT:
                pausing = True


close_canvas()
