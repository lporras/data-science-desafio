import numpy as np

# retorna un nuevo numpy array con valores reasignados
# np.where(una condiciones, se cumple, no se cumple)

notas = np.array([4.5, 6.6, 7.0, 2.0, 3.6, 4.6, 5.6, 5.8, 2.5])

notas.mean()
# Out[76]: 4.688888888888889

notas_bin = np.where(notas >= notas.mean(), 1, 0)
# Out[78]: array([0, 1, 1, 0, 0, 0, 1, 1, 0])

# notas[notas >= notas.mean()]