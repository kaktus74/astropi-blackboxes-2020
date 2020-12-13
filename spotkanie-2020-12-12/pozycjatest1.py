from ephem import readtle, degree
import time
import os
import csv
from datetime import datetime
from time import sleep
from dateutil.tz import tz


imie = "ISS zayra"
p1 = "1 25544U 98067A   20347.38065972  .00001339  00000-0  32251-4 0  9999"
p2 = "2 25544  51.6440 186.7650 0001859 122.9504 239.1247 15.49179161259649"

iss = readtle(imie,p1,p2)



def zapisuj():
    
    csv_sciezka = os.path.dirname(__file__) + "/data/pozycjatest1.csv"

    with open(csv_sciezka, 'w') as plik:
        pioro = csv.writer(plik,delimiter=';',quoting=csv.QUOTE_MINIMAL)

        tytuly = ("indeks","czas","sublat","sublong")
        pioro.writerow(tytuly)
        
        for i in range(1,11):
            iss.compute()
            czas = datetime.now(tz.tzutc())
            sleep(1)
            wiersz = (i, czas.strftime('%Y/%m/%d %H:%M:%S.%f'), iss.sublat / degree, iss.sublong / degree)
            pioro.writerow(wiersz)

zapisuj()
