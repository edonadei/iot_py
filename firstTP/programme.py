#! /usr/bin/env python
# enable functions and methods to manage the Pi
import RPi.GPIO as GPIO
# enable use of functions of time
import time
# GPIO used to connect an anode leg LED
# GPIO 17 is equal PIN 11 follow the physical enumeration
LED=17
#time to wait
FRESH=1
# setup the enumeration based on GPIO references 1
GPIO.setmode(GPIO.BCM)
# setup the port 17 as output, in this PIN the energy will go out
GPIO.setup(LED, GPIO.OUT)

#setup to have not energy by the port 17
GPIO.output(LED, GPIO.LOW)
# code of protection; if has no problem the block try will keep always on
try:
# infinite loop
	while True:
# Active the transmission of energy by port 17
		GPIO.output(LED, GPIO.HIGH)
# Wait 1 second
		time.sleep(FRESH)
# Cut off the transmission of energy
 		GPIO.output(LED, GPIO.LOW)
# wait 1 second
		time.sleep(FRESH)
# exceptions are anything that interrupt the try block.
# if a CTRL_C be pressed
except KeyboardInterrupt:
# setup the GPIO to default values; finish any transmission of energy
			GPIO.cleanup()