import RPi.GPIO as GPIO
import time
from threading import Thread

GPIO.setmode(GPIO.BCM)

RED_LED = 27
GREEN_LED = 22
BUZZER = 17

TRIG = 23
ECHO = 24

GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.output(RED_LED, False)
GPIO.output(GREEN_LED, False)
GPIO.output(BUZZER, False)

class AsyncBuzzer():
    def __init__(self):
        thread = Thread(target=self.run, args=())
        thread.daemon = True                            
        thread.start()                                  

    def run(self):
        while True:
            GPIO.output(BUZZER, True)
            time.sleep(self.timeBuzzer)
            GPIO.output(BUZZER, False)
            break


def humanDetected(distance):
    if distance < 101:
        GPIO.output(RED_LED, True)
        GPIO.out(GREEN_LED, False)
        AsyncBuzzer()
    else:
        GPIO.output(RED_LED, False)
        GPIO.out(GREEN_LED, True)



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
        humanDetected(distance)

except KeyboardInterrupt:
    GPIO.cleanup()
