import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from pico2d import *


open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('character.png')



x = 0
y = 30
count = 0

def move(state, speed):
    global x,y
    if state == 1:
        x += speed
    elif state == 2:
        y += speed
    elif state == 3:
        x -= speed
    elif state == 4:
        y -= speed


while True:
    clear_canvas()
    count += 1
    count = count% 1370
    if count < 400:
        move(1,2)
    elif count < 685:
        move(2,2)
    elif count < 1085:
        move(3,2)
    else:
        move(4,2)
    character.draw(x,y)
    
    grass.draw(400,30)
    update_canvas()


close_canvas()
