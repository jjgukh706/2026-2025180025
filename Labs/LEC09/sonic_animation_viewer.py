import os
from pico2d import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

CANVAS_W = 800
CANVAS_H = 600
CENTER_X = CANVAS_W // 2
CENTER_Y = CANVAS_H // 2
SCALE = 4

open_canvas(CANVAS_W, CANVAS_H)

sheet = load_image('sonic-sprite.png')

# 단일 테스트 프레임 (left, bottom, width, height)
sample_frame = (1, 447, 29, 39)

def draw_frame(sheet, frame, x, y):
    left, bottom, w, h = frame
    sheet.clip_draw(left, bottom, w, h, x, y, w * SCALE, h * SCALE)

running = True
while running:
    clear_canvas()
    draw_frame(sheet, sample_frame, CENTER_X, CENTER_Y)
    update_canvas()

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    delay(0.05)

close_canvas()
