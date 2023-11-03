import matplotlib
import numpy as np
import matplotlib.pyplot as plt

x = [1699017208,
1699017224,
1699017256,
1699017313,
1699017353,
1699017374,
1699017393,
1699017433,
1699017467,
1699017493,
1699017515,
1699017526,
1699017550,]
x = np.array(x)

y=[0,
262080,
524224,
1032128,
1556416,
1556416,
1818564,
2211780,
2473924,
2736068,
2998212,
2998212,
3140420,
]
y = np.array(y)

a, b = np.polyfit(x, y, 1)

plt.scatter(x,y , c='black', s=2)
plt.plot(x, a*x+b, c="red")

print(a,b)

plt.show()