import gc
import time
import random
from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN, PEN_P8
from ulab import numpy

"""
HELLO NEO.
"""

# MAXIMUM OVERKILL
# machine.freq(250_000_000)

gu = GalacticUnicorn()
gu.set_brightness(1.0)
graphics = PicoGraphics(DISPLAY_GALACTIC_UNICORN, pen_type=PEN_P8)


# Fill half the palette with GREEEN
for g in range(128):
    _ = graphics.create_pen(0, g, 0)

# And half with bright green for white sparkles
for g in range(128):
    _ = graphics.create_pen(128, 128 + g, 128)


def update():
    the_matrix[:] *= 0.65

    x = random.randint(0, width // 2)
    y = random.randint(0, height - 1)
    the_matrix[y][x] = random.randint(128, 255) / 255.0

    # Propagate downwards
    old = numpy.ndarray(the_matrix) * 0.5
    the_matrix[:] = numpy.roll(the_matrix, 1, axis=1)
    the_matrix[:] += old


def draw():
    # Copy the effect to the framebuffer
    memoryview(graphics)[:] = numpy.ndarray(numpy.clip(the_matrix, 0, 1) * 254, dtype=numpy.uint8).tobytes()
    gu.update(graphics)


width = GalacticUnicorn.WIDTH
height = GalacticUnicorn.HEIGHT
the_matrix = numpy.zeros((height, width))

t_count = 0
t_total = 0


while True:
    if gu.is_pressed(GalacticUnicorn.SWITCH_BRIGHTNESS_UP):
        gu.adjust_brightness(+0.01)

    if gu.is_pressed(GalacticUnicorn.SWITCH_BRIGHTNESS_DOWN):
        gu.adjust_brightness(-0.01)

    tstart = time.ticks_ms()
    gc.collect()
    update()
    draw()
    tfinish = time.ticks_ms()

    total = tfinish - tstart
    t_total += total
    t_count += 1

    if t_count == 60:
        per_frame_avg = t_total / t_count
        print(f"60 frames in {t_total}ms, avg {per_frame_avg:.02f}ms per frame, {1000/per_frame_avg:.02f} FPS")
        t_count = 0
        t_total = 0

    # pause for a moment (important or the USB serial device will fail)
    # try to pace at 60fps or 30fps
    if total > 1000 / 30:
        time.sleep(0.0001)
    elif total > 1000 / 60:
        t = 1000 / 30 - total
        time.sleep(t / 1000)
    else:
        t = 1000 / 60 - total
        time.sleep(t / 1000)
