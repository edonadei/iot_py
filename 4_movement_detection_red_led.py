import RPi.GPIO as GPIO
import time
PIR_MOTION = 17
RED_LED = 27
GREEN_LED = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_MOTION, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

GPIO.output(GREEN_LED, False)
GPIO.output(RED_LED, False)


try:
    while True:
        if GPIO.input(PIR_MOTION):
            # When output from motion sensor is HIGH
        GPIO.output(RED_LED, False)
        GPIO.output(GREEN_LED, True)
    else:
        # When output from motion sensor is LOW
        GPIO.output(GREEN_LED, False)
        GPIO.output(RED_LED, True)
except KeyboardInterrupt
