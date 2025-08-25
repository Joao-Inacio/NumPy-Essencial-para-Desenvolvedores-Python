import numpy as np


arr = input().strip().split(' ')


linhas = []

for i in range((int(arr[0]) + int(arr[1]))):
    n = arr = input().strip().split(' ')
    linhas.append([int(x) for x in n])

array = np.array(linhas)

print(array)
