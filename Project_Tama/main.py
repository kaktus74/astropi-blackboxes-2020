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
# Imports
TIME_OVER_FOV = 23.43

def compute_position ():
    """When given an object computed using TLE lines, this function will compute the object's position"""
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


def take_and_save_photo_with_exifs (gpslat, gpslatref, gpslon, gpslonref, ordinal, timezone, camera, directory_path):
    """This function takes photos and saves the gps position of the place the were taken at as their exif, as well as the ordinal number of the loop's turn they were taken
        Keyword arguments:
        gpslat         -- the latitude angle of ISS at the moment of taking the photo 
        gpslatref      -- the latitude reference (North/South) of ISS at the moment of taking the photo
        gpslon         -- the longitude angle of ISS at the moment of taking the photo 
        hgpislonref    -- the longitude reference (North/South) of ISS at the moment of taking the photo
        ordinal        -- the number of current loop's turn
        timezone       -- the UTC timezone object
        camera         -- SenseHat's camera object
        directory_path -- the path of the directory the photos are saved in
        """
    now = datetime.now(timezone)
    camera.resolution = (1920, 1080)
    logger.debug (f"I'm saving as exif: GPS latitude ({gpslat}), GPS latitude reference ({gpslatref}), GPS longitude ({gpslon}), GPS longitude reference ({gpslonref})")
    camera.exif_tags['GPS.GPSLatitude'] = gpslat
    camera.exif_tags['GPS.GPSLatitudeRef'] = gpslatref
    camera.exif_tags['GPS.GPSLongitude'] = gpslon
    camera.exif_tags['GPS.GPSLongitudeRef'] = gpslonref
    camera.exif_tags['IFD0.ImageDescription'] = "Copyrights: Black Boxes; Pac, pac"
    logger.info ("I am taking the photo")
    try:
        camera.capture(directory_path + '/{0:04}_{1}.jpg'.format(ordinal, now.strftime('%Y_%m_%d_%H_%M')))
    except Exception as e:
        logger.error (f'An error "{e}" occured. Photo could not have been saved')

def measure_magnetic_field (sensehat):
    """
    This function measures the magnetic field, using SenseHat, and computes the average vector of magnetic field's x, y, z vectors
    Keyword arguments:
    SenseHat -- SenseHat's object used for making measurements
"""
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
    """This function writes a headline for the csv file
        Keyword arguments:
        writer -- the file's writer
    """
    try:
        headline = ('index', 'time', 'lat', 'lon', 'x', 'y', 'z', 'm')
        writer.writerow(headline)
    except Exception as e:
        logger.error (f'An error "{e}" occured. Headline could not have been saved')

def save_data_to_csv(writer, index, gpslat, gpslon, time, magneticfield_x, magneticfield_y, magneticfield_z, magneticfield_m):
    """This function is saving data given in arguments to a csv file
        writer -- the file's writer
        index  -- the ordinal number of the current loop turn
        gpslat -- current latitude of ISS
        gpslon -- current longitude of ISS
        time   -- current time
        magneticfield_x -- the value of vector in x direction
        magneticfield_y -- the value of vector in y direction
        magneticfield_z -- the value of vector in z direction
        magneticfield_m -- the avarge value of the vectors
        """
    logger.info("I'm saving to csv.")
    try:
        formatedtime = time.strftime('%Y/%m/%d %H:%M:%S.%f')
        row = (index, formatedtime, gpslat, gpslon, magneticfield_x, magneticfield_y, magneticfield_z, magneticfield_m)
        writer.writerow(row)
    except Exception as e:
        logger.error (f'An error "{e}" occured. Data could not have been saved')
    sleep(0.005)

##def compute_average (avg_sum, avg_factor, start_time):
##    now = datetime.now(timezone.utc)
##    time_between_start_and_now = (now - start_time).total_seconds()
##    avg_sum = avg_sum + time_between_start_and_now
##    return [round (avg_sum/avg_factor, 5), avg_sum]

