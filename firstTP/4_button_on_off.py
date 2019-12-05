import RPi.GPIO as GPIO
import time

BUTTON=17
LED=27

# GPIO Number mode
GPIO.setmode(GPIO.BCM)
# Setup of the button
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup of the led
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

try:
	while True:
		# button state value
		button_state = GPIO.input(BUTTON)
		while ( button_state == True):
			GPIO.output(LED, GPIO.HIGH)
except:
	GPIO.cleanup()

