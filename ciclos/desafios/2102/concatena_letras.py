import string

def gen(n):
  letters = ""
  i = 0

  while i < n:
    letters += string.ascii_lowercase[i]
    i += 1
  return letters

#print(gen(4))
#print(gen(10))