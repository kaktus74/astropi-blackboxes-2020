import random as rnd

class SenseHatFake:

    def __init__(self, t):
        self.t = t

    @property
    def temperature(self):
        return self.t + rnd.random()
