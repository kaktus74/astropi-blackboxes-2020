import csv
import random

#TODO-4 Zamien zahardcodowaną ścieżkę na scieżkę ../data/random.csv względem pliku źródłowego
csv_sciezka = '/home/kaktus74/astropi2021/astropi-blackboxes-2020/spotkanie-2020-11-21/data/random.csv'


#TODO-5 Dodaj do pliku CSV kolejną kolumnę: losowe_imie ktorej wartość będzie losowo wybierana spośród Waszych imion
with open(csv_sciezka, 'w') as plik:
    #FIXME: użyj znaków cytujących. Patrz: https://docs.python.org/3/library/csv.html
    writer = csv.writer(plik,delimiter='.', quoting=csv.QUOTE_MINIMAL )

    naglowek = ("lp", "calkowita","ulamek")
    # A B
    # 1,"Oni,my ,wy"
    # 2,Ala ma kota

    writer.writerow(naglowek)
    for i in range(1,100):
        calkowita = random.randint(0,100)
        ulamek = random.random()
        #FIXME: wyswietlaj tylko 2 miejsca dziesietne
        wiersz = (i+1, calkowita,"{0:.2f}".format(ulamek))
        writer.writerow(wiersz)

        
