from pico2d import *

CANVAS_W, CANVAS_H = 800, 600


open_canvas()
ground = load_image('TUK_GROUND.png')
boy = load_image('animation_sheet.png')

x = CANVAS_W // 2
y = CANVAS_H // 2


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


running = True
while running:
    clear_canvas()
    ground.draw(CANVAS_W // 2, CANVAS_H // 2, CANVAS_W, CANVAS_H)
    boy.clip_draw(0 * 100, 200, 100, 100, x, y)
    update_canvas()
    handle_events()
    delay(0.05)

close_canvas()