def letra_x(n):
  contain = ""
  for i in range(n):
    array = list(" " * n)
    array[i] = "*"
    array[n - 1 - i] = "*"
    contain += "".join(array) + "\n"
  return contain

#print(letra_x(3))
#print(letra_x(4))
#print(letra_x(5))
#print(letra_x(11))