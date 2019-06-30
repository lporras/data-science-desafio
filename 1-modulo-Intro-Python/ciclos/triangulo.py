n = 5
contain = ""
for i in range(1, n + 1):
    contain += "*" * i + "\n"

print(contain[:-1])

n = 5
contain = ""

#for i in range(n):
#    for j in range(n - i):
#        contain += "*"
#    contain += "\n"
for i in range(n):
    contain += "*" * (n - i) + "\n"
print(contain)