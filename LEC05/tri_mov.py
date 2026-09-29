import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


from pico2d import *


open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('character.png')



x = 0
y = 30
count = 0

RIGHT_FRAMES = 400
DIAG_FRAMES = 348
TOTAL_FRAMES = RIGHT_FRAMES + DIAG_FRAMES * 2

DIAG = (400 / DIAG_FRAMES, 570 / DIAG_FRAMES)


def move(state, speed):
    global x,y
    vx, vy = speed
    if state == 1:
        x += vx
    elif state == 2:
        x -= vx
        y += vy
    elif state == 3:
        x -= vx
        y -= vy


while True:
    clear_canvas()
    count += 1
    count = count% TOTAL_FRAMES
    if count < RIGHT_FRAMES:
        move(1, (2, 0))
    elif count < RIGHT_FRAMES + DIAG_FRAMES:
        move(2, DIAG)
    else:
        move(3, DIAG)
    character.draw(x,y)
    
    grass.draw(400,30)
    update_canvas()


close_canvas()
