import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 50)
p.start(2.5)  # initial position

def askUserAngle():
    value = input("Choose your angle in degrees [0...360]: ")
    return value

def changeAngle(angleChoosenInDegrees):
    pwmValue = 2.5 + (angleChoosenInDegrees/18)
    p.ChangeDutyCycle(pwmValue)

try:
    while True:
        changeAngle(askUserAngle())
        
except KeyboardInterrupt:
    p.stop()  # stop the pulse emission
    GPIO.cleanup()