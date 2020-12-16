from sense_hat import SenseHat
sh = SenseHat()
import os
import csv
from time import sleep
from datetime import datetime
import dateutil.tz as tz

def sense (sensehat):
    path = os.path.dirname(__file__) + '/../data/magnetometr.csv'
    os.makedirs(os.path.dirname(os.path.realpath(path)), exist_ok = True)
    with open (path, 'w') as file:
        writer = csv.writer(file, delimiter=';',quoting=csv.QUOTE_MINIMAL)
        headline = ('index', 'time', 'x', 'y', 'z', 'm')
        writer.writerow(headline)
        timezone = tz.tzutc()
        for i in range(1, 51):
            now = datetime.now(timezone)
            sensed = sensehat.get_compass_raw()
            x = sensed['x']
            print ('x: ', x)
            y = sensed['y']
            print ('y: ', y)
            z = sensed['z']
            print ('z: ', z)
            m = pow((x*x + y*y + z*z), 1/3)
            print('m: ', m)
            row = (i, now.strftime('%Y/%m/%d %H:%M:%S.%f'), x, y, z, m)
            writer.writerow(row)
            sleep(0.5)

if __name__ == '__main__':
    sense (sh)
        
