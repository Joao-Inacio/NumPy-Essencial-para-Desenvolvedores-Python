import numpy as np
np.set_printoptions(legacy='1.13')

numero = input().strip()

digitos = [int(d) for d in numero if d.isdigit()]

print(np.eye(digitos[0], digitos[1], k=0))

