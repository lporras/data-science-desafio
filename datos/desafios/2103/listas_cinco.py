from velocidad import promedio
from listas_uno import all_cars

velocidades = list(map(lambda x: x[1], all_cars))
promedio_velocidades = promedio(velocidades)

velocidades_mayores = list(filter(lambda x: x > promedio_velocidades, velocidades))
print(velocidades_mayores)