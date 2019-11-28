import time
from datetime import datetime
from time import sleep

t_end = time.time() + 60 * 0.25
while time.time() < t_end:
    print(datetime.now())
    sleep(1)
    