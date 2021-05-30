from matplotlib import pyplot as plt

from math import sin

PI = 3.141519

n = 100

x_values = range(0,n)
y_values = [sin(float(x)/n*2*PI) for x in x_values] 


fig, ax = plt.subplots(2)

ax[0].plot(x_values, y_values)
#ax[1].plot(x_values, y_values)

fig.show()
