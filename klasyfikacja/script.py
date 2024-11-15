import numpy as np
import sys
import matplotlib
import matplotlib.pyplot as plt
import random


x = []
y = []

c = []

with open("loan_data.csv") as f:
    lines = f.readlines()[1:]
    for line in lines:
        try:
            line = line.strip().split(",")
            print(line)
            x.append(int(float(line[0])))
            y.append(float(line[3]))
            c.append("green" if line[-1] == "1" else "red")
        except Exception:
            print(f"failed to load line:\n{line}", file=sys.stderr)


x = np.array(x)
y = np.array(y)
c = np.array(c)

plt.scatter(x, y, c=c)
plt.show()
