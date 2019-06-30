opcion = ""

while opcion != "salir":
    print("Ingrese una opción")
    print("1: Sumar 2 + 2")
    print("2: Multiplicar 2 * 2")
    print("salir: Salida")

    opcion = input()

    if opcion == "1":
        print(2 + 2)
    elif opcion == "2":
        print(2 * 2)
    elif opcion == "salir":
        print("Saliendo")