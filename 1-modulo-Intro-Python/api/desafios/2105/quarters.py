from functools import reduce

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

'''
quarter_months = {
  "Q1": ["Enero", "Febrero", "Marzo"],
  "Q2": ["Abril", "Mayo", "Junio"],
  "Q3": ["Julio", "Agosto", "Septiembre"],
  "Q4": ["Octubre", "Noviembre", "Diciembre"]
}

quarters = {}

for quarter, months in quarter_months.items():
  total_months = 0
  for month in months:
    total_months += ventas[month]
  quarters[quarter] = total_months
'''

quarters = {
  "Q1": sum([ventas["Enero"], ventas["Febrero"], ventas["Marzo"]]),
  "Q2": sum([ventas["Abril"], ventas["Mayo"], ventas["Junio"]]),
  "Q3": sum([ventas["Julio"], ventas["Agosto"], ventas["Septiembre"]]),
  "Q4": sum([ventas["Octubre"], ventas["Noviembre"], ventas["Diciembre"]])
}
