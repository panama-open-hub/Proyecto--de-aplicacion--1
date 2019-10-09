import os
import time
import logging
import asyncio
import Adafruit_DHT

class Dht22:
    def __init__(self,pin=5):
        self.pin = pin

    def LeerTempHum(self):
        try:
            DHT_SENSOR = Adafruit_DHT.DHT22
            DHT_PIN = self.pin
            humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
            if humidity is not None and temperature is not None:
                msg = '{0},{1},{2:0.1f}*C,{3:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity)
                logging.debug(msg)
                return temperature, humidity
        except:
            logging.error("Nulo. Fallo al intentar leer temperatura / humedad")

    async def LeerTempHum_Async(self):
        try:
            DHT_SENSOR = Adafruit_DHT.DHT22
            DHT_PIN = self.pin
            humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
            asyncio.sleep(1)
            if humidity is not None and temperature is not None:
                msg = '{0},{1},{2:0.1f}*C,{3:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity)
                print(msg)
                return temperature,humidity
        except:
            logging.error("Nulo. Fallo al intentar leer temperatura / humedad")

    