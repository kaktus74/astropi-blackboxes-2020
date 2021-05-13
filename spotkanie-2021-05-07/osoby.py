dziennik = [["Aneta", 3.5], ["Arnold", 4.0], ["Bernard", 6.0], ["Zenobia", 5.0], ["Klementyna", 1.0]]

#print(dziennik)
zagrozone = [osoba[0] for osoba in dziennik if osoba[1] < 2.0]
#            ^^^^^^^^                       ^^^^^^^^^^^^^^^^^
#            mapowanie                      filtrowanie

#zagrozone = []
#for osoba in dziennik:
#    if osoba[1] < 2.0:
#        zagrozone.append(osoba)
#        #print(osoba)

print(zagrozone)        
