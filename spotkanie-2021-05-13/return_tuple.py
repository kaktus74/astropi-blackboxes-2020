import matplotlib.pyplot as plt

#def lokalizacja():
#    return 1,2

#x,y = lokalizacja()

#print(x,y)


fig, ax = plt.subplots(2,2)

ax[0][0].plot([1, 2,1],[1,2,3])
#              x0 x1y0  y1
ax[0][1].plot([1,2],[1,2])
plt.show()


