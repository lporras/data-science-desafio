import sys

sell_price = float(sys.argv[1])
users = int(sys.argv[2])
expenses = float(sys.argv[3])
last_year_utilities = 1000

if len(sys.argv) == 5:
    last_year_utilities = float(sys.argv[4])

utilities = sell_price * users - expenses
taxes = 0

if(utilities > 0):
    taxes = utilities * 0.35

utilities = utilities - taxes + last_year_utilities

print("Las utilidades son {} dolares".format(utilities))