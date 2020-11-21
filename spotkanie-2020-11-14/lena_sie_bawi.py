import csv



def czy_liczba(napisane):
    try:
        x = int(napisane)
        return x
    except ValueError:
        return False


def int_input(pytanie):
    s = input(pytanie)
    while czy_liczba(s) == False:
        s = input(pytanie)
    return czy_liczba(s)
    
    

def srednia():

    with open('
    
    x = non_negative_int_input('Ile osób')
    n = 0
    suma = 0
    while n < x:
        a = int_input('Ile lat ')
        suma = suma + a
        n = n + 1
    sredniaw = suma / x
    print(sredniaw)
    return(sredniaw)


try:
    srednia()
except ZeroDivisionError:
    print ('Wiek i ilość osób to chyba liczby większe od zera nie? Spróbuj jeszcze raz. Nie dawaj zera jeszcze raz.')
    srednia()
except ValueError:
    print ('Oczekuję liczby... Wiesz co to tak? Spróbuj jeszcze raz!')
    srednia()
