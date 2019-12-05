import RPi.GPIO as GPIO
import time
PIR_MOTION = 17
RED_LED = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_MOTION, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RED_LED, GPIO.OUT)

GPIO.output(RED_LED, False)

def blinkLED():
    GPIO.output(RED_LED, True)
    time.sleep(0.2)
    GPIO.output(RED_LED, False)

try:
    while True:
        if GPIO.input(PIR_MOTION):
            # When output from motion sensor is HIGH
            blinkLED()
            
except KeyboardInterrupt:
    GPIO.cleanup()