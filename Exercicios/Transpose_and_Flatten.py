import numpy as np


arr = input().strip().split(' ')

linhas = []

for i in range(int(arr[0])):
    n = arr = input().strip().split(' ')
    linhas.append([int(x) for x in n])

array = np.array(linhas)

def to_transpose(narray):
    return np.transpose(narray)

def to_flatten(narray):
    return narray.flatten()

print(to_transpose(array))
print(to_flatten(array))
