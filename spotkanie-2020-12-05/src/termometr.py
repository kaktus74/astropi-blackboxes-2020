from sense_hat import SenseHat
from time import sleep
import os
import csv
import time
from datetime import datetime
import dateutil.tz as tz

#TODO-6: Zapisz zmierzone dane w pliku csv w w ukladzie:
# kolumny: nr_pomiaru , temperatura ( z dokładnością do 4 miejsc po przecinku)
# sciezka docelowa: <plik_zrodlowy>/../data/temperatures.csv
# katalog data powinien bys stworzony recznie przed uruchomieniem
# skrypt bedzie uruchamiany z folderu domowego 

def zrob_pomiar(sense):
    
    csv_sciezka = os.path.dirname(__file__) + "/../data/temperatura.csv"

    os.makedirs(os.path.dirname(os.path.realpath(csv_sciezka)), exist_ok=True)

    with open(csv_sciezka, 'w') as plik:
        pioro = csv.writer(plik,delimiter=';',quoting=csv.QUOTE_MINIMAL)

        tytuly = ("indeks","czas","czas_dzialania","temperatura")
        pioro.writerow(tytuly)
        tz_polska = tz.gettz('Europe/Warsaw')
        poczatek = datetime.now(tz_polska)
        
        for i in range(1, 91):
            #todo: licz czas dzialania (w sekundach!) odejmujac aktualny czas od czasu gdy wystartowal program
            teraz = datetime.now(tz_polska)
            czas_dzialania = (teraz - poczatek).total_seconds()
            #(time.localtime.tm_hour(),time.localtime.tm_min(),time.localtime.tm_sec())
            temp = sense.temperature
            print(temp)
            sleep(0.25)
            #TODO: format czasu: dd/mm/rrrr hh:mm:ss.m_s
            #TODO: format czasu: 01/09/1939 04:16:59.6666
            #                    2020-12-05 12:43:22.062938+01:00
            wiersz = (i, teraz.strftime('%d/%m/%Y %H:%M:%S.%f'), '{0:.4f}'.format(czas_dzialania), "{0:.4f}".format(temp))
            pioro.writerow(wiersz)

        
#import fakesensehat as fs

if __name__ == '__main__':
    sense = SenseHat()
    zrob_pomiar(sense)
