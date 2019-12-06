import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

RED_LED = 27
TRIG = 23
ECHO = 24

def blinkLED(timeblink = 0.2):
    GPIO.output(RED_LED, False)
    time.sleep(timeblink)
    GPIO.output(RED_LED, True)
    time.sleep(timeblink)

GPIO.setup(RED_LED, GPIO.OUT)
GPIO.output(RED_LED, False)

print("Distance Measurement In Progress")
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("Waiting For Sensor To Settle")
time.sleep(2)

try:
    while True:
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        pulse_start = 0
        pulse_end = 0

        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)

        GPIO.output(RED_LED, False)
        GPIO.output(RED_LED, True)
        print("Distance:" + str(distance) + "cm")
        # var distance
        # if distance is > 1m blink 1s
        if (distance > 1000):
            blinkLED(1)
        elif (distance > 5 and distance < 1001):
            blinkLED(0.001*distance)
        else:
            blinkLED(0.05)
        # if distance >5cm & <1m blink proportionally 
        # if distance <5cm blink 50ms
except KeyboardInterrupt:
    GPIO.cleanup()
