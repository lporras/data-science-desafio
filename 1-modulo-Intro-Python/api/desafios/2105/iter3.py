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

def filter(dictionary, value):
  return {k:v for k, v in dictionary.items() if v > value}

#print(filter(ventas, 10000))