import pohLcd
from time import sleep

display = pohLcd.Pantalla()
display.Encender()
sleep(5)

display.Test()
sleep(5)

display.Limpiar()
sleep(2)

display.Imprimir()
sleep(5)

display.FechaHora()
sleep(3)

display.Apagar()
print("Terminado")