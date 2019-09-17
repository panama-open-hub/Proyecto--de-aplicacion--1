from gpiozero import LED
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
    
      

        
        
  



