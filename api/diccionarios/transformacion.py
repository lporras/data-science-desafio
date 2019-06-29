ventas_mensuales = {
    "Octubre": 65000,
    "Noviembre": 68000,
    "Diciembre": 72000
}

for mes, venta in ventas_mensuales.items():
    ventas_mensuales[mes] = venta * 1.1

print(ventas_mensuales)

ventas_mensuales = {
    "Octubre": 65000,
    "Noviembre": 68000,
    "Diciembre": 72000
}

nuevas_ventas_mensuales = {}

for mes, venta in ventas_mensuales.items():
    nuevas_ventas_mensuales[mes] = venta * 0.8

print(ventas_mensuales)
print(nuevas_ventas_mensuales)