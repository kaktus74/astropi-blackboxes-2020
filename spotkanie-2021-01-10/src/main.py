from sense_hat import SenseHat
from time import sleep
from datetime import datetime, timezone


name = 'ISS (ZARYA)'
line1 = 1 25544U 98067A   21002.23397689  .00001223  00000-0  30093-4 0  9999
line2 = 2 25544  51.6472  83.5832 0001012 178.9624 282.3149 15.49248482262878

iss = readtle(name, line1, line2) 

def check_position ():
    iss.compute()
    sublat = str(iss.sublat)
    sublon = str(iss.sublon)
    return (sublat, sublon)

def tales ():
    return 6

def take_photo(exif_gpslat, exif_gpslon):
    sleep (3)
def measure_magnetic_field (sensehat):
    sleep (0.5)
    return (1, 2, 3, 4)

def save_to_csv(pos_lat, pos_lon, time, mf_x, mf_y, mf_z, mf_m):
    sleep(0.01)
    

x = tales()
i = 1
first_now = datetime.now()
# TO DO datetime.now() + timedelta(sec
expected = 3
while expected - datetime.now() > 0:
    position_lat = check_position()[0]
    position_lon = check_position()[1]
    now = datetime.now (timezone.utc)
    magnetic_field_x = measure_magnetic_field(sense)[0]
    magnetic_field_y = measure_magnetic_field(sense)[1]
    magnetic_field_z = measure_magnetic_field(sense)[2]
    magnetic_field_m = measure_magnetic_field(sense)[3]
    save_to_csv (position_lat, position_lon, now, magnetic_field_x, magnetic_field_y, magnetic_field_z, magnetic_field_m)  
    if i%3 == 0:
        take_photo(position_lat, position_lon) 
    sleep(x/3)
    i+=1
