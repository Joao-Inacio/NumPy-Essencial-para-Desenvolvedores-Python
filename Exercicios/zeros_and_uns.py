import numpy as np

numero = input().strip()

digitos = [int(d) for d in numero if d.isdigit()]


print(np.zeros(shape=(digitos), dtype=int))
print(np.ones(shape=(digitos),dtype=int))
