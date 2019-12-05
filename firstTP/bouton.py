import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	while True:
			button_state = GPIO.input(18)
			if button_state == True:
				print('Button not Pressed...')
				time.sleep(0.05)
			else:
				print('Button Pressed...')
except:
	GPIO.cleanup()
