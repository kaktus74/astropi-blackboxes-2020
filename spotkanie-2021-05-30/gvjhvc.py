from datetime import datetime
import csv
import time
from datetime import datetime
#IN:
#2021 04 17  0000   59321       0    0     4.9    -8.0    -5.8    11.1   -31.8   301.3

#OUT:
#2021/04/17 22:47:00,-0.4847688674926758,-9.58865737915039,50.05764389038086,13.747065049470038
#...


with open("20210416_ace_mag_1m.txt", 'r') as txt:
    with open("20210416_ace_mag_1mv2.csv", 'w') as f:
        writer = csv.writer(f, delimiter=';',quoting=csv.QUOTE_ALL)
        data = list(txt.readlines())[20:101]
        for current_line in data:
            year = int(current_line[0:4])
            month = int(current_line[5:7])
            day = int(current_line[8:10])
            hour = int(current_line[12:14])
            minute = int(current_line[14:16])
            bx = float(current_line[41:45])
            by = float(current_line[50:54])
            bz = float(current_line[59:63])
            bt = float(current_line[66:69])
            #print(bx, by, bz, bt)
            #print(f'{year}/{month}/{day}')
            #print('%d/{month}/{day}')
            formated_time = datetime(year,month,day,hour,minute,0).strftime('%Y/%m/%d %H:%M:%S')
            writer.writerow((formated_time, bx, by, bz, bt))
            
        #print (data)
        
