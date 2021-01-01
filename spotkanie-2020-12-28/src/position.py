import zad1
from ephem import readtle, degree
from datetime import datetime, timezone

name = 'ISS zayra'
p1 = "1 25544U 98067A   20347.38065972  .00001339  00000-0  32251-4 0  9999"
p2 = "2 25544  51.6440 186.7650 0001859 122.9504 239.1247 15.49179161259649"

iss = readtle(name, p1, p2)

pos_lat = (zad1.angle2exif(str(iss.sublat)))
pos_lon = (zad1.angle2exif(str(iss.sublon)))
if pos_lat[0] == True:
    hemisphere = 'N'
else:
    hemisphere = 'S'
