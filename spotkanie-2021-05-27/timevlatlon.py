from csv import reader
from dateutil import parser
from matplotlib import pyplot
from latconv import to_coord

with open("data01.csv",'r') as f:
    dane1 = list(reader(f))[1:]
    dane2 = [data[0].split(';') for data in dane1]
    time = [parser.parse (data[1]) for data in dane2]
    lat = [to_coord(data[2]) for data in dane2]
    #print(lat)
    lon = [to_coord(data[3]) for data in dane2]
    #x = [float (cases[4]) for cases in dane2]
    #y = [float (cases[5]) for cases in dane2]
    #z = [float (cases[6]) for cases in dane2]
    m = [float (cases[7]) for cases in dane2]
    #m2 = [float(data[7] +float(data[2].split(':')[0]) ) for data in dane2]

    
    
    fig, ax = pyplot.subplots(3) # ax = axis
    #fig, ax = pyplot.subplots(2) # ax = [axis0, axis2]
    
    #ax.plot(time, x, label='x')#m2 = m-(lon*0.1)
    #ax.plot(time, y, label='y')
    #ax.plot(time, z, label='z')
    #ax[0].plot(time, m, label='m')
    #ax[0].plot(time, lon, label='lon')#lon wygląda tak -107:07:22.5
    #ax[0].plot(time, lat, label='lat')
    #ax[0].set_xlabel('x label')  # Add an x-label to the axes.
    #ax[0].set_ylabel('y label')  # Add a y-label to the axes.
    #ax[0].set_title("time v x,y,z,m,lon")  # Add a title to the axes.
    #ax[0].legend()  # Add a legend.

    #TODO: OZNACZENIA
    
    ax[0].scatter(lat,m)
    ax[1].scatter(lon,m)
    ax[2].plot(time,lat)

    pyplot.show()
