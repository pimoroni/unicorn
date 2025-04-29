# Clock example with NTP synchronization
#
# Create a secrets.py with your Wifi details to be able to get the time
# when the Stellar Unicorn isn't connected to Thonny.
#
# secrets.py should contain:
# WIFI_SSID = "Your WiFi SSID"
# WIFI_PASSWORD = "Your WiFi password"
#
# Clock synchronizes time on start, and resynchronizes if you press the A button
#
# This example uses a custom tiny font - find 3x5.bitmapfont in /common/fonts

import time
import math
import machine
import network
import ntptime
from stellar import StellarUnicorn
from picographics import PicoGraphics, DISPLAY_STELLAR_UNICORN as DISPLAY

try:
    from secrets import WIFI_SSID, WIFI_PASSWORD
    wifi_available = True
except ImportError:
    print("Create secrets.py with your WiFi credentials to get time from NTP")
    wifi_available = False


# constants for controlling the background colour throughout the day
MIDDAY_HUE = 1.1
MIDNIGHT_HUE = 0.8
HUE_OFFSET = -0.1

MIDDAY_SATURATION = 1.0
MIDNIGHT_SATURATION = 1.0

MIDDAY_VALUE = 0.8
MIDNIGHT_VALUE = 0.3


# create stellar object and graphics surface for drawing
su = StellarUnicorn()
graphics = PicoGraphics(DISPLAY)

# create the rtc object
rtc = machine.RTC()

width = StellarUnicorn.WIDTH
height = StellarUnicorn.HEIGHT

# set up some pens to use later
WHITE = graphics.create_pen(255, 255, 255)
BLACK = graphics.create_pen(0, 0, 0)


# function for drawing a gradient background
def gradient_background(start_hue, start_sat, start_val, end_hue, end_sat, end_val):
    half_width = width // 2
    for x in range(half_width):
        hue = ((end_hue - start_hue) * (x / half_width)) + start_hue
        sat = ((end_sat - start_sat) * (x / half_width)) + start_sat
        val = ((end_val - start_val) * (x / half_width)) + start_val
        graphics.set_pen(graphics.create_pen_hsv(hue, sat, val))
        for y in range(height):
            graphics.pixel(x, y)
            graphics.pixel(width - x - 1, y)

    graphics.set_pen(graphics.create_pen_hsv(end_hue, end_sat, end_val))
    for y in range(height):
        graphics.pixel(half_width, y)


# function for drawing outlined text
def outline_text(text, x, y):
    graphics.set_pen(BLACK)
    graphics.text(text, x - 1, y - 1, -1, 1)
    graphics.text(text, x, y - 1, -1, 1)
    graphics.text(text, x + 1, y - 1, -1, 1)
    graphics.text(text, x - 1, y, -1, 1)
    graphics.text(text, x + 1, y, -1, 1)
    graphics.text(text, x - 1, y + 1, -1, 1)
    graphics.text(text, x, y + 1, -1, 1)
    graphics.text(text, x + 1, y + 1, -1, 1)

    graphics.set_pen(WHITE)
    graphics.text(text, x, y, -1, 1)


# Connect to wifi and synchronize the RTC time from NTP
def sync_time():
    if not wifi_available:
        return

    # Start connection
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)

    # Wait for connect success or failure
    max_wait = 100
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print("waiting for connection...")
        time.sleep(0.2)

        redraw_display_if_reqd()
        su.update(graphics)

    if max_wait > 0:
        print("Connected")

        try:
            ntptime.settime()
            print("Time set")
        except OSError:
            pass

    wlan.disconnect()
    wlan.active(False)


# NTP synchronizes the time to UTC, this allows you to adjust the displayed time
# by one hour increments from UTC by pressing the volume up/down buttons
#
# We use the IRQ method to detect the button presses to avoid incrementing/decrementing
# multiple times when the button is held.
utc_offset = 0

up_button = machine.Pin(StellarUnicorn.SWITCH_VOLUME_UP, machine.Pin.IN, machine.Pin.PULL_UP)
down_button = machine.Pin(StellarUnicorn.SWITCH_VOLUME_DOWN, machine.Pin.IN, machine.Pin.PULL_UP)


def adjust_utc_offset(pin):
    global utc_offset, last_second
    if pin == up_button:
        utc_offset += 1
        last_second = None
    if pin == down_button:
        utc_offset -= 1
        last_second = None


up_button.irq(trigger=machine.Pin.IRQ_FALLING, handler=adjust_utc_offset)
down_button.irq(trigger=machine.Pin.IRQ_FALLING, handler=adjust_utc_offset)


year, month, day, wd, hour, minute, second, _ = rtc.datetime()

last_second = second


# Check whether the RTC time has changed and if so redraw the display
def redraw_display_if_reqd():
    global year, month, day, wd, hour, minute, second, last_second

    year, month, day, wd, hour, minute, second, _ = rtc.datetime()
    if second != last_second:
        hour = (hour + utc_offset) % 24
        time_through_day = (((hour * 60) + minute) * 60) + second
        percent_through_day = time_through_day / 86400
        percent_to_midday = 1.0 - ((math.cos(percent_through_day * math.pi * 2) + 1) / 2)
        print(percent_to_midday)

        hue = ((MIDDAY_HUE - MIDNIGHT_HUE) * percent_to_midday) + MIDNIGHT_HUE
        sat = ((MIDDAY_SATURATION - MIDNIGHT_SATURATION) * percent_to_midday) + MIDNIGHT_SATURATION
        val = ((MIDDAY_VALUE - MIDNIGHT_VALUE) * percent_to_midday) + MIDNIGHT_VALUE

        gradient_background(hue, sat, val,
                            hue + HUE_OFFSET, sat, val)

        clock = "{:02} {:02}".format(hour, minute)

        # calculate text position so that it is centred
        w = graphics.measure_text(clock, 1)
        x = int(width / 2 - w / 2 + 1)
        y = 5

        outline_text(clock, x, y)

        last_second = second


# set the font
graphics.set_font(open("3x5.bitmapfont", "rb").read())
su.set_brightness(0.5)

sync_time()

while True:
    if su.is_pressed(StellarUnicorn.SWITCH_BRIGHTNESS_UP):
        su.adjust_brightness(+0.01)
        last_second = None

    if su.is_pressed(StellarUnicorn.SWITCH_BRIGHTNESS_DOWN):
        su.adjust_brightness(-0.01)
        last_second = None

    if su.is_pressed(StellarUnicorn.SWITCH_A):
        sync_time()

    redraw_display_if_reqd()

    # update the display
    su.update(graphics)

    time.sleep(0.01)
