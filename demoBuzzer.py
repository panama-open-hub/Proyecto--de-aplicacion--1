from gpiozero import Button
from smbus2 import SMBus
import time

address = 0x20

def beep_on():
	bus.write_byte(address,0x7F&bus.read_byte(address)) #read one byte from address, offset 0
def beep_off():
	bus.write_byte(address,0x80|bus.read_byte(address)) #read one byte from address, offset 0
<<<<<<< Updated upstream
bus = SMBus(1)# Open i2c bus 1
=======
bus = SMBus(1) # Open i2c bus 1
    



>>>>>>> Stashed changes


if __name__ == '__main__':		# Program start from here
	try:
		beep_on()
		time.sleep(1.0)
		beep_off()
		time.sleep(3.0)
	except KeyboardInterrupt:  	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		pass