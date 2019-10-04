import pohBuzzer
from time import sleep
import logging
import asyncio

logging.basicConfig(level=logging.DEBUG)
bocina1 = pohBuzzer.Zumi2c()
loop = asyncio.get_event_loop()
loop.run_until_complete(bocina1.Test_Async())

"""
bocina1 = pohBuzzer.Zumi2c()
print(bocina1.address)
print(bocina1.buss)
bocina1.Encender()
sleep(2)
bocina1.Apagar()
sleep(1)
bocina1.Test()
"""