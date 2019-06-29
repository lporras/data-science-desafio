diccionario_a = {"nombre": "Alejandra", "apellido": "Lopez", "edad": 33, "altura": 1.55}
diccionario_b = {"altura": 155, "mascota": "miti", "ejercicio": "bicicleta"}
diccionario_a.update(diccionario_b)

print(diccionario_a)
# {'nombre': 'Alejandra', 'apellido': 'Lopez', 'edad': 33, 'altura': 155, 'mascota': 'miti', 'ejercicio': 'bicicleta'}
print(diccionario_b)
# {'altura': 155, 'mascota': 'miti', 'ejercicio': 'bicicleta'}