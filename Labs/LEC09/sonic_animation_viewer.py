import os
from pico2d import *

# 작업 경로를 스크립트 위치로 고정
os.chdir(os.path.dirname(os.path.abspath(__file__)))

open_canvas(800, 600)

while True:
    clear_canvas()
    update_canvas()
    delay(0.05)

close_canvas()
