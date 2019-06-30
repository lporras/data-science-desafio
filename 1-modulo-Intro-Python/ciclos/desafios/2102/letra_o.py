def letra_o(n):
  base = "*" * n
  middle = "*" + " " * (n - 2) + "*"
  result = base + "\n" + (middle + "\n")*(n-2) + base
  return result

#print(letra_o(5))
#print(letra_o(4))
#print(letra_o(10))