import RPi.GPIO as GPIO
import time

BUTTON_RED=17
BUTTON_BLUE=27
BUTTON_GREEN=22

LED_RED=5
LED_BLUE=6
LED_GREEN=13

# GPIO Number mode
GPIO.setmode(GPIO.BCM)

# Setup of the button
GPIO.setup(BUTTON_RED, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_BLUE, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_GREEN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# Setup of the leds
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.output(LED_RED, GPIO.LOW)

GPIO.setup(LED_BLUE, GPIO.OUT)
GPIO.output(LED_BLUE, GPIO.LOW)

GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.output(LED_GREEN, GPIO.LOW)

cmpt=0

try:
	while True:
                print(cmpt)
                cmpt = cmpt + 1
		# buttons states value
		button_state_red = GPIO.input(BUTTON_RED)
		button_state_blue = GPIO.input(BUTTON_BLUE)
		#button_state_green = GPIO.input(BUTTON_GREEN)
		
		if ( button_state_red == False):
			GPIO.output(LED_RED, GPIO.HIGH)
			print('LED_RED is up')
			time.sleep(1)
			GPIO.output(LED_RED, GPIO.LOW)
			
		
		if ( button_state_blue == False):
			GPIO.output(LED_BLUE, GPIO.HIGH)
			print('LED_BLUE is up')
			time.sleep(1)
			GPIO.output(LED_BLUE, GPIO.LOW)
		
		#if ( button_state_green == True):
		#	GPIO.output(LED_GREEN, GPIO.HIGH)
		#	print('LED_GREEN is up')
		#	GPIO.output(LED_GREEN, GPIO.LOW)
		#	time.sleep(1)
except:
	GPIO.cleanup()

