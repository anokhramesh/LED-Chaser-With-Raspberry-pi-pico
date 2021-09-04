#Knight Rider-3
from machine import Pin
from time import sleep_ms

Led_1 = Pin(16, Pin.OUT)
Led_2 = Pin(17, Pin.OUT)
Led_3 = Pin(18, Pin.OUT)
Led_4 = Pin(19, Pin.OUT)
Led_5 = Pin(20, Pin.OUT)
Led_6 = Pin(21, Pin.OUT)
led = [Led_1, Led_2, Led_3, Led_4, Led_5,Led_6]

delay = 30

while True:
    for i in range(0, 5, 1):
        led[i].on()
        sleep_ms(delay)
        led[i].off()
        sleep_ms(delay)
    for i in range(5, 0, -1):
        led[i].on()
        sleep_ms(delay)
        led[i].off()
        sleep_ms(delay)
