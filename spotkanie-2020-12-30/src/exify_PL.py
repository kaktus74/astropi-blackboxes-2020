from picamera import PiCamera
import os

cam = PiCamera()

with cam:
    cam.resolution = (1296, 972)
    cam.exif_tags['GPS.GPSLatitude'] = '53/1,26/1,261/10'
    cam.exif_tags['GPS.GPSLatitudeRef'] = 'N'
    cam.exif_tags['GPS.GPSLongitude'] = '14/1,29/1,337/10'
    cam.exif_tags['GPS.GPSLongitudeRef'] = 'E'
    cam.capture(os.path.dirname(__file__) + '/../data/nasz_exif.jpg')
