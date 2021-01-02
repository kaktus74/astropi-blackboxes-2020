import reverse_geocoder as rg
from ephem import readtle, degree
from time import sleep
from datetime import datetime, timezone


name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   20365.25294914  .00000870  00000-0  23743-4 0  9990"
line2 = "2 25544  51.6464  98.3330 0001208 167.2107 217.0739 15.49236186262418"

iss = readtle(name, line1, line2)
now_utc = datetime.now(timezone.utc)
iss.compute(now_utc)

pos = (iss.sublat / degree, iss.sublong / degree)

#pos = (69.358026, 88.136941)

location = rg.search(pos, mode=1)
print(location[0]['name'])
