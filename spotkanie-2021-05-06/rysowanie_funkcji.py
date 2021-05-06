from math import sin
def f(x):
    return sin(x/10)

xs = range(0,1000)


ys = [f(x) for x in xs]

print(list(xs))

print(ys)

from matplotlib import pyplot

pyplot.plot(xs, ys)
pyplot.show()


