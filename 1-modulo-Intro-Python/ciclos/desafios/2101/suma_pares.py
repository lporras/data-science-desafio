#Crear un programa llamado suma_pares.py que sume todos los números pares hasta "n"
# (incluyendo "n"si éste es par), donde "n" es ingresado por el usuario.
# Tip: El cero no es par; no afecta en la suma, pero se debe tener cuidado con los bordes del ciclo.

n = int(input("Ingrese un número\n"))
sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum += i
print(sum)