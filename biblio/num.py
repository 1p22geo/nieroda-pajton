import numpy as np;

tab1 = np.array([[1,2,3,4], [5,4,3,3], [1,5,3,2], [4,3,2,4]])
tab2 = np.array([[2,3,4,5], [6,2,3,2], [1,3,2,2], [4,4,2,1]])

q = tab1 * tab2

print(q)
print(q.shape)