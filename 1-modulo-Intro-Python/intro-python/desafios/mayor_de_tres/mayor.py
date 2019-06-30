import sys

first = int(sys.argv[1])
second = int(sys.argv[2])
third = int(sys.argv[3])

if first > second and first > third:
    print(first)
elif second > first and second > third:
    print(second)
else:
    print(third)