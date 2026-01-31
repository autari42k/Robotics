
from time import sleep
import RPi.GPIO as GPIO

button = 27
led1 = 22
led2 = 17
led3 = 2

LEDS = [
    led1, led2, led3
]

GPIO.setmode(GPIO.BCM)

GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
for i in range(len(LEDS)):
    GPIO.setup(LEDS[i], GPIO.OUT)

try:
    while True:
        button_state = GPIO.input(button)
        if button_state == GPIO.LOW:
            for _ in range(10):
                for pin in LEDS:
                    GPIO.output(pin, GPIO.HIGH)
                    sleep(0.5)
                
                for pin in reversed(LEDS):
                    GPIO.output(pin, GPIO.LOW)
                    sleep(0.5)
        else:
            for pin in LEDS:
                GPIO.output(pin, GPIO.LOW)
        
        sleep(0.01)

except KeyboardInterrupt:
    print("exiting")

finally:
    GPIO.cleanup()