import sys
import time
import RPi.GPIO as GPIO
import time
import Adafruit_DHT

LED = 27
sensor = 22
pin = 17

GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, False)

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)


def askUserTemperature():
    value = int(
        input("Choose your temperature in degre Celsius [0...A lot]: "))
    return value


temperatureToDoNotReach = askUserTemperature()

while True:
    if humidity is not None and temperature is not None:
        #print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        if (temperature > temperatureToDoNotReach):
            GPIO.output(LED, True)
        else:
            GPIO.output(LED, False)
    else:
        print('Failed to get reading. Try again!')
    time.sleep(2)
