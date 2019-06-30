#Crear  un  programa llamado solo_pares.py,
# que muestre  todos los  números  pares  hasta "n"(incluyendo "n", si éste es par),
# donde "n" es un valor ingresado por el usuario

n = int(input("Ingrese un número\n"))
for i in range(n + 1):
    if i % 2 == 0:
        print(i)