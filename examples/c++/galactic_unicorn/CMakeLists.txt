cmake_minimum_required(VERSION 3.12)

include(../../../firmware/pimoroni_pico_import.cmake)
include(../pico_sdk_import.cmake)

project("Galactic Unicorn Examples" C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

pico_sdk_init()

include(libraries/galactic_unicorn/galactic_unicorn)
include(libraries/pico_graphics/pico_graphics)

add_executable(rainbow_text rainbow_text.cpp)
target_link_libraries(rainbow_text pico_stdlib hardware_pio hardware_adc hardware_dma pico_graphics galactic_unicorn)
pico_enable_stdio_usb(rainbow_text 1)
pico_add_extra_outputs(rainbow_text)

add_executable(rainbow rainbow.cpp)
target_link_libraries(rainbow pico_stdlib hardware_pio hardware_adc hardware_dma pico_graphics galactic_unicorn)
pico_enable_stdio_usb(rainbow 1)
pico_add_extra_outputs(rainbow)

add_executable(nostalgia_prompt nostalgia_prompt.cpp)
target_link_libraries(nostalgia_prompt pico_stdlib hardware_pio hardware_adc hardware_dma pico_graphics galactic_unicorn)
pico_enable_stdio_usb(nostalgia_prompt 1)
pico_add_extra_outputs(nostalgia_prompt)

add_executable(eighties_super_computer eighties_super_computer.cpp)
target_link_libraries(eighties_super_computer pico_stdlib hardware_pio hardware_adc hardware_dma pico_graphics galactic_unicorn)
pico_enable_stdio_usb(eighties_super_computer 1)
pico_add_extra_outputs(eighties_super_computer)

add_executable(fire_effect fire_effect.cpp)
target_link_libraries(fire_effect pico_stdlib hardware_pio hardware_adc hardware_dma pico_graphics galactic_unicorn)
pico_enable_stdio_usb(fire_effect 1)
pico_add_extra_outputs(fire_effect)

add_executable(scroll_text scroll_text.cpp)
target_link_libraries(scroll_text pico_stdlib hardware_pio hardware_adc hardware_dma pico_graphics galactic_unicorn)
pico_enable_stdio_usb(scroll_text 1)
pico_add_extra_outputs(scroll_text)

add_executable(balls balls.cpp)
target_link_libraries(balls pico_stdlib hardware_pio hardware_adc hardware_dma pico_graphics galactic_unicorn)
pico_enable_stdio_usb(balls 1)
pico_add_extra_outputs(balls)

add_executable(lava_lamp lava_lamp.cpp)
target_link_libraries(lava_lamp pico_stdlib hardware_pio hardware_adc hardware_dma pico_graphics galactic_unicorn)
pico_enable_stdio_usb(lava_lamp 1)
pico_add_extra_outputs(lava_lamp)

add_executable(feature_test feature_test.cpp audio_samples.cpp)
target_link_libraries(feature_test pico_stdlib hardware_pio hardware_adc hardware_dma pico_graphics galactic_unicorn)
pico_enable_stdio_usb(feature_test 1)
pico_add_extra_outputs(feature_test)
