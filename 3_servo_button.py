import RPi.GPIO as GPIO
import time

BUTTON=17
MOTOR=12

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

p = GPIO.PWM(12, 50)
p.start(2.5)  # initial position


def askUserAngle():
    value = input("Choose your angle in degrees [0...360]: ")
    return value

def changeAngle(angleChoosenInDegrees):
    pwmValue = 2.5 + (angleChoosenInDegrees/18)
    p.ChangeDutyCycle(pwmValue)

initialAngleInDegree = 0

try:
    while True:
        
        button_state = GPIO.input(BUTTON)
        if (button_state == False):
            if (initialAngleInDegree == 180):
                initialAngleInDegree = 0
            else:
                initialAngleInDegree = initialAngleInDegree + 60
                changeAngle(initialAngleInDegree)        
except KeyboardInterrupt:
    p.stop()  # stop the pulse emission
    GPIO.cleanup()