import RPi.GPIO as GPIO
import time

def askUserMeterOrFeet():
    choice = raw_input("Meter(m) or feet(f): ")
    if (choice == "f"):
        return True
    else:
        return False

mesureInFeet = askUserMeterOrFeet()

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

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

        print("Distance:" + str(distance) + "cm")

        distanceInMeter = distance/100

        if mesureInFeet:
            print("Distance in feets: " + str(distanceInMeter*3.28) + "ft")
        else:
            print("Distance in meters: " + str(distanceInMeter) + "m")

except KeyboardInterrupt:
    GPIO.cleanup()
