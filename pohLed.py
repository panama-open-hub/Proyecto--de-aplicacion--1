#!/usr/bin/python3.4
import gpiozero as GPIO
import time
from signal import pause

led = LED(26)
button = Button(3)

button.when_pressed = led.on
button.when_released = led.off

pause()

try:
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT, initial = GPIO.LOW)
print(“Printing SOS”)

#S
GPIO.output(26,GPIO.HIGH)
time.sleep(0.5)
GPIO.output(26,GPIO.LOW)

time.sleep(0.5)

GPIO.output(26,GPIO.HIGH)
time.sleep(0.5)
GPIO.output(26,GPIO.LOW)

time.sleep(0.5)

GPIO.output(26,GPIO.HIGH)
time.sleep(0.5)
GPIO.output(26,GPIO.LOW)
#End of S

time.sleep(1.5)

#O
GPIO.output(26,GPIO.HIGH)
time.sleep(1.5)
GPIO.output(26,GPIO.LOW)

time.sleep(0.5)

GPIO.output(26,GPIO.HIGH)
time.sleep(1.5)
GPIO.output(26,GPIO.LOW)

time.sleep(0.5)

GPIO.output(26,GPIO.HIGH)
time.sleep(1.5)
GPIO.output(26,GPIO.LOW)
#End of O

time.sleep(1.5)

#S
GPIO.output(26,GPIO.HIGH)
time.sleep(0.5)
GPIO.output(26,GPIO.LOW)

time.sleep(0.5)

GPIO.output(26,GPIO.HIGH)
time.sleep(0.5)
GPIO.output(26,GPIO.LOW)

time.sleep(0.5)

GPIO.output(26,GPIO.HIGH)
time.sleep(0.5)
GPIO.output(26,GPIO.LOW)
#End of S

time.sleep(1.5)

print(“Finished”)

except Exception as ex:
print(“Error Occured”, ex)
finally:
GPIO.cleanup()