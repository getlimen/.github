"""Generate the Limen org avatar as PNG in multiple sizes.

Draws four filled rectangles forming a doorway: two posts, a lintel, and an
emphasized threshold, white on a dark slate background.
"""
from PIL import Image, ImageDraw

BG = "#0f172a"   # slate-900
FG = "#f8fafc"   # soft white


def draw_avatar(size: int) -> Image.Image:
    img = Image.new("RGB", (size, size), BG)
    d = ImageDraw.Draw(img)

    # Scale factor: original design targets a 1024 canvas
    s = size / 1024.0

    def sc(v):
        return int(round(v * s))

    # Post + lintel stroke width
    stroke = sc(56)
    # Threshold stroke width (emphasized, thicker)
    thres = sc(96)

    # Positions (matching limen-avatar.svg)
    post_left_x = sc(310) - stroke // 2
    post_right_x = sc(714) - stroke // 2
    top_y = sc(270) - stroke // 2
    bottom_y = sc(730) - thres // 2  # threshold centered on line

    # Left post
    d.rectangle(
        [post_left_x, sc(270) - stroke // 2, post_left_x + stroke, sc(730) + stroke // 2],
        fill=FG,
    )
    # Right post
    d.rectangle(
        [post_right_x, sc(270) - stroke // 2, post_right_x + stroke, sc(730) + stroke // 2],
        fill=FG,
    )
    # Lintel (top horizontal)
    d.rectangle(
        [sc(262) - stroke // 2, top_y, sc(762) + stroke // 2, top_y + stroke],
        fill=FG,
    )
    # Threshold (bottom, emphasized)
    d.rectangle(
        [sc(200) - thres // 2, bottom_y, sc(824) + thres // 2, bottom_y + thres],
        fill=FG,
    )

    return img


for size in (1024, 512, 256, 128, 64):
    img = draw_avatar(size)
    out = f"limen-avatar-{size}.png"
    img.save(out, "PNG")
    print(f"wrote {out}")
