import sys

ventas = {
  "Enero": 15000,
  "Febrero": 22000,
  "Marzo": 12000,
  "Abril": 17000,
  "Mayo": 81000,
  "Junio": 13000,
  "Julio": 21000,
  "Agosto": 41200,
  "Septiembre": 25000,
  "Octubre": 21500,
  "Noviembre": 91000,
  "Diciembre": 21000
}

ventas_inv = {v:k for k, v in ventas.items()}

values = sys.argv[1:]

for value in values:
  int_value = int(value)
  if int_value in ventas_inv:
    print(ventas_inv[int_value])
  else:
    print("no encontrado")
