import numpy as np

nombres = np.array(["Sebastian", "Pedro", "Maria", "Fernanda"])

notas = np.array([[5, 5, 6], [6, 6, 7], [7, 7, 6], [5, 4, 6]])

nombres == "Pedro"
# Out[56]: array([False,  True, False, False])

notas[nombres == "Pedro"]
# Out[57]: array([[6, 6, 7]])
notas[np.array([False, True, False, False])]
# Out[57]: array([[6, 6, 7]])

notas[~(nombres == "Pedro")]

#Out[58]:
#array([[5, 5, 6],
#       [7, 7, 6],
#       [5, 4, 6]])

