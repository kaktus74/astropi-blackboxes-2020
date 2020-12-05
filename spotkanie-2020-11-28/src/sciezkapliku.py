import os
import modul2

#plk_zrodlowy = __file__
# fld_zrodlowy = os.path.dirname(__file__)

#print("Plik źródłowy             : {0}".format(plk_zrodlowy))
#print("Folder pliku źródłowego   : {0}".format(fld_zrodlowy))


print("Moduł 1, __file__: {0}".format(__file__))
print("Moduł 1, __name__: {0}".format(__name__))

if __name__ == '__main__':
    print('Jestem modułem 1, zostałem odpalony jako główny')
    print('Jestem w folderze {0}'.format(os.path.dirname(__file__)))
