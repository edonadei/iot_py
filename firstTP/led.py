import RPi.GPIO as GPIO
import time
LED=17
LED2=27
FRESH=input("Enter value ")

# were using gpio numbers
GPIO.setmode(GPIO.BCM)

GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT)
GPIO.output(LED2, GPIO.LOW)

try:
	while True:
		GPIO.output(LED, GPIO.HIGH)
		GPIO.output(LED2, GPIO.LOW)
		time.sleep(FRESH)
		GPIO.output(LED, GPIO.LOW)
		GPIO.output(LED2, GPIO.HIGH)
		time.sleep(FRESH)
except KeyboardInterrupt:
	GPIO.cleanup()

