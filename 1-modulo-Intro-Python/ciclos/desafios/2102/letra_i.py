def letra_i(n):
  contain = ""

  for i in range(n):
    contain += "*"

  contain_middle = ""
  for i in range(n):
    if i == n//2:
      contain_middle += "*"
    else:
      contain_middle += " "

  contain += "\n" + (contain_middle + "\n") * (n - 2)

  for i in range(n):
    contain += "*"

  return contain

#print(letra_i(5))
#print(letra_i(7))
#print(letra_i(11))