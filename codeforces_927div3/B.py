import math

t = int(input())

for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    year = 0
    for zn in a:
        if zn > year:
            year = zn
        else:
            year = (year // zn + 1) * zn
    print(year)
