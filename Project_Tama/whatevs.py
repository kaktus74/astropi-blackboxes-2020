import os
#print (os.path.dirname(__file__))
import os.path
#print (os.path.exists(os.path.dirname(__file__) + '/niiiicosc'))
from picamera import PiCamera

##
##with PiCamera() as cam:
##    cam.capture (os.path.dirname(__file__) + '/random_photo.jpg')

try:
    int ("s")
except Exception as e:
    print (e)
