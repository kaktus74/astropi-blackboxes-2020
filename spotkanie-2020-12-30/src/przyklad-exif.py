from picamera import PiCamera
from time import sleep
import os
from datetime import datetime
import dateutil.tz as tz

camera = PiCamera()


with camera:
    camera.resolution = (1296,972)
    camera.exif_tags['GPS.GPSLatitude'] = "53/1,25/1,280/10"
    camera.exif_tags['GPS.GPSLatitudeRef'] = "N"
    camera.exif_tags['GPS.GPSLongitude'] = "14/1,28/1,566/10"
    camera.exif_tags['GPS.GPSLongitudeRef'] = "E"
    #camera.exif_tags['bez sensu'] = "ddasdas"
    camera.capture(os.path.dirname(__file__) + "/../data/exif.jpg")
# 53.424449, 14.482395 = 53°25'28.0"N 14°28'56.6"E

