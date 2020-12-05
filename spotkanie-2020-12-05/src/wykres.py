import pandas as pd
import os
import matplotlib.pyplot as plt

csv_file = os.path.dirname(__file__) + "/../data/temperatura.csv"
print(csv_file)


dane = pd.read_csv(csv_file, sep=';', index_col='czas')
dane.index = pd.to_datetime(dane.index, format='%Y-%m-%dT%H:%M:%S.%f')

czas = dane.index
temperatura = dane['temperatura']

print(czas)
print(temperatura)

plt.plot_date(czas, temperatura)
