from sense_hat import SenseHat
from time import sleep
from datetime import datetime, timezone, timedelta
from ephem import readtle
import sys
import os
from picamera import PiCamera
import dateutil.tz as tz
sense = SenseHat()
#############################################################################
name = 'ISS (ZARYA)'
line1 = '1 25544U 98067A   21002.23397689  .00001223  00000-0  30093-4 0  9999'
line2 = '2 25544  51.6472  83.5832 0001012 178.9624 282.3149 15.49248482262878'

iss = readtle(name, line1, line2)
#############################################################################

def check_position ():
    iss.compute()
    sublat = str(iss.sublat)
    sublon = str(iss.sublong)
    return (sublat, sublon)

def format_position(lat, lon):
    return ['lat', 'latref', 'lon', 'lonref']

def tales ():
    return 6

def take_photo (gpslat, gpslatref, gpslon, gpslonref, n, tz, cam, dirpath):
    now = datetime.now(tz)
    cam.resolution = (1296, 972)
    cam.exif_tags['GPS.GPSLatitude'] = gpslat
    cam.exif_tags['GPS.GPSLatitudeRef'] = gpslatref
    cam.exif_tags['GPS.GPSLongitude'] = gpslon
    cam.exif_tags['GPS.GPSLongitudeRef'] = gpslonref                  
    cam.capture(dirpath + '/{0:04}_{1}.jpg'.format(n, now.strftime('%Y_%m_%d_%H_%M')))

def measure_magnetic_field (sense):
    sleep (0.5)
    return (1, 2, 3, 4)

def save_to_csv(pos_lat, pos_lon, time, mf_x, mf_y, mf_z, mf_m):
    sleep(0.01)
    


# TODO datetime.now() + timedelta(sec
start = datetime.now(timezone.utc)
if len(sys.argv) > 1:
    if sys.argv[1] == 'test':
        expected = start + timedelta(seconds = 30)
else:
    expected = start + timedelta(seconds = 10800) #10800 s = 3 h
#TODO uruchamanie programu w trybie testowym
def box(camera):
    x = tales()
    i = 1
    print ('file: ', __file__)
    photos_path = os.path.dirname (os.path.realpath(__file__))+'/Photos'
    print (photos_path)
    print ('does it exist: ', os.path.exists(photos_path))
    if os.path.exists(photos_path) == False:            
        os.mkdir(photos_path)
    while expected - timedelta(seconds = 10) > datetime.now(timezone.utc):    #TO DO ile czasu w zapasie?
        checked_position = check_position()
        position_lat = checked_position[0]
        position_lon = checked_position[1]
        now = datetime.now (timezone.utc)
        measured_magnetic_field = measure_magnetic_field(sense)
        magnetic_field_x = measured_magnetic_field[0]
        magnetic_field_y = measured_magnetic_field[1]
        magnetic_field_z = measured_magnetic_field[2]
        magnetic_field_m = measured_magnetic_field[3]
        save_to_csv (position_lat, position_lon, now, magnetic_field_x, magnetic_field_y, magnetic_field_z, magnetic_field_m)  
        if i%3 == 0:
            formatted_position = format_position (position_lat, position_lon)
            take_photo(formatted_position[0], formatted_position[1], formatted_position[2], formatted_position[3], i, timezone.utc, camera, photos_path) 
        sleep(x/3)
        i+=1

if __name__ == '__main__':
    with PiCamera() as camera:
        box(camera)
