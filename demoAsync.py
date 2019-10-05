# countasync.py
import asyncio
import time
import pohLcd 
import pohLed 
import pohBuzzer

led1 = pohLed.Luz(26)
bocina1 = pohBuzzer.Zumi2c()
pantalla1 = pohLcd.Pantalla()


async def main():
    tareaLed = asyncio.create_task(led1.Parpadeo_Async(-1))
    tareaBocina = asyncio.create_task(bocina1.Test_Async())
    tareaPantalla = asyncio.create_task(pantalla1.MostrarFechaHora_async(True))
    await tareaLed
    await tareaBocina
    await tareaPantalla

if __name__ == "__main__":
    try:
        s = time.perf_counter()
        asyncio.run(main())
        elapsed = time.perf_counter() - s
        print(f"{__file__} executed in {elapsed:0.2f} seconds.")
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing Loop")
    

