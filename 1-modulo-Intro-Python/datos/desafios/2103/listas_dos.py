from velocidad import promedio
from listas_uno import all_cars

def promedio_all_cars(all_cars):
  numbers_1 = []
  numbers_2 = []
  numbers_3 = []
  for auto in all_cars:
    numbers_1.append(auto[1])
    numbers_2.append(auto[2])
    numbers_3.append(auto[4])
  return([promedio(numbers_1), promedio(numbers_2), promedio(numbers_3)])

promedios = promedio_all_cars(all_cars)
for i in promedios:
  print(i)