from pico2d import *
import random


class grass :

    pass


# Game object class here


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False









def reset_world():
    global running
    running = True





def update_world():
    pass





def render_world():
    clear_canvas()
    update_canvas()



# init code
open_canvas()


reset_world()


# roof code
while running():
    handle_events()
    update_canvas()
    render_world()
    delay(0.05)




# close code
close_canvas()

