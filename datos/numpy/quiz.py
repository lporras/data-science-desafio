import numpy as np

primera = np.arange(50)
segunda = primera[10:20]
segunda[2] = "100"
print(primera[12])
#100
type(primera[12])
#Out[102]: numpy.int64
type(segunda[2])
#Out[103]: numpy.int64

mascotas = np.array(["Copi-Copi", "Elemento", "Adjetivo", "Mente en Blanco", "Chaucha", "Cabecita", "Bigote", "Mutante"])

especies = np.array(["perro", "perro", "perro", "perro", "perro", "gato", "gato", "gato"])
filtrados = mascotas[~(especies == "gato")]
print(filtrados)
# ['Copi-Copi' 'Elemento' 'Adjetivo' 'Mente en Blanco' 'Chaucha']
