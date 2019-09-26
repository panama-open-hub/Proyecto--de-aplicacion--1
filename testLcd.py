import pohLcd
from time import sleep

display = pohLcd.Pantalla()

display.Encender()
sleep(1)
display.Limpiar()
sleep(1)
"""
display.Test()
sleep(3)
"""


display.Imprimir()
sleep(5)

display.FechaHora()
sleep(4)



display.Apagar()
print("Terminado")