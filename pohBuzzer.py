import gpiozero
from smbus2 import SMBus
import time
address = 0x20

class zum():
   def __int__(self,busNumber=1, address=0x20):
      self.bus = SMBus(busNumber)
      self.address = address

   def beep_on():
    	bus.write_byte(address,0x7F&bus.read_byte(address)) #read one byte from address, offset 0
   def beep_off():
      bus.write_byte(address,0x80|bus.read_byte(address)) #read one byte from address, offset 0

   def Encender(self,sleepTime=1):
      beep_on()
      print("Encendido")    
      sleep(sleepTime)

   def Apagar(self,sleepTime=1):
      beep_off()
      print("Apagado")
      sleep(sleepTime)
      



