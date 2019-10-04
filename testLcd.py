import pohLcd 
import pohLed
import time
import asyncio
import logging

try:
	logging.basicConfig(level=logging.DEBUG)
	pantalla1 = pohLcd.Pantalla()
	loop = asyncio.get_event_loop()
	loop.run_until_complete(pantalla1.MostrarFechaHora_async(True))
except KeyboardInterrupt:
	pass
finally:
	loop.close()
	print("Closing Loop")


	
"""
Led1 = pohLed.Luz(26)
display = pohLcd.Pantalla()
async def runPantalla():
	try:
		await asyncio.gather(display.Bienvenida_Async())
		await asyncio.sleep(2)
		while True:
			await asyncio.gather(display.FechaHora_async())
			await asyncio.sleep(0.98)
	except KeyboardInterrupt:
		await asyncio.gather(display.Limpiar_async(), display.Apagar_async())
		elapsed = time.perf_counter() - s
		print(f"{__file__} executed in {elapsed:0.2f} seconds.")
    
async def runLed():
	try:
		while True:
			await asyncio.gather(Led1.Encender_Async())
			await asyncio.sleep(3)
			await asyncio.gather(Led1.Apagar_Async())
	except KeyboardInterrupt:
		elapsed = time.perf_counter() - s
		print(f"{__file__} executed in {elapsed:0.2f} seconds.")


async def main():
	await asyncio.gather(runPantalla(), runLed())

if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
"""


"""
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
"""