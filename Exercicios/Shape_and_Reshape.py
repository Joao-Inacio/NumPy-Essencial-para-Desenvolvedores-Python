import numpy as np

def Reshape(arr):
    ar = np.array(arr, int)
    rs = np.reshape(ar, (3,3))
    return rs

arr = input().strip().split(' ')
result = Reshape(arr)
print(result)
