import RPi.GPIO as GPIO
import time

LED_RED=5
LED_BLUE=6
LED_GREEN=13

BUTTON_RED=17
BUTTON_BLUE=27
BUTTON_GREEN=22

BUZZER=18

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

# Set of the buzzer
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.output(BUZZER, GPIO.LOW)

def beep():
    GPIO.output(BUZZER, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(BUZZER,GPIO.LOW)
    time.sleep(0.2)

def redON():
    GPIO.output(LED_RED, GPIO.HIGH)
    beep()
    beep()
    beep()
    time.sleep(1)
    
def blueON():
    GPIO.output(LED_BLUE, GPIO.HIGH)
    beep()
    beep()
    time.sleep(1)
    
def greenON():
    GPIO.output(LED_GREEN, GPIO.HIGH)
    beep()
    time.sleep(1)
    
def redOFF():
    GPIO.output(LED_RED, GPIO.LOW)
    
def blueOFF():
    GPIO.output(LED_BLUE, GPIO.LOW)
    
def greenOFF():
    GPIO.output(LED_GREEN, GPIO.LOW)

try:
	while True:
            button_state_red = GPIO.input(BUTTON_RED)
            button_state_blue = GPIO.input(BUTTON_BLUE)
            button_state_green = GPIO.input(BUTTON_GREEN)
	
            if (button_state_red == False):
                redON()
            else:
                redOFF()
                
            if (button_state_blue == False):
                blueON()
            else:
                blueOFF()
                
            if (button_state_green == False):
                greenON()
            else:
                greenOFF()

except:
	GPIO.cleanup()
