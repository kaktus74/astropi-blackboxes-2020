#przyklad4-angle.py

from ephem import readtle, degree

station = "ISS zayra"
tle1 = "1 25544U 98067A   20347.38065972  .00001339  00000-0  32251-4 0  9999"
tle2 = "2 25544  51.6440 186.7650 0001859 122.9504 239.1247 15.49179161259649"

iss = readtle(station, tle1, tle2)

iss.compute()


lat = iss.sublat

print(type(lat))
print(float(lat))
print(str(lat))
      

