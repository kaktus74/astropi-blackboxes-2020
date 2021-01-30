from picamera import PiCamera
import os

# v_stracji_na_orbicie = 7660 m/s
# 161 m/pixel
# v_punktu_pod_stacją = 40 075 km / 5400 s = 7,421 km/s
# obwód_ziemi = 40 075 km
# wielkość_kwadratu = 1080 x 1080 pixels
# fov = 1080 * 161 = 173 880 m = 173,88 km
# 90 minut obieg ziemi = 5400 s
# co tyle km zdj? 148,42‬ = 7,421*20
# co ile sekund 173,88 km / 7,421 km/s = 23,43 s

def fov_time():
    # TODO return czas przelotu w s nad fov
    earth_circuit = 40075
    
    return 0

cam = PiCamera()

with cam:
    cam.resolution = (1920, 1080)
    cam.exif_tags['GPS.GPSLatitude'] = '53/1,26/1,261/10'
    cam.exif_tags['GPS.GPSLatitudeRef'] = 'N'
    cam.exif_tags['GPS.GPSLongitude'] = '14/1,29/1,337/10'
    cam.exif_tags['GPS.GPSLongitudeRef'] = 'E'
    cam.capture(os.path.dirname(__file__) + '/data/tales4.jpg')
