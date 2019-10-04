from gpiozero import LED,PWMLED
from datetime import datetime, timedelta
import time 
import logging
import asyncio

class Luz():
    def __init__(self, pin):
        self.pin = pin #gpio pin, not the board pin
        self.foco = LED(self.pin)

    def Encender(self):
        self.foco.on()
        logging.debug('Todo bien')

    async def Encender_Async(self):
        self.foco.on()
        await asyncio.sleep(1)
        
    def Apagar(self):
        if self.foco.is_active == True:
            self.foco.off()
        else:
            pass
    
    async def Apagar_Async(self):
        if self.foco.is_active == True:
            self.foco.off()
            await asyncio.sleep(1)
    
    def Parpadeo(self):
        while self.foco.on == True:
            timeout = 10   # [seconds]
            timeout_start = time.time()
            test = 0
            #print(datetime.now(),"Contando")
            while time.time() < timeout_start + timeout:
                if test == 10:
                    #print("Works")
                     #print(datetime.now())
                     break
                test = test + 1
                #print(datetime.now())
            self.foco.n(100)
            #print(datetime.now(),"Dispositivo apagandose") 
    

    async def Parpadeo_Async(self):
        self.foco.on()
        await asyncio.sleep(2)
        self.foco.off()


    def Brillo(self):
        while self.foco.on == True:
            tiempo = 10   # [seconds]
            timeout_start = time.time()
            test = 0
            print(datetime.now(),"Contando")
            while time.time() < timeout_start + tiempo:
                if test == 20:
                    print("Works 2")
                    #print(datetime.now())
                    #break
                test = test + 1
                #print(datetime.now())
            print(datetime.now(),"Brillo del LED?")
            brillo1 = int(input())
            brillopwm = brillo1/100.0
            print(str(brillopwm))
            PWMLED.intial_value(brillopwm)
            print("Brillo regulado a:%s" %brillo1)




