from itertools import groupby

lista = [1, 2, 6, 7, 2, 5, 8, 9, 1, 3, 6, 7]

diccionario = {}

for i in lista:
    if i in diccionario:
        diccionario[i] += 1
    else:
        diccionario[i] = 1

diccionario
# Out[22]: {1: 2, 2: 2, 6: 2, 7: 2, 5: 1, 8: 1, 9: 1, 3: 1}
lista.sort()

diccionario = {k: len(list(v)) for k, v in groupby(lista)}
diccionario
# Out[24]: {1: 1, 2: 1, 6: 1, 7: 1, 5: 1, 8: 1, 9: 1, 3: 1}

precios = {
    "notebook": 340000,
    "celular": 190000,
    "cargador": 12500,
    "tablet": 150000
}

lista_precios = list(precios.items())
print(lista_precios)
# [('notebook', 340000), ('celular', 190000), ('cargador', 12500), ('tablet', 150000)]

animales = ["perro", "gato", "erizo"]
animales.sort()

diccionario = {key: len(list(value)) for key, value in groupby(animales)}
diccionario
#Out[31]: {'erizo': 1, 'gato': 1, 'perro': 1}