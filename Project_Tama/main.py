from sense_hat import SenseHat
from time import sleep
from datetime import datetime, timezone, timedelta
from ephem import readtle
import sys
import os
from picamera import PiCamera
import dateutil.tz as tz
from logzero import logger, logfile, loglevel
logfile(os.path.dirname (os.path.realpath(__file__))+'/logs.log')
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

def format_position(value, lon_or_lat):
    value = value.split(':')
    if int(value[0]) >= 0:
        direction_ref = lon_or_lat [0]
    else:
        direction_ref = lon_or_lat[1]
    value_formatted = value[0]+'/1,'+value[1]+'/1,'+''.join(value[2].split('.'))+'/10'
    return [value_formatted, direction_ref]


def time_over_fov ():
    overlap_factor = 1
    time = overlap_factor * 23.43
    return time

def take_photo (gpslat, gpslatref, gpslon, gpslonref, n, tz, cam, dirpath):
    now = datetime.now(tz)
    cam.resolution = (1296, 972)
    cam.exif_tags['GPS.GPSLatitude'] = gpslat
    cam.exif_tags['GPS.GPSLatitudeRef'] = gpslatref
    cam.exif_tags['GPS.GPSLongitude'] = gpslon
    cam.exif_tags['GPS.GPSLongitudeRef'] = gpslonref
    logger.info ("I am taking the photo")
    try:
        cam.capture(dirpath + '/{0:04}_{1}.jpg'.format(n, now.strftime('%Y_%m_%d_%H_%M')))
    except Exception as e:
        logger.error (f'An error "{e}" occured. Photo could not have been saved')

def measure_magnetic_field (sense):
    sleep (0.5)
    #tab.append (zczytane x, zczytane y, zczytane z)
    logger.info ("Computing the length of magnetic field's vector")
    #m = pierwiastek sześcienny z sumy sześcianów x y z
    
    return (1, 2, 3, 4)

def save_to_csv(pos_lat, pos_lon, time, mf_x, mf_y, mf_z, mf_m):
    logger.info("I'm saving to csv.")
    try:
        sleep (0.005)
    except Exception as e:
        logger.error (f'An error "{e}" occured. Data could not have been saved')
    sleep(0.005)



# TODO datetime.now() + timedelta(sec
start = datetime.now(timezone.utc)
if len(sys.argv) > 1:
    if sys.argv[1] == 'test':
        expected = start + timedelta(seconds = 30)
else:
    expected = start + timedelta(seconds = 10800) #10800 s = 3 h

def box(camera):
    logfile(os.path.dirname (os.path.realpath(__file__))+'/logs.log')
    x = time_over_fov()
    logger.info (f"I calculated the duration of the loop it is: {x}")
    i = 1
    photos_path = os.path.dirname (os.path.realpath(__file__))+'/Photos'
    if os.path.exists(photos_path) == False:
        logger.info ("The Photos folder doesn't exist, I'm going to create it")
        os.mkdir(photos_path)
        logger.info ("I have succesfully created the Photos folder")
    else:
        logger.info ("The Photos folder exists")
    while expected - timedelta(seconds = 10) > datetime.now(timezone.utc):    #TO DO ile czasu w zapasie?
        checked_position = check_position()
        logger.info ("I have checked the position")
        position_lat = checked_position[0]
        position_lon = checked_position[1]
        logger.info ("I have separated the latitude and longitude data") 
        now = datetime.now (timezone.utc)
        logger.info ("I have checked the current time at the Prime Meridian")
        measured_magnetic_field = measure_magnetic_field(sense)
        logger.info ("I have measured the magnetic field and calculated the length of the vector of the force")
        magnetic_field_x = measured_magnetic_field[0]
        magnetic_field_y = measured_magnetic_field[1]
        magnetic_field_z = measured_magnetic_field[2]
        magnetic_field_m = measured_magnetic_field[3]
        logger.info ("I have separately saved the x, y, z values and length of the vector from the magnetic field measurements")
        save_to_csv (position_lat, position_lon, now, magnetic_field_x, magnetic_field_y, magnetic_field_z, magnetic_field_m)  
        if i%3 == 0:
            logger.info ("It is time to take the photo")
            formatted_position_lat = format_position (position_lat, ['N', 'S'])
            formatted_position_lon = format_position (position_lon, ['E', 'W'])
            logger.info ("I have formatted the position into the EXIF format")
            take_photo(formatted_position_lat[0], formatted_position_lat[1], formatted_position_lon[0], formatted_position_lon[1], i, timezone.utc, camera, photos_path) 
            logger.info ("I have taken the photo")
        logger.info ("I'm going to sleep for 3 seconds now")
        sleep(x/3)
        i+=1

if __name__ == '__main__':
    with PiCamera() as camera:
        box(camera)
