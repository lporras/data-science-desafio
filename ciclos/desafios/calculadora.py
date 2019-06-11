# calculadora.py : Crear un programa que permita ingresar de 4 opciones, identificadas con un
# número (1: sumar, 2: restar, 3: multiplicar, 4: dividir). Luego el usuario debe ingresar 2 números, sobre
# los cuales se realice la operación escogida. El programa debe mostrar el resultado.

option = None
options = ['1', '2', '3', '4']

while option not in options:
    print("Eliga una opción: \n")
    print("\t1: sumar\n")
    print("\t2: restar\n")
    print("\t3: multiplicar\n")
    print("\t4: dividir\n")
    option = input("Ingrese la opción elegida: ")

number_1 = int(input("Ingrese el primero número: "))
number_2 = int(input("Ingrese el segundo número: "))
result = 0

if option == '1':
    result = number_1 + number_2
elif option == '2':
    result = number_1 - number_2
elif option == '3':
    result = number_1 * number_2
elif option == '4':
    try:
        result = number_1 / number_2
    except ZeroDivisionError:
        result = None
        print("No es posible dividir por 0")

if result != None:
    print(f"El resultado es {result}")