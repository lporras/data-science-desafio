def multiplicar():
    print(2 * 2)

multiplicar()

def multiplicar_dos_numeros(x, y):
    print(x * y)

multiplicar_dos_numeros(5, 2)

a = int(input("Ingrese un numero:\n"))
b = int(input("Ingrese un numero:\n"))

multiplicar_dos_numeros(a, b)

def multiplicar_opcional(x, y = 1):
    print(x * y)

multiplicar_opcional(10, 8)
multiplicar_opcional(10)