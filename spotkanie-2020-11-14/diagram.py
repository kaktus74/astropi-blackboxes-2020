import pandas as pd
import matplotlib.pyplot as plt

frame = pd.read_csv('test.csv')
print(frame.describe())

    
wiek = frame["wiek"]
imie = frame["imie"]
frame.plot(kind="bar")
plt.show()
