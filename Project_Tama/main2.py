from sense_hat import SenseHat
from time import sleep
from datetime import datetime, timezone, timedelta
from ephem import readtle
import sys
import os
from picamera import PiCamera
import dateutil.tz as tz
from logzero import logger, logfile, loglevel
import csv
logfile(os.path.dirname (os.path.realpath(__file__))+'/logs.log')
sense = SenseHat()
#############################################################################
name = 'ISS (ZARYA)'
line1 = '1 25544U 98067A   21002.23397689  .00001223  00000-0  30093-4 0  9999'
line2 = '2 25544  51.6472  83.5832 0001012 178.9624 282.3149 15.49248482262878'

iss = readtle(name, line1, line2)
#############################################################################

def compute_position ():
    iss.compute()
    sublat = str(iss.sublat)
    sublon = str(iss.sublong)
    return (sublat, sublon)

def format_position(angle, lon_or_lat):
    angle = angle.split(':')
    if int(angle[0]) >= 0:
        angle_ref = lon_or_lat [0]
    else:
        angle_ref = lon_or_lat[1]
    angle_formatted = angle[0]+'/1,'+angle[1]+'/1,'+''.join(angle[2].split('.'))+'/10'
    return [angle_formatted, angle_ref]


def time_over_fov ():
    overlap_factor = 1
    time = overlap_factor * 23.43
    return time

def take_and_save_photo_with_exifs (gpslat, gpslatref, gpslon, gpslonref, ordinal, timezone, camera, directory_path):
    now = datetime.now(timezone)
    camera.resolution = (1296, 972)
    camera.exif_tags['GPS.GPSLatitude'] = gpslat
    camera.exif_tags['GPS.GPSLatitudeRef'] = gpslatref
    camera.exif_tags['GPS.GPSLongitude'] = gpslon
    camera.exif_tags['GPS.GPSLongitudeRef'] = gpslonref
    logger.info ("I am taking the photo")
    try:
        camera.capture(directory_path + '/{0:04}_{1}.jpg'.format(ordinal, now.strftime('%Y_%m_%d_%H_%M')))
    except Exception as e:
        logger.error (f'An error "{e}" occured. Photo could not have been saved')

def measure_magnetic_field (sensehat):
    sensed = sensehat.get_compass_raw()
    x = sensed['x']
    y = sensed['y']
    z = sensed['z']
    m = pow((x*x + y*y + z*z), 1/3)
    #tab.append (zczytane x, zczytane y, zczytane z)
    logger.info ("Computing the length of magnetic field's vector")
    #m = pierwiastek sześcienny z sumy sześcianów x y z
    
    return (x, y, z, m)

def write_headline_csv(writer):
    try:
        headline = ('index', 'time', 'lat', 'lon', 'x', 'y', 'z', 'm')
        writer.writerow(headline)
    except Exception as e:
        logger.error (f'An error "{e}" occured. Headline could not have been saved')

def save_data_to_csv(writer, index, gpslat, gpslon, time, magneticfield_x, magneticfield_y, magneticfield_z, magneticfield_m):
    logger.info("I'm saving to csv.")
    try:
        formatedtime = time.strftime('%Y/%m/%d %H:%M:%S.%f')
        row = (index, formatedtime, gpslat, gpslon, magneticfield_x, magneticfield_y, magneticfield_z, magneticfield_m)
        writer.writerow(row)
    except Exception as e:
        logger.error (f'An error "{e}" occured. Data could not have been saved')
    sleep(0.005)

def compute_average (avg_sum, avg_factor, start_time):
    now = datetime.now(timezone.utc)
    time_between_start_and_now = (now - start_time).total_seconds()
    print (time_between_start_and_now)
    avg_sum = avg_sum + time_between_start_and_now
    return [round (avg_sum/avg_factor, 5), avg_sum]



# TODO datetime.now() + timedelta(sec
start = datetime.now(timezone.utc)
if len(sys.argv) > 1:
    if sys.argv[1] == 'test':
        expected_finishing_time = start + timedelta(seconds = 30)
else:
    expected_finishing_time = start + timedelta(seconds = 10800) #10800 s = 3 h

def box(camera):
    avg_sum = 0.0
    avg = 0
    logfile(os.path.dirname (os.path.realpath(__file__))+'/logs.log')
    x = time_over_fov()
    logger.info (f"I have computed the time between taking photos, it is: {x}")
    i = 1
    photos_path = os.path.dirname (os.path.realpath(__file__))+'/Photos'
    if os.path.exists(photos_path) == False:
        logger.info ("The Photos folder doesn't exist, I'm going to create it")
        os.mkdir(photos_path)
        logger.info ("I have succesfully created the Photos folder")
    else:
        logger.info ("The Photos folder exists")
    with open (os.path.dirname(os.path.realpath(__file__))+'/data.csv', 'a') as file:
        writer = csv.writer(file, delimiter=';',quoting=csv.QUOTE_MINIMAL)
        write_headline_csv(writer)
        while expected_finishing_time - timedelta(seconds = avg) > datetime.now(timezone.utc): 
            start_time = datetime.now(timezone.utc)
            computed_position = compute_position()
            logger.info ("I have computed the position")
            position_lat = computed_position[0]
            position_lon = computed_position[1]
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
            save_data_to_csv (writer, i, position_lat, position_lon, now, magnetic_field_x, magnetic_field_y, magnetic_field_z, magnetic_field_m)
            if i%3 == 0:
                logger.info ("It is time to take the photo")
                formatted_position_lat = format_position (position_lat, ['N', 'S'])
                formatted_position_lon = format_position (position_lon, ['E', 'W'])
                logger.info ("I have formatted the position into the EXIF format")
                take_and_save_photo_with_exifs (formatted_position_lat[0], formatted_position_lat[1], formatted_position_lon[0], formatted_position_lon[1], i, timezone.utc, camera, photos_path) 
                logger.info ("I have taken the photo")
            logger.info ("I'm going to sleep for 3 seconds now")
            sleep(x/3)
            if i%3:
                avg_and_sum = compute_average (avg_sum, i, start_time)
                avg = avg_and_sum[0]
                avg_sum = avg_and_sum[1]
                logger.info (f"I have computed the average when I take the photo, it's {avg}")
            else:
                avg_and_sum = compute_average (avg_sum, i, start_time)
                avg = avg_and_sum[0]
                avg_sum = avg_and_sum[1]
                logger.info (f"I have computed the average when I didn't take the photo, it's {avg}")
            i+=1

if __name__ == '__main__':
    with PiCamera() as camera:
        box(camera)
