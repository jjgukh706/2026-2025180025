"""소년 상하좌우 이동 및 방향 바꾸기 (LEC10)

- 상/하/좌/우 방향키로 소년을 이동시키고 IDLE/달리기 애니메이션을 전환한다.
- 이동 방향에 따라 왼쪽(RUN_LEFT)은 clip_composite_draw의 flip='h'로 좌우 반전한다.
- 위/아래 이동 중에는 마지막 좌우 방향(dir)을 유지한다.
- 화면 경계에 도달하면 애니메이션은 유지한 채 이동만 멈춘다.
"""

from pico2d import *

CANVAS_W, CANVAS_H = 800, 600

# ---------- 스프라이트 시트 프레임 데이터 (animation_sheet.png) ----------
FRAME_W, FRAME_H = 100, 100    # 프레임 한 장 크기
N_FRAMES = 8                   # 행당 프레임 수
ROW_IDLE = 200                 # 대기(Idle) 애니메이션 행
ROW_RUN = 100                  # 달리기(Run) 애니메이션 행 (스타터 코드의 y=100 행과 일치)
CHAR_W, CHAR_H = 70, 70        # 캐릭터 출력(표시) 크기 - 100x100 원본을 축소해 출력

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
    global x, y, frame

    dx = int(right_key) - int(left_key)
    dy = int(up_key) - int(down_key)
    x += dx * MOVE_SPEED
    y += dy * MOVE_SPEED

    # 화면 경계 제한: 캐릭터 중심이 화면 밖으로 나가지 않는다.
    gap_x = CHAR_W // 2
    gap_y = CHAR_H // 2
    x = max(gap_x, min(x, CANVAS_W - gap_x))
    y = max(gap_y, min(y, CANVAS_H - gap_y))

    frame = (frame + 1) % N_FRAMES


def draw():
    clear_canvas()
    ground.draw(CANVAS_W // 2, CANVAS_H // 2, CANVAS_W, CANVAS_H)

    moving = left_key or right_key or up_key or down_key
    if moving and dir > 0:
        action = 'RUN_RIGHT'
    elif moving and dir < 0:
        action = 'RUN_LEFT'
    else:
        action = 'IDLE'

    if action == 'IDLE':
        row, flip = ROW_IDLE, ''      # 정지: IDLE 행
    elif action == 'RUN_RIGHT':
        row, flip = ROW_RUN, ''       # 오른쪽 이동: RUN 행, 원본 방향
    else:                             # RUN_LEFT
        row, flip = ROW_RUN, 'h'      # 왼쪽 이동: RUN 행 좌우 반전

    boy.clip_composite_draw(frame * FRAME_W, row, FRAME_W, FRAME_H, 0, flip, x, y, CHAR_W, CHAR_H)
    update_canvas()


running = True
while running:
    handle_events()
    update()
    draw()
    delay(0.05)

close_canvas()