from csv import reader
from dateutil import parser
from matplotlib import pyplot
from latconv import to_coord

with open("all_photos_seroihfjsh.csv",'r') as f:
    with open("gooddanesun.csv",'r') as sun:
        dane1 = list(reader(f, delimiter=','))[1:]
        dane2 = list(reader(sun, delimiter=';'))
        #dane2 = [data[0].split(',') for data in dane1]
        
        i = 2
        time = []
        day_night = []
        water = []
        hills = []
        m = []
        lat = []
        lon = []
        while i < len(dane1):
            time.append (parser.parse (dane1[i][1]))
            day_night.append (float (dane1[i][8]))
            water.append (float (dane1[i][9]))
            hills.append (float(dane1[i][10]))
            m.append (float (dane1[i][7]))
            lat.append (to_coord(dane1[i][2]))
            lon.append (to_coord(dane1[i][3]))
            i+=3

        suntime = [parser.parse (data[0]) for data in dane2]
        sunm = [float (data [4]) for data in dane2]
        #print (sunm)
        #time = [parser.parse (data[1]) for data in dane1] # [..,'2021-04-...','fdsfdsf'] => [2021-04-16...]
        #lat = [to_coord(data[2]) for data in dane1]
        #print(lat)
        #lon = [to_coord(data[3]) for data in dane1]
        #day_night = [print (len(data[8])) for data in dane1]
        #water = [float (data [9]) for data in dane1]
        #hills = [float (data [10]) for data in dane1]
        #x = [float (cases[4]) for cases in dane2]
        #y = [float (cases[5]) for cases in dane2]
        #z = [float (cases[6]) for cases in dane2]
        #m = [float (cases[7]) for cases in dane1]
        #m2 = [float(data[7] +float(data[2].split(':')[0]) ) for data in dane2]

        
        
        fig, ax = pyplot.subplots(2) # ax = axis
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
        
        #ax[0].scatter(day_night, m, label="day or night")
        #ax[0].set_title("Bt by the time of day (photos)")
        #ax[0].set_ylabel("Bt [nT]")
        #ax[0].set_xlabel("0 - day, 1 - night")#by "day" we mean a situation when the terrain below ISS is lit up by the sun
        #ax[1].scatter(water, m, label = "water")
        #ax[1].set_title("Bt by the presence of water")
        #ax[1].set_ylabel("Bt [nT]")
        #ax[1].set_xlabel("0 - above land , 1 - above ocean")
        #ax[2].scatter(hills, m, label="mountains")
        #ax[2].set_title("Bt by the presence of mountains")
        #ax[2].set_ylabel("Bt [nT]")
        #ax[2].set_xlabel("0 - no mountains below ISS, 1 - ISS is directly above mountains")
        #ax[0].scatter(lat, m)
        #ax[0].set_title("Bt (latitude)")
        #ax[0].set_ylabel("Bt [nT]")
        #ax[0].set_xlabel("latitude [deg]")
        #ax[1].scatter(lon, m)
        #ax[1].set_title("Bt (longitude)")
        #ax[1].set_ylabel("Bt [nT]")
        #ax[1].set_xlabel("longitude [deg]")
        ax[0].scatter(time,m)
        ax[0].set_title("Bt (time)")
        ax[0].set_ylabel("Bt [nT]")
        ax[0].set_xlabel("time")
        ax[0].set_xlim(time[0],time[-1])
        ax[1].plot(suntime,sunm)
        ax[1].set_title("Bt on ACE (time)")
        ax[1].set_ylabel("Bt [nT]")
        ax[1].set_xlabel("time")
        ax[1].set_xlim(time[0],time[-1])
        #ax[2].scatter(lon,lat)
        #ax[2].set_title("latitude (longitude)")
        #ax[2].set_ylabel("latitude [deg]")
        #ax[2].set_xlabel("longitude [deg]")
        #ax[1][2].scatter()
        
        #pyplot.dpi = 42000
        pyplot.tight_layout(0.5)
        pyplot.savefig("bboxandbeavers_btxtime.png",dpi=300 ,papertype="a4")
        pyplot.show()
        
