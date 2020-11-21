from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#TODO-6: Zapisz zmierzone dane w pliku csv w w ukladzie:
# kolumny: nr_pomiaru , temperatura ( z dokładnością do 4 miejsc po przecinku)
for i in range(1,100):
    t = sense.temperature
    sleep(0.1)
    print(t)

