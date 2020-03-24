from machine import Pin
import machine

import time

for i in range(0,9):
    
    led=Pin(4,Pin.OUT)
    led(1)
    time.sleep(1)
    led(0)
    time.sleep(1)

from wifi_connect import *
from epd import *



# print('sleeping in 2 seconds')
# time.sleep(2)
#machine.deepsleep(300000)

