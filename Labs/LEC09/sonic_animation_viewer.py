import os
from pico2d import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 캔버스 및 레이아웃 상수 정의
CANVAS_W = 800
CANVAS_H = 600
CENTER_X = CANVAS_W // 2
CENTER_Y = CANVAS_H // 2
SCALE = 4

open_canvas(CANVAS_W, CANVAS_H)

running = True
while running:
    clear_canvas()
    update_canvas()

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    delay(0.05)

close_canvas()
