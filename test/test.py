import matplotlib
import matplotlib.pyplot as plt
import math


xlist = [x/50 for x in range(1,1001)]
ylist = [math.sin(x) for x in xlist]


plt.figure(1)
plt.plot(xlist, ylist)
plt.show()