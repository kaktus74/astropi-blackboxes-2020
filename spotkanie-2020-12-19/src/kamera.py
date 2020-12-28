from picamera import PiCamera
from time import sleep
import os
from datetime import datetime
import dateutil.tz as tz

kamera = PiCamera()
kamera.resolution = (1296,972)
timezone = tz.tzutc()
start = datetime.now(timezone)
i = 1
with kamera:
    for i in range(1,13):
        print ('i: ', i)
        now = datetime.now(timezone)
        kamera.capture(os.path.dirname(__file__) + "/../data/{1:04}-{0}.jpg".format(now.strftime('%Y-%m-%d-%H-%M-%S-%f'),i))
        sleep(5)
#pythom symtax error
#with picamera.PiCamera() as camera:
