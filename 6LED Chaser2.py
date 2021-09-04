#6 LED Chaser-2
from machine import Pin
from time import sleep_ms

LED1 = Pin(16, Pin.OUT)
LED2 = Pin(17, Pin.OUT)
LED3 = Pin(18, Pin.OUT)
LED4 = Pin(19, Pin.OUT)
LED5 = Pin(20, Pin.OUT)
LED6 = Pin(21, Pin.OUT)
led = [LED1, LED2, LED3, LED4, LED5,LED6]



delay = 25

while True:
    for i in range(0, 5, 1):
        led[i].on()
        sleep_ms(delay)
        led[i+1].on()
        sleep_ms(delay)
        led[i].off()
        sleep_ms(delay*2)
    for i in range(5, 0, -1):
        led[i].on()
        sleep_ms(delay)
        led[i-1].on()
        sleep_ms(delay)
        led[i].off()
        sleep_ms(delay*2)