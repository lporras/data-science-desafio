import sys
import random

width = int(sys.argv[1])

if width < 10:
    width = 10

output = "@" * width + "\n"

for i in range(1, 10):
    start_random = int(0.8 * width)
    rand_number = random.randint(start_random, width)
    output += "@" * rand_number + "\n"

for j in range(1, i):
    rand_number_2 = random.randint(j, width)
    output += " " * rand_number_2 + "/\n"

print(output)