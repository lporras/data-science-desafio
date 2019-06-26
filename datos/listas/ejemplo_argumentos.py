import sys
recibidos = sys.argv
cantidad = len(recibidos)

int_args = []

for i in range(1, cantidad):
    int_args.append(int(recibidos[i]))

print(int_args)

