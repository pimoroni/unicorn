import math
from galactic import GalacticUnicorn

graphics = None
palette = None

width = GalacticUnicorn.WIDTH
height = GalacticUnicorn.HEIGHT


phase = 0
hue_offset = 0.0
stripe_width = 3.0
speed = 5.0


def init():
    pass


@micropython.native  # noqa: F821
def draw():
    global hue_offset, phase

    phase += speed

    phase_percent = phase / 15
    for x in range(width):
        hue = ((x + (hue_offset * width)) % width) / width
        for y in range(height):
            v = ((math.sin((x + y) / stripe_width + phase_percent) + 1.5) / 2.5)

            graphics.set_pen(graphics.create_pen_hsv(hue, 1.0, v))
            graphics.pixel(x, y)
