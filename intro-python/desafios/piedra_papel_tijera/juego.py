import sys
import random

user_move = sys.argv[1]
rand_number = random.randint(1, 3)
moves = {
    1: 'piedra',
    2: 'papel',
    3: 'tijera'
}
pc_move = moves[rand_number]

if user_move not in moves.values():
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
else:
    print(f"Computador juega {pc_move}")

    if user_move == 'piedra' and pc_move == 'tijera':
        print("Ganaste")
    elif user_move == 'tijera' and pc_move == 'papel':
        print("Ganaste")
    elif user_move == 'papel' and pc_move == 'piedra':
        print("Ganaste")
    elif user_move == pc_move:
        print("Empataste")
    else:
        print("Perdiste")

