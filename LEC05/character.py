import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


from pico2d import *


open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('character.png')


x = 0
while x < 800:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, 90)
    update_canvas()
    x += 2
    delay(0.01)

close_canvas()

