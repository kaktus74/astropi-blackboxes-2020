def czy_liczba(wart):
    try:
        int(wart)
        return True
    except ValueError: # np. 'ala'
            return False
    except TypeError: # np. None
            return False
    
def czy_wiek(wart):

    if czy_liczba(wart) == False:
        return False

    # wiem, juz ze to liczba wiec moge bezpiecznie kowertowac wart na int
    liczba = int(wart)    

    if liczba < 0:
        # ktos moglby uznac, ze 0 to tez dobry wiek, np dla noworodka a nawet,
        # ze -1 to dobry wiek kilkumiesiecznego plodu slonia;
        # my jednak umawiamy sie, ze najnizszy akceptowalny wiek to 1
        return False

    return True

def podaj_liczbe(pytanie):
    i = input(pytanie)
    while czy_liczba(i) == False:
        print('Ojoj, odpowiedź na pytanie''{0}'' musi być liczbą całkowitą'.format(pytanie))
        i = input(pytanie)
    return int(i)


def podaj_wiek(pytanie):
    i = input(pytanie)
    while czy_wiek(i) == False:
        print('Oj, podales/as cos nie tak. Odpowiedź nz ''{0}'' musi być liczbą nieujemną'.format(pytanie))
        i = input(pytanie)
    return int(i)

def srednia(tab):
    n = 0
    suma = 0
    while n < len(tab):
        suma = suma + tab[n]
        n = n + 1
    return suma / len(tab)

def ankieta():
    liczba_os = podaj_liczbe('Ile osob? ')
    lata = []
    
    #TODO: zmodyfikuj kod tak, aby zamiast while uzyc petli for
    for n in range(0,liczba_os):
        #TODO-3: zmodyfikuj kod tak, zeby system wyswietlil nr osoby o ktorej wiek pyta
        wiek = podaj_wiek('Ile lat (osoba {0})? '.format(n+1))
        lata.append(wiek)

    sredniaw = srednia(lata)
    print(sredniaw)
    

if __name__ == '__main__':
    ankieta()
