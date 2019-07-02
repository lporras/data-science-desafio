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

def agrupados(ventas):
  dic_agrupados = {}
  for key, value in ventas.items():
    if value in dic_agrupados:
      dic_agrupados[value] = dic_agrupados[value] + 1
    else:
      dic_agrupados[value] = 0
  return dic_agrupados

print(agrupados(ventas))