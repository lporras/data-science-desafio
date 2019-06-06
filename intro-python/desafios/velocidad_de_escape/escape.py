import sys
import math

gravity = float(sys.argv[1])
radio = float(sys.argv[2])

velocity = math.sqrt(2 * gravity * radio * 1000)
velocity = format(velocity, '.2f')

print("La velocidad de escape es {} m/s".format(velocity))