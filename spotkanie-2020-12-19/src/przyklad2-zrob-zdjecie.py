from picamera import PiCamera
from time import sleep

cam = PiCamera()

cam.resolution = (1920, 1080)
cam.start_preview()
sleep(2)
cam.capture("/tmp/test.jpg")
