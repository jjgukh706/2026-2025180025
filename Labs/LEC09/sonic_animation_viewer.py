import os
from pico2d import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

CANVAS_W = 800
CANVAS_H = 600
CENTER_X = CANVAS_W // 2
CENTER_Y = CANVAS_H // 2
SCALE = 4
BASE_H = 39 * SCALE

open_canvas(CANVAS_W, CANVAS_H)

sheet = load_image('sonic-sprite.png')

sample_frame = (1, 447, 29, 39)

def draw_frame(sheet, frame, x, y):
    left, bottom, w, h = frame
    draw_w = w * SCALE
    draw_h = h * SCALE
    # 발바닥 접지면 유지를 위한 높이 차이 보정
    y_offset = (draw_h - BASE_H) / 2
    sheet.clip_draw(left, bottom, w, h, x, y + y_offset, draw_w, draw_h)

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
