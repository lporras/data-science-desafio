import numpy as np

# se pueden crear arreglos de muchas dimensiones

matriz = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

matriz[2][1] == matriz[2, 1]

matriz[:2, 1:]
matriz[:2][1:]
matriz[0, 1:]

vector = np.array([])