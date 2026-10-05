import os
from pico2d import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

open_canvas(800, 600)

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
