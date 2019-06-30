from itertools import groupby

[(k, list(g)) for k, g in groupby('AAABBBCCD')]
'''
Out[14]:
[('A', ['A', 'A', 'A']),
 ('B', ['B', 'B', 'B']),
 ('C', ['C', 'C']),
 ('D', ['D'])]
'''

{k: len(list(g)) for k, g in groupby('AAAABBCCD') }
#Out[13]: {'A': 4, 'B': 2, 'C': 2, 'D': 1}

words = ["hola", "a", "todos", "y", "cada", "uno"]

{k: list(v) for k, v in groupby(words, key=len) }
# Out[16]: {4: ['cada'], 1: ['y'], 5: ['todos'], 3: ['uno']}
words.sort(key=lambda x: len(x))
{k: list(v) for k, v in groupby(words, key=len) }
# Out[19]: {1: ['a', 'y'], 3: ['uno'], 4: ['hola', 'cada'], 5: ['todos']}