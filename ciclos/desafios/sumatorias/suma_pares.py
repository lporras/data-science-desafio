# suma_pares.py : El programa debe sumar solo los números pares entre 1 y 100, y mostrar ese
# resultado. tip: Utilize % (módulo).

number = 100
i = 0
sum = 0

while i < number:
    i += 1
    if(i % 2 == 0):
        sum += i

print(f"La suma de los números pares entre 1 y 100 es: {sum}")

# Ver online en: https://repl.it/@lporras/sumaparespy
