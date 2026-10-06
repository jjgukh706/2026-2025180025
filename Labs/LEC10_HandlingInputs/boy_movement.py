from pico2d import *

CANVAS_W, CANVAS_H = 800, 600

# ---------- 스프라이트 시트 프레임 데이터 (animation_sheet.png) ----------
FRAME_W, FRAME_H = 100, 100    # 프레임 한 장 크기
N_FRAMES = 8                   # 행당 프레임 수
ROW_IDLE = 100                 # 대기(Idle) 애니메이션 행 - 프레임 변화가 작은 하단 그룹
ROW_RUN = 200                  # 달리기(Run) 애니메이션 행 - 프레임 변화가 큰 상단 그룹

# ---------- 캐릭터 상태 ----------
x = CANVAS_W // 2              # 캐릭터 중심 x
y = CANVAS_H // 2              # 캐릭터 중심 y
frame = 0                      # 재생 중인 프레임 번호

# ---------- 이동 상태 ----------
MOVE_SPEED = 5                 # 프레임당 이동 거리
dir = 1                        # 바라보는 방향: -1 왼쪽, +1 오른쪽
left_key = right_key = up_key = down_key = False


open_canvas()
ground = load_image('TUK_GROUND.png')
boy = load_image('animation_sheet.png')


def handle_events():
    global running, left_key, right_key, up_key, down_key, dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                left_key = True
                dir = -1
            elif event.key == SDLK_RIGHT:
                right_key = True
                dir = 1
            elif event.key == SDLK_UP:
                up_key = True
            elif event.key == SDLK_DOWN:
                down_key = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                left_key = False
            elif event.key == SDLK_RIGHT:
                right_key = False
            elif event.key == SDLK_UP:
                up_key = False
            elif event.key == SDLK_DOWN:
                down_key = False


def update():
    global x, frame

    dx = int(right_key) - int(left_key)
    x += dx * MOVE_SPEED
    frame = (frame + 1) % N_FRAMES


def draw():
    clear_canvas()
    ground.draw(CANVAS_W // 2, CANVAS_H // 2, CANVAS_W, CANVAS_H)

    moving = left_key or right_key
    if moving and dir > 0:
        action = 'RUN_RIGHT'
    elif moving and dir < 0:
        action = 'RUN_LEFT'
    else:
        action = 'IDLE'

    if action == 'IDLE':
        row, flip = ROW_IDLE, ''
    elif action == 'RUN_RIGHT':
        row, flip = ROW_RUN, ''
    else:
        row, flip = ROW_RUN, 'h'

    boy.clip_composite_draw(frame * FRAME_W, row, FRAME_W, FRAME_H, 0, flip, x, y)
    update_canvas()


running = True
while running:
    handle_events()
    update()
    draw()
    delay(0.05)

close_canvas()