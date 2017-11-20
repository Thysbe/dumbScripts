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


def proper_close():
    change_speed(standard_speed)
    root.destroy()

standard_speed = get_current_speed()


while True:
    print('Updating Mouse Speed!')
    change_speed(standard_speed)
    time.sleep(10)