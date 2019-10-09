
import pohDht
import time 
import logging
import asyncio

"""
logging.basicConfig(level=logging.DEBUG)
sensor1 = pohDht.Dht22(5)
t,h= sensor1.LeerTempHum()
print(t)
print(h)
"""

async def main():
    logging.basicConfig(level=logging.DEBUG)
    sensor1 = pohDht.Dht22(5)
    task1 = asyncio.create_task(sensor1.LeerTempHum_Async())
    await task1
    result_of_task1 = task1.result()
    print(result_of_task1)

if __name__ == "__main__":
    asyncio.run(main())

"""
try:
    logging.basicConfig(level=logging.DEBUG)
	sensor1 = pohDht.Dht22(5)
	loop = asyncio.get_event_loop()
	t, h = loop.run_until_complete(sensor1.LeerTempHum_Async())
    print(t)
    print(h) 
except KeyboardInterrupt:
	pass
finally:
	loop.close()
	print("Closing Loop")
"""
"""
import os
import time
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 5 #number of gpio

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        print('Date,Time,Temperature,Humidity\r\n')
        if humidity is not None and temperature is not None:
            print('{0},{1},{2:0.1f}*C,{3:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity))
        else:
            print("Failed to retrieve data from humidity sensor")

        time.sleep(30)
except KeyboardInterrupt:
    pass
finally:
    print("Script finalizado")
"""