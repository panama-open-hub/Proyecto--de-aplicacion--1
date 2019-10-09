# countasync.py
import asyncio
import time
import logging
import pohLcd 
import pohLed 
import pohBuzzer
import pohRtc
import pohDht

logging.basicConfig(level=logging.DEBUG)
led1 = pohLed.Luz(26)
bocina1 = pohBuzzer.Zumi2c()
pantalla1 = pohLcd.Pantalla()
sensor1 = pohDht.Dht22(5)



async def main():
    tareaLed = asyncio.create_task(led1.Parpadeo_Async(-1))
    tareaBocina = asyncio.create_task(bocina1.Test_Async())
    tareaSensor = asyncio.create_task(sensor1.LeerTempHum_Async())
    #tareaPantalla = asyncio.create_task(pantalla1.EscribirFechaHoraLoop_Async(True))
    #tareaPantalla = asyncio.create_task(pantalla1.EscribirHoraLoop_Async())
    await tareaLed
    await tareaBocina
    await tareaSensor
    asyncio.sleep(1)
    #await tareaPantalla

if __name__ == "__main__":
    try:
        s = time.perf_counter()
        asyncio.run(main())
        elapsed = time.perf_counter() - s
        print(f"{__file__} executed in {elapsed:0.2f} seconds.")
    except KeyboardInterrupt:
        pass
    finally:
        pantalla1.Apagar()
        print("Ciclo de tareas asincronas cerrado")
    

