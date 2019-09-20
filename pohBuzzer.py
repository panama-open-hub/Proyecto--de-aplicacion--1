import gpiozero
from smbus2 import SMBus
from time import sleep


class Zum():
   def __init__(self,busNumber=1, addr=0x20):
      self.address = addr
      self.buss = SMBus(busNumber)

   def beep_on(self):
    	self.buss.write_byte(self.address,0x7F&self.buss.read_byte(self.address)) #read one byte from address, offset 0
   def beep_off(self):
      self.buss.write_byte(self.address,0x80|self.buss.read_byte(self.address)) #read one byte from address, offset 0

   def Encender(self,sleepTime=1):
      self.beep_on()
      print("Encendido")    
      sleep(sleepTime)

   def Apagar(self,sleepTime=1):
      self.beep_off()
      print("Apagado")
      sleep(sleepTime)
      



