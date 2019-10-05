import pohLed
import time 
import logging
import asyncio

try:
	logging.basicConfig(level=logging.DEBUG)
	led1 = pohLed.Luz(26)
	loop = asyncio.get_event_loop()
	loop.run_until_complete(led1.Parpadeo_Async(7,1))
except KeyboardInterrupt:
	pass
finally:
	loop.close()
	print("Closing Loop")

"""
Led1 = pohLed.Luz(26)
Led1.Encender_Async()
Led1.Parpadeo_Async()
"""







