from csv import reader
from dateutil import parser
from matplotlib import pyplot

with open('Node2-100.csv', 'r') as f:

    data = list(reader(f))

    x_list = [parser.parse (i[19]) for i in data[1:]]
    y_list = [i[1] for i in data[1:]]

    pyplot.plot(x_list, y_list)
    pyplot.show()
