diccionario_productos = {
    "celular": 140000,
    "notebook": 489990,
    "tablet": 120000,
    "cargador": 12400
}

productos_caros = {}

for clave, valor in diccionario_productos.items():
    if valor > 120000:
        diccionario_productos[clave] = int(valor * 0.9)
    else:
        productos_caros[clave] = valor