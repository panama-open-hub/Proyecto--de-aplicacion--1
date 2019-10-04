# countasync.py
import asyncio
import time
import pohLcd as pantalla
import pohLed as luz

async def count():
    Led1 = luz.Luz(26)
    Led1.Encender()
    await asyncio.sleep(2)
    Led1.Encender()
    await asyncio.sleep(3)
    Led1.Apagar()
    await asyncio.sleep(2)
    #Led1.Parpadeo()
    await asyncio.sleep(1)
    print("TAREA DEL LED COMPLETADA")
    
async def count2():
    display = pantalla.Pantalla()
    display.Bienvenida()
    await asyncio.sleep(2)
    display.FechaHora()
    display.Limpiar()
    await asyncio.sleep(1)
    print("TAREA DE LA PANTALLA COMPLETADA")


async def main():
    await asyncio.gather(count(), count2())

if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
