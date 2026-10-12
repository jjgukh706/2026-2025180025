from pico2d import *


# fill here
hide_cursor()

character = load_image('animation_sheet.png')


def handle_events():
    global running

    global x,y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_MOUSEMOTION:
            x = event.x
            y = canvas_height - 1 - event.y


running = True
frame = 0

# fill here



while running:
    clear_canvas()

    tu_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100, 100, 100, x, y)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()




