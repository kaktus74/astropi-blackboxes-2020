import os
#import modul2

fld_roboczy = os.getcwd() #to samo co `$ pwd` w bashu 
print("Teraz jestem w (Folder roboczy) :\n{0}".format(fld_roboczy))


przejdz_do = input('Podaj nazwę foleru ')

fld_absolutny = os.path.realpath(przejdz_do)

print('Przechodzę do:\n{0}\npełna ścieżka:\n{1}'.format(przejdz_do, fld_absolutny))
os.chdir(przejdz_do)

fld_roboczy = os.getcwd() #to samo co `$ pwd` w bashu 
print("Teraz jestem w (Folder roboczy) :\n{0}".format(fld_roboczy))

print("Moje dzieci to:\n{0}".format(os.listdir()))

# plk_zrodlowy = __file__
# fld_zrodlowy = os.path.dirname(__file__)

#print("Plik źródłowy             : {0}".format(plk_zrodlowy))
#print("Folder pliku źródłowego   : {0}".format(fld_zrodlowy))



