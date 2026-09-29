import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


from pico2d import *


open_canvas(800, 600)

FRAME_W = 64
FRAME_H = 64

walk_sheet = load_image('sprites/walk.png')


def draw_frame(sheet, index, x, y):
    sheet.clip_draw(index * FRAME_W, 0, FRAME_W, FRAME_H, x, y)


index = 0
while True:
    clear_canvas()
    draw_frame(walk_sheet, index, 400, 300)
    update_canvas()
    index = (index + 1) % 8


close_canvas()
