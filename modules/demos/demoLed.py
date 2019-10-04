
import RPi.GPIO as GPIO
import time

"""
LED = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)
try:
	while True:
		GPIO.output(LED,GPIO.HIGH)
		time.sleep(3)
		GPIO.output(LED,GPIO.LOW)
		time.sleep(1)
		print("done")
except:
	print("except")
	GPIO.cleanup()

"""

from gpiozero import LED,PWMLED
from time import sleep

#led attached to gpio26 (pin 37 in the board)
led = LED(26)
#led = LED("BCM26")
#led = LED("BOARD37")
try:
	while True:
		led.on()
		sleep(3)
		led.off()
		sleep(1)
		print("done cycle")
except KeyboardInterrupt:
	pass
	led.off()
	led.close()


"""
led = PWMLED(32) 
try:
	while True:
		for dc in range(0,101,5):
			led.value = dc/100  # off
			sleep(0.05)
		for dc in range(100,-1,-5):
			led.value = dc/100  # off
			sleep(0.05)
except KeyboardInterrupt:
	pass
	led.off()
	led.close()
"""