from picamera import PiCamera
from time import sleep
import os
from datetime import datetime
import dateutil.tz as tz

oko = PiCamera()

with oko:
    oko.resolution = (1296,972)
    oko.exif_tags['GPS.GPSLatitude'] = "53/1,22/1,314/10"
    oko.exif_tags['GPS.GPSLatitudeRef'] = "N"
    oko.exif_tags['GPS.GPSLongitude'] = "14/1,39/1,451/10"
    oko.exif_tags['GPS.GPSLongitudeRef'] = "E"
    oko.exif_tags['Copyright'] = "Copyright: BlackBoxes"
    oko.capture(os.path.dirname(__file__) + '/../data/dommm.jpg')
