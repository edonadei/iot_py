import RPi.GPIO as GPIO
import time

BUZZER=5
BUTTON=17

# GPIO Number mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup of the leds
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.output(BUZZER, GPIO.LOW)

def buzzerON():
    GPIO.output(BUZZER,GPIO.HIGH)

def buzzerOFF():
    GPIO.output(BUZZER,GPIO.LOW)

try:
    while True:
        button_state = GPIO.input(BUTTON)
        if (button_state == False):
            buzzerON()
        else:
            buzzerOFF()

except:
	GPIO.cleanup()
