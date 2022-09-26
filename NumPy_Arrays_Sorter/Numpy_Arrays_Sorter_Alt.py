import numpy as np

a = np.array([3,45,6,7,1,22,4,5])
def sorting(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x
print(sorting(a))