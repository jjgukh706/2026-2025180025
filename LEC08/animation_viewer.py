import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


from pico2d import *


open_canvas(800, 600)

walk_sheet = load_image('sprites/walk.png')
walk_sheet.draw(400, 300)
update_canvas()
delay(2)

close_canvas()
