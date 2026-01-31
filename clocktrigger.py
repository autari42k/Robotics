import time
import RPi.GPIO as GPIO
from datetime import datetime

servo = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)

pwm = GPIO.PWM(servo, 50)
pwm.start(0)

def set_angle(angle):
    duty = 2 + (angle/18)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(0)


try:
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")

        if current_time == "11:40":
            print("Move to 90 degrees at 6:00 AM")
            set_angle(90)
except KeyboardInterrupt:
    print("Exiting...")

finally:
    pwm.stop()
    GPIO.cleanup()
    