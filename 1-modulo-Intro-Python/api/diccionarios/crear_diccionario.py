notas = {
    "Camila": 7,
    "Antonio": 5,
    "Felipe": 6,
    "Antonia": 7
}

notas["Felipe"]
notas["Camila"]

duplicados = {"clave": 1, "clave": 2}

notas["Alejandra"] = 4
notas["Alejandra"] = 6

diccionario = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 33,
    "altura": 1.75
}

for i in diccionario:
    print(i)

for clave in diccionario:
    valor = diccionario[clave]
    print("La clave es {} y el valor es {}".format(clave, valor))

"nombre" in diccionario
# True

for clave, valor in diccionario.items():
    print(clave, valor)

diccionario.items()
#Out[9]: dict_items([('nombre', 'Juan'), ('apellido', 'Perez'), ('edad', 33), ('altura', 1.75)])

usuarios_por_pais = {"Mexico": 65, "Chile": 50, "Argentina": 55}

for pais in usuarios_por_pais:
    print(pais)

for pais, usuarios in usuarios_por_pais.items():
    if usuarios > 60:
        print(pais)