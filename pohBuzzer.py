from gpiozero import Buzzer,TonalBuzzer
from gpiozero.tones import Tone
from time import sleep
from smbus2 import SMBus
import logging
import asyncio




class Zum():
   def __init__(self,pin=27):
      self.pin = pin
      self.bz = Buzzer(self.pin)
      logging.debug("Zumbador inicializado en el pin# " + str(self.pin))


   def Encender(self):
      if self.bz.is_active == False:
         self.bz.on()
         logging.debug("Bocina encendido")
   
   def Apagar(self):
      if self.bz.is_active == True:
         self.bz.off()
         logging.debug("Bocina apagada")

   def Test(self):
      if self.bz.is_active == False:
         self.bz.on()
         sleep(2)
         self.bz.off()
         sleep(2)
         self.bz.on()
         sleep(1)
         self.bz.off()
         sleep(1)
         self.bz.on()
         sleep(0.5)
         self.bz.off()
         sleep(0.5)

   async def Encender_Async(self):
      if self.bz.is_active == False:
         self.bz.on()
         logging.debug("Bocina encendido")
   
   async def Apagar_Async(self):
      if self.bz.is_active == True:
         self.bz.off()
         logging.debug("Bocina apagada")


class Zumi2c():
   def __init__(self,busNumber=1,addr=0x20):
      self.address = addr
      self.buss = SMBus(busNumber)
      logging.debug("Zumbador i2c inicializado en el pin# " )

   def beep_on(self):
    	self.buss.write_byte(self.address,0x7F&self.buss.read_byte(self.address)) #read one byte from address, offset 0
   def beep_off(self):
      self.buss.write_byte(self.address,0x80|self.buss.read_byte(self.address)) #read one byte from address, offset 0

   def Encender(self,sleepTime=1):
      logging.debug("Bocina encendida") 
      self.beep_on()
      sleep(sleepTime)

   def Apagar(self,sleepTime=1):
      self.beep_off()
      logging.debug("Bocina apagada")
      sleep(sleepTime)

   def Test(self):
      logging.debug("Bocina iniciando prueba")
      self.beep_on()
      sleep(2)
      self.beep_off()
      sleep(2)
      self.beep_on()
      sleep(1)
      self.beep_off()
      sleep(1)
      self.beep_on()
      sleep(0.5)
      self.beep_off()
      sleep(0.5)
   
   async def Encender_Async(self,sleepTime=0):
      await self.beep_on()
      logging.debug("Bocina encendida asincronicamente") 

   async def Apagar_Async(self,sleepTime=0):
      await self.beep_off()
      logging.debug("Bocina apagada asincronicamente")

   async def Test_Async(self):
      logging.debug("Bocina iniciando prueba")
      self.beep_on()
      await asyncio.sleep(3)
      self.beep_off()
      await asyncio.sleep(3)
      self.beep_on()
      await asyncio.sleep(2)
      self.beep_off()
      await asyncio.sleep(2)
      self.beep_on()
      await asyncio.sleep(1)
      self.beep_off()
      await asyncio.sleep(1)
      self.beep_on()
      await asyncio.sleep(0.5)
      self.beep_off()
      await asyncio.sleep(0.5)
   
   async def Inicio_Async(self):
         logging.debug("Tocando tonada de inicio")
         self.beep_on()
         await asyncio.sleep(0.25)
         self.beep_off()
         await asyncio.sleep(0.25)
         self.beep_on()
         await asyncio.sleep(0.25)
         self.beep_off()
         await asyncio.sleep(0.25)
         self.beep_on()
         await asyncio.sleep(0.25)
         self.beep_off()
         await asyncio.sleep(0.25)



class ZumTonal():
   def __init__(self,pin=27):
      self.pin = pin
      self.bz = TonalBuzzer(self.pin)
      
   def EscucharCancion(self, idx = 1):
      v1 = ["C4", "C4", "G4","G4","A4","A4","G4"]
      v2 = ["F4","F4","E4","E4","D4","D4","C4"]
      v3 = ["G4", "G4", "F4","F4","E4","E4","D4"]
      v4 = ["C4", "D4", "E4","F4","G4","G4"]
      v5 = ["A4","A4", "A4", "A4","G4","G4"]
      v6 = ["F4", "F4", "F4","F4","E4","E4"]
      v7 = ["D4","D4","D4","E4","C4","C4"]
      
      if idx == 1:
         song = [v1,v2,v3,v3,v1,v2]
      else:
         song = [v4,v5,v6,v7]

      self.bz.on()
      for verse in song:
         for note in verse:
            self.bz.play(note)
            sleep(0.4)
            self.bz.stop()
            sleep(0.1)
         sleep(0.2)
      self.bz.off()







