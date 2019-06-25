colores_1 = ["rojo", "naranjo", "amarillo"]
colores_2 = ["azul", "celeste"]
colores_todos = colores_1 + colores_2
print(colores_todos)

len(colores_todos) == len(colores_1) + len(colores_2)

print(colores_1 * 3)

colores_1.reverse()
# Retorna None

print(colores_1)

"verde" in colores_1

"rojo" in colores_1

print(colores_1.count("verder"))
print(colores_1.count("rojo"))


nombres = ["Ariel", "Juan", "Patricia", "Fernanda", "Sebastian"]

nombres_mayusculas = [i.upper() for i in nombres]

animales = ["Gato", "Perro", "Erizo"]

animales_mod = [i.upper() if i == "Gato" else i.lower() for i in animales]

animales.remove("Gato")

erizo = animales.pop()

animales.insert(0, "Pájaro")
animales.insert(0, "Gato")

for i in animales:
    print(i)

contador = 0

for i in animales:
    print(animales[contador])
    contador += 1

for index, element in enumerate(animales):
    print("indice: ", index, ", elemento: ", element)

