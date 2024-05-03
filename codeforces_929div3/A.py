t = int(input())

for i in range(t):
    n = int(input())
    print(sum([abs(int(i)) for i in input().split()]))