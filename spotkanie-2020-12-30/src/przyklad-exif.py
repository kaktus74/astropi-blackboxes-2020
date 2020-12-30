from picamera import PiCamera
from time import sleep
import os
from datetime import datetime
import dateutil.tz as tz

camera = PiCamera()


with camera:
    camera.resolution = (1296,972)
    camera.exif_tags['GPS.GPSLatitude'] = "44/1,45/1,123/10"
    camera.exif_tags['GPS.GPSLatitudeRef'] = "N"
    camera.exif_tags['GPS.GPSLongitude'] = "15/1,0/1,0/10"
    camera.exif_tags['GPS.GPSLongitudeRef'] = "E"
    camera.capture(os.path.dirname(__file__) + "/../data/exif.jpg")

