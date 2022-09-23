import time
import datetime
import os

while True:
    time_now = time.strftime("%H:%M:%S")
    print('\r{}'.format(time_now), end='')
    time.sleep(1)
   
os.system('clear')

