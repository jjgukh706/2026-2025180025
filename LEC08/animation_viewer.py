import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


from pico2d import *


open_canvas(800, 600)

SCALE = 5

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

while True:
    clear_canvas()
    name, sheet, frames, interval = ANIMATIONS[anim_index]
    draw_frame(sheet, frames[frame_index], 400, 300)
    label.draw(400, 560, '%s  frame %d / %d' % (name, frame_index + 1, len(frames)),
               (255, 255, 255))
    update_canvas()
    delay(interval)
    frame_index += 1
    if frame_index >= len(frames):
        frame_index = 0
        anim_index = (anim_index + 1) % len(ANIMATIONS)


close_canvas()
