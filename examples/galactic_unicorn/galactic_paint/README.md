# Galactic Paint

Galactic Paint lets you paint pixels onto your Galactic Unicorn over WiFi, in realtime!

## Setting Up

You will need to copy the `galactic_paint` subdirectory to your Pico's root filesystem. You can copy a directory in Thonny by right clicking on it in the Files window, and selecting 'Upload to Pico'.

You'll also need `WIFI_CONFIG.py` from the `common` directory to be saved to your Pico. Open up `WIFI_CONFIG.py` in Thonny to add your wifi details (and save it when you're done).

- [micropython/examples/common](https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/examples/common)

Finally, you'll need to install `micropython-phew` and `microdot` through Thonny's Tools -> Manage Packages.

Run `galactic_paint.py` through Thonny and it should get connected and give you a URL to visit. Open that URL in your browser and start painting!