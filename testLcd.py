import pohLcd
from time import sleep

display = pohLcd.Pantalla()
display.Encender()
sleep(5)

display.Test()
sleep(10)

display.Limpiar()
sleep(2)

display.Imprimir()
sleep(10)

display.Apagar()
print("Terminado")