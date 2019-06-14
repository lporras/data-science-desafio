# Debe crear un programa que logre replicar el siguiente patrón,
# donde el usuario ingrese un número, y ese número  corresponderá
# al  número  de  filas  que se  debe generar.
# La  solución debe estar dentro  del programa llamado genera_patron.py
#1
#12
#123
#1234
#12345

n = int(input("Ingrese un número\n"))

for i in range(n):
    contain = ""
    for j in range(i + 1):
        contain += f"{(j + 1)}"
    print(contain)