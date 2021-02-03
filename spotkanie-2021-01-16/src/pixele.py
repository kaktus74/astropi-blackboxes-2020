from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

def pudelko():
    X = [0, 0, 0]   #czarny ?
    O = [200, 180, 255] # ?

    box = [
        O, O, O, O, O, O, O, O,
        X, O, O, O, O, O, O, X,
        O, X, O, O, O, O, X, O,
        O, O, X, X, X, X, O, O,
        O, O, X, X, X, X, O, O,
        O, O, X, X, X, X, O, O,
        O, O, X, X, X, X, O, O,
        O, O, O, O, O, O, O, O]

    sense.set_pixels(box)

def bubr():
    X = [153, 217, 234] #LIGHT BLUE
    O = [61, 135, 98] #MARITIME
    A = [126, 80, 54] #BROWN1
    T = [78, 49, 33] #BROWN2
    R = [101, 64, 44] #BROWN3

    bebr = [
        X, X, X, X, X, X, X, X,
        X, X, X, A, A, X, X, X,
        X, X, A, O, A, A, X, X,
        X, X, T, A, A, A, X, X,
        X, X, X, R, A, A, X, T,
        X, X, X, R, A, A, X, T,
        X, X, T, A, A, A, T, X,
        X, X, X, X, X, X, X, X
        ]

    sense.set_pixels(bebr)

if __name__ == '__main__':
    pudelko()
    sleep(7)
    bubr()
    sleep(7)
    sense.clear()
