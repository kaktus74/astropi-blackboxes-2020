from picamera import PiCamera
import os
from datetime import datetime, timezone
import dateutil.tz as tz
import os.path
#TODO: Make "photos" directory (os.mkdirs())
##TODO#2: Timezone as parameter :> |/
#TODO#3: camera=PiCamera() in main |/
#TODO#4: Erase colons |/


def take_photo (gpslat, gpslatref, gpslon, gpslonref, n, tz):
    now = datetime.now(tz)
    camera = PiCamera()
    with camera:
        camera.resolution = (1296, 972)
        camera.exif_tags['GPS.GPSLatitude'] = gpslat
        camera.exif_tags['GPS.GPSLatitudeRef'] = gpslatref
        camera.exif_tags['GPS.GPSLongitude'] = gpslon
        camera.exif_tags['GPS.GPSLongitudeRef'] = gpslonref       
        if os.path.exists(os.path.dirname (__file__)+'/Photos') == False:
            os.mkdir(os.path.dirname (__file__) + '/Photos')           
        camera.capture(os.path.dirname(__file__) + '/Photos/{0:04}_{1}.jpg'.format(n, now.strftime('%Y_%m_%d_%H_%M')))

if __name__ == '__main__':
    i = 0
    while i < 10:
        take_photo('53/1,27/1,123/10', 'N', '42/1,12/1,123/10', 'E', i, timezone.utc)
        i+=1
