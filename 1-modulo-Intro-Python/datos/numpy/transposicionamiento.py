import numpy as np

array_30 = np.arange(30)

redimensionado = array_30.reshape((5, 6))
'''
Out[63]:
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23],
       [24, 25, 26, 27, 28, 29]])
'''

redimensionado.T
'''
Out[64]:
array([[ 0,  6, 12, 18, 24],
       [ 1,  7, 13, 19, 25],
       [ 2,  8, 14, 20, 26],
       [ 3,  9, 15, 21, 27],
       [ 4, 10, 16, 22, 28],
       [ 5, 11, 17, 23, 29]])
'''

# al usar reshape con un array,
# se debe tener en cuenta que la multiplicacion
# de los elementos de la tupla
# debe ser igual a la cantidad de elementos
# del array
5 * 6 == len(array_30)
#Out[65]: True