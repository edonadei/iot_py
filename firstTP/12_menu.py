import RPi.GPIO as GPIO
import time
import random

LED_RED=5
LED_BLUE=6
LED_GREEN=13

# GPIO Number mode
GPIO.setmode(GPIO.BCM)

# Setup of the leds
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.output(LED_RED, GPIO.LOW)

GPIO.setup(LED_BLUE, GPIO.OUT)
GPIO.output(LED_BLUE, GPIO.LOW)

GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.output(LED_GREEN, GPIO.LOW)

def redON():
    GPIO.output(LED_RED, GPIO.HIGH)
    
def blueON():
    GPIO.output(LED_BLUE, GPIO.HIGH)
    
def greenON():
    GPIO.output(LED_GREEN, GPIO.HIGH)
    
def redOFF():
    GPIO.output(LED_RED, GPIO.LOW)
    
def blueOFF():
    GPIO.output(LED_BLUE, GPIO.LOW)
    
def greenOFF():
    GPIO.output(LED_GREEN, GPIO.LOW)

try:
	while True:
            menu_choice = input("Make your choice: ")
            if (menu_choice == "1"):
                redON()
            elif (menu_choice == "2"):
                redOFF()
            elif (menu_choice == "3"):
                blueON()
            elif (menu_choice == "4"):
                blueOFF()
            elif (menu_choice == "5"):
                greenON()
            elif (menu_choice == "6"):
                greenOFF()
            elif (menu_choice == "7"):
                redON()
                blueON()
                greenON()
            elif (menu_choice == "8"):
                redOFF()
                blueOFF()
                greenOFF()
            elif (menu_choice == "9"):
                randomNumber = random.randrange(0,3)
                print(randomNumber)
                if (randomNumber == 0):
                    redON()
                elif (randomNumber == 1):
                    greenON()
                elif (randomNumber == 2):
                    blueON()
            elif (menu_choice == 0):
                print("Bye bye :)")
                break
            else:
                print("No choice")

except:
	GPIO.cleanup()
