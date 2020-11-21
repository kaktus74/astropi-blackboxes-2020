import csv
import random

#TODO-4 Zamien zahardcodowaną ścieżkę na scieżkę ../data względem pliku źródłowego
csv_sciezka = '/home/kaktus74/astropi2021/astropi-blackboxes-2020/spotkanie-2020-11-21/data/random.csv'


#TODO-5 Dodaj do pliku CSV kolejną kolumnę: losowe_imie ktorej wartość będzie losowo wybierana spośród Waszych imion
with open(csv_sciezka, 'w') as plik:
    #FIXME: użyj znaków cytujących. Patrz: https://docs.python.org/3/library/csv.html
    writer = csv.writer(plik)

    naglowek = ("lp", "calkowita","ulamek")

    writer.writerow(naglowek)
    for i in range(1,100):
        calkowita = random.randint(0,100)
        ulamek = random.random()
        #FIXME: wyswietlaj tylko 2 miejsca dziesietne
        wiersz = (i+1, calkowita,ulamek)
        writer.writerow(wiersz)

        
