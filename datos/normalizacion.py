import math

def modulo(lista):
  suma = 0

  for i in lista:
    suma += i ** 2

  return math.sqrt(suma)

def normalizar(lista):
  m = modulo(lista)
  normalized = []

  for i in lista:
    normalized.append(i / m)

  return normalized

output = normalizar([1, 2, 3])

print(output)

suma = 0

for i in output:
  suma += i ** 2

print(suma)

