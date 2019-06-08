import sys

sell_price = float(sys.argv[1])
users = int(sys.argv[2])
expenses = float(sys.argv[3])

utilities = sell_price * users - expenses
taxes = 0

if(utilities > 0):
    taxes = utilities * 0.35

utilities = utilities - taxes

print("Las utilidades son {} dolares".format(utilities))