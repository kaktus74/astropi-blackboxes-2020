from csv import reader
from dateutil import parser
from matplotlib import pyplot

with open('Node2-100.csv','r') as f:

    data = list(reader(f))[1:]

    tudu_dudu = [row[4] for row in data]
    czes = [parser.parse(row[-1]) for row in data]

    print(tudu_dudu)
    
    pyplot.ylabel('Humidity - woda w powietrzu')
    pyplot.plot(czes, tudu_dudu)
    
    pyplot.show()
    
