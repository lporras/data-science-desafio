def letra_o(n):
  contain = ""

  for i in range(n):
    contain += "*"

  contain += "\n"

  contain_middle = "*"

  for i in range(n - 2):
    contain_middle += " "

  contain_middle += "*\n"

  contain += (contain_middle * (n - 2))[:-1] + "\n"

  for i in range(n):
    contain += "*"

  return contain

#print(letra_o(5))
#print(letra_o(4))
#print(letra_o(10))