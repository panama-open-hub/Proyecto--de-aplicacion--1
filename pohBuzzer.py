from gpiozero import Buzzer,TonalBuzzer
from gpiozero.tones import Tone
from time import sleep
import logging
t = TonalBuzzer(27)
v1 = ["C4", "C4", "G4","G4","A4","A4","G4"]
v2 = ["F4","F4","E4","E4","D4","D4","C4"]
v3 = ["G4", "G4", "F4","F4","E4","E4","D4"]
v4 = ["C4", "D4", "E4","F4","G4","G4"]
v5 = ["A4","A4", "A4", "A4","G4","G4"]
v6 = ["F4", "F4", "F4","F4","E4","E4"]
v7 = ["D4","D4","D4","E4","C4","C4"]


class buzz():
   
   def __init__(self,pin=27):
      self.pin = pin

   def Encender(self):

      bz = Buzzer(self.pin)
      Buzzer.on()
      song = [v1,v2,v3,v3,v1,v2]

      for verse in song:
         for note in verse:
            t.play(note)
            sleep(0.4)
            t.stop()
            sleep(0.1)
         sleep(0.2)
      logging.debug("Encendido")

   def Apagado(self):

      bz= Buzzer(self.pin)
      
      Buzzer.on()

      song = [v4,v5,v6,v7]

      for verse in song:
         for note in verse:
            t.play(note)
            sleep(0.4)
            t.stop()
            sleep(0.1)
         sleep(0.2)
      Buzzer.off()

      logging.debug("Apagado")

   def log():

      logging.basicConfig(
         filename='logger.log',filemode='a', 
         format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
         level=logging.DEBUG)

"""
class Zumi2c():
   def __init__(self,busNumber=1,addr=0x20):
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
"""



