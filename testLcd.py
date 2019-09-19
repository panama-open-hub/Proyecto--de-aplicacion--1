import pohLcd
from time import sleep

display = pohLcd.Pantalla()
display.Encender()
sleep(3)
display.Test()
sleep(10)
display.Limpiar()
sleep(2)
display.Apagar()
print("Maquinitas xdd")