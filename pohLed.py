from gpiozero import LED
from datetime import datetime, timedelta
import time 

class Luz():
    def __init__(self, pin):
        self.pin = pin

    def Encender(self):
        led = LED(self. pin)
        led.on()
        print("Todo Bien")
        
    def Apagar(self):
        led = LED(self.pin)
        if LED.is_active == True:
            led.off()
        else:
            pass
    
    def Parpadeo(self):
        led = LED(self.pin)
        while led.on == True:
            timeout = 5   # [seconds]
            timeout_start = time.time()
            test = 0
            print(datetime.now(),"Contando")
            while time.time() < timeout_start + timeout:
                if test == 5:
                    print("Works")
                     #print(datetime.now())
                     #break
                test = test + 1
                #print(datetime.now())
            led.n(10)
            print(datetime.now(),"Dispositivo apagandose") 



