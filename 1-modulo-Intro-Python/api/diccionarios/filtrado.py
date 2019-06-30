ventas_mensuales = {
    "Octubre": 65000,
    "Noviembre": 68000,
    "Diciembre": 72000
}

def filtrar_valores_altos(diccionario):
    diccionario_filtrado = {}
    for clave, valor in diccionario.items():
        if valor > 70000:
            diccionario_filtrado[clave] = valor
    return diccionario_filtrado

print(filtrar_valores_altos(ventas_mensuales))