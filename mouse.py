# Bandaid fix for weird bugs on my PC: every time certain programs would open they would change
# my mouse speed. This just sets a default mouse speed and makes sure that it stays at that 
# speed. 

import ctypes
import time #Done for speed reasons I suppose lol

def change_speed(speed):
    #   1 - slow
    #   10 - standard
    #   20 - fast
    set_mouse_speed = 113   # 0x0071 for SPI_SETMOUSESPEED
    ctypes.windll.user32.SystemParametersInfoA(set_mouse_speed, 0, speed, 0)


def get_current_speed():
    get_mouse_speed = 112   # 0x0070 for SPI_GETMOUSESPEED
    speed = ctypes.c_int()
    ctypes.windll.user32.SystemParametersInfoA(get_mouse_speed, 0, ctypes.byref(speed), 0)
    return speed.value

standard_speed = get_current_speed()

while True:
    if get_current_speed() != standard_speed:
        print('Updating Mouse Speed!')
        change_speed(standard_speed)
        time.sleep(1)
