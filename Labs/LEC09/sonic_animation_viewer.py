import os
from pico2d import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

CANVAS_W = 800
CANVAS_H = 600
CENTER_X = CANVAS_W // 2
CENTER_Y = CANVAS_H // 2
SCALE = 4

open_canvas(CANVAS_W, CANVAS_H)

# 스프라이트 시트 리소스 로드
sheet = load_image('sonic-sprite.png')

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
