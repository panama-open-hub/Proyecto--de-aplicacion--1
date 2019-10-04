# countasync.py
import asyncio
#import modules.pohLcd
#import modules.pohLed


"""async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")
"""

async def Encender_Async(self):
        led = LED(self.pin)
        led.on()
        print ("LED ON")
        await asyncio.sleep(1)

 async def Parpadeo_Async(self):
        led = LED(self.pin)
            timeout = 10   # [seconds]
            timeout_start = time.time()
            test = 0
            print(datetime.now(),"Contando")
            while time.time() < timeout_start + timeout:
                if test == 10:
                    print ("Working")
                     break
                test = test + 1
            #led.on()
        await asyncio.sleep(2)
          print(datetime.now(),"Still Working")
        #led.off()

async def main():
    await asyncio.gather(Encender_Async(), Parpadeo_Async())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
