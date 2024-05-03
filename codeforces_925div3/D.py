t = int(input())

for i in range(t):
    n, x, y = map(int, input().split())
    a = [int(i) for i in input().split()]
    b = [i % y for i in a]
