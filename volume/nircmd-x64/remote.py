import os
import time

for x in range (20) :
    os.system('nircmd.exe changesysvolume -5000')
    time.sleep(1.5)
