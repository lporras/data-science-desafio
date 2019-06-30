#Crear una variante del programa anterior llamado solo_pares_refactor.py.
# En este caso, el cero nodebe ser considerado (el cero no es par)

n = int(input("Ingrese un número\n"))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)

