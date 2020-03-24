import machine
from machine import Pin, I2C, ADC
import time
import urequests
from time import sleep
import ads1x15

i2c = machine.I2C(-1,scl=machine.Pin(35), sda=machine.Pin(33))
i2c.init(scl=machine.Pin(12), sda=machine.Pin(33),freq=400000)

ag_address=72 #analog address
gain=0 #analog read gain (0-6.144v)
adc_1115 = ads1x15.ADS1115(i2c, ag_address, gain) #voltage analog
raw_v=adc_1115.read(1,0)
volt = adc_1115.raw_to_v(raw_v) #converted voltage
print(volt)