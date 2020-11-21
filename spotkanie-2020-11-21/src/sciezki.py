import os



fld_roboczy = os.getcwd() #to samo co `$ pwd` w bashu 
fld_dziecko = os.path.realpath("egg")
plk_zrodlowy = __file__
fld_zrodlowy = os.path.dirname(__file__)

print("Folder roboczy         : {0}".format(fld_roboczy))
print("Folder dziecko         : {0}".format(fld_dziecko))
print("Plik źródłowy          : {0}".format(plk_zrodlowy))
print("Folder pliku źródłowego: {0}".format(fld_zrodlowy))



