import os
os.chdir('/main')

import machine
import time
import epd
from write_log import reset_log
from machine import WDT
import wifi
import epd

#wdt = WDT(timeout=300000)

if machine.reset_cause()!=3:
    
    try:
        wifi.do_connect()
        epd.epd_pull()
        reset_log('0')
        #machine.deepsleep(300000)
    except Exception as mod_error:
        print('An error occured with one of the modules. Going to sleep in 5 seconds.')
        time.sleep(5)
        machine.reset()
        #machine.deepsleep(300000)
else:
    reset_log('1')
    f=open("reset_log.txt", "r")
    cycles=f.read()
    f.close()
    if int(cycles)>10:
        print('Too many resets. Shutting off.')
    else:
        machine.reset()

    
