import sys

n = int(sys.argv[1])

contain = ""

for i in range(n):
  contain += "*"

print(contain)

contain_middle = "*"

for i in range(n - 2):
  contain_middle += " "

contain_middle += "*\n"

print((contain_middle * (n - 2))[:-1])
print(contain)