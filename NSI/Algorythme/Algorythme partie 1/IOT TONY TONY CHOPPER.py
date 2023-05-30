#code de la petite carte:
from machine import Pin,I2C,RTC
from time import sleep

rtc = RTC()

#(year, month, day, weekday, hours, minutes, seconds, subseconds)
rtc.datetime((2023, 01, 12, 02,15,19, 15,0)) 

while True:
    horloge=rtc.datetime()
    print(horloge)
    sleep(1)
    