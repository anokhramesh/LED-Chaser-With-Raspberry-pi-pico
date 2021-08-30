from machine import Pin
from time import sleep

led1 = Pin(10, Pin.OUT)
led2 = Pin(11, Pin.OUT)
led3 = Pin(12, Pin.OUT)
led4 = Pin(13, Pin.OUT)
led5 = Pin(14, Pin.OUT)
led6 = Pin(15, Pin.OUT)
def Led_chaser (a,b,c,d,e,f):
    led1.value(a)
    led2.value(b)
    led3.value(c)
    led4.value(d)
    led5.value(e)
    led6.value(f)
    sleep(0.25)

while True:
    Led_chaser(0,0,0,0,0,0)
    Led_chaser(0,0,0,0,0,1)
    Led_chaser(0,0,0,0,1,1)
    Led_chaser(0,0,0,1,1,1)
    Led_chaser(0,0,1,1,1,1)
    Led_chaser(0,1,1,1,1,1)
    Led_chaser(1,1,1,1,1,1)
    Led_chaser(1,1,1,1,1,0)
    Led_chaser(1,1,1,1,0,0)
    Led_chaser(1,1,1,0,0,0)
    Led_chaser(1,1,0,0,0,0)
    Led_chaser(1,0,0,0,0,0)
   
    
    
    