import sys

saldo = 0

if len(sys.argv) == 2:
  saldo = int(sys.argv[1])

def depositar(saldo, cantidad):
  return saldo + cantidad

def girar(saldo, cantidad):
  if cantidad <= saldo:
    return saldo - cantidad
  else:
    return False

def mostrar_menu(saldo):
  while True:
    print("Bienvenido al portal del Banco Amigo. Escoja una opción:")
    print("1. Consultar saldo")
    print("2. Hacer depósito")
    print("3. Realizar giro")
    print("4. Salir")
    option = int(input("\n"))
    if option == 1:
      print(f"\nSu saldo es de {saldo}\n")
    elif option == 2:
      cantidad = int(input("\nDigite la cantidad a depositar: "))
      saldo = depositar(saldo, cantidad)
      print(f"\nSu nuevo saldo es de {saldo}\n")
    elif  option == 3:
      if saldo <= 0:
        print("\nNo puede realizar giros. Su saldo es 0\n")
      else:
        while True:
          cantidad = int(input("\nDigite la cantidad a girar: "))
          nuevo_saldo = girar(saldo, cantidad)
          if bool(nuevo_saldo):
            saldo = nuevo_saldo
            print(f"\nSu nuevo saldo es de {saldo}\n")
            break
          else:
            print(f"\nNo se puede girar esta cantidad. Su saldo es de {saldo}\n")
    elif option == 4:
      print("\nGracias por preferir siempre al Banco Amigo")
      break
    else:
      print("\nOpción inválida. Por favor ingrese 1, 2, 3 ó 4.")

mostrar_menu(saldo)

