import pohLcd
from time import sleep

display = pohLcd.Pantalla()

display.Bienvenida()
sleep(1)
display.Limpiar()
sleep(1)

display.Test()
sleep(3)

display.Limpiar()
sleep(1)

display.Imprimir()
sleep(5)

display.FechaHora()
sleep(7)

display.Apagar()
print("Terminado")