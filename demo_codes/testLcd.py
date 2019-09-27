import pohLcd
from time import sleep

Display = pohLcd.Pantalla()

Display.Encender()
sleep(3)
Display.Limpiar()
sleep(2)
Display.Apagar()
print("Maquinitas xdd")