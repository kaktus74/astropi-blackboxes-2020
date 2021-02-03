import os
#print (os.path.dirname(__file__))
import os.path
#print (os.path.exists(os.path.dirname(__file__) + '/niiiicosc'))
from picamera import PiCamera
from datetime import datetime, timezone, timedelta
from time import sleep

##
##with PiCamera() as cam:
##    cam.capture (os.path.dirname(__file__) + '/random_photo.jpg')

try:
    int ("s")
except Exception as e:
    print (e)
x = datetime.now(timezone.utc)
sleep (3)
y = datetime.now(timezone.utc)
delta = y - x
print (delta.total_seconds())
