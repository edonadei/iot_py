import RPi.GPIO as GPIO
import time

LED_RED=5
LDR=17
BUZZER=18

# GPIO Number mode
GPIO.setmode(GPIO.BCM)

# Setup of the button
GPIO.setup(LDR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup of the leds
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.output(LED_RED, GPIO.LOW)

# Set of the buzzer
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.output(BUZZER, GPIO.LOW)

def beepON():
    GPIO.output(BUZZER, GPIO.HIGH)

def beepOFF():
    GPIO.output(BUZZER, GPIO.LOW)

def redON():
    GPIO.output(LED_RED, GPIO.HIGH)
    
def redOFF():
    GPIO.output(LED_RED, GPIO.LOW)

isDark = False;
isDarkWarning = False;

try:
	while True:
            ldr_state = GPIO.input(LDR)
	
            if (isDark):
                beepON()
                time.sleep(2)
                beepOFF()
                isDark = False
                isDarkWarning = True
                
            if (isDarkWarning):
                redON()
	
            if (ldr_state == True):
                if (isDarkWarning != True):
                    isDark = True
            else:
                isDark = False
                isDarkWarning = False
                redOFF()
                beepOFF()
                
except:
	GPIO.cleanup()
