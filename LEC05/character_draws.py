import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


from math import pi, sin, cos

from pico2d import *


open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('character.png')



x = 0
y = 30
count = 0

CIRCLE_FRAMES = 360
SQUARE_FRAMES = 1370
TRIANGLE_FRAMES = 1096
TOTAL_FRAMES = CIRCLE_FRAMES + SQUARE_FRAMES + TRIANGLE_FRAMES

TRI_RIGHT_FRAMES = 400
TRI_DIAG_FRAMES = 348
TRI_DIAG = (400 / TRI_DIAG_FRAMES, 570 / TRI_DIAG_FRAMES)


def move_circle(t):
    global x,y
    radian = 2 * pi * t
    x = 400 + 200 * cos(radian)
    y = 300 + 200 * sin(radian)


def move_square(count, speed):
    global x,y
    if count < 400:
        x += speed
    elif count < 685:
        y += speed
    elif count < 1085:
        x -= speed
    else:
        y -= speed


def move_triangle(count, speed):
    global x,y
    vx, vy = speed
    if count < TRI_RIGHT_FRAMES:
        x += speed
    elif count < TRI_RIGHT_FRAMES + TRI_DIAG_FRAMES:
        x -= vx
        y += vy
    else:
        x -= vx
        y -= vy


while True:
    clear_canvas()
    count += 1
    count = count% TOTAL_FRAMES
    if count == CIRCLE_FRAMES or count == CIRCLE_FRAMES + SQUARE_FRAMES:
        x, y = 0, 30
    if count < CIRCLE_FRAMES:
        move_circle((count % CIRCLE_FRAMES) / CIRCLE_FRAMES)
    elif count < CIRCLE_FRAMES + SQUARE_FRAMES:
        move_square(count - CIRCLE_FRAMES, 2)
    else:
        move_triangle(count - CIRCLE_FRAMES - SQUARE_FRAMES, 2)
    character.draw(x,y)
    
    grass.draw(400,30)
    update_canvas()


close_canvas()
