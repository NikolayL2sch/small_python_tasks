t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    for j in range(2, 500000001):
        if a % j == 0 or b % j == 0:
            print(max(a, b) * j)
            break
