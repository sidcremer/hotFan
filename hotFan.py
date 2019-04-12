import sys, os, unittest
sys.path.append('/home/pi/hotFan/hs100/hs100')

from core import Core
from optparse import OptionParser

import time
import grovepi

global args

sensor = 0

while True:
    try:
        temp = grovepi.temp(sensor,'1.2')
        print("temp =", temp)
        time.sleep(.20)
	
	if temp > 25:
		Core("10.0.1.18", 9999, "False").request("on")

	if temp <= 25:
		Core("10.0.1.18", 9999, "False").request("off")

    except KeyboardInterrupt:
        break
    except IOError:
        print ("Error")
