from ephem import readtle, degree

station = "ISS zayra"
tle1 = "1 25544U 98067A   20347.38065972  .00001339  00000-0  32251-4 0  9999"
tle2 = "2 25544  51.6440 186.7650 0001859 122.9504 239.1247 15.49179161259649"

iss = readtle(station, tle1, tle2)

iss.compute()

lat = iss.sublat
print(lat)

def angle2exif(angle): #angle is string
    angle = str(angle)
    parts = angle.split(":")
    
    if int(parts[0]) < 0:
        rawd = False
    else: rawd = True

    part0 = int(parts[0])
    part1 = str(parts[1])
    part2 = float(parts[2])
    if rawd == False:
        part0 = part0 * -1
    part0 = str(part0) + "/1"
    part1 = part1 + "/1"
    part2 = part2 * 10
    part2 = str(int(part2)) + "/10"
    parts2 = [part0, part1, part2]
    trime = ",".join(parts2)
    
    tupl = (rawd, trime)
    return (tupl)

angle2exif(lat)
