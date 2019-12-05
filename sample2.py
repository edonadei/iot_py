import RPi.GPIO as GPIO
import time
PIR_MOTION = 4
LED = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_MOTION, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED, GPIO.OUT)

GPIO.output(LED, False)
try:
    while True:
        if GPIO.input(PIR_MOTION):
            # When output from motion sensor is HIGH
        print("Motion Detected")
        GPIO.output(LED, True)
    else:
        # When output from motion sensor is LOW
        GPIO.output(LED, False)
        except KeyboardInterrupt
