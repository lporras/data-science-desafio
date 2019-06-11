import sys

sell_price = float(sys.argv[1])
total_users = int(sys.argv[2])
premium_users = int(sys.argv[3])
free_users = int(sys.argv[4])
expenses = float(sys.argv[5])

utilities = sell_price * (2 * premium_users + (total_users - premium_users - free_users)) - expenses
taxes = 0

if(utilities > 0):
    taxes = utilities * 0.35

utilities = utilities - taxes

print("Las utilidades son {} dolares".format(utilities))

# Ver la versión online: https://repl.it/@lporras/emprendedor2py
