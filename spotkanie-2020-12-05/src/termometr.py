#from sense_hat import SenseHat
from time import sleep
import os
import csv
import time
from datetime import datetime

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
        
        for i in range(1,41):
            czas_dzialania = i*0.23
            czas = datetime.now()
            #(time.localtime.tm_hour(),time.localtime.tm_min(),time.localtime.tm_sec())
            temp = sense.temperature
            sleep(0.25)
            wiersz = (i, czas.isoformat(), czas_dzialania, "{0:.4f}".format(temp))
            pioro.writerow(wiersz)

        
import fakesensehat as fs

if __name__ == '__main__':
    sense = fs.SenseHatFake(22)
    zrob_pomiar(sense)
