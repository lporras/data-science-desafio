from velocidad import promedio
from listas_uno import all_cars

velocidades = list(map(lambda x: x[1], all_cars))

promedio_velocidades = promedio(velocidades)

for auto in all_cars:
  if auto[1] > promedio_velocidades:
    print(auto)

