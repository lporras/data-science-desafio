from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7]

map_numeros = map(lambda i: i * 2, numeros)

print(list(map_numeros))

return_even_filter = filter(lambda x: x % 2 == 0, numeros)

print(list(return_even_filter))

print(reduce(lambda x, y: x + y, numeros))