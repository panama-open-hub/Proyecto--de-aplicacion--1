from datetime import datetime, timedelta
from gpiozero import LED,PWMLED
import time
tiempo = 20
timeout = 10   # [seconds]
timeout_start = time.time()
test = 0
print(datetime.now(),"Contando")
while time.time() < timeout_start + timeout:
    if test == 10:
        print("Works")
        #print(datetime.now())55
        #break
    test = test + 1
    #print(datetime.now())
#led.n(10)
print(datetime.now(),"Dispositivo apagandose") 
while time.time() < timeout_start + tiempo:
    if test == 20:
        print("Works 2")
        #print(datetime.now())
        #break
    test = test + 1
    #print(datetime.now())
#led.n(10)
print(datetime.now(),"Brillo del LED?")
brillo = int(input())
brillopwm = brillo/100.0
x = round(brillopwm,2)
print(str(x))
print("Brillo regulado a:%s,porciento" %brillo)
