list({"k1": 5, "k2": 7}.items())

dict([("k1", 5), ("k2", 7)])

nombres = ["Alumno1", "Alumno2", "Alumno3"]
notas = [10, 3, 8]

notas_por_alumno = {}

for i in range(len(nombres)):
    alumno = nombres[i]
    nota = notas[i]
    notas_por_alumno[alumno] = nota

#In [6]: notas_por_alumno
#Out[6]: {'Alumno1': 10, 'Alumno2': 3, 'Alumno3': 8}

notas_por_alumno = dict(zip(nombres, notas))
notas_por_alumno
#Out[9]: {'Alumno1': 10, 'Alumno2': 3, 'Alumno3': 8}