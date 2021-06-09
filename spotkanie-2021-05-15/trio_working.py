from sense_hat import SenseHat
from time import sleep
from math import pi, sin
from matplotlib import pyplot as plt
import csv

def save_data_to_csv(writer, index, time, magneticfield_x, magneticfield_y, magneticfield_z, magneticfield_m):
    formatedtime = time.strftime('%Y/%m/%d %H:%M:%S.%f')
    row = (index, formatedtime, gpslat, gpslon, magneticfield_x, magneticfield_y, magneticfield_z, magneticfield_m)
    writer.writerow(row)
    sleep(0.3)


def measure_magnetic_field (sensehat):
    sensed = sensehat.get_compass_raw()
    x = sensed['x']
    y = sensed['y']
    z = sensed['z']
    m = pow((x*x + y*y + z*z), 1/3) 
    return (x, y, z, m)

def main ():
    with open (str(current_dir_path)+'/data01.csv', 'a') as file:
        writer = csv.writer(file, delimiter=';',quoting=csv.QUOTE_MINIMAL)
        write_headline_csv(writer)
        save_data_to_csv

