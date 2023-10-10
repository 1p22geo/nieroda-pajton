import matplotlib
import matplotlib.pyplot as plt
import random
x = []
y = []

a = (0,0)
b = (1,0)
c = (0.5, 3**(1/2))

q [0,0]

m = 1000
for e in range(1,m):
    point = random.choice(a,b,c)
    
    q[0] = (q[0] + point[0])/2
    q[1] = (q[1] + point[1])/2
    x.append(q[0])
    y.append(q[1])

    print(e)