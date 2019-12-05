import RPi.GPIO as GPIO
import time
import random

LED_RED=5
#LED_BLUE=6
LED_GREEN=13

#BUTTON_RED=17

# GPIO Number mode
GPIO.setmode(GPIO.BCM)

# Setup of the button
#GPIO.setup(BUTTON_RED, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup of the leds
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.output(LED_RED, GPIO.LOW)

#GPIO.setup(LED_BLUE, GPIO.OUT)
#GPIO.output(LED_BLUE, GPIO.LOW)

GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.output(LED_GREEN, GPIO.LOW)

def lightRed():
    GPIO.output(LED_RED,GPIO.HIGH)

def offRed():
    GPIO.output(LED_RED,GPIO.LOW)
    
def lightGreen():
    GPIO.output(LED_GREEN,GPIO.HIGH)

def offGreen():
    GPIO.output(LED_GREEN,GPIO.LOW)

gameWon = False
secret = random.randrange(0,20,1)
numberOfTries = 4

try:
    while (gameWon == False):
        
        numberOfTries = numberOfTries - 1
        
        if (numberOfTries == -1):
            print("No more tries ! Sorry boloss !")
            break
        
        x = int(input("Type a number [0...20]:"))
        
        if (x == secret):
            lightGreen()
            break
        else:
            lightRed()
            time.sleep(2)
            offRed()

except:
	GPIO.cleanup()
