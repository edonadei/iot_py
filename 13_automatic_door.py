import RPi.GPIO as GPIO
import time
from threading import Thread

GPIO.setmode(GPIO.BCM)

RED_LED = 27
GREEN_LED = 22
MOTOR = 17

TRIG = 23
ECHO = 24

GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.output(RED_LED, False)
GPIO.output(GREEN_LED, False)

GPIO.setup(MOTOR, GPIO.OUT)
p = GPIO.PWM(12, 50)
p.start(2.5)  # initial position

global canStartAnotherThread
canStartAnotherThread = True


class AsyncBehavior1():
    def __init__(self):
        thread = Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            # do something


class AsyncBehavior2():
    def __init__(self):
        thread = Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            # do something


def calculateDistance():
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
    return distance = round(distance, 2)


def shopOpened():
    GPIO.output(GREEN_LED, True)
    GPIO.out(RED_LED, False)
    While True:
        if (calculateDistance() < 101):
            p.ChangeDutyCycle(7.5)  # turn towards 90 degree
        else:
            p.ChangeDutyCycle(2.5)  # turn towards 90 degree


def shopClosed():
    GPIO.output(GREEN_LED, False)
    GPIO.out(RED_LED, True)


print("Distance Measurement In Progress")
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("Waiting For Sensor To Settle")
time.sleep(2)

try:
    while True:
        calculateDistance()

except KeyboardInterrupt:
    GPIO.cleanup()
