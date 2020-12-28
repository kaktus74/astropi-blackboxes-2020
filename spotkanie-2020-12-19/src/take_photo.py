from picamera import PiCamera
from time import sleep
import time
from datetime import datetime, timedelta
import os
import dateutil.tz as tz

now = datetime.now()
goal = now + timedelta(0, 60)
with PiCamera() as cam:
    cam.resolution = (1296,972)
    cam.start_preview()
    sleep(5)
    i = 1
    while goal-now >= timedelta (0, 0):
        teraz = datetime.now (tz.gettz("UTC"))
        print(__file__)
        cam.capture(os.path.dirname(__file__) + '/../data/{0:04d}-{1}.jpg'.format(i, teraz.strftime('%H%M%S%f')))
        sleep (5)
        i += 1
        now = datetime.now()
    print ('We be done')
