from csv import reader
from dateutil import parser
from matplotlib import pyplot

with open("covid.csv",'r') as f:
    rusispoaczn_data = [dane for dane in list(reader(f)) if dane[0] == 'RUS']
    time = [parser.parse (data[3]) for data in rusispoaczn_data]
    y_axis1 = [float (cases[10]) for cases in rusispoaczn_data]
    y_axis2 = [float (cases[11]) for cases in rusispoaczn_data]

    fig, ax = pyplot.subplots(2)

    pyplot.ylabel('Zachorowania na 1 000 000 ludzi.')
    ax[0].plot(time, y_axis1)
    pyplot.show()
