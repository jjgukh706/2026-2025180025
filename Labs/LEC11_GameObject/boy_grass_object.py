from pico2d import *
import random



class Grass :
    #잔디 속성을 초기화
    def __init__ (self):
        self.image = load_image('grass.png')
    
    def draw(self):
        self.image.draw(400,30)

    def update(self): #잔디는 움직이지 않으므로 update는 필요없다.
        pass



class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame+1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)




# Game object class here







def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



grass = None
team = None






def reset_world():
    global running
    running = True

    global grass
    grass = Grass()

    global team
    team = [Boy() for i in range(11)]





def update_world():
    grass.update()
    for boy in team:
        boy.update()
    





def render_world():
    clear_canvas()
    
    
    grass.draw()
    for boy in team:
        boy.draw()

    update_canvas()



# init code
open_canvas()


reset_world()


# roof code
while running:
    handle_events()
    update_canvas()
    render_world()
    delay(0.05)




# close code
close_canvas()

