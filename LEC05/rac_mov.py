import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


from pico2d import *

open_canvas(800, 600)



grass = load_image('grass.png')
character = load_image('character.png')



while True:
    clear_canvas()
    grass.draw(400,30)
    update_canvas()

close_canvas()