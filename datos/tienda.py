
articulos = [
  "celular", "LG K10", "90000",
  "tablet", "Galaxy TAB", "80000",
  "smart tv", "LED 43 Samsung", "485000",
  "celular", "Galaxy J7", "120000",
  "celular", "Huawei Y5", "59900",
  "notebook", "Lenovo ideapad", "250000",
  "tablet", "Huawei media", "139000",
  "notebook", "Acer", "145000"
]

celulares = []
tablets = []
smart_tv = []
notebooks = []

for index, elemento in enumerate(articulos):
  if index == 0 or index % 3 == 0:
    # Es categoria
    aux = elemento
  elif (index - 1) % 3 == 0:
    # es nombre
    pass
  elif (index - 2) % 3 == 0:
    #es precio
    int_precio = int(elemento)
    precio_final = int_precio

    if precio_final > 80000 and aux is not "notebook":
      precio_final = int(precio_final * 0.9)
    if aux == "celular":
      celulares.append(precio_final)
    elif aux == "tablet":
      tablets.append(precio_final)
    elif aux == "smart tv":
      smart_tv.append(precio_final)
    elif aux == "notebook":
      notebooks.append(precio_final)

celulares.sort()
celulares.reverse()

tablets.sort()
tablets.reverse()

smart_tv.sort()
smart_tv.reverse()

notebooks.sort()
notebooks.reverse()

print("Celulares:", celulares)
print("Tablets:", tablets)
print("Smart TV:", smart_tv)
print("Notebooks:", notebooks)
