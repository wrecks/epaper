import wifi
import ntptime
from machine import RTC


def time_pull():
    wifi.do_connect() #connect to wifi
    ntptime.settime() #pull time from NTP server
    (year, month, mday, week_of_year, hour, minute, second, milisecond)=RTC().datetime() 
    RTC().init((year, month, mday, week_of_year, hour-7, minute, second, milisecond))
    print('{:02d}/{:02d}/{:02d} {:02d}:{:02d}.{:02d}'.format(RTC().datetime()[1],RTC().datetime()[2],RTC().datetime()[0],RTC().datetime()[4],RTC().datetime()[5],RTC().datetime()[6]))