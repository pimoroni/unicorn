# Pico-powered Unicorn<!-- omit in toc -->
## Galactic, Cosmic, Stellar!<!-- omit in toc -->

This repository is home to the MicroPython firmware and examples for
Galactic, Cosmic and Stellar Unicorn - our sparkly Pico powered LED matrix boards.

- [Get Unicorn](#get-unicorn)
- [Download Firmware](#download-firmware)
- [Installation](#installation)
- [Useful Links](#useful-links)
- [Other Resources](#other-resources)
  - [Galactic](#galactic)
  - [Cosmic](#cosmic)
  - [Stellar](#stellar)

## Get Unicorn

* [Stellar 16x16 (Pico 2 W)](https://shop.pimoroni.com/products/space-unicorns?variant=40842632953939)
* [Galactic 53x11 (Pico 2 W)](https://shop.pimoroni.com/products/space-unicorns?variant=40842033561683)
* [Cosmic 32x32 (Pico 2 W)](https://shop.pimoroni.com/products/space-unicorns?variant=40842626596947)

## Download Firmware

You can find the latest firmware releases at [https://github.com/pimoroni/unicorn/releases/latest](https://github.com/pimoroni/unicorn/releases/latest).

There are seperate builds for Pico W / Pico 2 W - make sure you pick the correct one for your board!

The regular MicroPython build just updates the firmware on
your board. There's also a "-with-filesystem" build which includes a ready-to-go set
of examples (everything in the launch directory) that you can interact with right on your display.

:warning: If you've changed any of the code on your board then back up before
flashing "-with-filesystem" - *your files will be erased!*

## Installation

1. Connect your Unicorn to your computer with a micro-USB cable.
2. Put your device into bootloader mode by holding down the BOOTSEL button on the Pico whilst tapping RESET.
3. Drag and drop the downloaded .uf2 file to the "RPI-RP2" or "RP2350" drive that appears.
4. Your device should reset, and you should then be able to connect to it using [Thonny](https://thonny.org/).

## Useful Links
- [Learn: Getting Started with Pico](https://learn.pimoroni.com/article/getting-started-with-pico)
- [Pico Graphics documentation](https://github.com/pimoroni/pimoroni-pico/blob/main/micropython/modules/picographics/README.md)
- [Galactic Unicorn Function Reference](https://github.com/pimoroni/pimoroni-pico/blob/main/micropython/modules/galactic_unicorn/README.md)
- [Cosmic Unicorn Function Reference](https://github.com/pimoroni/pimoroni-pico/blob/main/micropython/modules/cosmic_unicorn/README.md)
- [Stellar Unicorn function reference](https://github.com/pimoroni/pimoroni-pico/blob/main/micropython/modules/stellar_unicorn/README.md)

## Other Resources

Here are some cool community projects and resources that you might find useful / inspirational! Note that code at the links below has not been tested by us and we're not able to offer support with it.

### Galactic
- :link: [Galactic Unicorn MQTT scroller (and 3D printed case)](https://github.com/ucl-casa-ce/Galactic-Unicorn-MQTT-Scroller)
- :link: [Compiling custom pimoroni-pico MicroPython (with ulab)](https://medium.com/@iestynlloyd/galactic-unicorns-and-custom-pimoroni-pico-firmware-38dd7c5913b8)
- :link: [Galactic Unicorn Graphical Workout](https://www.instructables.com/Galactic-Unicorn-Graphical-Workout/)
- :link: [Galactic Unicorn Bounce - Simple GFX Demo](https://www.instructables.com/Galactic-Unicorn-Bounce-Simple-GFX-Demo/)
- :link: [Cheerlights + Galactic Unicorn + MicroPython (beginner-friendly tutorial)](https://cheerlights.com/cheerlights-raspberry-pi-pico-w-micropython/)
- :link: [CheerClock (plus laser-cut templates for a fancy case/diffuser)](https://github.com/seanosteen/CheerClock)
- :link: [Giant Pomodoro timer using Galactic Unicorn](https://www.raspberrypi.com/news/make-a-giant-pomodoro-timer-using-galactic-unicorn/)
- :link: [Galactic Weather Clock](https://github.com/raphv/galactic-weather-clock)
- :link: [Unicorn Clock](https://github.com/hugokernel/UnicornClock)
- :link: [Unicorn Weather Station](https://github.com/TagWolf/UnicornWeatherStation)
- :link: [Unicorn News/RSS Feed Display](https://github.com/TagWolf/UnicornRSSDisplay)

### Cosmic
- :link: [Green Energy Display with Cosmic Unicorn](https://www.hackster.io/andreas-motzek/clock-and-green-energy-display-with-cosmic-unicorn-641dcb)
- :link: [cosmic-emoji-react - paint emojis from a computer, phone or tablet](https://github.com/chriscareycode/cosmic-unicorn/tree/main/cosmic-emoji-react)
- :link: [cosmic-paste - paste images from the clipboard to Cosmic Unicorn](https://github.com/chriscareycode/cosmic-unicorn/tree/main/cosmic-paste)
- :link: [Halloweenicorn - PIR enabled scarer](https://github.com/mrglennjones/Halloweenicorn)
- :link: [Cosmic Launcher - games and animations](https://github.com/mrkwllmsn/cosmic_laucher)

### Stellar
- Nothing here yet!
