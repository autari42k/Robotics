from gpiozero import LED
from time import sleep

leds = [
    LED(17), LED(22), LED(27)
]
for j in range(5):
    for i in range(0, len(leds) ):
        leds[i].on()
        sleep(0.7)
        leds[i].off() 
