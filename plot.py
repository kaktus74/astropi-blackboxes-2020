from matplotlib import pyplot as plt

fig, axs = plt.subplots(2,2)

x = [0,1,2,3,4,5]
y = [x*x for x in x]

axs[0][0].plot(x,y)

fig.show()
