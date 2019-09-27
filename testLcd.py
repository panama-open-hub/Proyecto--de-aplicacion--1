import pohLcd
from time import sleep

display = pohLcd.Pantalla()

display.Bienvenida()
sleep(1)
display.Limpiar()
sleep(1)

display.Test()
sleep(2)

display.Limpiar()
sleep(1)

display.Imprimir()
sleep(2)

display.FechaHora()
sleep(2)

display.Apagar()
print("Terminado")