import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from math import pi, sin, cos

from pico2d import *


open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('character.png')


CX = 400
CY = 300
HALF = 170
FRAMES = 360

MOVE_COUNT = 0

SQUARE = [
    (CX - HALF, CY - HALF),
    (CX + HALF, CY - HALF),
    (CX + HALF, CY + HALF),
    (CX - HALF, CY + HALF),
]

TRIANGLE = [
    (CX, CY + HALF),
    (CX + HALF, CY - HALF),
    (CX - HALF, CY - HALF),
]


def circle_pos(t):
    radian = 2 * pi * t
    return CX + HALF * cos(radian), CY + HALF * sin(radian)


def line_pos(t):
    n = len(SQUARE)
    index = int(t * n) % n
    ratio = t * n % 1
    ax, ay = SQUARE[index]
    bx, by = SQUARE[(index + 1) % n]
    return ax + (bx - ax) * ratio, ay + (by - ay) * ratio


def triangle_pos(t):
    n = len(TRIANGLE)
    index = int(t * n) % n
    ratio = t * n % 1
    ax, ay = TRIANGLE[index]
    bx, by = TRIANGLE[(index + 1) % n]
    return ax + (bx - ax) * ratio, ay + (by - ay) * ratio


def move():
    global MOVE_COUNT
    MOVE_COUNT += 1
    t = (MOVE_COUNT % FRAMES) / FRAMES
    mode = (MOVE_COUNT // FRAMES) % 3
    if mode == 0:
        return circle_pos(t)
    if mode == 1:
        return line_pos(t)
    return triangle_pos(t)


while True:
    clear_canvas()
    x, y = move()
    character.draw(x, y)
    grass.draw(400, 30)
    update_canvas()


close_canvas()
