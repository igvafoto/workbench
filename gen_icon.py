#!/usr/bin/env python3
"""Generate app icons for 依依的创作工作台 PWA (Liquid Glass 风格)."""
from PIL import Image, ImageDraw

VIOLET = (167, 139, 250)   # #a78bfa 淡紫罗兰
CORAL = (255, 127, 110)    # #ff7f6e 珊瑚橙
TEAL = (94, 207, 176)      # #5ecfb0 薄荷绿
WHITE = (255, 255, 255)


def make_icon(size, path):
    img = Image.new("RGB", (size, size), VIOLET)
    draw = ImageDraw.Draw(img)

    # 对角线渐变：淡紫罗兰 -> 珊瑚橙
    for y in range(size):
        t = y / float(size)
        r = int(VIOLET[0] * (1 - t) + CORAL[0] * t)
        g = int(VIOLET[1] * (1 - t) + CORAL[1] * t)
        b = int(VIOLET[2] * (1 - t) + CORAL[2] * t)
        draw.line([(0, y), (size, y)], fill=(r, g, b))

    # 白色圆角玻璃卡片（居中 62%）
    card = int(size * 0.62)
    x0 = (size - card) // 2
    y0 = (size - card) // 2
    rad = int(size * 0.18)
    draw.rounded_rectangle([x0, y0, x0 + card, y0 + card], radius=rad, fill=WHITE)

    # 三个彩色小圆点（珊瑚 / 薄荷 / 淡紫）：多平台创作台意象
    dot = int(size * 0.058)
    cy = y0 + int(card * 0.42)
    cx = x0 + int(card * 0.5)
    gap = int(size * 0.105)
    for i, c in enumerate([CORAL, TEAL, VIOLET]):
        dx = cx + (i - 1) * gap
        draw.ellipse([dx - dot, cy - dot, dx + dot, cy + dot], fill=c)

    # 珊瑚色小下划线点缀
    lw = max(int(size * 0.022), 4)
    ly = cy + dot + int(size * 0.065)
    draw.rounded_rectangle([cx - gap, ly, cx + gap, ly + lw], radius=lw // 2, fill=CORAL)

    img.save(path, "PNG")
    print("Generated:", path, "(%dx%d)" % (size, size))


make_icon(1024, "icon-1024.png")
make_icon(512, "icon-512.png")
make_icon(192, "icon-192.png")
make_icon(180, "apple-touch-icon.png")
