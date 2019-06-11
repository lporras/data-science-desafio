# promedio_usuario.py : El usuario debe ingresar un número, el cual indica al programa la cantidad de
# datos que se van a ingresar. Luego, debe ingresar la cantidad de datos indicada. El programa debe
# mostrar el promedio de los datos ingresados a continuación del primer argumento.
from functools import reduce

number = int(input("Ingresar la cantidad de números a pedir: "))
i = 0
numbers = []
while i < number:
    i += 1
    numbers.append(int(input("Ingrese un número: ")))

average = reduce((lambda x, y: x + y), numbers) / number

print(f"el promedio de los {number} ingresados es: {average}")