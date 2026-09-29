import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


from pico2d import *


open_canvas(800, 600)

FRAME_W = 64
FRAME_H = 64
SCALE = 5
DRAW_W = FRAME_W * SCALE
DRAW_H = FRAME_H * SCALE

walk_sheet = load_image('sprites/walk.png')
label = load_font('consola.ttf', 30)


def draw_frame(sheet, index, x, y):
    sheet.clip_draw(index * FRAME_W, 0, FRAME_W, FRAME_H,
                    x, y, DRAW_W, DRAW_H)


index = 0
while True:
    clear_canvas()
    draw_frame(walk_sheet, index, 400, 300)
    label.draw(400, 560, 'walk  frame %d / 8' % index, (255, 255, 255))
    update_canvas()
    delay(0.1)
    index = (index + 1) % 8


close_canvas()
