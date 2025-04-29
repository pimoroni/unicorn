import time
import math
from cosmic import CosmicUnicorn
from picographics import PicoGraphics, DISPLAY_COSMIC_UNICORN as DISPLAY

"""
Some good old fashioned rainbows!

You can adjust the cycling speed with A and B,
stripe width with C and D, hue with VOL + and -,
and the brightness with LUX + and -.
The sleep button stops the animation (can be started again with A or B).
"""

cu = CosmicUnicorn()
graphics = PicoGraphics(DISPLAY)

width = CosmicUnicorn.WIDTH
height = CosmicUnicorn.HEIGHT


@micropython.native  # noqa: F821
def draw():
    global hue_offset, phase
    phase_percent = phase / 15
    for x in range(width):
        hue = ((x + (hue_offset * width)) % width) / width
        for y in range(height):
            v = ((math.sin((x + y) / stripe_width + phase_percent) + 1.5) / 2.5)

            graphics.set_pen(graphics.create_pen_hsv(hue, 1.0, v))
            graphics.pixel(x, y)

    cu.update(graphics)


hue_offset = 0.0

animate = True
stripe_width = 3.0
speed = 1.0

cu.set_brightness(0.5)

phase = 0
while True:

    if animate:
        phase += speed

    if cu.is_pressed(CosmicUnicorn.SWITCH_VOLUME_UP):
        hue_offset += 0.01
        hue_offset = 1.0 if hue_offset > 1.0 else hue_offset

    if cu.is_pressed(CosmicUnicorn.SWITCH_VOLUME_DOWN):
        hue_offset -= 0.01
        hue_offset = 0.0 if hue_offset < 0.0 else hue_offset

    if cu.is_pressed(CosmicUnicorn.SWITCH_BRIGHTNESS_UP):
        cu.adjust_brightness(+0.01)

    if cu.is_pressed(CosmicUnicorn.SWITCH_BRIGHTNESS_DOWN):
        cu.adjust_brightness(-0.01)

    if cu.is_pressed(CosmicUnicorn.SWITCH_SLEEP):
        animate = False

    if cu.is_pressed(CosmicUnicorn.SWITCH_A):
        speed += 0.05
        speed = 10.0 if speed > 10.0 else speed
        animate = True

    if cu.is_pressed(CosmicUnicorn.SWITCH_B):
        speed -= 0.05
        speed = 0.0 if speed < 0.0 else speed
        animate = True

    if cu.is_pressed(CosmicUnicorn.SWITCH_C):
        stripe_width += 0.05
        stripe_width = 10.0 if stripe_width > 10.0 else stripe_width

    if cu.is_pressed(CosmicUnicorn.SWITCH_D):
        stripe_width -= 0.05
        stripe_width = 1.0 if stripe_width < 1.0 else stripe_width

    start = time.ticks_ms()

    draw()

    print("total took: {} ms".format(time.ticks_ms() - start))
