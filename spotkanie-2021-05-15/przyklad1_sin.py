from matplotlib import pyplot as plt

from math import sin

from random import random


def mov_avg(values, n):
    res = []
    for i in range(0,len(values)):
        if i < n -1:
            res.append(None)
        else:
            sum = 0
            for j in range(0,n):
                   sum = sum + values[i-j]
            res.append(float(sum) / n)
    return res
    

PI = 3.141519

n = 100


x_values = range(0,n)
y_values = [sin(float(x)/n*2*PI) for x in x_values] 

noise_level = 0.5
noise = [noise_level * random() for x in x_values] 

y_values_with_noise = [y_values[i] + noise[i] for i in range(0,len(y_values))]

p = 5
y_mov_avg = mov_avg(y_values_with_noise, p)


fig, ax = plt.subplots(4)

ax[0].plot(x_values, y_values)
ax[1].plot(x_values, noise)
ax[2].plot(x_values, y_values_with_noise)
ax[3].plot(x_values, y_mov_avg)

for axis in ax:
    axis.set_ylim(-1.5, 1.5)


plt.show()
