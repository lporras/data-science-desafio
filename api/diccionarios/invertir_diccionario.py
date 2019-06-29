diccionario_productos = {140000: "celular", 489990: "notebook", 120000: "tablet", 12400: "cargador"}

diccionario_inv = {}

for key, value in diccionario_productos.items():
    diccionario_inv[value] = key

print(diccionario_inv)
# {'celular': 140000, 'notebook': 489990, 'tablet': 120000, 'cargador': 12400}

diccionario_inv_2 = {v:k for k, v in diccionario_productos.items()}