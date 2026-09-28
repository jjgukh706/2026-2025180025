import os
import numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))


from pico2d import *


open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('character.png')



x = 0
y = 0
count = 0
radius = 200

while True:
    clear_canvas()
    count += 1
    count = count% 360
    radian = np.radians(count)
    x = 400 + radius * np.cos(radian)
    y = 300 + radius * np.sin(radian)
    character.draw(x,y)
    
    grass.draw(400,30)
    update_canvas()


close_canvas()
