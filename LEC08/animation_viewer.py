import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


from pico2d import *


open_canvas(800, 600)

SCALE = 5
DRAW_H = 64 * SCALE
REPEAT = 5
PAUSE = 1.0
CENTER_X = 400
CENTER_Y = 300
BAR_W = 600
BAR_Y = 40

# Every animation is stored as a list of frame rectangles
# (left, bottom, width, height) instead of a single frame size, so a sheet
# whose frames differ in size is played back exactly the same way.
#   - jump  : frame height changes (64 / 68 / 72 / 74 / 78)
#   - attack: frame width changes (82 ... 107, follows the sword reach)
# Frame counts also differ per animation (4 / 8 / 6 / 6 / 10).
WALK_FRAMES = [(i * 64, 0, 64, 64) for i in range(8)]
RUN_FRAMES = [(i * 64, 0, 64, 64) for i in range(6)]
JUMP_FRAMES = [(0, 0, 64, 64), (64, 0, 64, 68), (128, 0, 64, 74),
               (192, 0, 64, 78), (256, 0, 64, 72), (320, 0, 64, 64)]
ATTACK_FRAMES = [(0, 0, 85, 64), (85, 0, 89, 64), (174, 0, 89, 64),
                 (263, 0, 100, 64), (363, 0, 107, 64), (470, 0, 103, 64),
                 (573, 0, 94, 64), (667, 0, 87, 64), (754, 0, 83, 64),
                 (837, 0, 82, 64)]
IDLE_FRAMES = [(i * 64, 0, 64, 64) for i in range(4)]

ANIMATIONS = [
    ('idle', load_image('sprites/idle.png'), IDLE_FRAMES, 0.12),
    ('walk', load_image('sprites/walk.png'), WALK_FRAMES, 0.10),
    ('run', load_image('sprites/run.png'), RUN_FRAMES, 0.07),
    ('jump', load_image('sprites/jump.png'), JUMP_FRAMES, 0.10),
    ('attack', load_image('sprites/attack.png'), ATTACK_FRAMES, 0.06),
]

label = load_font(os.path.abspath('fonts/consola.ttf'), 28)


def draw_frame(sheet, frame, x, y):
    left, bottom, w, h = frame
    draw_w = w * SCALE
    draw_h = h * SCALE
    sheet.clip_draw(left, bottom, w, h, x, y - (draw_h - DRAW_H) / 2,
                    draw_w, draw_h)


anim_index = 0
frame_index = 0
repeat_count = 0
pausing = False

while True:
    clear_canvas()
    name, sheet, frames, interval = ANIMATIONS[anim_index]

    if pausing:
        label.draw(CENTER_X, CENTER_Y, name, (255, 255, 0))
    else:
        draw_frame(sheet, frames[frame_index], CENTER_X, CENTER_Y)
        label.draw(CENTER_X, 560, '%s  frame %d / %d  (loop %d / %d)' %
                   (name, frame_index + 1, len(frames), repeat_count + 1, REPEAT),
                   (255, 255, 255))

    progress = (anim_index + frame_index / len(frames)) / len(ANIMATIONS)
    draw_rectangle(CENTER_X - BAR_W / 2, BAR_Y,
                   CENTER_X + BAR_W / 2, BAR_Y + 12, 80, 80, 80)
    draw_rectangle(CENTER_X - BAR_W / 2, BAR_Y,
                   CENTER_X - BAR_W / 2 + BAR_W * progress, BAR_Y + 12,
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
