from math import pi, sin
from matplotlib import pyplot as plt
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
 
n = 100

x_values = range(0, n)
y_values = [sin(float(x)/n*2*pi)  for x in x_values]

noise_level = 0.3
noise = [random()*noise_level-noise_level/2 for x in x_values]
values_with_noise = [y_values[i]+noise[i] for i in range(0,n)]


values_smoothed = [ mov_avg(values_with_noise,3), mov_avg(values_with_noise,5),mov_avg(values_with_noise,20),mov_avg(values_with_noise,50)]

fig, ax = plt.subplots(7)

ax[0].plot(x_values, y_values)
ax[1].plot(x_values, noise)
ax[2].plot(x_values, values_with_noise)

i = 3
for smoothed in values_smoothed:
    ax[i].plot(x_values, smoothed)
    i = i + 1

    

for axis in ax:
    axis.set_ylim(-1.1,1.1)
    axis.set_xlim(0,100)

plt.show()

# 1 czysty sin
# 2 szum
# 3 sin + szum
# 4 wygladzony (smoothed)
