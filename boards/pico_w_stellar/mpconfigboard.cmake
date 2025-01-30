# cmake file for Pimoroni Inky with Raspberry Pi Pico W
set(MICROPY_BOARD RPI_PICO_W)
set(PICO_BOARD "pico_w")
set(UNICORN "stellar")

# The C malloc is needed by cyw43-driver Bluetooth and Pimoroni Pico modules
set(MICROPY_C_HEAP_SIZE 4096)

set(MICROPY_PY_LWIP ON)
set(MICROPY_PY_NETWORK_CYW43 ON)

# Bluetooth
set(MICROPY_PY_BLUETOOTH ON)
set(MICROPY_BLUETOOTH_BTSTACK ON)
set(MICROPY_PY_BLUETOOTH_CYW43 ON)

# Board specific version of the frozen manifest
set(MICROPY_FROZEN_MANIFEST ${MICROPY_BOARD_DIR}/manifest.py)

# dir2uf2 manifest and root directory
set(PIMORONI_UF2_MANIFEST ${CMAKE_CURRENT_LIST_DIR}/manifest.txt)
set(PIMORONI_UF2_DIR ${CMAKE_CURRENT_LIST_DIR}/../../examples/${UNICORN}_unicorn/launch)
include(${CMAKE_CURRENT_LIST_DIR}/../common.cmake)