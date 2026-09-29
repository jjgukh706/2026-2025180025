import os
import sys
import math

from PIL import Image, ImageDraw

os.chdir(os.path.dirname(os.path.abspath(__file__)))

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPRITE_DIR = os.path.join(ROOT_DIR, 'sprites')

FRAME_W = 64
FRAME_H = 64

SKIN = (245, 200, 160, 255)
HAIR = (80, 55, 30, 255)
SHIRT = (60, 120, 200, 255)
PANTS = (45, 60, 110, 255)
SHOE = (35, 35, 40, 255)
METAL = (200, 205, 215, 255)


def limb(draw, x0, y0, x1, y1, width, color):
    draw.line([(x0, y0), (x1, y1)], fill=color, width=width)
    r = width // 2
    draw.ellipse([x0 - r, y0 - r, x0 + r, y0 + r], fill=color)
    draw.ellipse([x1 - r, y1 - r, x1 + r, y1 + r], fill=color)


def draw_character(draw, w, h, pose):
    cx = w // 2
    ground = h - 4
    hip_y = ground - 24
    shoulder_y = ground - 42

    leg_a_x, leg_a_lift = pose['leg_a']
    leg_b_x, leg_b_lift = pose['leg_b']
    arm_a_x, arm_a_lift = pose['arm_a']
    arm_b_x, arm_b_lift = pose['arm_b']
    lean = pose.get('lean', 0)

    shoulder_x = cx + lean
    hip_x = cx + lean * 0.4

    draw.line([(hip_x, hip_y), (shoulder_x, shoulder_y)], fill=SHIRT, width=13)

    limb(draw, hip_x, hip_y, cx + leg_b_x, ground - leg_b_lift, 7, PANTS)
    limb(draw, hip_x, hip_y, cx + leg_a_x, ground - leg_a_lift, 7, PANTS)

    draw.ellipse([cx + leg_a_x - 5, ground - leg_a_lift - 3,
                  cx + leg_a_x + 5, ground - leg_a_lift + 3], fill=SHOE)
    draw.ellipse([cx + leg_b_x - 5, ground - leg_b_lift - 3,
                  cx + leg_b_x + 5, ground - leg_b_lift + 3], fill=SHOE)

    hand_a = (shoulder_x + arm_a_x, shoulder_y + 13 - arm_a_lift)
    hand_b = (shoulder_x + arm_b_x, shoulder_y + 13 - arm_b_lift)
    limb(draw, shoulder_x, shoulder_y, hand_b[0], hand_b[1], 5, SKIN)
    limb(draw, shoulder_x, shoulder_y, hand_a[0], hand_a[1], 5, SKIN)

    head_x = shoulder_x + 1
    head_y = shoulder_y - 8
    draw.ellipse([head_x - 7, head_y - 7, head_x + 7, head_y + 7], fill=SKIN)
    draw.chord([head_x - 7, head_y - 8, head_x + 7, head_y + 5], 180, 360, fill=HAIR)


def walk_pose(i, total):
    p = 2 * math.pi * i / total
    swing = 9 * math.sin(p) + 2.5 * math.sin(2 * p)
    swing_b = 9 * math.sin(p + math.pi) + 2.5 * math.sin(2 * p + math.pi)
    lift_a = max(0, 1.5 * math.sin(p + math.pi / 2) + 2.5 * math.sin(2 * p + math.pi / 2))
    lift_b = max(0, 1.5 * math.sin(p - math.pi / 2) + 2.5 * math.sin(2 * p - math.pi / 2))
    return {
        'leg_a': (swing, int(lift_a)),
        'leg_b': (swing_b, int(lift_b)),
        'arm_a': (-swing * 0.8, 0),
        'arm_b': (swing_b * 0.8, 0),
        'lean': 1,
    }


def build_walk(total=8):
    frames = []
    for i in range(total):
        frame = Image.new('RGBA', (FRAME_W, FRAME_H), (0, 0, 0, 0))
        draw_character(ImageDraw.Draw(frame), FRAME_W, FRAME_H, walk_pose(i, total))
        frames.append(frame)
    return frames, [(FRAME_W, FRAME_H)] * total


def save_sheet(name, frames, sizes):
    sheet_w = sum(s[0] for s in sizes)
    sheet_h = max(s[1] for s in sizes)
    sheet = Image.new('RGBA', (sheet_w, sheet_h), (0, 0, 0, 0))

    rects = []
    x = 0
    for frame, (w, h) in zip(frames, sizes):
        scaled = frame.resize((w, h), Image.NEAREST)
        sheet.paste(scaled, (x, sheet_h - h), scaled)
        rects.append((x, 0, w, h))
        x += w

    os.makedirs(SPRITE_DIR, exist_ok=True)
    path = os.path.join(SPRITE_DIR, name + '.png')
    sheet.save(path)
    print(path, sheet.size, rects)
    return rects


if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'walk'
    if target == 'walk':
        frames, sizes = build_walk()
        save_sheet('walk', frames, sizes)
