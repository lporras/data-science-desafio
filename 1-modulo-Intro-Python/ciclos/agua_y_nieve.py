import sys
import random

width = int(sys.argv[1])

if width < 10:
    width = 10

output = ""

for i in range(1, 10):
    rand_number = random.randint(i, width)
    output += " " * rand_number + "*\n"

    for j in range(1, i):
        rand_number_2 = random.randint(j, width)
        output += " " * rand_number_2 + "/\n"

print(output)