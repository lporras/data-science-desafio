# remplazar for por un while
#cuenta_regresiva = int(input("Ingrese un número para comenzar la cuenta\n"))

#for i in range(cuenta_regresiva):
#    tmp = cuenta_regresiva
#    print("Iteración {}".format(tmp - i))

cuenta_regresiva = int(input("Ingrese un número para comenzar la cuenta\n"))
i = 0
while i < cuenta_regresiva:
    tmp = cuenta_regresiva
    print("Iteración {}".format(tmp - i))
    i += 1