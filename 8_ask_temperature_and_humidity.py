import os
import glob
import time
import RPi.GPIO as GPIO
import time

RED_LED = 17
GREEN_LED = 22

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)

GPIO.output(RED_LED, False)
GPIO.output(GREEN_LED, False)

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
    return temp_c, temp_f

def askUserTemperature():
    value = int(input("Choose your temperature in degre Celsius [0...A lot]: "))
    return value

def askUserHumidity():
    value = int(input("Choose your humidity value: "))
    return value

temperatureToDoNotReach = askUserTemperature()
humidityToDoNotReach = askUserHumidity()

while True:
    if (read_temp() > temperatureToDoNotReach):
        GPIO.output(RED_LED, True)
    else: 
        GPIO.output(RED_LED, False)

    if (read_temp() > humidityToDoNotReach):
        GPIO.output(GREEN_LED, True)
    else: 
        GPIO.output(GREEN_LED, False)
