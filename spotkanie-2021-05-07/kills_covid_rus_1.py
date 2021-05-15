from csv import reader
from dateutil import parser
from matplotlib import pyplot

with open("covid.csv",'r') as f:
    tanea = [dane for dane in list(reader(f)) if dane[0] == 'RUS']
    time = [parser.parse (data[3]) for data in tanea]
    kills_total      = [int (cases[7]) for cases in tanea]
    killstreak_daily = [int (cases[8]) for cases in tanea]

    pyplot.ylabel('covid russia is in trouble')
    pyplot.plot(time, kills_total)
    pyplot.plot(time, killstreak_daily)
    pyplot.show()
