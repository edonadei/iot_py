import sys
import time
import RPi.GPIO as GPIO
import time
import Adafruit_DHT

sensor = 22
pin = 17

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

f = open("temp_and_humidity.txt","w+")
f.write("Temperature: {}°C\nHumidity: {}".format(temperature,humidity))
