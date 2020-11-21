import csv
import random

#TODO-4 Zamien zahardcodowaną ścieżkę na scieżkę ../data względem pliku źródłowego
csv_sciezka = '/home/kaktus74/astropi2021/astropi-blackboxes-2020/spotkanie-2020-11-21/data/random.csv'


#TODO-5 Dodaj do pliku CSV kolejną kolumnę: losowe_imie ktorej wartość będzie losowo wybierana spośród Waszych imion
with open(csv_sciezka, 'w') as plik:
    writer = csv.writer(plik)

    naglowek = ("lp", "losowa")

    writer.writerow(naglowek)
    for i in range(1,100):
        losowa = random.randint(0,100)
        wiersz = (i+1, losowa)
        writer.writerow(wiersz)

        
