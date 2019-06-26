import numpy as np

numpy_array = np.array([2, 4, 12])
type(numpy_array)
#Out[3]: numpy.ndarray

multiplicados_array = numpy_array * 3

multiplicados_array.shape

multiplicados_array.dtype

array_string = np.array(["gato", "perro", "erizo"])

type(array_string)
#Out[20]: numpy.ndarray

mixto = np.array(["gato", 1, 2.8])

type(mixto)