import RPi.GPIO as GPIO
import time

LED_RED=5
LED_BLUE=6
LED_GREEN=13

BUTTON_RED=17

# GPIO Number mode
GPIO.setmode(GPIO.BCM)

# Setup of the button
GPIO.setup(BUTTON_RED, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup of the leds
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.output(LED_RED, GPIO.LOW)

GPIO.setup(LED_BLUE, GPIO.OUT)
GPIO.output(LED_BLUE, GPIO.LOW)

GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.output(LED_GREEN, GPIO.LOW)

try:
	while True:
            button_state_red = GPIO.input(BUTTON_RED)
	
            if (button_state_red == True):
                time.sleep(0.5)
                GPIO.output(LED_RED, GPIO.HIGH)
                    
            else:
                GPIO.output(LED_RED,GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(LED_BLUE, GPIO.HIGH)
                time.sleep(2)
                GPIO.output(LED_BLUE,GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(LED_GREEN, GPIO.HIGH)
                time.sleep(5)
                GPIO.output(LED_GREEN,GPIO.LOW)
                GPIO.output(LED_RED, GPIO.LOW)

except:
	GPIO.cleanup()
