import numpy as np
a = np.arange(1,13).reshape(3,2,2)
print (a)
a.ndim
a.shape
a.size
np.eye(1, 4)
     
M = np.eye(5, dtype="int")

M[3:, :2] = 2
M[:2, 3:] = 3

print(M)
