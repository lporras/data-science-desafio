# promedio.py : El usuario debe ingresar número. El programa debe sumar todos los números desde 1
# hasta el número ingresado. Luego, debe mostrar el resultado de la suma divido por la cantidad de
# iteraciones.

number = int(input("Ingresar un numero: "))
i = 0
sum = 0

while i < number:
    i += 1
    sum += i



print(f"el promedio es: {sum/i}")

# Ver online en: https://repl.it/@lporras/promediopy
