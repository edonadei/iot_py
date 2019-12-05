import sys
import time
import RPi.GPIO as GPIO
import time
import Adafruit_DHT

RED_LED = 27
GREEN_LED = 22
sensor = 22
pin = 17

GPIO.setup(RED_LED, GPIO.OUT)
GPIO.output(RED_LED, False)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.output(GREEN_LED, False)

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)


def askUserTemperature():
    value = int(
        input("Choose your temperature in degre Celsius [0...A lot]: "))
    return value


def askUserHumidity():
    value = int(input("Choose your humidity value: "))
    return value

temperatureToDoNotReach = askUserTemperature()
humidityToDoNotReach = askUserHumidity()

while True:
    if humidity is not None and temperature is not None:
        if (temperature > temperatureToDoNotReach):
            GPIO.output(RED_LED, True)
        else:
            GPIO.output(RED_LED, False)

        if (humidity > humidityToDoNotReach):
            GPIO.output(GREEN_LED, True)
        else:
            GPIO.output(GREEN_LED, False)
    else:
        print('Failed to get reading. Try again!')
    time.sleep(2)
