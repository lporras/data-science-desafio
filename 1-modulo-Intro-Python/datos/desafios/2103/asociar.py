from velocidad import promedio

velocidades = [
  4,  4, 7, 7, 8, 9,
  10, 10, 10,11, 11,
  12, 12, 12, 12, 13,
  13, 13, 13, 14, 14,
  14, 14, 15, 15, 15,
  16, 16, 17, 17, 17,
  18, 18, 18, 18, 19,
  19, 19, 20, 20, 20,
  20, 20, 22, 23, 24,
  24, 24, 24, 25
]

distancias = [
  2, 10, 4, 22, 16,
  10, 18, 26, 34,
  17, 28, 14, 20,
  24, 28, 26, 34,
  34, 46, 26, 36,
  60, 80, 20, 26,
  54, 32, 40, 32,
  40, 50, 42, 56,
  76, 84, 36, 46,
  68, 32, 48, 52,
  56, 64, 66, 54,
  70, 92, 93, 120, 85
]

def zip(lista_1, lista_2):
  total_elementos = len(lista_1)
  lista_zip = []
  for i in range(total_elementos):
    lista_zip.append((lista_1[i], lista_2[i]))
  return lista_zip

velocidad_promedio = promedio(velocidades)
#print("velocidad promedio:", velocidad_promedio)
distancia_promedio = promedio(distancias)
#print("distancia promedio:", distancia_promedio)

velocidades_bajo_promedio = 0
velocidades_bajo_y_distiancias_sobre_promedio = 0
velocidades_sobre_promedio = 0
velocidades_sobre_y_distancias_bajo_promedio = 0

for pair in zip(velocidades, distancias):
  if pair[0] < velocidad_promedio:
    velocidades_bajo_promedio += 1
    if pair[1] > distancia_promedio:
      velocidades_bajo_y_distiancias_sobre_promedio += 1
  elif pair[0] > velocidad_promedio:
    velocidades_sobre_promedio += 1
    if pair[1] < distancia_promedio:
      velocidades_sobre_y_distancias_bajo_promedio += 1

print(velocidades_bajo_promedio)
print(velocidades_bajo_y_distiancias_sobre_promedio)
print(velocidades_sobre_promedio)
print(velocidades_sobre_y_distancias_bajo_promedio)
