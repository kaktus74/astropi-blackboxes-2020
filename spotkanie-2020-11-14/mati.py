def poprawnosc(i):
    try:
        i = int(243/int(i))
        return True
    except ValueError:
        return False
    except TypeError:
        return False
    except ZeroDivisionError:
        return False

def int_input(napis):
    i = input(napis)
    while poprawnosc(i) == False:
        print('Oj, podales/as cos nie tak. ')
        i = input(napis)
    return int(i)

def srednia():
    x = int_input('Ile osob? ')
    n = 0
    suma = 0
    while n < x:
        a = int_input('Ile lat? ')
        suma = suma + a
        n = n + 1
    sredniaw = suma / x
    print(sredniaw)
    return(sredniaw)

srednia()

#Why hello there
#Hi!
#To jest dobrze.