def compute_maximum_loop_duration (start_time, previous_max_loop_duration):
    """This function is computing maximum duration of loop
        Keyword argument:
        start_time -- the starting time of current turn
        previous_max_loop_duration -- the maximum duration of all previous turns
        """
    current_duration = datetime.now(timezone.utc) - start_time
    return max (current_duration.total_seconds(), previous_max_loop_duration)



def if_test():
    """The function checking if the call is final or testing, based on the programme arguments"""
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            return True
    else:
        return False

def compute_duration_time(if_test, start):
    """This function computes the duration time of the main loop, depending on if the call is final or testing.
        Keyword arguments:
        if_test -- a True/False value indicating if the call is final or testing
        start   -- the starting time of the loop
        """
    if if_test == True:
        return start + timedelta(seconds = 250)
    else:
        return start + timedelta(seconds = 10800)

def main(camera, time_between_photos=TIME_OVER_FOV):
    """The main fuction containing the loop which makes measurements
        Keyword arguments:
        camera -- SenseHat's camera object
        time_between_photos -- previously computed constant, which indicates the time between taking photos; computed using Thales' theorem
        """
    start = datetime.now(timezone.utc)
    expected_finishing_time = compute_duration_time(if_test(), start)
    avg_sum = 0.0
    avg = 0
    safety_buffer_sec = 180
    maximum_loop_duration = 0
    logfile(os.path.dirname (os.path.realpath(__file__))+'/logs.log')
    time_between_magnetic_field_measurements = time_between_photos/3
    logger.info (f"I have computed the time between making magnetic field measurements, it is: {time_between_magnetic_field_measurements}")
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
        while expected_finishing_time - timedelta(seconds = safety_buffer_sec + maximum_loop_duration) > datetime.now(timezone.utc):
            logger.info (f"I'm starting the loop number {i}")
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
            file.flush()
            if i%3 == 0:
                logger.info ("It is time to take the photo")
                formatted_position_lat = format_position (position_lat, ['N', 'S'])
                formatted_position_lon = format_position (position_lon, ['E', 'W'])
                logger.info ("I have formatted the position into the EXIF format")
                take_and_save_photo_with_exifs (formatted_position_lat[0], formatted_position_lat[1], formatted_position_lon[0], formatted_position_lon[1], i, timezone.utc, camera, photos_path) 
                logger.info ("I have taken the photo")
            logger.info ("I'm going to sleep for 3 seconds now")
            sleep(time_between_magnetic_field_measurements)
            maximum_loop_duration = compute_maximum_loop_duration (start_time, maximum_loop_duration)
            i+=1



if __name__ == '__main__':
    logfile(os.path.dirname (os.path.realpath(__file__))+'/logs.log')
    logger.info ('''We are staring our experiment. We will be saving magnetic field measurements and photos to analyse
them and search for connections between magnetic field and many factors, such as terrain. The
experiment is run by the team Black Boxes.''')
    logger.info (' ____  _            _      ____')
    logger.info ('| __ )| | __ _  ___| | __ | __ )  _____  _____  ___')
    logger.info ('|  _ \| |/ _` |/ __| |/ / |  _ \ / _ \ \/ / _ \/ __|')
    logger.info ('| |_) | | (_| | (__|   <  | |_) | (_) >  <  __/\__ \\')
    logger.info ('|____/|_|\__,_|\___|_|\_\ |____/ \___/_/\_\___||___/')
#############################################################################
    name = 'ISS (ZARYA)'
    line1 = '1 25544U 98067A   21044.24238633  .00000914  00000-0  24782-4 0  9993'
    line2 = '2 25544  51.6437 235.7688 0002867   6.5121 158.4468 15.48962733269387'

    iss = readtle(name, line1, line2)
#############################################################################
    sense = SenseHat()
    with PiCamera() as camera:
        main(camera)
