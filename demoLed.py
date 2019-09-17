#!/usr/bin/python3
from gpiozero import PWMLED
from time import sleep

led = PWMLED(26) 

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