import os



fld_roboczy = os.getcwd() #to samo co `$ pwd` w bashu 
fld_dziecko = os.path.realpath("egg")
fld_absolutny = os.path.realpath("/spam")
plk_zrodlowy = __file__
fld_zrodlowy = os.path.dirname(__file__)

print("Folder roboczy            : {0}".format(fld_roboczy))
print("Folder dziecko (wzgledna) : {0}".format(fld_dziecko))
print("Folder absolutny          : {0}".format(fld_absolutny))
print("Plik źródłowy             : {0}".format(plk_zrodlowy))
print("Folder pliku źródłowego   : {0}".format(fld_zrodlowy))



